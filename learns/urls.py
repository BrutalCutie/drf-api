from rest_framework.routers import DefaultRouter

from learns.apps import LearnsConfig
from learns.views import CourseViewSet, LessonViewSet

app_name = LearnsConfig.name

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='course')
router.register(r'lessons', LessonViewSet, basename='lesson')


urlpatterns = [


] + router.urls
