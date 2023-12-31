import sqlalchemy as sa
from decouple import config

def carga_data():
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

        # Cargo data
        with engine.connect() as connection:
            script_path = '/home/agustin/Documentos/postgres-python/sql_script/load_data.sql'
            with open(script_path, 'r') as script_file:
                script = script_file.read()
                connection.execute(sa.text(script))
                connection.commit()

        print("Data cargada correctamente")

    except sa.exc.SQLAlchemyError as e:
        # Errores específicos de SQLAlchemy
        print(f"Error al cargar data: {e}")
    except Exception as e:
        # Excepciones generales
        print(f"Error inesperado: {e}")

if __name__ == "__main__":
    archivo_sql = '/home/agustin/Documentos/postgres-python/sql_script/load_data.sql'
    carga_data()