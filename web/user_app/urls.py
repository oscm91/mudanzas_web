#!/usr/bin/python
#  -*- coding: utf-8 -*-

from django.conf.urls import url
from django.views.generic import TemplateView
from .views import LoginView, LogoutView, RegisterView

urlpatterns = [
    url(r'^login/$', LoginView, name='login'),
    url(r'^logout/$', LogoutView, name='logout'),
    url(r'^register/$', RegisterView, name='register'),
    url(r'^forgot/$', TemplateView.as_view(template_name = 'user_app/forgot.html'), name='forgot'),
]