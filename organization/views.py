from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from .forms import OrganizationForm
from .models import *

class OrganizationAdd(LoginRequiredMixin, CreateView):
    form_class = OrganizationForm
    template_name = 'organization/organization_add.html'
    success_url = reverse_lazy('account:account')
    login_url = reverse_lazy('account:login')
    # model = Organization
    # raise_exception = True  # если мы не хотим перенапровлять неавторизованного пользователя, а хотим отображать 403 (доступ запрещен), можно без него


class OrganizationOneShow(DetailView):
    model = Organization
    template_name = 'organization/organization_one_show.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'organization'

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['rubrics'] = Rubric.objects.all()
        return context
