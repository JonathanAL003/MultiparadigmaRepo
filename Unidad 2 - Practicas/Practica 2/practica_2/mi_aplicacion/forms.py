from django import forms
from .models import Maestros, Asignaturas, Clases, Alumnos, Calificaciones, Eventos

class MaestrosForm(forms.ModelForm):
    class Meta:
        model = Maestros
        fields = ['Nombre', 'Materia']

class AsignaturasForm(forms.ModelForm):
    class Meta:
        model = Asignaturas
        fields = ['Nombre', 'Maestro_ID']

class ClasesForm(forms.ModelForm):
    class Meta:
        model = Clases
        fields = ['Nombre', 'Asignatura_ID', 'Horario']

class AlumnosForm(forms.ModelForm):
    class Meta:
        model = Alumnos
        fields = ['Nombre', 'Edad', 'Grado', 'Maestro_ID']

class CalificacionesForm(forms.ModelForm):
    class Meta:
        model = Calificaciones
        fields = ['Alumno_ID', 'Asignatura_ID', 'Calificacion']

class EventosForm(forms.ModelForm):
    class Meta:
        model = Eventos
        fields = ['Nombre', 'Fecha', 'Responsable_ID']
