# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-01 19:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0031_auto_20171201_1346'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='group_reports',
        ),
        migrations.AddField(
            model_name='group',
            name='reports',
            field=models.CharField(default='', max_length=200),
        ),
    ]
