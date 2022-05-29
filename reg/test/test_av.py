# from django.test import TestCase
# from reg.models import User
#
# class StudentSerializerTestCase(APITestCase):
#     def student_creation_test(self):
#         payload = {
#             pasword="qwerty1234",
#             email="John@gmail.com",
#             username="111b2",
#             is_superuser=False,
#             is_active=True,
#             is_staff=True, created_at=datetime.date.today(),
#             updated_at=datetime.date.today())
#         }
#         response = self.client.post(reverse("student-create"), payload)
#         self.assertEqual(status.HTTP_201_CREATED, response.status_code)