import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.navegacion_locators import NavegacionLocators


ANCHORS = {
    "Nuestros Servicios": "#servicios",
    "Por qué TecFix": "#por-que-elegirnos",
    "Nuestro Proceso": "#proceso",
    "Tecnologías": "#tecnologias",
    "Preguntas Frecuentes": "#faq",
    "Generador de Casos de Prueba": "#gherkin-generator",
    "Contacto": "#contacto",
}


class NavegacionPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def abrir(self, url):
        self.driver.get(url)
        self.wait.until(EC.visibility_of_element_located(NavegacionLocators.HERO_H1))

    def navegar_a_seccion(self, nombre_seccion):
        anchor = ANCHORS.get(nombre_seccion)
        if anchor:
            self.driver.get(self.driver.current_url.split("#")[0] + anchor)
        else:
            raise ValueError(f"Sección desconocida: '{nombre_seccion}'")

    def obtener_titulo_pagina(self):
        return self.driver.title

    def obtener_texto_h1(self):
        h1 = self.wait.until(EC.visibility_of_element_located(NavegacionLocators.HERO_H1))
        return h1.text

    def logo_es_visible(self):
        return self.wait.until(
            EC.visibility_of_element_located(NavegacionLocators.LOGO)
        ).is_displayed()

    def hacer_clic_logo(self):
        logo = self.wait.until(EC.element_to_be_clickable(NavegacionLocators.LOGO))
        logo.click()

    def seccion_es_visible(self, locator):
        elemento = self.wait.until(EC.visibility_of_element_located(locator))
        return elemento.is_displayed()

    def cambiar_tamano_ventana(self, ancho, alto):
        self.driver.set_window_size(ancho, alto)

    def medir_tiempo_carga(self, url):
        inicio = time.time()
        self.driver.get(url)
        self.wait.until(EC.visibility_of_element_located(NavegacionLocators.HERO_H1))
        return time.time() - inicio

    def obtener_titulos_servicios(self):
        elementos = self.wait.until(
            EC.presence_of_all_elements_located(NavegacionLocators.TITULOS_SERVICIO)
        )
        return [e.text for e in elementos]

    def seccion_estadisticas_tiene_valores(self):
        self.wait.until(
            EC.visibility_of_element_located(NavegacionLocators.ESTADISTICAS_SECCION)
        )
        numeros = self.driver.find_elements(
            *NavegacionLocators.ESTADISTICAS_SECCION
        )
        return len(numeros) > 0
