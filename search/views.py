from django.shortcuts import render
from django.db.models import Value
from django.db.models import F
from django.db.models.functions import Concat
from account.models import CustomUser
from main.models import Location
from master.models import ServiceCategory


def search_view(request):
    locations = Location.objects.all()
    service_categorys = ServiceCategory.objects.all().order_by('name')
    age_list = range(16, 80)
    context = {
        'locations': locations,
        'age_list': age_list,
        'service_categorys': service_categorys,
        # 'subscription_to_me': subscription_to_me,
        # 'subscription_my_user': subscription_my_user,
        # 'subscription_my_master': subscription_my_master,
        # 'organizations': organizations,
        # 'feed': feed,
        # 'posts': posts,
    }
    return render(request, 'search/search.html', context)


def search_accounts(request):
    data = request.GET
    accounts = CustomUser.objects.annotate(full_name=Concat(F('last_name'), Value(' '), F('first_name'), Value(' '), F('surname'))).filter(full_name__icontains=data.get('text_search'))
    #
    # accounts = CustomUser.objects.all()
    # first_post_id = data.get('first_post_id')
    # if first_post_id:
    #     posts =AccountPost.objects.all().first()
    #     first_post = AccountPost.objects.get(pk=data.get('first_post_id'))
    #     posts = AccountPost.objects.filter(user=current, date_create__gt=first_post.date_create)[:4]
    # else:
    #     posts = AccountPost.objects.filter(user=current)[:4]
    context = {
        'accounts': accounts,
    }
    # account_post_one_show_json(post_end)
    return render(request, 'search/search_account.html', context)