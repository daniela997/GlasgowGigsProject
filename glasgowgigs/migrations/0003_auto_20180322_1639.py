# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-22 16:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glasgowgigs', '0002_auto_20180321_2149'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='facebook',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='venue',
            name='info',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='venue',
            name='instagram',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='venue',
            name='twitter',
            field=models.URLField(blank=True),
        ),
    ]