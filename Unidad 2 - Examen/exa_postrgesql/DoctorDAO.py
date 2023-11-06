from Doctor import Doctor
from Conexion import Conexion
from CursorDelPool import CursorDelPool
from logger_base import log

class DoctorDAO:
    _SELECCIONAR = "SELECT id, nombre, numero_telefono FROM doctor ORDER BY id"
    _INSERTAR = "INSERT INTO doctor(nombre, numero_telefono) VALUES(%s, %s)"
    _ACTUALIZAR = "UPDATE doctor SET nombre = %s, numero_telefono = %s WHERE id = %s"
    _ELIMINAR = "DELETE FROM doctor WHERE id = %s"
    _DOCTORES_SIN_CITA = "select d.id, d.nombre, d.numero_telefono from doctor as d left join consulta as c on c.id_doctor = d.id where c.id_doctor is null"

    @classmethod
    def Seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            doctores = []
            for r in registros:
                doctores.append(Doctor(r[0],r[1],r[2]))
            return doctores
    
    @classmethod
    def Insertar(cls, doctor):
        with CursorDelPool() as cursor:
            valores = (doctor.Nombre, doctor.NumeroTelefono)
            cursor.execute(cls._INSERTAR, valores)
            return cursor.rowcount
    
    @classmethod
    def Actualizar(cls, doctor):
        with CursorDelPool() as cursor:
            valores = (doctor.Nombre, doctor.NumeroTelefono, doctor.Id)
            cursor.execute(cls._ACTUALIZAR, valores)
            return cursor.rowcount
    
    @classmethod
    def Eliminar(cls, doctor):
        with CursorDelPool() as cursor:
            valores = (doctor.Id,)
            cursor.execute(cls._ELIMINAR, valores)
            return cursor.rowcount
        
    @classmethod
    def ObtenerDoctorSinCitas(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._DOCTORES_SIN_CITA)
            registros = cursor.fetchall()
            doctores = []
            for r in registros:
                doctores.append(Doctor(r[0],r[1],r[2]))
            return doctores