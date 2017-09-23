# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class StudentGroup(User):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    photo = models.CharField(max_length=500)


class Event(models.Model):
    name = models.CharField(max_length=30)
    start = models.DateTimeField()
    end = models.DateTimeField()
    description = models.CharField(max_length=500)
    place = models.CharField(max_length=30, default="Undefined")
    owner = models.ForeignKey(StudentGroup, on_delete=models.CASCADE, default=None)


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
