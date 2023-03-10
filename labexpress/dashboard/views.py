from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .forms import CustomerForm, RepairForm, UserForm, DeviceForm
from .models import Customer, Repair, Device
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
    devices = Device.objects.all()
    return render(request, 'dashboard/devices.html', {
        'devices': devices
    })


def CreateDevice(request):
    if request.method == 'POST':
        device_form = DeviceForm(request.POST)
        if device_form.is_valid():
            device_form.save()
            return redirect('devices')
    else:
        device_form = DeviceForm()
    return render(request, 'dashboard/create_device.html', {'device_form': device_form})


# def EditDevice(request, id):
#     repair_form = None
#     error = None
#     try:
#         editRepair = Repair.objects.get(id=id)
#         if request.method == 'GET':
#             repair_form = RepairForm(instance=editRepair)
#         else:
#             repair_form = RepairForm(request.POST, instance=editRepair)
#             if repair_form.is_valid():
#                 repair_form.save()
#             return redirect('repairs')
#     except ObjectDoesNotExist as e:
#         error = e

#     return render(request, 'dashboard/create_repair.html', {'repair_form': repair_form, 'error': error})


# def DeleteDevice(request, id):
#     delete_repair = Repair.objects.get(id=id)
#     if request.method == 'POST':
#         delete_repair.status = False
#         delete_repair.save()
#         return redirect('repairs')
#     return render(request, 'dashboard/delete_repair.html', {'delete_repair': delete_repair})


def Repairs(request):
    repairs = Repair.objects.filter(status=True)
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


def EditRepair(request, id):
    repair_form = None
    error = None
    try:
        editRepair = Repair.objects.get(id=id)
        if request.method == 'GET':
            repair_form = RepairForm(instance=editRepair)
        else:
            repair_form = RepairForm(request.POST, instance=editRepair)
            if repair_form.is_valid():
                repair_form.save()
            return redirect('repairs')
    except ObjectDoesNotExist as e:
        error = e

    return render(request, 'dashboard/create_repair.html', {'repair_form': repair_form, 'error': error})


def DeleteRepair(request, id):
    delete_repair = Repair.objects.get(id=id)
    if request.method == 'POST':
        delete_repair.status = False
        delete_repair.save()
        return redirect('repairs')
    return render(request, 'dashboard/delete_repair.html', {'delete_repair': delete_repair})
