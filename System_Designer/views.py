# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


# Create your views here.
def SDhome(request):
    return render(request, 'System_Designer/SDhome.html', {'test':'test'})


def SD_load(request):
    form = 'test'
    return render(request, 'System_Designer/sd_load.html', {'test':'test','form': form})

def SD_preferences(request):
    form = 'test'

    return render(request, 'System_Designer/sd_preferences.html', {'test':'test', 'form': form})

def SD_install(request):
    form = 'test'
    return render(request, 'System_Designer/sd_install.html', {'test':'test', 'form': form})

def SD_summary(request):
    return render(request, 'System_Designer/sd_summary.html', {'test':'test'})

def SD_recomendation(request):
    return render(request, 'System_Designer/sd_recommendation.html', {'test':'test'})

def SD_locations(request):
    return render(request, 'System_Designer/sd_locations.html', {'test':'test'})