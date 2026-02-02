import flet as ft

current_page = None

def set_page(page):
    global current_page
    current_page = page

def succesfull_toast(text):
    toast = ft.SnackBar(
        content=ft.Row(
            [
                ft.Icon(icon=ft.Icons.CHECK_ROUNDED, size=30, color=ft.Colors.GREEN),
                ft.Text(text, size=16, font_family="Comic")
            ],
            alignment=ft.CrossAxisAlignment.CENTER,
            spacing=2.5,
            margin=ft.Margin.only(left=-7.5)
        ),
        duration=2000,
        behavior=ft.SnackBarBehavior.FLOATING,
        margin=ft.Margin.only(left=450, bottom=20, right=25),
        shape=ft.RoundedRectangleBorder(radius=15)
    )

    current_page.overlay.append(toast)
    toast.open = True

def error_toast(text):
    toast = ft.SnackBar(
        content=ft.Row(
            [
                ft.Icon(icon=ft.Icons.CLEAR_ROUNDED, size=30, color=ft.Colors.RED),
                ft.Text(text, size=16, font_family="Comic")
            ],
            alignment=ft.CrossAxisAlignment.CENTER,
            spacing=0,
            margin=ft.Margin.only(left=-10)
        ),
        duration=2000,
        behavior=ft.SnackBarBehavior.FLOATING,
        margin=ft.Margin.only(left=600, bottom=20, right=25),
        shape=ft.RoundedRectangleBorder(radius=15)
    )

    current_page.overlay.append(toast)
    toast.open = True

def warning_toast(text):
    toast = ft.SnackBar(
        content=ft.Row(
            [
                ft.Icon(icon=ft.Icons.WARNING_AMBER_ROUNDED, size=30, color=ft.Colors.YELLOW_ACCENT),
                ft.Text(text, size=16, font_family="Comic")
            ],
            alignment=ft.CrossAxisAlignment.CENTER,
            spacing=2.5,
            margin=ft.Margin.only(left=-7.5)
        ),
        duration=2000,
        behavior=ft.SnackBarBehavior.FLOATING,
        margin=ft.Margin.only(left=500, bottom=20, right=25),
        shape=ft.RoundedRectangleBorder(radius=15)
    )

    current_page.overlay.append(toast)
    toast.open = True