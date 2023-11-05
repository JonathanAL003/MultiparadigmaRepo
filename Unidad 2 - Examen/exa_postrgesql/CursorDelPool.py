from logger_base import log
from Conexion import Conexion

class CursorDelPool:
    def __init__(self) -> None:
        self._conexion = None
        self._cursor = None

    def __enter__(self):                    #Se manda a llamar al inicio del with
        log.debug("Inicio bloque with")
        self._conexion = Conexion.ObtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor
    
    def __exit__(self, tipo_excepcion, valor_excepcion, detalle_excepcion):             #Se ejecuta cuando termina el bloque with o cuando ocurra un error dentro de él
        log.debug("Se ejecuta exit")
        if valor_excepcion:
            self._conexion.rollback()
        else:
            self._conexion.commit()
        self._cursor.close()
        Conexion.LiberarConexion(self._conexion)