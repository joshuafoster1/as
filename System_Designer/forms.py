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

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserDesignProfile
        fields = ['profile_name']
    def __init__(self, *args, **kwargs):
        user_pk = kwargs.pop('user_pk')
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['profile_name'].queryset =DesignProfile.objects.filter(user=user_pk)
