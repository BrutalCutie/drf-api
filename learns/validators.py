import re
from rest_framework.exceptions import ValidationError


class LessonValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        pattern = re.compile(r"youtube\.com")
        tmp = dict(value).get(self.field)

        if not bool(pattern.search(tmp)):
            raise ValidationError('Вы можете прикреплять видео только с видеохостинга "Youtube"')
