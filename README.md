# Proyecto API Task CRUD de Challenge

## Descripción

Este proyecto es una aplicación de gestión de tareas que te permite organizar y realizar un seguimiento de tus tareas diarias de manera efectiva con autenticacion JWT.

## Estado del Proyecto

Finalizado.

## Instalación

1. Clona el repositorio desde GitHub.
2. En el caso de utilizar virtualenv y no tenerlo instalado, utilizar comando: `pip install virtualenv`.
3. Crea un entorno virtual con el comando: `py -m venv venv`
4. Activa el entorno virtual con el comando: `venv\Scripts\activate`
5. Instala las dependencias: `pip install -r requirements.txt`
6. En el caso de no tener al super usuario, crearlo con el comando: `python manage.py createsuperuser`.
7. En el caso de tener que aplicar migraciones, utilizar los siguientes comandos: `python manage.py makemigrations` y luego `python manage.py migrate`.

## Uso

1. Una vez instalado, puedes iniciar la aplicación con el siguiente comando: `python manage.py runserver`.
2. Acceder a la ruta: `http://127.0.0.1:8000/api/schema/swagger/` (Dependiendo del puerto que usen), para acceder a swagger con todos sus metodos.
3. Una vez dentro de swagger, primero obtenemos nuestro token de autenticacion en el metodo: `/api/token` sino no tendremos autorizacion para utilizar los metodos.
4. Una vez dentro del metodo `/api/token`, seleccionamos `Try it out` y dentro del Request body ingresamos nuestro usuario y contraseña.
5. Al ingresar correctamente nuestros datos y seleccionar execute, en el Response body, en `access`, nos dara nuestro token para autorizarnos en los candados y asi utilizar los metodos. Token de ejemplo: `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA0MjkzMTM1LCJpYXQiOjE3MDQyOTI4MzUsImp0aSI6IjY1OWRiMzAzNDdkYjQzZDI4NDYxZDliZTJhNTFkZTk3IiwidXNlcl9pZCI6MX0.ZnaVnOn6jOO0LE0u9goUAEE30tZc6LQ4I2YsBDis3g0`.

## Nota
Al darnos nuestro token, el mismo tiene un tiempo de vencimiento de 1 minuto por defecto, al autenticarnos, el mismo debe ser ingresado sin las comillas. Estos pasos son orientados desde swagger para poder utilizar los metodos.




