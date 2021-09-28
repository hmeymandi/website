# Generated by Django 3.2.6 on 2021-09-02 13:26

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('idcart', models.CharField(max_length=10, unique=True)),
                ('phone', models.CharField(max_length=11)),
                ('email', models.EmailField(blank=True, max_length=254, unique=True)),
                ('address', models.CharField(max_length=250)),
                ('shift', models.CharField(blank=True, choices=[(' A شیفت ', ' A شیفت '), (' B شیفت ', ' B شیفت '), (' C شیفت ', ' C شیفت ')], max_length=10, null=True)),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='کاربر عادی')),
                ('is_admin', models.BooleanField(default=False, verbose_name='مدیر')),
                ('is_authe', models.BooleanField(default=True, verbose_name='سرشیفت')),
                ('is_manager', models.BooleanField(default=False, verbose_name='سرپرست')),
                ('is_nazer', models.BooleanField(default=False, verbose_name='ناظر')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]