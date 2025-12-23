import flet as ft
from widgets.dialogoAbout import DialogoAbout


class PopUpAbout(ft.PopupMenuButton):
    def __init__(self, page: ft.Page):
        self.page = page
        super().__init__(
            items=[
                ft.PopupMenuItem(
                    text="Acerca de",
                    icon=ft.Icons.INFO,
                    on_click=lambda e: DialogoAbout(self.page).show(),
                )
            ],
            icon_color="onprimary",
        )