# from django.forms import formset_factory
from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields=['product_name','price','unit']
        


