from django.db import models

class Maestros(models.Model):
    ID_Maestro = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=255)
    Materia = models.CharField(max_length=255)

    def __str__(self):
        return f"Maestro {self.ID_Maestro}, Nombre: {self.Nombre}, Materia: {self.Materia}"

class Asignaturas(models.Model):
    ID_Asignatura = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=255)
    Maestro_ID = models.ForeignKey(Maestros, on_delete=models.CASCADE)

    def __str__(self):
        return f"Asignatura {self.ID_Asignatura}, Nombre: {self.Nombre}, MaestroID: {self.Maestro_ID}"

class Clases(models.Model):
    ID_Clase = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=255)
    Asignatura_ID = models.ForeignKey(Asignaturas, on_delete=models.CASCADE)
    Horario = models.CharField(max_length=255)

    def __str__(self):
        return f"Clase {self.ID_Clase}, Nombre: {self.Nombre}, AsignaturaID: {self.Asignatura_ID}, Horario: {self.Horario}"

class Alumnos(models.Model):
    ID_Alumno = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=255)
    Edad = models.IntegerField()
    Grado = models.CharField(max_length=255)
    Maestro_ID = models.ForeignKey(Maestros, on_delete=models.CASCADE)

    def __str__(self):
        return f"Alumno {self.ID_Alumno}, Nombre: {self.Nombre}, Edad: {self.Edad}, Grado: {self.Grado}, MaestroID: {self.Maestro_ID}"

class Calificaciones(models.Model):
    ID_Calificacion = models.AutoField(primary_key=True)
    Alumno_ID = models.ForeignKey(Alumnos, on_delete=models.CASCADE)
    Asignatura_ID = models.ForeignKey(Asignaturas, on_delete=models.CASCADE)
    Calificacion = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"CalificacionID {self.ID_Calificacion}, AlumnoID: Alumno {self.Alumno_ID}, AsignaturaID {self.Asignatura_ID}, Calificación {self.Calificacion}"

class Eventos(models.Model):
    ID_Evento = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=255)
    Fecha = models.DateField()
    Responsable_ID = models.ForeignKey(Maestros, on_delete=models.CASCADE)

    def __str__(self):
        return f"Evento {self.ID_Evento}, Nombre: {self.Nombre}, Fecha {self.Fecha}, ResponsableID: {self.Responsable_ID}"
