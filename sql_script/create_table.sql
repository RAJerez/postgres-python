ALTER USER postgres CREATEDB;  -- Otorga el privilegio de crear bases de datos
ALTER USER postgres SUPERUSER;  -- Otorga el privilegio de superusuario


-- Tabla gasto
CREATE TABLE IF NOT EXISTS gasto (
    IdGasto SERIAL PRIMARY KEY,
    IdSucursal INTEGER,
    IdTipoGasto INTEGER,
    Fecha DATE,
    Monto DECIMAL(10,2)
);

-- Tabla Compra
CREATE TABLE IF NOT EXISTS compra (
    IdCompra SERIAL PRIMARY KEY,
    Fecha DATE,
    IdProducto INTEGER,
    Cantidad INTEGER,
    Precio DECIMAL(10,2),
    IdProveedor INTEGER
);

-- Tabla Venta
CREATE TABLE IF NOT EXISTS venta (
    IdVenta SERIAL PRIMARY KEY,
    Fecha DATE NOT NULL,
    FechaEntrega DATE NOT NULL,
    IdCanal INTEGER,
    IdCliente INTEGER,
    IdSucursal INTEGER,
    IdEmpleado INTEGER,
    IdProducto INTEGER,
    Precio VARCHAR(30),
    Cantidad VARCHAR(30)
    -- Precio DECIMAL(10,2),
    -- Cantidad INTEGER
    -- Por el momento usamos varchar porque viene sucia la data (valores vacios)
    -- En el proceso de limpieza y procesamiento se corrige
);

-- Tabla Sucursal
CREATE TABLE IF NOT EXISTS sucursal (
    IdSucursal SERIAL PRIMARY KEY,
    Sucursal VARCHAR(40),
    Domicilio VARCHAR(150),
    Localidad VARCHAR(80),
    Provincia VARCHAR(50),
    Latitud VARCHAR(30),
    Longitud VARCHAR(30)
);

-- Tabla Cliente
CREATE TABLE IF NOT EXISTS cliente (
    IdCliente SERIAL PRIMARY KEY,
    Provincia VARCHAR(50),
    NombreApellido VARCHAR(80),
    Domicilio VARCHAR(150),
    Telefono VARCHAR(30),
    Edad VARCHAR(5),
    Localidad VARCHAR(80),
    X VARCHAR(30),
    Y VARCHAR(30),
    FechaAlta DATE NOT NULL,
    UsuarioAlta VARCHAR(20),
    FechaUltimaModificacion DATE NOT NULL,
    UsuarioUltimaModificacion VARCHAR(20),
    MarcaBaja BOOLEAN,
    col10 VARCHAR(1)
);

-- Tabla Canal_Venta
CREATE TABLE IF NOT EXISTS canal_venta (
    IdCanal SERIAL PRIMARY KEY,
    Canal VARCHAR(50)
);

-- Tabla Producto
CREATE TABLE IF NOT EXISTS producto (
    IdProducto SERIAL PRIMARY KEY,
    Concepto VARCHAR(100),
    Tipo VARCHAR(50),
    Precio VARCHAR(30)
);

-- Tabla Tipo_Gasto
CREATE TABLE IF NOT EXISTS tipo_gasto (
    IdTipoGasto SERIAL PRIMARY KEY,
    Descripcion VARCHAR(100) NOT NULL,
    MontoAproximado DECIMAL(10,2) NOT NULL
);

-- Tabla Proveedor
CREATE TABLE IF NOT EXISTS proveedor (
    IdProveedor SERIAL PRIMARY KEY,
    Nombre VARCHAR(80),
    Domicilio VARCHAR(150),
    Ciudad VARCHAR(80),
    Provincia VARCHAR(50),
    Pais VARCHAR(20),
    Departamento VARCHAR(80)
);

-- Tabla Empleado
CREATE TABLE IF NOT EXISTS empleado (
    IdEmpleado SERIAL PRIMARY KEY,
    Apellido VARCHAR(100),
    Nombre VARCHAR(100),
    Sucursal VARCHAR(50),
    Sector VARCHAR(50),
    Cargo VARCHAR(50),
    Salario VARCHAR(30)
);