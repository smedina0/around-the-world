from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('articles/', views.ArticleListView.as_view(), name='article_list'),
    path('authored_articles/', views.AuthoredArticleListView.as_view(),
         name='authored_article'),
    path('authored_articles/<int:pk>',
         views.AuthoredArticleDetailView.as_view(), name='authored_article_detail'),
    path('authored_articles/create/', views.AuthoredArticleCreateView.as_view(),
         name='authored_article_create'),
    path('authored_articles/<int:pk>/update/',
         views.AuthoredArticleUpdateView.as_view(), name='authored_article_update'),
    path('authored_articles/<int:pk>/delete/',
         views.AuthoredArticleDeleteView.as_view(), name='authored_article_delete'),
    path('authored_articles/<int:authored_article_id>/add_photo',
         views.add_photo, name='add_photo'),
    path('accounts/signup/', views.signup, name='signup'),
]
