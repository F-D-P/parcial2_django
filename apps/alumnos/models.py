from django.db import models

from django.db import models

class Alumno(models.Model):
    nombre = models.CharField(max_length=100, default="Nombre")
    apellido = models.CharField(max_length=100, default="Apellido")
    dni = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(unique=True, default="sinemail@example.com")
    fecha_nacimiento = models.DateField(null=True, blank=True)
    carrera = models.CharField(
        max_length=100,
        choices=[
            ('sistemas', 'Ingeniería en Sistemas'),
            ('industrial', 'Ingeniería Industrial'),
            ('civil', 'Ingeniería Civil'),
        ],
        default='sistemas'
    )
    promedio = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        null=True,
        blank=True,
        default=0.00
    )

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"
