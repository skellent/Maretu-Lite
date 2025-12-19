import flet as ft

def main(page: ft.Page):
    page.title = "Skell's Maretu Lite"
    # page.window.full_screen = True
    page.fonts = {
        "Comfortaa": "../fonts/comfortaa.ttf"
    }
    page.theme = ft.Theme(
        font_family = "Comfortaa"
    )
    page.appbar = ft.AppBar(
        leading = ft.Container(
            content = ft.Image(
                src = "./icon-white.svg",
                fit = ft.ImageFit.CONTAIN,
            ),
            padding = 8
        ),
        title = ft.Text(
            "Skell's Maretu Lite",
            color = ft.Colors.WHITE
        ),
        center_title = True,
        bgcolor = ft.Colors.DEEP_PURPLE
    )

    page.update()

ft.app(
    target = main,
    assets_dir = "assets"
)