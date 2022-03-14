from django import forms
from django.forms import ModelForm
from .models import Vendor

class VendorForm(ModelForm):
    class Meta:
        model = Vendor
        
        fields = ('first_name', 'last_name', 'email', 'business_name', 'business_website')

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'business_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Business Name'}),
            'business_website': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Business Website'}),
        }