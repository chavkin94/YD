# Generated by Django 3.1 on 2022-05-23 05:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AccountMainImage',
            new_name='AccountPost',
        ),
    ]