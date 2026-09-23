class Atencion:
    def __init__(self, cita, diagnostico, observaciones):
        self._cita = cita
        self.diagnostico = diagnostico
        self.observaciones = observaciones

    @property
    def cita(self):
        return self._cita

    @property
    def diagnostico(self):
        return self._diagnostico

    @diagnostico.setter
    def diagnostico(self, valor):
        if valor.strip() == "":
            raise ValueError("El diagnostico no puede estar vacio")
        self._diagnostico = valor

    @property
    def observaciones(self):
        return self._observaciones

    @observaciones.setter
    def observaciones(self, valor):
        if valor.strip() == "":
            raise ValueError("Las observaciones no pueden estar vacias")
        self._observaciones = valor

    def resumen(self):
        return (
            f"Cita : {self._cita.codigo} - "
            f"Paciente : {self._cita.paciente.nombre} - "
            f"Medico : {self._cita.medico.nombre} - "
            f"Fecha : {self._cita.fecha} - "
            f"Hora : {self._cita.hora} - "
            f"Diagnostico : {self._diagnostico} - "
            f"Observaciones : {self._observaciones}"
        )