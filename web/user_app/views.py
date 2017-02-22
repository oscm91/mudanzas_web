#!/usr/bin/python
#  -*- coding: utf-8 -*-

from django.shortcuts import render
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect

from .models import UserCreateForm
from django.core.context_processors import csrf

def LoginView(request):
    if request.method == 'POST':
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        url_host = request.META.get('HTTP_ORIGIN', settings.LOGIN_URL)

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(url_host)
        return redirect(settings.LOGIN_URL)

    logout(request)
    return render(request, 'user_app/login.html', {})

def LogoutView(request):
    logout(request)
    return redirect(settings.LOGIN_URL)

def RegisterView(request):
    logout(request)
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect(settings.LOGIN_URL)
            except Exception as e:
                pass

    return render(request, 'user_app/register.html', {})