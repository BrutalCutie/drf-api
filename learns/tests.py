from rest_framework import status
from rest_framework.test import APITestCase

from learns.models import Course, Lesson, Subscription
from users.models import User


class CourseTestCase(APITestCase):
    user = None

    def setUp(self):
        self.user = User.objects.create(
            password="test_user",
            username="test_user",
            email="test_user@mail.ru",
            phone="12345",
            city="TestCity",
        )
        self.client.force_authenticate(user=self.user)

    def test_create_course(self):

        data = {
            "title": "TestCourse",
        }

        response = self.client.post(
            path="/courses/",
            data=data,
        )

        self.assertTrue(Course.objects.all().exists())

        self.assertEqual(
            response.json(),
            {
                "id": 1,
                "total_lessons": 0,
                "lessons": [],
                "is_subscribed": False,
                "subscribers": [],
                "title": "TestCourse",
                "preview": None,
                "description": None,
                "owner": self.user.id,
            },
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_course(self):
        data_list = [
            {
                "title": "TestCourse",
            },
            {
                "title": "TestCourse2",
            },
            {
                "title": "TestCourse3",
            },
        ]

        for data in data_list:
            self.client.post(
                path="/courses/",
                data=data,
            )

        self.assertEqual(Course.objects.all().count(), 3)


class LessonTestCase(APITestCase):
    course = None
    user = None

    def setUp(self):
        self.course = Course.objects.create(title="ForTestCourse")

        self.user = User.objects.create(
            password="test_user",
            username="test_user",
            email="test_user@mail.ru",
            phone="12345",
            city="TestCity",
        )
        self.client.force_authenticate(user=self.user)

    def test_create_lesson(self):

        data = {
            "title": "TestLesson",
            "video_link": "www.youtube.com/asdaw3125dsfas21",
            "course": self.course.pk,
        }

        response = self.client.post(
            path="/lessons/",
            data=data,
        )

        self.assertTrue(Course.objects.all().exists())

        self.assertEqual(
            response.json(),
            {
                "id": 1,
                "title": "TestLesson",
                "description": None,
                "preview": None,
                "video_link": "www.youtube.com/asdaw3125dsfas21",
                "course": self.course.id,
                "owner": self.user.id,
            },
        )

    def test_list_lesson(self):

        data_list = [
            {
                "title": "TestLesson1",
                "video_link": "www.youtube.com/asdaw3125dsfas213123",
                "course": self.course.pk,
            },
            {
                "title": "TestLesson2",
                "video_link": "www.youtube.com/asdaw3125dsfas211231",
                "course": self.course.pk,
            },
            {
                "title": "TestLesson3",
                "video_link": "www.youtube.com/asdaw3125dsfas213123",
                "course": self.course.pk,
            },
        ]

        for data in data_list:
            self.client.post(
                path="/lessons/",
                data=data,
            )

        self.assertEqual(Lesson.objects.all().count(), 3)

    def test_destroy_lesson(self):
        data = {
            "title": "TestLesson",
            "video_link": "www.youtube.com/asdaw3125dsfas21",
            "course": self.course.pk,
        }

        response = self.client.post(path="/lessons/", data=data)

        delete_response = self.client.delete(path=f"/lessons/{response.json().get("id")}/")

        self.assertFalse(Lesson.objects.all().exists())

        self.assertTrue(delete_response.status_code, status.HTTP_204_NO_CONTENT)

    def test_update_lesson(self):
        data = {
            "title": "TestLesson",
            "video_link": "www.youtube.com/asdaw3125dsfas21",
            "course": self.course.pk,
        }

        response = self.client.post(path="/lessons/", data=data)

        update_response = self.client.patch(
            path=f"/lessons/{response.json().get("id")}/",
            data={
                "title": "UpdatedTestLesson",
                "video_link": "www.youtube.com/asdaw3125dsfas21",
            },
        )

        self.assertTrue(Lesson.objects.get(title="UpdatedTestLesson"))

        self.assertEqual(update_response.status_code, status.HTTP_200_OK)

    def test_retrieve_lesson(self):
        data = {
            "title": "TestLesson",
            "video_link": "www.youtube.com/asdaw3125dsfas21",
            "course": self.course.pk,
        }

        response = self.client.post(path="/lessons/", data=data)
        lesson_id = response.json().get("id")

        get_query = self.client.get(path=f"/lessons/{lesson_id}/")

        self.assertEqual(get_query.json(), response.json())


class SubscriptionTestCase(APITestCase):
    course = None
    user = None

    def setUp(self):
        self.course = Course.objects.create(title="ForTestCourse")

        self.user = User.objects.create(
            password="test_user",
            username="test_user",
            email="test_user@mail.ru",
            phone="12345",
            city="TestCity",
        )
        self.client.force_authenticate(user=self.user)

    def test_sub_swich(self):
        data = {"course": self.course.id, "user": self.user.id}

        self.client.post(path="/subs/create/", data=data)

        self.assertTrue(Subscription.objects.filter(course__pk=self.course.pk).exists())

        self.client.post(path="/subs/create/", data=data)

        self.assertFalse(Subscription.objects.filter(course__pk=self.course.pk).exists())
