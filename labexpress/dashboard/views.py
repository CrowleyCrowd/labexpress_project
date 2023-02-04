from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'dashboard/index.html')

def users(request):
    return render(request, 'dashboard/users.html')

def customers(request):
    return render(request, 'dashboard/customers.html')

def repairs(request):
    return render(request, 'dashboard/repairs.html')

def devices(request):
    return render(request, 'dashboard/devices.html')

def login(request):
    return render(request, 'dashboard/login.html')