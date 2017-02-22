#!/usr/bin/python
#  -*- coding: utf-8 -*-

'''
Customs Middleware
'''

from django.contrib.auth import authenticate, login

class AuthRequired(object):
    def process_request(self, request):

        return None