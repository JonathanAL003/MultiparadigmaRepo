from logger_base import log

class Producto:
    def __init__(self,id_producto = None, nombre = None, descripcion = None, precio = None, stock = None) -> None:
        self._id_producto = id_producto
        self._nombre = nombre
        self._descripcion = descripcion
        self._precio = precio
        self._stock = stock
    
    def __str__(self) -> str:
        return f"""
        ID PRODUCTO {self._id_producto}, Nombre: {self._nombre},
        Descripción: {self._descripcion}, Precio: {self._precio}, Stock: {self._stock}
        """
    
    @property
    def IdProducto(self):
        return self._id_producto
    @IdProducto.setter
    def IdProducto(self, id):
        self._id_producto = id
    
    @property
    def Nombre(self):
        return self._nombre
    @Nombre.setter
    def Nombre(self, nombre):
        self._nombre = nombre

    @property
    def Descripcion(self):
        return self._descripcion
    @Descripcion.setter
    def Descripcion(self, descripcion):
        self._descripcion = descripcion
    
    @property
    def Precio(self):
        return self._precio
    @Precio.setter
    def Precio(self, precio):
        self._precio = precio

    @property
    def Stock(self):
        return self._stock
    @Stock.setter
    def Stock(self, stock):
        self._stock = stock