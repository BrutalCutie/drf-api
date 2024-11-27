from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from learns.models import Course, Lesson
from learns.serializers import CourseSerializer, LessonSerializer
from users.permissions import IsModer, IsOwner


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated]

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

        return super().get_permissions()


class LessonViewSet(viewsets.ModelViewSet):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        lesson = serializer.save()
        lesson.owner = self.request.user
        lesson.save()

    def get_permissions(self):
        if self.action in ['retrieve', 'update', 'partial_update']:
            self.permission_classes = [IsOwner | IsModer]

        elif self.action in ['destroy']:
            self.permission_classes = [~IsModer, IsOwner]
        elif self.action in ['create']:
            self.permission_classes = [~IsModer]

        return super().get_permissions()

