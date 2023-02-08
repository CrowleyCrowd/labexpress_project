from django.forms import ModelForm
from django import forms
import datetime
import time
from .models import Customer, Repair


class CustomerForm (ModelForm):
    class Meta:
        model = Customer
        fields = ['document', 'firstname', 'lastname', 'address', 'phone',
                  'cellphone', 'email']


class RepairForm (forms.ModelForm):
    date_reception = forms.DateField(
        widget=forms.TextInput(
            attrs={'type': 'date', 'class': 'form-control', 'style': 'width:150px'}),
        label='Fecha')
    time_reception = forms.TimeField(widget=forms.TextInput(attrs={'type': 'time', 'class': 'form-control', 'style': 'width:150px'}),
                                     label='Hora')
    details = forms.CharField(widget=forms.TextInput(attrs={'type': 'textarea', 'class': 'form-control', 'style': 'width:50%; height:100px'}),
                              label='Falla de Equipo')
    observations = forms.CharField(widget=forms.TextInput(attrs={'type': 'textarea', 'class': 'form-control', 'style': 'width:50%; height:100px'}),
                                   label='Observaciones del Equipo')
    date_repair = forms.DateField(
        widget=forms.TextInput(
            attrs={'type': 'date', 'class': 'form-control', 'style': 'width:150px'}),
        label='Fecha de Entrega')
    time_repair = forms.TimeField(widget=forms.TextInput(attrs={'type': 'time', 'class': 'form-control', 'style': 'width:150px'}),
                                  label='Hora de Entrega')

    class Meta:
        model = Repair
        fields = ['creator', 'customer', 'serial', 'date_reception', 'time_reception',
                  'details', 'observations', 'assignee', 'date_repair', 'time_repair']