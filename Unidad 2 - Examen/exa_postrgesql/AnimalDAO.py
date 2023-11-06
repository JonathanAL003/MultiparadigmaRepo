from Animal import Animal
from Doctor import Doctor
from Conexion import Conexion
from CursorDelPool import CursorDelPool
from logger_base import log

class AnimalDAO:
    _SELECCIONAR = "SELECT id, raza, fecha_ingreso, fecha_salida FROM animal ORDER BY id"
    _INSERTAR = "INSERT INTO animal(raza, fecha_ingreso, fecha_salida) VALUES(%s, %s, %s)"
    _ACTUALIZAR = "UPDATE animal SET raza = %s, fecha_ingreso = %s, fecha_salida = %s WHERE id = %s"
    _ELIMINAR = "DELETE FROM animal WHERE id = %s"
    _OBTENER_ANIMALES_CON_DOCTOR = "SELECT a.id, a.raza, a.fecha_ingreso, a.fecha_salida, d.id, d.nombre, d.numero_telefono FROM consulta as c join animal as a on c.id_animal = a.id join doctor as d on c.id_doctor = d.id"
    _OBTENER_ANIMAL_ESP_CON_DOCTOR = "SELECT a.id, a.raza, a.fecha_ingreso, a.fecha_salida, d.id, d.nombre, d.numero_telefono FROM consulta as c join animal as a on c.id_animal = a.id join doctor as d on c.id_doctor = d.id WHERE a.id = %s"
    
    @classmethod
    def Seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            animales = []
            for r in registros:
                animales.append(Animal(r[0],r[1],r[2],r[3]))
            return animales
    
    @classmethod
    def Insertar(cls, animal):
        with CursorDelPool() as cursor:
            valores = (animal.Raza, animal.FechaIngreso, animal.FechaSalida)
            cursor.execute(cls._INSERTAR, valores)
            return cursor.rowcount
    
    @classmethod
    def Actualizar(cls, animal):
        with CursorDelPool() as cursor:
            valores = (animal.Raza, animal.FechaIngreso, animal.FechaSalida, animal.Id)
            cursor.execute(cls._ACTUALIZAR, valores)
            return cursor.rowcount
    
    @classmethod
    def Eliminar(cls, animal):
        with CursorDelPool() as cursor:
            valores = (animal.Id,)
            cursor.execute(cls._ELIMINAR, valores)
            return cursor.rowcount
        
    @classmethod
    def ObtenerAnimalesConDoctor(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._OBTENER_ANIMALES_CON_DOCTOR)
            registros = cursor.fetchall()
            animales = []
            for r in registros:
                anim = Animal(r[0],r[1],r[2],r[3]) 
                doct = Doctor(r[4], r[5], r[6])
                reg = str(f"Id Animal: {anim.Id}, Raza: {anim.Raza}, Fecha Ingreso: {anim.FechaIngreso}, Fecha Salida: {anim.FechaSalida}, Id Doctor {doct.Id}, Nombre: {doct.Nombre}, Numero Telefono: {doct.NumeroTelefono}")
                animales.append(reg)
            return animales
        
    @classmethod
    def ObtenerAnimalEspecificoConDoctor(cls, animal):
        with CursorDelPool() as cursor:
            valores = (animal.Id,)
            cursor.execute(cls._OBTENER_ANIMAL_ESP_CON_DOCTOR, valores)
            registros = cursor.fetchall()
            animales = []
            for r in registros:
                anim = Animal(r[0],r[1],r[2],r[3]) 
                doct = Doctor(r[4], r[5], r[6])
                reg = str(f"Id Animal: {anim.Id}, Raza: {anim.Raza}, Fecha Ingreso: {anim.FechaIngreso}, Fecha Salida: {anim.FechaSalida}, Id Doctor {doct.Id}, Nombre: {doct.Nombre}, Numero Telefono: {doct.NumeroTelefono}")
                animales.append(reg)
            return animales