import flet as ft

class BotonPantallaCompleta(ft.IconButton):
    def cambiarPantallaCompleta(self, e):
        self.page.window.full_screen = not self.page.window.full_screen
        self.page.update()
    def __init__(self, page: ft.Page):
        self.page = page
        super().__init__(
            icon=ft.Icons.FULLSCREEN,
            icon_color="onprimary",
            on_click=self.cambiarPantallaCompleta,
        )