# Generated by Django 3.2.6 on 2021-10-07 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0015_auto_20211007_0951'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stationmodel',
            name='station_name',
        ),
        migrations.AlterField(
            model_name='reportmodel',
            name='subject',
            field=models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, related_name='cat', to='report.stationmodel', verbose_name='مکان'),
        ),
        migrations.AlterField(
            model_name='stationmodel',
            name='mastername',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='name', to='report.stationmodel', verbose_name='زیر دسته'),
        ),
    ]