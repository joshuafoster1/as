# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from .forms import *
from .models import *
from .tables import *
from django_tables2 import RequestConfig


### Global functions
def get_customer(request):
    """
    returns customer object.
    """

    pk = request.user.pk
    customer = Customer.objects.get(user__pk=pk)
    return customer

def get_user_DPs(request):
    """
    Returns all design profile objects for current user.
    """

    pk = request.user.pk
    user_DP = DesignProfile.objects.filter(user__pk=pk)
    return user_DP


### View functions
@login_required
def SDhome(request):
    """
    """

    return render(request, 'System_Designer/SDhome.html', {'test':'test'})

@login_required
def SD_load(request):
    """
    Contains form for accessory selection(LoadAccessoryForm), table for list of
    accessories (AccessoryTable). Serves to collect load information for user design
    profile. (Currently contains battery count table, may move to a different page)
    """


    customer = get_customer(request)
    connect_to_load = customer.current_design_profile
    if request.method == 'POST':
        form = LoadAccessoryForm(request.POST,user_pk = customer.pk)
        if form.is_valid():
            load_form = form.save(commit=False)
            load_form.load, created = Load.objects.get_or_create(design_profile=DesignProfile.objects.get(name=connect_to_load))
            load_form.save()
            return redirect('SD_load')
    else:
        form = LoadAccessoryForm(user_pk = customer.pk)

    table_data = LoadAccessory.objects.all().filter(load__design_profile__name=connect_to_load)
    table = AccessoryTable(table_data)
    RequestConfig(request).configure(table)

    return render(request, 'System_Designer/sd_load.html', {'table': table, 'test':'test','form': form}) # 'table2':table2,


def remove_accesory(request, pk):
    customer = get_customer(request)
    design_profile = customer.current_design_profile

    LoadAccessory.objects.filter(pk=pk).delete()

    return redirect('SD_load')


@login_required
def SD_recommendation(request):
    '''
    Need to define needs of the page. Currently mimics sd_load.
    '''

    customer = get_customer(request)
    connect_to_load = customer.current_design_profile
    customer.battery_selection()

    batteries = customer.battery_selection()
    batteries_dict = batteries['df'].to_dict('records')
    table = BatteryCountTable(
        batteries_dict,
        extra_columns=[(
            key,
            tables.Column(orderable=True)) for key in batteries['columns']])
    RequestConfig(request).configure(table)

    return render(request, 'System_Designer/sd_recommendation.html', {'table': table, 'test':'test'})
@login_required
def create_custom_accessory(request):
    """
    Simple view for custom accessory form. Assigns new acceessory to user.
    """

    customer = get_customer(request)

    if request.method == 'POST':
        form = CustomAccessoryForm(request.POST)
        if form.is_valid():
            custom_form = form.save(commit=False)
            custom_form.user_custom = customer
            custom_form.save()
            return redirect('SD_load')
    else:
        form = CustomAccessoryForm()
    return render(request, 'System_Designer/custom_accessory.html', {'test':'test','form': form})

@login_required
def SD_preferences(request):
    """
    Allow user to select preferences for design profile. Should assign preferences
    to the user. Designerpreferences model needs work...
    """

    customer = get_customer(request)
    current_DP = customer.current_design_profile
    preferences, created = Preferences.objects.get_or_create(design_profile = current_DP)
    if request.method == 'POST':
        form = SystemDesignerPreferencesForm(request.POST, instance = preferences)
        if form.is_valid():
            pref_form = form.save(commit=False)
            pref_form.save()
            return redirect('SD_install')
    else:
        form = SystemDesignerPreferencesForm(instance = preferences)
    return render(request, 'System_Designer/sd_preferences.html', {'test':'test', 'form': form})

@login_required
def SD_install(request):
    """
    """

    form = 'test'
    return render(request, 'System_Designer/sd_install.html', {'test':'test', 'form': form})
@login_required
def SD_summary(request):
    """
    User chooses design profile to work on from the user's design profiles.
    """

    customer = get_customer(request)

    if request.method == 'POST':
        form = ProfileForm(request.POST, user_pk = customer.user.pk)
        if form.is_valid():
            customer.current_design_profile = form.cleaned_data['current_design_profile']
            customer.save()
            return redirect('SD_load')
    else:
        form = ProfileForm(user_pk = customer.user.pk, initial = {'current_design_profile':customer.current_design_profile})
    return render(request, 'System_Designer/sd_summary.html', {'form': form, 'design_profile': customer.current_design_profile})

@login_required
def create_DP(request):
    """
    Simple view to create a design profile (DP) and assign to user. The user may
    have many DP's.
    """

    customer = get_customer(request)

    if request.method == 'POST':
        form = CreateDesignProfileForm(request.POST)
        if form.is_valid():
            new_DP = form.save(commit=False)
            if DesignProfile.objects.filter(name = new_DP.name, user = customer.user).exists():
                customer.current_design_profile = DesignProfile.objects.get(name = new_DP.name, user = customer.user)
            else:
                new_DP.user = User.objects.get(pk = customer.user.pk)
                new_DP.save()
                customer.current_design_profile = new_DP
            customer.save()
            return redirect('SD_load')
    else:
        form = CreateDesignProfileForm()
    return render(request, 'System_Designer/create_DP.html', {'form': form})
@login_required
def SD_recomendation(request):
    """
    """

    return render(request, 'System_Designer/sd_recommendation.html', {'test':'test'})
@login_required
def SD_locations(request):
    """
    """
    customer = get_customer(request)
    current_DP = customer.current_design_profile
    power_production, created = PowerProduction.objects.get_or_create(design_profile = current_DP)
    if request.method == 'POST':
        form = PowerProductionForm(request.POST, instance = power_production)
        if form.is_valid():
            pref_form = form.save(commit=False)
            pref_form.save()
            return redirect('SD_preferences')
    else:
        form = PowerProductionForm(instance = power_production)

    return render(request, 'System_Designer/sd_locations.html', {'test':'test', 'form': form})
@login_required
def custom_accessory(request):
    """
    JF - This appears to be a non/minimally functional duplicate of 'create_custom_accessory' view.
    """

    if request.method =='POST':
        form = CustomAccessoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('SD_load')
    else:
        form=CustomAccessoryForm()
    return render(request, 'System_Designer/create_DP.html', {'form':form})
