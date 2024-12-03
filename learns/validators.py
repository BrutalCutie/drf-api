import re
from rest_framework.exceptions import ValidationError


class LessonValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        pattern = re.compile(r"yotube\.com")
        value = dict(value).get(self.field)

        if not bool(pattern.match(value)):
            raise ValidationError('Вы можете прикреплять видео только с видеохостинга "Youtube"')


