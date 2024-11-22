from rest_framework import serializers

from learns.models import Course, Lesson


class CourseSerializer(serializers.ModelSerializer):
    total_lessons = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = "__all__"

    def get_total_lessons(self, instance):
        return instance.lessons.all().count()


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = "__all__"
