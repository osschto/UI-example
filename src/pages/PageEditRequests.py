import flet as ft
from sqlmodel import select

from db.db import get_session
from models.tables import Employee, Request
from utils.styles import (card_bgcolor, card_border_color, card_shadow_style,
                          main_text_style, page_topic_style,
                          default_border_color,
                          save_change_btn_style)
from utils.toast import succesfull_toast, warning_toast


#==================================================#
#====================FUNCTIONS=====================#
#==================================================#
def card(topic_icon, topic_text, control, width, height, underline_width):
    return ft.Container(
        width=width,
        height=height,
        padding=ft.Padding(left=10, top=5, right=10, bottom=10),
        bgcolor=card_bgcolor,
        border=ft.Border.all(1, card_border_color),
        border_radius=15,
        shadow=card_shadow_style,
        content=ft.Column(
            controls=[
                ft.Row(
                    [
                        ft.Icon(icon=topic_icon, size=21),
                        ft.Text(topic_text, style=main_text_style)
                    ],
                    margin=ft.Margin.only(left=5, bottom=-10),
                    spacing=8,
                    alignment=ft.CrossAxisAlignment.START
                ),
                ft.Container(bgcolor=ft.Colors.CYAN, width=len(topic_text)*underline_width, height=2, margin=ft.Margin.only(left=7)),
                ft.Row(
                    [
                        control
                    ],
                    alignment=ft.CrossAxisAlignment.CENTER
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

def load_dropdowns_e():
    db = next(get_session())
    requests = db.exec(select(Request)).all()
    employees = db.exec(select(Employee)).all()

    request_dropdown.options = [
        ft.dropdown.Option(
            text=f"№{req.num} - {req.equipment}",
            key=req.num
        ) for req in requests
    ]

    employee_dropdown.options = [
        ft.dropdown.Option(
            text=emp.name,
            key=emp.id
        ) for emp in employees
    ]

def get_all_values(e):
    db = next(get_session()) 
    request_db = db.exec(select(Request).where(Request.num == request_dropdown.value)).one()

    status_group.value = request_db.status
    description_field.value = request_db.description
    employee_dropdown.value = request_db.employee_id

def save_data(e):
    if not request_dropdown.value:
        warning_toast("Выберите заявку")
    elif not employee_dropdown.value:
        warning_toast("Выберите исполнителя")
    elif not status_group.value:
        warning_toast("Выберите статус")
    else:
        db = next(get_session())
        request_db = db.exec(select(Request).where(Request.num == request_dropdown.value)).one()
        employee_db = db.exec(select(Employee).where(Employee.id == employee_dropdown.value)).one()

        request_db.status = status_group.value
        request_db.employee_id = employee_db.id
        request_db.employee_name = employee_db.name
        request_db.description = description_field.value

        db.add(request_db)
        db.commit()

        succesfull_toast("Изменения сохранены")

#==================================================#
#=====================CONTROLS=====================#
#==================================================#

#==================================================#
#=====================REQUEST=====================#
#==================================================#
request_dropdown = ft.Dropdown(leading_icon=ft.Icons.ASSIGNMENT_ROUNDED,
                               text="Выберите заявку", text_style=main_text_style,
                               border_radius=10, border_color=default_border_color,
                               width=300,
                               on_text_change=get_all_values)

request_card = card(ft.Icons.LIST_ALT_ROUNDED, "Заявка", request_dropdown, 365, 115, 12)

#==================================================#
#=====================EMPLOYEE=====================#
#==================================================#
employee_dropdown = ft.Dropdown(leading_icon=ft.Icons.FACE_ROUNDED,
                               text="Выберите исполнителя", text_style=main_text_style,
                               border_radius=10, border_color=default_border_color,
                               width=275)

employee_card = card(ft.Icons.PERSON_ROUNDED, "Исполнитель", employee_dropdown, 335, 130, 11)

#==================================================#
#======================STATUS======================#
#==================================================#
status_group = ft.RadioGroup(
    content=ft.Column(
        spacing=-5,
        margin=ft.Margin.only(top=-5, left=-10),
        controls=[
            ft.Radio(value="awaiting", label="В ожидании",
                     fill_color=ft.Colors.RED, label_style=main_text_style, hover_color=ft.Colors.TRANSPARENT),
            ft.Radio(value="in work", label="В работе",
                     fill_color=ft.Colors.YELLOW, label_style=main_text_style, hover_color=ft.Colors.TRANSPARENT),
            ft.Radio(value="completed", label="Выполнено",
                     fill_color=ft.Colors.GREEN, label_style=main_text_style, hover_color=ft.Colors.TRANSPARENT)
        ]
    )
)

status_card = card(ft.Icons.SYNC_ALT_ROUNDED, "Статус", status_group, 180, 130, 12)

#==================================================#
#====================DESCRIPTION===================#
#==================================================#
description_field = ft.TextField(hint_text="Можно оставить это поле пустым", text_style=main_text_style,
                                 border_color=default_border_color, border_radius=10,
                                 capitalization=ft.TextCapitalization.SENTENCES,
                                 multiline=True, min_lines=3, max_lines=3,
                                 width=475)

description_card = card(ft.Icons.DESCRIPTION_ROUNDED, "Описание", description_field, 530, 155, 12)

#==================================================#
#====================SAVE BUTTON===================#
#==================================================#
save_change_btn = ft.Button("Сохранить изменения", icon=ft.Icons.SAVE_AS_ROUNDED, style=save_change_btn_style,
                     width=300, height=50,
                     on_click=save_data)

#==================================================#
#=======================PAGE=======================#
#==================================================#
page_edit_requests = ft.Column(
    margin=ft.Margin.only(top=15, left=35),
    controls=[
        ft.Row(
            [
                ft.Text("Редактирование заявки", style=page_topic_style)
            ],
            alignment=ft.CrossAxisAlignment.CENTER
        ),
        ft.Row(
            [
                request_card
            ],
            alignment=ft.CrossAxisAlignment.CENTER
        ),
        ft.Row(
            [
                employee_card, status_card
            ],
            alignment=ft.CrossAxisAlignment.CENTER
        ),
        ft.Row(
            [
                description_card
            ],
            alignment=ft.CrossAxisAlignment.CENTER
        ),
        ft.Row(
            [
                save_change_btn
            ],
            alignment=ft.CrossAxisAlignment.CENTER
        )
    ]
)