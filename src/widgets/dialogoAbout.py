import flet as ft

dialogoAbout = ft.AlertDialog(
    modal = True,
    title = ft.Text("Skell's Maretu Lite"),
    content = ft.Text("Aplicación de punto de venta local para Android y Windows."),
    actions = [
        ft.TextButton("Aceptar", on_click = lambda e: page.close(dialogoAbout))
    ],
    actions_alignment = ft.MainAxisAlignment.END
)