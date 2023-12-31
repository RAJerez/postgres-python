import sqlalchemy as sa
from decouple import config

def create_tables():
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

        # Creo tablas
        with engine.connect() as connection:
            script_path = '/home/agustin/Documentos/postgres-python/sql_script/create_table.sql'
            with open(script_path, 'r') as script_file:
                script = script_file.read()
                connection.execute(sa.text(script))
                connection.commit()

        print("Tablas creadas exitosamente.")

    except sa.exc.SQLAlchemyError as e:
        # Errores específicos de SQLAlchemy
        print(f"Error al crear tablas: {e}")
    except Exception as e:
        # Excepciones generales
        print(f"Error inesperado: {e}")

if __name__ == "__main__":
    create_tables()