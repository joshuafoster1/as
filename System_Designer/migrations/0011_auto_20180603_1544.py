# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-03 22:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('System_Designer', '0010_auto_20180530_0933'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='specSheet',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='cratetable',
            name='c_rate',
            field=models.FloatField(),
        ),
    ]
