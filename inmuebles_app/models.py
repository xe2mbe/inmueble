from django.db import models
from django.db.models.base import ModelStateFieldsCacheDescriptor

# Create your models here.


class Inmueble(models.Model):
    direccion = models.CharField(max_length=250)
    pais = models.CharField(max_length=250)
    descripcion = models.CharField(max_length=250)
    imagen = models.CharField(max_length = 255)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.direccion
    
    