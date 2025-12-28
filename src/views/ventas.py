# Importacion de Flet
import flet as ft
# Importacion de Vistas
from views.base import VistaSecundaria

class Ventas(VistaSecundaria):
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
                        text = "Vender",
                        icon = ft.Icons.ADD_SHOPPING_CART,
                        content = ft.Container(
                            content = None,
                            padding = 20,
                            expand = True
                        ),
                    ),
                    ft.Tab(
                        text = "Historial",
                        icon = ft.Icons.LIST,
                        content = ft.Container(
                            padding = 20,
                            content = ft.Column(
                                controls = None
                            )
                        ),
                    )
                ]
            )
        ]
        super().__init__(
            pagina,
            "Ventas",
            instancia.controles,
            "/ventas"
        )
        return None