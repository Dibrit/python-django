from django.test import TestCase
from reg.models import User
import datetime


class UserModelTestcase(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create(pasword="qwerty1234", email="John@gmail.com", username="111b2", is_superuser=False, is_active=True, is_staff=True, created_at=datetime.date.today(), updated_at=datetime.date.today())

    def test_string_method(self):
        student = User.objects.get(id=1)
        expected_string = f"Name: {student.username}"
        self.assertEqual(str(student), expected_string)

    def test_get_absolute_url(self):
        student = User.objects.get(id=1)
        self.assertEqual(student.get_absolute_url(), "/reg/1")