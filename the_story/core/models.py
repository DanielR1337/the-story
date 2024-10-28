from django.conf import settings
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)

# Create your models here.

class UserManager(BaseUserManager):
    # Manager for Users

    def create_user(self, email, password=None, **extra_fields):
        # Create, save and return a new user.
        if not email:
            raise ValueError('User must have an email address.')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        # Create and return a new supoeruser.
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

class User(AbstractBaseUser, PermissionsMixin):
    # User in the system.
    email = models.EmailField(max_length=255, unique=True)
    name=models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

class Bird(models.Model):
    """Bird to be registered when found"""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=255)
    sciName = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    family = models.CharField(max_length=255)
    order = models.CharField(max_length=255)
    status = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Breeding(models.Model):
    """Breeding contains questions to increase status level"""

    question = models.TextField()
    answer = models.CharField(max_length=255)
    region = models.CharField(max_length=255)

    def __str__(self):
        return self.question