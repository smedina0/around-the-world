from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('articles/', views.ArticleListView.as_view(), name='article_list'),
    path('authored_articles/', views.AuthoredArticleListView.as_view(),
         name='authored_article'),

]
