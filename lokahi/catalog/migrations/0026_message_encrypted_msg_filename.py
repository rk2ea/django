# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-30 08:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0025_auto_20171129_1724'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='encrypted_msg_filename',
            field=models.FilePathField(null=True),
        ),
    ]
