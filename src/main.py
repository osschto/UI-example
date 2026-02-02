import flet as ft

from pages.PageAddRequests import date_picker, page_add_requests, get_last_num
from pages.PageEditRequests import page_edit_requests
from db.db import create_db
from utils.toast import set_page
from utils.styles import navigation_selected_text_style, navigation_unselected_text_style

async def main(page: ft.Page):
    page.title = "TASK"
    page.fonts = {"Comic" : "fonts/comic.ttf"}
    page.window.icon = "images/icon.ico"
    page.window.resizable = False
    page.window.maximizable = False
    page.window.width = 750
    page.window.height = 500
    page.padding = 0
    page.update()

    set_page(page)

    await page.window.center()

    def change_page(e):
        if navigation_menu.content.selected_index == 0:
            page_content.content = page_add_requests
        elif navigation_menu.content.selected_index == 1:
            page_content.content = page_edit_requests

    page_content = ft.Container(
        content=page_add_requests
    )

    navigation_menu = ft.Container(
        width=85,
        content=ft.NavigationRail(
            selected_index=0,
            unselected_label_text_style=navigation_unselected_text_style,
            selected_label_text_style=navigation_selected_text_style,
            margin=ft.Margin.only(left=0),
            height=200,
            on_change=change_page,
            leading=ft.Text("Меню", size=18, font_family="Comic"),
            destinations=[
                ft.NavigationRailDestination(icon=ft.Icons.HOME, label="Главная"),
                ft.NavigationRailDestination(icon=ft.Icons.EDIT, label="Изменить"),
                ft.NavigationRailDestination(icon=ft.Icons.ADD, label="Назначить")
            ]
        )
    )

    page.overlay.append(date_picker)
    page.add(
        ft.Stack(
            [
                page_content,
                navigation_menu
            ]
        )
    )

if __name__ == "__main__":
    create_db()
    get_last_num()
    ft.run(main, assets_dir="assets")
