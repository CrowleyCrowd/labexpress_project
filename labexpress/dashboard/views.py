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

   return render(request, 'dashboard/customers.html',{
        'customers': customers
    })

def repairs(request):
    return render(request, 'dashboard/repairs.html')

def devices(request):
    return render(request, 'dashboard/devices.html')


def creat_customer(request):
    if  request.method == 'GET':
      return  render(request, 'dashboard/creat_customers.html', {
      'form': NewCusTomer })
    else:
        try:
           form =NewCusTomer(request.POST)
           newCustomer= form.save(commit=False)
           newCustomer.user= request.user
           newCustomer.save()
           return redirect('customers')
        except ValueError:
            return render(request, 'dashboard/creat_customers.html', {
                'form': NewCusTomer,
                 'error':'Erorr'})


=======
def createDevices(request):
    return render(request, 'dashboard/create_device.html')

def login(request):

