import flet as ft


def main(page: ft.Page):
  page.title = "Calculadora Financiera"
  page.theme_mode = ft.ThemeMode.DARK
  page.padding = 20

  # -------------------------------------------------------------------------
  # 1. PESTAÑA: Capital Inicial (% de cuenta)
  # -------------------------------------------------------------------------
  cap_balance = ft.TextField(
      label="Balance actual ($)", keyboard_type=ft.KeyboardType.NUMBER
  )
  cap_pct = ft.TextField(
      label="% a invertir (ej: 30)", keyboard_type=ft.KeyboardType.NUMBER
  )
  res_cap = ft.Text(value="", weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN)

  def calc_cap(e):
    try:
      balance = float(cap_balance.value)
      pct = float(cap_pct.value)
      capital = balance * (pct / 100)
      remanente = balance - capital
      res_cap.value = (
          f"Capital inicial: ${capital:.2f}\nBalance restante: ${remanente:.2f}"
      )
    except ValueError:
      res_cap.value = "Error: Introduce números válidos"
    page.update()

  btn_cap = ft.ElevatedButton(text="Calcular Capital", on_click=calc_cap)
  tab_capital = ft.Tab(
      text="1. Capital",
      content=ft.Column(
          [cap_balance, cap_pct, btn_cap, res_cap],
          spacing=12,
          scroll=ft.ScrollMode.AUTO,
      ),
  )

  # -------------------------------------------------------------------------
  # 2. PESTAÑA: Rango de Precio
  # -------------------------------------------------------------------------
  rng_min = ft.TextField(
      label="Precio mínimo", keyboard_type=ft.KeyboardType.NUMBER
  )
  rng_max = ft.TextField(
      label="Precio máximo", keyboard_type=ft.KeyboardType.NUMBER
  )
  res_rng = ft.Text(value="", weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN)

  def calc_rng(e):
    try:
      mn = float(rng_min.value)
      mx = float(rng_max.value)
      diff = mx - mn
      pct = (diff / mn) * 100 if mn != 0 else 0
      res_rng.value = f"Diferencia: ${diff:.2f} ({pct:.2f}%)"
    except ValueError:
      res_rng.value = "Error: Introduce números válidos"
    page.update()

  btn_rng = ft.ElevatedButton(text="Calcular Rango", on_click=calc_rng)
  tab_rango = ft.Tab(
      text="2. Rango",
      content=ft.Column(
          [rng_min, rng_max, btn_rng, res_rng],
          spacing=12,
          scroll=ft.ScrollMode.AUTO,
      ),
  )

  # -------------------------------------------------------------------------
  # 3. PESTAÑA: Precio de Venta y Stop Loss
  # -------------------------------------------------------------------------
  vnt_compra = ft.TextField(
      label="Precio de compra", keyboard_type=ft.KeyboardType.NUMBER
  )
  vnt_pct = ft.TextField(
      label="% buscado (ej: 10)", keyboard_type=ft.KeyboardType.NUMBER
  )
  vnt_tarifa = ft.TextField(
      label="Tarifa broker total ($)",
      value="2",
      keyboard_type=ft.KeyboardType.NUMBER,
  )
  res_vnt = ft.Text(value="", weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN)

  def calc_vnt(e):
    try:
      pc = float(vnt_compra.value)
      pct = float(vnt_pct.value)
      tarifa = float(vnt_tarifa.value)
      pv = (pc * (1 + (pct / 100))) + (tarifa / 100)
      res_vnt.value = f"Precio de venta sugerido: ${pv:.2f}"
    except ValueError:
      res_vnt.value = "Error: Introduce números válidos"
    page.update()

  btn_vnt = ft.ElevatedButton(text="Calcular Venta", on_click=calc_vnt)

  sl_capital = ft.TextField(
      label="Capital invertido ($)", keyboard_type=ft.KeyboardType.NUMBER
  )
  sl_pct = ft.TextField(
      label="Stop loss (% desfavorable, ej: 20)",
      keyboard_type=ft.KeyboardType.NUMBER,
  )
  res_sl = ft.Text(value="", weight=ft.FontWeight.BOLD, color=ft.Colors.RED_400)

  def calc_sl(e):
    try:
      cap = float(sl_capital.value)
      pct = float(sl_pct.value)
      perdida = cap * (pct / 100)
      remanente = cap - perdida
      res_sl.value = (
          f"Salir a partir de: -${perdida:.2f} de pérdida\nCapital restante:"
          f" ${remanente:.2f}"
      )
    except ValueError:
      res_sl.value = "Error: Introduce números válidos"
    page.update()

  btn_sl = ft.ElevatedButton(
      text="Calcular Stop Loss",
      on_click=calc_sl,
      color=ft.Colors.WHITE,
      bgcolor=ft.Colors.RED_700,
  )

  tab_venta_sl = ft.Tab(
      text="3. Venta / SL",
      content=ft.Column(
          [
              vnt_compra,
              vnt_pct,
              vnt_tarifa,
              btn_vnt,
              res_vnt,
              ft.Divider(height=25, color=ft.Colors.GREY_700),
              ft.Text(
                  "Gestión de Riesgo (Stop Loss)",
                  weight=ft.FontWeight.BOLD,
                  size=16,
              ),
              sl_capital,
              sl_pct,
              btn_sl,
              res_sl,
          ],
          spacing=12,
          scroll=ft.ScrollMode.AUTO,
      ),
  )

  # -------------------------------------------------------------------------
  # 4. PESTAÑA: Ganancia Real
  # -------------------------------------------------------------------------
  gan_compra = ft.TextField(
      label="Precio de compra real", keyboard_type=ft.KeyboardType.NUMBER
  )
  gan_venta = ft.TextField(
      label="Precio de venta real", keyboard_type=ft.KeyboardType.NUMBER
  )
  res_gan = ft.Text(value="", weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN)

  def calc_gan(e):
    try:
      pc = float(gan_compra.value)
      pv = float(gan_venta.value)
      diff = pv - pc
      pct = (diff / pc) * 100 if pc != 0 else 0
      res_gan.value = f"Ganancia: ${diff:.2f} ({pct:.2f}%)"
    except ValueError:
      res_gan.value = "Error: Introduce números válidos"
    page.update()

  btn_gan = ft.ElevatedButton(text="Calcular Ganancia", on_click=calc_gan)
  tab_ganancia = ft.Tab(
      text="4. Ganancia",
      content=ft.Column(
          [gan_compra, gan_venta, btn_gan, res_gan],
          spacing=12,
          scroll=ft.ScrollMode.AUTO,
      ),
  )

  # Renderizado de pestañas
  tabs_control = ft.Tabs(
      selected_index=0,
      tabs=[tab_capital, tab_rango, tab_venta_sl, tab_ganancia],
  )
  page.add(tabs_control)


# -------------------------------------------------------------------------
# Arranque: usa el runtime nativo en Android y el estándar en Web
# -------------------------------------------------------------------------
try:
  from flet_runtime.app import app as run_app

  run_app(target=main)
except Exception:
  ft.app(target=main)
