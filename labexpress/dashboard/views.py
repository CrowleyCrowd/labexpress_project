from django.shortcuts import render, redirect

from .forms import CustomerForm, RepairForm, UserForm
from .models import Customer, Repair
from django.contrib.auth.models import User
# Create your views here.

def Index(request):
    return render(request, 'dashboard/index.html')


def Users(request):
    Users = User.objects.all()
    return render(request, 'dashboard/users.html', {
        'users': Users
    })


def CreateUser(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('users')
    else:
        user_form = UserForm()
    return render(request, 'dashboard/create_user.html', {'user_form': user_form})


def Customers(request):
    customers = Customer.objects.all()
    return render(request, 'dashboard/customers.html', {
        'customers': customers
    })


def CreateCustomer(request):
    if request.method == 'GET':
        return render(request, 'dashboard/create_customer.html', {
            'form': CustomerForm})
    else:
        try:
            form = CustomerForm(request.POST)
            customer_form = form.save(commit=False)
            customer_form.user = request.user
            customer_form.save()
            return redirect('customers')
        except ValueError:
            return render(request, 'dashboard/create_customer.html', {
                'form': CustomerForm,
                'error': 'Error'})


def Devices(request):
    return render(request, 'dashboard/devices.html')


def CreateDevice(request):
    return render(request, 'dashboard/create_device.html')


def Repairs(request):
    repairs = Repair.objects.all()
    return render(request, 'dashboard/repairs.html', {
        'repairs': repairs
    })


def CreateRepair(request):
    if request.method == 'POST':
        repair_form = RepairForm(request.POST)
        if repair_form.is_valid():
            repair_form.save()
            return redirect('repairs')
    else:
        repair_form = RepairForm()
    return render(request, 'dashboard/create_repair.html', {'repair_form': repair_form})


def CreateDevices(request):
    return render(request, 'dashboard/create_device.html')
