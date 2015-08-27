from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Group(models.Model):
    owner = models.ForeignKey(User)
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
