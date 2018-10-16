import datetime

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from django.db import models
from tinymce import HTMLField
from django.utils import timezone
from django.core.cache import cache

POSTS_KEY = "posts.all"

class Post(models.Model):
    post_title = models.CharField(max_length=200)
    post_subtitle = models.CharField(max_length=200, null=True)
    post_body = HTMLField('Content', null=True)
    pub_date = models.DateTimeField('date published', null=True)
    primary_photo = models.ImageField(null=True, upload_to='blog/')
    def __str__(self):
        return self.post_body
    def was_published_in_the_past(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now 

@receiver(post_save, sender=Post)
def invalidate_cache_save(sender, **kwargs):
    cache.delete(POSTS_KEY)

@receiver(post_delete, sender=Post)
def invalidate_cache_delete(sender, **kwargs):
    cache.delete(POSTS_KEY)