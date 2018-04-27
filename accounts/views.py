# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from System_Designer.models import Customer

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            customer = Customer()
            customer.user = user
            customer.save()
            return redirect('splash')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
