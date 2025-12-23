import flet as ft
from widgets.dialogoAbout import DialogoAbout

class PopUpAbout(ft.PopupMenuButton):
    def __init__(self, page: ft.Page, dialogo: DialogoAbout):
        self.page = page
        self.dialogo = dialogo
        super().__init__(
            items = [
                ft.PopupMenuItem(
                    content = ft.Row(
                        controls = [
                            ft.Icon(ft.Icons.INFO, color = "primary"),
                            ft.Text("Acerca de", color = "primary")
                        ]
                    ), # ft.Icons.INFO
                    on_click = lambda e: self.page.open(self.dialogo),
                )
            ],
            icon_color="onprimary",
        )