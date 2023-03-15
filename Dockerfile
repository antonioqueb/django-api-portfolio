# Utilizamos la imagen más reciente de Python 3.9 basada en Debian Buster (slim) como base
FROM python:3.9-slim-buster

# Establecemos la variable de entorno PYTHONUNBUFFERED para asegurar que la salida de Python se muestre de inmediato en la consola
ENV PYTHONUNBUFFERED 1

# Definimos el directorio de trabajo en la imagen de Docker
# Todas las instrucciones posteriores se ejecutarán en este directorio
WORKDIR /backend

# Actualizamos los paquetes del sistema operativo e instalamos las dependencias necesarias para las bibliotecas de Python
# Luego, limpiamos la caché de paquetes para reducir el tamaño de la imagen
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    gcc \
    musl-dev \
    postgresql-client \
    python3-dev \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --upgrade pip \
    && apt-get clean

# Copiamos el archivo de dependencias de Python (requirements.txt) al directorio de trabajo en la imagen de Docker
COPY requirements.txt /backend/

# Instalamos las dependencias de Python necesarias para nuestra aplicación usando el archivo requirements.txt
RUN pip install -r requirements.txt

EXPOSE 8000

# Copiamos el código fuente de nuestra aplicación al directorio de trabajo en la imagen de Docker
COPY . /backend
