# Proyecto: tecfix-qa

## Descripción
Framework de automatización QA para https://tecfix.co/

## Stack tecnológico
- Lenguaje: Python
- BDD: Behave
- Automatización UI: Selenium con Page Object Model
- Pruebas API: requests de Python
- Control de versiones: GitHub

## Estructura del proyecto
- agents/ → agentes QA del equipo
- features/ → casos de prueba en Gherkin en español
- steps/ → step definitions en Python
- pages/ → clases Page Object
- locators/ → selectores CSS y XPath

## Convenciones
- Casos de prueba en español
- Steps reutilizables y genéricos
- Usar WebDriverWait, nunca time.sleep()
- Un archivo .feature por módulo
