# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-23 13:10
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 23, 13, 10, 19, 547205, tzinfo=utc)),
        ),
    ]
