CREATE TABLE IF NOT EXISTS productos(
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    categoria   TEXT NOT NULL,
    nombre      TEXT NOT NULL UNIQUE,
    precio      NUMERIC NOT NULL,
    proveedor   TEXT
);