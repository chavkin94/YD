from django.urls import path, reverse_lazy
from .views import *

app_name = 'organization'

urlpatterns = [
    path('add/', OrganizationAdd.as_view(), name='organization_add'),
    path('all/', OrganizationAllShow.as_view(), name='organization_all_show'),
    path('<slug:slug>/', OrganizationOneShow.as_view(), name='organization_one_show'),
    path('<slug:slug>/update/', OrganizationUpdate.as_view(), name='organization_update'),

]