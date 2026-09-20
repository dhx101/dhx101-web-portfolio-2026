---
title: WordPress con Elementor o código a medida: qué te conviene
description: Comparativa honesta entre WordPress con un constructor visual y un desarrollo a medida, para elegir según lo que tu negocio necesita de verdad y no por moda.
date: 2026-05-08
updated: 2026-09-18
image: /assets/blog/wordpress-elementor-vs-codigo-a-medida.webp
image_alt: Desarrollador programando, comparando WordPress y desarrollo a medida
---

Cuando alguien me pregunta si debería hacer su web "en WordPress o en código", la pregunta útil no es cuál es mejor en general, sino cuál resuelve mejor su caso. He trabajado con las dos: más de una decena de webs de clientes con WordPress y Elementor, hoy también con Bricks Builder, y proyectos a medida como mi [Web Client Portal](/proyectos/), hecho con Next.js. Cada opción tiene un terreno en el que gana con claridad. Te explico cuál es cada uno y cómo decidir.

## Qué significa cada opción

- **WordPress con un constructor visual** (Elementor, Bricks): un gestor de contenidos sobre el que se diseña la web con bloques visuales. Es la opción más habitual para webs de negocio.
- **Código a medida:** una aplicación programada desde cero con frameworks como Next.js o React, pensada para un problema concreto.

WordPress es [software de código abierto con licencia GPLv2](https://wordpress.org/about/), y según su propia web lo usa más del 43 % de todas las webs. Esa popularidad tiene una consecuencia práctica: es fácil encontrar quien la mantenga, y hay una solución probada para casi cualquier necesidad común.

## Cuándo WordPress con un constructor es la opción correcta

- **Webs de presentación y tiendas estándar.** Restaurantes, clínicas, estudios de arquitectura o agencias: páginas de servicios, formulario de contacto, blog y, si hace falta, una tienda con WooCommerce.
- **Cuando vas a editar tú el contenido.** Cambiar textos, subir fotos o publicar en el blog sin pedir ayuda cada vez.
- **Presupuestos y plazos ajustados.** El [directorio oficial de WordPress](https://wordpress.org/plugins/) tiene más de 72.000 plugins gratuitos, así que casi siempre hay algo que resuelve formularios, reservas, idiomas o SEO sin programarlo desde cero.
- **Cuando quieres independencia del proveedor.** Al ser tan extendido, cualquier otro profesional puede continuar el trabajo.

El precio de esta comodidad es el mantenimiento: actualizaciones, plugins que chocan entre sí y webs que engordan si nadie las vigila. Lo cuento en [mantenimiento web](/blog/mantenimiento-web-por-que-es-necesario/), y los fallos típicos en [errores SEO comunes en Elementor](/blog/errores-seo-comunes-en-elementor/).

## Cuándo el código a medida gana

- **Lógica de negocio propia que ningún plugin resuelve bien.** Por ejemplo, un panel donde cada cliente ve solo el estado de su web y sus facturas, y puede pagarlas online. Eso no es "una web con contenido": es una aplicación con usuarios, permisos y una base de datos detrás.
- **Integraciones complejas** con pasarelas de pago, CRMs o sistemas internos que necesitan control total sobre el servidor.
- **Cuando el proyecto va a crecer en funcionalidades** de forma continua, no solo en contenido.
- **Cuando la fiabilidad importa tanto como el diseño.** En código propio puedes cubrir el sistema con pruebas automáticas, algo mucho más difícil de garantizar en una web montada a base de plugins de terceros.

El Web Client Portal es justo ese caso: Next.js, TypeScript, PostgreSQL, pagos con Stripe, una cola de emails con reintentos y pruebas automatizadas. Si te interesan los detalles técnicos, cuento [por qué migré de SQLite a Postgres](/blog/de-sqlite-a-postgres-por-que-migre-mi-base-de-datos/) y [cómo monté la cola de emails](/blog/cola-de-emails-con-reintentos-en-nextjs/).

El precio de esta opción es mayor al principio y cualquier cambio necesita a un desarrollador.

## Un punto intermedio: WordPress y algo propio al lado

A veces la respuesta no es "uno u otro". En el Web Client Portal, los sitios WordPress de los clientes siguen siendo su web pública, y el panel propio se conecta a ellos para consultar su estado. WordPress hace lo que hace bien, publicar contenido, y la aplicación a medida resuelve el proceso de negocio que ningún plugin cubría.

## Dos casos reales, uno de cada lado

- **Makisu Sushi Petrer:** un restaurante que necesita que lo encuentren en Google, enseñar su carta y que la gente llame para reservar. Lo hice con WordPress y Bricks, porque todo eso es contenido y un constructor visual lo resuelve de sobra, con mucho menos coste que una aplicación.
- **Web Client Portal:** usuarios con permisos, facturas, pagos online y avisos automáticos cuando algo falla. Eso ya no es una web, es una aplicación, y por eso la construí a medida.

La diferencia no está en el tamaño del proyecto, sino en si lo que necesitas es mostrar información o hacer funcionar un proceso.

## Cómo decidir

Hazte tres preguntas:

1. **¿Necesito mostrar contenido o resolver un proceso con reglas propias?** Lo primero apunta a WordPress; lo segundo, a código a medida.
2. **¿Quién va a editar la web el día a día?** Si eres tú, sin conocimientos técnicos, WordPress te lo pone más fácil.
3. **¿Cuánto va a crecer?** Si en un año seguirá siendo una web de presentación, no pagues por una aplicación.

## Preguntas frecuentes

### ¿Una web a medida es siempre más rápida?

Puede serlo, porque solo carga lo que necesita, pero una web WordPress bien optimizada puede ser muy rápida. Lo que la hace lenta suele ser el exceso de plugins e imágenes, no WordPress en sí.

### ¿Me quedo atado al desarrollador con código a medida?

Más que con WordPress, sí. Por eso conviene que el código sea tuyo, esté documentado y use tecnologías conocidas.

### ¿Cuánto cuesta cada opción?

La web a medida cuesta más al principio. Te explico qué mueve el precio en [cuánto cuesta una página web](/blog/cuanto-cuesta-una-pagina-web-negocio-local/).

## Conclusión

WordPress con un constructor visual es la mejor opción para la mayoría de webs de negocio: rápida de montar, fácil de editar y con soluciones para casi todo. El código a medida gana cuando tu negocio necesita una aplicación, no una web. Elige por lo que necesitas hoy y en un año, no por moda.

### ¿No tienes claro cuál te conviene?

Te ayudo a decidirlo con honestidad, sin venderte la opción más cara por defecto. [Contáctame](/#contacto).
