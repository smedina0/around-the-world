from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField

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


class AuthoredArticle(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    content = RichTextField()
    facebook_link = models.URLField(max_length=255, blank=True, null=True)
    twitter_link = models.URLField(max_length=255, blank=True, null=True)
    instagram_link = models.URLField(max_length=255, blank=True, null=True)
    linkedin_link = models.URLField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('authored_article_detail', kwargs={'pk': self.id})
