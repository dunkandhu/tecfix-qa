# language: es
@generador
Característica: Generador de Casos de Prueba de tecfix.co
  Como visitante interesado en QA
  Quiero usar el generador de casos de prueba
  Para obtener escenarios de prueba automáticamente según mi contexto

  Antecedentes:
    Dado que el usuario abre el sitio "https://tecfix.co/"
    Y el usuario navega a la sección "Generador de Casos de Prueba"

  @smoke
  Escenario: El generador de casos de prueba está visible
    Entonces el formulario del generador debe estar visible
    Y el campo "Tipo de Prueba" debe estar presente
    Y el campo "Tecnología/Framework" debe estar presente
    Y el campo "Descripción de la Prueba" debe estar presente
    Y el botón "Generar Casos de Prueba" debe estar presente

  @funcional
  Escenario: Generación exitosa de casos de prueba
    Cuando el usuario selecciona el tipo de prueba "E2E Test"
    Y el usuario selecciona la tecnología "Selenium"
    Y el usuario ingresa la descripción "Validar el flujo de contacto por WhatsApp"
    Y el usuario hace clic en el botón "Generar Casos de Prueba"
    Entonces el área de resultados debe mostrar casos de prueba generados
    Y el botón "Copiar" debe estar habilitado
    Y el botón "Nuevos" debe estar habilitado

  @funcional
  Escenario: Generación con contexto adicional
    Cuando el usuario selecciona el tipo de prueba "API Test"
    Y el usuario selecciona la tecnología "Python"
    Y el usuario ingresa la descripción "Probar endpoint de generación de casos"
    Y el usuario ingresa el contexto adicional "Usar requests y validar status 200"
    Y el usuario hace clic en el botón "Generar Casos de Prueba"
    Entonces el área de resultados debe mostrar casos de prueba generados

  @funcional
  Esquema del escenario: Generación con distintos tipos de prueba
    Cuando el usuario selecciona el tipo de prueba "<tipo>"
    Y el usuario selecciona la tecnología "Python"
    Y el usuario ingresa la descripción "Prueba de ejemplo para validación"
    Y el usuario hace clic en el botón "Generar Casos de Prueba"
    Entonces el área de resultados debe mostrar casos de prueba generados

    Ejemplos:
      | tipo              |
      | Unit Test         |
      | Integration Test  |
      | E2E Test          |
      | API Test          |
      | Validation Test   |
      | User Flow Test    |

  @funcional
  Esquema del escenario: Generación con distintas tecnologías
    Cuando el usuario selecciona el tipo de prueba "E2E Test"
    Y el usuario selecciona la tecnología "<tecnologia>"
    Y el usuario ingresa la descripción "Prueba de ejemplo"
    Y el usuario hace clic en el botón "Generar Casos de Prueba"
    Entonces el área de resultados debe mostrar casos de prueba generados

    Ejemplos:
      | tecnologia        |
      | JavaScript/Node.js|
      | Python            |
      | Java              |
      | C#                |
      | React             |
      | Angular           |
      | Selenium          |
      | Cypress           |
      | SQL               |

  @funcional
  Escenario: El botón Copiar copia el resultado al portapapeles
    Cuando el usuario selecciona el tipo de prueba "Unit Test"
    Y el usuario selecciona la tecnología "Python"
    Y el usuario ingresa la descripción "Validar función de suma"
    Y el usuario hace clic en el botón "Generar Casos de Prueba"
    Y el área de resultados muestra casos de prueba generados
    Cuando el usuario hace clic en el botón "Copiar"
    Entonces el contenido del resultado debe estar en el portapapeles

  @funcional
  Escenario: El botón Nuevos limpia el resultado para una nueva generación
    Dado que el usuario ya generó casos de prueba anteriormente
    Cuando el usuario hace clic en el botón "Nuevos"
    Entonces el área de resultados debe estar vacía o mostrar el estado inicial
    Y el formulario debe estar listo para una nueva generación

  @negativo
  Escenario: Envío del formulario sin descripción
    Cuando el usuario selecciona el tipo de prueba "E2E Test"
    Y el usuario selecciona la tecnología "Selenium"
    Y el usuario deja vacío el campo "Descripción de la Prueba"
    Y el usuario hace clic en el botón "Generar Casos de Prueba"
    Entonces debe aparecer un mensaje de validación en el campo de descripción

  @negativo
  Escenario: Descripción con texto muy corto
    Cuando el usuario selecciona el tipo de prueba "E2E Test"
    Y el usuario selecciona la tecnología "Python"
    Y el usuario ingresa la descripción "x"
    Y el usuario hace clic en el botón "Generar Casos de Prueba"
    Entonces el sistema debe manejar la solicitud sin errores fatales

  @negativo
  Escenario: Descripción con caracteres especiales
    Cuando el usuario selecciona el tipo de prueba "Validation Test"
    Y el usuario selecciona la tecnología "Python"
    Y el usuario ingresa la descripción "<script>alert('xss')</script>"
    Y el usuario hace clic en el botón "Generar Casos de Prueba"
    Entonces el sistema no debe ejecutar scripts en el área de resultados
    Y el área de resultados debe mostrar texto plano sin ejecutar código

  @regresion
  Escenario: El generador sigue funcionando tras múltiples usos consecutivos
    Dado que el usuario ya generó casos de prueba anteriormente
    Cuando el usuario hace clic en el botón "Nuevos"
    Y el usuario selecciona el tipo de prueba "Integration Test"
    Y el usuario selecciona la tecnología "Java"
    Y el usuario ingresa la descripción "Validar integración con base de datos"
    Y el usuario hace clic en el botón "Generar Casos de Prueba"
    Entonces el área de resultados debe mostrar casos de prueba generados
