from django.db import models

# Create your models here.

class Adopcion( models.Model ):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)
    cedula = models.CharField(max_length=30)
    direccion = models.CharField(max_length=100)
    def _str_(self):
        return self.nombres