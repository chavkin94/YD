from django.db import models
from django.urls import reverse

from account.models import CustomUser
from main.models import Location


class Master(models.Model):
    name = models.CharField(max_length=255, blank=True, verbose_name="Имя мастера")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    location = models.ForeignKey(Location, blank=True, on_delete=models.PROTECT, verbose_name="Расположение")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    phone_number = models.CharField(max_length=30, verbose_name="Номер телефона", blank=True, null=True)
    is_activated = models.BooleanField(default=True, db_index=True, verbose_name='Активное')
    email = models.EmailField(blank=True, verbose_name="email")
    start_year = models.DateField(verbose_name="Год начала работы")
    description = models.TextField(blank=True, verbose_name="Описание мастера")
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT, verbose_name="Пользователь")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('master:master_one_show', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Мастер'
        verbose_name_plural = 'Мастера'
