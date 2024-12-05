from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import User, Payment
from .serializers import UserSerializer, PaymentSerializer, UserDetailSerializer
from .services import create_session, create_product, create_stripe_price


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('username', 'first_name', "email")
    ordering_fields = ('last_login', 'email', 'username', 'first_name', "city")
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [AllowAny]

        return super().get_permissions()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return UserDetailSerializer
        return UserSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(user.password)
        user.save()


class PaymentViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering_fields = ("payment_date",)
    filterset_fields = ("payment_method", "course", "lesson",)
    permission_classes = [IsAuthenticated]


    def perform_create(self, serializer):
        payment = serializer.save(user=self.request.user)
        creation_item = create_product(payment.lesson or payment.course)
        amount = create_stripe_price(payment.payment_sum, creation_item)

        session_id, payment_link = create_session(amount)
        payment.payment_link = payment_link
        payment.session_id = session_id

        payment.save()

