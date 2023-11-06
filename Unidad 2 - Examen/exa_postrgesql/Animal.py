from logger_base import log

class Animal:
    def __init__(self, id=None,raza=None,fecha_ingreso=None,fecha_salida=None) -> None:
        self._id = id
        self._raza = raza
        self._fecha_ingreso = fecha_ingreso 
        self._fecha_salida = fecha_salida
    
    def __str__(self) -> str:
        return f"""
        ID ANIMAL {self._id}, 
        Raza: {self._raza},
        Fecha De Ingreso (dd/mm/YYYY): {self._fecha_ingreso},
        Fecha De Salida (dd/mm/YYYY): {self._fecha_salida}
        """

    @property
    def Id(self):
        return self._id
    @Id.setter
    def Id(self, id):
        self._id = id

    @property
    def Raza(self):
        return self._raza
    @Raza.setter
    def Raza(self, raza):
        self._raza = raza

    @property
    def FechaIngreso(self):
        return self._fecha_ingreso
    @FechaIngreso.setter
    def FechaIngreso(self, fecha_ingreso):
        self._fecha_ingreso = fecha_ingreso

    @property
    def FechaSalida(self):
        return self._fecha_salida
    @FechaSalida.setter
    def FechaSalida(self, fecha_salida):
        self._fecha_salida = fecha_salida