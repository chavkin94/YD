from django import forms
from .models import *


class OrganizationAddForm(forms.ModelForm):

    class Meta:
        model = Organization
        # fields = '__all__'  #какие поля нужно отобразить в форме в данном случае все
        fields = ['name', 'slug', 'location', 'phone_number', 'email', 'description', 'user']
        widgets = {
           'name': forms.TextInput(attrs={'class': 'form-input'}),
           'description': forms.Textarea(attrs={'cols': 60, 'row': 10}),
        }


class OrganizationUpdateForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ['name', 'slug', 'location', 'phone_number', 'email', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'description': forms.Textarea(attrs={'cols': 60, 'row': 10}),
        }