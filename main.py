import flet as ft


# Función auxiliar para compatibilidad de botones en Flet 1.0 y versiones previas
def crear_boton(texto, accion):
    try:
        return ft.Button(content=texto, on_click=accion)
    except Exception:
        try:
            return ft.Button(content=ft.Text(texto), on_click=accion)
        except Exception:
            try:
                return ft.ElevatedButton(text=texto, on_click=accion)
            except Exception:
                return ft.FilledButton(texto, on_click=accion)


def main(page: ft.Page):
    page.title = "Calculadora Financiera"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 20
    page.scroll = ft.ScrollMode.AUTO

    # ==========================================
    # PESTAÑA 1: CALCULAR PRECIO DE VENTA
    # ==========================================
    p1_compra = ft.TextField(label="Precio de compra ($)", keyboard_type=ft.KeyboardType.NUMBER)
    p1_pct = ft.TextField(label="% Ganancia buscada (ej: 10)", keyboard_type=ft.KeyboardType.NUMBER)
    p1_resultado = ft.Text(value="", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_400)

    def calcular_tab1(e):
        try:
            pc = float(p1_compra.value)
            pct = float(p1_pct.value)
            pv = pc * (1 + (pct / 100))
            p1_resultado.value = f"Precio de venta objetivo: ${pv:.2f}"
        except ValueError:
            p1_resultado.value = "Ingresa números válidos"
        page.update()

    btn_tab1 = crear_boton("Calcular Venta", calcular_tab1)

    tab1_content = ft.Column([
        ft.Text("Objetivo de Venta", size=20, weight=ft.FontWeight.BOLD),
        p1_compra,
        p1_pct,
        btn_tab1,
        p1_resultado
    ], spacing=15)

    # ==========================================
    # PESTAÑA 2: GANANCIA REAL + CONTRATOS
    # ==========================================
    p2_compra = ft.TextField(label="Precio de compra ($)", keyboard_type=ft.KeyboardType.NUMBER)
    p2_venta = ft.TextField(label="Precio de venta ($)", keyboard_type=ft.KeyboardType.NUMBER)
    p2_contratos = ft.TextField(label="Cantidad de contratos", value="1", keyboard_type=ft.KeyboardType.NUMBER)
    
    p2_res_diferencia = ft.Text(value="", size=16, weight=ft.FontWeight.W_500)
    p2_res_pct = ft.Text(value="", size=16, weight=ft.FontWeight.W_500)
    p2_res_total = ft.Text(value="", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_400)

    def calcular_tab2(e):
        try:
            pc = float(p2_compra.value)
            pv = float(p2_venta.value)
            contratos = float(p2_contratos.value)

            diff = pv - pc
            pct = (diff / pc) * 100 if pc != 0 else 0
            # 100 acciones por cada contrato de opciones
            ganancia_total = diff * 100 * contratos

            color_resultado = ft.Colors.GREEN_400 if diff >= 0 else ft.Colors.RED_400

            p2_res_diferencia.value = f"Diferencia por acción: ${diff:.2f}"
            p2_res_pct.value = f"Rendimiento: {pct:.2f}%"
            p2_res_total.value = f"Ganancia Total: ${ganancia_total:.2f}"
            p2_res_total.color = color_resultado

        except ValueError:
            p2_res_total.value = "Ingresa números válidos"
            p2_res_total.color = ft.Colors.RED_400
        page.update()

    btn_tab2 = crear_boton("Calcular Ganancia", calcular_tab2)

    tab2_content = ft.Column([
        ft.Text("Cálculo de Ganancia (Opciones)", size=20, weight=ft.FontWeight.BOLD),
        p2_compra,
        p2_venta,
        p2_contratos,
        btn_tab2,
        p2_res_diferencia,
        p2_res_pct,
        p2_res_total
    ], spacing=12)

    # ==========================================
    # PESTAÑA 3: RANGO %
    # ==========================================
    p3_min = ft.TextField(label="Precio mínimo / inicial", keyboard_type=ft.KeyboardType.NUMBER)
    p3_max = ft.TextField(label="Precio máximo / final", keyboard_type=ft.KeyboardType.NUMBER)
    p3_resultado = ft.Text(value="", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_400)

    def calcular_tab3(e):
        try:
            p_min = float(p3_min.value)
            p_max = float(p3_max.value)
            diferencia = p_max - p_min
            var_pct = (diferencia / p_min) * 100 if p_min != 0 else 0
            p3_resultado.value = f"Diferencia: ${diferencia:.2f} | Variación: {var_pct:.2f}%"
        except ValueError:
            p3_resultado.value = "Ingresa números válidos"
        page.update()

    btn_tab3 = crear_boton("Calcular Rango", calcular_tab3)

    tab3_content = ft.Column([
        ft.Text("Diferencia de Rango %", size=20, weight=ft.FontWeight.BOLD),
        p3_min,
        p3_max,
        btn_tab3,
        p3_resultado
    ], spacing=15)

    # ==========================================
    # CONTENEDORES DE CADA PESTAÑA
    # ==========================================
    vista_venta = ft.Container(content=tab1_content, visible=False)
    vista_ganancia = ft.Container(content=tab2_content, visible=True)  # Vista inicial activa
    vista_rango = ft.Container(content=tab3_content, visible=False)

    # ==========================================
    # SELECTOR DE NAVEGACIÓN SUPERIOR
    # ==========================================
    def cambiar_pestana(indice):
        vista_venta.visible = (indice == 0)
        vista_ganancia.visible = (indice == 1)
        vista_rango.visible = (indice == 2)

        for i, boton in enumerate(botones_pestanas):
            if i == indice:
                boton.bgcolor = ft.Colors.BLUE_600
                boton.border = ft.border.all(1, ft.Colors.BLUE_300)
            else:
                boton.bgcolor = ft.Colors.GREY_800
                boton.border = ft.border.all(1, ft.Colors.TRANSPARENT)
        page.update()

    def crear_pestana_boton(indice, titulo, icono, activa=False):
        return ft.Container(
            content=ft.Row(
                [
                    ft.Icon(icono, size=16, color=ft.Colors.WHITE),
                    ft.Text(titulo, size=13, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=5,
            ),
            bgcolor=ft.Colors.BLUE_600 if activa else ft.Colors.GREY_800,
            border=ft.border.all(1, ft.Colors.BLUE_300 if activa else ft.Colors.TRANSPARENT),
            border_radius=8,
            padding=ft.padding.symmetric(vertical=10, horizontal=6),
            expand=True,
            alignment=ft.Alignment(0, 0),
            on_click=lambda e, idx=indice: cambiar_pestana(idx),
        )

    botones_pestanas = [
        crear_pestana_boton(0, "Venta", ft.Icons.ATTACH_MONEY, activa=False),
        crear_pestana_boton(1, "Ganancia", ft.Icons.TRENDING_UP, activa=True),
        crear_pestana_boton(2, "Rango %", ft.Icons.PERCENT, activa=False),
    ]

    barra_pestanas = ft.Container(
        content=ft.Row(botones_pestanas, spacing=8),
        margin=ft.margin.only(bottom=15),
    )

    page.add(
        barra_pestanas,
        vista_venta,
        vista_ganancia,
        vista_rango,
    )


# ==========================================
# INICIO OFICIAL
# ==========================================
if hasattr(ft, "run"):
    ft.run(main)
elif hasattr(ft, "app"):
    ft.app(target=main)
