from django.shortcuts import render
from . import views
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Article, AuthoredArticle
import requests
from django.conf import settings
import random

# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


class ArticleListView(ListView):
    model = Article
    context_object_name = 'articles'
    template_name = 'articles/article_index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        articles_data = self.get_queryset()
        context['trending_articles'] = articles_data['trending_articles']
        context['articles'] = articles_data['articles']
        return context

    def get_queryset(self):
        # Fetch 2 trending articles using top-headlines
        trending_url = 'https://newsapi.org/v2/top-headlines'
        trending_params = {
            'language': 'en',
            'apiKey': settings.NEWS_API_KEY,
            'pageSize': 2,  # Increase the pageSize to 2
            'page': random.randint(1, 9),
        }
        trending_response = requests.get(trending_url, params=trending_params)

        print("Trending response status code:", trending_response.status_code)
        print("Trending response content:", trending_response.text)

        # Fetch popular articles using the everything endpoint
        url = 'https://newsapi.org/v2/everything'
        params = {
            'q': 'news',
            'language': 'en',
            'sortBy': 'popularity',
            'apiKey': settings.NEWS_API_KEY,
            'pageSize': 9,
            'page': random.randint(1, 9),
        }
        response = requests.get(url, params=params)

        # Create Article instances for trending articles without saving them to the database
        trending_articles = []
        if trending_response.status_code == 200:
            trending_data = trending_response.json()
            for item in trending_data['articles']:
                article = Article(
                    title=item['title'],
                    author=item.get('author', ''),
                    description=item['description'],
                    content=item.get('content', ''),
                    url=item['url'],
                    url_to_image=item['urlToImage'],
                    published_at=item['publishedAt'],
                    source_name=item['source']['name'],
                )
                trending_articles.append(article)

        articles = []
        if response.status_code == 200:
            data = response.json()
            for item in data['articles']:
                article = Article(
                    title=item['title'],
                    author=item.get('author', ''),
                    description=item['description'],
                    content=item.get('content', ''),
                    url=item['url'],
                    url_to_image=item['urlToImage'],
                    published_at=item['publishedAt'],
                    source_name=item['source']['name'],
                )
                articles.append(article)

        return {
            'trending_articles': trending_articles,
            'articles': articles,
        }


class AuthoredArticleListView(ListView):
    model = AuthoredArticle
    context_object_name = 'authored_articles'
    template_name = 'authored_articles/article_index.html'

    def get_queryset(self):
        return AuthoredArticle.objects.all()


class AuthoredArticleDetailView(DetailView):
    model = AuthoredArticle
    template_name = 'authored_articles/article_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['authored_article'] = self.object
        return context


class AuthoredArticleCreateView(CreateView):
    model = AuthoredArticle
    template_name = 'authored_articles/article_create.html'
    fields = '__all__'

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'article_id': self.id})
