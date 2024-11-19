from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(verbose_name="почта", unique=True)
    phone = models.CharField(max_length=15, verbose_name="номер телефона", blank=False, null=False)
    city = models.CharField(max_length=50, verbose_name="город")
    avatar = models.ImageField(upload_to="users-avatars", blank=True, null=True, verbose_name="фото профиля")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["phone_number"]

    def __str__(self):
        return f"{self.pk} | {self.email}"

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"
