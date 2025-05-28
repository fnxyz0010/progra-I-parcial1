from Inputs import *

cantidad_participantes = 5
cantidad_jurados = 3

participantes = ingresar_participantes(cantidad_participantes)
puntajes = ingresar_puntajes(cantidad_jurados, cantidad_participantes)
promedios = calc_promedios(cantidad_jurados, puntajes)

# todo: hacer un menu para decidir que mostrar

mostrar_puntuaciones(cantidad_jurados, participantes, puntajes, promedios)
mostrar_promedios_menores_a(4, promedios, participantes)
mostrar_promedios_menores_a(8, promedios, participantes)
mostrar_promedio_jurados(promedios)
mostrar_jurado_estricto(promedios)
mostrar_jurado_generoso(promedios)
mostrar_participantes_puntuaciones_iguales(promedios, participantes)
# mostrar_participante_por_nombre(puntajes, participantes, cantidad_jurados)
