# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-03 02:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0032_auto_20171201_1410'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='sender',
            field=models.TextField(default='', help_text='Enter your username'),
            preserve_default=False,
        ),
    ]
