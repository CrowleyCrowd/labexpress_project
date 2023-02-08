from django.shortcuts import render, redirect

from .forms import CustomerForm, RepairForm
from .models import Customer, Repair


# Create your views here.

def Index(request):
    return render(request, 'dashboard/index.html')


def Users(request):
    return render(request, 'dashboard/users.html')


def CreateUser(request):
    return render(request, 'dashboard/create_user.html')


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
