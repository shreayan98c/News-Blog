from django.db import models

# Create your models here.

class Article(models.Model):
	source = models.CharField(max_length=200, null=True, blank=True)
	author = models.CharField(max_length=200, default="Anonymous", null=True, blank=True)
	title = models.CharField(max_length=200, null=True, blank=True)
	description = models.CharField(max_length=500, null=True, blank=True)
	url = models.CharField(max_length=200, null=True, blank=True)
	urlToImg = models.CharField(max_length=200, null=True, blank=True)
	publishedAt = models.DateTimeField('Date Published', null=True, blank=True)
	content = models.TextField(null=True, blank=True)

	def __str__(self):
		return self.title