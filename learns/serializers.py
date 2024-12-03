from rest_framework import serializers

from learns.models import Course, Lesson
from learns.validators import LessonValidator


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = "__all__"
        validators = [
            LessonValidator(field='video_link'),

        ]


class CourseSerializer(serializers.ModelSerializer):
    total_lessons = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True)

    class Meta:
        model = Course
        fields = "__all__"

    def get_total_lessons(self, instance):
        return instance.lessons.all().count()



