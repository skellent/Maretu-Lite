import flet as ft
from widgets.dialogoAbout import DialogoAbout
from widgets.appBar       import AppBarSecundaria
from typing import Any

def reportes(page: ft.Page) -> Any:
    dialogoAbout: DialogoAbout = DialogoAbout(page)
    return ft.View(
        "/reportes",
        controls = [
            AppBarSecundaria(page, dialogoAbout, "Reportes")
        ]
    )