import datetime

from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import JSONField

class Project(models.Model):

	project_title = models.CharField(max_length=200)
	project_description = models.TextField(max_length=1000)
	tech_used = JSONField()
	sub_description = JSONField()
	project_link = models.URLField(max_length=100)
	project_date = models.DateTimeField('project date')
	project_photo = models.ImageField()