CREATE DATABASE IF NOT EXISTS pixelplanet;
USE pixelplanet;

CREATE TABLE socios (
    ClienteID INT AUTO_INCREMENT PRIMARY KEY,
    NombreSocio VARCHAR(50) NOT NULL,
    Apellidos VARCHAR(50),
    FechaNacim DATE,
    Email VARCHAR(100) NOT NULL UNIQUE,
    Telefono VARCHAR(20) NOT NULL UNIQUE,
    Puntos INT DEFAULT 0
);

CREATE TABLE empleados (
    EmpleadoID INT AUTO_INCREMENT PRIMARY KEY,
    Email VARCHAR(100) NOT NULL UNIQUE,
    Contrasenia VARCHAR(100) NOT NULL,
    Rol VARCHAR(30) NOT NULL -- 'mostrador' o 'zona_juegos'
);

CREATE TABLE emp_mostrador (
    EmpleadoMostrID INT PRIMARY KEY,
    NumVentas INT DEFAULT 0,
    FOREIGN KEY (EmpleadoMostrID) REFERENCES empleados(EmpleadoID)
);

CREATE TABLE emp_zona_juegos (
    EmpleadoZDJID INT PRIMARY KEY,
    NumTorneos INT DEFAULT 0,
    NumSpeedruns INT DEFAULT 0,
    FOREIGN KEY (EmpleadoZDJID) REFERENCES empleados(EmpleadoID)
);

CREATE TABLE productos (
    ProductoID INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(100) NOT NULL,
    Descripcion TEXT,
    Precio DECIMAL(10,2) NOT NULL,
    Cantidad INT NOT NULL
);

CREATE TABLE genero_prod (
    ProductoID INT,
    Genero VARCHAR(50),
    PRIMARY KEY (ProductoID, Genero),
    FOREIGN KEY (ProductoID) REFERENCES productos(ProductoID)
);

CREATE TABLE zonajuego (
    ZonaID INT AUTO_INCREMENT PRIMARY KEY,
    Capacidad INT NOT NULL
);

CREATE TABLE asignzona (
    ZonaID INT,
    ClienteID INT,
    Horario VARCHAR(20),
    TraeJuego BOOLEAN,
    PRIMARY KEY (ZonaID, ClienteID, Horario),
    FOREIGN KEY (ZonaID) REFERENCES zonajuego(ZonaID),
    FOREIGN KEY (ClienteID) REFERENCES socios(ClienteID)
);

CREATE TABLE venta (
    EmpleadoMostrID INT,
    ProductoID INT,
    Fecha DATE NOT NULL,
    FOREIGN KEY (EmpleadoMostrID) REFERENCES emp_mostrador(EmpleadoMostrID),
    FOREIGN KEY (ProductoID) REFERENCES productos(ProductoID)
);

CREATE TABLE resenas (
    ResenaID INT AUTO_INCREMENT PRIMARY KEY,
    Estrellas INT NOT NULL,
    Comentario TEXT,
    Fecha DATE,
    CodProducto INT NOT NULL,
    CodEmpleado INT NOT NULL,
    FOREIGN KEY (CodProducto) REFERENCES productos(ProductoID),
    FOREIGN KEY (CodEmpleado) REFERENCES empleados(EmpleadoID)
);

CREATE TABLE torneos (
    TorneoID INT AUTO_INCREMENT PRIMARY KEY,
    NombreTorneo VARCHAR(100) NOT NULL,
    Juego VARCHAR(100),
    Fecha DATE,
    CodEmpleado INT NOT NULL,
    FOREIGN KEY (CodEmpleado) REFERENCES empleados(EmpleadoID)
);

CREATE TABLE participantes (
    TorneoID INT,
    ClienteID INT,
    PRIMARY KEY (TorneoID, ClienteID),
    FOREIGN KEY (TorneoID) REFERENCES torneos(TorneoID),
    FOREIGN KEY (ClienteID) REFERENCES socios(ClienteID)
);

CREATE TABLE speedruns (
    SpeedrunID INT AUTO_INCREMENT PRIMARY KEY,
    Juego VARCHAR(100),
    EmailSocio VARCHAR(100),
    Tiempo TIME,
    CodEmpleado INT NOT NULL,
    FOREIGN KEY (CodEmpleado) REFERENCES empleados(EmpleadoID)
);

INSERT INTO empleados (Email, Contrasenia, Rol) VALUES 
('empleado1@tienda.com', 'password123', 'mostrador'),
('juegos1@tienda.com', 'gamezone456', 'zona_juegos');

-- Insertar detalles específicos para el empleado de mostrador
INSERT INTO emp_mostrador (EmpleadoMostrID, NumVentas) VALUES 
(1, 0); 

INSERT INTO emp_zona_juegos (EmpleadoZDJID, NumTorneos, NumSpeedruns) VALUES 
(2, 0, 0); 

INSERT INTO socios (NombreSocio, Apellidos,FechaNacim, Email, Telefono) VALUES 
('Pepe', 'Miguel', '1990-05-15', 'pepe@gmail.com', '123456789'),
('Maria', 'Rodriguez', '2001-04-21', 'maria@gmail.com', '679453762');

INSERT INTO zonajuego (Capacidad) VALUES 
(2),(4),(4),(3),(5),(3);

ALTER TABLE productos ADD COLUMN Cantidad INT NOT NULL;