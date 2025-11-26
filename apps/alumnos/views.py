from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Alumno
from .forms import AlumnoForm

@login_required
def dashboard_view(request):
    alumnos = Alumno.objects.all()
    return render(request, 'alumnos/dashboard.html', {'alumnos': alumnos})

@login_required
def alumno_create(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            alumno = form.save(commit=False)
            alumno.usuario = request.user  # asignar el usuario dueño
            alumno.save()
            return redirect('dashboard')
    else:
        form = AlumnoForm()
    return render(request, 'alumnos/alumno_form.html', {'form': form})

@login_required
def alumno_update(request, id):
    alumno = get_object_or_404(Alumno, id=id, usuario=request.user)
    if request.method == 'POST':
        form = AlumnoForm(request.POST, instance=alumno)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = AlumnoForm(instance=alumno)
    return render(request, 'alumnos/alumno_form.html', {'form': form})

@login_required
def alumno_delete(request, id):
    alumno = get_object_or_404(Alumno, id=id, usuario=request.user)
    if request.method == 'POST':
        alumno.delete()
        return redirect('dashboard')
    return render(request, 'alumnos/alumno_confirm_delete.html', {'alumno': alumno})

@login_required
def alumno_detail(request, id):
    alumno = get_object_or_404(Alumno, id=id, usuario=request.user)
    return render(request, 'alumnos/alumno_detail.html', {'alumno': alumno})

def alumno_list(request):
    alumnos = Alumno.objects.all()   
    return render(request, 'alumnos/alumno_list.html', {'alumnos': alumnos})