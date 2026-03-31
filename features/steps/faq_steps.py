from behave import given, when, then
from pages.navegacion_page import NavegacionPage
from pages.faq_page import FaqPage
from locators.faq_locators import FaqLocators


@given('el usuario navega a la sección "Preguntas Frecuentes"')
def step_ir_faq(context):
    if not hasattr(context, "nav_page"):
        context.nav_page = NavegacionPage(context.driver)
    context.nav_page.navegar_a_seccion("Preguntas Frecuentes")
    context.faq_page = FaqPage(context.driver)


@given('que el usuario expandió la primera pregunta del acordeón')
def step_expandir_primera_pregunta(context):
    if not hasattr(context, "faq_page"):
        context.faq_page = FaqPage(context.driver)
    context.faq_page.hacer_clic_item(1)


@when('el usuario hace clic en la primera pregunta del acordeón')
def step_clic_primera_pregunta(context):
    context.faq_page.hacer_clic_item(1)


@when('el usuario hace clic en la segunda pregunta del acordeón')
def step_clic_segunda_pregunta(context):
    context.faq_page.hacer_clic_item(2)


@when('el usuario hace clic en la pregunta número {numero:d}')
def step_clic_pregunta_numero(context, numero):
    context.faq_page.hacer_clic_item(numero)
    context.ultimo_numero_faq = numero


@when('el usuario hace clic nuevamente en esa pregunta')
def step_clic_misma_pregunta(context):
    context.faq_page.hacer_clic_item(1)


@then('la sección de preguntas frecuentes debe estar visible')
def step_faq_visible(context):
    context.faq_page = FaqPage(context.driver)
    assert context.faq_page.seccion_es_visible()


@then('debe mostrar al menos una pregunta en el acordeón')
def step_al_menos_una_pregunta(context):
    total = context.faq_page.contar_items()
    assert total >= 1, f"Se esperaba al menos 1 pregunta, hay {total}"


@then('la respuesta de esa pregunta debe hacerse visible')
def step_respuesta_visible(context):
    assert context.faq_page.respuesta_es_visible(1), \
        "La respuesta de la primera pregunta no es visible"


@then('la respuesta número {numero:d} debe hacerse visible')
def step_respuesta_numero_visible(context, numero):
    assert context.faq_page.respuesta_es_visible(numero), \
        f"La respuesta {numero} no es visible"


@then('el ícono del acordeón debe cambiar de estado')
def step_icono_cambia(context):
    texto_toggle = context.faq_page.obtener_texto_toggle(1)
    assert texto_toggle != "+", \
        f"El ícono sigue siendo '+', debería haber cambiado al expandirse"


@then('la respuesta debe ocultarse')
def step_respuesta_oculta(context):
    assert context.faq_page.respuesta_esta_oculta(1), \
        "La respuesta sigue visible tras hacer clic nuevamente"


@then('el ícono del acordeón debe regresar a su estado inicial')
def step_icono_regresa(context):
    texto_toggle = context.faq_page.obtener_texto_toggle(1)
    assert texto_toggle == "+", \
        f"El ícono no regresó a '+', valor actual: '{texto_toggle}'"


@then('la respuesta de la segunda pregunta debe hacerse visible')
def step_segunda_respuesta_visible(context):
    assert context.faq_page.respuesta_es_visible(2), \
        "La respuesta de la segunda pregunta no es visible"


@then('la respuesta de la primera pregunta debe ocultarse')
def step_primera_respuesta_oculta(context):
    assert context.faq_page.respuesta_esta_oculta(1), \
        "La primera respuesta sigue abierta (el acordeón debería cerrarla)"


@then('el texto de la respuesta no debe desbordarse del contenedor')
def step_sin_desbordamiento(context):
    assert context.faq_page.respuesta_no_desborda_contenedor(1), \
        "El texto de la respuesta se desborda del contenedor en vista móvil"
