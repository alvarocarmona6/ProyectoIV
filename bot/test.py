import funciones
import unittest

class Test(unittest.TestCase):
        
        def test_ComprobarClasificacionCorrecta(self): # Compruebo que los equipos estan entre 1 y 15 en la clasificacion
                self.assertTrue(1 <= funciones.ObtenerClasificacionEquipo('Cavaliers') <= 15)
                self.assertTrue(1 <= funciones.ObtenerClasificacionEquipo('Bulls') <= 15)
                self.assertTrue(1 <= funciones.ObtenerClasificacionEquipo('Celtics') <= 15)
                self.assertTrue(1 <= funciones.ObtenerClasificacionEquipo('Hornets') <= 15)
                


        def test_ComprobarTamanioClasificacion(self):
                self.assertEqual(len(funciones.ObtenerClasificacion()), 4)  #Compruebo que el tamanio de la lista de la clasificacion es 
                                                                            #4 ya que de momento tengo 4 equipos

        def test_ComprobarPuntuacionCorrecta(self): #Compruebo que los puntos de los jugadores estan en un rango considerable
                self.assertTrue( 0 <= funciones.ObtenerPuntosJugadores('Curry') <= 1000)
                self.assertTrue( 0 <= funciones.ObtenerPuntosJugadores('Lebron') <= 1000)
                self.assertTrue( 0 <= funciones.ObtenerPuntosJugadores('Harden') <= 1000)

if __name__ == '__main__':
        unittest.main()
                
