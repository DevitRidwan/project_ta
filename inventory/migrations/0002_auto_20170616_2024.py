# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-16 20:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='JenisItem',
            new_name='KategoriItem',
        ),
    ]