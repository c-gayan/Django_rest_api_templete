from django.db import models
from django.db.models.base import Model
from django.db.models.fields import BooleanField, DateTimeField

# Create your models here.
class Todo(models.Model):
    name = models.CharField(max_length=100)
    task = models.CharField(max_length=300)
    reminder = BooleanField(default=False, blank=True)
    created_at = DateTimeField(auto_now_add=True)