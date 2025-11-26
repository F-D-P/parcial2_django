from django.db import models
from django.contrib.auth.models import User

class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    curso = models.CharField(max_length=50)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # dueño del alumno

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.curso}"
