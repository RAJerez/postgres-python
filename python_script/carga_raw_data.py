import pandas as pd
import sqlalchemy as sa
from decouple import config

def carga_data(archivo_csv, nombre_tabla):
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

        # Carga data usando pandas
        df = pd.read_csv(archivo_csv)
        df.to_sql(nombre_tabla, con=engine, index=False, if_exists='replace')

        print(f"Data cargada correctamente en la tabla {nombre_tabla}")

    except sa.exc.SQLAlchemyError as e:
        # Errores específicos de SQLAlchemy
        print(f"Error al cargar data: {e}")
    except Exception as e:
        # Excepciones generales
        print(f"Error inesperado: {e}")

if __name__ == "__main__":
    path = '/home/agustin/Documentos/postgres-python/csv_data/'

    # Diccionario data {'tabla':'nombre de archivo'}
    data = {'canal_venta':'CanalDeVenta.csv',
            'cliente':'Clientes.csv',
            'compra':'Compra.csv',
            'empleado':'Empleados.csv',
            'gasto':'Gasto.csv',
            'producto':'Productos.csv',
            'proveedor':'Proveedores.csv',
            'sucursal':'Sucursales.csv',
            'tipo_gasto':'TiposDeGasto.csv',
            'venta':'Venta.csv',
    }

    # Itero en el diccionario y hago la carga en cada tabla con el archivo correspondiente
    for tabla, archivo_csv in data.items():
        archivo_completo = path + archivo_csv
        carga_data(archivo_completo, tabla)