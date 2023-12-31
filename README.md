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


6- Ejecutar el script connection.py. El mismo revisa que la conexión se realize.

    python3 connection.py


7- Ejecutar el script tables.py. El mismo creará las tablas.

    python3 tables.py