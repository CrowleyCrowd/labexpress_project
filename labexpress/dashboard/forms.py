from django.forms import ModelForm
from .models import Customer


class newCustomer (ModelForm):
    class Meta:
        model = Customer
        fields = ['document', 'firstname', 'lastname', 'address', 'phone',
                  'cellphone', 'email']