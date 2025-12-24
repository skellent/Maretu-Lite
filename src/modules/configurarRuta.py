import os
import flet as ft
from pathlib import Path
from typing  import Any

def rutaSegura(nombre_app = "maretu-lite"):
    ruta: Any = os.getenv("FLET_APP_STORAGE_DATA")
    if ruta:
        return ruta
    home: Path = Path.home()
    if os.name == "nt":
        fallback: Path = home / "AppData" / "Local" / nombre_app
    else:
        fallback: Path = home / ".local" / "share" / nombre_app
    fallback.mkdir(parents=True, exist_ok=True)
    
    return str(fallback)

if __name__ == "__main__":
    print("Ejecutando configurarRuta.py")