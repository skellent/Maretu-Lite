import os
import flet as ft
from modules.maretuSQL import MaretuSQL
from typing            import Any

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR     = os.path.dirname(CURRENT_DIR)

def inventario(page: ft.Page) -> Any:
    ruta_sql_tabla = os.path.join(SRC_DIR, "querys", "tablas", "productos.sql")
    ruta_sql_ver = os.path.join(SRC_DIR, "querys", "consultas", "verProductos.sql")
    ruta_db = "No definida aún"

    try:
        ruta_db = page.client_storage.get("db_path")
        if ruta_db is None:
            user_dir = os.environ.get("FLET_APP_STORAGE_DATA")
            if not user_dir:
                if os.name == 'nt':
                    user_dir = os.path.join(os.environ['LOCALAPPDATA'], "MaretuLite")
                else:
                    user_dir = os.path.join(os.path.expanduser("~"), ".maretu_lite")
            ruta_db = os.path.join(user_dir, "maretu.db")
        print(f"DEBUG: Intentando abrir el archivo en: {os.path.abspath(ruta_db)}")
        print(f"DEBUG: ¿El archivo existe físicamente?: {os.path.exists(ruta_db)}")
        maretuSQL: MaretuSQL = MaretuSQL(ruta_db)
        maretuSQL.Cursor.execute(maretuSQL.Leer("querys/tablas/productos.sql"))
        maretuSQL.Conexion.commit()
        maretuSQL.Cursor.execute(maretuSQL.Leer("querys/consultas/verProductos.sql"))
        listado = maretuSQL.Cursor.fetchall()
        print(listado)

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
            padding = 0,
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
                ),
                ft.Tabs(
                    selected_index = 0,
                    animation_duration = 300,
                    scrollable = False, 
                    expand = True,
                    indicator_color = ft.Colors.DEEP_PURPLE_ACCENT,
                    tabs = [
                        ft.Tab(
                            text = "Listado",
                            icon = ft.Icons.ALL_INBOX,
                            content = ft.Container(
                                content = ft.ListView(
                                    controls = [ft.Text(f"Producto: {producto}") for producto in listado],
                                    expand   = True
                                ),
                                padding = 20
                            ),
                        ),
                        ft.Tab(
                            text = "Agregar",
                            icon = ft.Icons.ADD_BOX,
                            content = ft.Container(
                                content = ft.Text("Formulario de registro aquí"),
                                alignment = ft.alignment.center
                            ),
                        ),
                        ft.Tab(
                            text = "Stock",
                            icon = ft.Icons.NUMBERS,
                            content = ft.Container(
                                content = ft.Text("Formulario de Stock aquí"),
                                alignment = ft.alignment.center
                            ),
                        )
                    ]
                )
            ]
        )
    
    except Exception as e:
        return ft.View(
            "/inventario",
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
                            ft.Text(f"Ruta DB detectada: {ruta_db}"),
                            ft.Text(f"Ruta SQL tabla: {ruta_sql_tabla}"),
                            ft.ElevatedButton("Volver al Inicio", on_click = lambda _: page.go("/"))
                        ], 
                        spacing = 10
                    )
                )
            ]
        )