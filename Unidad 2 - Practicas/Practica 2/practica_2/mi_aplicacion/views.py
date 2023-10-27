from django.shortcuts import render, redirect, get_object_or_404
from .models import Maestros, Asignaturas, Clases, Alumnos, Calificaciones, Eventos
from .forms import MaestrosForm, AsignaturasForm, ClasesForm, AlumnosForm, CalificacionesForm, EventosForm

# Vistas para Maestros
def lista_maestros(request):
    maestros = Maestros.objects.all()
    return render(request, 'lista_maestros.html', {'maestros': maestros})

def nueva_maestro(request):
    if request.method == 'POST':
        form = MaestrosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_maestros')
    else:
        form = MaestrosForm()
    return render(request, 'nueva_maestro.html', {'form': form})

def editar_maestro(request, id):
    maestro = get_object_or_404(Maestros, pk=id)
    if request.method == 'POST':
        form = MaestrosForm(request.POST, instance=maestro)
        if form.is_valid():
            form.save()
            return redirect('lista_maestros')
    else:
        form = MaestrosForm(instance=maestro)
    return render(request, 'editar_maestro.html', {'form': form, 'maestro': maestro})

def eliminar_maestro(request, id):
    maestro = get_object_or_404(Maestros, pk=id)
    maestro.delete()
    return redirect('lista_maestros')

# Vistas para Asignaturas
def lista_asignaturas(request):
    asignaturas = Asignaturas.objects.all()
    return render(request, 'lista_asignaturas.html', {'asignaturas': asignaturas})

def nueva_asignatura(request):
    if request.method == 'POST':
        form = AsignaturasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_asignaturas')
    else:
        form = AsignaturasForm()
    return render(request, 'nueva_asignatura.html', {'form': form})

def editar_asignatura(request, id):
    asignatura = get_object_or_404(Asignaturas, pk=id)
    if request.method == 'POST':
        form = AsignaturasForm(request.POST, instance=asignatura)
        if form.is_valid():
            form.save()
            return redirect('lista_asignaturas')
    else:
        form = AsignaturasForm(instance=asignatura)
    return render(request, 'editar_asignatura.html', {'form': form, 'asignatura': asignatura})

def eliminar_asignatura(request, id):
    asignatura = get_object_or_404(Asignaturas, pk=id)
    asignatura.delete()
    return redirect('lista_asignaturas')

# Vistas para Clases
def lista_clases(request):
    clases = Clases.objects.all()
    return render(request, 'lista_clases.html', {'clases': clases})

def nueva_clase(request):
    if request.method == 'POST':
        form = ClasesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clases')
    else:
        form = ClasesForm()
    return render(request, 'nueva_clase.html', {'form': form})

def editar_clase(request, id):
    clase = get_object_or_404(Clases, pk=id)
    if request.method == 'POST':
        form = ClasesForm(request.POST, instance=clase)
        if form.is_valid():
            form.save()
            return redirect('lista_clases')
    else:
        form = ClasesForm(instance=clase)
    return render(request, 'editar_clase.html', {'form': form, 'clase': clase})

def eliminar_clase(request, id):
    clase = get_object_or_404(Clases, pk=id)
    clase.delete()
    return redirect('lista_clases')

# Vistas para Alumnos
def lista_alumnos(request):
    alumnos = Alumnos.objects.all()
    return render(request, 'lista_alumnos.html', {'alumnos': alumnos})

def nuevo_alumno(request):
    if request.method == 'POST':
        form = AlumnosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_alumnos')
    else:
        form = AlumnosForm()
    return render(request, 'nuevo_alumno.html', {'form': form})

def editar_alumno(request, id):
    alumno = get_object_or_404(Alumnos, pk=id)
    if request.method == 'POST':
        form = AlumnosForm(request.POST, instance=alumno)
        if form.is_valid():
            form.save()
            return redirect('lista_alumnos')
    else:
        form = AlumnosForm(instance=alumno)
    return render(request, 'editar_alumno.html', {'form': form, 'alumno': alumno})

def eliminar_alumno(request, id):
    alumno = get_object_or_404(Alumnos, pk=id)
    alumno.delete()
    return redirect('lista_alumnos')

# Vistas para Calificaciones
def lista_calificaciones(request):
    calificaciones = Calificaciones.objects.all()
    return render(request, 'lista_calificaciones.html', {'calificaciones': calificaciones})

def nueva_calificacion(request):
    if request.method == 'POST':
        form = CalificacionesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_calificaciones')
    else:
        form = CalificacionesForm()
    return render(request, 'nueva_calificacion.html', {'form': form})

def editar_calificacion(request, id):
    calificacion = get_object_or_404(Calificaciones, pk=id)
    if request.method == 'POST':
        form = CalificacionesForm(request.POST, instance=calificacion)
        if form.is_valid():
            form.save()
            return redirect('lista_calificaciones')
    else:
        form = CalificacionesForm(instance=calificacion)
    return render(request, 'editar_calificacion.html', {'form': form, 'calificacion': calificacion})

def eliminar_calificacion(request, id):
    calificacion = get_object_or_404(Calificaciones, pk=id)
    calificacion.delete()
    return redirect('lista_calificaciones')

# Vistas para Eventos
def lista_eventos(request):
    eventos = Eventos.objects.all()
    return render(request, 'lista_eventos.html', {'eventos': eventos})

def nuevo_evento(request):
    if request.method == 'POST':
        form = EventosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_eventos')
    else:
        form = EventosForm()
    return render(request, 'nuevo_evento.html', {'form': form})

def editar_evento(request, id):
    evento = get_object_or_404(Eventos, pk=id)
    if request.method == 'POST':
        form = EventosForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('lista_eventos')
    else:
        form = EventosForm(instance=evento)
    return render(request, 'editar_evento.html', {'form': form, 'evento': evento})

def eliminar_evento(request, id):
    evento = get_object_or_404(Eventos, pk=id)
    evento.delete()
    return redirect('lista_eventos')