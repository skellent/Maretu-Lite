import flet as ft
from widgets.botonMenu import BotonMenu
from typing import Any

def principal(page: ft.Page) -> Any:
    dialogoAbout = ft.AlertDialog(
        modal = True,
        title = ft.Text(
            "Skell's Maretu Lite"
        ),
        content = ft.Text(
            """Maretu (Skell's Maretu "Lite") es una aplicación de punto de venta para dispositivos Android y próximamente ejecutable en Windows; funcionando completamente de manera local sin dependencias al internet."""
        ),
        actions = [
            ft.TextButton(
                "Aceptar",
                on_click = lambda e: page.close(dialogoAbout)
            )
        ],
        actions_alignment=ft.MainAxisAlignment.END
    )

    def botonPantallaCompleta() -> None|ft.IconButton:
        if page.platform == ft.PagePlatform.ANDROID or page.platform == ft.PagePlatform.ANDROID_TV:            
            return [ft.PopupMenuButton(
                items = [
                    ft.PopupMenuItem(
                        text = "Acerca de",
                        on_click = lambda e: page.open(dialogoAbout)
                    )
                ],
                icon_color = ft.Colors.WHITE
            )]
        else:
            return [
                ft.IconButton(
                    ft.Icons.FULLSCREEN,
                    icon_color = ft.Colors.WHITE,
                    on_click = cambiarPantallaCompleta
                ),
                ft.PopupMenuButton(
                    items=[
                        ft.PopupMenuItem(
                            text = "Acerca de",
                            on_click = lambda e: page.open(dialogoAbout)
                        )
                    ],
                    icon_color = ft.Colors.WHITE
                )
            ]

    def cambiarPantallaCompleta(e: ft.EventType) -> None:
        page.window.full_screen = not page.window.full_screen
        page.update()

    return ft.View(
        "/",
        controls = [
            ft.AppBar(
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
                bgcolor = ft.Colors.DEEP_PURPLE,
                actions = botonPantallaCompleta()
            ),
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