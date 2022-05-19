from django.db import models
from django.urls import reverse

from account.models import CustomUser


class Organization(models.Model):
    name = models.CharField(max_length=255, blank=True, verbose_name="Наименование организации")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    location = models.CharField(max_length=255, blank=True, verbose_name="Расположение")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    phone_number = models.CharField(max_length=30, verbose_name="Номер телефона", blank=True, null=True)
    is_activated = models.BooleanField(default=True, db_index=True, verbose_name='Активное')
    email = models.EmailField(blank=True, verbose_name="email")
    description = models.TextField(blank=True, verbose_name="Описание организации")
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT, verbose_name="Пользователь")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('organization:organization_one_show', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'


class OrganizationCategory(models.Model):
    name = models.CharField(max_length=255, blank=True, verbose_name="Наименование категории организации")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    description = models.TextField(blank=True, verbose_name="Описание категории организации")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория организации'
        verbose_name_plural = 'Категории организаций'


class COrganizationAndOrganizationCategory(models.Model):
    FKOrganizationCategory = models.ForeignKey(OrganizationCategory, on_delete=models.PROTECT, verbose_name="Категория Организации")
    FKOrganization = models.ForeignKey(Organization, on_delete=models.PROTECT, verbose_name="Организация")

    class Meta:
        verbose_name = 'Связь Организация и Категория организации'
        verbose_name_plural = 'Связь Организация и Категория организации'
