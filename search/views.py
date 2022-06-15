from django.shortcuts import render
from django.db.models import Value
from django.db.models import F,Q
from django.db.models.functions import Concat
from account.models import CustomUser, AccountPost
from main.models import Location
from master.models import ServiceCategory, Master, MasterPost, Service
from datetime import date


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
    count_elem = int(data.get('count_elem'))
    number_start = int(data.get('number_elem'))
    number_end = number_start + count_elem
    accounts = CustomUser.objects.annotate(
            full_name=Concat(F('last_name'), Value(' '), F('first_name'), Value(' '), F('surname'))).filter(
            full_name__icontains=data.get('text_search'))
    if data.get('btn_group_value') != 'btn_all':
        if data.get('filters_account_gender') != '':
            accounts = accounts.filter(gender=data.get('filters_account_gender'))
    accounts = accounts[number_start: number_end]
    context = {
        'accounts': accounts,
    }
    return render(request, 'search/search_account.html', context)


def search_masters(request):
    data = request.GET
    count_elem = int(data.get('count_elem'))
    number_start = int(data.get('number_elem'))
    number_end = number_start + count_elem
    masters = Master.objects.filter(name__icontains=data.get('text_search'))
    if data.get('btn_group_value') != 'btn_all':
        if data.get('filters_master_id_location') != '':
            location = Location.objects.get(name__icontains=data.get('filters_master_id_location'))
            masters = masters.filter(location__pk=location.pk)
    masters = masters[number_start: number_end]
    context = {
        'masters': masters,
    }
    return render(request, 'search/search_master.html', context)


def search_posts(request):
    data = request.GET
    count_elem = int(data.get('count_elem'))
    number_start = int(data.get('number_elem'))
    number_end = number_start + count_elem
    posts_account = AccountPost.objects.filter(Q(title__icontains=data.get('text_search')) | Q(content__icontains=data.get('text_search')))
    posts_master = MasterPost.objects.filter(Q(title__icontains=data.get('text_search')) | Q(content__icontains=data.get('text_search')))
    posts = posts_account.union(posts_master).order_by('date_create')
    posts = posts[number_start: number_end]
    context = {
        'posts': posts,
    }
    return render(request, 'search/search_post.html', context)


def search_services(request):
    data = request.GET
    count_elem = int(data.get('count_elem'))
    number_start = int(data.get('number_elem'))
    number_end = number_start + count_elem
    services = Service.objects.filter(Q(name__icontains=data.get('text_search')) | Q(description__icontains=data.get('text_search')) | Q(custom_category=data.get('text_search')))
    if data.get('btn_group_value') != 'btn_all':
        if data.get('filters_service_id_service_category') != '':
            service_category = ServiceCategory.objects.get(slug=data.get('filters_service_id_service_category'))
            services = services.filter(serviceCategory__pk=service_category.pk)
    services = services[number_start: number_end]
    context = {
        'services': services,
    }
    return render(request, 'search/search_service.html', context)
