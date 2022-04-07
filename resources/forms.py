from django import forms
from django.forms import ModelForm
from .models import Resource

class ResourceForm(ModelForm):
    class Meta:
        model = Resource
        
        fields = ('first_name', 'last_name', 'title')

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),                 
        }