
#from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
]