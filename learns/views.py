from rest_framework import viewsets

from learns.models import Course, Lesson
from learns.serializers import CourseSerializer, LessonSerializer


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class LessonViewSet(viewsets.ModelViewSet):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


# class LessonListApiView(generics.ListAPIView):
#     serializer_class = LessonSerializer
#     queryset = Lesson.objects.all()
#
#
# class LessonCreateApiView(generics.CreateAPIView):
#     serializer_class = LessonSerializer
#
#
# class LessonRetrieveApiView(generics.RetrieveAPIView):
#     serializer_class = LessonSerializer
#     queryset = Lesson.objects.all()
#
#
# class LessonUpdateApiView(generics.UpdateAPIView):
#     serializer_class = LessonSerializer
#     queryset = Lesson.objects.all()
#
#
# class LessonDeleteApiView(generics.DestroyAPIView):
#     serializer_class = LessonSerializer
#     queryset = Lesson.objects.all()
