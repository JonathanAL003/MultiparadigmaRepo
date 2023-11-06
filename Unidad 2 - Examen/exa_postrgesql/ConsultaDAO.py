from Consulta import Consulta
from Conexion import Conexion
from CursorDelPool import CursorDelPool
from logger_base import log

class ConsultaDAO:
    _SELECCIONAR = "SELECT id_animal, id_doctor, servicio, costo FROM consulta ORDER BY id_animal, id_doctor"
    _INSERTAR = "INSERT INTO consulta(id_animal, id_doctor, servicio, costo) VALUES(%s, %s, %s, %s)"
    _ACTUALIZAR = "UPDATE consulta SET servicio = %s, costo = %s WHERE id_animal = %s AND id_doctor = %s"
    _ELIMINAR = "DELETE FROM consulta WHERE id_animal = %s AND id_doctor = %s"
    _CONSULTA_DIA_ANTERIOR = "select c.id_animal, c.id_doctor, c.servicio, c.costo from consulta as c join animal as a on c.id_animal = a.id where a.fecha_ingreso = %s"

    @classmethod
    def Seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            consultas = []
            for r in registros:
                consultas.append(Consulta(r[0],r[1],r[2],r[3]))
            return consultas
    
    @classmethod
    def Insertar(cls, consulta):
        with CursorDelPool() as cursor:
            valores = (consulta.IdAnimal, consulta.IdDoctor, consulta.Servicio, consulta.Costo)
            cursor.execute(cls._INSERTAR, valores)
            return cursor.rowcount
    
    @classmethod
    def Actualizar(cls, consulta):
        with CursorDelPool() as cursor:
            valores = (consulta.Servicio, consulta.Costo, consulta.IdAnimal, consulta.IdDoctor)
            cursor.execute(cls._ACTUALIZAR, valores)
            return cursor.rowcount
    
    @classmethod
    def Eliminar(cls, consulta):
        with CursorDelPool() as cursor:
            valores = (consulta.IdAnimal, consulta.IdDoctor)
            cursor.execute(cls._ELIMINAR, valores)
            return cursor.rowcount
        
    @classmethod
    def DiaAnterior(cls, dia):
        with CursorDelPool() as cursor:
            valores = (dia,)
            registros = cursor.execute(cls._CONSULTA_DIA_ANTERIOR, valores)
            consultas = []
            for r in registros:
                consultas.append(Consulta(r[0],r[1],r[2],r[3]))
            return consultas
