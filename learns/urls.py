from django.urls import path
from rest_framework.routers import DefaultRouter

from learns.apps import LearnsConfig
from learns import views
from learns.views import CourseViewSet

app_name = LearnsConfig.name

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns = [
    path('lesson/list/', views.LessonListApiView.as_view(), name='lesson-list'),
    path('lesson/create/', views.LessonCreateApiView.as_view(), name='lesson-create'),
    path('lesson/detail/<int:pk>/', views.LessonRetrieveApiView.as_view(), name='lesson-detail'),
    path('lesson/update/<int:pk>/', views.LessonUpdateApiView.as_view(), name='lesson-update'),
    path('lesson/delete/<int:pk>/', views.LessonDeleteApiView.as_view(), name='lesson-delete'),

] + router.urls
