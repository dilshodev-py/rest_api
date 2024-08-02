from django.contrib.auth.models import User
from django.db import models
from django.db.models import Model


class Category(Model):
    name = models.CharField(max_length=10, unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name