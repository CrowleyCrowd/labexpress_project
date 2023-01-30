from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('users/', views.users, name='users'),
    path('customers/', views.customers, name='customers'),
    path('devices/', views.devices, name='devices'),
    path('repairs/', views.repairs, name='repairs'),
    
]