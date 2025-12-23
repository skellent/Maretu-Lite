import flet as ft
from widgets.dialogoAbout import DialogoAbout
from widgets.appBar       import AppBarSecundaria
from typing import Any

def inventario(page: ft.Page) -> Any:
    dialogoAbout: DialogoAbout = DialogoAbout(page)
    return ft.View(
        "/inventario",
        padding = 0,
        controls = [
            AppBarSecundaria(page, dialogoAbout, "Inventario"),
            ft.Tabs(
                selected_index = 0,
                animation_duration = 300,
                scrollable = False, 
                expand = True,
                indicator_color = ft.Colors.DEEP_PURPLE_ACCENT,
                tabs = [
                    ft.Tab(
                        text = "Listado",
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
                            content = ft.Text("Formulario de registro aquí"),
                            alignment = ft.alignment.center
                        ),
                    ),
                    ft.Tab(
                        text = "Stock",
                        icon = ft.Icons.NUMBERS,
                        content = ft.Container(
                            content = ft.Text("Formulario de Stock aquí"),
                            alignment = ft.alignment.center
                        ),
                    )
                ]
            )
        ]
    )
