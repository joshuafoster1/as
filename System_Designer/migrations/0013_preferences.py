# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-10 00:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('System_Designer', '0012_batteryproduct_optimaldepthofdischarge'),
    ]

    operations = [
        migrations.CreateModel(
            name='Preferences',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days_autonomous', models.IntegerField(default=3)),
                ('isolator', models.BooleanField(default=False)),
                ('alternatorAmps', models.FloatField(default=90)),
                ('winterCamping', models.BooleanField(default=False)),
                ('batteryMonitoringSystem', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Preference',
                'verbose_name_plural': 'Preferences',
            },
        ),
    ]
