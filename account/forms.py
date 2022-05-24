from django import forms
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError

# from main.apps import user_registered
from account.models import CustomUser, AccountPost


#Форма редактирования пользовательских данных
class ChangeUserInfoForm(forms.ModelForm):
    # email = forms.EmailField(required=True, label='Адрес электронной почты')
    username = forms.CharField(label='Логин на сайте', widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    surname = forms.CharField(label='Отчество', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-control'}))
    birthday = forms.DateField(label='Дата рождения', widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})) # Работает только если убрать 'type': 'date'
    gender = forms.ChoiceField(label='Пол', widget=forms.Select(attrs={'class': 'form-control'}), choices=(('', ""), ('m', "мужской"), ('w', "женский")))
    email = forms.EmailField(label='Email', required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    phone_number = forms.CharField(label='Номер телефона', widget=forms.TextInput(attrs={'class': 'form-control', 'id':'phone'}))

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'surname', 'last_name', 'birthday', 'gender', 'email', 'phone_number')


#Форма регистрации пользователя
class RegisterUserForm(forms.ModelForm):
    email = forms.EmailField(label='Email', required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    username = forms.CharField(label='Логин на сайте', widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    surname = forms.CharField(label='Отчество', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-control'}))
    birthday = forms.DateField(label='Дата рождения', widget=forms.DateInput(
        attrs={'class': 'form-control', 'type': 'date'}))  # Работает только если убрать 'type': 'date'
    gender = forms.ChoiceField(label='Пол', widget=forms.Select(attrs={'class': 'form-control'}),
                               choices=(('', ""), ('m', "мужской"), ('w', "женский")))
    phone_number = forms.CharField(label='Номер телефона', widget=forms.TextInput(attrs={'class': 'form-control', 'id':'phone'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}), help_text=password_validation.password_validators_help_text_html())
    password2 = forms.CharField(label='Пароль (повторно)', widget=forms.PasswordInput(attrs={'class': 'form-control'}), help_text='Введите тот же самый пароль еще раз для проверки')

    def clean_password1(self):
        password1 = self.cleaned_data['password1']
        if password1:
            password_validation.validate_password(password1)
        return password1

    def clean(self):
        super().clean()
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 and password2 and password1 != password2:
            errors = {'password2': ValidationError('Введенные пароли не совпадают', code='password_mismatch')}
            raise ValidationError(errors)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.is_activated = False
        if commit:
            user.save()
        # user_registered.send(RegisterUserForm, instance=user)
        return user

    class Meta:
        model = CustomUser
        fields = 'username', 'password1', 'password2', 'first_name', 'surname', 'last_name', 'birthday', 'gender', 'email', 'phone_number'

#Форма создания поста
class AccountPostAddForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['master'].empty_label = "Категория не выбрана"

    class Meta:
        model = AccountPost
        fields = ['user', 'slug', 'title', 'image', 'content']
        widgets = {
           'user': forms.Select(attrs={'class': 'form-control mt-2'}),
           'slug': forms.TextInput(attrs={'class': 'form-control mt-2'}),
           'title': forms.TextInput(attrs={'class': 'form-control mt-2'}),
            'image': forms.FileInput(attrs={'class': 'form-control mt-2 w-50'}),
           'content': forms.TextInput(attrs={'class': 'form-control mt-2'}),
        }
