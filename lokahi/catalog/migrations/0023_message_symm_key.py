# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-28 23:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0022_auto_20171128_1833'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='symm_key',
            field=models.TextField(default='default'),
            preserve_default=False,
        ),
    ]
