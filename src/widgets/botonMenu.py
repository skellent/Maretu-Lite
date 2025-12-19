import flet as ft

class BotonMenu(ft.Container):
    def __init__(self, texto, icono, color = ft.Colors.DEEP_PURPLE, on_click = None):
        super().__init__()
        self.expand = True 
        self.bgcolor = color
        self.border_radius = 50
        self.ink = True
        self.on_click = on_click
        self.content = ft.Column(
            [
                ft.Icon(
                    name = icono,
                    size = 75,
                    color = ft.Colors.WHITE
                ),
                ft.Text(
                    value = texto,
                    color = ft.Colors.WHITE,
                    weight = ft.FontWeight.BOLD,
                    text_align = ft.TextAlign.CENTER
                ),
            ],
            alignment = ft.MainAxisAlignment.CENTER,
            horizontal_alignment = ft.CrossAxisAlignment.CENTER,
        )