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
    if largo(nombre) < 3:
        return False

    if not es_alfabetico(nombre):
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


def validar_numero(dato: str) -> bool:
    """Ingresa un dato y valida que sea un numero.

    Args:
        msg (str): Mensaje para mostrar.

    Returns:
        int | None: El dato convertido a numero o None si no es de valor numerico.
    """
    if not es_digito(dato):
        return False
    return True


def mostrar_puntuaciones(
    cant_jurados: int,
    participantes: list[str],
    puntajes: list[list[int]],
    promedios: list[float],
) -> None:
    for i in rango(fin=20):
        print("\n")

    print("################ PUNTUACIONES DE TODOS LOS PARTICIPANTES ################\n")

    for p in rango(fin=largo(participantes)):
        print(f"NOMBRE PARTICIPANTE: {participantes[p]}")
        for j in rango(fin=cant_jurados):
            print(f"PUNTAJE JURADO {j + 1}: {puntajes[j][p]}")
        print(f"PUNTAJE PROMEDIO: {promedios[p]:.2f}\n")

    input("Enter para continuar.")

    for i in rango(fin=20):
        print("\n")


def mostrar_promedios_menores_a(
    promedio: int, promedios: list[float], participantes: list[str]
) -> None:
    for i in rango(fin=20):
        print("\n")

    print(f"################ PROMEDIOS MENORES A {promedio} ################\n")

    sin_participantes = True
    for i in rango(fin=largo(promedios)):
        if int(promedios[i]) < promedio:
            print(f"NOMBRE PARTICIPANTE: {participantes[i]}")
            print(f"PROMEDIO: {promedios[i]:.2f}\n")
            sin_participantes = False
    if sin_participantes:
        print(f"No hay participantes con promedios menores a {promedio}.\n")

    input("Enter para continuar.")

    for i in rango(fin=20):
        print("\n")


def calc_promedios(cant_jurados: int, puntajes: list[list[int]]) -> list[float]:
    """Calcula los puntajes promedio por participante.

    Args:
        cant_jurados (int): Cantidad de jurados.
        puntajes (list[list[int]]): Matriz [jurado][participante] con los puntajes.

    Returns:
        list[float]: Lista de promedios por participante.
    """
    cant_participantes = largo(puntajes[0])
    promedios = [0.0] * cant_participantes

    for p in rango(fin=cant_participantes):
        suma = 0
        for j in rango(fin=cant_jurados):
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
    cant_jurados = largo(puntajes)
    promedios = [0.0] * cant_jurados

    for j in rango(fin=cant_jurados):
        suma = 0
        cantidad = largo(puntajes[j])
        for i in rango(fin=cantidad):
            suma += puntajes[j][i]
        promedios[j] = suma / cantidad

    return promedios


def mostrar_promedio_jurados(promedios: list[float]) -> None:
    for i in rango(fin=20):
        print("\n")

    print("################ PROMEDIO DE CADA JURADO ################\n")

    for i in rango(fin=largo(promedios)):
        print(f"JURADO {i + 1}: {promedios[i]:.2f}\n")

    input("Enter para continuar.")

    for i in rango(fin=20):
        print("\n")


def mostrar_jurado_estricto(promedios: list[float]) -> None:
    for i in rango(fin=20):
        print("\n")

    print("################ JURADO MAS ESTRICTO ################\n")

    promedio_mas_bajo = promedios[0]
    jurado = 0
    for i in rango(fin=largo(promedios)):
        if promedios[i] < promedio_mas_bajo:
            promedio_mas_bajo = promedios[i]
            jurado = i

    print(f"EL JURADO {jurado + 1} FUE EL MAS ESTRICTO.")
    print(f"PROMEDIO: {promedio_mas_bajo:.2f}\n")

    input("Enter para continuar.")

    for i in rango(fin=20):
        print("\n")


def mostrar_jurado_generoso(promedios: list[float]) -> None:
    for i in rango(fin=20):
        print("\n")

    print("################ JURADO MAS GENEROSO ################\n")

    promedio_mas_alto = promedios[0]
    jurado = 0
    for i in rango(fin=largo(promedios)):
        if promedios[i] > promedio_mas_alto:
            promedio_mas_alto = promedios[i]
            jurado = i

    print(f"EL JURADO {jurado + 1} FUE EL MAS GENEROSO.")
    print(f"PROMEDIO: {promedio_mas_alto:.2f}\n")

    input("Enter para continuar.")

    for i in rango(fin=20):
        print("\n")


def mostrar_participantes_puntuaciones_iguales(
    promedios: list[float], participantes: list[str]
):
    for i in rango(fin=20):
        print("\n")

    print("################ PUNTUACIONES IGUALES ################\n")

    indices_iguales = []
    for i in rango(fin=largo(promedios)):
        for j in rango(comienzo=i + 1, fin=largo(promedios)):
            if promedios[i] == promedios[j]:
                indices_iguales = agregar_a_lista(indices_iguales, i)
                indices_iguales = agregar_a_lista(indices_iguales, j)

    indices_iguales_unicos = filtrar_repetidos(indices_iguales)

    for i in rango(fin=largo(indices_iguales_unicos)):
        participante = participantes[indices_iguales_unicos[i]]
        print(f"NOMBRE PARTICIPANTE: {participante}")
        print(f"PROMEDIO: {promedios[indices_iguales_unicos[i]]:.2f}\n")

    input("Enter para continuar.")

    for i in rango(fin=20):
        print("\n")


def buscar_participante_por_nombre(participantes: list[str]) -> int:
    nombre = input("Buscar participante: ")
    for i in rango(fin=largo(participantes)):
        if nombre.lower() == participantes[i].lower():
            return i
    return -1


def mostrar_participante_por_nombre(
    puntajes: list[list[int]], participantes: list[str], cantidad_jurados: int
):
    for i in rango(fin=20):
        print("\n")

    print("################ PARTICIPANTE POR NOMBRE ################\n")

    indice = buscar_participante_por_nombre(participantes)

    if indice == -1:
        print("\nNo se encontro un participante con este nombre.\n")

        input("Enter para continuar.")

        for i in rango(fin=20):
            print("\n")

        return None

    print(f"\nPARTICIPANTE ENCONTRADO: {participantes[indice]}")

    suma = 0
    for i in rango(fin=largo(puntajes)):
        puntaje = puntajes[i][indice]
        print(f"JURADO {i + 1}: {puntaje}")
        suma += puntaje

    print(f"PROMEDIO: {(suma / cantidad_jurados):.2f}\n")

    input("Enter para continuar.")

    for i in rango(fin=20):
        print("\n")


# FUNCIONES DE UTILIDAD
def agregar_a_lista(lista: list, item) -> list:
    nueva_lista = [0] * (largo(lista) + 1)
    contador = 0
    for elemento in lista:
        nueva_lista[contador] = elemento
        contador += 1
    nueva_lista[contador] = item
    return nueva_lista


def filtrar_repetidos(lista: list) -> list:
    unicos = []
    for i in rango(fin=largo(lista)):
        en_lista = False
        for j in rango(fin=largo(unicos)):
            if lista[i] == unicos[j]:
                en_lista = True
                break
        if not en_lista:
            unicos = agregar_a_lista(unicos, lista[i])
    return unicos


def es_digito(item: str) -> bool:
    if item == "":
        return False
    for i in item:
        if i < "0" or i > "9":
            return False
    return True


def es_alfabetico(texto: str) -> bool:
    for i in texto:
        if i < "a" or i > "z":
            if i < "A" or i > "Z":
                return False
    return True


def largo(lista: list | str) -> int:
    cantidad = 0
    for _ in lista:
        cantidad += 1
    return cantidad


def rango(comienzo=0, fin=0) -> list[int]:
    cant_elementos = []
    while comienzo < fin:
        cant_elementos = agregar_a_lista(cant_elementos, comienzo)
        comienzo += 1
    return cant_elementos
