from django import forms

from master.models import Master, MasterPost, Service


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
            'start_year': forms.TextInput(attrs={'class': 'form-control mt-2', 'type': 'number'}),
            'user': forms.Select(attrs={'class': 'form-control mt-2'}),
            'image': forms.FileInput(attrs={'class': 'form-control mt-2 w-50', 'type': 'file', 'accept': '.jpg,.png'}),
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
            'image': forms.FileInput(attrs={'class': 'form-control mt-2 w-50', 'type': 'file', 'accept': '.jpg,.png'}),
        }


# Форма создания поста
class PostAddForm(forms.ModelForm):

    class Meta:
        model = MasterPost
        fields = ['master', 'slug', 'title', 'image', 'content']
        widgets = {
            'master': forms.Select(attrs={'class': 'form-control mt-2'}),
            'slug': forms.TextInput(attrs={'class': 'form-control mt-2'}),
            'title': forms.TextInput(attrs={'class': 'form-control mt-2'}),
            'image': forms.FileInput(attrs={'class': 'form-control mt-2 w-50'}),
            'content': forms.Textarea(attrs={'class': 'form-control mt-2'}),
        }


class ServiceAddForm(forms.ModelForm):

    class Meta:
        model = Service
        fields = ['name', 'slug', 'price', 'description', 'custom_category', 'serviceCategory', 'master',
                  'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control mt-2'}),
            'slug': forms.TextInput(attrs={'class': 'form-control mt-2'}),
            'price': forms.TextInput(attrs={'class': 'form-control mt-2'}),
            'description': forms.Textarea(attrs={'cols': 60, 'row': 10, 'class': 'form-control mt-2'}),
            'custom_category': forms.TextInput(attrs={'class': 'form-control mt-2'}),
            'serviceCategory': forms.Select(attrs={'class': 'form-control mt-2'}),
            'master': forms.Select(attrs={'class': 'form-control mt-2'}),
            'image': forms.FileInput(attrs={'class': 'form-control mt-2 w-50', 'type': 'file', 'accept': '.jpg,.png'}),
        }


class ServiceUpdateForm(forms.ModelForm):

    class Meta:
        model = Service
        fields = ['name', 'slug', 'price', 'description', 'custom_category', 'serviceCategory', 'master',
                  'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control mt-2'}),
            'slug': forms.TextInput(attrs={'class': 'form-control mt-2'}),
            'price': forms.TextInput(attrs={'class': 'form-control mt-2'}),
            'description': forms.Textarea(attrs={'cols': 60, 'row': 10, 'class': 'form-control mt-2'}),
            'custom_category': forms.TextInput(attrs={'class': 'form-control mt-2'}),
            'serviceCategory': forms.Select(attrs={'class': 'form-control mt-2'}),
            'master': forms.Select(attrs={'class': 'form-control mt-2'}),
            'image': forms.FileInput(attrs={'class': 'form-control mt-2 w-50', 'type': 'file', 'accept': '.jpg,.png'}),
        }