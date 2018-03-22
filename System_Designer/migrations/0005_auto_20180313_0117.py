# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-13 08:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('System_Designer', '0004_auto_20180303_2132'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('description', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock', models.PositiveIntegerField()),
                ('available', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('ahCapacity', models.PositiveIntegerField()),
                ('operatingVoltage', models.DecimalField(decimal_places=1, max_digits=4)),
                ('operatingTempMax', models.DecimalField(decimal_places=1, max_digits=4)),
                ('operatingTempMin', models.DecimalField(decimal_places=1, max_digits=4)),
                ('chargingCurrentMax', models.DecimalField(decimal_places=1, max_digits=4)),
                ('chargingCurrentFloat', models.DecimalField(decimal_places=1, max_digits=4)),
                ('chargingCurrentEqualize', models.DecimalField(decimal_places=1, max_digits=4)),
                ('chargingTempCompensation', models.DecimalField(decimal_places=2, max_digits=4)),
                ('terminalType', models.CharField(max_length=200)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=6)),
                ('length', models.DecimalField(decimal_places=2, max_digits=4)),
                ('width', models.DecimalField(decimal_places=2, max_digits=4)),
                ('height', models.DecimalField(decimal_places=2, max_digits=4)),
                ('peakOutputWatts', models.IntegerField()),
                ('peakOutputVoltage', models.DecimalField(decimal_places=1, max_digits=4)),
                ('peakOutputCurrent', models.DecimalField(decimal_places=1, max_digits=4)),
                ('openCircuitVoltage', models.DecimalField(decimal_places=1, max_digits=4)),
                ('shortCircuitCurrent', models.DecimalField(decimal_places=1, max_digits=4)),
                ('maxSystemVoltage', models.DecimalField(decimal_places=1, max_digits=5)),
                ('moduleEffeciency', models.DecimalField(decimal_places=2, max_digits=4)),
                ('connectorType', models.CharField(max_length=200)),
                ('numberOfCells', models.IntegerField()),
                ('conversionType', models.CharField(max_length=200)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ProductType', to='System_Designer.Category')),
            ],
        ),
        migrations.AlterField(
            model_name='designprofile',
            name='system_level',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='loadaccessory',
            name='estimated_usage',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='powerproduction',
            name='vehicular_moves',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='vehicleinstall',
            name='panel_type_preference',
            field=models.CharField(max_length=1),
        ),
    ]
