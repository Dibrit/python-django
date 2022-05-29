from django.test import TestCase
from reg.models import User
from django.urls import reverse


class StudentListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_user = 1
        for i in range(number_of_user):
            User.objects.create(first_name=f"John{i}", last_name=f"Doe{i}")

    def test_url_exists(self):
        response = self.client.get("/reg")
        self.assertEqual(response.status_code, 200)

    def test_url_accessible_by_name(self):
        response = self.client.get(reverse('user'))
        self.assertEqual(response.status_code, 200)
