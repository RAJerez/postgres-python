import sqlalchemy as sa
from decouple import config

def prueba_conn():
    # Se traen las variables de entorno desde el archivo ".env"
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

if __name__ == "__main__":
    prueba_conn()