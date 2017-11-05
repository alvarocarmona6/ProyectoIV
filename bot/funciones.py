from bs4 import BeautifulSoup
import requests
import html5lib
import re 

lista_jugadores_puntos = {'Curry': 25 , 'Lebron' : 15, 'Harden': 10}
clasificacion_equipo = {'Cavaliers': 1 , 'Bulls' : 5 , 'Celtics' : 3 , 'Hornets' : 8 } 


def ObtenerPuntosJugadores(jugador):

        return lista_jugadores_puntos.get(jugador)


def ObtenerClasificacionEquipo(equipo):
        return clasificacion_equipo.get(equipo)


def ObtenerClasificacion():

        clasificacion_ordenada =sorted(clasificacion_equipo.items(), key=lambda clasificacion_equipo: clasificacion_equipo[1])
        return clasificacion_ordenada




def Saludo():

        mensaje = "Hola este bot te informara sobre la NBA, escribe /clasificacion para ver la clasificacion actual de la NBA, gracias :) "

        return mensaje




def Clasificacion():
        req = requests.get('http://www.20minutos.es/deportes/estadisticas/nba/standings_conference.asp')

        soup = BeautifulSoup(req.text, "html5lib")

        puesto = soup.find_all('td', {'class' : 'shs1stCol shsNamD'})


        patron = re.compile('</span></span>(.*?)</a>')

        nombres= patron.findall(str(puesto))

        mensaje = ""
        mensaje = mensaje +"\nConferencia Este:\n"
        for x in range(len(nombres)):
                if(x == 15):
                        mensaje = mensaje +"\n\nConferencia Oeste:\n"
                        mensaje = mensaje +  "\nEn el puesto " + str(x-14) + " " + nombres[x]
                elif(x>15):
                        mensaje = mensaje + "\nEn el puesto " + str(x-14) + " " +  nombres[x]

                else:
                        mensaje = mensaje +  "\nEn el puesto " + str(x+1) + " " + nombres[x]

        return mensaje





	
