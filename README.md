# Calculadora con python

## Descripción de ejecucion de calculadora
Este proyecto es una calculadora básica en Python que permite realizar operaciones de suma, resta, multiplicación y división. La calculadora también proporciona un menú interactivo que permite al usuario seleccionar la operación deseada y luego ingresar los números para realizar la operación.
## Requisitos
Antes de ejecutar la calculadora, asegúrate de tener Python instalado en tu sistema.
## Intrucciones de instalacion y configuracion
1. Clona o descarga este repositorio en tu sistema.

2. Asegúrate de tener Python instalado. Puedes verificar si Python está instalado ejecutando el siguiente comando en la terminal:

   ```markdown
   python --version
    ```
Si Python no está instalado, descárgalo e instálalo desde python.org.
## Intrucciones de ejecucion
Para ejecutar la calculadora, sigue estos pasos:

1. Abre una terminal y navega hasta la carpeta donde se encuentra el archivo `calculadora.py`.

2. Ejecuta el archivo `calculadora.py` utilizando Python:

   ```bash
   python calculadora.py
    ```
La calculadora mostrará un menú interactivo que te permitirá seleccionar la operación que deseas realizar. Sigue las instrucciones en la terminal para ingresar los números necesarios y obtener el resultado de la operación.

Para salir de la calculadora, selecciona la opción "5" en el menú.

## Para crear el contenedor en dockers
Comando para construir la imegen desde dockerfile

```sh
docker build -t calculadora-app .
```

Ejecutar la imagen construida

```sh
docker run -p 3000:80 calculadora-app
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