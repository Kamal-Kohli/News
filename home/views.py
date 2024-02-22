from django.views.generic import TemplateView
import requests

API_KEY = '2228671f48644d399e8cc37fb14015f6'

# Create your views here.
class Index(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        country = self.request.GET.get('country')  # Accessing request using self.request
        category = self.request.GET.get('category')  # Accessing request using self.request

        if country:
            url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}'
            response = requests.get(url)
            data = response.json()
            articles = data['articles']
        elif category:
            url = f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={API_KEY}'
            response = requests.get(url)
            data = response.json()
            articles = data['articles']
        else:
            articles = []  # Set articles to an empty list if neither country nor category is provided
        
        context['articles'] = articles
        return context
