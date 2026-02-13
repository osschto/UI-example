import flet as ft

#==================================================#
#=====================CONTROLS=====================#
#==================================================#
request_table = ft.DataTable(
    expand=True,
    column_spacing=5,
    vertical_lines=ft.BorderSide(width=2, color=ft.Colors.with_opacity(0.15, ft.Colors.WHITE)),
    horizontal_lines=ft.BorderSide(width=2,  color=ft.Colors.with_opacity(0.15, ft.Colors.WHITE)),
    show_bottom_border=True,
    columns=[
        ft.DataColumn(label="№ заявки"),
        ft.DataColumn(label="Дата"),
        ft.DataColumn(label="Имя клиента"),
        ft.DataColumn(label="Оборудование"),
        ft.DataColumn(label="Тип поломки"),
        ft.DataColumn(label="Описание проблемы"),
        ft.DataColumn(label="Статус заявки"),
        ft.DataColumn(label="Исполнитель")
    ],
    rows=[
        ft.DataRow(
            cells=[
                ft.DataCell(ft.Text("123")),
                ft.DataCell(ft.Text("123")),
                ft.DataCell(ft.Text("123")),
                ft.DataCell(ft.Text("123")),
                ft.DataCell(ft.Text("123")),
                ft.DataCell(ft.Text("123")),
                ft.DataCell(ft.Text("123")),
                ft.DataCell(ft.Text("123"))
            ]
        )
    ]
)

#==================================================#
#=======================PAGE=======================#
#==================================================#
page_search = ft.Column(
    controls=[
        ft.Row(
            [
              request_table
            ]
        )
    ]
)