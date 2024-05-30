from django.test import TestCase
from accounts.models import CustomUser


class CustomUserTestCase(TestCase):
    def setUp(self):
        CustomUser.objects.create(name="Admin",surname="admin", email="admin@admin.com",password="password", is_active=True)

    def test_model_creation(self):
        obj = CustomUser.objects.get(name="Admin")
        self.assertEqual(obj.name, "Admin")
        self.assertEqual(obj.email, "admin@admin.com")
