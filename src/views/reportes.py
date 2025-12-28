# Importacion de Flet
import flet as ft
# Importacion de Vistas
from views.base import VistaSecundaria

class Reportes(VistaSecundaria):
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
                        text = "Gráficas",
                        icon = ft.Icons.BAR_CHART,
                        content = ft.Container(
                            content = None,
                            padding = 20,
                            expand = True
                        ),
                    ),
                    ft.Tab(
                        text = "Estadísticas",
                        icon = ft.Icons.QUERY_STATS,
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
            "Reportes",
            instancia.controles,
            "/reportes"
        )
        return None