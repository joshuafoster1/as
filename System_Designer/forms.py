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
    def __init__(self, *args, **kwargs):
        user_pk = kwargs.pop('user_pk')
        super(LoadAccessoryForm, self).__init__(*args, **kwargs)
        self.fields['accessory'].queryset =Accessory.objects.filter(user_custom=None)|Accessory.objects.filter(user_custom__pk=user_pk)


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserDesignProfile
        fields = ['profile_name']
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['profile_name'].queryset =DesignProfile.objects.filter(user=user_pk)

class CreateDesignProfileForm(forms.ModelForm):
    class Meta:
        model = DesignProfile
        fields = ['name', 'system_level']

class CustomAccessoryForm(forms.ModelForm):
    class Meta:
        model = Accessory
        fields = ['name','draw_watts', 'draw_amperage', 'draw_voltage', 'is_Ac']

class SystemDesignerPreferencesForm(forms.ModelForm):

    class Meta:
        model = Preferences
        fields = ['days_autonomous', 'isolator', 'alternatorAmps', 'winterCamping', 'batteryMonitoringSystem']
#my gut tells me this needs to be linked to the UserDesignProfile here
