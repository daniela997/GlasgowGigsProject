# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-21 14:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glasgowgigs', '0034_auto_20180321_1212'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='latitude',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='venue',
            name='longitude',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]