# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-14 20:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_auto_20171114_1314'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='owner',
            field=models.CharField(default='admin', max_length=50),
        ),
    ]