# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-05 00:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0047_auto_20171204_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='avatar',
            field=models.ImageField(default='report/pictures/no-pic.jpg', upload_to=''),
        ),
    ]
