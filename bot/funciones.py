

lista_jugadores_puntos = {'Curry': 25 , 'Lebron' : 15, 'Harden': 10}
clasificacion_equipo = {'Cavaliers': 1 , 'Bulls' : 5 , 'Celtics' : 3 , 'Hornets' : 8 } 


def ObtenerPuntosJugadores(jugador):

        return lista_jugadores_puntos.get(jugador)


def ObtenerClasificacionEquipo(equipo):
        return clasificacion_equipo.get(equipo)


def ObtenerClasificacion():

        clasificacion_ordenada =sorted(clasificacion_equipo.items(), key=lambda clasificacion_equipo: clasificacion_equipo[1])
        return clasificacion_ordenada




