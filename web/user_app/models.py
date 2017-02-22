#!/usr/bin/python
#  -*- coding: utf-8 -*-

from django.db import models

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)
    fullname = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["fullname"]
        if commit:
            user.save()
        return user