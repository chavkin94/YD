from django.urls import path, reverse_lazy
from .views import *

app_name = 'subscription'

urlpatterns = [
    path('subscripe/', subscripe_unsubscripe, name='subscripe_unsubscripe'),

    # path('', main, name='main'),
    # path('basket_adding/', basket_adding, name='basket_adding'),

]
