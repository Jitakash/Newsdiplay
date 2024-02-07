from django.shortcuts import render
import requests
API_KEY='4081754be1854e4db9edfaf4c8f40044'

def home(request):
    country=request.GET.get('country')
    category=request.GET.get('category')

    if country:
        url=f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
    else:
        url=f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
    return render(request,'news_api/home.html',context={'articles':articles})
