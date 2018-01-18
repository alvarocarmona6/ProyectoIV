# coding: utf-8
from fabric.api import *


def EliminarAplicacion():
	# Borramos directorio 
        run('sudo rm -rf ./ProyectoIV')


def InstalarAplicacion():

        #Primero elimino la aplicacion si la hubiese
        EliminarAplicacion()
        #Clono el repositorio
        run('git clone https://github.com/alvarocarmona6/ProyectoIV.git')


        #Herramientas
        run('sudo apt-get update') # Actualizar repositorios
        run('sudo apt -y update && sudo apt install -y python-minimal') #Python
        run('sudo apt-get install -y libpq-dev') #Postgre
        run('sudo apt-get install -y build-essential') #Requirements
        run('sudo apt-get install -y python-pip') #Pip
        run('sudo apt install gunicorn') #gunicorn

        #Dependencias
        run('pip install -r ~/ProyectoIV/requirements.txt')





def Iniciar():

        run('cd ./ProyectoIV &&  sudo gunicorn --config=config_gunicorn.py web:app -D', pty=False)
        run('cd ./ProyectoIV &&  sudo python bot/NBAbot.py', pty=False)
        
        
        
        
