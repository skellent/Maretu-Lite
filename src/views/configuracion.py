# Importacion de Flet
import flet as ft
# Importacion de Vistas
from views.base import VistaSecundaria

class Configuracion(VistaSecundaria):
    def cambiarColor(instancia) -> ft.Colors:
        color: str|None = instancia.pagina.client_storage.get("color")
        match color:
            case "purple"|None:
                return ft.Colors.DEEP_PURPLE
            case "green":
                return ft.Colors.GREEN
            case "blue":
                return ft.Colors.BLUE
            case "red":
                return ft.Colors.RED

    def cambiarTema(instancia) -> ft.ThemeMode:
        """Método de Personalización a la página"""
        match instancia.pagina.client_storage.get("tema"):
            case "claro":
                return ft.ThemeMode.LIGHT
            case "oscuro":
                return ft.ThemeMode.DARK
            case "sistema" | None:
                return ft.ThemeMode.SYSTEM

    def guardarColor(instancia, e: ft.Event) -> None:
        instancia.pagina.client_storage.set("color", instancia.colorConfiguracion.value)
        instancia.pagina.theme = ft.Theme(
            color_scheme_seed = instancia.cambiarColor(),
            font_family       = "Comfortaa",
            use_material3     = True
        )
        instancia.pagina.update()
        return None

    def guardarTema(instancia, e: ft.EventType) -> None:
        instancia.pagina.client_storage.set("tema", instancia.temaConfiguracion.value)
        instancia.pagina.theme_mode = instancia.cambiarTema()
        instancia.pagina.update()
        return None

    def __init__(instancia, pagina: ft.Page) -> None:
        """Método de construcción"""
        instancia.pagina = pagina
        instancia.colorConfiguracion: ft.RadioGroup = ft.RadioGroup(
            content = ft.Column(
                [
                    ft.Text(
                        value = "Paleta de Colores",
                        text_align = ft.TextAlign.CENTER,
                        size = 20
                    ),
                    ft.Radio(
                        value = "purple",
                        label = "Morado"
                    ),
                    ft.Radio(
                        value = "green",
                        label = "Verde"
                    ),
                    ft.Radio(
                        value = "blue",
                        label = "Azul"
                    ),
                    ft.Radio(
                        value = "red",
                        label = "Rojo"
                    )
                ],
            ),
            on_change = instancia.guardarColor
        )
        instancia.temaConfiguracion: ft.RadioGroup = ft.RadioGroup(
            content = ft.Column(
                [
                    ft.Text(
                        value = "Tema de Iluminación",
                        text_align = ft.TextAlign.CENTER,
                        size = 20
                    ),
                    ft.Radio(
                        value = "sistema",
                        label = "Sistema (Default)"
                    ),
                    ft.Radio(
                        value = "claro",
                        label = "Claro"
                    ),
                    ft.Radio(
                        value = "oscuro",
                        label = "Oscuro"
                    )
                ],
            ),
            on_change = instancia.guardarTema
        )
        instancia.depuracion: ft.Column = ft.Column(
            controls = [
                ft.Text(
                    value = "Depuración",
                    text_align = ft.TextAlign.CENTER,
                    size = 20
                ),
                ft.Text( value = f"Ruta de E & L => {None}" )
            ]
        )
        if instancia.pagina.client_storage.get("color") == None:
            instancia.pagina.colorConfiguracion.value = "purple" 
        else:
            instancia.colorConfiguracion.value = instancia.pagina.client_storage.get("color")
        if instancia.pagina.client_storage.get("tema") == None:
            instancia.temaConfiguracion.value = "sistema"
        else:
            instancia.temaConfiguracion.value = instancia.pagina.client_storage.get("tema")
        instancia.controles: list[ft.Container] = [
            ft.Container(
                expand = True,
                content = ft.ListView(
                    spacing = 5,
                    controls = [
                        ft.Container(
                            content = instancia.colorConfiguracion,
                            border_radius = 35,
                            bgcolor = ft.Colors.SURFACE_CONTAINER_HIGHEST,
                            padding = 25
                        ),
                        ft.Container(
                            content = instancia.temaConfiguracion,
                            border_radius = 35,
                            bgcolor = ft.Colors.SURFACE_CONTAINER_HIGHEST,
                            padding = 25
                        ),
                        ft.Container(
                            content = instancia.depuracion,
                            border_radius = 35,
                            bgcolor = ft.Colors.SURFACE_CONTAINER_HIGHEST,
                            padding = 25
                        )
                    ]
                )
            )
        ]
        super().__init__(
            pagina,
            "Configuración",
            instancia.controles,
            "/configuracion"
        )
        return None