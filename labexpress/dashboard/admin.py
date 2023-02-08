from django.contrib import admin
from .models import Profile
from .models import Customer
from .models import Category
from .models import Brand
from .models import Product
from .models import Device
from .models import Repair

# Register your models here.

admin.site.register(Profile)
admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(Device)
admin.site.register(Repair)
