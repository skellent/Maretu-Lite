# Importacion de Flet
import flet as ft
# Importacion de Vistas
from views.base import VistaSecundaria

class Clientes(VistaSecundaria):
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
                        text = "Listado",
                        icon = ft.Icons.LIST,
                        content = ft.Container(
                            content = None,
                            padding = 20,
                            expand = True
                        ),
                    ),
                    ft.Tab(
                        text = "Registrar",
                        icon = ft.Icons.PERSON_ADD,
                        content = ft.Container(
                            padding = 20,
                            content = ft.Column(
                                controls = None
                            )
                        ),
                    ),
                    ft.Tab(
                        text = "Editar",
                        icon = ft.Icons.EDIT,
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
            "Clientes",
            instancia.controles,
            "/clientes"
        )
        return None