from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

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
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('authored_article_detail', kwargs={'pk': self.id})


class Photo(models.Model):
    url = models.CharField(max_length=200)
    authored_article = models.ForeignKey(
        AuthoredArticle, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for authored_article_id: {self.authored_article_id} @{self.url}"
