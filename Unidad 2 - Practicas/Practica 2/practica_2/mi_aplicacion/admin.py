from django.contrib import admin
from .models import Maestros, Asignaturas, Clases, Alumnos, Calificaciones, Eventos

admin.site.register(Maestros)
admin.site.register(Asignaturas)
admin.site.register(Clases)
admin.site.register(Alumnos)
admin.site.register(Calificaciones)
admin.site.register(Eventos)
