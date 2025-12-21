import os
import shutil
import flet as ft
import sqlite3
from views.principal     import principal
from views.ventas        import ventas
from views.reportes      import reportes
from views.inventario    import inventario
from views.clientes      import clientes
from views.configuracion import configuracion
from widgets.botonMenu   import BotonMenu
from typing              import Any

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

def inicializarBaseDeDatos(page: ft.Page):
    databaseNombre = "maretu.db"
    user_dir = os.environ.get("FLET_APP_STORAGE_DATA")

    if not user_dir:
        if os.name == 'nt': # Windows
            user_dir = os.path.join(os.environ['LOCALAPPDATA'], "MaretuLite")
        else: # Linux / macOS fallback
            user_dir = os.path.join(os.path.expanduser("~"), ".maretu_lite")
    
    destino_db = os.path.join(user_dir, databaseNombre)
    
    if not os.path.exists(user_dir):
        os.makedirs(user_dir, exist_ok = True)
    
    base_path = os.path.dirname(os.path.abspath(__file__))
    origen_db = os.path.join(base_path, "database", databaseNombre)
    
    if not os.path.exists(destino_db):
        try:
            if os.path.exists(origen_db):
                shutil.copy(origen_db, destino_db)
            else:
                conn = sqlite3.connect(destino_db)
                conn.close()
        except Exception as e:
            print(f"Error crítico al copiar BD: {e}")
            
    return destino_db

def main(page: ft.Page) -> Any:
    page.title = "Skell's Maretu Lite"
    page.fonts = {
        "Comfortaa": "fonts/comfortaa.ttf"
    }
    page.theme = ft.Theme(
        color_scheme_seed = ft.Colors.DEEP_PURPLE,
        font_family       = "Comfortaa"
    )

    try:
        ruta_db = inicializarBaseDeDatos(page)
        page.client_storage.set("db_path", ruta_db)
    except Exception as e:
        print(f"Error en el inicio: {e}")
        
    page.client_storage.set("root_path", ROOT_PATH)

    def cambioDeRuta(route):
        page.views.clear()
        if page.route == "/":
            page.views.append(principal(page))
        elif page.route == "/ventas":
            page.views.append(ventas(page))
        elif page.route == "/reportes":
            page.views.append(reportes(page))
        elif page.route == "/inventario":
            page.views.append(inventario(page))
        elif page.route == "/clientes":
            page.views.append(clientes(page))
        elif page.route == "/configuracion":
            page.views.append(configuracion(page))
        page.update()

    def eliminarVista(view):
        if len(page.views) > 1:
            page.views.pop()
            top_view = page.views[-1]
            page.go(top_view.route)

    page.on_route_change = cambioDeRuta
    page.on_view_pop     = eliminarVista
    
    page.go(page.route)
    page.update()

ft.app(
    target     = main,
    assets_dir = "assets"
)