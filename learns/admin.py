from django.contrib import admin

from learns.models import Lesson, Course, Subscription


@admin.register(Lesson)
class AdminLesson(admin.ModelAdmin):
    list_display = ("id", 'title', 'owner__email', 'owner__id')


@admin.register(Course)
class AdminCourse(admin.ModelAdmin):
    list_display = ("id", 'title', 'owner__email', 'owner__id')


@admin.register(Subscription)
class SubscriptionCourse(admin.ModelAdmin):
    list_display = ("id", 'course__title')
