from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_get_user_with_email_successful(self):
        """Test creating a new user with email address is successful"""
        email = "test@siddhant.com"
        password = "testpass123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email(self):
        """Test New user email is normalized"""

        email = 'test@SIDDHANT.com'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_invalid_user_email(self):
        """Test user with no email gives invalid error"""

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""

        user = get_user_model().objects.create_superuser(
            "test@siddhant.com",
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
