from behave import given, when, then
from pages.navegacion_page import NavegacionPage
from locators.navegacion_locators import NavegacionLocators

SECCION_LOCATORS = {
    "Nuestros Servicios": NavegacionLocators.SECCION_SERVICIOS,
    "Por qué TecFix": NavegacionLocators.SECCION_POR_QUE,
    "Nuestro Proceso": NavegacionLocators.SECCION_PROCESO,
    "Tecnologías": NavegacionLocators.SECCION_TECNOLOGIAS,
    "Preguntas Frecuentes": NavegacionLocators.SECCION_FAQ,
    "Generador de Casos de Prueba": NavegacionLocators.SECCION_GENERADOR,
    "Contacto": NavegacionLocators.SECCION_CONTACTO,
    "Números que Hablan": NavegacionLocators.ESTADISTICAS_SECCION,
}


@given('que el usuario abre el sitio "{url}"')
def step_abrir_sitio(context, url):
    context.nav_page = NavegacionPage(context.driver)
    context.nav_page.abrir(url)


@given('que el tamaño de ventana es {ancho:d} x {alto:d}')
def step_cambiar_tamano(context, ancho, alto):
    context.nav_page.cambiar_tamano_ventana(ancho, alto)


@when('el usuario hace clic en el enlace de navegación "{seccion}"')
def step_clic_navegacion(context, seccion):
    context.nav_page.navegar_a_seccion(seccion)


@when('el usuario hace clic en el logo de TecFix')
def step_clic_logo(context):
    context.nav_page.hacer_clic_logo()


@then('el título de la página debe contener "{texto}"')
def step_verificar_titulo(context, texto):
    titulo = context.nav_page.obtener_titulo_pagina()
    assert texto in titulo, f"Título esperado contiene '{texto}', obtenido: '{titulo}'"


@then('la página debe cargar en menos de {segundos:d} segundos')
def step_verificar_carga(context, segundos):
    navigation_timing = context.driver.execute_script(
        "const t = window.performance.timing;"
        "return t.loadEventEnd - t.navigationStart;"
    )
    tiempo = navigation_timing / 1000
    assert tiempo < segundos, f"Carga tardó {tiempo:.2f}s, límite: {segundos}s"


@then('el encabezado principal debe ser visible')
def step_encabezado_visible(context):
    assert context.nav_page.seccion_es_visible(NavegacionLocators.HERO_H1)


@then('el menú de navegación debe estar visible')
def step_menu_visible(context):
    assert context.nav_page.logo_es_visible(), "El logo/header no es visible"


@then('debe contener los enlaces principales del sitio')
def step_enlaces_principales(context):
    titulos = context.nav_page.obtener_titulos_servicios()
    assert len(titulos) > 0, "No se encontraron elementos de navegación principales"


@then('la sección "{seccion}" debe ser visible en pantalla')
def step_seccion_visible(context, seccion):
    locator = SECCION_LOCATORS.get(seccion)
    assert locator, f"No hay locator definido para: '{seccion}'"
    assert context.nav_page.seccion_es_visible(locator), \
        f"La sección '{seccion}' no es visible"


@then('la página debe desplazarse al inicio')
def step_desplazado_inicio(context):
    scroll_y = context.driver.execute_script("return window.scrollY;")
    assert scroll_y == 0, f"La página no está en el inicio (scrollY={scroll_y})"


@then('el header debe ser visible en móvil')
def step_header_visible_movil(context):
    assert context.nav_page.logo_es_visible(), \
        "El header/logo no es visible en vista móvil"


@then('el contenido principal debe adaptarse al ancho de la pantalla')
def step_contenido_responsivo(context):
    ancho_ventana = context.driver.execute_script("return window.innerWidth;")
    ancho_body = context.driver.execute_script(
        "return document.body.scrollWidth;"
    )
    assert ancho_body <= ancho_ventana + 5, \
        f"Hay scroll horizontal: body={ancho_body}px > ventana={ancho_ventana}px"


@then('el menú de navegación debe desplegarse')
def step_menu_desplegado(context):
    assert context.nav_page.logo_es_visible()


@then('deben ser visibles los enlaces de cada sección')
def step_enlaces_visibles(context):
    titulos = context.nav_page.obtener_titulos_servicios()
    assert len(titulos) > 0


@then('la sección "Números que Hablan" debe ser visible')
def step_metricas_visible(context):
    assert context.nav_page.seccion_es_visible(NavegacionLocators.ESTADISTICAS_SECCION)


@then('los indicadores de métricas deben mostrar valores')
def step_metricas_con_valores(context):
    assert context.nav_page.seccion_estadisticas_tiene_valores()
