from django.contrib import admin
from .models import Article, AuthoredArticle

# Register your models here.
admin.site.register(Article)
admin.site.register(AuthoredArticle)
