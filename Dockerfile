# Usa la imagen base de Debian Slim
FROM python:3.10-slim

# Instala git
RUN apt-get update && apt-get install -y git
RUN apt-get install nano
RUN apt-get install wget
RUN apt-get install curl
#-tengo que poner y-
RUN apt-get install unzip
RUN curl -s https://ohmyposh.dev/install.sh | bash -s
RUN oh-my-posh font install
#-elige la fuente-
RUN echo 'export TERM=xterm-256color' >> ~/.bashrc
RUN mkdir ~/oh-my-posh
RUN wget https://raw.githubusercontent.com/JanDeDobbeleer/oh-my-posh/main/themes/emodipt-extend.omp.json
RUN mv emodipt-extend.omp.json ~/oh-my-posh
RUN echo 'eval "$(oh-my-posh init bash --config ~/oh-my-posh/emodipt-extend.omp.json)"' >> ~/.bashrc

# Establece el directorio de trabajo en /home/project
WORKDIR /home/project

# Copia el contenido de la raíz donde está el Dockerfile al directorio /home/project
COPY . /home/project

# Instala las dependencias especificadas en el archivo requirements.txt
RUN pip install --upgrade pip
RUN pip install --upgrade awscli pip
RUN pip install --no-cache-dir -r requirements.txt

# Define el comando por defecto cuando el contenedor se ejecuta
CMD ["bash"]
