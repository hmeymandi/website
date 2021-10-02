# Generated by Django 3.2.6 on 2021-09-30 12:43

import datetime
from django.db import migrations, models
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0003_auto_20210930_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportmodel',
            name='date',
            field=django_jalali.db.models.jDateTimeField(default=datetime.datetime(2021, 9, 30, 16, 13, 14, 46899), verbose_name='تاریخ ثبت'),
        ),
        migrations.AlterField(
            model_name='reportmodel',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='آدرس گزارش'),
        ),
    ]