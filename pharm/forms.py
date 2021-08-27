from django import forms
from django.db.models import fields

from .models import *

class AddProduct(forms.ModelForm):
    Model = Product

    class Meta:
        fields = ['name','description','available_quantity','exp_date','unit_price']
    # name = forms.CharField(max_length=750)
    # description = forms.Textarea()
    # price = forms.IntegerField()
    # quantity = forms.IntegerField()

