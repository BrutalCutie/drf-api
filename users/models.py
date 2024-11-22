from django.contrib.auth.models import AbstractUser
from django.db import models
from learns.models import Lesson, Course


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


class Payment(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ("CASH", "Наличные"),
        ("ACCOUNT", "Перевод на счёт"),
    ]

    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='payments',
                             verbose_name="пользователь")
    payment_date = models.DateField(verbose_name='дата платежа',
                                    auto_now_add=True)
    course = models.ForeignKey(Course,
                               on_delete=models.CASCADE,
                               related_name='payment_courses')
    lesson = models.ForeignKey(Lesson,
                               on_delete=models.CASCADE,
                               related_name='payment_lessons')
    payment_sum = models.PositiveIntegerField(verbose_name="Сумма оплаты")
    payment_method = models.CharField(choices=PAYMENT_METHOD_CHOICES)

    def __str__(self):
        return f"pk: {self.pk} | user pk: {self.user.pk}"

    class Meta:
        verbose_name = "платёж"
        verbose_name_plural = "платежи"
