from paciente import Paciente
from medico import Medico
from cita import Cita
from sistema_kawsay import SistemaKawsay


especialidades = [
    "Medicina General",
    "Pediatria",
    "Ginecologia y Obstetricia",
    "Topico",
    "Odontologia"
]


def registrar_paciente(sistema):

    print("\n--- REGISTRAR PACIENTE ---")

    try:
        codigo = input("Codigo del paciente (ejemplo: P004): ")
        nombre = input("Nombre del paciente: ")
        edad = int(input("Edad: "))

        sistema.crear_persona(
            "paciente",
            codigo,
            nombre,
            edad
        )

        print("Paciente registrado correctamente.")

    except ValueError as e:
        print(f"Error: {e}")


def registrar_medico(sistema):

    print("\n--- REGISTRAR MEDICO ---")

    try:
        codigo = input("Codigo del medico (ejemplo: M007): ")
        nombre = input("Nombre del medico: ")

        print("\nEspecialidades disponibles:")

        for i in range(len(especialidades)):
            print(f"{i + 1}. {especialidades[i]}")

        opcion = int(input("Seleccione una especialidad: "))

        if opcion < 1 or opcion > len(especialidades):
            raise ValueError("Opcion de especialidad no valida")

        especialidad = especialidades[opcion - 1]

        sistema.crear_persona(
            "medico",
            codigo,
            nombre,
            especialidad
        )

        print("Medico registrado correctamente.")

    except ValueError as e:
        print(f"Error: {e}")


def buscar_por_codigo(sistema):

    print("\n--- BUSCAR POR CODIGO ---")

    codigo = input("Ingrese el codigo: ")

    resultado = sistema.buscar_por_codigo(codigo)

    if resultado is None:
        print("No se encontro ningun registro.")
        return

    if isinstance(resultado, Paciente):

        print("\nPaciente encontrado:")
        print(resultado.resumen())

        citas = sistema.obtener_citas_paciente(
            resultado.codigo
        )

        if len(citas) == 0:
            print("No tiene citas registradas.")
        else:
            print("\nCitas del paciente:")

            for cita in citas:
                print(cita.resumen())

        atenciones = []

        for cita in citas:
            atenciones_cita = sistema.obtener_atenciones_cita(
                cita.codigo
            )

            for atencion in atenciones_cita:
                atenciones.append(atencion)

        if len(atenciones) == 0:
            print("\nNo tiene atenciones registradas.")
        else:
            print("\nAtenciones del paciente:")

            for atencion in atenciones:
                print(atencion.resumen())

    elif isinstance(resultado, Medico):

        print("\nMedico encontrado:")
        print(resultado.resumen())

        citas = sistema.obtener_citas_medico(
            resultado.codigo
        )

        if len(citas) == 0:
            print("No tiene citas registradas.")
        else:
            print("\nCitas del medico:")

            for cita in citas:
                print(cita.resumen())

    elif isinstance(resultado, Cita):

        print("\nCita encontrada:")
        print(resultado.resumen())

        atenciones = sistema.obtener_atenciones_cita(
            resultado.codigo
        )

        if len(atenciones) == 0:
            print("Esta cita aun no ha sido atendida.")
        else:
            print("\nAtenciones de la cita:")

            for atencion in atenciones:
                print(atencion.resumen())


def programar_cita(sistema):

    print("\n--- PROGRAMAR CITA ---")

    try:
        codigo = input(
            "Codigo de cita (ejemplo C004): "
        )

        cod_paciente = input(
            "Codigo del paciente (ejemplo P001): "
        )

        cod_medico = input(
            "Codigo del medico (ejemplo M001): "
        )

        print("\nIngrese la fecha de la cita.")

        anio = int(input("Año: "))
        mes = int(input("Mes: "))
        dia = int(input("Dia: "))

        if anio <= 0:
            raise ValueError(
                "El año debe ser mayor que 0"
            )

        if mes < 1 or mes > 12:
            raise ValueError(
                "El mes debe estar entre 1 y 12"
            )

        if dia < 1 or dia > 31:
            raise ValueError(
                "El dia debe estar entre 1 y 31"
            )

        fecha = f"{anio:04d}-{mes:02d}-{dia:02d}"

        print("\nIngrese la hora de la cita.")
        print("Horario permitido: 07:00 a 15:00.")

        hora = int(input("Hora: "))
        minuto = int(input("Minuto: "))

        if hora < 7 or hora > 15:
            raise ValueError(
                "La hora debe estar entre 07:00 y 15:00"
            )

        if minuto < 0 or minuto > 59:
            raise ValueError(
                "Los minutos deben estar entre 00 y 59"
            )

        if hora == 15 and minuto > 0:
            raise ValueError(
                "La hora maxima permitida es 15:00"
            )

        hora_formato = f"{hora:02d}:{minuto:02d}"

        sistema.programar_cita(
            codigo,
            cod_paciente,
            cod_medico,
            fecha,
            hora_formato
        )

        print("Cita programada correctamente.")

    except ValueError as e:
        print(f"Error: {e}")


def registrar_atencion(sistema):

    print("\n--- REGISTRAR ATENCION ---")

    try:
        codigo = input(
            "Codigo de cita (ejemplo C002): "
        )

        diagnostico = input(
            "Diagnostico: "
        )

        observaciones = input(
            "Observaciones: "
        )

        sistema.registrar_atencion(
            codigo,
            diagnostico,
            observaciones
        )

        print("Atencion registrada correctamente.")

    except ValueError as e:
        print(f"Error: {e}")


def mostrar_pacientes(sistema):

    print("\n--- PACIENTES ---")

    if len(sistema.pacientes) == 0:
        print("No hay pacientes registrados.")
        return

    for paciente in sistema.pacientes.values():
        print(paciente.resumen())


def mostrar_medicos(sistema):

    while True:

        print("\n--- MEDICOS ---")
        print("1. Todos los medicos")

        for i in range(len(especialidades)):
            print(
                f"{i + 2}. "
                f"{especialidades[i]}"
            )

        print(f"{len(especialidades) + 2}. Volver")

        opcion = input("Seleccione una opcion: ")

        try:

            opcion = int(opcion)

            if opcion == 1:

                if len(sistema.medicos) == 0:
                    print("No hay medicos registrados.")
                else:
                    for medico in sistema.medicos.values():
                        print(medico.resumen())

            elif opcion >= 2 and opcion <= len(especialidades) + 1:

                especialidad = especialidades[opcion - 2]

                medicos = sistema.filtrar_medicos_por_especialidad(
                    especialidad
                )

                print(
                    f"\n--- MEDICOS DE "
                    f"{especialidad.upper()} ---"
                )

                if len(medicos) == 0:
                    print(
                        "No hay medicos registrados "
                        "en esta especialidad."
                    )
                else:
                    for medico in medicos:
                        print(medico.resumen())

            elif opcion == len(especialidades) + 2:
                break

            else:
                print("Opcion no valida.")

        except ValueError:
            print("Debe ingresar un numero.")


def mostrar_citas(sistema):

    print("\n--- CITAS ---")

    if len(sistema.citas) == 0:
        print("No hay citas registradas.")
        return

    for cita in sistema.citas.values():
        print(cita.resumen())


def mostrar_citas_atendidas(sistema):

    print("\n--- CITAS ATENDIDAS ---")

    if len(sistema.historial_atenciones) == 0:
        print("No hay citas atendidas.")
        return

    for atencion in sistema.historial_atenciones:
        print(atencion.resumen())


def mostrar_registros(sistema):

    while True:

        print("\n--- MOSTRAR REGISTROS ---")
        print("1. Mostrar Pacientes")
        print("2. Mostrar Medicos")
        print("3. Mostrar Citas")
        print("4. Mostrar Citas Atendidas")
        print("5. Volver")

        opcion = input("Seleccione una opcion: ")

        match opcion:

            case "1":
                mostrar_pacientes(sistema)

            case "2":
                mostrar_medicos(sistema)

            case "3":
                mostrar_citas(sistema)

            case "4":
                mostrar_citas_atendidas(sistema)

            case "5":
                break

            case _:
                print("Opcion no valida.")


def main():

    sistema = SistemaKawsay()

    while True:

        print("\n==============================")
        print("       SISTEMA KAWSAY")
        print("==============================")
        print("1. Registrar Paciente")
        print("2. Registrar Medico")
        print("3. Buscar por Codigo")
        print("4. Programar Cita")
        print("5. Registrar Atencion")
        print("6. Mostrar Registros")
        print("7. Salir")
        print("==============================")

        opcion = input("Seleccione una opcion: ")

        match opcion:

            case "1":
                registrar_paciente(sistema)

            case "2":
                registrar_medico(sistema)

            case "3":
                buscar_por_codigo(sistema)

            case "4":
                programar_cita(sistema)

            case "5":
                registrar_atencion(sistema)

            case "6":
                mostrar_registros(sistema)

            case "7":
                print("Saliendo del Sistema Kawsay...")
                break

            case _:
                print("Opcion no valida.")


if __name__ == "__main__":
    main()