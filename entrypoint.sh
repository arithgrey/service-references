#!/bin/sh
# Ejecuta las migraciones si es necesario
echo "Microservice references"
echo "Running makemigrations and migrate..."
echo "Running makemigrations and migrate..."
echo "Running makemigrations and migrate..."
echo "Running makemigrations and migrate..."

python manage.py makemigrations image business
python manage.py makemigrations
python manage.py migrate
# Inicia el servidor con watchmedo
echo "Starting the server with watchmedo..."

python load_data.py 

watchmedo auto-restart --directory=./ --pattern=*.py --recursive -- gunicorn -b 0.0.0.0:8080 app.wsgi:application
