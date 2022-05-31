# https://www.youtube.com/watch?v=9QNw5v6BUBE&list=PLSWnD6rL-m9adebgpvvOLH5ASGJiznWdg&index=13
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse

from account.models import CustomUser
from main.models import test
from master.models import Master
from subscription.models import Subscription


def index(request):
        return render(request, 'main/index.html')


def feed(request):
        return render(request, 'main/content/feed.html')


def search(request):
        return render(request, 'main/content/search.html')




def main(request):
        user = CustomUser.objects.all().first()
        return render(request, 'main/main.html', locals())


def basket_adding(request):
        return_dict = dict()
        data = request.POST
        print(data)
        user = CustomUser.objects.get(pk=data.get("user_id"))
        master = Master.objects.all().first()
        new_test = Subscription.objects.create(subscriber=user, user =user, master=master)
        return JsonResponse(return_dict)



