from django.shortcuts import render
from mi_aplicacion.models import Maestros, Asignaturas, Clases, Alumnos, Calificaciones, Eventos

def index(request):
    return render(request, 'bienvenido.html')

def lista_maestros(request):
    maestros = Maestros.objects.all()
    return render(request, 'mi_aplicacion/lista_maestros.html', {'maestros': maestros})

def lista_asignaturas(request):
    asignaturas = Asignaturas.objects.all()
    return render(request, 'mi_aplicacion/lista_asignaturas.html', {'asignaturas': asignaturas})

def lista_clases(request):
    clases = Clases.objects.all()
    return render(request, 'mi_aplicacion/lista_clases.html', {'clases': clases})

def lista_alumnos(request):
    alumnos = Alumnos.objects.all()
    return render(request, 'mi_aplicacion/lista_alumnos.html', {'alumnos': alumnos})

def lista_calificaciones(request):
    calificaciones = Calificaciones.objects.all()
    return render(request, 'mi_aplicacion/lista_calificaciones.html', {'calificaciones': calificaciones})

def lista_eventos(request):
    eventos = Eventos.objects.all()
    return render(request, 'mi_aplicacion/lista_eventos.html', {'eventos': eventos})
