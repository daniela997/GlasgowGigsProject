# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-09 12:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glasgowgigs', '0004_auto_20180309_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='slug',
            field=models.SlugField(unique=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='slug',
            field=models.SlugField(unique=True),
        ),
        migrations.AlterField(
            model_name='venue',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
