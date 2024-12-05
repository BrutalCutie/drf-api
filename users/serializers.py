from rest_framework import serializers

from users.models import User, Payment
from users.validators import PaymentValidator


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
        validators = [
            PaymentValidator(fields=['lesson', 'course']),
        ]



class UserDetailSerializer(serializers.ModelSerializer):
    payments = PaymentSerializer(many=True)

    class Meta:
        model = User
        fields = "__all__"
