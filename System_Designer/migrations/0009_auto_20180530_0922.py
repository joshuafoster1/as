# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-05-30 16:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('System_Designer', '0008_auto_20180529_1005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessory',
            name='draw_amperage',
            field=models.FloatField(verbose_name='Amps'),
        ),
        migrations.AlterField(
            model_name='accessory',
            name='draw_voltage',
            field=models.FloatField(verbose_name='Voltage'),
        ),
        migrations.AlterField(
            model_name='accessory',
            name='draw_watts',
            field=models.FloatField(verbose_name='Watts'),
        ),
        migrations.AlterField(
            model_name='batteryproduct',
            name='chargingCurrentEqualize',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='batteryproduct',
            name='chargingCurrentFloat',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='batteryproduct',
            name='chargingCurrentMax',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='batteryproduct',
            name='chargingTempCompensation',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='batteryproduct',
            name='operatingTempMax',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='batteryproduct',
            name='operatingTempMin',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='batteryproduct',
            name='operatingVoltage',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='chargecontrollerproduct',
            name='batteryVoltageMax',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='chargecontrollerproduct',
            name='batteryVoltageMin',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='chargecontrollerproduct',
            name='loadCurrentRating',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='chargecontrollerproduct',
            name='maxBattCurrent',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='chargecontrollerproduct',
            name='openCircuitVoltage',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='chargecontrollerproduct',
            name='operatingTempMax',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='chargecontrollerproduct',
            name='operatingTempMin',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='chargecontrollerproduct',
            name='peakEffieciency',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='chargecontrollerproduct',
            name='selfConsumption',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='chargecontrollerproduct',
            name='voltageAccuracy',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='chargecontrollerproduct',
            name='wireSizeIn',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='chargecontrollerproduct',
            name='wireSizeOut',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='chargerproduct',
            name='dcOuputVoltage',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='chargerproduct',
            name='dcOutputVoltageFullLoad',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='chargerproduct',
            name='effeciency',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='chargerproduct',
            name='inputVoltageMax',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='chargerproduct',
            name='inputVoltageMin',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='chargerproduct',
            name='maxAcCurrent',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='chargerproduct',
            name='maxPowerOutput',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='chargerproduct',
            name='operatingTempMax',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='chargerproduct',
            name='operatingTempMin',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='chargerproduct',
            name='outputAmperageContinuous',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='cratetable',
            name='ah_capacity',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='inverterchargerproduct',
            name='acInputVoltageMax',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='inverterchargerproduct',
            name='acInputVoltageMin',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='inverterchargerproduct',
            name='acTransferRelayAmps',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='inverterchargerproduct',
            name='batteryVoltageNominal',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='inverterchargerproduct',
            name='dcOuputVoltage',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='inverterchargerproduct',
            name='dcOutputVoltageFullLoad',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='inverterchargerproduct',
            name='effeciency',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='inverterchargerproduct',
            name='effeciencyFullLoad',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='inverterchargerproduct',
            name='effeciencyPeak',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='inverterchargerproduct',
            name='inputVoltageMax',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='inverterchargerproduct',
            name='inputVoltageMin',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='inverterchargerproduct',
            name='lowBatteryCutoutHigh',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='inverterchargerproduct',
            name='lowBatteryCutoutLow',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='inverterchargerproduct',
            name='lowBatteryCutoutMid',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='inverterchargerproduct',
            name='maxAcCurrent',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='inverterchargerproduct',
            name='maxPowerOutput',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='inverterchargerproduct',
            name='noLoadDraw',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='inverterchargerproduct',
            name='offModeDraw',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='inverterchargerproduct',
            name='operatingTempMax',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='inverterchargerproduct',
            name='operatingTempMin',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='inverterchargerproduct',
            name='outputAmperageContinuous',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='inverterchargerproduct',
            name='outputCurrentContinuous',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='inverterchargerproduct',
            name='outputFreqency',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='inverterchargerproduct',
            name='outputVoltageMax',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='inverterchargerproduct',
            name='outputVoltageMin',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='inverterchargerproduct',
            name='outputWattsContinuous',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='inverterchargerproduct',
            name='outputWattsSurge',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='inverterproduct',
            name='acInputVoltageMax',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='inverterproduct',
            name='acInputVoltageMin',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='inverterproduct',
            name='acTransferRelayAmps',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='inverterproduct',
            name='batteryVoltageNominal',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='inverterproduct',
            name='effeciencyFullLoad',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='inverterproduct',
            name='effeciencyPeak',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='inverterproduct',
            name='inputVoltageMax',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='inverterproduct',
            name='inputVoltageMin',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='inverterproduct',
            name='lowBatteryCutoutHigh',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='inverterproduct',
            name='lowBatteryCutoutLow',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='inverterproduct',
            name='lowBatteryCutoutMid',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='inverterproduct',
            name='noLoadDraw',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='inverterproduct',
            name='offModeDraw',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='inverterproduct',
            name='operatingTempMax',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='inverterproduct',
            name='operatingTempMin',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='inverterproduct',
            name='outputCurrentContinuous',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='inverterproduct',
            name='outputFreqency',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='inverterproduct',
            name='outputVoltageMax',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='inverterproduct',
            name='outputVoltageMin',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='inverterproduct',
            name='outputWattsContinuous',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='inverterproduct',
            name='outputWattsSurge',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='moduleproduct',
            name='maxSystemVoltage',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='moduleproduct',
            name='moduleEffeciency',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='moduleproduct',
            name='openCircuitVoltage',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='moduleproduct',
            name='operatingTempMax',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='moduleproduct',
            name='operatingTempMin',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='moduleproduct',
            name='operatingVoltage',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='moduleproduct',
            name='peakOutputCurrent',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='moduleproduct',
            name='peakOutputVoltage',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='moduleproduct',
            name='shortCircuitCurrent',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='moduleproduct',
            name='wireSizeOut',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='height',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='length',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='weight',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='width',
            field=models.FloatField(),
        ),
    ]