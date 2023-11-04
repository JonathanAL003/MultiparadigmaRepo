from logger_base import log

class Proveedor:
    def __init__(self, id_proveedor=None,nombre=None,rfc=None,curp=None,anio_fundacion=None) -> None:
        self._id_proveedor = id_proveedor
        self._nombre = nombre
        self._rfc = rfc
        self._curp = curp 
        self._anio_fundacion = anio_fundacion
    
    def __str__(self) -> str:
        return f"""
        ID PROVEEDOR {self._id_proveedor}, Nombre: {self._nombre},
        RFC: {self._rfc}, CURP: {self._curp},
        Año de Fundación: {self._anio_fundacion}
        """
    
    @property
    def IdProveedor(self):
        return self._id_proveedor
    @IdProveedor.setter
    def IdProveedor(self, id_provedor):
        self._id_proveedor = id_provedor

    @property
    def Nombre(self):
        return self._nombre
    @Nombre.setter
    def Nombre(self, nombre):
        self._nombre = nombre

    @property
    def RFC(self):
        return self._rfc
    @RFC.setter
    def RFC(self, rfc):
        self._rfc = rfc

    @property
    def CURP(self):
        return self._curp
    @CURP.setter
    def CURP(self, curp):
        self._curp = curp

    @property
    def AnioFundacion(self):
        return self._anio_fundacion
    @AnioFundacion.setter
    def AnioFundacion(self, anio):
        self._anio_fundacion = anio