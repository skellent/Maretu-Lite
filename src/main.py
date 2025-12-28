# Importacion de Flet
import flet as ft
# Importacion de Vistas
from views import principal
# Importacion de Modulos

# Clase Primaria
class Primaria:
    def eliminarVista(instancia, view: ft.View) -> None:
        """Método de eliminación de vistas"""
        if len(instancia.page.views) > 1:
            instancia.page.views.pop()
            instancia.page.go( instancia.page.views[-1] )

    def cambioRuta(instancia, route: ft.Page.route):
        """Método de cambio de ruta de la página"""
        instancia.pagina.views.clear()
        match instancia.pagina.route:
            case "/":
                instancia.pagina.views.append( principal.principal(instancia.pagina) )
        instancia.pagina.update()

    def cambiarTema(instancia) -> ft.ThemeMode:
        """Método de Personalización a la página"""
        match instancia.pagina.client_storage.get("tema"):
            case "claro":
                return ft.ThemeMode.LIGHT
            case "oscuro":
                return ft.ThemeMode.DARK
            case "sistema" | None:
                return ft.ThemeMode.SYSTEM

    def config(instancia) -> None:
        """Método de Personalización a la página"""
        instancia.pagina.title      = instancia.titulo
        instancia.pagina.theme      = instancia.paleta
        instancia.pagina.on_route_change = instancia.cambioRuta
        instancia.pagina.on_view_pop = instancia.eliminarVista
        instancia.pagina.go("/")
        # instancia.pagina.update() # Actualizar Cambios

    def start(instancia, page: ft.Page) -> None:
        """Método de Inicio de Ejecución"""
        instancia.pagina: ft.Page = page
        instancia.config()

    def __init__(instancia, titulo: str, tipografia: dict[str: str], paleta: ft.Theme) -> None:
        """Método Constructor"""
        instancia.titulo: str                = titulo
        instancia.tipografia: dict[str: str] = tipografia
        instancia.paleta: ft.Theme           = paleta

# Proceso Principal
if __name__ == "__main__":
    # Ajustes
    titulo: str                = "Skell's Maretu Lite"
    tipografia: dict[str: str] = { "Comfortaa": "fonts/Comfortaa.ttf" }
    paleta: ft.Theme           = ft.Theme(
        color_scheme_seed      = ft.Colors.GREEN,
        font_family            = "Comfortaa",
        use_material3          = True
    )
    # Aplicacion Primaria
    aplicacion: Primaria = Primaria(
        titulo     = titulo,
        tipografia = tipografia,
        paleta     = paleta
    )
    ft.app(
        target     = aplicacion.start,
        assets_dir = "assets"
    )