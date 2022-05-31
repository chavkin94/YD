from django.contrib.auth.models import User
from django.db import models

from account.models import CustomUser
from master.models import Master


class Subscription(models.Model):
    subscriper = models.ForeignKey(CustomUser, related_name='subscriber', on_delete=models.PROTECT, verbose_name="Подписчик")
    user = models.ForeignKey(CustomUser, blank=True, related_name='user', null=True, on_delete=models.PROTECT, verbose_name="Пользователь")
    master = models.ForeignKey(Master, blank=True, on_delete=models.PROTECT, null=True, verbose_name="Мастер")

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'

