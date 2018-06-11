# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-10 00:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('System_Designer', '0013_preferences'),
    ]

    operations = [
        migrations.AddField(
            model_name='preferences',
            name='design_profile',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='prefferences', to='System_Designer.DesignProfile'),
            preserve_default=False,
        ),
    ]
