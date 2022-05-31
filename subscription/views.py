from django.http import JsonResponse
from django.shortcuts import render

from account.models import CustomUser
from master.models import Master
from subscription.models import Subscription
from django.core.exceptions import ObjectDoesNotExist


def subscripe_unsubscripe(request):
    return_dict = dict()
    data = request.POST
    err = False
    subscriper=None
    user = None
    master = None
    try:
        subscriper = CustomUser.objects.get(username=data.get("user_current_slug"))
    except ObjectDoesNotExist:
        err = True

    url_type = data.get("url_type")
    if url_type == 'account':
        try:
            user = CustomUser.objects.get(username=data.get("user_slug"))
        except ObjectDoesNotExist:
            err = True
    elif url_type == 'master':
        try:
            master = Master.objects.get(slug=data.get("master_slug"))
        except ObjectDoesNotExist:
            err = True

    if subscriper:
        if url_type == 'account':
            try:

                subscripe = Subscription.objects.get(subscriper=subscriper, user=user)
                subscripe.delete()
            except ObjectDoesNotExist:
                Subscription.objects.create(subscriper=subscriper, user=user)
        elif url_type == 'master':
            try:

                subscripe = Subscription.objects.get(subscriper=subscriper, master=master)
                subscripe.delete()
            except ObjectDoesNotExist:
                Subscription.objects.create(subscriper=subscriper, master=master)


    return JsonResponse(return_dict)
