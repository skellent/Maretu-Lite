import flet as ft
from widgets.botonMenu import BotonMenu
from typing import Any

def inventario(page: ft.Page) -> Any:
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

    return ft.View(
        "/inventario",
        controls = [
            ft.AppBar(
                leading = ft.IconButton(
                    icon = ft.Icons.ARROW_BACK_IOS_NEW, # Un ícono más moderno
                    icon_color = ft.Colors.WHITE,
                    on_click = lambda _: page.go("/") # Regresa a la raíz
                ),
                title = ft.Text(
                    "Inventario",
                    color = ft.Colors.WHITE
                ),
                center_title = True,
                bgcolor = ft.Colors.DEEP_PURPLE,
                actions = [ft.PopupMenuButton(
                            items = [
                                ft.PopupMenuItem(
                                    text = "Acerca de",
                                    on_click = lambda e: page.open(dialogoAbout)
                                )
                            ],
                            icon_color = ft.Colors.WHITE
                        )],
                automatically_imply_leading = True
            )
        ]
    )