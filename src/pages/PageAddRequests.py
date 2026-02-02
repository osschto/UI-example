import flet as ft
from sqlmodel import desc, select

from db.db import get_session
from models.tables import Request
from utils.toast import succesfull_toast, warning_toast
from utils.styles import default_text_style, default_border_style, add_data_btn_style

#-------------------------FUNCTIONS-------------------------#
def open_date_picker(e):
    date_picker.open = True
    date_picker.update()

def save_date(e):
    if date_picker.value:
        local_date = date_picker.value.astimezone()
        date_field.value = local_date.strftime("%d.%m.%Y")
        date_field.update()

def update_page():
    num_field.value = None
    date_field.value = None
    equipment_field.value = None
    type_field.value = None
    description_field.value = None
    client_field.value = None
    status_group.value = None
    get_last_num()

def get_last_num():
    db = next(get_session())
    last_num = db.exec(select(Request).order_by(Request.num.desc())).first()
    
    if last_num:
        num_field.value = last_num.num + 1 
    else:
        num_field.value = 1

def save_data(e):
    db = next(get_session())
    try:
        request_db = Request(
            num = num_field.value,
            date = date_picker.value.date(),
            equipment = equipment_field.value,
            type = type_field.value,
            description = description_field.value,
            client = client_field.value,
            status = status_group.value
        )

        db.add(request_db)
        db.commit()

        succesfull_toast("Заявка успешно добавлена")
        update_page()

    except Exception:
        warning_toast("Заполните все поля")
#-------------------------FUNCTIONS-------------------------#

#-------------------------CONTROLS-------------------------#
num_field = ft.TextField(label="Номер заказа", text_style=default_text_style,
                         border_color=default_border_style, read_only=True, width=200)

date_field = ft.TextField(label="Дата добавления", hint_text="ДД.ММ.ГГГГ",
                          text_style=default_text_style, border_color=default_border_style,
                          read_only=True, width=200, on_click=open_date_picker)

date_picker = ft.DatePicker(on_change=save_date)

equipment_field = ft.TextField(label="Оборудование", hint_text="Например, телевизор",
                               text_style=default_text_style, border_color=default_border_style,
                               width=265)

type_field = ft.TextField(label="Тип неисправности", hint_text="Например, короткое замыкание",
                          text_style=default_text_style, border_color=default_border_style,
                          width=265)

description_field = ft.TextField(label="Описание проблемы", text_style=default_text_style,
                                 border_color=default_border_style, multiline=True, max_lines=5,
                                 width=540)

client_field = ft.TextField(label="Клиент, сделавший заказ", hint_text="Введите имя клиента",
                            text_style=default_text_style, border_color=default_border_style,
                            width=250)

status_group = ft.RadioGroup(
    content=ft.Column(
        controls=[
            ft.Radio(value="awaiting", label="В ожидании",
                     fill_color=ft.Colors.RED, label_style=default_text_style, hover_color=ft.Colors.TRANSPARENT),
            ft.Radio(value="in work", label="В работе",
                     fill_color=ft.Colors.YELLOW, label_style=default_text_style, hover_color=ft.Colors.TRANSPARENT),
            ft.Radio(value="completed", label="Выполнено",
                     fill_color=ft.Colors.GREEN, label_style=default_text_style, hover_color=ft.Colors.TRANSPARENT)
        ],
        spacing=0
    )
)

add_data_btn = ft.Button("Добавить", style=add_data_btn_style,
                         width=150, height=50, on_click=save_data)
#-------------------------CONTROLS-------------------------#

#-------------------------PAGE-------------------------#
page_add_requests = ft.Column(
        controls = [
            ft.Row(
                [
                    ft.Text("Добавление заявки", size=18, font_family="Comic")
                ],
                alignment=ft.CrossAxisAlignment.CENTER
            ),
            ft.Row(
                [
                    num_field,
                    date_field
                ],
                alignment=ft.CrossAxisAlignment.CENTER
            ),
            ft.Row(
                [
                    equipment_field,
                    type_field
                ],
                alignment=ft.CrossAxisAlignment.CENTER
            ),
            ft.Row(
                [
                    description_field
                ],
                alignment=ft.CrossAxisAlignment.CENTER
            ),
            ft.Row(
                [
                    client_field,
                    status_group
                ],
                alignment=ft.CrossAxisAlignment.CENTER
            ),
            ft.Row(
                [
                    add_data_btn,
                ],
                alignment=ft.CrossAxisAlignment.CENTER
            )
        ]
)
#-------------------------PAGE-------------------------#