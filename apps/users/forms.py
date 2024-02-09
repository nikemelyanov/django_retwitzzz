from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from apps.users.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input', 'placeholder': 'Введите имя пользователя'
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'input', 'placeholder': 'Введите пароль'
    }))

    class Meta():
        model = User
        fields = ['username', 'password']


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': '', 'placeholder': 'Введите имя'
    }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': '', 'placeholder': 'Введите фамилию'
    }))

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': '', 'placeholder': 'Введите имя пользователя'
    }))

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': '', 'placeholder': 'Введите адрес эл. почты'
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': '', 'placeholder': 'Введите пароль'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': '', 'placeholder': 'Подтвердите пароль'
    }))

    class Meta():
        model = User
        fields = ['first_name', 'last_name', 'username',
                  'email', 'password1', 'password2']