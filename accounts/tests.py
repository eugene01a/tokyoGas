from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from .models import Pref, CustomUser


# API-based registration tests for React frontend integration.
class RegistrationAPITests(TestCase):
    def setUp(self):
        self.pref = Pref.objects.create(name='Tokyo')
        self.api_url = reverse('accounts:api_register')
        self.client = APIClient()

    def test_api_register_valid_data_creates_user(self):
        response = self.client.post(self.api_url, {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'StrongPass1',
            'tel': '09012345678',
            'pref': self.pref.pk,
        }, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertTrue(CustomUser.objects.filter(email='test@example.com').exists())

    def test_api_register_rejects_short_username(self):
        response = self.client.post(self.api_url, {
            'username': 'ab',
            'email': 'test2@example.com',
            'password': 'StrongPass1',
            'tel': '09012345678',
            'pref': self.pref.pk,
        }, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('username', response.data)
        self.assertFalse(CustomUser.objects.filter(email='test2@example.com').exists())

    def test_api_register_rejects_invalid_email(self):
        response = self.client.post(self.api_url, {
            'username': 'testuser2',
            'email': 'invalid-email',
            'password': 'StrongPass1',
            'tel': '09012345678',
            'pref': self.pref.pk,
        }, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('email', response.data)
        self.assertFalse(CustomUser.objects.filter(username='testuser2').exists())
        # Tests rejection of invalid email formats.
        response = self.client.post(self.register_url, {
            'username': 'validuser',
            'email': 'bad-email',
            'password': 'StrongPass1',
            'tel': '09012345678',
            'pref': self.pref.pk,
        })
        self.assertContains(response, 'Enter a valid email address.')

    def test_register_form_rejects_duplicate_email(self):
        # Tests rejection of duplicate email addresses.
        CustomUser.objects.create_user(username='existing', email='duplicate@example.com', password='StrongPass1', pref=self.pref)
        response = self.client.post(self.register_url, {
            'username': 'newuser',
            'email': 'duplicate@example.com',
            'password': 'StrongPass1',
            'tel': '09012345678',
            'pref': self.pref.pk,
        })
        self.assertContains(response, 'A user with this email already exists.')

    def test_register_form_rejects_weak_password(self):
        # Tests rejection of passwords not meeting complexity requirements.
        response = self.client.post(self.register_url, {
            'username': 'validuser',
            'email': 'test4@example.com',
            'password': 'weakpass',
            'tel': '09012345678',
            'pref': self.pref.pk,
        })
        self.assertContains(response, 'Password must contain at least one uppercase letter.')

    def test_register_form_rejects_non_digit_tel(self):
        # Tests rejection of non-digit telephone numbers.
        response = self.client.post(self.register_url, {
            'username': 'validuser',
            'email': 'test5@example.com',
            'password': 'StrongPass1',
            'tel': '090-1234-5678',
            'pref': self.pref.pk,
        })
        self.assertContains(response, 'Telephone number must contain digits only.')

    def test_register_form_rejects_invalid_pref(self):
        # Tests rejection of invalid prefecture IDs.
        response = self.client.post(self.register_url, {
            'username': 'validuser',
            'email': 'test6@example.com',
            'password': 'StrongPass1',
            'tel': '09012345678',
            'pref': 999,
        })
        self.assertContains(response, 'Selected prefecture does not exist.')


class RegistrationAPITests(TestCase):
    # API tests verify backend validation and endpoint behavior.
    def setUp(self):
        # Sets up API client, test prefecture, and API URL.
        self.client = APIClient()
        self.pref = Pref.objects.create(name='Osaka')
        self.api_url = reverse('accounts:api_register')

    def test_api_creates_user_with_valid_data(self):
        # Tests successful user creation via API with valid data.
        response = self.client.post(self.api_url, {
            'username': 'apiuser',
            'email': 'api@example.com',
            'password': 'StrongPass1',
            'tel': '08012345678',
            'pref': self.pref.pk,
        }, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertTrue(CustomUser.objects.filter(email='api@example.com').exists())

    def test_api_rejects_duplicate_email(self):
        # Tests API rejection of duplicate emails.
        CustomUser.objects.create_user(username='existing', email='duplicateapi@example.com', password='StrongPass1', pref=self.pref)
        response = self.client.post(self.api_url, {
            'username': 'apiuser',
            'email': 'duplicateapi@example.com',
            'password': 'StrongPass1',
            'tel': '08012345678',
            'pref': self.pref.pk,
        }, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('email', response.json())

    def test_api_rejects_weak_password(self):
        # Tests API rejection of weak passwords.
        response = self.client.post(self.api_url, {
            'username': 'apiuser',
            'email': 'api2@example.com',
            'password': 'weakpass',
            'tel': '08012345678',
            'pref': self.pref.pk,
        }, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('password', response.json())
