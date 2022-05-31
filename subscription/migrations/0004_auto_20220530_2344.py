# Generated by Django 3.1 on 2022-05-30 14:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('master', '0002_service_servicecategory'),
        ('subscription', '0003_auto_20220526_1023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='master',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='master.master', verbose_name='Мастер'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
