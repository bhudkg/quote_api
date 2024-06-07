from django.shortcuts import render
import requests
from django.http import HttpResponse
# Create your views here.

def index(request):
    api_url = 'https://newsapi.org/v2/everything?q=tesla&from=2024-05-07&sortBy=publishedAt&apiKey=3e4beeca7c1b41a298498490f8dded20'
    response = requests.get(api_url)
    data = response.json()

    context = {
        'data':data
    }

    return render(request, 'index.html', context)

