import os
import sqlite3 as SQL

class MaretuSQL():
    def __init__(instancia, ruta: str):
        instancia.Conexion = SQL.connect(
            ruta,
            check_same_thread=False
        )
        instancia.Cursor = instancia.Conexion.cursor()
    
    def Leer(instancia, ruta: str) -> str:
        root = os.path.dirname(
            os.path.dirname(
                os.path.abspath(__file__)
            )
        )
        ruta_absoluta = os.path.join(
            root,
            ruta
        )
        with open(ruta_absoluta, "r", encoding="utf-8") as f:
            return f.read()

    def RemplazarArgumentos(instancia, texto:str, diccionario: dict) -> str:
        nuevoTexto: str = texto
        for llave in diccionario:
            nuevoTexto = nuevoTexto.replace(llave, diccionario[llave])
        return nuevoTexto

if __name__ == "__main__":
    maretuSQL: MaretuSQL = MaretuSQL("../database/testing.db")
    consulta: str = maretuSQL.Leer("../querys/tablas/clientes.sql")
    print(consulta)
    maretuSQL.Cursor.execute(consulta)
