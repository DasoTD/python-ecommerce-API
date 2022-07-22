from django.contrib import admin
from . models import Customer
from . models import CustomerOrder

# Register your models here.
admin.site.register(Customer)
admin.site.register(CustomerOrder)