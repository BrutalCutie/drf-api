from rest_framework import viewsets
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from learns.models import Course, Lesson
from learns.paginators import LessonPagination, CoursePagination
from learns.serializers import CourseSerializer, LessonSerializer

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


# class SubscriptionListAPIView(generics.ListAPIView):
#     serializer_class = SubscriptionSerializer
#     queryset = Subscription.objects.all()
#     permission_classes = [AllowAny]


# class SubscriptionSwitchAPIView(generics.CreateAPIView):
#     serializer_class = SubscriptionSerializer
#     queryset = Subscription.objects.all()
#     permission_classes = [AllowAny]


