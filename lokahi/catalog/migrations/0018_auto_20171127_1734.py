# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-27 22:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0017_auto_20171126_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='filename',
            field=models.FileField(upload_to=''),
        ),
    ]