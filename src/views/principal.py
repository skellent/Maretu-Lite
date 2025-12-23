import flet as ft
from widgets.dialogoAbout import DialogoAbout
from widgets.botonMenu    import BotonMenu
from widgets.appBar       import AppBarPrincipal
from typing import Any

def principal(page: ft.Page) -> Any:
    dialogoAbout: DialogoAbout = DialogoAbout(page)
    return ft.View(
        "/",
        controls = [
            AppBarPrincipal(page, dialogoAbout),
            ft.Column(
                expand = True,
                spacing = 15,
                controls = [
                    # Fila 1 (2 botones)
                    ft.Row(
                        expand = True,
                        spacing = 15,
                        controls = [
                            BotonMenu("Ventas", ft.Icons.ADD_SHOPPING_CART, on_click = lambda e: page.go("/ventas")),
                            BotonMenu("Reportes", ft.Icons.ATTACH_MONEY, on_click = lambda e: page.go("/reportes")),
                        ]
                    ),
                    # Fila 2 (2 botones)
                    ft.Row(
                        expand = True,
                        spacing = 15,
                        controls = [
                            BotonMenu("Inventario", ft.Icons.ALL_INBOX, on_click = lambda e: page.go("/inventario")),
                            BotonMenu("Clientes", ft.Icons.GROUP, on_click = lambda e: page.go("/clientes")),
                        ]
                    ),
                    # Fila 3 (1 botón ancho total)
                    ft.Row(
                        expand = True,
                        controls = [
                            BotonMenu("Configuración", ft.Icons.SETTINGS, on_click = lambda e: page.go("/configuracion")),
                        ]
                    ),
                ]
            )
        ]
    )