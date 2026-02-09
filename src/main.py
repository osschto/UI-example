import flet as ft

from db.db import create_db
from pages.PageAddRequests import date_picker, get_last_num, page_add_requests
from pages.PageAssignEmployees import load_dropdowns_a, page_assign
from pages.PageEditRequests import load_dropdowns_e, page_edit_requests
from utils.styles import page_topic_style, navigation_selected_text_style, navigation_unselected_text_style
from utils.toast import set_page

async def main(page: ft.Page):
    page.title = "TASK"
    page.fonts = {"Comic" : "fonts/comic.ttf"}
    page.window.icon = "images/icon.ico"
    page.window.always_on_top = True #develop
    page.window.resizable = False
    page.window.maximizable = False
    page.window.width = 800
    page.window.height = 600
    page.padding = 0
    page.update()

    set_page(page)

    await page.window.center()

    def change_page(e):
        if navigation_menu.content.selected_index == 0:
            page_content.content = page_add_requests
        elif navigation_menu.content.selected_index == 1:
            page_content.content = page_edit_requests
            load_dropdowns_e()
        elif navigation_menu.content.selected_index == 2:
            page_content.content = page_assign
            load_dropdowns_a()

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
            leading=ft.Text("Меню", style=page_topic_style),
            destinations=[
                ft.NavigationRailDestination(icon=ft.Icons.HOME, label="Добавить"),
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
