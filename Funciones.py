"""
Todas las funciones deben estar documentadas.
"""

import re


def validar_nombre(nombre: str) -> bool:
    """Chequea si un nombre tiene al menos 3 caracteres y solo contiene letras y espacios.

    Args:
        nombre (str): Nombre del participante.

    Returns:
        bool: True si cumple con los requisitos, False si no cumple con los requisitos.
    """
    if len(nombre) < 3:
        return False

    if not bool(re.fullmatch(r"[A-Za-z\s]+", nombre)):
        return False

    return True


def validar_puntaje(puntaje: int) -> bool:
    """Chequea si el puntaje se encuentra entre 1 y 10.

    Args:
        puntaje (int): Puntaje

    Returns:
        bool: True si cumple con los requisitos, False si no cumple con los requisitos.
    """
    if puntaje < 1 or puntaje > 10:
        return False
    return True


def validar_numero(dato) -> bool:
    """Ingresa un dato y valida que sea un numero.

    Args:
        msg (str): Mensaje para mostrar.

    Returns:
        int | None: El dato convertido a numero o None si no es de valor numerico.
    """
    if not dato.isdigit():
        return False
    return True


def mostrar_puntuaciones(
    cant_jurados: int,
    participantes: list[str],
    puntajes: list[list[int]],
    promedios: list[float],
) -> None:
    print("-----PUNTUACIONES-----\n")

    for p in range(len(participantes)):
        print(f"NOMBRE PARTICIPANTE: {participantes[p]}")
        for j in range(cant_jurados):
            print(f"PUNTAJE JURADO {j + 1}: {puntajes[j][p]}")
        print(f"PUNTAJE PROMEDIO: {promedios[p]:.2f}\n")


def mostrar_promedios_menores_a(
    promedio: int, promedios: list[float], participantes: list[str]
) -> None:
    print(f"-----PROMEDIOS MENORES A {promedio}-----\n")

    sin_participantes = True
    for i in range(len(promedios)):
        if int(promedios[i]) < promedio:
            print(f"NOMBRE PARTICIPANTE: {participantes[i]}")
            print(f"PROMEDIO: {promedios[i]:.2f}\n")
            sin_participantes = False
    if sin_participantes:
        print(f"No hay participantes con promedios menores a {promedio}.\n")


def calc_promedios(cant_jurados: int, puntajes: list[list[int]]) -> list[float]:
    """Calcula los puntajes promedio por participante.

    Args:
        cant_jurados (int): Cantidad de jurados.
        puntajes (list[list[int]]): Matriz [jurado][participante] con los puntajes.

    Returns:
        list[float]: Lista de promedios por participante.
    """
    cant_participantes = len(puntajes[0])
    promedios = [0.0] * cant_participantes

    for p in range(cant_participantes):
        suma = 0
        for j in range(cant_jurados):
            suma += puntajes[j][p]
        promedios[p] = suma / cant_jurados

    return promedios


def calc_promedio_jurados(puntajes: list[list[int]]) -> list[float]:
    """Calcula el promedio de puntajes dados por cada jurado.

    Args:
        puntajes (list[list[int]]): Matriz [jurado][participante] con los puntajes.

    Returns:
        list[float]: Lista de promedios por jurado.
    """
    cant_jurados = len(puntajes)
    promedios = [0.0] * cant_jurados

    for j in range(cant_jurados):
        suma = 0
        cantidad = len(puntajes[j])
        for i in range(cantidad):
            suma += puntajes[j][i]
        promedios[j] = suma / cantidad

    return promedios


def mostrar_promedio_jurados(promedios: list[float]) -> None:
    print("-----PROMEDIO DE CADA JURADO-----\n")
    for i in range(len(promedios)):
        print(f"JURADO {i + 1}: {promedios[i]:.2f}")


def mostrar_jurado_estricto(promedios: list[float]) -> None:
    print("-----JURADO MAS ESTRICTO-----\n")
    promedio_mas_bajo = promedios[0]
    jurado = 0
    for i in range(len(promedios)):
        if promedios[i] < promedio_mas_bajo:
            promedio_mas_bajo = promedios[i]
            jurado = i

    print(f"EL JURADO {jurado + 1} FUE EL MAS ESTRICTO.")
    print(f"PROMEDIO: {promedio_mas_bajo:.2f}\n")


def mostrar_jurado_generoso(promedios: list[float]) -> None:
    print("-----JURADO MAS GENEROSO-----\n")
    promedio_mas_alto = promedios[0]
    jurado = 0
    for i in range(len(promedios)):
        if promedios[i] > promedio_mas_alto:
            promedio_mas_alto = promedios[i]
            jurado = i

    print(f"EL JURADO {jurado + 1} FUE EL MAS GENEROSO.")
    print(f"PROMEDIO: {promedio_mas_alto:.2f}\n")


def mostrar_participantes_puntuaciones_iguales(promedios: list[float]) -> list[int]:
    print("-----PARTICIPANTES CON PUNTUACIONES IGUALES-----\n")

    length = len(promedios)
    posiciones_repetidas = [0] * length
    contador = 0

    for i in range(length):
        encontrado = False
        for j in range(length):
            if i != j and promedios[i] == promedios[j]:
                encontrado = True
                break
        if encontrado:
            ya_esta = False
            for k in range(contador):
                if posiciones_repetidas[k] == i:
                    ya_esta = True
                    break
            if not ya_esta:
                posiciones_repetidas[contador] = i
                contador += 1

    return posiciones_repetidas[:contador]


def buscar_participante_por_nombre(participantes):
    print("-----PARTICIPANTE POR NOMBRE-----\n")
    nombre = input("Nombre del participante: ")
    for i in range(len(participantes)):
        if nombre.lower() == participantes[i].lower():
            return i
    return -1


def mostrar_participante_por_nombre(
    puntajes: list[list[int]], participantes: list[str], cantidad_jurados: int
) -> None:
    pos = buscar_participante_por_nombre(participantes)

    if pos == -1:
        print("No se encontro un participante con este nombre.")
        return None

    print(f"NOMBRE PARTICIPANTE: {participantes[pos]}")

    suma = 0
    for i in range(len(puntajes[pos])):
        print(f"JURADO {i + 1}: {puntajes[pos][i]}")
        suma += puntajes[pos][i]

    print(f"PUNTAJE PROMEDIO: {(suma / cantidad_jurados):.2f}/10\n")


# [0, 0, 0, 0, 0]

# [
#  [0, 0, 0],
#  [0, 0, 0],
#  [0, 0, 0],
#  [0, 0, 0],
#  [0, 0, 0],
# ]
