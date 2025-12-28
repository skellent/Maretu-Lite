# Importacion de Flet
import flet as ft
# Importacion de Vistas
from views.base import VistaSecundaria

class Error(VistaSecundaria):
    def __init__(instancia, pagina: ft.Page) -> None:
        """Método de construcción"""
        instancia.pagina = pagina
        instancia.controles: list[ft.Container] = [
            ft.Container(
                padding = 20,
                content = ft.Column(
                    controls = [
                        ft.Icon(ft.Icons.ERROR_OUTLINE, color = "red", size = 50),
                        ft.Text("Error Crítico", size = 25, weight = "bold", color = "red"),
                        ft.Text(f"Detalle: {str(instancia.pagina.client_storage.get("error"))}", size = 16, selectable = True, italic = True),
                        ft.Divider(),
                        ft.ElevatedButton("Volver al Inicio", on_click = lambda _: instancia.pagina.go("/"))
                    ], 
                    spacing = 10
                )
            )
        ]
        super().__init__(
            pagina,
            "ERROR",
            instancia.controles,
            "/error"
        )
        return None