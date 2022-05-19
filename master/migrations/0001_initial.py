# Generated by Django 3.1 on 2022-05-19 05:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0007_location'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Master',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='Имя мастера')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Время изменения')),
                ('phone_number', models.CharField(blank=True, max_length=30, null=True, verbose_name='Номер телефона')),
                ('is_activated', models.BooleanField(db_index=True, default=True, verbose_name='Активное')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email')),
                ('start_year', models.DateField(verbose_name='Год начала работы')),
                ('description', models.TextField(blank=True, verbose_name='Описание мастера')),
                ('location', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='main.location', verbose_name='Расположение')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Мастер',
                'verbose_name_plural': 'Мастера',
            },
        ),
    ]