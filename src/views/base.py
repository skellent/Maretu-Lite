# Importacion de Flet
import flet as ft
# Importacion de Tipo
from typing import Any
# Importacion de Widgets
from widgets.appBar       import AppBarSecundaria
from widgets.dialogoAbout import DialogoAbout

class VistaBase:
    def start(instancia) -> ft.View:
        """Método para retornar la vista deseada"""
        return ft.View(
            instancia.ruta,
            instancia.controles
        )

    def __init__(instancia, pagina: ft.Page, ruta:str, controles: list[Any] = [ft.Text("Vista Base")]) -> None:
        """Método constructor"""
        instancia.pagina: ft.Page       = pagina
        instancia.ruta: str             = ruta
        instancia.controles: list[None] = controles
        return None
    
class VistaSecundaria(VistaBase):
    def __init__(instancia, pagina: ft.Page, titulo: str, controles: list[Any] = [], ruta: str = "/plantilla"):
        """Método constructor"""
        instancia.pagina = pagina
        dialogo: DialogoAbout = DialogoAbout(instancia.pagina)
        controles.append(AppBarSecundaria(instancia.pagina, dialogo, titulo))
        
        super().__init__(
            pagina,
            None,
            controles
        )