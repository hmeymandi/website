# Generated by Django 3.2.6 on 2021-10-25 11:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models
import jdatetime


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='نام')),
                ('slug', models.SlugField(unique=True, verbose_name='آدرس')),
                ('status', models.BooleanField(default=True, verbose_name='نمایش ')),
                ('position', models.IntegerField(default=None, verbose_name='موقیعت')),
                ('device_name', models.ForeignKey(blank=True, max_length=75, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='device', to='report.devicemodel', verbose_name='نام بخش')),
            ],
            options={
                'verbose_name': 'نام تجهیز',
                'verbose_name_plural': 'نام تجهیز',
            },
        ),
        migrations.CreateModel(
            name='Informationmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='عنوان')),
                ('slug', models.CharField(max_length=100, unique=True)),
                ('status', models.BooleanField(default=True, verbose_name='نمایش')),
                ('position', models.IntegerField(verbose_name='موقیعت')),
            ],
            options={
                'verbose_name': 'اطلاعات',
                'verbose_name_plural': 'اطلاعات',
                'ordering': ['position'],
            },
        ),
        migrations.CreateModel(
            name='StationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titel', models.CharField(max_length=50, verbose_name='عنوان')),
                ('slug', models.SlugField(unique=True, verbose_name='آدرس')),
                ('status', models.BooleanField(default=True, verbose_name='نمایش ')),
                ('position', models.IntegerField(default=None, verbose_name='موقیعت')),
                ('mastername', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='name', to='report.stationmodel', verbose_name='زیر دسته')),
            ],
            options={
                'verbose_name': 'نام ایستگاه و مکان های مترو',
                'verbose_name_plural': 'نام ایستگاه و مکان های مترو',
            },
        ),
        migrations.CreateModel(
            name='Reportmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report', models.CharField(max_length=550, verbose_name='شرح خرابی')),
                ('date', django_jalali.db.models.jDateTimeField(default=jdatetime.datetime.now, verbose_name='تاریخ ثبت')),
                ('shift', models.CharField(choices=[('شیفت A', 'شیفت A'), ('شیفت B', 'شیفت B'), ('شیفت C', 'شیفت C')], max_length=50, null=True, verbose_name='شیفت')),
                ('acepet', models.CharField(choices=[('تایید نشده', 'تایید نشده'), ('تایید سر شیفت', 'تایید سر شیفت'), ('تایید نهایی', 'تایید نهایی')], default='تایید نشده', max_length=30, verbose_name='وضیعت')),
                ('slug', models.SlugField(blank=True, unique=True, verbose_name='آدرس گزارش')),
                ('numbercmms', models.CharField(default='ICT-', max_length=50, null=True, verbose_name='شماره دستور کار')),
                ('categ', models.ManyToManyField(related_name='info', to='report.Informationmodel', verbose_name='دسته بندیُ')),
                ('device', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='report.devicemodel', verbose_name='نام تجهیز')),
                ('subject', models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, related_name='cat', to='report.stationmodel', verbose_name='مکان')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='نام کاربری')),
            ],
            options={
                'verbose_name': 'گزارش',
                'verbose_name_plural': 'گزارش',
            },
        ),
    ]
