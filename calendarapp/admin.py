# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Event, StudentGroup, Course, Evaluation

# Register your models here.

admin.site.register(Event)
admin.site.register(StudentGroup)
admin.site.register(Course)
admin.site.register(Evaluation)
