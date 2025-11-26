from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Alumno
from .forms import AlumnoForm

@login_required
def dashboard(request):
    alumnos = Alumno.objects.filter(usuario=request.user)
    return render(request, "alumnos/dashboard.html", {"alumnos": alumnos})

@login_required
def alumno_create(request):
    if request.method == "POST":
        form = AlumnoForm(request.POST)
        if form.is_valid():
            alumno = form.save(commit=False)
            alumno.usuario = request.user
            alumno.save()
            return redirect("dashboard")
    else:
        form = AlumnoForm()
    return render(request, "alumnos/alumno_form.html", {"form": form})
