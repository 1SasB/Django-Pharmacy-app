from django import forms

from .models import *

class AddProduct(forms.Form):
    name = forms.CharField(max_length=750)
    description = forms.Textarea()
    price = forms.IntegerField()
    quantity = forms.IntegerField()

