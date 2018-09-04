import datetime

from django.db import models
from django.utils import timezone

class Post(models.Model):
    post_title = models.CharField(max_length=200)
    post_subtitle = models.CharField(max_length=200, null=True)
    post_body = models.TextField(max_length=5000, null=True)
    pub_date = models.DateTimeField('date published', null=True)
    primary_photo = models.ImageField(null=True, upload_to='blog/')
    body_photo = models.ImageField(blank=True, null=True, upload_to='blog/')
    def __str__(self):
        return self.post_body
    def was_published_in_the_past(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now   