# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from .forms import *
from .models import *
from .tables import *
from django_tables2 import RequestConfig

# Create your views here.
def get_customer(request):
    pk = request.user.pk
    customer = Customer.objects.get(user__pk=pk)
    return customer

def get_user_DPs(request):
    pk = request.user.pk
    user_DP = DesignProfile.objects.filter(user__pk=pk)
    return user_DP

def get_current_user_DP(request):
    pk = request.user.pk
    user_DP = get_object_or_404(UserDesignProfile, user__pk=pk)
    return user_DP


def SDhome(request):
    return render(request, 'System_Designer/SDhome.html', {'test':'test'})


def SD_load(request):
    customer = get_customer(request)
    connect_to_load = customer.current_design_profile
    customer.battery_selection()
    if request.method == 'POST':
        form = LoadAccessoryForm(request.POST,user_pk = customer.pk)
        if form.is_valid():
            load_form = form.save(commit=False)
            load_form.load, created = Load.objects.get_or_create(design_profile=DesignProfile.objects.get(name=connect_to_load))
            load_form.save()
            return redirect('SD_load')
    else:
        form = LoadAccessoryForm(user_pk = customer.pk)

    batteries = customer.battery_selection()
    batteries_dict = batteries['df'].to_dict('records')
    table2 = BatteryCountTable(batteries_dict, extra_columns=[(key, tables.Column()) for key in batteries_dict[0].keys()])
    table_data = LoadAccessory.objects.all().filter(load__design_profile__name=connect_to_load)
    table = AccessoryTable(table_data)
    RequestConfig(request).configure(table)

    return render(request, 'System_Designer/sd_load.html', {'table': table, 'table2':table2, 'test':'test','form': form})

def SD_recommendation(request):
    '''
    BD- attempted to mimic the load page to return the table appropriately and work backwords, but i'm missing something.
    if the tables are added in the sd_recommendations.html file, it breaks
    '''
    customer = get_customer(request)
    connect_to_load = customer.current_design_profile
    customer.battery_selection()
    if request.method == 'POST':
        form = LoadAccessoryForm(request.POST,user_pk = customer.pk)
        if form.is_valid():
            load_form = form.save(commit=False)
            load_form.load, created = Load.objects.get_or_create(design_profile=DesignProfile.objects.get(name=connect_to_load))
            load_form.save()
            return redirect('SD_load')
    else:
        form = LoadAccessoryForm(user_pk = customer.pk)

    batteries = customer.battery_selection()
    batteries_dict = batteries['df'].to_dict('records')
    table2 = BatteryCountTable(batteries_dict, extra_columns=[(key, tables.Column()) for key in batteries_dict[0].keys()])
    table_data = LoadAccessory.objects.all().filter(load__design_profile__name=connect_to_load)
    table = AccessoryTable(table_data)
    RequestConfig(request).configure(table)

    return render(request, 'System_Designer/sd_recommendation.html', {'table': table, 'table2':table2, 'test':'test','form': form})

def create_custom_accessory(request):
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


def SD_preferences(request):
    customer = get_customer(request)
    connect_to_load = customer.current_design_profile

    if request.method == 'POST':
        form = SystemDesignerPreferencesForm(request.POST)
        if form.is_valid():
            pref_form = form.save(commit=False)
            pref_form.save()
            return redirect('SD_preferences')
    else:
        form = SystemDesignerPreferencesForm()
    return render(request, 'System_Designer/sd_preferences.html', {'test':'test', 'form': form})


def SD_install(request):
    form = 'test'
    return render(request, 'System_Designer/sd_install.html', {'test':'test', 'form': form})

def SD_summary(request):
    customer = get_customer(request)
    if request.method == 'POST':
        form = ProfileForm(request.POST, user_pk = customer.user.pk)
        if form.is_valid():
            customer.current_design_profile = form.cleaned_data['profile_name']
            customer.save()
            return redirect('SD_load')
    else:
        form = ProfileForm(user_pk = customer.user.pk)
    return render(request, 'System_Designer/sd_summary.html', {'form': form})

def create_DP(request):
    customer = get_customer(request)

    if request.method == 'POST':
        form = CreateDesignProfileForm(request.POST)
        if form.is_valid():
            new_DP = form.save(commit=False)
            new_DP.user = User.objects.get(pk = customer.user.pk)
            new_DP.save()
            customer.current_design_profile = new_DP
            customer.save()
            return redirect('SD_load')
    else:
        form = CreateDesignProfileForm()
    return render(request, 'System_Designer/create_DP.html', {'form': form})

def SD_recomendation(request):
    return render(request, 'System_Designer/sd_recommendation.html', {'test':'test'})

def SD_locations(request):
    return render(request, 'System_Designer/sd_locations.html', {'test':'test'})

def custom_accessory(request):
    if request.method =='POST':
        form = CustomAccessoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('SD_load')
    else:
        form=CustomAccessoryForm()
    return render(request, 'System_Designer/create_DP.html', {'form':form})
