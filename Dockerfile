FROM ubuntu:16.04
MAINTAINER Alvaro Carmona Oliva

#Añadimos las variables de entorno
ARG token_bot

ARG database_db

ENV TOKEN=$token_bot

ENV DATABASE_URL=$database_db

RUN apt-get -y update

#Primero de todo instalamos git y clonamos el directorio
RUN apt-get install -y git
RUN git clone https://github.com/alvarocarmona6/ProyectoIV.git

RUN apt-get update
RUN apt-get install -y python-pip
RUN apt-get install -y git
RUN git clone https://github.com/josegob/IV-Proyecto.git
RUN pip install -r ProyectoIV/requirements.txt

CMD cd ProyectoIV/bot && python NBAbot.py
