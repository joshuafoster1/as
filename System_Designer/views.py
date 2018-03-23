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
    user_DP = get_current_user_DP(request)
    connect_to_load = user_DP.profile_name
    print(user_DP)
    if request.method == 'POST':
        form = LoadAccessoryForm(request.POST)
        if form.is_valid():
            load_form = form.save(commit=False)
            load_form.load, created = Load.objects.get_or_create(design_profile=DesignProfile.objects.get(name=user_DP.profile_name))
            load_form.save()
            return redirect('SD_load')
    else:
        form = LoadAccessoryForm()
        table_data = LoadAccessory.objects.all().filter(load__design_profile__name=user_DP.profile_name)
        table = AccessoryTable(table_data)
        RequestConfig(request).configure(table)
    return render(request, 'System_Designer/sd_load.html', {'table': table, 'test':'test','form': form})

def SD_preferences(request):
    form = 'test'

    return render(request, 'System_Designer/sd_preferences.html', {'test':'test', 'form': form})

def SD_install(request):
    form = 'test'
    return render(request, 'System_Designer/sd_install.html', {'test':'test', 'form': form})

def SD_summary(request):
    user_DPs = get_user_DPs(request)
    user_DP = get_current_user_DP(request)
    print(user_DP.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, user_pk = user_DP.user.pk)
        if form.is_valid():
            user_DP.profile_name = form.cleaned_data['profile_name']
            user_DP.save()
            print(user_DP.user, user_DP)
            return redirect('SD_load')
    else:
        form = ProfileForm(user_pk = user_DP.user.pk)
    return render(request, 'System_Designer/sd_summary.html', {'form': form})

def create_DP(request):
    user_DP = get_current_user_DP(request)
    if request.method == 'POST':
        form = CreateDesignProfileForm(request.POST)
        if form.is_valid():
            new_DP = form.save(commit=False)
            new_DP.user = User.objects.get(pk = user_DP.user.pk)
            new_DP.save()
            user_DP.profile_name = new_DP
            user_DP.save()
            return redirect('SD_load')
    else:
        form = CreateDesignProfileForm()
    return render(request, 'System_Designer/create_DP.html', {'form': form})

def SD_recomendation(request):
    return render(request, 'System_Designer/sd_recommendation.html', {'test':'test'})

def SD_locations(request):
    return render(request, 'System_Designer/sd_locations.html', {'test':'test'})
