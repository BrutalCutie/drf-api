from rest_framework import serializers

from learns.models import Course, Lesson


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class LessonsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = "__all__"
