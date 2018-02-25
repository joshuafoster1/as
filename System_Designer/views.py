# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def SDhome(request):
    return render(request, 'SDhome.html', {'test':'test'})


def SD_load(request):
    form = 'test'
    return render(request, 'sd_load.html', {'test':'test','form': form})

def SD_preferences(request):
    form = 'test'

    return render(request, 'sd_preferences.html', {'test':'test', 'form': form})

def SD_install(request):
    form = 'test'
    return render(request, 'sd_install.html', {'test':'test', 'form': form})

def SD_summary(request):
    return render(request, 'sd_summary.html', {'test':'test'})

def SD_reccomendation(request):
    return render(request, 'sd_reccommendation.html', {'test':'test'})
