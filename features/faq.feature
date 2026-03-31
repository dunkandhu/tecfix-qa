# language: es
@faq
Característica: Sección de Preguntas Frecuentes de tecfix.co
  Como visitante con dudas sobre los servicios
  Quiero interactuar con la sección de FAQ
  Para resolver mis preguntas sin necesidad de contactar al equipo

  Antecedentes:
    Dado que el usuario abre el sitio "https://tecfix.co/"
    Y el usuario navega a la sección "Preguntas Frecuentes"

  @smoke
  Escenario: La sección FAQ está visible con sus preguntas
    Entonces la sección de preguntas frecuentes debe estar visible
    Y debe mostrar al menos una pregunta en el acordeón

  @funcional
  Escenario: Expandir una pregunta del acordeón
    Cuando el usuario hace clic en la primera pregunta del acordeón
    Entonces la respuesta de esa pregunta debe hacerse visible
    Y el ícono del acordeón debe cambiar de estado

  @funcional
  Escenario: Cerrar una pregunta ya abierta del acordeón
    Dado que el usuario expandió la primera pregunta del acordeón
    Cuando el usuario hace clic nuevamente en esa pregunta
    Entonces la respuesta debe ocultarse
    Y el ícono del acordeón debe regresar a su estado inicial

  @funcional
  Esquema del escenario: Cada pregunta del acordeón es interactiva
    Cuando el usuario hace clic en la pregunta número <numero>
    Entonces la respuesta número <numero> debe hacerse visible

    Ejemplos:
      | numero |
      | 1      |
      | 2      |
      | 3      |
      | 4      |

  @funcional
  Escenario: Solo una pregunta permanece abierta a la vez
    Dado que el usuario expandió la primera pregunta del acordeón
    Cuando el usuario hace clic en la segunda pregunta del acordeón
    Entonces la respuesta de la segunda pregunta debe hacerse visible
    Y la respuesta de la primera pregunta debe ocultarse

  @regresion
  Escenario: El acordeón funciona correctamente en móvil
    Dado que el tamaño de ventana es 390 x 844
    Y el usuario navega a la sección "Preguntas Frecuentes"
    Cuando el usuario hace clic en la primera pregunta del acordeón
    Entonces la respuesta de esa pregunta debe hacerse visible
    Y el texto de la respuesta no debe desbordarse del contenedor
