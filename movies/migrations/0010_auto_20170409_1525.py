# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-09 12:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0009_auto_20170409_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='dvd_release_date',
            field=models.DateField(default=datetime.datetime(2017, 4, 9, 12, 25, 39, 873553, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='movie',
            name='dvd_release_date_status',
            field=models.CharField(choices=[('NA', 'N/A'), ('NF', 'not received'), ('R', 'valid date received')], default='NF', max_length=2),
        ),
    ]
