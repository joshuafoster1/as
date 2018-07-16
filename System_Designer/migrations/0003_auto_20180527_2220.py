# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-28 05:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('System_Designer', '0002_auto_20180527_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loadaccessory',
            name='drawAmperage',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=10, verbose_name='Amps'),
        ),
        migrations.AlterField(
            model_name='loadaccessory',
            name='drawVoltage',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=10, verbose_name='Voltage'),
        ),
        migrations.AlterField(
            model_name='loadaccessory',
            name='drawWatts',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=10, verbose_name='Watts'),
        ),
    ]