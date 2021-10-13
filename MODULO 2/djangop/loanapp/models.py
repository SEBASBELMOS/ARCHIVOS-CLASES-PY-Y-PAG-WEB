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
    servicio = models.CharField(max_length=50, choices=serv_opc)
    precio = models.FloatField(default=None)


