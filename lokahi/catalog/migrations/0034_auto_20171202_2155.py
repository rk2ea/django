# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-03 02:55
from __future__ import unicode_literals

import catalog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0033_message_sender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='sender',
            field=models.TextField(verbose_name=catalog.models.User),
        ),
    ]
