# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-04 05:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('System_Designer', '0003_auto_20180303_2054'),
    ]

    operations = [
        migrations.AddField(
            model_name='designprofile',
            name='profile_name',
            field=models.CharField(default='test', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='designprofile',
            name='system_level',
            field=models.CharField(blank=True, choices=[(1, 'Silver'), (2, 'Gold'), (3, 'Platinum')], max_length=10),
        ),
    ]