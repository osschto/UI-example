import flet as ft

from db.db import create_db
from utils.navigation import navigation_menu, page_content
from utils.toast import set_page


async def main(page: ft.Page):
    page.title = "TASK"
    page.fonts = {"Comic" : "fonts/comic.ttf"}
    page.window.icon = "images/icon.ico"
    page.window.always_on_top = True
    page.window.resizable = False
    page.window.maximizable = False
    page.window.width = 800
    page.window.height = 600
    page.padding = 0
    page.update()

    set_page(page)

    await page.window.center()

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
    ft.run(main, assets_dir="assets")
