Se debe tener preinstalados:
 
 - Python3
 - Docker
 - Docker Compose



1- Ir al directorio:

    cd /home/agustin/Documentos/postgres-python

2- Crear entorno virtual y activarlo:

    python3 -m virtualenv venv

    source venv/bin/activate

3- Instalar requeriments.txt

    pip3 install -r "requirements.txt"

4- Iniciar contenedor base de datos postgres:

    sudo docker compose up -d

5- Conectar base de datos con DBeaver: