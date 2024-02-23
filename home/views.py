from django.views.generic import TemplateView
from django.shortcuts import render

import requests

API_KEY = '2228671f48644d399e8cc37fb14015f6'

# Create your views here.
def fetch_news_data(page_size=10):
    url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}'
    response = requests.get(url)
    data = response.json()

    articles = data['articles']

    return data

class Index(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        articles_data = fetch_news_data(page_size=20)  # Fetch 20 articles
        context['articles'] = articles_data['articles']
        context['total_articles'] = articles_data['totalResults']
        return context