## File Upload

Caracteristicas:

- Docker
- Docker Compose
- Docker Machine
- Python 3.5

### OS X Instrucciones

1. Ejecutar nueva maquina - `docker-machine create -d virtualbox dev`
1. Construir imagenes - `docker-compose build`
1. Iniciar servicios - `docker-compose up -d`
1. Crear migraciones - `docker-compose run web /usr/local/bin/python manage.py migrate`
1. Crear migraciones - `docker-compose run web /usr/local/bin/python manage.py createsuperuser --username=username --email=username@example.com`
1. Obtener ip - `docker-machine ip dev`

### Notas:

Crear un archivo .env para guardar variable de entorno con las siguientes claves:

1. SECRET_KEY=**
1. DB_NAME=**
1. DB_USER=**
1. DB_PASS=**
1. DB_SERVICE=postgres
1. DB_PORT=5432