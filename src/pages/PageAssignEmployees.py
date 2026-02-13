import flet as ft
from sqlmodel import select

from db.db import get_session
from models.tables import Employee, Request
from utils.styles import (card_bgcolor, card_border_color, card_shadow_style,
                          page_topic_style, main_text_style,
                          default_border_color,
                          assign_employee_btn_style)
from utils.toast import succesfull_toast, warning_toast

#==================================================#
#====================FUNCTIONS=====================#
#==================================================#
def card(topic_icon, topic_text, control, width, height, underline_width):
    return ft.Container(
        width=width,
        height=height,
        padding=ft.Padding.only(left=10, top=10, right=10, bottom=10),
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
            ]
        )
    )

def card_with_divider(topic_icon, topic_text, control1, control2, width, height, underline_width):
    return ft.Container(
        width=width,
        height=height,
        padding=ft.Padding.only(left=10, top=10, right=10, bottom=10),
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
                        control1,
                        ft.Container(bgcolor=ft.Colors.CYAN, width=2, height=45),
                        control2
                    ],
                    alignment=ft.CrossAxisAlignment.CENTER
                )
            ]
        )
    )

def load_dropdowns_a():
    db = next(get_session())
    requests = db.exec(select(Request).where(Request.employee_name == None)).all()
    employees = db.exec(select(Employee)).all()

    request_dropdown.options = [
        ft.dropdown.Option(
            text=f"№{req.num} - {req.equipment}",
            key=req.num
        ) for req in requests
    ]

    employee_dropdown.options = [
        ft.dropdown.Option(
            text=e.name,
            key=e.id
        ) for e in employees
    ]

def add_new_employee(e):
    if not new_employee_field.value:
        warning_toast("Заполните поле", 565)
    else:
        db = next(get_session())
        employee_db = Employee(name=new_employee_field.value)

        db.add(employee_db)
        db.commit()

        new_employee_field.value = None
        new_employee_field.hint_text="Напишите ФИО и нажмите Enter"

        succesfull_toast("Исполнитель успешно добавлен", 435)
        load_dropdowns_a()
        
def assign(e):
    if not request_dropdown.value:
        warning_toast("Выберите заявку", 550)
    elif not employee_dropdown.value:
        warning_toast("Выберите исполнителя", 500)
    else:
        db = next(get_session())
        request_db = db.exec(select(Request).where(Request.num == request_dropdown.value)).first()
        employee_db = db.exec(select(Employee).where(Employee.id == employee_dropdown.value)).first()

        request_db.employee_id = employee_db.id
        request_db.employee_name = employee_db.name

        db.add(request_db)
        db.commit()

        request_dropdown.value = None      
        employee_dropdown.value = None
        request_dropdown.hint_text = "Выберите заявку"        
        employee_dropdown.hint_text = "Выберите исполнителя"
    
        succesfull_toast("Исполнитель успешно назначен", 450)
        load_dropdowns_a()        

#==================================================#
#=====================CONTROLS=====================#
#==================================================#

#==================================================#
#===============REQUEST AND EMPLOYEE===============#
#==================================================#
request_dropdown = ft.Dropdown(leading_icon=ft.Icons.ASSIGNMENT_ROUNDED,
                               hint_text="Выберите заявку", hint_style=main_text_style,
                               text_style=main_text_style,
                               border_radius=10, border_color=default_border_color,
                               width=270)

employee_dropdown = ft.Dropdown(leading_icon=ft.Icons.FACE_ROUNDED,
                                hint_text="Выберите исполнителя", hint_style=main_text_style,
                                text_style=main_text_style,
                                border_radius=10, border_color=default_border_color,
                                width=270)

request_and_employee_card = card_with_divider(ft.Icons.VIEW_LIST_ROUNDED, "Заявки и исполнители",
                                              request_dropdown, employee_dropdown,
                                              615, 115, 9.25)

#==================================================#
#===================NEW EMPLOYEE===================#
#==================================================#
new_employee_field = ft.TextField(hint_text="Напишите ФИО и нажмите Enter", text_style=main_text_style,
                                  border_radius=10, border_color=default_border_color,
                                  capitalization=ft.TextCapitalization.WORDS,
                                  width=275,
                                  on_submit=add_new_employee)

new_employee_card = card(ft.Icons.PERSON_ADD_ALT_ROUNDED, "Добавить нового исполнителя",
                         new_employee_field,
                         325, 115, 9)

#==================================================#
#===================ASSING BUTTON==================#
#==================================================#
assign_employee_btn = ft.Button("Назначить", icon=ft.Icons.ASSIGNMENT_TURNED_IN_ROUNDED, style=assign_employee_btn_style,
                                width=200, height=50,
                                on_click=assign)

#==================================================#
#=======================PAGE=======================#
#==================================================#
page_assign = ft.Column(
    margin=ft.Margin.only(top=15, left=35),
    controls=[
        ft.Row(
            [
                ft.Text("Назначение исполнителя", style=page_topic_style)
            ],
            alignment=ft.CrossAxisAlignment.CENTER
        ),
        ft.Row(
            [
                request_and_employee_card
            ],
            alignment=ft.CrossAxisAlignment.CENTER
        ),
        ft.Row(
            [
                new_employee_card
            ],
            alignment=ft.CrossAxisAlignment.CENTER
        ),
        ft.Row(
            [
                assign_employee_btn
            ],
            alignment=ft.CrossAxisAlignment.CENTER
        )
    ]
)