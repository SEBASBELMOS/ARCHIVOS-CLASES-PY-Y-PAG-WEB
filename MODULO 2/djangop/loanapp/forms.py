from django.forms import EmailInput, PasswordInput, TextInput, ModelForm
from loanapp.models import *
from django import forms

class UsuarioForm(forms.Form):
    usuario = forms.CharField(max_length=30, widget=TextInput(attrs={
        'class':'form-control'
        }))
    nombres = forms.CharField(max_length=30, widget=TextInput(attrs={
        'class':'form-control'
    }))
    apellidos = forms.CharField(max_length=60, widget=TextInput(attrs={
        'class':'form-control'
    }))
    email = forms.CharField(max_length=60, widget=EmailInput(attrs={
        'class':'form-control',
        'placeholder':'nombre@correo'
    }))
    contraseña = forms.CharField(max_length=60, widget=PasswordInput(attrs={
        'class':'form-control'
    }))
    contraseña_verificar = forms.CharField(max_length=60, widget=PasswordInput(attrs={
    'class':'form-control'
    }))

class LoginForm(forms.Form):
    usuario = forms.CharField(max_length=30, widget=TextInput(attrs={
        'class':'form-control'
        }))
    contraseña = forms.CharField(max_length=60, widget=PasswordInput(attrs={
        'class':'form-control'
    }))