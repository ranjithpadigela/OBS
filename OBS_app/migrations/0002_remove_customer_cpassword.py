# Generated by Django 4.0.6 on 2022-07-21 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OBS_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='cpassword',
        ),
    ]