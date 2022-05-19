from django.urls import path, reverse_lazy
from .views import *

app_name = 'master'

urlpatterns = [
    path('add/', MasterAdd.as_view(), name='master_add'),
    path('all/', MasterAllShow.as_view(), name='master_all_show'),
    path('<slug:slug>/', MasterOneShow.as_view(), name='master_one_show'),
    path('<slug:slug>/update/', MasterUpdate.as_view(), name='master_update'),

]