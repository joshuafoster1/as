# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse, reverse_lazy

from django.db import models

# Create your models here.

### design profile allows for multiple profiles per user

class SystemLevel(models.Model):
    """
    Lookup table
    """
    level = models.CharField(max_length=20)

    def __str__(self):
        return self.level

class DesignProfile(models.Model):
    """
    This model is the container/tag that relates all associated elements for
    a system
    """

    name = models.CharField(max_length=50)
    system_level = models.ForeignKey(SystemLevel)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    current_design_profile = models.ForeignKey(DesignProfile, null=True, blank=True)

    def __str__(self):
        return self.user.username
class UserDesignProfile(models.Model):
    """
    This model holds in it's profile name value the current profile the
    user is working on
    """
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    profile_name = models.ForeignKey(DesignProfile)

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

    def __str__(self):
        return self.profile_name.name
###add lookup table for vehivcle type rough dimesion

class VehicleInstall(models.Model):
    design_profile=models.ForeignKey(DesignProfile, related_name='vehicle_install')
    vehicle_type=models.CharField(max_length=30) # make a foriegn key for table
    panel_type_preference = models.CharField(max_length=1)#f=fixed m=mounted b=both
    #mountingSpace = [L,W] to be used for calculating panel space

    def __str__(self):
        return self.vehicle_type
### unique items that will contribute to peak load
class Accessory(models.Model):
    """
    Lookup table for individual accessories
    """

    name = models.CharField(max_length=30)
    draw_volts = models.IntegerField()
    draw_amps = models.IntegerField()
    draw_watts = models.IntegerField()
    alternating_current = models.BooleanField()

    def __str__(self):
        return self.name

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
    days_autonomous = models.IntegerField()

    def total(self):
        return 'calcuted output'
    def __str__(self):
        return str(self.total())

#the load functions as a "Profile" for the overall consumption of energy. Including the sum of
#all of the accessories and things like winter camping(time of year), location(latitude), and....maybe thats it?
class Load(models.Model):
    """
    Linking model for many to many relationship of accessories to the design Profile
    """

    design_profile = models.ForeignKey(DesignProfile, related_name='load')
    accessories = models.ManyToManyField(Accessory, through='LoadAccessory') #for each, we want draw and ac_dc

    def __str__(self):
        return self.design_profile.profile_name.name + " Load"

    def get_accessory_amp_calcs(self):
        '''
        Take all accesories and calculate the peak load potential for the system.
        Calculates the total amp*hours for all accessories to be used on the system.

        Battery storage must be at minimum 2 x daily_Ah, but likely higher.

        BD - this will be used primarily to calculate if the battery bank can handle a full blown draw (dont want to
        exceed a @20hr draw rate) as well as if the inverter is of adequite size. (Inverter is ac only, may need to track those specifics of ac vs dc)
        '''

        accessories = list(LoadAccessory.objects.filter(load=self))

        peak_amps = 0
        dc_daily_Ah = 0
        ac_daily_Ah = 0
        for accessory in accesories:
            peak_amps += accessory.accessory.amps * accessory.quantity
            if accessory.accessory.alternating_current:
                ac_daily_Ah +=accessory.accessory.amps * accessory.estimated_usage * accessory.quantity
            else:
                daily_Ah += accessory.accessory.amps * accessory.estimated_usage * accessory.quantity
        daily_Ah = flt(ac_daily_Ah) * 120 / .9 + dc_daily_Ah

        return {'peak_amps': peak_amps, 'daily_AH':daily_Ah}


    def estimated_recharge_potential(self):
        '''
        estimate the likely recharge needs based on latitude, winter camoing potential
        vehicular moves.

        BD -- It may be wise to think about this more as "estimated recharge potential". Capacity will be a static amount based on battery selection.
        '''

### linking table for many to many relationship
class LoadAccessory(models.Model):
    """
    Linking table for many to many relationship of accessories to load.
    """
    load = models.ForeignKey(Load)
    accessory = models.ForeignKey(Accessory) #name
    estimated_usage = models.IntegerField() #usage as time in hrs/day
    quantity = models.IntegerField()
    drawVoltage = models.DecimalField(max_digits=10, decimal_places=4, default=0, verbose_name='Voltage')
    drawAmperage = models.DecimalField(max_digits=10, decimal_places=4, default=0, verbose_name='Amps')
    drawWatts = models.DecimalField(max_digits=10, decimal_places=4, default=0, verbose_name='Watts')
    isAc = models.BooleanField(default=False, verbose_name='AC Load')

    def __str__(self):
        return self.load.design_profile.profile_name.name + ' ' + self.accessory.name

    #drawWatts these three will need to be able to be 2 of 3 input. then using W = V*A we can calculate the format we need.
    #number of units
    #def accessoryDraw -- this should be the primary output of the class.
    #accessoryAc_dc -- this will be the other output of the class.

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class Product(models.Model):
    ### We are going to need to normalize this model/table.
    ### THis means we need to hash out the details of how to organize the information
    ### and create a better table structure.

    #Create the primary product class that holds all of the BASIC and universal information
    category = models.ForeignKey(Category, related_name='ProductType') #[battery, panel, solarChargeController, inverter, charger, inverter/charger]
    name = models.CharField(max_length=200, db_index=True)
    brand = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    #image = models.ImageField(upload_to='#', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    weight = models.DecimalField(max_digits=6, decimal_places=2)
    length = models.DecimalField(max_digits=4, decimal_places=2)
    width = models.DecimalField(max_digits=4, decimal_places=2)
    height = models.DecimalField(max_digits=4, decimal_places=2)
    warranty = models.TextField(blank=True)
    mfgPartNumber = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    #Now creating subclasses which inherit all attributes from Product class
    #Add product type specific attributes
class batteryProduct(Product):

    ahCapacity = models.PositiveIntegerField()
    operatingVoltage = models.DecimalField(max_digits=4, decimal_places=1)
    operatingTempMax = models.DecimalField(max_digits=4, decimal_places=1)
    operatingTempMin = models.DecimalField(max_digits=4, decimal_places=1)
    chargingCurrentMax = models.DecimalField(max_digits=4, decimal_places=1)
    chargingCurrentFloat = models.DecimalField(max_digits=4, decimal_places=1)
    chargingCurrentEqualize = models.DecimalField(max_digits=4, decimal_places=1)
    chargingTempCompensation = models.DecimalField(max_digits=4, decimal_places=2)
    terminalType = models.CharField(max_length=200)


    def __str__(self):
        return self.name

class moduleProduct(Product):

    peakOutputWatts = models.IntegerField()
    operatingVoltage = models.DecimalField(max_digits=4, decimal_places=1)
    peakOutputVoltage = models.DecimalField(max_digits=4, decimal_places=1)
    peakOutputCurrent = models.DecimalField(max_digits=4, decimal_places=1)
    openCircuitVoltage = models.DecimalField(max_digits=4, decimal_places=1)
    shortCircuitCurrent = models.DecimalField(max_digits=4, decimal_places=1)
    maxSystemVoltage = models.DecimalField(max_digits=5, decimal_places=1)
    moduleEffeciency = models.DecimalField(max_digits=4, decimal_places=2)
    connectorType = models.CharField(max_length=200)
    numberOfCells = models.IntegerField()
    operatingTempMax = models.DecimalField(max_digits=4, decimal_places=1)
    operatingTempMin = models.DecimalField(max_digits=4, decimal_places=1)
    wireSizeOut = models.DecimalField(max_digits=4, decimal_places=1)

    def __str__(self):
        return self.name

class chargeControllerProduct(Product):

    conversionType = models.CharField(max_length=200)
    maxBattCurrent = models.DecimalField(max_digits=4, decimal_places=1)
    loadCurrentRating = models.DecimalField(max_digits=4, decimal_places=1)
    openCircuitVoltage = models.DecimalField(max_digits=4, decimal_places=1)
    peakEffieciency = models.DecimalField(max_digits=4, decimal_places=1)
    batteryVoltageMin = models.DecimalField(max_digits=4, decimal_places=1)
    batteryVoltageMax = models.DecimalField(max_digits=4, decimal_places=1)
    voltageAccuracy = models.DecimalField(max_digits=4, decimal_places=1)
    selfConsumption = models.DecimalField(max_digits=4, decimal_places=1)
    surgeProtection = models.BooleanField(default=True)
    operatingTempMax = models.DecimalField(max_digits=4, decimal_places=1)
    operatingTempMin = models.DecimalField(max_digits=4, decimal_places=1)
    wireSizeIn = models.DecimalField(max_digits=4, decimal_places=1)
    wireSizeOut = models.DecimalField(max_digits=4, decimal_places=1)
    batteryTemperatureSensor = models.BooleanField(default=True)
    chargeModes = models.CharField(max_length=200)

    #accessories[groundFaultProtection, remoteTemperatureSensor, remoteMeter, communicationAdapter, meterHub, relayDriver ]

class inverterProduct(Product):

    outputWattsContinuous = models.DecimalField(max_digits=4, decimal_places=1)
    outputWattsSurge = models.DecimalField(max_digits=4, decimal_places=1)
    outputCurrentContinuous = models.DecimalField(max_digits=4, decimal_places=1)
    outputVoltageMin = models.DecimalField(max_digits=4, decimal_places=1)
    outputVoltageMax = models.DecimalField(max_digits=4, decimal_places=1)
    outputFreqency = models.DecimalField(max_digits=4, decimal_places=1)
    outputWaveform = models.CharField(max_length=200)
    effeciencyFullLoad = models.DecimalField(max_digits=4, decimal_places=1)
    effeciencyPeak = models.DecimalField(max_digits=4, decimal_places=1)
    noLoadDraw = models.DecimalField(max_digits=4, decimal_places=1)
    offModeDraw = models.DecimalField(max_digits=4, decimal_places=1)
    acInputVoltageMin = models.DecimalField(max_digits=4, decimal_places=1)
    acInputVoltageMax = models.DecimalField(max_digits=4, decimal_places=1)
    acTransferRelayAmps = models.DecimalField(max_digits=4, decimal_places=1)
    inputVoltageMin = models.DecimalField(max_digits=4, decimal_places=1)
    inputVoltageMax = models.DecimalField(max_digits=4, decimal_places=1)
    batteryVoltageNominal = models.DecimalField(max_digits=4, decimal_places=1)
    lowBatteryCutoutLow = models.DecimalField(max_digits=4, decimal_places=1)
    lowBatteryCutoutMid = models.DecimalField(max_digits=4, decimal_places=1)
    lowBatteryCutoutHigh = models.DecimalField(max_digits=4, decimal_places=1)
    acRecepticles = models.BooleanField(default=True)
    operatingTempMax = models.DecimalField(max_digits=4, decimal_places=1)
    operatingTempMin = models.DecimalField(max_digits=4, decimal_places=1)


    def __str__(self):
        return self.name

class chargerProduct(Product):

    dcOuputVoltage = models.DecimalField(max_digits=4, decimal_places=1)
    outputAmperageContinuous = models.DecimalField(max_digits=4, decimal_places=1)
    dcOutputVoltageFullLoad = models.DecimalField(max_digits=4, decimal_places=1)
    maxPowerOutput = models.DecimalField(max_digits=4, decimal_places=1)
    inputVoltageMin = models.DecimalField(max_digits=4, decimal_places=1)
    inputVoltageMax = models.DecimalField(max_digits=4, decimal_places=1)
    inputVoltageFrequency = models.IntegerField()
    maxAcCurrent = models.DecimalField(max_digits=4, decimal_places=1)
    effeciency = models.DecimalField(max_digits=4, decimal_places=1)
    operatingTempMax = models.DecimalField(max_digits=4, decimal_places=1)
    operatingTempMin = models.DecimalField(max_digits=4, decimal_places=1)

    def __str__(self):
        return self.name

class inverterChargerProduct(Product):

    outputWattsContinuous = models.DecimalField(max_digits=4, decimal_places=1)
    outputWattsSurge = models.DecimalField(max_digits=4, decimal_places=1)
    outputCurrentContinuous = models.DecimalField(max_digits=4, decimal_places=1)
    outputVoltageMin = models.DecimalField(max_digits=4, decimal_places=1)
    outputVoltageMax = models.DecimalField(max_digits=4, decimal_places=1)
    outputFreqency = models.DecimalField(max_digits=4, decimal_places=1)
    outputWaveform = models.CharField(max_length=200)
    effeciencyFullLoad = models.DecimalField(max_digits=4, decimal_places=1)
    effeciencyPeak = models.DecimalField(max_digits=4, decimal_places=1)
    noLoadDraw = models.DecimalField(max_digits=4, decimal_places=1)
    offModeDraw = models.DecimalField(max_digits=4, decimal_places=1)
    acInputVoltageMin = models.DecimalField(max_digits=4, decimal_places=1)
    acInputVoltageMax = models.DecimalField(max_digits=4, decimal_places=1)
    acTransferRelayAmps = models.DecimalField(max_digits=4, decimal_places=1)
    inputVoltageMin = models.DecimalField(max_digits=4, decimal_places=1)
    inputVoltageMax = models.DecimalField(max_digits=4, decimal_places=1)
    batteryVoltageNominal = models.DecimalField(max_digits=4, decimal_places=1)
    lowBatteryCutoutLow = models.DecimalField(max_digits=4, decimal_places=1)
    lowBatteryCutoutMid = models.DecimalField(max_digits=4, decimal_places=1)
    lowBatteryCutoutHigh = models.DecimalField(max_digits=4, decimal_places=1)
    acRecepticles = models.BooleanField(default=True)
    operatingTempMax = models.DecimalField(max_digits=4, decimal_places=1)
    operatingTempMin = models.DecimalField(max_digits=4, decimal_places=1)
    dcOuputVoltage = models.DecimalField(max_digits=4, decimal_places=1)
    outputAmperageContinuous = models.DecimalField(max_digits=4, decimal_places=1)
    dcOutputVoltageFullLoad = models.DecimalField(max_digits=4, decimal_places=1)
    maxPowerOutput = models.DecimalField(max_digits=4, decimal_places=1)
    inputVoltageFrequency = models.IntegerField()
    maxAcCurrent = models.DecimalField(max_digits=4, decimal_places=1)
    effeciency = models.DecimalField(max_digits=4, decimal_places=1)

    def __str__(self):
        return self.name



### TODO: need preferences table plus potential ref tables
### TODO: need install option tables plus potential ref tables
