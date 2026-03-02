# Imports
import flet as ft

# Flet app structure and setup
def main(page: ft.page): # we create a main function which includes the whole app?
    page.title = "Temperature converter"
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 200
    page.window_height = 600
    page.window_resizable = True
    page.padding = 20

    # input field for celsius, f, k
    celsius_input = ft.TextField(
        label="Celcius",
        hint_text="Enter temperature in Celsius",
        keyboard_type=ft.KeyboardType.NUMBER,
        color=ft.Colors.WHITE,
        border_color=ft.Colors.WHITE,
        on_change= lambda e: celsius(e.control.value)
    )

    fahrenheit_input = ft.TextField(
        label="Fahrenheit",
        hint_text="Enter temperature in Fahrenheit",
        keyboard_type=ft.KeyboardType.NUMBER,
        color=ft.Colors.WHITE,
        border_color=ft.Colors.WHITE,
        on_change = lambda e: fahrenheit(e.control.value)
    )

    kelvin_input = ft.TextField(
        label="Kelvin",
        hint_text="Enter temperature in Kelvin",
        keyboard_type=ft.KeyboardType.NUMBER,
        color=ft.Colors.WHITE,
        border_color=ft.Colors.WHITE,
        on_change= lambda e: kelvin(e.control.value)
    )

    # add functionality to the app
    def celsius(celsius_input):
        try:
            if celsius_input and celsius_input.strip():
                c = float(celsius_input)
                f = c * 9 / 5 + 32
                k = c + 273.15
                fahrenheit_input.value = f"{f:.2f}"
                kelvin_input.value = f"{k:.2f}"
                page.update()
        except ValueError:
            celsius_input.value = f"Error"


    def fahrenheit(fahrenheit_input):
        if fahrenheit_input and fahrenheit_input.strip():
            f = float(fahrenheit_input)
            c = (f - 32) * 5 / 9
            k = c + 273.15
            celsius_input.value = f"{c:.2f}"
            kelvin_input.value = f"{k:.2f}"
            page.update()


    def kelvin(kelvin_input):
        if kelvin_input and kelvin_input.strip():
            k = float(kelvin_input)
            c = k - 273.15
            f = c * 9 / 5 + 32
            celsius_input.value = f"{c:.2f}"
            fahrenheit_input.value = f"{f:.2f}"
            page.update()

    def clear_all(e):
        celsius_input.value = ""
        fahrenheit_input.value = ""
        kelvin_input.value = ""
        page.update()

    # Create the main UI of the app -> containers
    page.add(
        ft.Column([
            ft.Text(
                "Tempature converter",
                size=28,
                weight=ft.FontWeight.BOLD,
                text_align=ft.TextAlign.CENTER,
                color=ft.Colors.PINK
            ),
            ft.Divider(height=20),

            celsius_input,
            ft.Divider(height=10),
            fahrenheit_input,
            ft.Divider(height=10),
            kelvin_input,
            ft.Divider(height=20),

            ft.Button(
                "Clear All",
                on_click=clear_all,
                icon=ft.Icons.CLEAR,
                style=ft.ButtonStyle(
                    bgcolor=ft.Colors.RED_400,
                    color=ft.Colors.WHITE
                )
            ),

            ft.Divider(height=20),

            ft.Container(
                content=ft.Column([
                    ft.Text("Conversion Formulas:", weight=ft.FontWeight.BOLD),
                    ft.Text(" - Celsius to Fahrenheit: F = (C * 9/5 + 32)"),
                    ft.Text(" - Fahrenheit to Celsius: C = (F - 32) * 5/9"),
                    ft.Text(" - Celsius to Kelvin: K = C + 273.15")
                ], spacing=5),
                padding=ft.padding.all(15),
                bgcolor=ft.Colors.GREY_700,
                border_radius=10
            ) # div
        ],
            scroll=ft.ScrollMode.AUTO,
            spacing=0
        )
    )

# Run a flet app
if __name__ == "__main__":
    ft.app(target=main)