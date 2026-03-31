from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.contacto_locators import ContactoLocators


class ContactoPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def seccion_es_visible(self):
        return self.wait.until(
            EC.visibility_of_element_located(ContactoLocators.SECCION)
        ).is_displayed()

    def obtener_href_whatsapp(self):
        link = self.wait.until(
            EC.presence_of_element_located(ContactoLocators.LINK_WHATSAPP)
        )
        return link.get_attribute("href")

    def obtener_href_email(self):
        link = self.wait.until(
            EC.presence_of_element_located(ContactoLocators.LINK_EMAIL)
        )
        return link.get_attribute("href")

    def obtener_target_whatsapp(self):
        link = self.wait.until(
            EC.presence_of_element_located(ContactoLocators.LINK_WHATSAPP)
        )
        return link.get_attribute("target")

    def whatsapp_es_visible(self):
        return self.wait.until(
            EC.visibility_of_element_located(ContactoLocators.LINK_WHATSAPP)
        ).is_displayed()

    def email_es_visible(self):
        return self.wait.until(
            EC.visibility_of_element_located(ContactoLocators.LINK_EMAIL)
        ).is_displayed()

    def chat_widget_es_visible(self):
        return self.wait.until(
            EC.visibility_of_element_located(ContactoLocators.CHAT_BTN_FLOTANTE)
        ).is_displayed()

    def chat_input_es_interactivo(self):
        campo = self.wait.until(
            EC.presence_of_element_located(ContactoLocators.CHAT_INPUT)
        )
        return campo.is_enabled()

    def escribir_en_chat(self, mensaje):
        campo = self.wait.until(
            EC.element_to_be_clickable(ContactoLocators.CHAT_INPUT)
        )
        campo.clear()
        campo.send_keys(mensaje)

    def obtener_texto_chat_input(self):
        campo = self.driver.find_element(*ContactoLocators.CHAT_INPUT)
        return campo.get_attribute("value")

    def link_tiene_tamano_toque_adecuado(self, locator, minimo_px=44):
        elemento = self.driver.find_element(*locator)
        alto = elemento.rect["height"]
        ancho = elemento.rect["width"]
        return alto >= minimo_px or ancho >= minimo_px
