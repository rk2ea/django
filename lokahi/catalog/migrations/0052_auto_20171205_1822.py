# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-05 23:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0051_auto_20171205_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='name',
            field=models.CharField(default='group', max_length=50, unique=True),
        ),
    ]
