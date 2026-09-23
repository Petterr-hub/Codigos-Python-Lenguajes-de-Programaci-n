class Cita:
    def __init__(self, codigo, paciente, medico, fecha, hora):
        self._codigo = codigo
        self._paciente = paciente
        self._medico = medico
        self._fecha = fecha
        self._hora = hora

    @property
    def codigo(self):
        return self._codigo

    @property
    def paciente(self):
        return self._paciente

    @property
    def medico(self):
        return self._medico

    @property
    def fecha(self):
        return self._fecha

    @fecha.setter
    def fecha(self, valor):
        self._fecha = valor

    @property
    def hora(self):
        return self._hora

    @hora.setter
    def hora(self, valor):
        self._hora = valor

    def resumen(self):
        return (
            f"Cita : {self._codigo} - "
            f"Paciente : {self._paciente.nombre} - "
            f"Medico : {self._medico.nombre} - "
            f"Fecha : {self._fecha} - "
            f"Hora : {self._hora}"
        )