from fabric.api import *


def instalar():
        run('sudo git clone https://github.com/alvarocarmona6/ProyectoIV/')
        run('cd ./ProyectoIV && sudo pip install -r requirements.txt')

def servicios():
        run('cd ./ProyectoIV && sudo chmod +x prueba.sh', pty=False)
        run('cd ./ProyectoIV && sudo sh prueba.sh', pty=False)

def borrar():
        run('sudo rm -rf ./ProyectoIV')

def kill_py():
        run('sudo pkill python')
