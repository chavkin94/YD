from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.views.generic import UpdateView, CreateView, TemplateView, DetailView

from account.forms import ChangeUserInfoForm, RegisterUserForm, AccountPostAddForm
from account.models import CustomUser, AccountPost

from django.core.signing import BadSignature

from master.models import Master
from organization.models import Organization
from subscription.models import Subscription
from .utilities import signer


# Подкласс выполняющий вход
class CULoginView(LoginView):
        template_name = 'registration/login.html'


#Добавление поста
class AccountPostAdd(LoginRequiredMixin, CreateView):
    form_class = AccountPostAddForm
    template_name = 'account/post_add.html'
    success_url = reverse_lazy('account:account')
    login_url = reverse_lazy('account:login')

    def get_initial(self):
        # if CustomUser.objects.get(username=self.request.user.username):
            initial = super(AccountPostAdd, self).get_initial()
            initial['user'] = self.request.user
            return initial


#Просмотр поста
class AccountPostShow(DetailView):
    model = AccountPost
    template_name = 'account/post.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'post'

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


#Страница пользователя
@login_required
def account_show(request):
        masters = Master.objects.filter(user=request.user)
        organizations = Organization.objects.filter(user=request.user)
        posts = AccountPost.objects.filter(user=request.user)
        context = {
            'masters': masters,
            'organizations': organizations,
            'posts':posts
        }

        return render(request, 'account/account.html', context)


#Просмотр другого пользователя
class AccountAnotherShow(DetailView):
    model = CustomUser
    template_name = 'account/account_another.html'
    slug_field = 'username'
    slug_url_kwarg = 'slug'
    context_object_name = 'account'

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


#Подкласс выполняющий выход пользователя, миксин LoginRequiredMixin делает доступной только зарегистрированным пользователям
class CULogoutView(LoginRequiredMixin, LogoutView):
        template_name = 'registration/logout.html'


#класс изменения данных пользователя
class CUChangeUserInfoView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
        model = CustomUser
        template_name = 'account/account_change_info.html'
        form_class = ChangeUserInfoForm
        success_url = reverse_lazy('account:account')
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
        success_url = reverse_lazy('account:password_change_done')
        success_message = 'Пароль пользователя изменен'

#класс успешной смены пароля
class CUPasswordChangeDoneView(TemplateView):
        template_name = 'registration/password_change_done.html'

#класс регистрации пользователя
class CURegisterUserView(CreateView):
        model = CustomUser
        template_name = 'registration/register_user.html'
        form_class = RegisterUserForm
        success_url = reverse_lazy('account:register_done')


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
        return render(request, template)


# #Подписаться
# @login_required
# def user_subscription(request):
#         masters = Master.objects.filter(user=request.user)
#         organizations = Organization.objects.filter(user=request.user)
#         posts = AccountPost.objects.filter(user=request.user)
#         context = {
#             'masters': masters,
#             'organizations': organizations,
#             'posts':posts
#         }
#
#         return render(request, 'account/account.html', context)


def fun_sub(request):

    return HttpResponse("Hello Python")
    # Subscription.objects.create(subscriber = username, user = username)

