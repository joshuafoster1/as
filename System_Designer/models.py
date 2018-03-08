# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse, reverse_lazy

from django.db import models

# Create your models here.

### design profile allows for multiple profiles per user
class DesignProfile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    profile_name = models.CharField(max_length=50)
    system_level = models.CharField(max_length=10)

    #profile name -- we need to asign a name for the specific profile eg van, 4runner, etc...
    #load profile -- there will have to be an independent object with the loads for this vehicle. (a culmination of accessories)
    #variables for "options" set under the "preferences page. e.g. follows
        #batteryMonitoringSystem -- bool does this have a battery monitor
        #systemLevel -- Good, better, best; Silver, Gold, PLATNUM (this will effect cost directly)

    def battery_selection(self):
        '''
        take peak load and max load parameters and determine the Battery bank
        to meet customer needs
        '''
        pass

    def panel_selection(self):
        pass
###add lookup table for vehivcle type rough dimesion

class VehicleInstall(models.Model):
    design_profile=models.ForeignKey(DesignProfile, related_name='vehicle_install')
    vehicle_type=models.CharField(max_length=30) # make a foriegn key for table
    panel_type_preference = models.CharField(max_length=1)#f=fixed m=mounted b=both
    #mountingSpace = [L,W] to be used for calculating panel space

### unique items that will contribute to peak load
class Accessory(models.Model):
    accessory_name = models.CharField(max_length=30)
    draw_volts = models.IntegerField()
    draw_amps = models.IntegerField()
    draw_watts = models.IntegerField()
    ac_dc = models.BooleanField()

### unique factors that play a role determining the overall system capacity
class PowerProduction(models.Model):
    winter_camping = models.BooleanField() #default no?
    vehicular_moves = models.IntegerField() #directly tied to "isolator"
    #isolator -- boolean (does it charge while driving)
    #alternatorAmps -- output of the alternator (tied to isolator)
    #solar_panel -- this is gonna be the selected panel thats producing power
    #solar_panel2 -- incase there are two different sized panels
    #generator -- this is going to have to be its own product with lots of variables to calculate on, if blank we need to ignore it.
    #solarLocation -- this is going to be a singular variable designed around this map. /static/img/solarProductionMap.jpeg the user will click their "worst case area of travel" which will just spit back a number. (covering hours/day of sunlight, and insulation)



#the load functions as a "Profile" for the overall consumption of energy. Including the sum of
#all of the accessories and things like winter camping(time of year), location(latitude), and....maybe thats it?
class Load(models.Model):
    design_profile = models.ForeignKey(DesignProfile, related_name='load')
    accessories = models.ManyToManyField(Accessory, through='LoadAccessory') #for each, we want draw and ac_dc
    days_autonomous = models.IntegerField()


    def peak_load(self):
        '''
        Take all accesories and calculate the peak load potential for the system.

        BD - this will be used primarily to calculate if the battery bank can handle a full blown draw (dont want to
        exceed a @20hr draw rate) as well as if the inverter is of adequite size. (Inverter is ac only, may need to track those specifics of ac vs dc)
        '''
        pass

    def estimated_daily_Ah(self):
        '''
        Calculates the total amp*hours for all accessories to be used on the system.
        '''
        pass

    def estimated_recharge_capacity(self):
        '''
        estimate the likely recharge needs based on latitude, winter camoing potential
        vehicular moves.

        BD -- It may be wise to think about this more as "estimated recharge potential". Capacity will be a static amount based on battery selection.
        '''

### linking table for many to many relationship
class LoadAccessory(models.Model):
    load = models.ForeignKey(Load)
    accessory = models.ForeignKey(Accessory) #name
    estimated_usage = models.IntegerField() #usage as time in hrs/day
    quantity = models.IntegerField()

    #drawVolts
    #drawAmps
    #drawWatts these three will need to be able to be 2 of 3 input. then using W = V*A we can calculate the format we need.
    #number of units
    #def accessoryDraw -- this should be the primary output of the class.
    #accessoryAc_dc -- this will be the other output of the class.

# class Product(models.Model):    (is it wise to make this globally instead of within the system designer as i'll also be using it nearly exclusively for the store webApp?--we'll talk about how this works)
    #category [battery, panel, solarChargeController, inverter, charger, inverter/charger]
        #battery [ahCapacity, voltage, operatingTempRange, maxChargeCurrent, floatChargeVoltage, equalizationVoltage, temperatureCompensationFactor(for charging), terminalType, weight, dimensions[L, W, H] ]

        #module(panel) [peakPower(watts), nominalVoltage, maxVoltage, maxCurrent(amps), openCircuitVoltage, shortCircuitCurrent, maxSysVoltage, moduleEffeciency, dimensions[L, W, H], weight, connectorType, numberOfCells, operatingTemperatureRange[min, max]]

        #solarChargeController(sCC?) [conversionType(PWM or MPPT), maxBattCurrent, loadCurrentRating, openCircuitVoltage, peakEffieciency, batteryVoltageRange[min, max], voltageAccuracy, selfConsumption, surgeProtection, operatingTemperatureRange[min, max]
        #                               weight, dimensions[L, W, H], wireSizeIn, wireSizeOut, batteryTemperatureSensor, chargeModes[(dynamic list of modes?)]warranty, mfgPartNumber
        #                               accessories[groundFaultProtection, remoteTemperatureSensor, remoteMeter, communicationAdapter, meterHub, relayDriver, ]]

        #inverter [inverter(bool y/n), outputWattsContinuous, outputWattsSurge, outputCurrentContinuous, outputVoltageRange[min, max], outputFreqency, outputWaveform, effeciencyFullLoad, effeciencyPeak, noLoadDraw, offModeDraw, acInputVoltageRange[min, max]
        #           acTransferRelayAmps, inputVoltageRange[min, max] batteryVoltageNominal, lowBatteryCutout[low, mid, high] acRecepticles, operatingTemperatureRange[min, max] weight, dimensions[L, W, H] warranty, mfgPartNumber ]

        #charger [charger(bool y/n), dcOuputVoltage, outputAmperageContinuous, dcOutputVoltageFullLoad, maxPowerOutput(watts), inputVoltageRange[min, max], inputVoltageFrequency, maxAcCurrent, effenciency, operatingTemperatureRange[min, max] weight, dimensions[L, W, H] ]

        #inverterCharger


### TODO: need preferences table plus potential ref tables
### TODO: need install option tables plus potential ref tables
