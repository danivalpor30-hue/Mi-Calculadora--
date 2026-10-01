# -------------------------------------------------------------------------
# Inicialización blindada para Android móvil y Web
# -------------------------------------------------------------------------
def iniciar_app():
  # Intento 1: motor móvil nativo flet_runtime
  try:
    import flet_runtime.app as fra

    if hasattr(fra, "app") and callable(fra.app):
      fra.app(target=main)
      return
    elif callable(fra):
      fra(target=main)
      return
  except Exception:
    pass

  # Intento 2: ejecución flet estándar
  try:
    import flet as ft

    if hasattr(ft, "app") and callable(ft.app):
      ft.app(target=main)
      return
    elif hasattr(ft, "run") and callable(ft.run):
      ft.run(main)
      return
  except Exception:
    pass


if __name__ == "__main__":
  iniciar_app()
else:
  iniciar_app()
