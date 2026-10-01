import flet as ft


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

    btn_tab1 = ft.ElevatedButton("Calcular Venta", on_click=calcular_tab1)

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
            # Cada contrato equivale a 100 acciones
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

    btn_tab2 = ft.ElevatedButton("Calcular Ganancia", on_click=calcular_tab2)

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

    btn_tab3 = ft.ElevatedButton("Calcular Rango", on_click=calcular_tab3)

    tab3_content = ft.Column([
        ft.Text("Diferencia de Rango %", size=20, weight=ft.FontWeight.BOLD),
        p3_min,
        p3_max,
        btn_tab3,
        p3_resultado
    ], spacing=15)

    # ==========================================
    # NAVEGACIÓN POR PESTAÑAS
    # ==========================================
    tabs = ft.Tabs(
        selected_index=1,
        animation_duration=300,
        tabs=[
            ft.Tab(text="Venta", icon=ft.Icons.ATTACH_MONEY, content=ft.Container(content=tab1_content, padding=10)),
            ft.Tab(text="Ganancia", icon=ft.Icons.TRENDING_UP, content=ft.Container(content=tab2_content, padding=10)),
            ft.Tab(text="Rango %", icon=ft.Icons.PERCENT, content=ft.Container(content=tab3_content, padding=10)),
        ],
        expand=1,
    )

    page.add(tabs)


# ==========================================
# ARRANQUE COMPATIBLE (MÓVIL, WEB Y DESKTOP)
# ==========================================
def iniciar_app():
    # 1. Si ft.app es directamente una función ejecutable
    if hasattr(ft, "app") and callable(ft.app):
        ft.app(target=main)
        return

    # 2. Si ft.app es un módulo y la función está adentro como ft.app.app
    if hasattr(ft, "app") and hasattr(ft.app, "app") and callable(ft.app.app):
        ft.app.app(target=main)
        return

    # 3. Intentar a través de flet_runtime
    try:
        import flet_runtime.app as fra
        if callable(fra):
            fra(target=main)
            return
        if hasattr(fra, "app") and callable(fra.app):
            fra.app(target=main)
            return
    except Exception:
        pass

    # 4. Intentar a través de flet.app
    try:
        import flet.app as fa
        if callable(fa):
            fa(target=main)
            return
        if hasattr(fa, "app") and callable(fa.app):
            fa.app(target=main)
            return
    except Exception:
        pass


iniciar_app()
