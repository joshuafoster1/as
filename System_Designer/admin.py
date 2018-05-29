# -*- coding: utf-8 -*-
# created super user, Username: admin Password: admin123

from __future__ import unicode_literals
from import_export.admin import ImportExportModelAdmin

from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Accessory)
class AccessoryAdmin(ImportExportModelAdmin):
    pass

@admin.register(batteryProduct)
class ProductAdmin(ImportExportModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    pass

@admin.register(LoadAccessory)
class LoadAccessoryAdmin(ImportExportModelAdmin):
    pass

@admin.register(Load)
class LoadAdmin(ImportExportModelAdmin):
    pass

@admin.register(PowerProduction)
class PowerProductionAdmin(ImportExportModelAdmin):
    pass

@admin.register(VehicleInstall)
class VehicleInstallAdmin(ImportExportModelAdmin):
    pass

@admin.register(UserDesignProfile)
class UserDesignProfileAdmin(ImportExportModelAdmin):
    pass

@admin.register(DesignProfile)
class DesignProfileAdmin(ImportExportModelAdmin):
    pass

@admin.register(SystemLevel)
class SystemLevelAdmin(ImportExportModelAdmin):
    pass

@admin.register(Customer)
class CustomerAdmin(ImportExportModelAdmin):
    pass

@admin.register(CRateTable)
class CRateTableAdmin(ImportExportModelAdmin):
    pass

@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    pass
