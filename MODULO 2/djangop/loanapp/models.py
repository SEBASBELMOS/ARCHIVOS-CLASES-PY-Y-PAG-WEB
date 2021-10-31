from django.db import models
from django.db.models.base import Model
from django.db.models.fields.related import OneToOneField
from django.contrib.auth.models import User
# Create your models here.

class persona(models.Model):
    usuario = models.CharField(max_length=20, default='')
    email=models.EmailField(max_length=30, default='')
    contraseña = models.CharField(max_length=20, default='')
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=60)


class usuarios(models.Model):
    usuario = models.CharField(max_length=20, default='')
    contraseña = models.CharField(max_length=20, default='')


