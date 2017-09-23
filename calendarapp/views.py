# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views.generic.base import TemplateView, View
from django.http import HttpResponse
from .forms import RegisterUserForm


# Create your views here.


class HomePageView(TemplateView):
    template_name = 'calendarapp/home.html'


class RegisterPageView(View):
    form_class = RegisterUserForm
    template_name = 'calendarapp/register.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):

        form = self.form_class(request.POST)

        if form.is_valid():

            student_group = form.save(commit=False)

            username = form.cleaned_data['username']

            student_group.username = username
            student_group.name = form.cleaned_data['name']
            student_group.email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            student_group.set_password(password)

            student_group.save()

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    # TODO: REDIRECT TO GOOD PAGE
                    return HttpResponse('success')

            #TODO: REDIRECT TO ERROR PAGE


class ForgotPasswordPageView(TemplateView):
    template_name = 'calendarapp/forgot-password.html'

class ProfilePageView(TemplateView):
    template_name = 'calendarapp/profile.html'


