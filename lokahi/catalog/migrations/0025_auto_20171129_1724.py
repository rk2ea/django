# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-29 22:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0024_user_public_key'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='symm_key',
            new_name='public_key',
        ),
    ]
