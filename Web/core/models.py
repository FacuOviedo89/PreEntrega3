from django.db import models

# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    telefono = models.IntegerField(max_length=50)

    def __str__(self):
        return f"{self.id} - {self.nombre} - {self.apellido} - {self.telefono}"
    