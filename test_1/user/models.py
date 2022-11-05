from django.contrib.auth.models import AbstractUser
from django.db import models

class Info(models.Model):
    balance = models.IntegerField()
    title = models.CharField(max_length=100)

class Categories(models.Model):
    cats = models.CharField(max_length=50)

    def __str__(self):
        return self.cats