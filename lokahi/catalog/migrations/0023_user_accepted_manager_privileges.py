# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-29 22:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0022_auto_20171129_1608'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='accepted_manager_privileges',
            field=models.BooleanField(default=False),
        ),
    ]