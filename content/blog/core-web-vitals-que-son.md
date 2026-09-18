---
title: Core Web Vitals: qué son y cómo afectan a tu SEO
description: Qué son los Core Web Vitals de Google (LCP, INP y CLS), qué valores se consideran buenos, cómo medirlos bien y cómo mejorarlos en una web WordPress.
date: 2026-06-10
updated: 2026-09-18
image: /assets/blog/core-web-vitals-que-son.webp
image_alt: Métricas de velocidad y rendimiento web en pantalla
---

Una web lenta pierde clientes antes de que lean nada: la imagen principal tarda en aparecer, el botón no responde o el texto salta justo cuando vas a pulsar. Google mide exactamente esas tres molestias con los Core Web Vitals. En este post te explico qué mide cada una, qué valores son buenos, cómo medirlas sin engañarte y qué suelo corregir primero en una web WordPress.

## Qué son los Core Web Vitals

Son tres métricas que miden la experiencia real de carga, respuesta y estabilidad de una página. Forman parte del [SEO On-Page](/blog/seo-on-page/) técnico, y Google confirma en su documentación sobre experiencia de página que [sus sistemas de posicionamiento las usan](https://developers.google.com/search/docs/appearance/page-experience). No son la única señal ni la más importante, pero sí de las pocas que puedes medir con números exactos.

## Las tres métricas

### LCP (Largest Contentful Paint)

Mide cuánto tarda en aparecer el elemento más grande visible al entrar en la página, que suele ser la imagen principal o un bloque de texto grande. Google considera bueno un LCP de 2,5 segundos o menos.

**Causas típicas de un LCP lento:** imágenes enormes sin comprimir, un servidor que tarda en responder o una página que carga demasiados recursos antes de mostrar el contenido principal.

### INP (Interaction to Next Paint)

Mide cuánto tarda la web en reaccionar cuando tocas, haces clic o escribes. El objetivo es quedarse en 200 milisegundos o menos. INP [sustituyó a la antigua métrica FID](https://web.dev/blog/inp-cwv-launch) como Core Web Vital en marzo de 2024; según web.dev, para resolver muchas de las carencias que tenía FID al medir la respuesta de la página.

**Causas típicas:** mucho JavaScript ejecutándose a la vez, widgets de terceros pesados o animaciones mal optimizadas.

### CLS (Cumulative Layout Shift)

Mide cuánto se mueve el contenido mientras carga, como cuando vas a pulsar un botón y aparece una imagen encima que te hace pulsar otra cosa. El objetivo es 0,1 o menos.

**Causas típicas:** imágenes o banners sin dimensiones reservadas, anuncios que se insertan tarde o fuentes que cambian el tamaño del texto al cargar.

## Cómo se mide "bueno": el percentil 75

Este detalle se suele pasar por alto. Según [web.dev](https://web.dev/articles/vitals), la guía técnica de Google para desarrolladores, una página cumple si alcanza los tres objetivos en el percentil 75 de las visitas, por separado en móvil y en ordenador. Dicho de otra forma: no basta con que tu web vaya rápida en tu ordenador de la oficina. Tiene que ir bien para al menos tres de cada cuatro personas que la visitan, incluidas las que entran con un móvil modesto y mala cobertura.

## Cómo comprobar los tuyos

La herramienta más directa es **PageSpeed Insights** (pagespeed.web.dev). Pero hay que saber leerla, porque [da dos tipos de datos](https://developers.google.com/speed/docs/insights/v5/about):

- **Datos de campo:** los de usuarios reales de Chrome, del informe CrUX. Son los que importan para el posicionamiento, pero solo aparecen si tu web tiene suficiente tráfico.
- **Datos de laboratorio:** una simulación con Lighthouse. Sirven para encontrar el problema, pero no reflejan lo que vive tu cliente.

Si tu web es pequeña y PageSpeed no muestra datos de campo, es normal. En ese caso, guíate por los de laboratorio y por el informe de Core Web Vitals de Search Console cuando tengas datos.

## Cómo mejorarlos en WordPress

Es de las partes de mi trabajo que más resultados da. En Ángulo Tres, la agencia en la que fui el único perfil técnico, conseguí que las webs de los clientes cargaran hasta un 60 % más rápido trabajando justo sobre estas métricas. Lo que reviso primero:

### Para el LCP

- Comprimir las imágenes y usar formatos modernos como WebP.
- **No aplicar carga diferida (lazy loading) a la imagen principal.** Un análisis de web.dev con datos reales encontró que [las webs que usan lazy loading tienden a tener peor LCP](https://web.dev/articles/lcp-lazy-loading), también en WordPress, sobre todo cuando se aplica a imágenes que se ven nada más entrar.
- Un hosting con buen tiempo de respuesta del servidor y caché activada.

### Para el INP

- Quitar plugins y complementos que cargan JavaScript en todas las páginas aunque no se usen.
- Retrasar scripts de terceros que no son imprescindibles al cargar (chats, píxeles, mapas).

### Para el CLS

- Indicar siempre el ancho y el alto de imágenes y vídeos, o reservar su espacio con CSS. Es la [primera recomendación de web.dev para evitar saltos](https://web.dev/articles/optimize-cls).
- Reservar el hueco de banners, avisos de cookies y cualquier elemento que se inserte tarde.

Si tu web está hecha con un maquetador visual, te interesará también este repaso de [errores SEO comunes en Elementor](/blog/errores-seo-comunes-en-elementor/).

## Preguntas frecuentes

### ¿Si mejoro los Core Web Vitals subiré en Google?

No hay garantía. Google los usa, pero prioriza que el contenido sea relevante y útil. Donde más pesan es cuando varias páginas responden igual de bien a una búsqueda.

### ¿Por qué PageSpeed me da una nota distinta cada vez?

La nota de 0 a 100 sale de la simulación de laboratorio, que varía entre pruebas. Los datos de campo, cuando existen, son más estables porque resumen semanas de visitas reales.

### ¿Tengo que llegar a 100 en PageSpeed?

No. Lo importante es que las tres métricas estén en verde para tus usuarios reales. Una web con buenos datos de campo y una nota de 85 está mejor que una con 100 en laboratorio y datos reales en rojo.

## Conclusión

Los Core Web Vitals miden si tu web se siente rápida y estable para quien la usa: que cargue lo importante, que responda al tocar y que no se mueva. Mídelos con datos reales, corrige primero lo que más afecta a tus visitas y acompáñalo de una buena base de [SEO](/blog/que-es-el-seo/) y de un [mantenimiento web](/blog/mantenimiento-web-por-que-es-necesario/) que evite que la web vuelva a engordar con el tiempo.

### ¿Quieres saber cómo están tus Core Web Vitals?

Los mido con datos reales, te digo qué corregir primero y lo optimizo sin tocar tu diseño. [Contáctame](/#contacto).
