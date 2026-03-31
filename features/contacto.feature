# language: es
@contacto
Característica: Canales de contacto de tecfix.co
  Como visitante interesado en los servicios
  Quiero poder contactar al equipo de TecFix
  Para solicitar información o una cotización

  Antecedentes:
    Dado que el usuario abre el sitio "https://tecfix.co/"
    Y el usuario navega a la sección "Contacto"

  @smoke
  Escenario: La sección de contacto está visible
    Entonces la sección de contacto debe estar visible
    Y debe mostrar al menos un canal de comunicación

  @funcional
  Escenario: El enlace de WhatsApp tiene el número correcto
    Entonces el enlace de WhatsApp debe contener el número "573212331643"
    Y el enlace debe apuntar al dominio "wa.me"

  @funcional
  Escenario: El enlace de email tiene la dirección correcta
    Entonces el enlace de email debe contener "contacto@tecfix.co"
    Y el enlace debe usar el protocolo "mailto"

  @funcional
  Escenario: El enlace de WhatsApp abre en nueva pestaña o aplicación
    Cuando el usuario hace clic en el botón de contacto por WhatsApp
    Entonces el enlace debe tener el atributo target "_blank" o abrir la app de WhatsApp

  @funcional
  Escenario: El chat widget está disponible en la página
    Entonces el widget de chat debe estar visible en la página
    Y el campo de texto del chat debe ser interactivo

  @funcional
  Escenario: El usuario puede escribir un mensaje en el chat widget
    Cuando el usuario hace clic en el widget de chat
    Y el usuario escribe "Quiero información sobre automatización"
    Entonces el campo de texto debe contener el mensaje escrito

  @funcional
  Escenario: Los canales de contacto son visibles en la sección correspondiente
    Entonces el enlace de WhatsApp debe ser visible y tener tamaño de toque adecuado
    Y el enlace de email debe ser visible

  @regresion
  Escenario: Los enlaces de contacto son accesibles en móvil
    Dado que el tamaño de ventana es 390 x 844
    Y el usuario navega a la sección "Contacto"
    Entonces el enlace de WhatsApp debe ser visible y tener tamaño de toque adecuado
    Y el enlace de email debe ser visible y tener tamaño de toque adecuado
