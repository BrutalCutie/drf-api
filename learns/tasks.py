import datetime

from celery import shared_task
from django.core.mail import send_mail

from users.models import User
from .models import Course
from config.settings import EMAIL_HOST_USER


@shared_task
def send_notification(course_pk):

    course = Course.objects.filter(pk=course_pk).first()

    if not course:
        return None

    subs = course.subscriptions.all()

    users_to_notify = [x.user for x in subs]

    if not users_to_notify:
        return None

    subject = 'Здравствуй, {first_name} {last_name}!'
    text = f'Курс {course.title} был обновлён.\n\nЭто сообщение пришло потому, что вы подписаны на обновление курса.'

    for user in users_to_notify:
        send_mail(
            subject=subject.format(
                first_name=user.first_name,
                last_name=user.last_name,
            ),
            message=text,
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email,]
        )


@shared_task
def get_sleepy_guy():
    all_users = User.objects.exclude(username='admin')
    now = datetime.datetime.now()

    report_list = []

    for user in all_users:
        last_login = user.last_login
        if not last_login:  # Если None - Вероятно пользователь ещё не верифицировался, а значит и так не активен
            continue

        if last_login + datetime.timedelta(days=30) > now:
            user.is_active = False
            user.save()

            report_list.append(user.email)

    print(f"=== {now.day}.{now.month}.{now.year}: Отчёт проверки на приостановку активности пользователей ===")
    print(f"Остановленных пользователей: {len(report_list)}")
    if len(report_list) > 0:
        print(f"Данные: {', '.join(report_list)}")




