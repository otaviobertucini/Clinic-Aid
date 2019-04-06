from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):

    role = models.CharField(max_length=10, blank=False, null=True)
