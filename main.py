import flet as ft
import os

# arquivo = ft.FilePicker()
# ler_arquivo_excel = open("","w")


def click(e):
    print("Click")


def main(page: ft.Page):
    page.title = "Gerador de Encartes"
    page.theme = ft.Theme(color_scheme_seed=ft.Colors.GREEN_400)
    page.fonts = {
        "normal": "fonts/RobotoCondensed-Light.ttf",
        "normal_italic": "fonts/RobotoCondensed-LightItalic.ttf",
        "titulo": "fonts/RobotoCondensed-Medium.ttf",
    }
    page.navigation_bar = ft.CupertinoNavigationBar(
        bgcolor=ft.Colors.BLUE,
        inactive_color=ft.Colors.BLACK,
        active_color=ft.Colors.WHITE,
        on_change=lambda e: print("Selecionar", e.control.selected_index),
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.FOLDER_OPEN, label="Header"),
            ft.NavigationBarDestination(icon=ft.Icons.FOLDER_OPEN, label="Footer"),
            ft.NavigationBarDestination(icon=ft.Icons.PLAY_CIRCLE, label="Gerar")
        ],
    )

    texto = ft.Text("Gerador de Encartes", size=50,font_family='titulo')

    # botao = ft.ElevatedButton(
    #                         "Gerar Encarte",
    #                         on_click=click,
    #                         on_focus=True,
    #                         color='Green',
    #                         icon=ft.Icons.PLAY_CIRCLE,
    #                         width=320)
    # header = ft.ElevatedButton(
    #                         "Adicionar Header",
    #                         on_click=click,
    #                         on_focus=True,
    #                         color='Red',
    #                         icon=ft.Icons.ADD_TO_PHOTOS,
    #                         style=ft.ButtonStyle(overlay_color=ft.Colors.RED_50),
    #                         width=320)

    # footer = ft.ElevatedButton(
    #                         "Adicionar Footer",
    #                         on_click=click,
    #                         on_focus=True,
    #                         color='Red',
    #                         icon=ft.Icons.ADD_TO_PHOTOS,
    #                         style=ft.ButtonStyle(overlay_color=ft.Colors.RED_50),
    #                         width=320)

    page.add(
        ft.Column(
            [
                ft.Row([texto], alignment=ft.MainAxisAlignment.CENTER),
                # ft.Row([header,footer], alignment=ft.MainAxisAlignment.CENTER),
                # ft.Row([botao], alignment=ft.MainAxisAlignment.CENTER)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )


ft.app(target=main)
