import datetime

from django.db import models
from django.utils import timezone

class Post(models.Model):
    post_title = models.CharField(max_length=200)
    post_subtitle = models.CharField(max_length=200)
    post_body = models.TextField(max_length=1000)
    pub_date = models.DateTimeField('date published')
    primary_photo = models.ImageField()
    body_photo = models.ImageField()
    def __str__(self):
        return self.post_body
    def was_published_in_the_past(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now   