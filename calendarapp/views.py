# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView, View
from django.http import HttpResponse
from schedule.models import Calendar, Event

from calendarapp.models import StudentGroup
from .forms import RegisterUserForm, RegisterEventForm, EditEventForm, EditProfileForm
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
            acro = form.cleaned_data['acro']

            student_group.username = username
            student_group.name = form.cleaned_data['name']
            student_group.email = form.cleaned_data['email']
            student_group.acro = acro
            password = form.cleaned_data['password']
            student_group.set_password(password)

            student_group.save()
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    # TODO: REDIRECT TO GOOD PAGE
                    return redirect("/calendarapp/profile/"+str(student_group.id))

            #TODO: REDIRECT TO ERROR PAGE

        return HttpResponse('not in if')


@method_decorator(login_required(login_url='/calendarapp/login/'), name='dispatch')
class ForgotPasswordPageView(TemplateView):
    template_name = 'calendarapp/forgot-password.html'


class ProfilePageView(TemplateView):
    template_name = 'calendarapp/profile.html'

    def get(self, request, *args, **kwargs):

        profile_id = kwargs['profile_id']
        student_group = StudentGroup.objects.filter(pk=profile_id).first()
        user = User.objects.filter(pk=profile_id).first()

        if user.is_superuser:
            return HttpResponse("Page not found")

        name = student_group.name
        description = student_group.description
        events = Event.objects.filter(creator=student_group).all()
        image_url = student_group.image.url
        return render(request, self.template_name, {
            'name': name,
            'description': description,
            'image': image_url,
            'event_list': events
        })


class GroupsList(TemplateView):
    template_name = 'calendarapp/groups-list.html'

    def get(self, request, *args, **kwargs):

        student_groups = StudentGroup.objects.all()

        return render(request, self.template_name, {
            'student_groups': student_groups
        })


class EventView(TemplateView):
    template_name = 'calendarapp/event.html'

    def get(self, request, *args, **kwargs):
        event_id = kwargs['event_id']

        event = Event.objects.filter(pk=event_id).first()

        title = event.title
        description = event.description

        return render(request, self.template_name, {
            'title': title,
            'description': description,
        })


@method_decorator(login_required(login_url='/calendarapp/login/'), name='dispatch')
class DashboardView(TemplateView):
    template_name = "calendarapp/fullcalendar.html"


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

            calendar = Calendar.objects.filter(slug='NUCLEOS').first()
            new_event.creator = user
            new_event.start = start
            new_event.end = end
            new_event.calendar = calendar

            new_event.save()

            if new_event is not None:
                return redirect('/calendarapp/event/'+str(new_event.pk))


@method_decorator(login_required(login_url='/calendarapp/login/'), name='dispatch')
class ListEventsView(View):
    template_name = 'calendarapp/list_events.html'

    def get(self, request):

        username = request.user
        events = Event.objects.filter(creator=username).all()

        return render(request, self.template_name, {'event_list': events})


@method_decorator(login_required(login_url='/calendarapp/login/'), name='dispatch')
class EditEventView(View):
    template_name = 'calendarapp/edit_event.html'
    form_class = EditEventForm

    def get(self, request):
        event_id = request.GET.get('event')
        event = Event.objects.filter(pk=event_id).first()
        date_start = str(event.start).split(" ")[0]
        time_start = str(event.start).split(" ")[1].split("+")[0]
        date_end = str(event.end).split(" ")[0]
        time_end = str(event.end).split(" ")[1].split("+")[0]
        return render(request, self.template_name, {
            'event_id': event_id,
            'title': event.title,
            'description': event.description,
            'date_start': date_start,
            'time_start': time_start,
            'date_end': date_end,
            'time_end': time_end,
        })

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            event_id = form.cleaned_data['event_id']
            event = Event.objects.filter(pk=event_id).first()

            start_date = form.cleaned_data['date_start']
            end_date = form.cleaned_data['date_end']
            start_time = form.cleaned_data['time_start']
            end_time = form.cleaned_data['time_end']
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']

            start = datetime.combine(start_date, start_time)
            end = datetime.combine(end_date, end_time)

            event.start = start
            event.end = end
            event.title = title
            event.description = description
            event.save()
            return redirect('/calendarapp/dashboard')


@method_decorator(login_required(login_url='/calendarapp/login/'), name='dispatch')
class DeleteEventView(View):

    def get(self, request):
        event_id = request.GET.get('event')
        Event.objects.filter(pk=event_id).first().delete()
        return redirect('/calendarapp/dashboard')


@method_decorator(login_required(login_url='/calendarapp/login/'), name='dispatch')
class EditProfileView(View):
    template_name = 'calendarapp/edit_profile.html'
    form_class = EditProfileForm

    def get(self, request):

        user = request.user

        if user.is_superuser:
            return HttpResponse("<center><h1>HELLO SUPER USER, YOU CAN'T EDIT YOUR PROFILE<h1></center>")

        pk = user.pk
        student_group = StudentGroup.objects.filter(pk=pk).first()
        name = student_group.name
        email = student_group.email
        description = student_group.description

        return render(request, self.template_name, {
            'name': name,
            'email': email,
            'description': description,
        })

    def post(self, request):
        form = self.form_class(request.POST,request.FILES)

        if form.is_valid():
            user = request.user
            pk = user.pk
            student_group = StudentGroup.objects.filter(pk=pk).first()

            student_group.name = form.cleaned_data['name']
            student_group.email = form.cleaned_data['email']
            student_group.description = form.cleaned_data['description']
            student_group.image = form.cleaned_data['image']

            student_group.save()

            return redirect('/calendarapp/dashboard')
