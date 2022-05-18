from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordResetView, \
    PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path, reverse_lazy
from .views import *

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),

    #Страница пользователя
    path('account/', account, name='account'),

    #изменение данных пользователя
    path('accounts/change/', CUChangeUserInfoView.as_view(), name='account_change'),

    # Авторизация
    path('accounts/login/', CULoginView.as_view(), name='login'),

    # Выход
    path('accounts/logout/', CULogoutView.as_view(), name='logout'),

    # Смена пароля
    path('accounts/password/change/', CUPasswordChangeView.as_view(), name='password_change'),

    # Регистрация пользователя
    path('accounts/register/', CURegisterUserView.as_view(), name='register'),

    # При успешной регистрации пользователя
    path('accounts/register/done/', CURegisterUserDoneView.as_view(), name='register_done'),

    # Активация пользователя не работал сигнал нужно доделать, чтоб отправлялся на почту
    # path('accounts/register/activate/<str:sign>/', user_activate(), name='register_activate'),



    # При успешной смене пароля
    path('accounts/password_change/done/',
         PasswordChangeView.as_view(
             template_name='registration/password_change_done.html'
         ),
         name='password_change_done'),

    # # Сброс пароля
    # path('accounts/reset/<uidb64>/<token>/',
    #      PasswordResetConfirmView.as_view(
    #          template_name='registration/password_reset_confirm_password.html',
    #      ),
    #      name='password_reset_confirm'),
    #
    # # Сброс пароля
    # path('accounts/reset/done/',
    #      PasswordResetCompleteView.as_view(
    #          template_name='registration/password_confirmed.html',
    #      ),
    #      name='password_complete'),

]
