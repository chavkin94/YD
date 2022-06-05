import json

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.views.generic import UpdateView, CreateView, TemplateView, DetailView

from account.forms import ChangeUserInfoForm, RegisterUserForm, AccountPostAddForm, AccountSubscriptionForm
from account.models import CustomUser, AccountPost

from django.core.signing import BadSignature

from master.models import Master, MasterPost
from organization.models import Organization
from subscription.models import Subscription
from .utilities import signer
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator



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
        subscription_to_me = Subscription.objects.filter(user=request.user)
        subscription_my_user = Subscription.objects.filter(subscriper=request.user, master=None)
        subscription_my_master = Subscription.objects.filter(subscriper=request.user, user=None)
        feed_account = AccountPost.objects.filter(user__subscriber__user=request.user)
        feed_master = MasterPost.objects.filter(master__subscription__subscriper=request.user)
        feed = feed_account.union(feed_master).order_by('date_create')
        # posts = AccountPost.objects.filter(user=request.user)
        # posts_paginator = Paginator(posts_all, 1)
        # posts = posts_paginator.page(1)
        # posts = post_page.object_list
        context = {
            'masters': masters,
            'subscription_to_me': subscription_to_me,
            'subscription_my_user': subscription_my_user,
            'subscription_my_master': subscription_my_master,
            'organizations': organizations,
            'feed': feed,
            # 'posts': posts,
        }

        return render(request, 'account/account.html', context)

def post_one_show(request):
    data = request.GET
    current = CustomUser.objects.get(username=data.get('user_master_current_slug'))
    first_post_id = data.get('first_post_id')
    if first_post_id:
        posts =AccountPost.objects.all().first()
        first_post = AccountPost.objects.get(pk=data.get('first_post_id'))
        posts = AccountPost.objects.filter(user=current, date_create__gt=first_post.date_create)[:4]
    else:
        posts = AccountPost.objects.filter(user=current)[:4]
    context = {
        'posts': posts,
    }
    # account_post_one_show_json(post_end)
    return render(request, 'account/post_one.html', context)


    # return HttpResponse('<p>Here will be your HTML page</p>')
# def post_pagination_1(request,page):
#     masters = Master.objects.filter(user=request.user)
#     organizations = Organization.objects.filter(user=request.user)
#     posts_all = AccountPost.objects.filter(user=request.user)
#     posts_paginator = Paginator(posts_all, 1)
#     posts = posts_paginator.page(1)

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


#Просмотр другого пользователя
class AccountAnotherShow(DetailView):
    form_class = AccountSubscriptionForm
    model = CustomUser
    template_name = 'account/account_another.html'
    slug_field = 'username'
    slug_url_kwarg = 'slug'
    context_object_name = 'account'

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context['user'] = self.request.user
        context['url_type'] = 'account'
        context['subscripe'] = None
        context['subscription_to_me'] = Subscription.objects.filter(user__username=self.kwargs['slug'])
        context['subscription_my_user'] = Subscription.objects.filter(subscriper__username=self.kwargs['slug'], master=None)
        context['subscription_my_master'] = Subscription.objects.filter(subscriper__username=self.kwargs['slug'], user=None)




        user = CustomUser.objects.get(username=self.kwargs['slug'])
        try:
            subscriper = CustomUser.objects.get(username=self.request.user)
            context['subscripe'] = Subscription.objects.get(subscriper=subscriper, user=user)
        except ObjectDoesNotExist:
            context['subscripe'] = None
        return context

