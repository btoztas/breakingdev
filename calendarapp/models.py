# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class StudentGroup(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    photo = models.CharField(max_length=500)
    # password =


class Event(models.Model):
    name = models.CharField(max_length=30)
    start = models.DateTimeField()
    end = models.DateTimeField()
    description = models.CharField(max_length=500)
