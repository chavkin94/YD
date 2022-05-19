from django.urls import path, reverse_lazy
from .views import *

app_name = 'organization'

urlpatterns = [
    path('add/', OrganizationAdd.as_view(), name='organization_add'),
    #Страница Организации
    path('<slug:slug>/', OrganizationOneShow.as_view(), name='organization_one_show'),
]