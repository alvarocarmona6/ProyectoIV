[![Build Status](https://travis-ci.org/alvarocarmona6/ProyectoIV.svg?branch=master)](https://travis-ci.org/alvarocarmona6/ProyectoIV)
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/alvarocarmona6/ProyectoIV)


# ProyectoIV 

# Bot NBA

Mi proyecto para este curso será crear un boot de Telegram, para dar información sobre la NBA como por ejemplo los resultados de los partidos, los maximos anotadores y la clasificación, se programará en Python. Se utilizará la tecnica web scraping para extraer información de paginas web con  una biblioteca de Python llamada Beautiful Soup para analizar los documentos HTML, por ejemplo una pagina para extraer información sobre la NBA podría ser la siguiente: [as](https://as.com/baloncesto/nba.html).

# Herramientas

* Python para la programación del Bot.
* API de Telegram.
* Biblioteca Beautiful Soup para extraer información.
* Base de datos (aun por determinar).
* Despliegue de la nube (posiblemente Microsoft Azure).


# Integración Continua
Para ello voy a usar TDD donde consiste en ir haciendo pruebas o test donde estos test se les pasa al código del proyecto para así poder ir desarrollando el proyecto de una manera más clara. Esto facilitará problemas en el futuro. Sí nuestro código pasa los test significa que va cumpliendo con los requisitos establecidos hasta el momento, si los requisitos cambian durante el proyecto ( que es lo más probable ) es tan sencillo como modificar los test y así el código que estaba y el nuevo que está por venir siempre esté actualizado con los requisitos actuales.


# Despliegue

El Pass elegido es Heroku ya que es facil de usar y la base de datos PostgreSQL es gratuita.
En primer lugar instalamos [**Heroku CLI**](https://devcenter.heroku.com/articles/getting-started-with-python#set-up) con el siguiente comando:

```bash
$ wget -O- https://toolbelt.heroku.com/install-ubuntu.sh | sh
```

Luego me doy de alta en la aplicación [**Heroku**](https://signup.heroku.com/?c=70130000001x9jEAAQ). Una vez reguistrado creamos nuestra app la mia se llama nbaivbot 

![imagen](https://github.com/alvarocarmona6/ProyectoIV/blob/master/capturas/capturanbaivbot.png)

Enlazo mi repositorio GitHub con Heroku, y lo configuro para que cuando haga un push en GitHub y haya pasado los test de TravisCI se despliegue automaticamente.

![imagen](https://github.com/alvarocarmona6/ProyectoIV/blob/master/capturas/configuracionheroku.png)

Para la base de datos he instalado  el addon de PostgreSQL que es gratuito.

![imagen](https://github.com/alvarocarmona6/ProyectoIV/blob/master/capturas/basededatosheroku.png)

A continuacion creo en el respositorio el archivo Procfile que contendrá información de lo que tiene que hacer Heroku para el despliegue,
mi archivo Procfile es el [siguiente](https://github.com/alvarocarmona6/ProyectoIV/blob/master/Procfile).

Despliegue https://nbaivbot.herokuapp.com/

Mi bot ya tiene algunas funcionalidades hecha como mostrar la clasificación actualizada de la NBA o decir el mejor jugador. Se puede comprobar en telegram buscando @NBA_IV_Bot 


## Despliegue en Docker

Lo primero que tenemos que hacer es registrarnos en la página de [Docker](https://www.docker.com/) e irnos al apartado de Create automated build, autorizando a Docker a que este conectado con nuestra cuenta.
![imagen](https://github.com/alvarocarmona6/ProyectoIV/blob/master/capturas/capturadocker2.png)

Ahora creamos el fichero Dockerfile para que así Docker pueda crear el contenedor

		FROM ubuntu:16.04
                MAINTAINER Alvaro Carmona Oliva

                #Añadimos las variables de entorno
                ARG token_bot

                ARG database

                ENV TOKEN=$token_bot

                ENV DATABASE_URL=$database

                RUN apt-get update
                RUN apt-get install -y python-setuptools
                RUN apt-get install -y python-dev
                RUN apt-get install -y build-essential
                RUN apt-get install -y libpq-dev
                RUN apt-get install -y python-pip
                RUN pip install --upgrade
                RUN apt-get install net-tools

                RUN apt-get install -y git
                RUN git clone https://github.com/alvarocarmona6/ProyectoIV.git


                RUN pip install -r ProyectoIV/requirements.txt

                EXPOSE 80
                WORKDIR ProyectoIV/
                CMD ./prueba.sh


Ahora al hacer pull Docker hará un build automático

![imagen](https://github.com/alvarocarmona6/ProyectoIV/blob/master/capturas/capturadocker1.png)

Una vez terminado se puede hacer pull del repositorio con docker alvaroc96/proyectoiv y ejecutarlo con sudo docker run -e "TOKEN=a" -e "DATABASE_URL=b" -i -t alvaroc96/proyectoiv


![imagen](https://github.com/alvarocarmona6/ProyectoIV/blob/master/capturas/capturadocker3.png)

Enlace del repositorio en Docker Hub: https://hub.docker.com/r/alvaroc96/proyectoiv/

Para el despliegue en Zeit tenemos que instalar now con npm install -g now , posteriormente ejecuntando en el directorio donde esta el fichero Dockerfile  now -e "TOKEN=a" -e "DATABASE_URL=b" se desplegará automáticamente.
Contenedor: https://proyectoiv-yrjpfrexfv.now.sh/


## Despliegue en AWS con Vagrant 
Una vez que estemos registrado en la pagina de [amazon](https://aws.amazon.com/es/) y tengamos instalado virtual box y vagrant con sus correspondientes plugin para aws.
Cuando tengamos todo esto instalado ejecutamos vagrant init en nuestro repositorio para que se cree el archivo [VagrantFile](https://github.com/alvarocarmona6/ProyectoIV/blob/master/Vagrantfile) el cual he tenido que modificar.


## Ansible
Al final del archivo [VagrantFile](https://github.com/alvarocarmona6/ProyectoIV/blob/master/Vagrantfile) incluimos un archivo [Ansible](https://github.com/alvarocarmona6/ProyectoIV/blob/master/ansible.yml) que se va a encargar de aprovisionar nuestro Iass . 
Una vez que esto se ejecute podremos acceder mediante ssh con el comando ssh -i clave.pem ubuntu@DNS.

## Fabric
Vamos a utilizar fabric para agilizar todo el proceso.Para eso tenemos nuestro fichero [fabric](https://github.com/alvarocarmona6/ProyectoIV/blob/master/fabfile.py). Para usarlo se ejecuta el siguiente comando fab  -i KEY.pem -H ubuntu@DNS funcion.
Despliegue final : 13.58.173.122
