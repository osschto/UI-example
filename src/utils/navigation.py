import flet as ft
from utils.styles import navigation_selected_text_style, navigation_unselected_text_style, page_topic_style
from pages.PageAddRequests import get_last_num, page_add_requests
from pages.PageAssignEmployees import load_dropdowns_a, page_assign
from pages.PageEditRequests import load_dropdowns_e, page_edit_requests
from pages.PageRegistration import reg
from pages.PageLogin import log

#==================================================#
#====================FUNCTIONS=====================#
#==================================================#
def navigate(e):
    if navigation_menu.content.selected_index == 0:
        page_content.content = page_add_requests
    elif navigation_menu.content.selected_index == 1:
        page_content.content = page_edit_requests
        load_dropdowns_e()
    elif navigation_menu.content.selected_index == 2:
        page_content.content = page_assign
        load_dropdowns_a()

#==================================================#
#==============MENU AND PAGE CONTENT===============#
#==================================================#
page_content = ft.Container(content=log)

navigation_menu = ft.Container(
    margin=ft.Margin.only(top=7),
    width=85,
    content=ft.NavigationRail(
        selected_index=0,
        unselected_label_text_style=navigation_unselected_text_style,
        selected_label_text_style=navigation_selected_text_style,
        margin=ft.Margin.only(left=0),
        height=200,
        on_change=navigate,
        leading=ft.Text("Меню", style=page_topic_style),
        destinations=[
            ft.NavigationRailDestination(icon=ft.Icons.HOME, label="Добавить"),
            ft.NavigationRailDestination(icon=ft.Icons.EDIT, label="Изменить"),
            ft.NavigationRailDestination(icon=ft.Icons.ADD, label="Назначить")
        ]
    )
)

navigation_menu.visible = False
get_last_num()