# language: es
@smoke
Característica: Navegación principal de tecfix.co
  Como visitante del sitio
  Quiero poder navegar por todas las secciones
  Para encontrar la información que necesito sin inconvenientes

  Antecedentes:
    Dado que el usuario abre el sitio "https://tecfix.co/"

  @smoke
  Escenario: La página principal carga correctamente
    Entonces el título de la página debe contener "TecFix"
    Y la página debe cargar en menos de 3 segundos
    Y el encabezado principal debe ser visible

  @smoke
  Escenario: El menú de navegación está visible
    Entonces el menú de navegación debe estar visible
    Y debe contener los enlaces principales del sitio

  @funcional
  Esquema del escenario: Navegación por anclas a cada sección
    Cuando el usuario hace clic en el enlace de navegación "<seccion>"
    Entonces la sección "<seccion>" debe ser visible en pantalla

    Ejemplos:
      | seccion              |
      | Nuestros Servicios   |
      | Por qué TecFix       |
      | Nuestro Proceso      |
      | Tecnologías          |
      | Preguntas Frecuentes |
      | Contacto             |

  @funcional
  Escenario: El logo redirige al inicio de la página
    Cuando el usuario hace clic en el logo de TecFix
    Entonces la página debe desplazarse al inicio

  @funcional
  Escenario: Diseño responsivo en móvil
    Dado que el tamaño de ventana es 390 x 844
    Entonces el header debe ser visible en móvil
    Y el contenido principal debe adaptarse al ancho de la pantalla

  @funcional
  Escenario: Diseño responsivo en tablet
    Dado que el tamaño de ventana es 768 x 1024
    Entonces el contenido principal debe adaptarse al ancho de la pantalla

  @funcional
  Escenario: La sección de métricas muestra valores numéricos
    Entonces la sección "Números que Hablan" debe ser visible
    Y los indicadores de métricas deben mostrar valores
