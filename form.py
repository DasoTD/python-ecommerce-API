from django import forms
from .models import Customer
from .models import CustomerOrder
from .models import Customerdetails


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [ 'name', 'gender', 'age', 'description']

class CustomerOrder(forms.ModelForm):
    class Meta:
        model = CustomerOrder
        fields = ['name', 'product', 'description', 'size', 'choice']

class Customerdetails(forms.ModelForm):
    class Meta:
        model = Customerdetails
        fields = ['f_name','l_name','gmail', 'gender', 'date']