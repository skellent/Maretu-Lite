import os
import sqlite3 as SQL

class MaretuSQL():
    def __init__(instancia, ruta: str):
        instancia.Conexion = SQL.connect(
            ruta,
            check_same_thread=False
        )
        instancia.Cursor = instancia.Conexion.cursor()
    
    def RemplazarArgumentos(instancia, texto:str, diccionario: dict) -> str:
        nuevoTexto: str = texto
        for llave in diccionario:
            nuevoTexto = nuevoTexto.replace(llave, diccionario[llave])
        return nuevoTexto

if __name__ == "__main__":
    print("Ejecutando maretuSQL.py")
