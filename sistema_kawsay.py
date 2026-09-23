from paciente import Paciente
from medico import Medico
from cita import Cita
from atencion import Atencion


class SistemaKawsay:

    def __init__(self):
        self.pacientes = {}
        self.medicos = {}
        self.citas = {}
        self.historial_atenciones = []

        self.cargar_datos_prueba()

    def cargar_datos_prueba(self):

        self.crear_persona(
            "paciente",
            "P001",
            "Jorge Aguayo",
            28
        )

        self.crear_persona(
            "paciente",
            "P002",
            "Lucia Ramirez",
            35
        )

        self.crear_persona(
            "paciente",
            "P003",
            "Carlos Mendoza",
            19
        )

        self.crear_persona(
            "medico",
            "M001",
            "Marcos Fernandez",
            "Medicina General"
        )

        self.crear_persona(
            "medico",
            "M002",
            "Carla Flores",
            "Medicina General"
        )

        self.crear_persona(
            "medico",
            "M003",
            "Ana Torres",
            "Pediatria"
        )

        self.crear_persona(
            "medico",
            "M004",
            "Patricia Salazar",
            "Ginecologia y Obstetricia"
        )

        self.crear_persona(
            "medico",
            "M005",
            "Luis Herrera",
            "Topico"
        )

        self.crear_persona(
            "medico",
            "M006",
            "Diego Vargas",
            "Odontologia"
        )

        self.programar_cita(
            "C001",
            "P001",
            "M001",
            "2026-09-23",
            "09:00"
        )

        self.programar_cita(
            "C002",
            "P002",
            "M003",
            "2026-09-24",
            "10:30"
        )

        self.programar_cita(
            "C003",
            "P003",
            "M006",
            "2026-09-25",
            "14:00"
        )

        self.registrar_atencion(
            "C001",
            "Control general",
            "El paciente presenta una evolucion favorable."
        )

    def crear_persona(
        self,
        tipo,
        codigo,
        nombre,
        dato_extra
    ):

        if self.buscar_por_codigo(codigo):
            raise ValueError("El codigo ya existe")

        if tipo == "paciente":

            nuevo = Paciente(
                codigo,
                nombre,
                dato_extra
            )

            self.pacientes[codigo] = nuevo

        elif tipo == "medico":

            nuevo = Medico(
                codigo,
                nombre,
                dato_extra
            )

            self.medicos[codigo] = nuevo

        return nuevo

    def buscar_por_codigo(self, codigo):

        if codigo in self.pacientes:
            return self.pacientes[codigo]

        elif codigo in self.medicos:
            return self.medicos[codigo]

        elif codigo in self.citas:
            return self.citas[codigo]

        return None

    def programar_cita(
        self,
        cod_cita,
        cod_paciente,
        cod_medico,
        fecha,
        hora
    ):

        if cod_cita in self.citas:
            raise ValueError(
                "El codigo de cita ya existe"
            )

        paciente = self.pacientes.get(cod_paciente)
        medico = self.medicos.get(cod_medico)

        if paciente is None:
            raise ValueError(
                "El paciente no existe"
            )

        if medico is None:
            raise ValueError(
                "El medico no existe"
            )

        nueva_cita = Cita(
            cod_cita,
            paciente,
            medico,
            fecha,
            hora
        )

        self.citas[cod_cita] = nueva_cita

        return nueva_cita

    def registrar_atencion(
        self,
        cod_cita,
        diagnostico,
        observaciones
    ):

        if cod_cita not in self.citas:
            raise ValueError(
                "El codigo de cita no existe"
            )

        cita = self.citas[cod_cita]

        nueva_atencion = Atencion(
            cita,
            diagnostico,
            observaciones
        )

        self.historial_atenciones.append(
            nueva_atencion
        )

        return nueva_atencion

    def obtener_citas_paciente(self, codigo):

        citas = []

        for cita in self.citas.values():

            if cita.paciente.codigo == codigo:
                citas.append(cita)

        return citas

    def obtener_citas_medico(self, codigo):

        citas = []

        for cita in self.citas.values():

            if cita.medico.codigo == codigo:
                citas.append(cita)

        return citas

    def obtener_atenciones_cita(self, codigo_cita):

        atenciones = []

        for atencion in self.historial_atenciones:

            if atencion.cita.codigo == codigo_cita:
                atenciones.append(atencion)

        return atenciones

    def filtrar_medicos_por_especialidad(
        self,
        especialidad
    ):

        resultado = filter(
            lambda medico:
            medico.especialidad == especialidad,
            self.medicos.values()
        )

        return list(resultado)