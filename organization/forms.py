from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import *


class OrganizationAddForm(forms.ModelForm):

    class Meta:
        model = Organization
        # fields = '__all__'  #какие поля нужно отобразить в форме в данном случае все
        fields = ['name', 'slug', 'location', 'phone_number', 'email', 'description', 'user']
        widgets = {
           'name': forms.TextInput(attrs={'class': 'form-control mt-2'}),
           'slug': forms.TextInput(attrs={'class': 'form-control mt-2'}),
           'location': forms.TextInput(attrs={'class': 'form-control mt-2'}),
           'phone_number': forms.TextInput(attrs={'class': 'form-control mt-2', 'id':'phone', 'type':'text'}),
           'email': forms.EmailInput(attrs={'class': 'form-control mt-2'}),
           'description': forms.Textarea(attrs={'cols': 60, 'row': 10, 'class': 'form-control mt-2'}),
           'user': forms.Select(attrs={'class': 'form-control mt-2'}),
        }

class OrganizationUpdateForm(forms.ModelForm):
    class Meta:
        model = Organization
        # fields = '__all__'  #какие поля нужно отобразить в форме в данном случае все
        fields = ['name', 'slug', 'location', 'phone_number', 'email', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control mt-2'}),
            'slug': forms.TextInput(attrs={'class': 'form-control mt-2'}),
            'location': forms.TextInput(attrs={'class': 'form-control mt-2'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control mt-2', 'id': 'phone', 'type': 'text'}),
            'email': forms.EmailInput(attrs={'class': 'form-control mt-2'}),
            'description': forms.Textarea(attrs={'cols': 60, 'row': 10, 'class': 'form-control mt-2'}),
        }