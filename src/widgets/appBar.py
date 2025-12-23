import flet as ft
from typing import Any
from widgets.dialogoAbout import DialogoAbout
from widgets.popupAbout import PopUpAbout
from widgets.botonPantallaCompleta import BotonPantallaCompleta

class AppBarPrincipal(ft.AppBar):
    def __init__(self, page: ft.Page) -> Any:
        self.page = page
        super().__init__()
        self.center_title = True
        self.bgcolor = "primary"
        self.color = "onprimary"
        self.title = ft.Text("Skell's Maretu Lite")
        self.leading = ft.Container(
            padding = 8,
            content = ft.Image(
                src = "img/icon-white.svg",
                fit = ft.ImageFit.CONTAIN,
                color = "onprimary"
            )
        )
        self.actions =  [PopUpAbout(self.page)] if page.platform == ft.PagePlatform.ANDROID else [BotonPantallaCompleta(self.page), PopUpAbout(self.page)]