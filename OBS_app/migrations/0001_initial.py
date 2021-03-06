# Generated by Django 4.0.6 on 2022-07-20 15:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('bid', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200, null=True)),
                ('Author', models.CharField(max_length=200, null=True)),
                ('Price', models.DecimalField(decimal_places=4, max_digits=12)),
                ('Edition', models.IntegerField()),
                ('pub_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderid', models.IntegerField()),
                ('books', models.ManyToManyField(to='OBS_app.book')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=200, null=True)),
                ('cpassword', models.CharField(max_length=12, null=True)),
                ('cphone', models.CharField(max_length=200, null=True)),
                ('cemail', models.CharField(max_length=200, null=True)),
                ('cAddress', models.CharField(max_length=200, null=True)),
                ('cdate_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('books', models.ManyToManyField(to='OBS_app.book')),
                ('customer', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='OBS_app.customer')),
            ],
        ),
    ]
