from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Votre nom dutilisateur',
        'class': 'w-full px-4 py-2 mt-2 border border-gray-300 rounded-lg focus:outline-none focus:border-teal-500'
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Votre mot de passe',
        'class': 'w-full px-4 py-2 mt-2 border border-gray-300 rounded-lg focus:outline-none focus:border-teal-500'
    }))


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Votre nom dutilisateur',
        'class': 'w-full px-4 py-2 mt-2 border border-gray-300 rounded-lg focus:outline-none focus:border-teal-500'
    }))

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Votre email',
        'class': 'w-full px-4 py-2 mt-2 border border-gray-300 rounded-lg focus:outline-none focus:border-teal-500'
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Votre mot de passe',
        'class': 'w-full px-4 py-2 mt-2 border border-gray-300 rounded-lg focus:outline-none focus:border-teal-500'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirmez votre mot de passe',
        'class': 'w-full px-4 py-2 mt-2 border border-gray-300 rounded-lg focus:outline-none focus:border-teal-500'
    }))
