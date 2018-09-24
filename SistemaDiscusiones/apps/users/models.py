from django.db import models

from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    programa=models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.email