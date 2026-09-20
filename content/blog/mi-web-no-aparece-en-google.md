---
title: Mi web no aparece en Google: guía paso a paso
description: Por qué tu web no sale en Google, cómo comprobarlo en un minuto y qué revisar (robots.txt, noindex, servidor) para que el buscador la indexe.
date: 2026-09-20
updated: 2026-09-21
image: /assets/blog/mi-web-no-aparece-en-google.webp
image_alt: Hombre sentado ante ordenadores analizando datos representando el posicionamiento de una web en Google
---

Lanzas la web de tu negocio, buscas el nombre de tu empresa en el buscador y te encuentras con la peor sorpresa posible: tu sitio no se muestra por ningún lado. Es una situación muy común que suele generar frustración, pero en la gran mayoría de los casos se debe a fallos técnicos sencillos de resolver o a que no se han respetado los tiempos de los motores de búsqueda. En esta guía te explico paso a paso cómo diagnosticar y solucionar el problema si tu web no aparece en Google.

## ¿De verdad no está indexada? La comprobación inicial

Antes de entrar en pánico, hay que entender la diferencia entre no estar indexado y no estar posicionado. El rastreo es el proceso por el cual los robots de Google descubren tu web, mientras que la indexación es la decisión de almacenar esa página y mostrarla en los resultados, tal como separa [la documentación de Google sobre cómo funciona la Búsqueda](https://developers.google.com/search/docs/fundamentals/how-search-works?hl=es). Si estás empezando a trabajar la visibilidad de tu negocio, te sugiero leer sobre [qué es el SEO y por qué es importante para tu página web](/blog/que-es-el-seo/).

Para comprobar si Google conoce tu web, desactiva la opción de "Búsqueda Segura" en tu navegador para evitar filtros innecesarios [según indica Google](https://support.google.com/webmasters/answer/7474347?hl=es). Luego, realiza una búsqueda utilizando el operador `site:` seguido de tu dominio, por ejemplo, `site:tu-dominio.com`. Si tu sitio tiene menos de 500 páginas, no necesitas informes complejos; esta búsqueda directa es la forma más rápida de verificar si tus páginas clave aparecen en el índice [como detalla la ayuda de Search Console](https://support.google.com/webmasters/answer/7440203?hl=es). Si no aparece ningún resultado, entonces confirmamos que tu web no aparece en Google y debemos buscar la causa técnica.

## Los fallos técnicos más comunes que bloquean a Google

Cuando un sitio web es invisible para los buscadores, suele deberse a configuraciones incorrectas que impiden el paso de los rastreadores. Estos son los tres puntos críticos que siempre recomiendo revisar en primer lugar:

1. **El archivo robots.txt bloquea el acceso:** Este archivo de texto plano indica a los rastreadores a qué URLs de tu sitio pueden acceder [según la introducción a robots.txt de Google](https://developers.google.com/search/docs/crawling-indexing/robots/intro?hl=es). Si por error contiene la línea `Disallow: /`, estarás cerrando la puerta por completo a Googlebot. Puedes comprobarlo fácilmente escribiendo `tudominio.com/robots.txt` en tu navegador.
2. **La etiqueta meta noindex está activa:** Es muy habitual que los desarrolladores marquen la web como "no indexable" mientras trabajan en el entorno de pruebas y olviden desmarcar la casilla al lanzar la web definitiva. Esta directiva se inserta en el código HTML como `<meta name="robots" content="noindex">` y hace que Google retire la página de los resultados aunque otros sitios enlacen a ella [como explica la guía de la directiva noindex](https://developers.google.com/search/docs/crawling-indexing/block-indexing?hl=es).
3. **Problemas de disponibilidad del servidor:** Si tu servidor de alojamiento web es lento, inestable o sufre caídas constantes, Googlebot no podrá acceder a tu contenido. La capacidad de rastreo de Google está limitada por el ancho de banda, el tiempo y la disponibilidad de sus rastreadores: si tu servidor responde rápido se pueden rastrear más páginas de tu sitio, y si no, menos [como detalla la guía de errores de rastreo](https://developers.google.com/search/docs/crawling-indexing/troubleshoot-crawling-errors).

> **Importante:** Si has migrado tu web recientemente o has cambiado de HTTP a HTTPS, asegúrate de implementar redirecciones 301 correctas para que Google entienda que tu contenido se ha mudado y no pierdas el posicionamiento acumulado [según las recomendaciones oficiales](https://support.google.com/webmasters/answer/7474347?hl=es).

## Cómo usar Google Search Console para diagnosticar el problema

La herramienta definitiva para saber exactamente qué le pasa a tu web es Google Search Console [y su informe de indexación de páginas](https://support.google.com/webmasters/answer/7440203?hl=es). En su sección de "Páginas", dentro del menú de "Indexación", encontrarás un desglose detallado de los motivos por los que algunas URLs no se están mostrando.

No todas las páginas de tu web deben indexarse. Es normal y correcto que URLs duplicadas, páginas de políticas de privacidad o pasarelas de pago queden fuera del índice [según la documentación de Search Console](https://support.google.com/webmasters/answer/7440203?hl=es). Sin embargo, debes preocuparte si tus páginas de servicios o de contacto muestran estados de exclusión.

| Estado en Search Console | Qué significa realmente | Qué acción debes tomar |
| :--- | :--- | :--- |
| **Rastreada: actualmente sin indexar** | Google ha rastreado la página pero no la ha indexado; puede indexarla más adelante y no hace falta que vuelvas a solicitar el rastreo [según el informe de indexación](https://support.google.com/webmasters/answer/7440203?hl=es). | Mejora el contenido, añade enlaces internos y aporta valor real. |
| **Descubierta: actualmente sin indexar** | Google ha encontrado la URL pero todavía no la ha rastreado, normalmente porque ha calculado que hacerlo sobrecargaría el servidor [según el informe de indexación](https://support.google.com/webmasters/answer/7440203?hl=es). | Optimiza la velocidad de carga y la estructura de enlaces internos. |
| **Excluida por etiqueta 'noindex'** | Hay una directiva en el código que prohíbe expresamente la indexación de esa URL [como explica Google](https://developers.google.com/search/docs/crawling-indexing/block-indexing?hl=es). | Elimina la etiqueta noindex si es una página que quieres mostrar. |

Para solucionar estos problemas de forma estructural, te recomiendo aplicar buenas prácticas de [SEO On-Page para optimizar tu web desde dentro](/blog/seo-on-page/). Además, recuerda que la velocidad y la experiencia de usuario son factores determinantes. Si tu web tarda demasiado en cargar, Googlebot reducirá la frecuencia de sus visitas, por lo que es vital entender las [Core Web Vitals y cómo afectan a tu SEO](/blog/core-web-vitals-que-son/).

Si acabas de publicar tu sitio, ten paciencia. El proceso de rastreo e indexación no es inmediato y suele tardar desde unos días hasta varias semanas [según la ayuda de Search Console](https://support.google.com/webmasters/answer/7474347?hl=es). Si quieres saber más sobre los plazos habituales en el posicionamiento, puedes leer el artículo sobre [cuánto tarda el SEO en dar resultados](/blog/cuanto-tarda-en-verse-resultados-seo/).

## Preguntas frecuentes

### ¿Cuánto tarda Google en indexar una página nueva?
Para la mayoría de los sitios web, Google tarda al menos tres días en rastrear contenido nuevo [según la documentación de Google](https://developers.google.com/search/docs/crawling-indexing/troubleshoot-crawling-errors), y el proceso completo va de un día a varias semanas [según la ayuda de Search Console](https://support.google.com/webmasters/answer/7474347?hl=es). Si tu web es completamente nueva o tiene pocos enlaces externos, el buscador puede tardar algo más de tiempo en descubrirla e indexarla por primera vez.

### ¿Por qué mi web aparece con el comando site: pero no al buscar mis servicios?
Que una página esté indexada solo significa que está en la base de datos de Google, pero no garantiza que aparezca en las primeras posiciones para búsquedas competitivas [según Search Console](https://support.google.com/webmasters/answer/7440203?hl=es). Si tu web sale con el operador `site:` pero no por tus palabras clave, necesitas trabajar el posicionamiento orgánico y la relevancia de tus contenidos.

### ¿Sirve de algo pulsar repetidamente el botón de solicitar indexación?
No. Google avisa de que hay una cuota para enviar URLs concretas y de que solicitar varias veces el rastreo de una misma URL no hará que se rastree más rápido [según su guía para pedir que Google vuelva a rastrear](https://developers.google.com/search/docs/crawling-indexing/ask-google-to-recrawl?hl=es). Esta función solo sirve para avisar a Google de un cambio de contenido puntual, pero no corregirá una estructura deficiente, la falta de enlaces internos o un contenido de baja calidad.

## Conclusión
Si tu web no aparece en Google, casi siempre se debe a un bloqueo técnico en el archivo robots.txt, a una etiqueta noindex residual o simplemente a que el buscador necesita más tiempo para rastrear tu sitio. Utilizar Google Search Console te permitirá identificar el origen exacto del problema para corregirlo de manera estructural. Una vez resueltos estos bloqueos, tu negocio estará listo para empezar a ganar visibilidad en los resultados de búsqueda.

### ¿Quieres que revise por qué tu web no aparece en Google?

Analizo la configuración técnica de tu sitio para eliminar bloqueos y asegurar que los buscadores indexen tu contenido correctamente. [Contáctame](/#contacto).
