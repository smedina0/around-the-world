from django.shortcuts import render
from . import views
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Article
import requests
from django.conf import settings

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
        context['trending_article'] = articles_data['trending_article']
        context['articles'] = articles_data['articles']
        return context

    def get_queryset(self):
        # Fetch a trending article using top-headlines
        trending_url = 'https://newsapi.org/v2/top-headlines'
        trending_params = {
            'language': 'en',
            'apiKey': settings.NEWS_API_KEY,
            'pageSize': 1,
        }
        trending_response = requests.get(trending_url, params=trending_params)

        # Fetch popular articles using the everything endpoint
        url = 'https://newsapi.org/v2/everything'
        params = {
            'q': 'en',
            'sortBy': 'popularity',
            'apiKey': settings.NEWS_API_KEY,
            'pageSize': 9,
        }
        response = requests.get(url, params=params)

        # Create Article instances without saving them to the database
        articles = []
        if trending_response.status_code == 200:
            trending_data = trending_response.json()
            for item in trending_data['articles']:
                trending_article = Article(
                    title=item['title'],
                    author=item.get('author', ''),
                    description=item['description'],
                    content=item.get('content', ''),
                    url=item['url'],
                    url_to_image=item['urlToImage'],
                    published_at=item['publishedAt'],
                    source_name=item['source']['name'],
                )

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
            'trending_article': trending_article if trending_response.status_code == 200 else None,
            'articles': articles,
        }
