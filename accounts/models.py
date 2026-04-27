from django.contrib.auth.models import AbstractUser
from django.db import models


class Pref(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'Prefecture'
        verbose_name_plural = 'Prefectures'

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    # Enforce email uniqueness at the DB layer in addition to app validation.
    email = models.EmailField(unique=True)
    tel = models.CharField(max_length=20, null=True, blank=True)
    pref = models.ForeignKey(Pref, on_delete=models.PROTECT, null=True, blank=True, related_name='users')

    def __str__(self):
        return self.username
