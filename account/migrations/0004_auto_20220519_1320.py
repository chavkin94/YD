# Generated by Django 3.1 on 2022-05-19 04:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_location'),
        ('account', '0003_auto_20220519_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='location',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='main.location', verbose_name='Расположение'),
        ),
    ]