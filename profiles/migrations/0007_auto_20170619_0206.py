# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-18 19:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_auto_20170618_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiles',
            name='tgl_lahir',
            field=models.DateField(default=datetime.date(2017, 6, 19)),
        ),
    ]
