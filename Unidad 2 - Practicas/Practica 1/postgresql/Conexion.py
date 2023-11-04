import psycopg2
from psycopg2 import pool
from logger_base import log

class Conexion:
    _DATABASE = 'practica1_postgresql'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _PORT = '5432'
    _HOST = '127.0.0.1'
    _MIN_CON = 1
    _MAX_CON = 5
    _POOL = None

    @classmethod
    def ObtenerPool(cls):
        try:
            if cls._POOL == None:
                cls._POOL = pool.SimpleConnectionPool(
                    cls._MIN_CON,
                    cls._MAX_CON,
                    host = cls._HOST,
                    user = cls._USERNAME,
                    password = cls._PASSWORD,
                    port = cls._PORT,
                    database = cls._DATABASE
                )
                log.debug("Creacion del Pool", pool)
                return cls._POOL
            else:
                return cls._POOL
        except Exception as ex:
            log.error(ex)
    
    @classmethod
    def ObtenerConexion(cls):
        conexion = cls.ObtenerPool().getconn()
        log.debug(f"Conexion obtenida {conexion}")
        return conexion

    @classmethod
    def LiberarConexion(cls,conexion):
        cls.ObtenerPool().putconn(conexion)
        log.debug(f"Conexion regresada {conexion}")

    @classmethod
    def CerrarConexiones(cls):
        cls.ObtenerPool().closeall()
        log.debug(f"Conexiones cerradas")