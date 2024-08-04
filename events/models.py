from django.db import models


class Event(models.Model):
	name = models.CharField(max_length=64, null=False, blank=False)
	date = models.DateField()
	location = models.CharField(max_length=64, null=False, blank=False)
	category = models.CharField(max_length=32, null=False, blank=False)
