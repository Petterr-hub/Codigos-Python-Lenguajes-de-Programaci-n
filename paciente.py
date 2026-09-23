class Paciente:
    def __init__(self, codigo, nombre, edad):
        self._codigo = codigo
        self.nombre = nombre
        self.edad = edad

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
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        if edad < 0 or edad > 120:
            raise ValueError("La edad debe estar entre 0 y 120")
        self._edad = edad

    def resumen(self):
        return (
            f"ID : {self._codigo} - "
            f"Paciente : {self._nombre} - "
            f"Edad : {self._edad}"
        )