from bs4 import BeautifulSoup
import requests
import html5lib
import re


def Clasificacion():
        req = requests.get('http://www.20minutos.es/deportes/estadisticas/nba/standings_conference.asp')

        soup = BeautifulSoup(req.text, "html5lib")

        puesto = soup.find_all('td', {'class' : 'shs1stCol shsNamD'})


        patron = re.compile('</span></span>(.*?)</a>')

        nombres= patron.findall(str(puesto))


        print("Conferencia Este:\n")
        for x in range(len(nombres)):
                if(x == 15):
                        print("Conferencia Oeste:\n")
                        print "En el puesto " + str(x-14) + " esta "+ nombres[x]
                elif(x>15):
                        print "En el puesto " + str(x-14) + " esta "+ nombres[x]

                else:
                        print "En el puesto " + str(x+1) + " esta "+ nombres[x]

	
