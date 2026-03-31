from selenium.webdriver.common.by import By


class NavegacionLocators:
    # Header / Logo
    LOGO = (By.CSS_SELECTOR, "div.logo")

    # Secciones por ID (acceso directo via URL anchor o scroll)
    SECCION_HERO = (By.CSS_SELECTOR, "section.hero")
    SECCION_SERVICIOS = (By.CSS_SELECTOR, "#servicios")
    SECCION_POR_QUE = (By.CSS_SELECTOR, "#por-que-elegirnos")
    SECCION_ESTADISTICAS = (By.CSS_SELECTOR, "#estadisticas")
    SECCION_PROCESO = (By.CSS_SELECTOR, "#proceso")
    SECCION_TECNOLOGIAS = (By.CSS_SELECTOR, "#tecnologias")
    SECCION_GENERADOR = (By.CSS_SELECTOR, "#gherkin-generator")
    SECCION_FAQ = (By.CSS_SELECTOR, "#faq")
    SECCION_CONTACTO = (By.CSS_SELECTOR, "#contacto")

    # Hero - contenido
    HERO_H1 = (By.CSS_SELECTOR, "section.hero h1")
    HERO_H2 = (By.CSS_SELECTOR, "section.hero h2")
    HERO_DESCRIPCION = (By.CSS_SELECTOR, "section.hero p")

    # Servicios - tarjetas (XPath por texto es más estable que nth-child)
    SERVICIOS_GRID = (By.CSS_SELECTOR, "#servicios .services-grid")
    TARJETAS_SERVICIO = (By.CSS_SELECTOR, "#servicios .service-card")
    TARJETA_AUTOMATIZACION = (
        By.XPATH,
        "//div[@class='service-card'][.//h3[text()='Automatización de Procesos']]",
    )
    TARJETA_PRUEBAS = (
        By.XPATH,
        "//div[@class='service-card'][.//h3[text()='Pruebas Automatizadas']]",
    )
    TARJETA_DESARROLLO = (
        By.XPATH,
        "//div[@class='service-card'][.//h3[text()='Desarrollo Web']]",
    )
    TARJETA_INTEGRACIONES = (
        By.XPATH,
        "//div[@class='service-card'][.//h3[text()='Integraciones y Scripts']]",
    )
    TITULOS_SERVICIO = (By.CSS_SELECTOR, "#servicios .service-card h3")

    # Métricas / Estadísticas
    ESTADISTICAS_SECCION = (By.CSS_SELECTOR, "#estadisticas")

    # Nota: No existe menú de navegación (<nav>) ni hamburguesa en el DOM.
    # La navegación se realiza directamente por URL anchor: https://tecfix.co/#seccion
