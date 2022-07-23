from django.db import models
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.models import User


class author(models.Model):
    username = models.CharField(max_length=30, default=None)

class postgmodels(models.Model):
    title = models.CharField(max_length=30)
    author = models.ForeignKey(User, default=None, null=True, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    comment = models.TextField()
    created = models.DateTimeField(default=datetime.now())
    
    def __str__(self):
        return f'{self.title} - {self.title}'

