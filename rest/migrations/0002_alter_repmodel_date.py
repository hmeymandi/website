# Generated by Django 3.2.6 on 2021-09-30 10:36

import datetime
from django.db import migrations
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repmodel',
            name='date',
            field=django_jalali.db.models.jDateTimeField(default=datetime.datetime(2021, 9, 30, 14, 6, 4), null=True, verbose_name='تاریخ ثبت'),
        ),
    ]