from django.shortcuts import render
from django.http import HttpResponse
from .models import Profile


def index(request):
    return HttpResponse('HELLO DASHBOARD')