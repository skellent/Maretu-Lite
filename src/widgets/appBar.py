import flet as ft
from typing import Any
from widgets.dialogoAbout import DialogoAbout
from widgets.popupAbout import PopUpAbout
from widgets.botonPantallaCompleta import BotonPantallaCompleta

class AppBarPrincipal(ft.AppBar):
    def __init__(self, page: ft.Page, dialogo: DialogoAbout) -> Any:
        self.page = page
        self.dialogo = dialogo
        super().__init__(
            center_title = True,
            bgcolor = "primary",
            color = "onprimary",
            title = ft.Text("Skell's Maretu Lite"),
            leading = ft.Container(
                padding = 8,
                content = ft.Image(
                    src = "img/icon-white.svg",
                    fit = ft.ImageFit.CONTAIN,
                    color = "onprimary"
                )
            ),
            actions =  [PopUpAbout(self.page, self.dialogo)] if page.platform == ft.PagePlatform.ANDROID else [BotonPantallaCompleta(self.page), PopUpAbout(self.page,  self.dialogo)]
        )

class AppBarSecundaria(ft.AppBar):
    def __init__(self, page: ft.Page, dialogo: DialogoAbout, titulo: str) -> Any:
        self.page = page
        self.dialogo = dialogo
        super().__init__(
            center_title = True,
            bgcolor = "primary",
            color = "onprimary",
            title = ft.Text(titulo),
            leading = ft.Row(
                alignment=ft.MainAxisAlignment.START, # Los pega al inicio (izquierda)
                spacing=10, # Controla los píxeles ex
                tight=True,
                controls = [
                    ft.IconButton(
                        icon = ft.Icons.ARROW_BACK_IOS_NEW,
                        icon_color = "onprimary",
                        on_click = lambda _: self.page.go("/")
                    ),
                    ft.Image(
                        src = "img/icon-white.svg",
                        fit = ft.ImageFit.CONTAIN,
                        color = "onprimary",
                        width = 40,
                        height = 40
                    )
                ]
            ),
            actions = [PopUpAbout(self.page, self.dialogo)]
        )