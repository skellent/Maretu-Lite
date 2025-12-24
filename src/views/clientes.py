import flet as ft
from typing               import Any
from widgets.dialogoAbout import DialogoAbout
from widgets.appBar       import AppBarSecundaria
from modules              import configurarRuta
from modules.maretuSQL    import MaretuSQL

def clientes(page: ft.Page) -> Any:
    try:
        maretuSQL: MaretuSQL = MaretuSQL(f"{configurarRuta.rutaSegura()}/maretu.db")
        dialogoAbout: DialogoAbout = DialogoAbout(page)
        return ft.View(
            "/clientes",
            padding  = 0, 
            controls = [
                AppBarSecundaria(page, dialogoAbout, "Clientes"),
                ft.Tabs(
                    selected_index = 0,
                    animation_duration = 300,
                    scrollable = False, 
                    expand = True,
                    tabs = [
                        ft.Tab(
                            text = "Listado",
                            icon = ft.Icons.LIST,
                            content = ft.Container(
                                content = None,
                                padding = 20,
                                expand = True
                            ),
                        ),
                        ft.Tab(
                            text = "Registrar",
                            icon = ft.Icons.PERSON_ADD,
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
            "/clientes",
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