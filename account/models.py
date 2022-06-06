from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

from main.models import Location
from datetime import datetime
from django.template.defaultfilters import slugify
from os.path import splitext


def image_url_main(instance, filename):
    slug = slugify(instance.username)
    year = datetime.now().year
    month = datetime.now().month
    day = datetime.now().day
    name1 = datetime.now().timestamp()
    name2 = splitext(filename)[1]
    return 'account/%s/images_main/%s/%s/%s/%s%s' % (slug, year, month, day, name1, name2)


def image_url(instance, filename):
    slug = slugify(instance.user)
    year = datetime.now().year
    month = datetime.now().month
    day = datetime.now().day
    name1 = datetime.now().timestamp()
    name2 = splitext(filename)[1]
    return 'account/%s/images/%s/%s/%s/%s%s' % (slug, year, month, day, name1, name2)


class CustomUser(AbstractUser):
    gender = [
        (None, 'Выберите пол'),
        ('m', 'мужской'),
        ('w', 'женский'),
    ]
    surname = models.CharField(max_length=30, verbose_name="Отчество", blank=True, null=True)
    gender = models.CharField(max_length=30, choices=gender, blank=True,  verbose_name="Пол", default=None, null=True)
    birthday = models.DateField(verbose_name="Дата рождения", blank=True, null=True)
    phone_number = models.CharField(max_length=30, verbose_name="Номер телефона", blank=True, null=True)
    is_activated = models.BooleanField(default=True, db_index=True, verbose_name='Прошел активацию?')
    date_update = models.DateTimeField(auto_now=True, verbose_name='Дата изменения', null=True)
    image = models.ImageField(blank=True, upload_to=image_url_main, verbose_name="Изображение")
    # location = models.ForeignKey(Location, blank=True, on_delete=models.PROTECT, verbose_name="Расположение")

    def get_absolute_url(self):
        return reverse('account:account', kwargs={'username': self.username})

    def delete(self, *args, **kwargs):
        for ai in self.additionalimage_set.all():
            ai.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class AccountPost(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT, verbose_name="Пользователь")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="slug")
    title = models.CharField(max_length=100, verbose_name="Заголовок", blank=True, null=True)
    image = models.ImageField(blank=True, upload_to=image_url, verbose_name="Изображение")
    content = models.TextField(max_length=2048, blank=True, verbose_name="Содержание")
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания', null=True)
    date_update = models.DateTimeField(auto_now=True, verbose_name='Дата изменения', null=True)

    def delete(self, *args, **kwargs):
        for ai in self.additionalimage_set.all():
            ai.delete()
        super().delete(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('account:account_post', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Пост пользователя'
        verbose_name_plural = 'Посты пользователя'