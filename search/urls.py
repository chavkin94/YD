from django.urls import path, reverse_lazy, include
from .views import *

app_name = 'organization'

urlpatterns = [
    path('', search_view, name='search_view'),
    path('search/accounts/', search_accounts, name='search_accounts'),
]