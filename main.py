import flet as ft


def main(page: ft.Page):
    page.title = "Calculadora Financiera"
    page.padding = 20

    input_p_compra = ft.TextField(
        label="Precio de compra", keyboard_type=ft.KeyboardType.NUMBER
    )
    input_pct_buscado = ft.TextField(
        label="% buscado (ej: 10)", keyboard_type=ft.KeyboardType.NUMBER
    )
    res_op1 = ft.Text(value="", weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN)

    def calcular_op1(e):
        try:
            pc = float(input_p_compra.value or "")
            pct = float(input_pct_buscado.value or "")
            pv = pc * (1 + pct / 100)
            res_op1.value = f"Precio de venta: ${pv:.2f}"
        except ValueError:
            res_op1.value = "Error: Introduce números válidos"
        page.update()

    input_p_compra_ef = ft.TextField(
        label="Precio de compra efectuado", keyboard_type=ft.KeyboardType.NUMBER
    )
    input_p_venta_ef = ft.TextField(
        label="Precio de venta efectuado", keyboard_type=ft.KeyboardType.NUMBER
    )
    res_op2 = ft.Text(value="", weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN)

    def calcular_op2(e):
        try:
            compra = float(input_p_compra_ef.value or "")
            venta = float(input_p_venta_ef.value or "")
            if compra <= 0:
                res_op2.value = "Error: La compra debe ser mayor a 0"
            else:
                ganancia = venta - compra
                pct = (ganancia / compra) * 100
                res_op2.value = (
                    f"Ganancia: ${ganancia:.2f} | % Ganancia: {pct:.2f}%"
                )
        except ValueError:
            res_op2.value = "Error: Introduce números válidos"
        page.update()

    input_p_min = ft.TextField(
        label="Precio mínimo", keyboard_type=ft.KeyboardType.NUMBER
    )
    input_p_max = ft.TextField(
        label="Precio máximo", keyboard_type=ft.KeyboardType.NUMBER
    )
    res_op3 = ft.Text(value="", weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN)

    def calcular_op3(e):
        try:
            p_min = float(input_p_min.value or "")
            p_max = float(input_p_max.value or "")
            if p_min <= 0:
                res_op3.value = "Error: El mínimo debe ser mayor a 0"
            else:
                dif = p_max - p_min
                pct_dif = (dif / p_min) * 100
                res_op3.value = (
                    f"Diferencia: ${dif:.2f} | Diferencia %: {pct_dif:.2f}%"
                )
        except ValueError:
            res_op3.value = "Error: Introduce números válidos"
        page.update()

    def formulario(*controls):
        return ft.Column(
            expand=True,
            scroll=ft.ScrollMode.AUTO,
            spacing=15,
            controls=list(controls),
        )

    tabs = ft.Tabs(
        selected_index=0,
        length=3,
        expand=True,
        content=ft.Column(
            expand=True,
            controls=[
                ft.TabBar(
                    tabs=[
                        ft.Tab(label="1. Venta"),
                        ft.Tab(label="2. Ganancia"),
                        ft.Tab(label="3. Rango %"),
                    ]
                ),
                ft.TabBarView(
                    expand=True,
                    controls=[
                        formulario(
                            input_p_compra,
                            input_pct_buscado,
                            ft.Button(
                                content="Calcular Precio de Venta",
                                on_click=calcular_op1,
                            ),
                            res_op1,
                        ),
                        formulario(
                            input_p_compra_ef,
                            input_p_venta_ef,
                            ft.Button(
                                content="Calcular Ganancia", on_click=calcular_op2
                            ),
                            res_op2,
                        ),
                        formulario(
                            input_p_min,
                            input_p_max,
                            ft.Button(
                                content="Calcular Diferencia %",
                                on_click=calcular_op3,
                            ),
                            res_op3,
                        ),
                    ],
                ),
            ],
        ),
    )

    page.add(
        ft.Text("Calculadora Financiera", size=24, weight=ft.FontWeight.BOLD),
        tabs,
    )


ft.run(main)
