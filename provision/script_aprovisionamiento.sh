#!/bin/bash
vagrant up --provider=azure

fab -f despliegue/fabfile.py -H vagrant@maquinanbabot.westus.cloudapp.azure.com InstalarAplicacion
fab -f despliegue/fabfile.py -H vagrant@maquinanbabot.westus.cloudapp.azure.com Iniciar
