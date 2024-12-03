from django.urls import path
from rest_framework.routers import DefaultRouter

from learns.apps import LearnsConfig
from learns.views import (CourseViewSet, LessonViewSet,
                          # SubscriptionListAPIView
                          )

app_name = LearnsConfig.name

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='course')
router.register(r'lessons', LessonViewSet, basename='lesson')


urlpatterns = [
    # path('subs/list/', SubscriptionListAPIView.as_view(), name='subs_list')

] + router.urls
