import datetime

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from django.db import models
from tinymce import HTMLField
from taggit.managers import TaggableManager
from taggit.models import TaggedItemBase
from django.utils import timezone

PROJECTS_KEY = "projects.all"

class Project(models.Model):
	project_title = models.CharField(max_length=200)
	project_description = HTMLField('Content', null=True)
	tech_used = TaggableManager()
	PRODUCTMANAGER = 'PM'
	WEBDEVELOPER = 'WD'
	MACHINELEARNING = 'ML'
	GAMEDEVELOPER = 'GD'
	PROJECT_TYPE_CHOICES = (
		(PRODUCTMANAGER, 'Product Manager'),
		(WEBDEVELOPER, 'Web Developer'),
		(MACHINELEARNING, 'Machine Learning'),
		(GAMEDEVELOPER, 'Game Developer'),
	)
	project_type = models.CharField(
		max_length=2,
		choices=PROJECT_TYPE_CHOICES,
		default=WEBDEVELOPER,
	)
	project_link = models.URLField(max_length=100)
	project_date = models.DateField('project date')
	project_photo = models.ImageField(null=True, upload_to='projects/')
	def __str__(self):
		return self.project_description

@receiver(post_save, sender=Project)
def invalidate_cache(sender, **kwargs):
    cache.delete(PROJECTS_KEY)

@receiver(post_deleete, sender=Project)
def invalidate_cache(sender, **kwargs):
    cache.delete(PROJECTS_KEY)