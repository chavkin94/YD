# Generated by Django 3.1 on 2022-05-19 04:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_location'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='location',
            field=models.ForeignKey(blank=True, default=0, on_delete=django.db.models.deletion.PROTECT, to='main.location', verbose_name='Расположение'),
            preserve_default=False,
        ),
    ]