import flet as ft
from widgets.dialogoAbout import DialogoAbout
from widgets.appBar       import AppBarSecundaria
from typing import Any

def ventas(page: ft.Page) -> Any:
    dialogoAbout: DialogoAbout = DialogoAbout(page)
    return ft.View(
        "/ventas",
        controls = [
            AppBarSecundaria(page, dialogoAbout, "Ventas")
        ]
    )