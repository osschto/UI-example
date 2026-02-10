import hashlib

import flet as ft
from sqlmodel import select

from db.db import get_session
from models.tables import User
from utils.navigation import page_add_requests
from utils.styles import (card_bgcolor, card_border_color, card_shadow_style,
                          main_text_style, page_topic_style,
                          default_border_color, field_label_text_style,
                          auth_btn_style)
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
                        ft.Container(content=ft.Text("Создать аккаунт", style=main_text_style), on_click=navigate)
                    ],
                     alignment=ft.CrossAxisAlignment.CENTER
                )
            ]
        )
    )

def succesfull_auth():
    from utils.navigation import navigation_menu, page_content
    page_content.content = page_add_requests
    navigation_menu.visible = True

def navigate(e):
    from utils.navigation import page_content
    from pages.PageRegistration import reg
    page_content.content = reg

def authorize(e):
    if not login_field.value:
        warning_toast("Введите логин", 575)
    elif not password_field.value:
        warning_toast("Введите пароль", 575)
    else:
        db = next(get_session())

        password = password_field.value
        hash_password = hashlib.sha256(password.encode()).hexdigest()
        
        user_db = db.exec(select(User).where(User.pas == hash_password)).first()
        if user_db:
            succesfull_auth()
            succesfull_toast("Успешный вход", 550)
        else:
            warning_toast("Неверный логин или пароль", 450)


login_field = ft.TextField(label="Введите логин", label_style=field_label_text_style,
                           border_color=default_border_color, border_radius=10,
                           text_style=main_text_style)
password_field = ft.TextField(label="Введите пароль", label_style=field_label_text_style,
                              border_color=default_border_color, border_radius=10,
                              text_style=main_text_style,
                              password=True)

auth_btn = ft.Button("Авторизоваться", style=auth_btn_style,
                     width=200, height=40,
                     on_click=authorize)

log_and_pass_card = card("Авторизация",
                         login_field, password_field, auth_btn,
                         350, 275)

auth = ft.Column(
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