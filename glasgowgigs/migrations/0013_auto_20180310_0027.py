# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-10 00:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('glasgowgigs', '0012_event_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='address',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='event_venue_address', to='glasgowgigs.Venue'),
        ),
    ]