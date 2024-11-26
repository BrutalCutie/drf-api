from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.views import UserViewSet, PaymentViewSet

router = DefaultRouter()
router.register('users', UserViewSet, basename='users')
router.register('payments', PaymentViewSet, basename='payments')

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name='token-obtain-pair'),
    path("token/refresh/", TokenRefreshView.as_view(), name='token-obtain-refresh')

] + router.urls
