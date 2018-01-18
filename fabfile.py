# coding: utf-8
from fabric.api import *


def EliminarAplicacion():
	# Borramos directorio 
        run('sudo rm -rf ./ProyectoIV')


def InstalacionAplicacion():

        EliminarAplicacion()
        run('git clone https://github.com/alvarocarmona6/ProyectoIV.git')


        #Herramientas
        run('sudo apt-get update') # Actualizar repositorios
        run('sudo apt -y update && sudo apt install -y python-minimal') #Python
        run('sudo apt-get install -y libpq-dev') #Postgre
        run('sudo apt-get install -y build-essential') #Requirements
        run('sudo apt-get install -y python-pip') #Pip
        run('sudo pip install gunicorn') #gunicorn

        #Dependencias
        run('cd ./ProyectoIV && sudo pip install -r requirements.txt')





def Iniciar():

        run('cd ./ProyectoIV && sudo sh prueba.sh', pty=False)
        
        
