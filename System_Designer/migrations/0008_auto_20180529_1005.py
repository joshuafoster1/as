# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-05-29 17:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('System_Designer', '0007_remove_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cratetable',
            name='ah_capacity',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
