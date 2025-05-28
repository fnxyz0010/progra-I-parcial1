from Funciones import *


def ingresar_participantes(num_participantes: int) -> list[str]:
    participantes = [""] * num_participantes
    contador = 0

    while True:
        if contador >= num_participantes:
            break

        p = input(f"NOMBRE PARTICIPANTE {contador + 1}: ")

        if not validar_nombre(p):
            print(
                "El nombre debe tener al menos 3 caracteres y solo contener letras y espacios."
            )
            continue

        participantes[contador] = p
        contador += 1

    return participantes


def ingresar_puntajes(num_jurados: int, num_participantes: int) -> list[list[int]]:
    puntajes = [[0 for _ in range(num_participantes)] for _ in range(num_jurados)]
    participante = 0
    jurado = 0

    for i in range(num_participantes):
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
