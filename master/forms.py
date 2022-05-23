from django import forms

from master.models import Master


class MasterAddForm(forms.ModelForm):

    class Meta:
        model = Master
        fields = ['name', 'slug', 'location', 'phone_number', 'email', 'description', 'start_year', 'user', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control mt-2'}),
            'slug': forms.TextInput(attrs={'class': 'form-control mt-2'}),
            'location': forms.Select(attrs={'class': 'form-control mt-2'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control mt-2', 'id': 'phone', 'type': 'text'}),
            'email': forms.EmailInput(attrs={'class': 'form-control mt-2'}),
            'description': forms.Textarea(attrs={'cols': 60, 'row': 10, 'class': 'form-control mt-2'}),
            'start_year': forms.DateInput(attrs={'class': 'form-control mt-2', 'type': 'date'}),
            'user': forms.Select(attrs={'class': 'form-control mt-2'}),
            'image': forms.TextInput(attrs={'class': 'form-control mt-2 w-50', 'type': 'file'}),
        }

class MasterUpdateForm(forms.ModelForm):
    class Meta:
        model = Master
        fields = ['name', 'slug', 'location', 'phone_number', 'email', 'start_year', 'description', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control mt-2'}),
            'slug': forms.TextInput(attrs={'class': 'form-control mt-2'}),
            'location': forms.Select(attrs={'class': 'form-control mt-2'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control mt-2', 'id': 'phone', 'type': 'text'}),
            'email': forms.EmailInput(attrs={'class': 'form-control mt-2'}),
            'start_year': forms.DateInput(attrs={'class': 'form-control mt-2', 'type': 'date'}),
            'description': forms.Textarea(attrs={'cols': 60, 'row': 10, 'class': 'form-control mt-2'}),
            'image': forms.TextInput(attrs={'class': 'form-control mt-2 w-50', 'type': 'file'}),
        }