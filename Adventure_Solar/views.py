# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def info(request):
    return render(request, 'info.html')

def store(request):
    return render(request, 'store.html')

