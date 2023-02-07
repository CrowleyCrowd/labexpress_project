from django.shortcuts import render, redirect

from .forms import NewCusTomer
from .models import Customer


# Create your views here.

def index(request):
    return render(request, 'dashboard/index.html')


def users(request):
    return render(request, 'dashboard/users.html')


def createUser(request):
    return render(request, 'dashboard/create_user.html')


def customers(request):
    customers = Customer.objects.all()
    return render(request, 'dashboard/customers.html', {
        'customers': customers
    })


def createCustomer(request):
    if request.method == 'GET':
        return render(request, 'dashboard/create_customer.html', {
            'form': NewCusTomer})
    else:
        try:
            form = NewCusTomer(request.POST)
            newCustomer = form.save(commit=False)
            newCustomer.user = request.user
            newCustomer.save()
            return redirect('customers')
        except ValueError:
            return render(request, 'dashboard/create_customer.html', {
                'form': NewCusTomer,
                'error': 'Error'})


def devices(request):
    return render(request, 'dashboard/devices.html')


def createDevice(request):
    return render(request, 'dashboard/create_device.html')


def repairs(request):
    return render(request, 'dashboard/repairs.html')


def createRepair(request):
    return render(request, 'dashboard/create_repair.html')
