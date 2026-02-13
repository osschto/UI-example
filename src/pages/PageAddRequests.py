import flet as ft
from sqlmodel import desc, select
from datetime import datetime

from db.db import get_session
from models.tables import Request
from utils.styles import (card_shadow_style, card_bgcolor, card_border_color,
                          main_text_style, page_topic_style, field_label_text_style,
                          default_border_color,
                          add_data_btn_style)
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

def get_last_num():
    db = next(get_session())
    request_db = db.exec(select(Request).order_by(desc(Request.num))).first()
    
    if not request_db:
        num_field.value = 1
    else:
        num_field.value = request_db.num + 1

def open_date_picker(e):
    e.page.overlay.append(date_picker)
    date_picker.open = True

def set_date(e):
    date = date_picker.value
    local_date = date.astimezone().strftime("%d.%m.%Y")
    
    date_field.value = local_date

def save_data(e):
    if not date_field.value:
        warning_toast("Введите дату", 575)
    elif not client_field.value:
        warning_toast("Введите имя клиента", 515)
    elif not equipment_field.value:
        warning_toast("Введите оборудование", 515)
    elif not type_field.value:
        warning_toast("Введите тип поломки", 525)
    else:
        db = next(get_session())
        request_db = Request(
            num=num_field.value,
            date=date_picker.value,
            equipment=equipment_field.value,
            type=type_field.value,
            description=description_field.value,
            client=client_field.value,
            status=status_group.value)

        db.add(request_db)
        db.commit()

        num_field.value = None
        date_field.value = None
        equipment_field.value = None
        type_field.value = None
        description_field.value = None
        client_field.value = None
        status_group.value = "awaiting"

        succesfull_toast("Заявка успешно добавлена", 475)
        get_last_num()

#==================================================#
#=====================CONTROLS=====================#
#==================================================#

#==================================================#
#=================NUMBER AND DATE==================#
#==================================================#
num_field = ft.TextField(label="№ заявки", label_style=field_label_text_style,
                         text_style=main_text_style,
                         border_color=default_border_color, border_radius=10,
                         width=110,
                         read_only=True)

date_field = ft.TextField(label="Дата", label_style=field_label_text_style,
                          hint_text="ДД.ММ.ГГГГ", hint_style=main_text_style,
                          text_style=main_text_style,
                          border_color=default_border_color, border_radius=10,
                          width=150,
                          on_click=open_date_picker)

date_picker = ft.DatePicker(entry_mode=ft.DatePickerEntryMode.CALENDAR_ONLY,
                            locale=ft.Locale("ru"),
                            last_date=datetime.now(),
                            on_change=set_date)

num_and_date_card = card_with_divider(ft.Icons.DATE_RANGE_ROUNDED, "Номер и дата",
                                      num_field, date_field,
                                      325, 115, 10)

#==================================================#
#====================CLIENT NAME===================#
#==================================================#
client_field = ft.TextField(hint_text="Введите имя клиента", hint_style=main_text_style,
                            text_style=main_text_style, capitalization=ft.TextCapitalization.SENTENCES,
                            border_color=default_border_color, border_radius=10,
                            width=250)

client_card = card(ft.Icons.FACE_6_ROUNDED, "Имя клиента",
                   client_field,
                   290, 115, 10.5)

#==================================================#
#================EQUIPMENT AND TYPE================#
#==================================================#
equipment_field = ft.TextField(label="Оборудование", label_style=field_label_text_style,
                          hint_text="Например, телевизор", hint_style=main_text_style,
                          text_style=main_text_style, capitalization=ft.TextCapitalization.SENTENCES,
                          border_color=default_border_color, border_radius=10,
                          width=281)

type_field = ft.TextField(label="Тип поломки", label_style=field_label_text_style,
                          hint_text="Например, короткое замыкание", hint_style=main_text_style,
                          text_style=main_text_style, capitalization=ft.TextCapitalization.SENTENCES,
                          border_color=default_border_color, border_radius=10,
                          width=281)

equipment_and_type_card = card_with_divider(ft.Icons.ARTICLE_ROUNDED, "Оборудование и тип",
                                            equipment_field, type_field,
                                            625, 115, 9.5)

#==================================================#
#====================DESCRIPTION===================#
#==================================================#
description_field = ft.TextField(hint_text="Можно оставить это поле пустым", hint_style=main_text_style,
                                 text_style=main_text_style, capitalization=ft.TextCapitalization.SENTENCES,
                                 min_lines=3, max_lines=3, multiline=True,
                                 border_color=default_border_color, border_radius=10,
                                 width=395, height=150)

description_card = card(ft.Icons.DESCRIPTION, "Описание проблемы",
                        description_field,
                        440, 160, 10.25)

#==================================================#
#======================STATUS======================#
#==================================================#
status_group = ft.RadioGroup(
    value="awaiting",
    content=ft.Column(
        spacing=0,
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

status_card = card(ft.Icons.SYNC_ALT_ROUNDED, "Статус",
                   status_group,
                   175, 160, 12)

#==================================================#
#====================ADD BUTTON====================#
#==================================================#
add_data_btn = ft.Button("Добавить", icon=ft.Icons.ADD_BOX_ROUNDED, style=add_data_btn_style,
                         width=200, height=50,
                         on_click=save_data)

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
                num_and_date_card, client_card
            ],
            alignment=ft.CrossAxisAlignment.CENTER
        ),
        ft.Row(
            [
                equipment_and_type_card
            ],
            alignment=ft.CrossAxisAlignment.CENTER
        ),
        ft.Row(
            [
                description_card, status_card
            ],
            alignment=ft.CrossAxisAlignment.CENTER
        ),
        ft.Row(
            [
                add_data_btn
            ],
            alignment=ft.CrossAxisAlignment.CENTER
        )
    ]
)