from logger_base import log

class Doctor:
    def __init__(self, id=None,nombre=None,numero_telefono=None) -> None:
        self._id = id
        self._nombre = nombre
        self._numero_telefono = numero_telefono
    
    def __str__(self) -> str:
        return f"""
        ID DOCTOR {self._id}, 
        Nombre: {self._nombre},
        Numero De Teléfono: {self._numero_telefono}
        """

    @property
    def Id(self):
        return self._id
    @Id.setter
    def Id(self, id):
        self._id = id

    @property
    def Nombre(self):
        return self._nombre
    @Nombre.setter
    def Nombre(self, nombre):
        self._nombre = nombre

    @property
    def NumeroTelefono(self):
        return self._numero_telefono
    @NumeroTelefono.setter
    def NumeroTelefono(self, numero_telefono):
        self._numero_telefono = numero_telefono