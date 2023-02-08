from django.urls import path

from . import views
from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

urlpatterns = [
    path('repairs/create_repair/', login_required(views.CreateRepair),
         name='create_repair'),
    path('repairs/', login_required(views.Repairs), name='repairs'),
    path('devices/create_device', login_required(views.CreateDevice),
         name='create_device'),
    path('devices/', login_required(views.Devices), name='devices'),
    path('customers/create_customer/',
         login_required(views.CreateCustomer), name='create_customer'),
    path('customers/', login_required(views.Customers), name='customers'),
    path('users/create_user', login_required(views.CreateUser),
         name='create_user'),
    path('users/', login_required(views.Users), name='users'),
    path('', login_required(views.Index), name='index'),
    path('accounts/logout', logout,
         {'template_name': 'logged_out.html'}, name='logout'),
    path('', login, {'template_name': 'login.html'}, name='login')
]
