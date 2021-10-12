from django.db import models
from django.db.models.base import Model
from django.db.models.fields.related import OneToOneField

# Create your models here.

serv_opc = [
    ('M','Maquillaje'),
    ('TC','Tratamientos Corporales'),
    ('TF','Tratamientos Faciales'),
    ('E','Especial')
]

class serv(models.Model):
    fecha = models.DateField(max_length=13)
    servicio = models.CharField(max_length=50, choices=serv_opc)

class cita(models.Model):
    precio = models.FloatField()
    duracion = models.DurationField()

class Persona(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(max_length=40)

