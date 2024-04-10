# Usa la imagen base de Debian Slim
FROM python:3.10-slim

# Instala git
RUN apt-get update && apt-get install -y git

# Establece el directorio de trabajo en /home/project
WORKDIR /home/project

# Copia el contenido de la raíz donde está el Dockerfile al directorio /home/project
COPY . /home/project

# Instala las dependencias especificadas en el archivo requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Define el comando por defecto cuando el contenedor se ejecuta
CMD ["bash"]
