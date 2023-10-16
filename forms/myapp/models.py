from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=150)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=105)
    notes = models.TextField(max_length=1000)
    def __str__(self):
        return self.username
