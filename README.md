1- Ir al directorio:

    $ cd /home/agustin/Documentos/postgres-python


2- iniciar contenedor base de datos postgres:

    $ docker run --name mi-postgres -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=postgres-python -p 5432:5432 -v /home/agustin/Documentos/postgres-python/postgres-python-db:/var/lib/postgresql/data -d postgres:14

3- lo que sigue: