# tecfix-qa# 🤖 TecFix QA Automation

Framework de automatización QA para [tecfix.co](https://tecfix.co/) desarrollado con Python, Behave y Selenium.

![GitHub Actions](https://github.com/dunkandhu/tecfix-qa/actions/workflows/qa-tests.yml/badge.svg)
[![Allure Report](https://img.shields.io/badge/Allure-Report-green)](https://dunkandhu.github.io/tecfix-qa)

## 🛠️ Stack tecnológico

- **Python 3.14** — Lenguaje principal
- **Behave** — Framework BDD
- **Selenium** — Automatización UI
- **WebDriver Manager** — Gestión de drivers
- **GitHub Actions** — CI/CD

## 📁 Estructura del proyecto
```
tecfix-qa/
├── agents/          → Equipo de 9 agentes QA con IA
├── features/        → Casos de prueba en Gherkin
│   └── steps/       → Step definitions en Python
├── pages/           → Page Objects
├── locators/        → Selectores CSS y XPath
└── CLAUDE.md        → Contexto del proyecto para Claude Code
```

## 🧪 Módulos automatizados

- ✅ Navegación general
- ✅ FAQ con acordeón
- ✅ Generador de casos de prueba
- ✅ Contacto

## 🚀 Cómo ejecutar

**Instalar dependencias:**
```
pip install behave selenium webdriver-manager
```

**Correr todas las pruebas:**
```
python -m behave
```

**Correr un módulo específico:**
```
python -m behave features/navegacion.feature
```

## 🤖 Equipo de Agentes QA con IA

Este proyecto usa un equipo de 9 agentes especializados con Claude Code:

- 00 Orquestador — Coordina al equipo
- 01 Experto en Negocio — Conoce tecfix.co
- 02 Analista QA — Detecta qué probar
- 03 Escritor Gherkin — Genera casos de prueba
- 04 Automatizador — Crea steps y page objects
- 05 Experto API — Pruebas de servicios
- 06 Experto SQL — Validaciones de datos
- 07 Experto Frontend — Selectores y UI
- 08 Accesibilidad — UX y accesibilidad
- 09 Revisor — QA Lead del equipo

## 📊 Reporte de Pruebas

Ver reporte en vivo 👉 https://dunkandhu.github.io/tecfix-qa

## 👤 Autor

**Duncan** — QA Automation Engineer
