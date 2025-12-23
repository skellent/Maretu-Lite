import flet as ft
from views.principal     import principal
from views.ventas        import ventas
from views.reportes      import reportes
from views.inventario    import inventario
from views.clientes      import clientes
from views.configuracion import configuracion
from typing              import Any

def main(page: ft.Page) -> Any:
    page.title = "Skell's Maretu Lite"
    page.fonts = {"Comfortaa": "fonts/comfortaa.ttf"}
    page.theme = ft.Theme(
        color_scheme_seed = page.client_storage.get("color") if page.client_storage.get("color") != None else ft.Colors.GREEN,
        font_family = "Comfortaa",
        use_material3 = True
    )

    def cambioDeRuta(route) -> None:
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

    def eliminarVista(view) -> None:
        if len(page.views) > 1:
            page.views.pop()
            top_view = page.views[-1]
            page.go(top_view.route)

    page.on_route_change = cambioDeRuta
    page.on_view_pop = eliminarVista
    
    page.go(page.route)
    page.update()

ft.app(
    target = main,
    assets_dir = "assets"
)