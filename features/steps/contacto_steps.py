from behave import given, when, then
from pages.navegacion_page import NavegacionPage
from pages.contacto_page import ContactoPage
from locators.contacto_locators import ContactoLocators


@given('el usuario navega a la sección "Contacto"')
def step_ir_contacto(context):
    if not hasattr(context, "nav_page"):
        context.nav_page = NavegacionPage(context.driver)
    context.nav_page.navegar_a_seccion("Contacto")
    context.contacto_page = ContactoPage(context.driver)


@given('que el usuario está en la parte superior del sitio')
def step_usuario_en_hero(context):
    context.driver.execute_script("window.scrollTo(0, 0);")
    if not hasattr(context, "contacto_page"):
        context.contacto_page = ContactoPage(context.driver)


@when('el usuario hace clic en el botón de contacto por WhatsApp')
def step_clic_whatsapp(context):
    href = context.contacto_page.obtener_href_whatsapp()
    context.whatsapp_href = href


@when('el usuario hace clic en el widget de chat')
def step_clic_chat_widget(context):
    context.driver.find_element(*ContactoLocators.CHAT_BTN_FLOTANTE).click()


@when('el usuario escribe "{mensaje}"')
def step_escribir_chat(context, mensaje):
    context.contacto_page.escribir_en_chat(mensaje)
    context.mensaje_escrito = mensaje


@then('la sección de contacto debe estar visible')
def step_seccion_contacto_visible(context):
    context.contacto_page = ContactoPage(context.driver)
    assert context.contacto_page.seccion_es_visible()


@then('debe mostrar al menos un canal de comunicación')
def step_al_menos_un_canal(context):
    whatsapp = context.contacto_page.whatsapp_es_visible()
    email = context.contacto_page.email_es_visible()
    assert whatsapp or email, "No se encontró ningún canal de contacto visible"


@then('el enlace de WhatsApp debe contener el número "{numero}"')
def step_numero_whatsapp(context, numero):
    href = context.contacto_page.obtener_href_whatsapp()
    assert numero in href, \
        f"Número esperado '{numero}' no encontrado en href: '{href}'"


@then('el enlace debe apuntar al dominio "{dominio}"')
def step_dominio_whatsapp(context, dominio):
    href = context.contacto_page.obtener_href_whatsapp()
    assert dominio in href, \
        f"Dominio esperado '{dominio}' no encontrado en href: '{href}'"


@then('el enlace de email debe contener "{email}"')
def step_email_correcto(context, email):
    href = context.contacto_page.obtener_href_email()
    assert email in href, \
        f"Email esperado '{email}' no encontrado en href: '{href}'"


@then('el enlace debe usar el protocolo "{protocolo}"')
def step_protocolo_email(context, protocolo):
    href = context.contacto_page.obtener_href_email()
    assert href.startswith(protocolo), \
        f"Se esperaba protocolo '{protocolo}', href obtenido: '{href}'"


@then('el enlace debe tener el atributo target "{target}" o abrir la app de WhatsApp')
def step_target_whatsapp(context, target):
    target_actual = context.contacto_page.obtener_target_whatsapp()
    assert target_actual == target, \
        f"target esperado '{target}', obtenido '{target_actual}'"


@then('el widget de chat debe estar visible en la página')
def step_chat_visible(context):
    assert context.contacto_page.chat_widget_es_visible()


@then('el campo de texto del chat debe ser interactivo')
def step_chat_interactivo(context):
    assert context.contacto_page.chat_input_es_interactivo()


@then('el campo de texto debe contener el mensaje escrito')
def step_mensaje_en_chat(context):
    texto = context.contacto_page.obtener_texto_chat_input()
    assert texto == context.mensaje_escrito, \
        f"Mensaje esperado: '{context.mensaje_escrito}', obtenido: '{texto}'"


@then('el enlace de email debe ser visible')
def step_email_visible(context):
    assert context.contacto_page.email_es_visible(), \
        "El enlace de email no es visible en la sección de contacto"


@then('el enlace de WhatsApp debe ser visible y tener tamaño de toque adecuado')
def step_whatsapp_toque_adecuado(context):
    assert context.contacto_page.whatsapp_es_visible()
    assert context.contacto_page.link_tiene_tamano_toque_adecuado(
        ContactoLocators.LINK_WHATSAPP
    ), "El enlace de WhatsApp tiene un área de toque menor a 44px"


@then('el enlace de email debe ser visible y tener tamaño de toque adecuado')
def step_email_toque_adecuado(context):
    assert context.contacto_page.email_es_visible()
    assert context.contacto_page.link_tiene_tamano_toque_adecuado(
        ContactoLocators.LINK_EMAIL
    ), "El enlace de email tiene un área de toque menor a 44px"
