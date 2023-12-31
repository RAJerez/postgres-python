import sqlalchemy as sa
from sqlalchemy import create_engine
from decouple import config
import pandas as pd

# Se traen las variables de entorno desde archivo ".env"
user = config('POSTGRES_USER')
password = config('POSTGRES_PASSWORD')
host = config('POSTGRES_HOST')
port = config('POSTGRES_PORT')
database = config('POSTGRES_DB')

connection_string = f'postgresql://{user}:{password}@{host}:{port}/{database}'

# Test estado de la conexión
try:
    engine = sa.create_engine(connection_string)
    
    with engine.connect() as connection:
        result = connection.execute(sa.text('SELECT 1'))
        print("Conexión exitosa.")
    
except Exception as error:
    print(f"Error al conectar: {error}")
    


#Load data into postgresql database
#df.to_sql("table_name", engine, schema="public", if_exists=['fail','replace','append'])