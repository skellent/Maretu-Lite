import flet as ft
from typing import Any

class DialogoAbout(ft.AlertDialog):
    def __init__(self, page: ft.Page) -> Any:
        self.page = page
        super().__init__(
            modal = True,
            title = ft.Text("Skell's Maretu Lite"),
            content = ft.Text("Aplicación de punto de venta local para Android y Windows."),
            actions = [
                ft.TextButton(
                    "Aceptar",
                    on_click = self.page.close(self)
                )
            ],
            actions_alignment = ft.MainAxisAlignment.END,
        )