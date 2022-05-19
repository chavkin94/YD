from django import forms

from master.models import Master


class MasterAddForm(forms.ModelForm):

    class Meta:
        model = Master
        fields = ['name', 'slug', 'location', 'phone_number', 'email', 'description', 'start_year', 'user']
        widgets = {
           'name': forms.TextInput(attrs={'class': 'form-input'}),
           'description': forms.Textarea(attrs={'cols': 60, 'row': 10}),
            'start_year': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
        }

class MasterUpdateForm(forms.ModelForm):
    class Meta:
        model = Master
        fields = ['name', 'slug', 'location', 'phone_number', 'email', 'start_year', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'description': forms.Textarea(attrs={'cols': 60, 'row': 10}),
            'start_year': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
        }