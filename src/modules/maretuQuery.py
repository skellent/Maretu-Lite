# CONSTANTES CON LAS QUERYS PREDEFINIDAS EN "querys"

class Tablas:
    CLIENTES: str = """CREATE TABLE IF NOT EXISTS clientes(id INTEGER PRIMARY KEY AUTOINCREMENT, cedula INTEGER NOT NULL UNIQUE, nombre TEXT NOT NULL, telefono TEXT);"""
    PRODUCTOS: str = """CREATE TABLE IF NOT EXISTS productos(id INTEGER PRIMARY KEY AUTOINCREMENT, categoria TEXT NOT NULL, nombre TEXT NOT NULL UNIQUE, precio NUMERIC NOT NULL, proveedor TEXT);"""

class Insertar:
    CLIENTE: str = """INSERT INTO clientes(cedula, nombre, telefono) VALUES(<cedula>, "<nombre>", "<telefono>")"""
    PRODUCTO: str = """INSERT INTO productos(categoria, nombre, proveedor, precio) VALUES("<categoria>", "<nombre>", "<proveedor>", <precio>)"""