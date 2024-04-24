ARG PYTHON_VERSION=python:3.10.4-alpine
FROM ${PYTHON_VERSION} 

RUN apk add --no-cache build-base
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . .

EXPOSE 8080

# Ejecuta el comando por defecto para iniciar el servidor en prod
#CMD ["gunicorn", "--bind", "0.0.0.0:8000", "enid.wsgi:application"]
CMD ["sh", "-c", "watchmedo auto-restart --directory=./ --pattern=*.py --recursive -- gunicorn -b 0.0.0.0:8080 app.wsgi:application"]