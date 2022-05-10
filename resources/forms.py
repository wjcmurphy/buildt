from django import forms
from django.forms import ModelForm
from .models import Resource, Skill, Booking

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

class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ('start_date', 'end_date', 'hours_per_day')
        widgets = {
            'start_date': forms.widgets.DateInput(attrs={'type': 'date'}),
            'end_date': forms.widgets.DateInput(attrs={'type': 'date'}),
            'hours_per_day': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Hours Per Day'}),            
        }
    