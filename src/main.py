import flet as ft
from widgets.botonMenu import BotonMenu

def main(page: ft.Page):
    page.title = "Skell's Maretu Lite"
    # page.window.full_screen = True
    page.fonts = {
        "Comfortaa": "../fonts/comfortaa.ttf"
    }
    page.theme = ft.Theme(
        font_family = "Comfortaa"
    )
    page.appbar = ft.AppBar(
        leading = ft.Container(
            content = ft.Image(
                src = "./icon-white.svg",
                fit = ft.ImageFit.CONTAIN,
            ),
            padding = 8
        ),
        title = ft.Text(
            "Skell's Maretu Lite",
            color = ft.Colors.WHITE
        ),
        center_title = True,
        bgcolor = ft.Colors.DEEP_PURPLE
    )

    layout = ft.Column(
        expand = True,
        spacing = 15,
        controls=[
            # Fila 1 (2 botones)
            ft.Row(
                expand = True,
                spacing = 15,
                controls = [
                    BotonMenu("Ventas", ft.Icons.ADD_SHOPPING_CART),
                    BotonMenu("Reportes", ft.Icons.ATTACH_MONEY),
                ]
            ),
            # Fila 2 (2 botones)
            ft.Row(
                expand = True,
                spacing = 15,
                controls = [
                    BotonMenu("Inventario", ft.Icons.ALL_INBOX),
                    BotonMenu("Clientes", ft.Icons.GROUP),
                ]
            ),
            # Fila 3 (1 botón ancho total)
            ft.Row(
                expand = True,
                controls = [
                    BotonMenu("Configuración", ft.Icons.SETTINGS),
                ]
            ),
        ]
    )

    page.add(layout)

    page.update()

ft.app(
    target = main,
    assets_dir = "assets"
)