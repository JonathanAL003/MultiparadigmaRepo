from Proveedor import Proveedor
from Conexion import Conexion
from CursorDelPool import CursorDelPool
from logger_base import log

class ProveedorDAO:
    _SELECCIONAR = "SELECT id_proveedor, nombre, rfc, curp, anio_fundacion FROM proveedor ORDER BY id_proveedor"
    _INSERTAR = "INSERT INTO proveedor(nombre, rfc, curp, anio_fundacion) VALUES(%s, %s, %s, %s)"
    _ACTUALIZAR = "UPDATE proveedor SET nombre = %s, rfc = %s, curp = %s, anio_fundacion = %s WHERE id_proveedor = %s"
    _ELIMINAR = "DELETE FROM proveedor WHERE id_proveedor = %s"

    @classmethod
    def Seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            proveedores = []
            for r in registros:
                proveedores.append(Proveedor(r[0],r[1],r[2],r[3],r[4]))
            return proveedores
    
    @classmethod
    def Insertar(cls, proveedor):
        with CursorDelPool() as cursor:
            valores = (proveedor.Nombre, proveedor.RFC, proveedor.CURP, proveedor.AnioFundacion)
            cursor.execute(cls._INSERTAR, valores)
            return cursor.rowcount
    
    @classmethod
    def Actualizar(cls, proveedor):
        with CursorDelPool() as cursor:
            valores = (proveedor.Nombre, proveedor.RFC, proveedor.CURP, proveedor.AnioFundacion, proveedor.IdProveedor)
            cursor.execute(cls._ACTUALIZAR, valores)
            return cursor.rowcount
    
    @classmethod
    def Eliminar(cls, proveedor):
        with CursorDelPool() as cursor:
            valores = (proveedor.IdProveedor,)
            cursor.execute(cls._ELIMINAR, valores)
            return cursor.rowcount