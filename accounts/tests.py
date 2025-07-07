from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserProfile
from django.urls import reverse

class UserProfileModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='zazima', password='1234', email='mutanuzippy04@gmail.com')
        self.profile = UserProfile.objects.create(user=self.user, bio='Test bio')

    def test_user_profile_creation(self):
        self.assertEqual(self.profile.user.username, 'zazima')
        self.assertEqual(self.profile.bio, 'Test bio')
        self.assertFalse(self.profile.is_verified)

class UserViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='zazima', password='1234', email='mutanuzippy04@gmail.com')
        self.profile = UserProfile.objects.create(user=self.user, bio='Test bio')

    def test_register_view(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/register.html')

    def test_profile_view(self):
        self.client.login(username='zazima', password='1234')
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile/profile.html')

    def test_edit_profile_view(self):
        self.client.login(username='zazima', password='1234')
        response = self.client.get(reverse('edit_profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile/edit_profile.html')