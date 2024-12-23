"""Test models"""

from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models

def create_user(email='user@example.com', password='testpass123'):
    """Create and return a new user."""
    return get_user_model().objects.create_user(email, password)

class ModelTests(TestCase):
    """Test models."""

    def test_create_user_with_email_successful(self):
        """Test creating a user with an email is successful"""
        email = 'test@example.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        # Test email is normalized for new users.
        sample_emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.COM', 'TEST3@example.com'],
            ['test4@example.COM', 'test4@example.com'],
        ]
        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'sample123')
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
        # Test that creating a user without an email raises a ValueError.
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'test123')

    def test_create_superuser(self):
        # Test creating a superuser
        user = get_user_model().objects.create_superuser(
            'test@example.com',
            'test123',
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_create_bird(self):
        """Test creating a discovered bird."""
        user = create_user()

        bird = models.Bird.objects.create(
            name="Black-bellied Whistling-Duck",
            sciName="Dendrocygna autumnalis",
            region=[
                "North America"
            ],
            family="Anatidae",
            order="Anseriformes",
            status="Low Concern",
            user=user
        )

        self.assertEqual(str(bird), bird.name)

    def test_create_breeding(self):
        """Test creating breeding action."""
        breeding = models.Breeding.objects.create(
            question = "What is the scientific name of the Wild Turkey?",
            answer = "	Meleagris gallopavo",
                        region=[
                "North America"
            ]
        )

        self.assertEqual(str(breeding), breeding.question)