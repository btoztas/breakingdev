# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime

from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView, View
from django.http import HttpResponse
from .forms import RegisterUserForm, RegisterEventForm
from django.contrib.auth.decorators import login_required


# Create your views here.


class HomePageView(TemplateView):
    template_name = 'calendarapp/home.html'


class HomePage2View(TemplateView):
    template_name = 'calendarapp/home2.html'


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


@method_decorator(login_required(login_url='/calendarapp/login/'), name='dispatch')
class ForgotPasswordPageView(TemplateView):
    template_name = 'calendarapp/forgot-password.html'


class ProfilePageView(TemplateView):
    template_name = 'calendarapp/profile.html'


@method_decorator(login_required(login_url='/calendarapp/login/'), name='dispatch')
class CreateEventView(View):
    template_name = 'calendarapp/createEvent.html'
    form_class = RegisterEventForm

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):

        form = self.form_class(request.POST)

        if form.is_valid():
            start_date = form.cleaned_data['date_start']
            end_date = form.cleaned_data['date_end']
            start_time = form.cleaned_data['time_start']
            end_time = form.cleaned_data['time_end']

            new_event = form.save(commit=False)
            user = request.user
            start = datetime.combine(start_date, start_time)
            end = datetime.combine(end_date, end_time)

            new_event.creator = user
            new_event.start = start
            new_event.end = end

            new_event.save()

            if new_event is not None:
                return HttpResponse('success')
