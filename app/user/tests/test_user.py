from django.test import TestCase, Client
from django.contrib.auth import get_user_model

from user.models import User


def create_user(**params):
    return get_user_model().objects.create_user(**params)


class UserTests(TestCase):

    def test_create_user_str(self):
        """Test to create a user with a string representation"""
        user = User.objects.create(
            name='test',
            email='test@email.com',
            password='test123'
        )

        self.assertEqual(str(user), user.email)

    def test_create_user_successful(self):
        """Test to create a user with success"""
        payload = {
            'email': 'test@email.com',
            'password': 'test12345',
            'name': 'Test'
        }
        self.client.post('/signup/', payload)

        exists = User.objects.filter(
            email=payload['email']
        ).exists()
        self.assertTrue(exists)

    def test_user_exists(self):
        """Test creating user that already exists fails"""
        payload = {
            'email': 'test@email.com',
            'password': 'test12345',
            'name': 'Test'
        }
        create_user(**payload)
        self.client.post('/signup/', payload)

        comment = User.objects.all().order_by('-email')
        self.assertEqual(comment.count(), 1)
