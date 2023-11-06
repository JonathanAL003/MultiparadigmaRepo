from logger_base import log

class Consulta:
    def __init__(self, id_animal = None, id_doctor = None, servicio = None, costo = None) -> None:
        self._id_animal = id_animal
        self._id_doctor = id_doctor
        self._serivicio = servicio
        self._costo = costo

    def __str__(self) -> str:
        return f"""
        ID CONSULTA (ID ANIMAL: {self._id_animal} ID DOCTOR: {self._id_doctor}),
        Servicio: {self._serivicio},
        Costo: {self._costo}
        """
    
    @property
    def IdAnimal(self):
        return self._id_animal
    @IdAnimal.setter
    def IdAnimal(self, id_animal):
        self._id_animal = id_animal

    @property
    def IdDoctor(self):
        return self._id_doctor
    @IdDoctor.setter
    def IdDoctor(self, id_doctor):
        self._id_doctor = id_doctor

    @property
    def Servicio(self):
        return self._serivicio
    @Servicio.setter
    def Servicio(self, servicio):
        self._serivicio = servicio

    @property
    def Costo(self):
        return self._costo
    @Costo.setter
    def Costo(self, costo):
        self._costo = costo