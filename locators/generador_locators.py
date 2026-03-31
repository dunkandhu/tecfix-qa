from selenium.webdriver.common.by import By


class GeneradorLocators:
    # Contenedor principal
    SECCION = (By.CSS_SELECTOR, "#gherkin-generator")
    FORMULARIO = (By.CSS_SELECTOR, "#gherkinForm")

    # Campos del formulario — todos tienen ID (STABLE)
    SELECT_TIPO_PRUEBA = (By.CSS_SELECTOR, "#testType")
    SELECT_TECNOLOGIA = (By.CSS_SELECTOR, "#technology")
    TEXTAREA_DESCRIPCION = (By.CSS_SELECTOR, "#testDescription")
    TEXTAREA_CONTEXTO = (By.CSS_SELECTOR, "#additionalContext")

    # Botón de envío
    BTN_GENERAR = (By.CSS_SELECTOR, "button.gherkin-submit-btn")

    # Valores del select Tipo de Prueba (atributo value en el option)
    TIPO_UNITARIA = "unitaria"
    TIPO_INTEGRACION = "integracion"
    TIPO_E2E = "e2e"
    TIPO_API = "api"
    TIPO_VALIDACION = "validacion"
    TIPO_FLUJO = "flujo"

    # Valores del select Tecnología/Framework (atributo value en el option)
    TECH_JAVASCRIPT = "javascript"
    TECH_PYTHON = "python"
    TECH_JAVA = "java"
    TECH_CSHARP = "csharp"
    TECH_REACT = "react"
    TECH_ANGULAR = "angular"
    TECH_SELENIUM = "selenium"
    TECH_CYPRESS = "cypress"
    TECH_SQL = "sql"
    TECH_OTRO = "otro"

    # Área de resultados — oculta (display:none) hasta que se genera
    RESULTADOS_CONTENEDOR = (By.CSS_SELECTOR, "#gherkinResults")
    RESULTADOS_CODIGO = (By.CSS_SELECTOR, "#gherkinCode")

    # Botones de resultados (STABLE — tienen ID)
    BTN_COPIAR = (By.CSS_SELECTOR, "#copyGherkin")
    BTN_NUEVOS = (By.CSS_SELECTOR, "#newGherkin")

    # Estado de carga (oculto por defecto, visible durante la generación)
    LOADING_SPINNER = (By.CSS_SELECTOR, "#gherkinLoading")
    LOADING_TEXTO = (By.CSS_SELECTOR, "#gherkinLoading p")
