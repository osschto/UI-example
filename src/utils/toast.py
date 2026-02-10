import flet as ft

current_page = None

def set_page(page):
    global current_page
    current_page = page

def succesfull_toast(text, margin_left):
    toast = ft.SnackBar(
        content=ft.Row(
            [
                ft.Icon(icon=ft.Icons.CHECK_ROUNDED, size=30, color=ft.Colors.GREEN),
                ft.Text(text, size=16, weight=ft.FontWeight.W_500, font_family="Comic")
            ],
            alignment=ft.CrossAxisAlignment.CENTER,
            spacing=2.5,
            margin=ft.Margin.only(left=-7.5)
        ),
        bgcolor=ft.Colors.with_opacity(0.8, color=ft.Colors.WHITE),
        duration=2000,
        behavior=ft.SnackBarBehavior.FLOATING,
        margin=ft.Margin.only(left=margin_left, bottom=20, right=25),
        shape=ft.RoundedRectangleBorder(radius=15)
    )

    current_page.overlay.append(toast)
    toast.open = True

def warning_toast(text, margin_left):
    toast = ft.SnackBar(
        content=ft.Row(
            [
                ft.Icon(icon=ft.Icons.WARNING_AMBER_ROUNDED, size=30, color=ft.Colors.YELLOW_ACCENT),
                ft.Text(text, size=16, weight=ft.FontWeight.W_500, font_family="Comic")
            ],
            alignment=ft.CrossAxisAlignment.CENTER,
            spacing=2.5,
            margin=ft.Margin.only(left=-7.5)
        ),
        bgcolor=ft.Colors.with_opacity(0.8, color=ft.Colors.WHITE),        
        duration=2000,
        behavior=ft.SnackBarBehavior.FLOATING,
        margin=ft.Margin.only(left=margin_left, bottom=20, right=25),
        shape=ft.RoundedRectangleBorder(radius=15)
    )

    current_page.overlay.append(toast)
    toast.open = True