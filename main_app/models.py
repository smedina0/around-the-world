from django.db import models
from django.urls import reverse

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    content = models.TextField()
    url = models.URLField(max_length=255, blank=True)
    url_to_image = models.URLField(max_length=255, blank=True)
    published_at = models.DateTimeField()
    source_name = models.CharField(max_length=255, blank=True)
