from Inputs import *
from Funciones import *

cantidad_participantes = 5
cantidad_jurados = 3

print("################### INGRESA A LOS PARTICIPANTES ###################\n")
participantes = ingresar_participantes(cantidad_participantes)

print("\n")

print("################ INGRESA EL PUNTAJE DE LOS JURADOS ################\n")
puntajes = ingresar_puntajes(cantidad_jurados, cantidad_participantes)

print("\n")

promedios = calc_promedios(cantidad_jurados, puntajes)

for i in rango(fin=20):
    print("\n")

while True:
    print("Que queres hacer?\n")
    print("\t - 1: Mostrar las puntuaciones de todos los participantes")
    print("\t - 2: Mostrar los promedios menores a 4")
    print("\t - 3: Mostrar los promedios menores a 8")
    print("\t - 4: Mostrar el promedio de jurados")
    print("\t - 5: Mostrar el jurado mas estricto")
    print("\t - 6: Mostrar el jurado mas generoso")
    print("\t - 7: Mostrar participantes con misma puntuacion (promedio)")
    print("\t - 8: Buscar un participante por nombre")
    print("\t - 0: Salir.\n")

    comando = input("Comando (1-8): ")

    if not es_digito(comando):
        for i in rango(fin=20):
            print("\n")
        print("Comando invalido: elegir entre 1 y 8.\n")
        input("Enter para continuar.")
        for i in rango(fin=20):
            print("\n")
        continue

    match int(comando):
        case 0:
            break
        case 1:
            mostrar_puntuaciones(cantidad_jurados, participantes, puntajes, promedios)
            continue
        case 2:
            mostrar_promedios_menores_a(4, promedios, participantes)
            continue
        case 3:
            mostrar_promedios_menores_a(8, promedios, participantes)
            continue
        case 4:
            mostrar_promedio_jurados(promedios)
            continue
        case 5:
            mostrar_jurado_estricto(promedios)
            continue
        case 6:
            mostrar_jurado_generoso(promedios)
            continue
        case 7:
            mostrar_participantes_puntuaciones_iguales(promedios, participantes)
            continue
        case 8:
            mostrar_participante_por_nombre(puntajes, participantes, cantidad_jurados)
            continue
        case _:
            print("Comando invalido: elegir entre 1 y 8.")
            continue
