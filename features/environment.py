import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


BASE_URL = os.environ.get("BASE_URL", "https://tecfix.co")


def before_all(context):
    context.base_url = BASE_URL


def before_scenario(context, scenario):
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1280,800")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    context.driver = webdriver.Chrome(options=options)


def after_scenario(context, scenario):
    if hasattr(context, "driver") and context.driver:
        if scenario.status == "failed":
            _capturar_pantalla(context, scenario.name)
        context.driver.quit()


def _capturar_pantalla(context, nombre_escenario):
    carpeta = "reports/screenshots"
    os.makedirs(carpeta, exist_ok=True)
    nombre_archivo = nombre_escenario.replace(" ", "_").replace("/", "-")[:80]
    ruta = os.path.join(carpeta, f"{nombre_archivo}.png")
    context.driver.save_screenshot(ruta)
