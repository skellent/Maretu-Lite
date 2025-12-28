# Importacion de Flet
import flet as ft
# Importacion de Clase Base
from views.base import VistaBase
# Importacion de Widgets
from widgets.dialogoAbout import DialogoAbout
from widgets.botonMenu    import BotonMenu
from widgets.appBar       import AppBarPrincipal

class MenuPrincipal(VistaBase):
    def __init__(instancia, pagina: ft.Page) -> None:
        """Método constructor"""
        instancia.pagina = pagina
        dialogo: DialogoAbout = DialogoAbout(instancia.pagina)
        super().__init__(
            pagina,
            "/",
            [
                AppBarPrincipal(instancia.pagina, dialogo),
                ft.Column(
                    expand = True,
                    spacing = 15,
                    controls = [
                        # Fila 1 (2 botones)
                        ft.Row(
                            expand = True,
                            spacing = 15,
                            controls = [
                                BotonMenu("Ventas", ft.Icons.ADD_SHOPPING_CART, on_click = lambda e: instancia.pagina.go("/ventas")),
                                BotonMenu("Reportes", ft.Icons.ATTACH_MONEY, on_click = lambda e: instancia.pagina.go("/reportes")),
                            ]
                        ),
                        # Fila 2 (2 botones)
                        ft.Row(
                            expand = True,
                            spacing = 15,
                            controls = [
                                BotonMenu("Inventario", ft.Icons.ALL_INBOX, on_click = lambda e: instancia.pagina.go("/inventario")),
                                BotonMenu("Clientes", ft.Icons.GROUP, on_click = lambda e: instancia.pagina.go("/clientes")),
                            ]
                        ),
                        # Fila 3 (1 botón ancho total)
                        ft.Row(
                            expand = True,
                            controls = [
                                BotonMenu("Configuración", ft.Icons.SETTINGS, on_click = lambda e: instancia.pagina.go("/configuracion")),
                            ]
                        ),
                    ]
                )
            ]
        )
        return None

"""
class MenuPrincipal(VistaBase):
    def __init__(instancia, pagina: ft.Page) -> None:
        ""Método constructor""
        instancia.pagina = pagina
        instancia.ruta = "/"
        dialogo: DialogoAbout = DialogoAbout(instancia.pagina)
        instancia.controles = [
            AppBarPrincipal(instancia.pagina, dialogo),
            ft.Column(
                expand = True,
                spacing = 15,
                controls = [
                    # Fila 1 (2 botones)
                    ft.Row(
                        expand = True,
                        spacing = 15,
                        controls = [
                            BotonMenu("Ventas", ft.Icons.ADD_SHOPPING_CART, on_click = lambda e: instancia.pagina.go("/ventas")),
                            BotonMenu("Reportes", ft.Icons.ATTACH_MONEY, on_click = lambda e: instancia.pagina.go("/reportes")),
                        ]
                    ),
                    # Fila 2 (2 botones)
                    ft.Row(
                        expand = True,
                        spacing = 15,
                        controls = [
                            BotonMenu("Inventario", ft.Icons.ALL_INBOX, on_click = lambda e: instancia.pagina.go("/inventario")),
                            BotonMenu("Clientes", ft.Icons.GROUP, on_click = lambda e: instancia.pagina.go("/clientes")),
                        ]
                    ),
                    # Fila 3 (1 botón ancho total)
                    ft.Row(
                        expand = True,
                        controls = [
                            BotonMenu("Configuración", ft.Icons.SETTINGS, on_click = lambda e: instancia.pagina.go("/configuracion")),
                        ]
                    ),
                ]
            )
        ]
        return None
"""