import telebot 
from telebot import types 
from telebot import util
import time 
import funciones as fun
import os

TOKEN = os.environ['TOKEN']
bot = telebot.TeleBot(TOKEN)

def listener(messages): 
	for m in messages: 
        	if m.content_type == 'text': 
			cid = m.chat.id 
		    	print ("[" + str(cid) + "]: " + m.text) 

bot.set_update_listener(listener)

@bot.message_handler(commands=['hola']) 
def hola(m): #
	
	cid = m.chat.id # Guardamos el ID de la conversacion para poder responder.
	mensaje= "Hola este bot te informará sobre la NBA, escribe /clasificacion para ver la clasificacion actual de la NBA, gracias :) "
	bot.send_message( cid, mensaje)


bot.set_update_listener(listener)


@bot.message_handler(commands=['clasificacion']) 
def clasificacion(m): # Definimos una funcion que resuelva lo que necesitemos.
	
	cid = m.chat.id # Guardamos el ID de la conversacion para poder responder.
	mensaje= fun.Clasificacion()
	bot.send_message( cid, mensaje)


bot.set_update_listener(listener)

bot.polling(none_stop=True)
