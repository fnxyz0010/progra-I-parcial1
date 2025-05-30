from Funciones import *


def ingresar_participantes(cantidad_participantes: int) -> list[str]:
    """Ingresa los nombres de los participantes.

    Args:
        cantidad_participantes (int): Cantidad de participantes a ingresar.

    Returns:
        list[str]: Lista de nombres de los participantes.
    """
    participantes = []
    contador = 0

    while True:
        if contador >= cantidad_participantes:
            break

        nombre = input(f"NOMBRE PARTICIPANTE {contador + 1}: ")
        if not validar_nombre(nombre):
            print(
                "El nombre debe tener al menos 3 caracteres y solo contener letras y espacios."
            )
            continue

        participantes = agregar_a_lista(participantes, nombre)
        contador += 1

    return participantes


def ingresar_puntajes(num_jurados: int, cant_participantes: int) -> list[list[int]]:
    """Ingresa los puntajes de los jurados para cada participante.

    Args:
        cant_jurados (int): Cantidad de jurados.
        cant_participantes (int): Cantidad de participantes.

    Returns:
        list[list[int]]: Matriz con los puntajes de cada jurado para cada participante.
    """
    puntajes = [
        [0 for _ in rango(fin=cant_participantes)] for _ in rango(fin=num_jurados)
    ]
    participante = 0
    jurado = 0

    for i in rango(fin=cant_participantes):
        print(f"PARTICIPANTE {i + 1}:")

        while True:
            if jurado >= num_jurados:
                break

            puntaje = input(f"PUNTAJE JURADO {jurado + 1} (1-10): ")

            if not validar_numero(puntaje):
                print("El puntaje debe ser un valor numerico.")
                continue

            puntaje = int(puntaje)

            if not validar_puntaje(puntaje):
                print("El puntaje debe ser un numero entre 1 y 10.")
                continue

            puntajes[jurado][participante] = puntaje
            jurado += 1

        print("\n")
        participante += 1
        jurado = 0
        i += 1

    return puntajes
