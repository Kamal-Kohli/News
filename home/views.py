from django.views.generic import TemplateView
from django.shortcuts import render
import requests

API_KEY = '2228671f48644d399e8cc37fb14015f6'


def fetch_news_data(request, page_size=10):
    country = request.GET.get('country')
    category = request.GET.get('category')

    if country:
        url = (f'https://newsapi.org/v2/top-headlines?country={country}'
               f'&apiKey={API_KEY}')
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
    else:
        url = (f'https://newsapi.org/v2/top-headlines?category={category}'
               f'&apiKey={API_KEY}')
        response = requests.get(url)
        data = response.json()
        articles = data['articles']

    return data


class Index(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        articles_data = fetch_news_data(self.request, page_size=20)
        context['articles'] = articles_data['articles']
        context['total_articles'] = articles_data['totalResults']
        return context

        