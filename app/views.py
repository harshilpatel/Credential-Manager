# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from app.models import *
import uuid
# Create your views here.

def editData(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    address = request.POST.get('address')
    country = request.POST.get('country')
    birth = request.POST.get('birth')

    person, created = Prson.objects.get_or_create(email = email)
    if not created:
        person.name = name
        person.email = email
        person.phone = phone
        person.address = address
        person.country = country
        person.birth = birth
        person.save()
        return render(request, 'home.html', {'person': person})
    else:
        return render(request, 'home.html', {'error' : "Invalid URL"})

    return render(request, 'home.html', {

    })

def submitData(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    address = request.POST.get('address')
    country = request.POST.get('country')
    birth = request.POST.get('birth')

    person, created = Person.objects.get_or_create(email = email)
    if created:
        person.name = name
        person.email = email
        person.phone = phone
        person.address = address
        person.country = country
        person.birth = birth
        person.uuid = str(uuid.uuid4())
        person.save()
        return render(request, 'home.html', {'person': person})
    else:
        return render(request, 'home.html', {'error' : "Email already Exists"})

    return render(request, 'home.html', {

    })

def getData(request, user_uuid):
    try:
        person = Person.objects.get(uuid = user_uuid)
    except:
        return redirect('/')
    if request.GET.get('edit') == '1':
        return render(request, 'home.html', {'person': person, 'edit' : True})
    else:
        person = Person.objects.filter(uuid = user_uuid).values('name', 'email', 'phone','address','country','birth')[0]
        return JsonResponse(person, safe=False)
def home(request):
    return render(request, 'home.html', {})
