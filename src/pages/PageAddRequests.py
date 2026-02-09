import flet as ft
from sqlmodel import desc, select

from db.db import get_session
from models.tables import Request
from utils.styles import (card_shadow_style, card_bgcolor, card_border_color,
                          main_text_style, page_topic_style,
                          default_border_color,
                          add_data_btn_style)
from utils.toast import succesfull_toast, warning_toast

#==================================================#
#====================FUNCTIONS=====================#
#==================================================#
def card(topic_icon, topic_text, control1, control2, control3, control4, control5, control6, control7, width, height, underline_width):
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
                        control1,
                        ft.Container(bgcolor=ft.Colors.CYAN, width=2, height=45),
                        control2,
                        ft.Container(bgcolor=ft.Colors.CYAN, width=2, height=45),
                        control3
                    ],
                    alignment=ft.CrossAxisAlignment.CENTER
                ),
                ft.Row(
                    [
                        control4,
                        ft.Container(bgcolor=ft.Colors.CYAN, width=2, height=45),
                        control5
                    ],
                    alignment=ft.CrossAxisAlignment.CENTER                    
                ),
                ft.Row(
                    [
                        control6,
                        ft.Container(bgcolor=ft.Colors.CYAN, width=2, height=45),
                        control7
                    ],
                    alignment=ft.CrossAxisAlignment.CENTER                    
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

#==================================================#
#=====================CONTROLS=====================#
#==================================================#
num_field = ft.TextField(label="№ заявки", text_style=main_text_style,
                         border_color=default_border_color, border_radius=10,
                         width=110,
                         read_only=True)

date_field = ft.TextField(label="Дата", text_style=main_text_style,
                          hint_text="ДД.ММ.ГГГГ", hint_style=main_text_style,
                          width=150,
                          border_color=default_border_color, border_radius=10)

client_name_field = ft.TextField(label="Имя клиента", text_style=main_text_style,
                          hint_text="Введите имя клиента", hint_style=main_text_style,
                          width=250,
                          border_color=default_border_color, border_radius=10)

equipment_field = ft.TextField(label="Оборудовние", text_style=main_text_style,
                          hint_text="Например, телевизор", hint_style=main_text_style,
                          width=250,
                          border_color=default_border_color, border_radius=10)

type_field = ft.TextField(label="Тип поломки", text_style=main_text_style,
                          hint_text="Например, короткое замыкание", hint_style=main_text_style,
                          width=250,
                          border_color=default_border_color, border_radius=10)

description_field = ft.TextField(label="Описание проблемы", text_style=main_text_style,
                          hint_text="Можно оставить это поле пустым", hint_style=main_text_style,
                          width=400, height=150,
                          min_lines=3, max_lines=3, multiline=True,
                          border_color=default_border_color, border_radius=10)

status_group = ft.RadioGroup(
    content=ft.Column(
        spacing=0,
        margin=ft.Margin.only(left=0, top=-50, right=0, bottom=0),
        controls=[
            ft.Text("Статус заявки", style=main_text_style),
            ft.Radio(label="В ожидании", label_style=main_text_style),
            ft.Radio(label="В работе", label_style=main_text_style),
            ft.Radio(label="Выполнено", label_style=main_text_style)
        ]
    )
)

all_controls_card = card(ft.Icons.ALL_INBOX, "Добавление заявки",
                         num_field, date_field, client_name_field,
                         equipment_field, type_field,
                         description_field, status_group,
                         600, 325, 9.5)

#==================================================#
#=======================PAGE=======================#
#==================================================#
page_add_requests = ft.Column(
    margin=ft.Margin.only(top=15, left=35),
    controls = [
        ft.Row(
            [
                ft.Text("Добавление заявки", style=page_topic_style)
            ],
            alignment=ft.CrossAxisAlignment.CENTER
        ),
        ft.Row(
            [
                all_controls_card
            ],
            alignment=ft.CrossAxisAlignment.CENTER
        )
    ]
)