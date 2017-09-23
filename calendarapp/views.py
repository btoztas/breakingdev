# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib import messages
# Create your views here.

from django.views.generic.base import TemplateView
from django.http import HttpResponse

class HomePageView(TemplateView):
    template_name = 'calendarapp/index.html'

class LoginPageView(TemplateView):
    template_name = 'calendarapp/login.html'

class RegisterPageView(TemplateView):
    template_name = 'calendarapp/register.html'

class ForgotPasswordPageView(TemplateView):
    template_name = 'calendarapp/forgot-password.html'

class ProfilePageView(TemplateView):
    template_name = 'calendarapp/profile.html'


