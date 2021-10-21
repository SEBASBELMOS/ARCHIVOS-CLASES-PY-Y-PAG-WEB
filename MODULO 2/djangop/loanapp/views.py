from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def home(request):
    return render(request, 'index.html')

def login(request):
    if request.method == "POST":
        usuario = request.POST['usuario']
        contraseña = request.POST['contraseña']
        usuarios = {
            'usuario':usuario,
            'contraseña':contraseña,
        }
        try:
            datos=usuarios.objects.create(usuario=usuario,contraseña=contraseña)
            contexto = {
                'usuario':usuario,
                'estado':True,
                }
            return render(request, 'respuesta.html',contexto)
        except ValueError as e:
            contexto={
                'estado':False,
                'error':e,
            }
            return render(request, 'respuesta.html',contexto)
    else:
        return render(request, 'login.html')

