from Juego import Juego
from Conexion import Conexion
from CursorDelPool import CursorDelPool
from logger_base import log

class JuegoDAO:
    _SELECCIONAR = "SELECT id_juego, nombre, desarrollador, anio_publicacion FROM juego ORDER BY id_juego"
    _INSERTAR = "INSERT INTO juego(nombre, desarrollador, anio_publicacion) VALUES(%s, %s, %s)"
    _ACTUALIZAR = "UPDATE juego SET nombre = %s, desarrollador = %s, anio_publicacion = %s WHERE id_juego = %s"
    _ELIMINAR = "DELETE FROM juego WHERE id_juego = %s"

    @classmethod
    def Seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            juegos = []
            for r in registros:
                juegos.append(Juego(r[0],r[1],r[2],r[3]))
            return juegos
    
    @classmethod
    def Insertar(cls, juego):
        with CursorDelPool() as cursor:
            valores = (juego.Nombre, juego.Desarrollador, juego.AnioPublicacion)
            cursor.execute(cls._INSERTAR, valores)
            return cursor.rowcount
    
    @classmethod
    def Actualizar(cls, juego):
        with CursorDelPool() as cursor:
            valores = (juego.Nombre, juego.Desarrollador, juego.AnioPublicacion, juego.IdJuego)
            cursor.execute(cls._ACTUALIZAR, valores)
            return cursor.rowcount
    
    @classmethod
    def Eliminar(cls, juego):
        with CursorDelPool() as cursor:
            valores = (juego.IdJuego,)
            cursor.execute(cls._ELIMINAR, valores)
            return cursor.rowcount