from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def prueba(request):
    hora = datetime.now()
    return HttpResponse(f"La hora es: {hora}")

def suma(request):
    suma1 = 3 + 4
    return HttpResponse(f"La suma de 3 mas 4 es igual a {suma1}")