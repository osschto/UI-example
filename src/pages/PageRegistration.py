import hashlib

import flet as ft
from sqlmodel import select

from db.db import get_session
from models.tables import User
from utils.styles import (card_bgcolor, card_border_color, card_shadow_style,
                          main_text_style, page_topic_style,
                          default_border_color, field_label_text_style,
                          reg_btn_style)
from utils.toast import succesfull_toast, warning_toast


def card(topic_text, control1, control2, btn, width, height):
    return ft.Container(
        width=width,
        height=height,
        padding=ft.Padding.only(left=10, top=25, right=10, bottom=10),
        bgcolor=card_bgcolor,
        border=ft.Border.all(1, card_border_color),
        border_radius=15,
        shadow=card_shadow_style,
        content=ft.Column(
            controls=[
                ft.Row(
                    [
                        ft.Text(topic_text, style=page_topic_style)
                    ],
                    margin=ft.Margin.only(bottom=15),
                    spacing=8,
                    alignment=ft.CrossAxisAlignment.CENTER
                ),
                ft.Row(
                    [
                        control1
                        
                    ],
                    alignment=ft.CrossAxisAlignment.CENTER
                ),
                ft.Row(
                    [
                        control2
                    ],
                    alignment=ft.CrossAxisAlignment.CENTER
                ),
                ft.Row(
                    [
                        btn
                    ],
                     alignment=ft.CrossAxisAlignment.CENTER
                ),
                ft.Row(
                    [
                        ft.Container(content=ft.Text("Войти в аккаунт", style=main_text_style), on_click=navigate)
                    ],
                     alignment=ft.CrossAxisAlignment.CENTER
                )
            ]
        )
    )

def succesfull_reg():
    from utils.navigation import page_content
    from pages.PageAuthorization import auth
    page_content.content = auth

def navigate(e):
    from pages.PageAuthorization import auth
    from utils.navigation import page_content
    page_content.content = auth

def register(e):
    db = next(get_session())
    user_db = db.exec(select(User).where(User.log == login_field.value)).first()
    if user_db:
        warning_toast("Пользователь уже существует", 450)
    elif not login_field.value:
        warning_toast("Введите логин", 575)
    elif not password_field.value:
        warning_toast("Введите пароль", 575)
    else:
        login = login_field.value
        password = password_field.value
        hash_password = hashlib.sha256(password.encode()).hexdigest()

        user_db = User(log=login, pas=hash_password)

        db.add(user_db)
        db.commit()

        login_field.value = None
        password_field.value = None

        succesfull_reg()
        succesfull_toast("Зарегестрировано", 550)

login_field = ft.TextField(label="Введите логин", label_style=field_label_text_style,
                           border_color=default_border_color, border_radius=10,
                           text_style=main_text_style)
password_field = ft.TextField(label="Введите пароль", label_style=field_label_text_style,
                              border_color=default_border_color, border_radius=10,
                              text_style=main_text_style,
                              password=True)

reg_btn = ft.Button("Зарегестрироваться", style=reg_btn_style,
                    width=200, height=40,
                    on_click=register)

log_and_pass_card = card("Регистрация",
                         login_field, password_field, reg_btn,
                         350, 275)

reg = ft.Column(
    margin=ft.Margin.only(top=90),
    controls=[
        ft.Row(
            [
                log_and_pass_card
            ],
            alignment=ft.CrossAxisAlignment.CENTER
        )
    ],
    alignment=ft.MainAxisAlignment.END
)