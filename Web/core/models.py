from django.db import models

# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    edad = models.IntegerField(default=0)
    telefono = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.id} - {self.nombre} - {self.apellido} - {self.edad} - {self.telefono}"
    