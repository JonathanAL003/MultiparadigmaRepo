from logger_base import log

class Juego:
    def __init__(self, id_juego=None,nombre=None,desarrollador=None,anio_publicacion=None) -> None:
        self._id_juego = id_juego
        self._nombre = nombre
        self._desarrollador = desarrollador 
        self._anio_publicacion = anio_publicacion
    
    def __str__(self) -> str:
        return f"""
        ID JUEGO {self._id_juego}, Nombre: {self._nombre},
        desarrollador: {self._desarrollador}, Año de Publicación: {self._anio_publicacion}
        """

    @property
    def IdJuego(self):
        return self._id_juego
    @IdJuego.setter
    def IdJuego(self, id_juego):
        self._id_juego = id_juego

    @property
    def Nombre(self):
        return self._nombre
    @Nombre.setter
    def Nombre(self, nombre):
        self._nombre = nombre

    @property
    def Desarrollador(self):
        return self._desarrollador
    @Desarrollador.setter
    def Desarrollador(self, desarrollador):
        self._desarrollador = desarrollador

    @property
    def AnioPublicacion(self):
        return self._anio_publicacion
    @AnioPublicacion.setter
    def AnioPublicacion(self, anio):
        self._anio_publicacion = anio