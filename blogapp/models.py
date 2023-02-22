from datetime import datetime

from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField(default = datetime.now, blank=True)
    body = models.CharField(max_length=10000)