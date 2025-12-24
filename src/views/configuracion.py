import flet as ft
from modules              import configurarRuta
from widgets.dialogoAbout import DialogoAbout
from widgets.appBar       import AppBarSecundaria
from typing import Any

def configuracion(page: ft.Page) -> Any:
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
    def guardarColor(e) -> None:
        page.client_storage.set("color", colorConfiguracion.value)
        page.theme = ft.Theme( color_scheme_seed = cambiarColor() )
        page.update()
    def guardarTema(e) -> None:
        page.client_storage.set("tema", temaConfiguracion.value)
        page.theme_mode = cambiarTema()
        page.update()

    colorConfiguracion: Any = ft.RadioGroup(
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
        on_change = guardarColor
    )
    temaConfiguracion: Any = ft.RadioGroup(
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
        on_change = guardarTema
    )
    depuracion: Any = ft.Column(
        controls = [
            ft.Text(
                value = "Depuración",
                text_align = ft.TextAlign.CENTER,
                size = 20
            ),
            ft.Text( value = f"Ruta de E & L => {configurarRuta.rutaSegura()}" )
        ]
    )

    if page.client_storage.get("color") == None:
        colorConfiguracion.value = "purple" 
    else:
        colorConfiguracion.value = page.client_storage.get("color")
    if page.client_storage.get("tema") == None:
        temaConfiguracion.value = "sistema"
    else:
        temaConfiguracion.value = page.client_storage.get("tema")

    dialogoAbout: DialogoAbout = DialogoAbout(page)
    return ft.View(
        "/configuracion",
        controls = [
            AppBarSecundaria(page, dialogoAbout, "Confguración"),
            ft.Container(
                expand = True,
                content = ft.ListView(
                    spacing = 5,
                    controls = [
                        ft.Container(
                            content = colorConfiguracion,
                            border_radius = 35,
                            bgcolor = ft.Colors.SURFACE_CONTAINER_HIGHEST,
                            padding = 25
                        ),
                        ft.Container(
                            content = temaConfiguracion,
                            border_radius = 35,
                            bgcolor = ft.Colors.SURFACE_CONTAINER_HIGHEST,
                            padding = 25
                        ),
                        ft.Container(
                            content = depuracion,
                            border_radius = 35,
                            bgcolor = ft.Colors.SURFACE_CONTAINER_HIGHEST,
                            padding = 25
                        )
                    ]
                )
            )
        ]
    )