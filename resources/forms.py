from django import forms
from django.forms import ModelForm
from .models import Resource, Skill

class ResourceForm(ModelForm):
    class Meta:
        model = Resource
        
        fields = ('first_name', 'last_name', 'title', 'skills','cost_per_hour')

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),                 
            'cost_per_hour': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cost Per Hour'}),            
        }
