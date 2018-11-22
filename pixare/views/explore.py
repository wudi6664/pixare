# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect

def news(request):
    return render(request, 'explore.html', {})

def hots(request):
    return render(request, 'explore.html', {})