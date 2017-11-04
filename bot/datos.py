import telebot 
import time 
import datetime
import psycopg2
import os
import urlparse

urlparse.uses_netloc.append("postgres")
url = urlparse.urlparse(os.environ["DATABASE_URL"])

def insertar_jugador(nombre,equipo):
	conn = psycopg2.connect(database=url.path[1:],user=url.username,password=url.password,host=url.hostname,port=url.port)
	cursor = conn.cursor()
	cursor.execute("Insert into jugador(nombre, equipo) values (%s, %s);", (nombre, equipo))
	conn.commit()
	cursor.close()
        conn.close()


def mostrar_jugador():
	array = []
	conn = psycopg2.connect(database=url.path[1:],user=url.username,password=url.password,host=url.hostname,port=url.port)
	cursor = conn.cursor()
	cursor.execute("select * from jugador;")
	for jugador in cursor:
		array.append(jugador[0])
	cursor.close()
	conn.close()
        return array
