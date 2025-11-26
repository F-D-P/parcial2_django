from django import forms
from .models import Alumno

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['nombre', 'apellido', 'dni', 'email', 'fecha_nacimiento', 'carrera', 'promedio']
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'carrera': forms.Select(attrs={'class': 'form-select'}),
            'promedio': forms.NumberInput(attrs={'step': '0.01', 'class': 'form-control'}),
        }
