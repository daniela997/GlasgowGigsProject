# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-10 22:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glasgowgigs', '0027_auto_20180310_2144'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='info',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
