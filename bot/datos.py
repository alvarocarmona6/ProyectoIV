import telebot 
import time 
import datetime
import psycopg2
import os
import urlparse

urlparse.uses_netloc.append("postgres")
url = urlparse.urlparse("postgres://ibsqzhxgjddkrv:e63327f87dab947e1a3499e583d38d5d74eb9b01e14839d3a69e5912688b5285@ec2-54-75-231-85.eu-west-1.compute.amazonaws.com:5432/dcloadl8hlor2p")

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
