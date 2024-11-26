from rest_framework.routers import DefaultRouter

from learns.apps import LearnsConfig
from learns.views import CourseViewSet, LessonViewSet

app_name = LearnsConfig.name

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='course')
router.register(r'lessons', LessonViewSet, basename='lesson')


urlpatterns = [

    # path('lesson/list/', views.LessonListApiView.as_view(), name='lesson-list'),
    # path('lesson/create/', views.LessonCreateApiView.as_view(), name='lesson-create'),
    # path('lesson/detail/<int:pk>/', views.LessonRetrieveApiView.as_view(), name='lesson-detail'),
    # path('lesson/update/<int:pk>/', views.LessonUpdateApiView.as_view(), name='lesson-update'),
    # path('lesson/delete/<int:pk>/', views.LessonDeleteApiView.as_view(), name='lesson-delete'),

] + router.urls
