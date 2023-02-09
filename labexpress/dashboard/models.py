from django.db import models
from django.contrib.auth.models import User
import datetime
import time

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField('Dirección', max_length=100, blank=True)
    phone = models.CharField('Teléfono', max_length=20, blank=True)
    cellphone = models.CharField('Celular', max_length=20, blank=True)
    # status = models.TextField(max_length=20, choices=status_choices)


class Customer(models.Model):
    document = models.CharField(
        'Documento de Identidad', primary_key=True, max_length=50, blank=False)
    firstname = models.CharField('Nombre', max_length=20, blank=False)
    lastname = models.CharField('Apellido', max_length=20, blank=False)
    address = models.CharField('Dirección', max_length=20, blank=True)
    phone = models.CharField('Teléfono', max_length=20, blank=True)
    cellphone = models.CharField('Celular', max_length=20, blank=True)
    email = models.CharField('Correo Electrónico', max_length=20, blank=True)
    register = models.DateTimeField(
        'Fecha de Registro', auto_now=True, auto_now_add=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)





class Category(models.Model):
    description = models.CharField(
        'Tipo de Equipo', max_length=100, blank=False)


class Brand(models.Model):
    description = models.CharField('Marca', max_length=100, blank=False)


class Product(models.Model):  # Hace referencia al modelo del equipo
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    description = models.CharField('Modelo', max_length=100, blank=False)


class Device(models.Model):
    serial = models.CharField(
        'Número de Serie', max_length=100, primary_key=True, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Repair(models.Model):
    # Usuario que crea la orden
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, blank=False)
    serial = models.ForeignKey(Device, on_delete=models.CASCADE, blank=False)
    date_reception = models.DateField(
        'Fecha de Recepción', blank=False)  # Fecha de Recepción
    time_reception = models.TimeField('Hora de Recepción', blank=False)
    details = models.TextField('Descripción de Falla',
                               max_length=1000, blank=False)  # Detalles de la Falla
    # Observaciones del Dispositivo
    observations = models.TextField(
        'Observaciones del Equipo', max_length=1000, blank=True)
    # Usuario asignado a la reparación
    assignee = models.ForeignKey(
        User, related_name='%(class)s_assignee', on_delete=models.CASCADE)
    date_repair = models.DateField(
        'Fecha Prometida', blank=False)  # Fecha prometida
    time_repair = models.TimeField(
        'Hora Prometida', blank=False)  # Hora Prometida
