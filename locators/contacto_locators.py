from selenium.webdriver.common.by import By


class ContactoLocators:
    # Contenedor principal
    SECCION = (By.CSS_SELECTOR, "#contacto")

    # Enlace de WhatsApp (STABLE — href único)
    LINK_WHATSAPP = (By.CSS_SELECTOR, "a.whatsapp-button")
    LINK_WHATSAPP_POR_HREF = (By.CSS_SELECTOR, "a[href='https://wa.me/573212331643']")

    # Enlace de email (STABLE — href único)
    LINK_EMAIL = (By.CSS_SELECTOR, "a[href='mailto:contacto@tecfix.co']")
    LINK_EMAIL_POR_CLASE = (By.CSS_SELECTOR, "#contacto .contact-link")

    # Datos esperados para validación
    WHATSAPP_NUMERO = "573212331643"
    WHATSAPP_DOMINIO = "wa.me"
    EMAIL_DIRECCION = "contacto@tecfix.co"
    EMAIL_PROTOCOLO = "mailto"
    WHATSAPP_TARGET = "_blank"

    # Chat Widget — todos los elementos tienen ID (STABLE)
    CHAT_WIDGET = (By.CSS_SELECTOR, "#chatWidget")
    CHAT_HEADER = (By.CSS_SELECTOR, "#chatHeader")
    CHAT_TOGGLE_BTN = (By.CSS_SELECTOR, "#chatToggle")
    CHAT_BODY = (By.CSS_SELECTOR, "#chatBody")
    CHAT_MENSAJES = (By.CSS_SELECTOR, "#chatMessages")
    CHAT_INPUT = (By.CSS_SELECTOR, "#chatInput")
    CHAT_BTN_ENVIAR = (By.CSS_SELECTOR, "#chatSend")
    CHAT_BTN_FLOTANTE = (By.CSS_SELECTOR, "#chatButton")

    # Mensajes del bot dentro del chat
    MENSAJES_BOT = (By.CSS_SELECTOR, "#chatMessages .bot-message .message-content p")
    MENSAJES_USUARIO = (By.CSS_SELECTOR, "#chatMessages .user-message .message-content p")
