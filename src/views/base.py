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
        try:
            return ft.View(
                instancia.ruta,
                instancia.controles
            )
        except Exception as e:
            return ft.View(
                "/reportes",
                controls = [
                    ft.AppBar(title = ft.Text("Error de sistema"), bgcolor = ft.Colors.RED_700),
                    ft.Container(
                        padding = 20,
                        content = ft.Column(
                            controls = [
                                ft.Icon(ft.Icons.ERROR_OUTLINE, color = "red", size = 50),
                                ft.Text("Error Crítico", size = 25, weight = "bold", color = "red"),
                                ft.Text(f"Detalle: {str(e)}", size = 16, selectable = True, italic = True),
                                ft.Divider(),
                                ft.ElevatedButton("Volver al Inicio", on_click = lambda _: instancia.pagina.go("/"))
                            ], 
                            spacing = 10
                        )
                    )
                ]
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