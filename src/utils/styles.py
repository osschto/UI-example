import flet as ft

#==================================================#
#========================TEXT======================#
#==================================================#
main_text_style = ft.TextStyle(size=14, font_family="Comic")
page_topic_style = ft.TextStyle(size=20, weight=ft.FontWeight.W_600, font_family="Comic")
navigation_selected_text_style = ft.TextStyle(size=14, font_family="Comic")
navigation_unselected_text_style = ft.TextStyle(size=12, font_family="Comic")

#==================================================#
#========================CARD======================#
#==================================================#
card_border_color = ft.Colors.with_opacity(0.1, color=ft.Colors.WHITE)
card_bgcolor = ft.Colors.with_opacity(0.05, color=ft.Colors.WHITE)
card_shadow_style = ft.BoxShadow(blur_radius=15,
                                 color=ft.Colors.with_opacity(0.15, ft.Colors.BLACK),
                                 offset=ft.Offset(0, 5))

#==================================================#
#======================BORDER======================#
#==================================================#
default_border_color = ft.Colors.with_opacity(0.1, ft.Colors.WHITE)

#==================================================#
#======================BUTTON======================#
#==================================================#
add_data_btn_style = ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5),
                                    color=ft.Colors.GREEN_600,
                                    text_style=ft.TextStyle(size=20,font_family="Comic"))
assign_employee_btn_style = ft.ButtonStyle(icon_size=30,
                                           shape=ft.RoundedRectangleBorder(radius=10),
                                           color=ft.Colors.ORANGE_ACCENT_400,
                                           text_style=ft.TextStyle(size=20, font_family="Comic"))
save_change_btn_style = ft.ButtonStyle(icon_size=30,
                                shape=ft.RoundedRectangleBorder(radius=10),
                                color=ft.Colors.GREEN_600,
                                text_style=ft.TextStyle(size=20, font_family="Comic"))