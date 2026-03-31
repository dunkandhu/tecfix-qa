from selenium.webdriver.common.by import By


class FaqLocators:
    # Contenedor principal
    SECCION = (By.CSS_SELECTOR, "#faq")
    LISTA_FAQ = (By.CSS_SELECTOR, "#faq .faq-list")

    # Todos los items del acordeón
    TODOS_LOS_ITEMS = (By.CSS_SELECTOR, "#faq .faq-item")

    # Items por índice (nth-child — frágil si se reordena el contenido)
    ITEM_1 = (By.CSS_SELECTOR, "#faq .faq-item:nth-child(1)")
    ITEM_2 = (By.CSS_SELECTOR, "#faq .faq-item:nth-child(2)")
    ITEM_3 = (By.CSS_SELECTOR, "#faq .faq-item:nth-child(3)")
    ITEM_4 = (By.CSS_SELECTOR, "#faq .faq-item:nth-child(4)")

    # Preguntas (clickable) por texto — más robusto que nth-child
    PREGUNTA_TIEMPO_DESARROLLO = (
        By.XPATH,
        "//div[@class='faq-question'][.//h3[contains(text(),'Cuánto tiempo')]]",
    )
    PREGUNTA_SOPORTE = (
        By.XPATH,
        "//div[@class='faq-question'][.//h3[contains(text(),'soporte')]]",
    )
    PREGUNTA_TAMANO_EMPRESA = (
        By.XPATH,
        "//div[@class='faq-question'][.//h3[contains(text(),'cualquier tamaño')]]",
    )
    PREGUNTA_METODOS_PAGO = (
        By.XPATH,
        "//div[@class='faq-question'][.//h3[contains(text(),'métodos de pago')]]",
    )

    # Respuestas (visibles cuando el item está expandido)
    TODAS_LAS_RESPUESTAS = (By.CSS_SELECTOR, "#faq .faq-item .faq-answer")
    RESPUESTA_ITEM_1 = (By.CSS_SELECTOR, "#faq .faq-item:nth-child(1) .faq-answer")
    RESPUESTA_ITEM_2 = (By.CSS_SELECTOR, "#faq .faq-item:nth-child(2) .faq-answer")
    RESPUESTA_ITEM_3 = (By.CSS_SELECTOR, "#faq .faq-item:nth-child(3) .faq-answer")
    RESPUESTA_ITEM_4 = (By.CSS_SELECTOR, "#faq .faq-item:nth-child(4) .faq-answer")

    # Ícono toggle +/- de cada pregunta
    TODOS_LOS_TOGGLES = (By.CSS_SELECTOR, "#faq .faq-question .faq-toggle")
    TOGGLE_ITEM_1 = (By.CSS_SELECTOR, "#faq .faq-item:nth-child(1) .faq-toggle")
    TOGGLE_ITEM_2 = (By.CSS_SELECTOR, "#faq .faq-item:nth-child(2) .faq-toggle")
    TOGGLE_ITEM_3 = (By.CSS_SELECTOR, "#faq .faq-item:nth-child(3) .faq-toggle")
    TOGGLE_ITEM_4 = (By.CSS_SELECTOR, "#faq .faq-item:nth-child(4) .faq-toggle")

    # Textos de las preguntas
    TEXTOS_PREGUNTAS = (By.CSS_SELECTOR, "#faq .faq-question h3")

    # Preguntas conocidas del sitio (para validar presencia)
    PREGUNTAS_ESPERADAS = [
        "¿Cuánto tiempo toma desarrollar una solución?",
        "¿Ofrecen soporte después de la entrega?",
        "¿Trabajan con empresas de cualquier tamaño?",
        "¿Qué métodos de pago aceptan?",
    ]
