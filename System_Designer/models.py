# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models

# Create your models here.
### design profile allows for multiple profiles per user
class DesignProfile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)


    def battery_selection(self):
        '''
        take peak load and max load parameters and determine the Battery bank
        to meet customer needs
        '''
        pass

    def panel_selection(self):
        pass

class VehicleInstall(models.Model):
    design_profile=models.ForeignKey(DesignProfile, related_name='vehicle_install')
    vehicle_type=models.CharField(max_length=30)
    panel_type_preference = models.CharField(max_length=2)#f=fixed m=mounted b=both


### unique items that will contribute to peak load
class Accessory(models.Model):
    accessory = models.CharField(max_length=30)
    wattage = models.IntegerField()
    amperes = models.IntegerField()
    ac_dc = models.CharField(max_length=2)

### unique factors that play a role determining the overall system capacity
class Load(models.Model):
    design_profile = models.ForeignKey(DesignProfile, related_name='load')
    accessories = models.ManyToManyField(Accessory, through='LoadAccessory')
    days_autonomous = models.IntegerField()
    winter_camping = models.BooleanField() #default no?
    # latitude = ?
    vehicular_moves = models.IntegerField()

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
    accessory = models.ForeignKey(Accessory)
    estimated_usage = models.IntegerField()

### TODO: need preferences table plus potential ref tables
### TODO: need install option tables plus potential ref tables.
