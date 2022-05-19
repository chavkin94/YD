from django.urls import path, reverse_lazy
from .views import *

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
]
