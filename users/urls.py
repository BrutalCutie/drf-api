from rest_framework.routers import DefaultRouter

from users.views import UserViewSet, PaymentViewSet

router = DefaultRouter()
router.register('users', UserViewSet, basename='users')
router.register('payments', PaymentViewSet, basename='payments')

urlpatterns = [

] + router.urls
