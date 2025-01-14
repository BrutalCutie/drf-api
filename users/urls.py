from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import UserViewSet, PaymentViewSet

app_name = UsersConfig.name

router = DefaultRouter()
router.register("users", UserViewSet, basename="users")
router.register("payments", PaymentViewSet, basename="payments")

urlpatterns = [
    path("users/token/", TokenObtainPairView.as_view(), name="token-obtain-pair"),
    path("users/token/refresh/", TokenRefreshView.as_view(), name="token-obtain-refresh"),
] + router.urls
