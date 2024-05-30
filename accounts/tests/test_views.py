
from django.test import TestCase
from django.urls import reverse


class LoginViewTestCase(TestCase):
    def test_login_view(self):
        response = self.client.get(reverse('accounts:login'))
        self.assertEqual(response.status_code, 200)


