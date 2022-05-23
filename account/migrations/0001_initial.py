# Generated by Django 3.1 on 2022-05-22 05:59

import account.models
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('surname', models.CharField(blank=True, max_length=30, null=True, verbose_name='Отчество')),
                ('gender', models.CharField(blank=True, choices=[(None, 'Выберите пол'), ('m', 'мужской'), ('w', 'женский')], default=None, max_length=30, null=True, verbose_name='Пол')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
                ('phone_number', models.CharField(blank=True, max_length=30, null=True, verbose_name='Номер телефона')),
                ('is_activated', models.BooleanField(db_index=True, default=True, verbose_name='Прошел активацию?')),
                ('date_update', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата изменения')),
                ('image', models.ImageField(blank=True, upload_to=account.models.image_url_main, verbose_name='Изображение')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='AccountMainImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='slug')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='Заголовок')),
                ('image', models.ImageField(blank=True, upload_to=account.models.image_url, verbose_name='Изображение')),
                ('content', models.TextField(blank=True, verbose_name='Содержание')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Пост пользователя',
                'verbose_name_plural': 'Посты пользователя',
            },
        ),
    ]
