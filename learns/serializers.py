from rest_framework import serializers

from learns.models import Course, Lesson, Subscription
from learns.validators import LessonValidator


class SubscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscription
        fields = "__all__"


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = "__all__"
        validators = [
            LessonValidator(field='video_link'),
        ]


class CourseSerializer(serializers.ModelSerializer):
    total_lessons = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True)
    is_subscribed = serializers.SerializerMethodField()
    subscribers = SubscriptionSerializer(many=True, read_only=True, source='subscriptions')

    class Meta:
        model = Course
        fields = "__all__"

    def get_total_lessons(self, instance):
        return instance.lessons.all().count()

    def get_is_subscribed(self, instance):
        user_id = self.context["request"].user
        sub_info = instance.subscriptions.filter(user=user_id)

        return sub_info.exists()
