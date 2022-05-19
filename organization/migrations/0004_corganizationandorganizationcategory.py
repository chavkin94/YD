# Generated by Django 3.1 on 2022-05-19 03:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0003_auto_20220519_1056'),
    ]

    operations = [
        migrations.CreateModel(
            name='COrganizationAndOrganizationCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FKOrganization', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='organization.organization', verbose_name='Организация')),
                ('FKOrganizationCategory', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='organization.organizationcategory', verbose_name='Категория Организации')),
            ],
            options={
                'verbose_name': 'Связь Организация и Категория организации',
                'verbose_name_plural': 'Связь Организация и Категория организации',
            },
        ),
    ]