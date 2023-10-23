# Calculadora con python

## Descripción de ejecucion de calculadora
Calculadora básica con python en el archivo calc.py
## Requisitos
## Intrucciones de instalacion y configuracion
## Intrucciones de ejecucion


## Descripción de ejecucion de dockers
Comando para construir la imegen desde dockerfile

```sh
docker build -t demo-httpd:l14 .
```

Ejecutar la imagen construida

```sh
docker run -p 3000:80 demo-httpd:l14
```

#utilizar el docker compose

para utilizar docker-compose se utiliza un archivo denominado 
`docker-compose.yml` .

para dar de alta los servicios definicods en el docker-compose se debe ejecutar el siguiente comando

```sh
docker-compose up -d
```

para detener los servicios se debe ejecutar lo siguiente:

```sh
docker-compose stop
```

para volver a iniciar los servicios se debe ejecutar lo siguiente: 
```sh
docker-compose start
```

para desinstalar los servicios del contenedor se debe ejecutar lo siguiente:
```sh
docker-compose down
```

si se necesita recontruir la imegen de los servicios con docker-compose, se utiliza el siguiente
comando:
```sh
docker-compose up -d --build
```

para consultar el estado de los contenedores
```sh
docker ps
```