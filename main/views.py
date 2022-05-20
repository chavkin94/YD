from django.shortcuts import render


def index(request):
        return render(request, 'main/index.html')


def feed(request):
        return render(request, 'main/content/feed.html')


def search(request):
        return render(request, 'main/content/search.html')

