# Importacion de Flet
import flet as ft
# Importacion de Vistas
from views.base import VistaSecundaria

class Inventario(VistaSecundaria):
    def __init__(instancia, pagina: ft.Page) -> None:
        """Método de construcción"""
        instancia.controles: list[ft.Container] = [
            ft.Tabs(
                selected_index = 0,
                animation_duration = 300,
                scrollable = False, 
                expand = True,
                tabs = [
                    ft.Tab(
                        text = "Productos",
                        icon = ft.Icons.ALL_INBOX,
                        content = ft.Container(
                            content = None,
                            padding = 20
                        ),
                    ),
                    ft.Tab(
                        text = "Agregar",
                        icon = ft.Icons.ADD_BOX,
                        content = ft.Container(
                            content = None,
                            alignment = ft.alignment.center
                        ),
                    ),
                    ft.Tab(
                        text = "Stock",
                        icon = ft.Icons.NUMBERS,
                        content = ft.Container(
                            content = None,
                            alignment = ft.alignment.center
                        ),
                    )
                ]
            )
        ]
        super().__init__(
            pagina,
            "Inventario",
            instancia.controles,
            "/inventario"
        )
        return None