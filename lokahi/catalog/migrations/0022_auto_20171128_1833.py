# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-28 23:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0021_comment_is_encrypted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='is_encrypted',
        ),
        migrations.AddField(
            model_name='message',
            name='is_encrypted',
            field=models.BooleanField(default=False),
        ),
    ]
