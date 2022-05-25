from django.urls import path, reverse_lazy, include

from .views import *

app_name = 'master'

urlpatterns = [
    path('<slug:slug>/post_add/', PostAdd.as_view(), name='post_add'),
    path('<slug:master_slug>/post/<slug:slug>/', PostShow.as_view(), name='post'),
    path('add/', MasterAdd.as_view(), name='master_add'),
    path('all/', MasterAllShow.as_view(), name='master_all_show'),
    path('<slug:slug>/', MasterOneShow.as_view(), name='master_one_show'),
    path('<slug:slug>/update/', MasterUpdate.as_view(), name='master_update'),
    path('<slug:slug>/service_add/', ServiceAdd.as_view(), name='service_add'),
    path('<slug:master_slug>/service/<slug:slug>/', ServiceShow.as_view(), name='service_one_show'),
    path('<slug:master_slug>/service/<slug:slug>/update/', ServiceUpdate.as_view(), name='service_update'),
]