import telebot 
from telebot import types 
from telebot import util
import time 
import funciones as fun
import funcionesdatos as fundatos
import os

TOKEN ='420201411:AAEdz3u2FZmA9kZ9O0cPDyl1YzPO390pw34'
bot = telebot.TeleBot(TOKEN)

def listener(messages): 
	for m in messages: 
        	if m.content_type == 'text': 
                        cid = m.chat.id 
                        print ("[" + str(cid) + "]: " + m.text) 

bot.set_update_listener(listener)


@bot.message_handler(commands=['hola']) 
def hola(m): 
	
	cid = m.chat.id 
	mensaje= fun.Saludo()
	bot.send_message( cid, mensaje)


bot.set_update_listener(listener)

@bot.message_handler(commands=['mejorjugador']) 
def mejorjugador(m): 
	
        
	cid = m.chat.id 
	mensaje2= fundatos.MejorJugador()
	bot.send_message( cid, mensaje2)


bot.set_update_listener(listener)





@bot.message_handler(commands=['clasificacion']) 
def clasificacion(m):
	
	cid = m.chat.id
	mensaje2= fun.Clasificacion()
	bot.send_message( cid, mensaje2)


bot.set_update_listener(listener)

bot.polling(none_stop=True)
