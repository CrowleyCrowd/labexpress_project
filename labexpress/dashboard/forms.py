from django.forms import ModelForm
from django import forms
import datetime
import time
from .models import Customer, Repair, Device
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name','last_name','email', 'password','date_joined','is_staff','is_superuser','is_active']


class CustomerForm (ModelForm):
    class Meta:
        model = Customer
        fields = ['document', 'firstname', 'lastname', 'address', 'phone',
                  'cellphone', 'email']


class RepairForm (forms.ModelForm):
    date_reception = forms.DateField(
        widget=forms.TextInput(
            attrs={'type': 'date', 'class': 'form-control', 'style': 'width:150px'}))
    time_reception = forms.TimeField(widget=forms.TextInput(
        attrs={'type': 'time', 'class': 'form-control', 'style': 'width:150px'}))
    details = forms.CharField(widget=forms.TextInput(
        attrs={'type': 'textarea', 'class': 'form-control', 'style': 'width:50%; height:100px'}))
    observations = forms.CharField(widget=forms.TextInput(
        attrs={'type': 'textarea', 'class': 'form-control', 'style': 'width:50%; height:100px'}))
    date_repair = forms.DateField(
        widget=forms.TextInput(
            attrs={'type': 'date', 'class': 'form-control', 'style': 'width:150px'}))
    time_repair = forms.TimeField(widget=forms.TextInput(
        attrs={'type': 'time', 'class': 'form-control', 'style': 'width:150px'}))

    class Meta:
        model = Repair
        fields = ['creator', 'customer', 'serial', 'date_reception', 'time_reception',
                  'details', 'observations', 'assignee', 'date_repair', 'time_repair']
        
        
    class DeviceForm:
        model = Device    
        fields = ['serial', 'category', 'brand', 'product'] 
