from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'movies/list.html')

def details(request):
    return render(request, 'movies/detail.html')

def search(request):
    return render(request, 'movies/search.html')