from Producto import Producto
from Conexion import Conexion
from CursorDelPool import CursorDelPool
from logger_base import log

class ProductoDAO:
    _SELECCIONAR = "SELECT id_producto, nombre, descripcion, precio, stock FROM producto ORDER BY id_producto"
    _INSERTAR = "INSERT INTO producto(nombre, descripcion, precio, stock) VALUES(%s, %s, %s, %s)"
    _ACTUALIZAR = "UPDATE producto SET nombre = %s, descripcion = %s, precio = %s, stock = %s WHERE id_producto = %s"
    _ELIMINAR = "DELETE FROM producto WHERE id_producto = %s"

    @classmethod
    def Seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            productos = []
            for r in registros:
                productos.append(Producto(r[0],r[1],r[2],r[3],r[4]))
            return productos
    
    @classmethod
    def Insertar(cls, producto):
        with CursorDelPool() as cursor:
            valores = (producto.Nombre, producto.Descripcion, producto.Precio, producto.Stock)
            cursor.execute(cls._INSERTAR, valores)
            return cursor.rowcount
    
    @classmethod
    def Actualizar(cls, producto):
        with CursorDelPool() as cursor:
            valores = (producto.Nombre, producto.Descripcion, producto.Precio, producto.Stock, producto.IdProducto)
            cursor.execute(cls._ACTUALIZAR, valores)
            return cursor.rowcount
    
    @classmethod
    def Eliminar(cls, producto):
        with CursorDelPool() as cursor:
            valores = (producto.IdProducto,)
            cursor.execute(cls._ELIMINAR, valores)
            return cursor.rowcount