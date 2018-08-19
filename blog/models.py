import datetime

from django.db import models
from django.utils import timezone

class Post(models.Model):
    post_title = models.CharField(max_length=200)
    post_body = models.TextField(max_length=1000)
    pub_date = models.DateTimeField('date published')