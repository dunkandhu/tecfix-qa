from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from locators.generador_locators import GeneradorLocators


class GeneradorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def formulario_es_visible(self):
        return self.wait.until(
            EC.visibility_of_element_located(GeneradorLocators.FORMULARIO)
        ).is_displayed()

    def campo_es_visible(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        ).is_displayed()

    def seleccionar_tipo_prueba(self, valor_visible):
        select_elem = self.wait.until(
            EC.element_to_be_clickable(GeneradorLocators.SELECT_TIPO_PRUEBA)
        )
        Select(select_elem).select_by_visible_text(valor_visible)

    def seleccionar_tecnologia(self, valor_visible):
        select_elem = self.wait.until(
            EC.element_to_be_clickable(GeneradorLocators.SELECT_TECNOLOGIA)
        )
        Select(select_elem).select_by_visible_text(valor_visible)

    def ingresar_descripcion(self, texto):
        campo = self.wait.until(
            EC.visibility_of_element_located(GeneradorLocators.TEXTAREA_DESCRIPCION)
        )
        campo.clear()
        campo.send_keys(texto)

    def ingresar_contexto(self, texto):
        campo = self.wait.until(
            EC.visibility_of_element_located(GeneradorLocators.TEXTAREA_CONTEXTO)
        )
        campo.clear()
        campo.send_keys(texto)

    def hacer_clic_generar(self):
        btn = self.wait.until(
            EC.element_to_be_clickable(GeneradorLocators.BTN_GENERAR)
        )
        btn.click()

    def esperar_resultados(self):
        self.wait.until(
            EC.invisibility_of_element_located(GeneradorLocators.LOADING_SPINNER)
        )
        self.wait.until(
            EC.visibility_of_element_located(GeneradorLocators.RESULTADOS_CONTENEDOR)
        )

    def resultados_son_visibles(self):
        contenedor = self.driver.find_element(*GeneradorLocators.RESULTADOS_CONTENEDOR)
        return contenedor.is_displayed()

    def obtener_texto_resultado(self):
        codigo = self.wait.until(
            EC.visibility_of_element_located(GeneradorLocators.RESULTADOS_CODIGO)
        )
        return codigo.text

    def boton_copiar_es_visible(self):
        return self.wait.until(
            EC.visibility_of_element_located(GeneradorLocators.BTN_COPIAR)
        ).is_displayed()

    def boton_nuevos_es_visible(self):
        return self.wait.until(
            EC.visibility_of_element_located(GeneradorLocators.BTN_NUEVOS)
        ).is_displayed()

    def hacer_clic_copiar(self):
        btn = self.wait.until(EC.element_to_be_clickable(GeneradorLocators.BTN_COPIAR))
        btn.click()

    def hacer_clic_nuevos(self):
        btn = self.wait.until(EC.element_to_be_clickable(GeneradorLocators.BTN_NUEVOS))
        btn.click()

    def resultados_estan_ocultos(self):
        contenedor = self.driver.find_element(*GeneradorLocators.RESULTADOS_CONTENEDOR)
        return not contenedor.is_displayed()

    def descripcion_tiene_validacion_html5(self):
        campo = self.driver.find_element(*GeneradorLocators.TEXTAREA_DESCRIPCION)
        return not campo.get_attribute("validity") or \
               self.driver.execute_script(
                   "return !arguments[0].validity.valid;", campo
               )

    def obtener_texto_resultado_raw(self):
        return self.driver.find_element(*GeneradorLocators.RESULTADOS_CODIGO).text
