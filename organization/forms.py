from django import forms
from .models import *


class OrganizationAddForm(forms.ModelForm):
    OrganizationCategory = forms.ModelChoiceField(label='Вид организации', queryset=OrganizationCategory.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}),)
    class Meta:
        model = Organization
        # fields = '__all__'  #какие поля нужно отобразить в форме в данном случае все
        fields = ['name', 'slug', 'location', 'phone_number', 'email', 'description', 'user', 'image']
        widgets = {
           'name': forms.TextInput(attrs={'class': 'form-control mt-2'}),
           'slug': forms.TextInput(attrs={'class': 'form-control mt-2'}),
           'location': forms.Select(attrs={'class': 'form-control mt-2'}),
           'phone_number': forms.TextInput(attrs={'class': 'form-control mt-2', 'id':'phone', 'type':'text'}),
           'email': forms.EmailInput(attrs={'class': 'form-control mt-2'}),
           'description': forms.Textarea(attrs={'cols': 60, 'row': 10, 'class': 'form-control mt-2'}),
           'user': forms.Select(attrs={'class': 'form-control mt-2'}),
           'image': forms.FileInput(attrs={'class': 'form-control mt-2 w-50', 'type': 'file'}),
        }

    def save(self, commit=True):
        organization = super().save(commit=False)
        organizationcategory = self.cleaned_data['OrganizationCategory']

        OrganizationCategory.objects.create(FKOrganizationCategory=organization, FKOrganization=organization)

        if commit:
            organization.save()
        # user_registered.send(RegisterUserForm, instance=user)
        return organization


class OrganizationUpdateForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ['name', 'slug', 'location', 'phone_number', 'email', 'description', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control mt-2'}),
            'slug': forms.TextInput(attrs={'class': 'form-control mt-2'}),
            'location': forms.Select(attrs={'class': 'form-control mt-2'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control mt-2', 'id': 'phone', 'type': 'text'}),
            'email': forms.EmailInput(attrs={'class': 'form-control mt-2'}),
            'description': forms.Textarea(attrs={'cols': 60, 'row': 10, 'class': 'form-control mt-2'}),
            'image': forms.FileInput(attrs={'class': 'form-control mt-2 w-50', 'type': 'file'}),
        }