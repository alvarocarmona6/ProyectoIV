import datos


def MejorJugador():

        lista = datos.mostrar_jugador()
        mensaje = "El mejor jugador es " + lista[0]
        return mensaje

