-- Tabla Gasto
COPY compra FROM '/home/agustin/Documentos/postgres-python/csv_data/Gasto.csv' WITH CSV HEADER DELIMITER ',';


-- Tabla Compra
COPY compra FROM '/home/agustin/Documentos/postgres-python/csv_data/Compra.csv' WITH CSV HEADER DELIMITER ',';


-- Tabla Venta
COPY compra FROM '/home/agustin/Documentos/postgres-python/csv_data/Venta.csv' WITH CSV HEADER DELIMITER ',';


-- Tabla sucursal
COPY compra FROM '/home/agustin/Documentos/postgres-python/csv_data/Sucursales_ANSI.csv' WITH CSV HEADER DELIMITER ';';
COPY compra FROM '/home/agustin/Documentos/postgres-python/csv_data/Sucursales_UTF8.csv' WITH CSV HEADER DELIMITER ';';


-- Tabla cliente
COPY compra FROM '/home/agustin/Documentos/postgres-python/csv_data/Clientes.csv' WITH CSV HEADER DELIMITER ';';


-- Tabla canal_venta
COPY compra FROM '/home/agustin/Documentos/postgres-python/csv_data/CanalDeVenta.csv' WITH CSV HEADER DELIMITER ',';


-- Tabla producto
COPY compra FROM '/home/agustin/Documentos/postgres-python/csv_data/Productos.csv' WITH CSV HEADER DELIMITER ',';


-- Tabla a tipo_gasto
COPY compra FROM '/home/agustin/Documentos/postgres-python/csv_data/TiposDeGasto.csv' WITH CSV HEADER DELIMITER ',';


-- Tabla proveedor
COPY compra FROM '/home/agustin/Documentos/postgres-python/csv_data/Proveedores.csv' WITH CSV HEADER DELIMITER ',';

-- Empleado
COPY compra FROM '/home/agustin/Documentos/postgres-python/csv_data/compra.csv' WITH CSV HEADER DELIMITER ',';
