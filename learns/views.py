from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from learns.models import Course, Lesson, Subscription
from learns.paginators import LessonPagination, CoursePagination
from learns.serializers import CourseSerializer, LessonSerializer, SubscriptionSerializer
from learns.tasks import send_notification
from users.models import User

from users.permissions import IsModer, IsOwner


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = CoursePagination

    def perform_create(self, serializer):
        course = serializer.save()
        course.owner = self.request.user
        course.save()

    def perform_update(self, serializer):
        course = serializer.save()
        course_pk = course.pk

        send_notification.delay(course_pk)

    def get_permissions(self):
        if self.action in ['retrieve', 'update', 'partial_update']:
            self.permission_classes = [IsOwner | IsModer]

        elif self.action in ['destroy']:
            self.permission_classes = [~IsModer, IsOwner]
        elif self.action in ['create']:
            self.permission_classes = [~IsModer]
        elif self.action in ['list']:
            self.permission_classes = [IsModer]

        return super().get_permissions()


class LessonViewSet(viewsets.ModelViewSet):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = LessonPagination

    def perform_create(self, serializer):
        lesson = serializer.save()
        lesson.owner = self.request.user
        lesson.save()

    def get_permissions(self):

        if self.action in ['retrieve', 'update', 'partial_update']:
            self.permission_classes = [IsOwner | IsModer]

        elif self.action in ['destroy']:
            self.permission_classes = [~IsModer | IsOwner]

        elif self.action in ['create']:
            self.permission_classes = [~IsModer]

        elif self.action in ['list']:
            self.permission_classes = [IsModer]

        return super().get_permissions()


class SubscriptionListApiView(generics.ListAPIView):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()
    permission_classes = [IsAuthenticated]


class SubscriptionCreateApiView(generics.CreateAPIView):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user_id = request.data.get('user')
        user = get_object_or_404(User, pk=user_id)
        course_id = request.data.get('course')
        course_item = get_object_or_404(Course, pk=course_id)

        obj = user.subscriptions.filter(course__pk=course_id)

        if obj.exists():
            message = "Подписка отключена"
            obj.delete()

        else:
            message = "Подписка оформлена"
            Subscription.objects.create(user=user, course=course_item)

        return Response({"message": message})


class SubscriptionRetrieveApiView(generics.RetrieveAPIView):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()
    permission_classes = [IsAuthenticated]


class SubscriptionUpdateApiView(generics.UpdateAPIView):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()
    permission_classes = [IsAuthenticated]


class SubscriptionDestroyApiView(generics.DestroyAPIView):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()
    permission_classes = [IsAuthenticated]
