class Medico:
    def __init__(self, codigo, nombre, especialidad):
        self._codigo = codigo
        self.nombre = nombre
        self.especialidad = especialidad

    @property
    def codigo(self):
        return self._codigo

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        if nombre.strip() == "":
            raise ValueError("El nombre no puede estar vacio")
        self._nombre = nombre

    @property
    def especialidad(self):
        return self._especialidad

    @especialidad.setter
    def especialidad(self, especialidad):
        if especialidad.strip() == "":
            raise ValueError("La especialidad no puede estar vacia")
        self._especialidad = especialidad

    def resumen(self):
        return (
            f"ID : {self._codigo} - "
            f"Medico : {self._nombre} - "
            f"Especialidad : {self._especialidad}"
        )