from django.contrib.auth.models import AbstractUser
from django.db import models


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

    # class Meta(Abstractuser.Meta):
    #     pass
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'