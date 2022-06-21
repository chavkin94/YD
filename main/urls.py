from django.urls import path, reverse_lazy
from .views import *

app_name = 'main'

urlpatterns = [
    path('authorization', index, name='index'),
    path('feed', feed, name='feed'),
    path('search', search, name='search'),

    path('m/', main, name='main'),
    path('basket_adding/', basket_adding, name='basket_adding'),

]
