# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect

def index(request):
    return render(request, 'index.html', {})

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

