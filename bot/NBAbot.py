import telebot 
from telebot import types 
from telebot import util
import time # Libreria para hacer que el programa que controla el bot no se acabe.
import ObtenerClasificacion as fun
import os

bot = telebot.TeleBot("420201411:AAEOSUZRDddSvFdqTsWNipk5Aj2IKRYzkz4")

def listener(messages): # Con esto, estamos definiendo una funcion llamada 'listener', que recibe como parametro un dato llamado 'messages'.
	for m in messages: # Por cada dato 'm' en el dato 'messages'
        	if m.content_type == 'text': # Filtramos mensajes que sean tipo texto.
			cid = m.chat.id # Almacenaremos el ID de la conversacion.
		    	print ("[" + str(cid) + "]: " + m.text) # Y haremos que imprima algo parecido a esto -> [52033876]: /start

bot.set_update_listener(listener)

@bot.message_handler(commands=['clasificacion']) 
def clasificacion(m): # Definimos una funcion que resuelva lo que necesitemos.
	
	cid = m.chat.id # Guardamos el ID de la conversacion para poder responder.
	mensaje= fun.Clasificacion()
	bot.send_message( cid, mensaje)


bot.set_update_listener(listener)

bot.polling(none_stop=True)
