from django.db import models

# Create your models here.

class cita(models.Model):
    servicio = models.CharField(max_length=30)
    precio = models.FloatField()
    duracion = models.DurationField()

    def __str__(self):
        return self.titulo
