import flet as ft
from sqlmodel import select

from db.db import get_session
from models.tables import Request, Employee
from utils.styles import default_border_style, default_text_style


def get_data():
    db = next(get_session())
    requests = db.exec(select(Request)).all()
    employees = db.exec(select(Employee)).all()

    request_dropdown.options = [
        ft.dropdown.Option(
            text=f"{req.num} - {req.equipment}",
            key=req.num
        ) for req in requests
    ]

    employee_dropdown.options = [
        ft.dropdown.Option(
            text=e.name,
            key=e.id
        ) for e in employees
    ]

request_dropdown = ft.Dropdown(text="Выберите заявку", text_style=default_text_style,
                               border_color=default_border_style,
                               width=250, height=100
)

employee_dropdown = ft.Dropdown(text="Выберите исполнителя", text_style=default_text_style,
                                   border_color=default_border_style,
                                   width=250, height=100
)

page_assign = ft.Column(
    controls=[
        ft.Row(
            [
                ft.Text("Назначение исполнителя", size=18, font_family="Comic")
            ],
            alignment=ft.CrossAxisAlignment.CENTER
        ) ,
        ft.Row(
            [
                request_dropdown,
                employee_dropdown
            ],
            alignment=ft.CrossAxisAlignment.CENTER
        )
    ]
)