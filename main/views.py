from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.views.generic import UpdateView, CreateView, TemplateView

from main.forms import ChangeUserInfoForm, RegisterUserForm
from main.models import CustomUser

from django.core.signing import BadSignature
from .utilities import signer


def index(request):
        return render(request, 'main/index.html')


# Подкласс выполняющий вход
class CULoginView(LoginView):
        template_name = 'registration/login.html'

#Страница пользователя
@login_required
def account(request):
        return render(request, 'main/account.html')

#Подкласс выполняющий выход пользователя, миксин LoginRequiredMixin делает доступной только зарегистрированным пользователям
class CULogoutView(LoginRequiredMixin, LogoutView):
        template_name = 'registration/logout.html'


#класс изменения данных пользователя
class CUChangeUserInfoView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
        model = CustomUser
        template_name = 'main/account_change_info.html'
        form_class = ChangeUserInfoForm
        success_url = reverse_lazy('main:account')
        success_message = 'Данные пользователя изменены'

        def setup(self, request, *args, **kwargs):
                self.user_id = request.user.pk
                return super().setup(request, *args, **kwargs)

        def get_object(self, queryset=None):
                if not queryset:
                        queryset = self.get_queryset()
                return get_object_or_404(queryset, pk=self.user_id)

#класс смены пароля
class CUPasswordChangeView(SuccessMessageMixin,LoginRequiredMixin, PasswordChangeView):
        template_name = 'registration/password_change.html'
        success_url = reverse_lazy('main:password_change_done')
        success_message = 'Пароль пользователя изменен'


#класс регистрации пользователя
class CURegisterUserView(CreateView):
        model = CustomUser
        template_name = 'registration/register_user.html'
        form_class = RegisterUserForm
        success_url = reverse_lazy('main:register_done')


#класс успешной регистрации пользователя
class CURegisterUserDoneView(TemplateView):
        template_name = 'registration/register_done.html'


#Контроллер активацйии пользователя
def user_activate(request, sign):
        try:
                username = signer.unsign(sign)
        except BadSignature:
                return render(request, 'registration/bad_signature.html')
        user = get_object_or_404(CustomUser, username=username)
        if user.is_activated:
                template = 'registration/user_is_activated.html'
        else:
                templale = 'registration/activation_done.html'
                user.is_activated = True
                user.save()
        return render(request,template)