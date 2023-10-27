"""
URL configuration for practica_2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webapp.views import *
from mi_aplicacion.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),

    # URLs para Maestros
    path('lista_maestros', lista_maestros, name='lista_maestros'),
    path('nueva_maestro', nueva_maestro, name='nueva_maestro'),
    path('editar_maestro/<int:id>', editar_maestro, name='editar_maestro'),
    path('eliminar_maestro/<int:id>', eliminar_maestro, name='eliminar_maestro'),

    # URLs para Asignaturas
    path('lista_asignaturas', lista_asignaturas, name='lista_asignaturas'),
    path('nueva_asignatura', nueva_asignatura, name='nueva_asignatura'),
    path('editar_asignatura/<int:id>', editar_asignatura, name='editar_asignatura'),
    path('eliminar_asignatura/<int:id>', eliminar_asignatura, name='eliminar_asignatura'),

    # URLs para Clases
    path('lista_clases', lista_clases, name='lista_clases'),
    path('nueva_clase', nueva_clase, name='nueva_clase'),
    path('editar_clase/<int:id>', editar_clase, name='editar_clase'),
    path('eliminar_clase/<int:id>', eliminar_clase, name='eliminar_clase'),

    # URLs para Alumnos
    path('lista_alumnos', lista_alumnos, name='lista_alumnos'),
    path('nuevo_alumno', nuevo_alumno, name='nuevo_alumno'),
    path('editar_alumno/<int:id>', editar_alumno, name='editar_alumno'),
    path('eliminar_alumno/<int:id>', eliminar_alumno, name='eliminar_alumno'),

    # URLs para Calificaciones
    path('lista_calificaciones', lista_calificaciones, name='lista_calificaciones'),
    path('nueva_calificacion', nueva_calificacion, name='nueva_calificacion'),
    path('editar_calificacion/<int:id>', editar_calificacion, name='editar_calificacion'),
    path('eliminar_calificacion/<int:id>', eliminar_calificacion, name='eliminar_calificacion'),

    # URLs para Eventos
    path('lista_eventos', lista_eventos, name='lista_eventos'),
    path('nuevo_evento', nuevo_evento, name='nuevo_evento'),
    path('editar_evento/<int:id>', editar_evento, name='editar_evento'),
    path('eliminar_evento/<int:id>', eliminar_evento, name='eliminar_evento'),
]

