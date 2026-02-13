import flet as ft

from pages.PageAddRequests import get_last_num, page_add_requests
from pages.PageAssignEmployees import load_dropdowns_a, page_assign
from pages.PageAuthorization import page_auth
from pages.PageEditRequests import load_dropdowns_e, page_edit_requests
from pages.PageSearch import page_search
from utils.styles import navigation_selected_text_style, navigation_unselected_text_style, page_topic_style


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

def logout(e):
    page_content.content = page_auth
    navigation_menu.visible = False

#==================================================#
#==============MENU AND PAGE CONTENT===============#
#==================================================#
page_content = ft.Container(content=page_search)

add_destination = ft.NavigationRailDestination(icon=ft.Icons.HOME, label="Добавить")
edit_destination = ft.NavigationRailDestination(icon=ft.Icons.EDIT, label="Изменить")
assign_destination = ft.NavigationRailDestination(icon=ft.Icons.ADD, label="Назначить")

navigation_menu = ft.Container(
    margin=ft.Margin.only(top=7),
    width=85,
    content=ft.NavigationRail(
        selected_index=0,
        unselected_label_text_style=navigation_unselected_text_style,
        selected_label_text_style=navigation_selected_text_style,
        margin=ft.Margin.only(left=0),
        height=550,
        on_change=navigate,
        leading=ft.Text("Меню", style=page_topic_style),
        trailing=ft.IconButton(icon=ft.Icons.LOGOUT, icon_size=28, margin=ft.Margin.only(left=10, top=250), on_click=logout),
        destinations=[
            add_destination,
            edit_destination,
            assign_destination
        ]
    )
)

navigation_menu.visible = False
get_last_num()