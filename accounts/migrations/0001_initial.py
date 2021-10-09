# Generated by Django 3.2.6 on 2021-10-09 21:15

from django.db import migrations, models
import django.db.models.manager
import django_jalali.db.models


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
                ('first_name', models.CharField(max_length=100, verbose_name='نام')),
                ('last_name', models.CharField(max_length=100, verbose_name='نام خانوادگی')),
                ('idcart', models.CharField(max_length=10, unique=True, verbose_name='شماره ملی(شناسه کاربری)')),
                ('phone', models.CharField(max_length=11, verbose_name='تلفن همراه')),
                ('email', models.EmailField(blank=True, max_length=254, unique=True, verbose_name='ایمیل')),
                ('address', models.CharField(max_length=250, verbose_name='آدرس')),
                ('shift', models.CharField(blank=True, choices=[(' A شیفت ', ' A شیفت '), (' B شیفت ', ' B شیفت '), (' C شیفت ', ' C شیفت ')], max_length=10, null=True, verbose_name='شیفت')),
                ('date', django_jalali.db.models.jDateField(null=True, verbose_name='تاریخ استخدام')),
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
