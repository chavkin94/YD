# Generated by Django 3.1 on 2022-05-19 04:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_location'),
        ('organization', '0004_corganizationandorganizationcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='location',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='main.location', verbose_name='Расположение'),
        ),
    ]
