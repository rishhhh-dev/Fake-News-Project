from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.


class post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=30)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
