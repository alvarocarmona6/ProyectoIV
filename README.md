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



Enlace del repositorio en Docker Hub: https://hub.docker.com/r/alvaroc96/proyectoiv/

Para el despliegue en Zeit tenemos que instalar now con npm install -g now , posteriormente ejecuntando en el directorio donde esta el fichero Dockerfile  now -e "TOKEN=a" -e "DATABASE_URL=b" se desplegará automáticamente.
Contenedor: https://proyectoiv-yrjpfrexfv.now.sh/


## Despliegue en Azure

Lo primero de todo es instalar Vagrant que  nos va permitir crear nuestra máquina virtual , yo ya lo tenia instalado de la asignatura DAI.
Aun así con **sudo apt-get install vagrant** se instala sencillamente.
Una vez instalado vagrant tenemos que tener una cuenta en Azure (yo la tengo desde el principio de curso ya que nuestro profesor nos dio un cupón para canjear ). Seguidamente nos intalamos el plugin de azure en vagrant con **vagrant plugin install vagrant-azure**
![imagen](https://github.com/alvarocarmona6/ProyectoIV/blob/master/capturas/hito5-1.png)

Ahora con **sudo npm install -g azure-cli** nos instalamos el cliente de Azure en la terminal para asi poder hacer el correspondiente login y poder crear posteriormente la maquina virtual.
![imagen](https://github.com/alvarocarmona6/ProyectoIV/blob/master/capturas/hito5-2.png)

A partir de aqui ya podemos hacer login en la terminal con **azure login** entrando en la pagina que aparece en la captura e insertando el codigo que nos muestra.
![imagen](https://github.com/alvarocarmona6/ProyectoIV/blob/master/capturas/hito5-6.png)
[Aquí](https://docs.microsoft.com/es-es/azure/) se puede encontrar todo para tener Azure bien configurado.
Primero creo mi aplicación, en la pantalla de azure abajo a la izquierda en Más servicios->Registros de aplicaciones-> nuevo registro de aplicaciones.
![imagen](https://github.com/alvarocarmona6/ProyectoIV/blob/master/capturas/hito5-10.png)
Como se ve en la captura yo ya tengo creada mi aplicacion que se llama **NBAbot**, una vez se tiene la aplicación hay que crear una certificado digital que para eso se puede usar openssl que ya sé de la asginatura SPSI con el comando **openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout clave.key -out clavea.key** y con el comando **openssl x509 -inform pem -in clave.key -outform der -out clave.cer** lo paso a formato cer, una vez lo tengo lo subo a través de la plataforma de Azure dentro de nuestra aplicación en el apartado de claves.
![imagen](https://github.com/alvarocarmona6/ProyectoIV/blob/master/capturas/hito5-11.png) también genero una contraseña para la aplicación , cuando se guarda esta contraseña nos da una clave que deberemos guardar para después configurar el Vagrantfile.
Una vez tengo todo esto ya puedo configurar mi fichero VagrantFile que está configurado de la siguiente manera:





        Vagrant.configure('2') do |config|
          config.vm.box = 'azure'
          config.vm.box_url = 'https://github.com/msopentech/vagrant-azure/raw/master/dummy.box' #Caja base vacia
          # use local ssh key to connect to remote vagrant box
          config.ssh.private_key_path = '~/.ssh/id_rsa'
          config.vm.network "public_network" 
          config.vm.network "forwarded_port", guest: 80, host: 80

          config.vm.provider :azure do |azure, override|


            # configuration needed for Azure
            azure.vm_name = "maquinanbabot"
            azure.tenant_id = 'id del directorio'
            azure.client_id = 'id de la aplicacion'
            azure.client_secret = 'contraseña de la aplicacion'
            azure.subscription_id = 'id de la suscripciones'
            azure.vm_size = "Standard_DS2_v2"
          end

          # configuration of ansible
          config.vm.provision :ansible do |ansible|
                ansible.playbook = "playbook.yml"
          end

        end

En el Vagrantfile he utilizado ansible  (se instala con **sudo apt-get install ansible**) en el fichero [var](https://github.com/alvarocarmona6/ProyectoIV/blob/master/var.yml) declaro la variable system_packages que contendra tanto build-essential como git para que el fichero [playbook](https://github.com/alvarocarmona6/ProyectoIV/blob/master/playbook.yml) con el task instala dichos paquetes para así automatizar el proceso ,ya que cuando cree la máquina virtual se intalará también esos dos paquetes.

Antes de crear la maquina virtual tenemos que darle permiso a la aplicacion de colaborador de la siguiente manera:

![imagen](https://github.com/alvarocarmona6/ProyectoIV/blob/master/capturas/hito5-12.png)


Una vez hecho esto creamos la maquina virtual con **vagrant up --provider=azure**
![imagen](https://github.com/alvarocarmona6/ProyectoIV/blob/master/capturas/hito5-6.png)
