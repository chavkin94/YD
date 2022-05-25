from django.contrib.auth.models import User
from django.db import models

from account.models import CustomUser
from master.models import Master


class Subscription(models.Model):
    subscriber = models.ForeignKey(CustomUser, related_name='subscriber', on_delete=models.PROTECT, verbose_name="Подписчик")
    user = models.ForeignKey(CustomUser, related_name='user', on_delete=models.PROTECT, verbose_name="Пользователь")
    master = models.ForeignKey(Master, on_delete=models.PROTECT, verbose_name="Мастер")

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'

