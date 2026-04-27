from django.contrib.auth.models import AbstractUser
from django.db import models


class Pref(models.Model):
    # Model representing Japanese prefectures for user registration.
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        # Meta class for model metadata: sets verbose names for admin interface.
        verbose_name = 'Prefecture'
        verbose_name_plural = 'Prefectures'

    def __str__(self):
        # Returns the prefecture name as the string representation.
        return self.name


class CustomUser(AbstractUser):
    # Custom user model extending Django's AbstractUser with additional fields.
    # Enforce email uniqueness at the DB layer in addition to app validation.
    email = models.EmailField(unique=True)
    tel = models.CharField(max_length=20, null=True, blank=True)
    pref = models.ForeignKey(Pref, on_delete=models.PROTECT, null=True, blank=True, related_name='users')

    def __str__(self):
        # Inherits the default __str__ from AbstractUser, which returns username.
        return self.username
