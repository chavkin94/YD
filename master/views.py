from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, TemplateView, ListView

from .forms import *
from .models import *


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
        # context['rubrics'] = Rubric.objects.all()
        return context


class MasterUpdate(LoginRequiredMixin, UpdateView):
    form_class = MasterUpdateForm
    model = Master
    template_name = 'master/master_update.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'master'
    success_url = reverse_lazy('master:master_one_show')

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
