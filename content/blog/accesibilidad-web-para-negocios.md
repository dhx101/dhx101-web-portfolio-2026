---
title: Accesibilidad web: qué es y por qué le importa a tu negocio
description: Qué es la accesibilidad web, a cuántos clientes afecta, qué dice la normativa europea y los cambios más sencillos para que tu web la pueda usar todo el mundo.
date: 2026-09-19
---

Una web accesible es una web que puede usar cualquier persona: quien ve mal, quien no puede usar el ratón, quien navega con un lector de pantalla o quien simplemente está al sol con el móvil. Suena a requisito técnico, pero afecta directamente a cuánta gente puede comprarte, reservar o pedirte presupuesto. En este post te explico qué es, a cuánta gente afecta y por dónde empezar sin rehacer la web.

## Qué es la accesibilidad web

La accesibilidad consiste en diseñar y desarrollar la web para que funcione con todo tipo de capacidades. La [guía de diseño inclusivo de Google](https://developers.google.com/tech-writing/accessibility/self-study/inclusive-design) lo plantea teniendo en cuenta tres situaciones distintas:

- **Permanentes**: una persona ciega o con movilidad reducida.
- **Temporales**: un brazo roto, o las pupilas dilatadas después de ir al oculista.
- **Situacionales**: una sala a oscuras, un sitio con mucho ruido o tener las manos ocupadas.

Esa última categoría es la que más se olvida y la que mejor explica por qué no es un tema de "unos pocos". Cualquiera de tus clientes pasa por alguna de esas situaciones en algún momento.

## A cuánta gente afecta

Según recoge [web.dev en su curso de accesibilidad](https://web.dev/learn/accessibility/why/), la Organización Mundial de la Salud estima que más del 15 % de la población mundial, unos 1.300 millones de personas, se identifica como persona con discapacidad. Y si se suman sus familias, amigos y entorno, ese mercado llega al 53 % de todos los consumidores.

Dicho de otra forma: una web difícil de usar no solo deja fuera a una minoría, también complica la decisión de compra a la gente de su alrededor.

> **Importante:** según ese mismo curso, en la Unión Europea las exigencias de accesibilidad se aplican tanto al sector público como a empresas privadas. Si vendes online o das servicio a clientes, conviene que confirmes con un asesor qué te afecta en tu caso concreto.

## El efecto rampa: lo que haces por unos lo notan todos

Google explica en su documentación sobre [los beneficios de las interfaces adaptables](https://developers.google.com/natively-adaptive-interfaces/guides/benefits) el llamado efecto rampa: el rebaje de la acera pensado para sillas de ruedas acaba ayudando a quien lleva un carrito, un carro de reparto o una maleta. En la web pasa lo mismo, y la mayoría de mejoras de accesibilidad benefician a todo el mundo:

| Mejora | A quién ayuda primero | A quién más ayuda |
|---|---|---|
| Buen contraste de texto | Personas con baja visión | Cualquiera que lea al sol |
| Navegación con teclado | Personas que no usan ratón | Quien rellena formularios rápido |
| Texto que se amplía bien | Personas con baja visión | Quien lee en un móvil pequeño |
| Formularios bien etiquetados | Usuarios de lectores de pantalla | Quien rellena con prisa o distraído |

Además, una web más clara y ordenada es también una web que pierde menos visitas por el camino. Si te preocupa eso, repasa las [señales de que tu web te hace perder clientes](/blog/senales-de-que-tu-web-te-hace-perder-clientes/).

## Por dónde empezar: cambios sencillos

No hace falta rehacer la web para mejorar mucho. Estos son los cambios que te recomiendo revisar primero, todos recogidos en [el módulo de accesibilidad de web.dev](https://web.dev/learn/design/accessibility?hl=es-419) y en [las recomendaciones de Google para el frontend](https://developers.google.com/solutions/content-driven/frontend/accessibility):

1. **Usa HTML semántico y etiqueta todos los campos de los formularios**, para que las tecnologías de asistencia entiendan qué es cada cosa.
2. **Comprueba el contraste** entre el texto y el fondo, sobre todo en botones y textos pequeños.
3. **No dependas solo del color**: un enlace debería distinguirse también por estar subrayado o en negrita.
4. **Usa unidades relativas** como `rem` para el texto y comprueba que la web sigue funcionando al ampliar el tamaño de letra entre un 200 % y un 400 %.
5. **Haz visible el foco del teclado** con `:focus-visible` y revisa que el orden de tabulación siga el orden visual.
6. **Respeta a quien pide menos movimiento** envolviendo las animaciones en `prefers-reduced-motion`.
7. **Indica el idioma** de la página con el atributo `lang`.

Muchos de estos puntos también mejoran cómo entiende Google tu página. Si quieres ver esa parte, te lo explico en [qué es el SEO On-Page](/blog/seo-on-page/).

## Cómo comprobar si tu web es accesible

La propia guía de web.dev menciona varias herramientas gratuitas: el **inspector de accesibilidad de Firefox**, que además te enseña el orden de tabulación de la página, las herramientas para desarrolladores de Chrome, que simulan distintos tipos de visión, y extensiones como VisBug para revisar el contraste.

Las recomendaciones de Google añaden algo que ninguna herramienta sustituye: probar los formularios con tecnologías de asistencia, como un lector de pantalla, para vivir la experiencia de quien las necesita. Si tu web es de WordPress y la mantiene otra persona, pídele que incluya estas comprobaciones; es parte del [mantenimiento web que tu página necesita](/blog/mantenimiento-web-por-que-es-necesario/).

## Preguntas frecuentes

### ¿La accesibilidad solo importa a las webs grandes?

No. Según web.dev, en la Unión Europea las exigencias alcanzan también a empresas privadas, y el público al que afecta, sumando el entorno de las personas con discapacidad, llega al 53 % de los consumidores. Para un negocio local, eso son clientes que hoy pueden estar marchándose sin decir nada.

### ¿Puedo arreglarlo sin rehacer la web?

En la mayoría de casos, sí. Contraste, etiquetas de formularios, textos alternativos, foco visible e idioma de la página son cambios acotados. Lo que más cuesta suele ser un diseño con componentes a medida mal construidos; si ese es tu caso, te puede interesar comparar [WordPress con Elementor o código a medida](/blog/wordpress-elementor-vs-codigo-a-medida/).

### ¿Qué herramienta uso para revisar mi web?

Para empezar, el inspector de accesibilidad de Firefox y las herramientas de desarrollo de Chrome, que son gratuitas. Te dan una lista de problemas por los que empezar, pero conviene completarlas con una prueba real usando el teclado y un lector de pantalla.

## Conclusión

La accesibilidad web no es un extra para cumplir: decide cuánta gente puede usar tu web de verdad. Afecta a más clientes de los que parece, en la Unión Europea también alcanza a empresas privadas y la mayoría de mejoras son sencillas y benefician a todos tus visitantes.

### ¿Quieres saber cómo de accesible es tu web?

Reviso tu web con estas herramientas, te digo qué falla y lo corrijo sin cambiar el diseño que ya tienes. [Contáctame](/#contacto).
