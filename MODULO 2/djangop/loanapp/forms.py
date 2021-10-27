from django.forms import EmailInput, PasswordInput, TextInput
from loanapp.models import *
from django import forms

class PersonaForm(forms.Form):
    nombres = forms.CharField(max_length=30, widget=TextInput(attrs={
        'class':'form-control'
    }))
    apellidos = forms.CharField(max_length=60, widget=TextInput(attrs={
        'class':'form-control'
    }))
    email = forms.CharField(max_length=60, widget=TextInput(attrs={
        'class':'form-control',
        'placeholder':'nombre@correo'
    }))
    password = forms.CharField(max_length=60, widget=TextInput(attrs={
        'class':'form-control'
    }))
    password_verificar = forms.CharField(max_length=60, widget=TextInput(attrs={
    'class':'form-control'
    }))