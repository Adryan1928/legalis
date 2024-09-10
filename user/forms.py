from .models import Client
from django import forms
from django.contrib.auth.models import User

classes = 'bg-neutral-200 focus:border-none focus:outline-none'

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'password']

        widgets = {
            'first_name': forms.TextInput(attrs={'class': classes, 'placeholder': 'Digite seu nome'}),
            'email': forms.EmailInput(attrs={'class': classes, 'placeholder': 'email@email.com'}),
            'password': forms.PasswordInput(attrs={'class': classes, 'placeholder': 'Digite sua senha'}),
        }
        labels = {
            'first_name': 'Nome',
            'email': 'Email',
            'password': 'Senha',
        }

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['profile_photo']

        widgets = {
            'profile_photo': forms.FileInput(attrs={'class': classes})
        }

        labels = {
            'profile_photo': 'Foto de Perfil'
        }
