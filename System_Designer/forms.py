from django import forms
from .models import *

class PowerProductionForm(forms.ModelForm):
    class Meta:
        model = PowerProduction
        fields = ['winter_camping', 'vehicular_moves']

class LoadAccessoryForm(forms.ModelForm):
    class Meta:
        model = LoadAccessory
        fields = ['accessory', 'estimated_usage', 'quantity']
