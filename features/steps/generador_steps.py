from behave import given, when, then
from pages.navegacion_page import NavegacionPage
from pages.generador_page import GeneradorPage
from locators.generador_locators import GeneradorLocators

TIPOS_PRUEBA = {
    "Unit Test": "Prueba Unitaria",
    "Integration Test": "Prueba de Integración",
    "E2E Test": "Prueba E2E",
    "API Test": "Prueba de API",
    "Validation Test": "Prueba de Validación",
    "User Flow Test": "Prueba de Flujo de Usuario",
}

TECNOLOGIAS = {
    "JavaScript/Node.js": "JavaScript / Node.js",
    "Python": "Python",
    "Java": "Java",
    "C#": "C#",
    "React": "React",
    "Angular": "Angular",
    "Selenium": "Selenium",
    "Cypress": "Cypress",
    "SQL": "SQL",
    "Other": "Otro",
}


@given('el usuario navega a la sección "Generador de Casos de Prueba"')
def step_ir_generador(context):
    context.nav_page = NavegacionPage(context.driver)
    context.nav_page.navegar_a_seccion("Generador de Casos de Prueba")
    context.gen_page = GeneradorPage(context.driver)


@given('que el usuario ya generó casos de prueba anteriormente')
def step_generar_previo(context):
    context.nav_page = NavegacionPage(context.driver)
    context.nav_page.navegar_a_seccion("Generador de Casos de Prueba")
    context.gen_page = GeneradorPage(context.driver)
    context.gen_page.seleccionar_tipo_prueba("Prueba Unitaria")
    context.gen_page.seleccionar_tecnologia("Python")
    context.gen_page.ingresar_descripcion("Prueba previa para setup del escenario")
    context.gen_page.hacer_clic_generar()
    context.gen_page.esperar_resultados()


@then('el formulario del generador debe estar visible')
def step_formulario_visible(context):
    if not hasattr(context, "gen_page"):
        context.gen_page = GeneradorPage(context.driver)
    assert context.gen_page.formulario_es_visible()


@then('el campo "{nombre}" debe estar presente')
def step_campo_presente(context, nombre):
    locators = {
        "Tipo de Prueba": GeneradorLocators.SELECT_TIPO_PRUEBA,
        "Tecnología/Framework": GeneradorLocators.SELECT_TECNOLOGIA,
        "Descripción de la Prueba": GeneradorLocators.TEXTAREA_DESCRIPCION,
        "Contexto Adicional": GeneradorLocators.TEXTAREA_CONTEXTO,
    }
    locator = locators.get(nombre)
    assert locator, f"No hay locator para el campo: '{nombre}'"
    assert context.gen_page.campo_es_visible(locator), \
        f"El campo '{nombre}' no está visible"


@then('el botón "{nombre}" debe estar presente')
def step_boton_presente(context, nombre):
    locators = {
        "Generar Casos de Prueba": GeneradorLocators.BTN_GENERAR,
        "Copiar": GeneradorLocators.BTN_COPIAR,
        "Nuevos": GeneradorLocators.BTN_NUEVOS,
    }
    locator = locators.get(nombre)
    assert locator, f"No hay locator para el botón: '{nombre}'"
    assert context.gen_page.campo_es_visible(locator), \
        f"El botón '{nombre}' no está visible"


@when('el usuario selecciona el tipo de prueba "{tipo}"')
def step_seleccionar_tipo(context, tipo):
    texto_visible = TIPOS_PRUEBA.get(tipo, tipo)
    context.gen_page.seleccionar_tipo_prueba(texto_visible)


@when('el usuario selecciona la tecnología "{tecnologia}"')
def step_seleccionar_tecnologia(context, tecnologia):
    texto_visible = TECNOLOGIAS.get(tecnologia, tecnologia)
    context.gen_page.seleccionar_tecnologia(texto_visible)


@when('el usuario ingresa la descripción "{descripcion}"')
def step_ingresar_descripcion(context, descripcion):
    context.gen_page.ingresar_descripcion(descripcion)


@when('el usuario ingresa el contexto adicional "{contexto}"')
def step_ingresar_contexto(context, contexto):
    context.gen_page.ingresar_contexto(contexto)


@when('el usuario deja vacío el campo "Descripción de la Prueba"')
def step_dejar_descripcion_vacia(context):
    context.gen_page.ingresar_descripcion("")


@when('el usuario hace clic en el botón "Generar Casos de Prueba"')
def step_clic_generar(context):
    context.gen_page.hacer_clic_generar()


@when('el usuario hace clic en el botón "Copiar"')
def step_clic_copiar(context):
    context.gen_page.hacer_clic_copiar()


@when('el usuario hace clic en el botón "Nuevos"')
def step_clic_nuevos(context):
    context.gen_page.hacer_clic_nuevos()


@then('el área de resultados debe mostrar casos de prueba generados')
def step_resultados_visibles(context):
    context.gen_page.esperar_resultados()
    assert context.gen_page.resultados_son_visibles(), \
        "El área de resultados no está visible tras la generación"
    texto = context.gen_page.obtener_texto_resultado()
    assert len(texto.strip()) > 0, "El resultado generado está vacío"


@then('el área de resultados muestra casos de prueba generados')
def step_resultados_ya_visibles(context):
    assert context.gen_page.resultados_son_visibles()


@then('el botón "Copiar" debe estar habilitado')
def step_boton_copiar_habilitado(context):
    assert context.gen_page.boton_copiar_es_visible()


@then('el botón "Nuevos" debe estar habilitado')
def step_boton_nuevos_habilitado(context):
    assert context.gen_page.boton_nuevos_es_visible()


@then('el contenido del resultado debe estar en el portapapeles')
def step_verificar_portapapeles(context):
    texto_resultado = context.gen_page.obtener_texto_resultado_raw()
    assert len(texto_resultado.strip()) > 0, \
        "No hay contenido en el resultado para copiar"


@then('el área de resultados debe estar vacía o mostrar el estado inicial')
def step_resultados_limpios(context):
    assert context.gen_page.resultados_estan_ocultos(), \
        "El área de resultados sigue visible tras hacer clic en Nuevos"


@then('el formulario debe estar listo para una nueva generación')
def step_formulario_listo(context):
    assert context.gen_page.formulario_es_visible()


@then('debe aparecer un mensaje de validación en el campo de descripción')
def step_validacion_descripcion(context):
    assert context.gen_page.descripcion_tiene_validacion_html5(), \
        "No se detectó validación HTML5 en el campo de descripción vacío"


@then('el sistema debe manejar la solicitud sin errores fatales')
def step_sin_errores_fatales(context):
    context.gen_page.esperar_resultados()
    logs = context.driver.get_log("browser")
    errores_criticos = [l for l in logs if l["level"] == "SEVERE"]
    assert len(errores_criticos) == 0, \
        f"Se encontraron errores críticos en consola: {errores_criticos}"


@then('el sistema no debe ejecutar scripts en el área de resultados')
def step_sin_xss(context):
    context.gen_page.esperar_resultados()
    alertas = context.driver.execute_script("return window.__xss_triggered__ || false;")
    assert not alertas, "Posible XSS detectado: se ejecutó código en el resultado"


@then('el área de resultados debe mostrar texto plano sin ejecutar código')
def step_resultado_texto_plano(context):
    texto = context.gen_page.obtener_texto_resultado()
    assert "<script>" not in texto.lower(), \
        "El resultado contiene etiquetas script sin sanitizar"
