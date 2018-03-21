# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-21 21:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glasgowgigs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=7, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='venue',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=7, max_digits=10, null=True),
        ),
    ]