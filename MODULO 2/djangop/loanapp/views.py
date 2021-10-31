from django.shortcuts import redirect, render
from django.http import HttpResponse, response
from datetime import datetime
from django.urls import reverse
from loanapp.models import *
from loanapp.forms import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'index.html')

def login_(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['usuario']
            contraseña = form.cleaned_data['contraseña']
            user = authenticate(username=usuario, password=contraseña)
            if user is not None:
                login(request, user)
                return redirect(reverse('home'))
            else:
                messages.warning(request, 'El usuario y/o contraseña es incorrecto')
                return redirect(reverse('login_user'))
        else:
            messages.warning(request, 'Error al leer los datos enviados')
            return redirect(reverse('login_user'))            
    else:
        contexto = dict()
        contexto['formLogin'] = LoginForm()
        return render(request, 'login_usuario.html', contexto)

def registrar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['usuario']
            email = form.cleaned_data['email']
            contraseña = form.cleaned_data['contraseña']
            contraseña_verificar = form.cleaned_data['contraseña_verificar']
            nombres = form.cleaned_data['nombres']
            apellidos = form.cleaned_data['apellidos']
            if contraseña == contraseña_verificar:
                User.objects.create_user(usuario, email, contraseña)
                messages.success(request, 'Usuario creado correctamente.')
                return redirect(reverse('registrar_usuario'))
            else:
                messages.warning(request, 'Contraseña no coincide')
                return redirect(reverse('registrar_usuario'))            
        else:
            messages.warning(request, 'Datos no validos')
            return redirect(reverse('registrar_usuario')) 
    else:      
        contexto = dict()
        contexto['UsuarioForm'] = UsuarioForm()
        return render(request, 'registrar_usuario.html', contexto)

@login_required(login_url='/usuario/login/')
def logout_(request):
    logout(request)
    return redirect(reverse('inicio'))