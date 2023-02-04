from django.urls import path

from . import views
from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

urlpatterns = [
    #path('login/', views.login, name='login'),
    path('repairs/', login_required(views.repairs), name='repairs'),
    path('devices/', login_required(views.devices), name='devices'),
    path('customers/', login_required(views.customers), name='customers'),
    path('users/', login_required(views.users), name='users'),
    path('', login_required(views.index), name='index'),
    path('',login,{'template_name':'login.html'}, name = 'login')
]