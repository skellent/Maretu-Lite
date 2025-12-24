import flet as ft
from typing               import Any
from widgets.dialogoAbout import DialogoAbout
from widgets.appBar       import AppBarSecundaria
from modules              import configurarRuta
from modules.maretuSQL    import MaretuSQL

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
    )
