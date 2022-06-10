from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, TemplateView, ListView

from subscription.models import Subscription
from .forms import *
from .models import *

from django.core import serializers


class MasterAdd(LoginRequiredMixin, CreateView):
    form_class = MasterAddForm
    template_name = 'master/master_add.html'
    success_url = reverse_lazy('account:account')
    login_url = reverse_lazy('account:login')


class MasterOneShow(DetailView):
    model = Master
    template_name = 'master/master_one_show.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'master'

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = Service.objects.filter(master__slug=self.kwargs['slug'])
        context['posts'] = MasterPost.objects.filter(master__slug=self.kwargs['slug'])
        context['services'] = Service.objects.filter(master__slug=self.kwargs['slug'])
        context['user'] = self.request.user
        context['url_type'] = 'master'
        context['subscripe'] = None
        context['subscription_to_me'] = Subscription.objects.filter(master__slug=self.kwargs['slug'])
        context['subscription_count'] = context['subscription_to_me'].count()
        master = Master.objects.get(slug=self.kwargs['slug'])
        try:
            subscriper = CustomUser.objects.get(username=self.request.user)
            context['subscripe'] = Subscription.objects.get(subscriper=subscriper, master=master)
        except ObjectDoesNotExist:
            context['subscripe'] = None
        return context




class MasterUpdate(LoginRequiredMixin, UpdateView):
    form_class = MasterUpdateForm
    model = Master
    template_name = 'master/master_update.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'master'
    # success_url = reverse_lazy('master:master_one_show')

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class MasterAllShow(ListView):
    model = Master
    template_name = 'master/master_all_show.html'
    context_object_name = 'masters'

    def get_queryset(self):
        return Master.objects.all()

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


#Добавление поста
class PostAdd(LoginRequiredMixin, CreateView):
    model = MasterPost
    form_class = PostAddForm
    template_name = 'master/post_add.html'
    login_url = reverse_lazy('account:login')
    # initial = {'master':}

    def get_success_url(self):
        return reverse('master:master_one_show', kwargs={'slug': str(self.object.master.slug)})

    def get_initial(self):
        if Master.objects.get(slug=self.kwargs.get('slug')):
            initial = super(PostAdd, self).get_initial()
            initial['master'] = Master.objects.get(slug=self.kwargs.get('slug'))
            return initial

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context



#Просмотр поста
class PostShow(DetailView):
    model = MasterPost
    template_name = 'master/post.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'post'

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context



#Добавление услуги
class ServiceAdd(LoginRequiredMixin, CreateView):
    model = Service
    form_class = ServiceAddForm
    template_name = 'master/service_add.html'
    login_url = reverse_lazy('account:login')

    def get_success_url(self):
        return reverse('master:master_one_show', kwargs={'slug': str(self.object.master.slug)})

    def get_initial(self):
        if Master.objects.get(slug=self.kwargs.get('slug')):
            initial = super(ServiceAdd, self).get_initial()
            initial['master'] = Master.objects.get(slug=self.kwargs.get('slug'))
            return initial

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


#Просмотр услуги
class ServiceShow(DetailView):
    model = Service
    template_name = 'master/service.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'service'

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['master'] = Master.objects.get(slug=self.kwargs['master_slug'])
        return context


class ServiceUpdate(LoginRequiredMixin, UpdateView):
    form_class = ServiceUpdateForm
    model = Service
    template_name = 'master/service_update.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'service'
    # success_url = reverse_lazy('master:master_one_show')

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def post_one_show(request):
    data = request.GET
    current = Master.objects.get(slug=data.get('user_master_current_slug'))
    first_post_id = data.get('first_post_id')
    if first_post_id:
        # posts =MasterPost.objects.all().first()
        first_post = MasterPost.objects.get(pk=data.get('first_post_id'))
        posts = MasterPost.objects.filter(master=current, date_create__gt=first_post.date_create)[:4]
    else:
        posts = MasterPost.objects.filter(master=current)[:4]
    context = {
        'master': current,
        'posts': posts,
    }
    return render(request, 'master/post_one.html', context)