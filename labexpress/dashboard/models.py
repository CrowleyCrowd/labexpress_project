from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Profile(models.Model):
    #status_choices = ('Activo', 'Inactivo')

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.TextField(max_length=20, blank=True)
    cellphone = models.TextField(max_length=20, blank=True)
    address = models.TextField(max_length=100, blank=True)
    #status = models.TextField(max_length=20, choices=status_choices)

class Customer(models.Model):
    document = models.TextField(max_length=20, blank=True)
    firstname = models.TextField(max_length=20, blank=False)
    lastname = models.TextField(max_length=20, blank=False)
    address = models.TextField(max_length=20, blank=True)
    phone = models.TextField(max_length=20, blank=True)
    cellphone = models.TextField(max_length=20, blank=True)
    email = models.TextField(max_length=20, blank=True)
    register = models.DateTimeField(blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Category(models.Model):
    description = models.TextField(max_length=100, blank=False)

class Brand(models.Model):
    description = models.TextField(max_length=100, blank=False)

class Product(models.Model): # Hace referencia al modelo del equipo
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    description = models.TextField(max_length=100, blank=False)

class Device(models.Model):
    serial = models.TextField(max_length=100, primary_key=True,blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class Order(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE) # Usuario que crea la orden
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=False)
    serial = models.ForeignKey(Device, on_delete=models.CASCADE, blank=False)
    date_reception = models.DateTimeField(blank=False)
    details = models.TextField(max_length=1000, blank=False) # Detalles de la Falla
    observations = models.TextField(max_length=1000, blank=True) # Observaciones del Dispositivo
    assignee = models.ForeignKey(User, related_name='%(class)s_assignee', on_delete=models.CASCADE) # Usuario asignado a la reparación
    date_repair = models.DateTimeField(blank=False) # Fecha prometida