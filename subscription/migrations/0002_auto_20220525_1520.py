# Generated by Django 3.1 on 2022-05-25 06:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('subscription', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='subscriber',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='subscriber', to='account.customuser', verbose_name='Подписчик'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='subscription',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]