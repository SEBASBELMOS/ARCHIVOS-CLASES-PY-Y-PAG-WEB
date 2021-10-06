from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def prueba(request):
    hora = datetime.now()
    return HttpResponse(f"La hora es: {hora}")

def suma(request):
    suma1 = 3 + 4
    return HttpResponse(f"La suma de 3 mas 4 es igual a {suma1}")

def calcular(request, fecha, fecha2):
    edad = 2021 - fecha
    return HttpResponse(f"En el {fecha2} cumple {edad}")