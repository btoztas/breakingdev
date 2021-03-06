# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from schedule.models import Event
# Create your models here.
from schedule.models import Calendar


class StudentGroup(User):
    name = models.CharField(max_length=30)
    acro = models.CharField(max_length=10)
    description = models.CharField(max_length=500, default="Por inserir")
    image = models.ImageField(upload_to='', default='none.png')


class Event(Event):
    image = models.ImageField(upload_to='', default='none.png')
    type = models.CharField(max_length=30)
    place = models.CharField(max_length=30)

class Degree(models.Model):
    acro = models.CharField(max_length=30)
    photo = models.CharField(max_length=500)
    name = models.CharField(max_length=500)


class Evaluation(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    start = models.DateTimeField()
    end = models.DateTimeField()
    place = models.CharField(max_length=30, default="Undefined")
    owner = models.ForeignKey(Degree, on_delete=models.CASCADE, default=None)
