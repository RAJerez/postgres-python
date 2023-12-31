#### Esta es una opción sin usar sqlalchemy. 

# En caso de no tener configuradas las variables de entorno, especificarlas.
# pip3 install psicopg2 python-dotenv python-decouple

import psycopg2
from decouple import config

try:
    connection=psycopg2.connect(
        host = config('POSTGRES_HOST'),
        user = config('POSTGRES_USER'),
        password = config('POSTGRES_PASSWORD'),
        database = config('POSTGRES_DB')
    )
    
    print("Conexión exitosa.")
    cursor=connection.cursor()
    cursor.execute("SELECT version()")
    row=cursor.fetchone()
    print(row)
    
except Exception as error:
    print(f"Error al conectar: {error}")