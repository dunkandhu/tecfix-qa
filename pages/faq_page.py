from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.faq_locators import FaqLocators


class FaqPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def seccion_es_visible(self):
        return self.wait.until(
            EC.visibility_of_element_located(FaqLocators.SECCION)
        ).is_displayed()

    def contar_items(self):
        items = self.wait.until(
            EC.presence_of_all_elements_located(FaqLocators.TODOS_LOS_ITEMS)
        )
        return len(items)

    def hacer_clic_item(self, numero):
        locators_por_numero = {
            1: FaqLocators.ITEM_1,
            2: FaqLocators.ITEM_2,
            3: FaqLocators.ITEM_3,
            4: FaqLocators.ITEM_4,
        }
        locator = locators_por_numero.get(numero)
        if not locator:
            raise ValueError(f"Número de item inválido: {numero}")
        pregunta = self.wait.until(
            EC.element_to_be_clickable(
                (locator[0], locator[1] + " .faq-question")
            )
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", pregunta)
        self.driver.execute_script("arguments[0].click();", pregunta)

    def respuesta_es_visible(self, numero):
        locators_por_numero = {
            1: FaqLocators.RESPUESTA_ITEM_1,
            2: FaqLocators.RESPUESTA_ITEM_2,
            3: FaqLocators.RESPUESTA_ITEM_3,
            4: FaqLocators.RESPUESTA_ITEM_4,
        }
        locator = locators_por_numero.get(numero)
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except Exception:
            return False

    def respuesta_esta_oculta(self, numero):
        return not self.respuesta_es_visible(numero)

    def obtener_texto_toggle(self, numero):
        locators_toggle = {
            1: FaqLocators.TOGGLE_ITEM_1,
            2: FaqLocators.TOGGLE_ITEM_2,
            3: FaqLocators.TOGGLE_ITEM_3,
            4: FaqLocators.TOGGLE_ITEM_4,
        }
        toggle = self.driver.find_element(*locators_toggle[numero])
        return toggle.text

    def obtener_textos_preguntas(self):
        elementos = self.wait.until(
            EC.presence_of_all_elements_located(FaqLocators.TEXTOS_PREGUNTAS)
        )
        return [e.text for e in elementos]

    def respuesta_no_desborda_contenedor(self, numero):
        locators_por_numero = {
            1: FaqLocators.RESPUESTA_ITEM_1,
            2: FaqLocators.RESPUESTA_ITEM_2,
            3: FaqLocators.RESPUESTA_ITEM_3,
            4: FaqLocators.RESPUESTA_ITEM_4,
        }
        respuesta = self.driver.find_element(*locators_por_numero[numero])
        seccion = self.driver.find_element(*FaqLocators.SECCION)
        return respuesta.rect["width"] <= seccion.rect["width"]
