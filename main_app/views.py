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

    def get_queryset(self):
        # Fetch data from the News API
        url = 'https://newsapi.org/v2/everything'
        params = {
            'q': 'Technology',
            'sortBy': 'popularity',
            'apiKey': settings.NEWS_API_KEY,
            'pageSize': 10,
        }
        response = requests.get(url, params=params)

        # Create Article instances without saving them to the database
        articles = []
        if response.status_code == 200:
            data = response.json()
            # print(data)
            for item in data['articles']:
                article = Article(
                    title=item['title'],
                    author=item['author'],
                    description=item['description'],
                    content=item['content'],
                    url=item['url'],
                    url_to_image=item['urlToImage'],
                    published_at=item['publishedAt'],
                    source_name=item['source']['name'],
                )
                articles.append(article)
        return articles
