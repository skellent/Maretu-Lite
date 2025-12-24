import flet as ft
from views.principal     import principal
from views.ventas        import ventas
from views.reportes      import reportes
from views.inventario    import inventario
from views.clientes      import clientes
from views.configuracion import configuracion
from typing              import Any

def main(page: ft.Page) -> Any:
    def cambiarColor() -> ft.Colors:
        color: str|None = page.client_storage.get("color")
        if color == None:
            return ft.Colors.DEEP_PURPLE
        else:
            match color:
                case "purple":
                    return ft.Colors.DEEP_PURPLE
                case "green":
                    return ft.Colors.GREEN
                case "blue":
                    return ft.Colors.BLUE
                case "red":
                    return ft.Colors.RED
    def cambiarTema() -> ft.ThemeMode:
        tema: str|None = page.client_storage.get("tema")
        if tema == None:
            if page.platform_brightness == ft.Brightness.LIGHT:
                return ft.ThemeMode.LIGHT 
            else:
                return ft.ThemeMode.DARK
        else:
            match tema:
                case "claro":
                    return ft.ThemeMode.LIGHT
                case "oscuro":
                    return ft.ThemeMode.DARK
                case "sistema":
                    return page.platform_brightness

    page.title = "Skell's Maretu Lite"
    page.fonts = {"Comfortaa": "fonts/comfortaa.ttf"}
    page.theme_mode = cambiarTema()
    page.theme = ft.Theme(
        color_scheme_seed = cambiarColor(),
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