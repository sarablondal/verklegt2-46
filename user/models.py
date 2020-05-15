from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.CharField(max_length=9999, blank=True)
    name = models.CharField(max_length=255, blank=True)

