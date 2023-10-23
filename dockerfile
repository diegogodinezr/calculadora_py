# Utiliza la imagen base de apache
# en la version 2.4.12
FROM httpd:2.4.12

#Copia los archivo del proyecot a la carpeta htdocs
COPY . /usr/local/apache2/htdocs/

# Expone el puerto 80
EXPOSE 80

# Inicia el servicio httpd con argumentos -D FOREGROUND
CMD [ "httpd", "-D", "FOREGROUND" ]