vagrant up --provider=aws

fab -i clave.pem -H ubuntu@DNS install
fab -i clave.pem -H ubuntu@DNS services
