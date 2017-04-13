# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length = 100, blank = True, null = True)
    email = models.CharField(max_length = 100, blank = True, null = True)
    phone = models.CharField(max_length = 100, blank = True, null = True)
    address = models.CharField(max_length = 100, blank = True, null = True)
    country = models.CharField(max_length = 100, blank = True, null = True)
    birth = models.CharField(max_length = 100, blank = True, null = True)
    image = models.CharField(max_length = 100, blank = True, null = True)
    uuid = models.CharField(max_length = 100, blank = True)
