from django.contrib import admin

from learns.models import Lesson, Course


@admin.register(Lesson)
class AdminLesson(admin.ModelAdmin):
    list_filter = ("id", 'title')


@admin.register(Course)
class AdminCourse(admin.ModelAdmin):
    list_filter = ("id", 'title')
