from django.urls import path
from rest_framework.routers import DefaultRouter

from learns.apps import LearnsConfig
from learns import views

app_name = LearnsConfig.name

router = DefaultRouter()
router.register(r"courses", views.CourseViewSet, basename="course")
router.register(r"lessons", views.LessonViewSet, basename="lesson")

urlpatterns = [
    path("subs/list/", views.SubscriptionListApiView.as_view(), name="subs_list"),
    path("subs/create/", views.SubscriptionCreateApiView.as_view(), name="subs_create"),
    path(
        "subs/retrieve/<int:pk>/",
        views.SubscriptionRetrieveApiView.as_view(),
        name="subs_retrieve",
    ),
    path(
        "subs/update/<int:pk>/",
        views.SubscriptionUpdateApiView.as_view(),
        name="subs_update",
    ),
    path(
        "subs/delete/<int:pk>/",
        views.SubscriptionDestroyApiView.as_view(),
        name="subs_delete",
    ),
] + router.urls
