import flet as ft
from typing               import Any
from widgets.dialogoAbout import DialogoAbout
from widgets.appBar       import AppBarSecundaria
from modules              import configurarRuta
from modules.maretuSQL    import MaretuSQL

def ventas(page: ft.Page) -> Any:
    dialogoAbout: DialogoAbout = DialogoAbout(page)
    try:
        maretuSQL: MaretuSQL = MaretuSQL(f"{configurarRuta.rutaSegura()}/maretu.db")
        dialogoAbout: DialogoAbout = DialogoAbout(page)
        return ft.View(
            "/ventas",
            padding  = 0, 
            controls = [
                AppBarSecundaria(page, dialogoAbout, "Ventas"),
                ft.Tabs(
                    selected_index = 0,
                    animation_duration = 300,
                    scrollable = False, 
                    expand = True,
                    tabs = [
                        ft.Tab(
                            text = "Vender",
                            icon = ft.Icons.ADD_SHOPPING_CART,
                            content = ft.Container(
                                content = None,
                                padding = 20,
                                expand = True
                            ),
                        ),
                        ft.Tab(
                            text = "Historial",
                            icon = ft.Icons.LIST,
                            content = ft.Container(
                                padding = 20,
                                content = ft.Column(
                                    controls = None
                                )
                            ),
                        )
                    ]
                )
            ]
        )
    except Exception as e:
        return ft.View(
            "/ventas",
            controls = [
                ft.AppBar(title = ft.Text("Error de sistema"), bgcolor = ft.Colors.RED_700),
                ft.Container(
                    padding = 20,
                    content = ft.Column(
                        controls = [
                            ft.Icon(ft.Icons.ERROR_OUTLINE, color = "red", size = 50),
                            ft.Text("Error Crítico", size = 25, weight = "bold", color = "red"),
                            ft.Text(f"Detalle: {str(e)}", size = 16, selectable = True, italic = True),
                            ft.Divider(),
                            ft.Text(f"Ruta DB detectada: {configurarRuta.rutaSegura}"),
                            ft.ElevatedButton("Volver al Inicio", on_click = lambda _: page.go("/"))
                        ], 
                        spacing = 10
                    )
                )
            ]
        )