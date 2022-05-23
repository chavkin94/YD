from django.urls import path, reverse_lazy
from .views import *

app_name = 'account'

urlpatterns = [
    #Страница пользователя
    path('', account_show, name='account'),

    path('post_add/', AccountPostAdd.as_view(), name='account_post_add'),

    #изменение данных пользователя
    path('change/', CUChangeUserInfoView.as_view(), name='account_change'),

    # Авторизация
    path('login/', CULoginView.as_view(), name='login'),

    # Выход
    path('logout/', CULogoutView.as_view(), name='logout'),

    # Смена пароля
    path('password/change/', CUPasswordChangeView.as_view(), name='password_change'),

    # При успешной смене пароля
    path('password/change/done/', CUPasswordChangeDoneView.as_view(), name='password_change_done'),

    # Регистрация пользователя
    path('register/', CURegisterUserView.as_view(), name='register'),

    # При успешной регистрации пользователя
    path('register/done/', CURegisterUserDoneView.as_view(), name='register_done'),

    # Активация пользователя не работал сигнал нужно доделать, чтоб отправлялся на почту
    # path('accounts/register/activate/<str:sign>/', user_activate(), name='register_activate'),

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
