from django import forms
from .models import *

class PowerProductionForm(forms.ModelForm):
    class Meta:
        model = PowerProduction
        fields = ['winter_camping', 'vehicular_moves', 'sunlight_hours', 'insolation_multiplyer']


class LoadAccessoryForm(forms.ModelForm):
    """
    select accessory for association with a design profile. Pulls from all
    acccessories and custom accessories
    """
    class Meta:
        model = LoadAccessory
        fields = ['accessory', 'estimated_usage', 'quantity']

    def __init__(self, *args, **kwargs):
        user_pk = kwargs.pop('user_pk')
        super(LoadAccessoryForm, self).__init__(*args, **kwargs)
        # This line pulls general accessories and private custom accesssories for input user(user_pk)
        self.fields['accessory'].queryset = Accessory.objects.filter(user_custom=None) | Accessory.objects.filter(user_custom__pk=user_pk)


class ProfileForm(forms.ModelForm):
    """
    Select a design profile for input user (user_pk)
    """
    class Meta:
        model = Customer
        fields = ['current_design_profile']

    def __init__(self, *args, **kwargs):
        user_pk = kwargs.pop('user_pk')
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['current_design_profile'].queryset = DesignProfile.objects.filter(user=user_pk)


class CreateDesignProfileForm(forms.ModelForm):
    """
    Create new design profile. On form processing, the design profile is assigned
    to current user.
    """
    class Meta:
        model = DesignProfile
        fields = ['name', 'system_level']


class CustomAccessoryForm(forms.ModelForm):
    """
    Form to allow creation of a custom accessory. On form processing the acceessory
    is assigned to the current user.
    """
    class Meta:
        model = Accessory
        fields = ['name','draw_watts', 'draw_amperage', 'draw_voltage', 'is_Ac']


class SystemDesignerPreferencesForm(forms.ModelForm):

    class Meta:
        model = Preferences
        fields = ['days_autonomous', 'isolator', 'alternatorAmps', 'winterCamping', 'batteryMonitoringSystem']
#my gut tells me this needs to be linked to the UserDesignProfile here
