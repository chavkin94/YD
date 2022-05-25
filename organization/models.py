from django.db import models
from django.urls import reverse

from account.models import CustomUser
from main.models import Location
from datetime import datetime
from django.template.defaultfilters import slugify
from os.path import splitext


def image_url_main(instance, filename):
    slug = slugify(instance.user)
    slug_organization = slugify(instance.slug)
    year = datetime.now().year
    month = datetime.now().month
    day = datetime.now().day
    name1 = datetime.now().timestamp()
    name2 = splitext(filename)[1]
    return '%s/organization/%s/images_main/%s/%s/%s/%s%s' % (slug, slug_organization, year, month, day, name1, name2)


def image_url(instance, filename):
    slug = slugify(instance.organization.slug)
    slug_organization = slugify(instance.organization.user)
    year = datetime.now().year
    month = datetime.now().month
    day = datetime.now().day
    name1 = datetime.now().timestamp()
    name2 = splitext(filename)[1]
    return '%s/organization/%s/images/%s/%s/%s/%s%s' % (slug, slug_organization, year, month, day, name1, name2)


class Organization(models.Model):
    name = models.CharField(max_length=255, blank=False, verbose_name="Наименование организации")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    location = models.ForeignKey(Location, blank=True, on_delete=models.PROTECT, verbose_name="Расположение")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    phone_number = models.CharField(max_length=30, verbose_name="Номер телефона", blank=True, null=True)
    is_activated = models.BooleanField(default=True, db_index=True, verbose_name='Активное')
    email = models.EmailField(blank=True, verbose_name="email")
    description = models.TextField(blank=True, verbose_name="Описание организации")
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT, verbose_name="Пользователь")
    image = models.ImageField(blank=True, upload_to=image_url_main, verbose_name="Изображение")
    category = models.ManyToManyField('OrganizationCategory', verbose_name="Категория")

    def delete(self, *args, **kwargs):
        for ai in self.additionalimage_set.all():
            ai.delete()
        super().delete(*args, **kwargs)

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
    # ManyToManyField

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория организации'
        verbose_name_plural = 'Категории организаций'


class OrganizationPost(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.PROTECT, verbose_name="Организация")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="slug")
    title = models.CharField(max_length=100, verbose_name="Заголовок", blank=True, null=True)
    image = models.ImageField(blank=True, upload_to=image_url, verbose_name="Изображение")
    content = models.TextField(blank=True, verbose_name="Содержание")

    def delete(self, *args, **kwargs):
        for ai in self.additionalimage_set.all():
            ai.delete()
        super().delete(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('organization:organization_post', kwargs={'organization_slug': self.organization.slug, 'slug': self.slug})

    class Meta:
        verbose_name = 'Пост организации'
        verbose_name_plural = 'Посты организации'