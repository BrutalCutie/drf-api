from django.conf import settings
from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=30, verbose_name="название курса", null=False, blank=False)
    preview = models.ImageField(upload_to='course-preview', verbose_name="превью курса", null=True, blank=True)
    description = models.TextField(verbose_name="описание курса", null=True, blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE,
                              related_name='courses',
                              verbose_name='курсы',
                              blank=True,
                              null=True)

    def __str__(self):
        return f"{self.pk} | {self.title}"

    class Meta:
        verbose_name = "курс"
        verbose_name_plural = "курсы"


class Lesson(models.Model):
    title = models.CharField(max_length=30, verbose_name="название урока", null=False, blank=False)
    description = models.TextField(verbose_name="описание урока", null=True, blank=True)
    preview = models.ImageField(upload_to='lesson-preview', verbose_name="превью урока", null=True, blank=True)
    video_link = models.CharField(verbose_name="ссылка на видео")
    course = models.ForeignKey(Course, related_name='lessons', verbose_name='Курс', on_delete=models.CASCADE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE,
                              related_name='lessons',
                              verbose_name='уроки',
                              blank=True,
                              null=True)

    def __str__(self):
        return f"{self.pk} | {self.title}"

    class Meta:
        verbose_name = "урок"
        verbose_name_plural = "уроки"
