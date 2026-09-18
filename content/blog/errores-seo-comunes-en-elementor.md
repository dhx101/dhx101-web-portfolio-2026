---
title: Errores de SEO más comunes en webs hechas con Elementor
description: Los errores de SEO que más se repiten en webs hechas con WordPress y Elementor, qué dice Google de cada uno y cómo corregirlos sin rehacer el diseño.
date: 2026-06-24
updated: 2026-09-18
image: /assets/blog/errores-seo-comunes-en-elementor.webp
image_alt: Pantalla mostrando el diseño de una página web hecha con Elementor
---

Elementor es una herramienta muy buena para maquetar rápido, y gran parte de mis primeros proyectos para clientes están hechos con ella. Pero esa misma rapidez hace que ciertos errores de [SEO On-Page](/blog/seo-on-page/) se cuelen sin que nadie se dé cuenta: todo se ve bien en pantalla y, por debajo, la web carga lenta o Google no entiende qué ofreces. Estos son los errores que más conviene revisar, qué dice Google de cada uno y cómo corregirlos sin tocar tu diseño.

## 1. Imágenes pesadas subidas tal cual

Es el error más frecuente: fotos subidas directamente desde el móvil o la cámara, de varios megas cada una, a veces usadas en un fondo que se ve a 400 píxeles de ancho.

Cada imagen de más es tiempo de carga, y la imagen grande de la cabecera suele ser el elemento que decide tu LCP, la métrica de carga de los [Core Web Vitals](/blog/core-web-vitals-que-son/).

**Cómo corregirlo:** redimensiona las imágenes al tamaño en que se muestran, conviértelas a WebP y comprime antes de subir. En una web ya hecha, un plugin de optimización puede convertir y comprimir la biblioteca existente.

## 2. Carga diferida en la imagen principal

La carga diferida (*lazy loading*) retrasa las imágenes hasta que vas a verlas. Es útil más abajo en la página, pero es mala idea en la imagen que se ve nada más entrar. Un análisis de web.dev con datos reales encontró que [las webs que usan lazy loading tienden a tener peor LCP](https://web.dev/articles/lcp-lazy-loading), también en WordPress.

**Cómo corregirlo:** asegúrate de que la imagen principal de cada página no se cargue en diferido. Muchas configuraciones de optimización lo aplican a todas las imágenes sin distinguir.

## 3. Animaciones de entrada en lo más importante

Las animaciones de aparición (fundido, deslizamiento) quedan bonitas, pero tienen un coste escondido. Según la [definición oficial del LCP](https://web.dev/articles/lcp), los elementos con opacidad 0 no cuentan como contenido visible. Si tu titular o tu imagen principal empiezan invisibles para aparecer con un fundido, el navegador no los da por pintados hasta que termina la animación.

**Cómo corregirlo:** quita las animaciones de entrada de la cabecera y del primer bloque visible. Resérvalas para elementos secundarios más abajo.

## 4. Texto alternativo vacío

Elementor no obliga a rellenar el texto alternativo al subir una imagen, así que muchas webs acaban con decenas de imágenes sin él. Según la documentación de [Google Imágenes](https://developers.google.com/search/docs/appearance/google-images), el texto alternativo es el atributo más importante para que Google entienda de qué trata una imagen, y además es imprescindible para quien usa un lector de pantalla.

**Cómo corregirlo:** repasa la biblioteca de medios y describe cada imagen relevante como se la describirías a alguien por teléfono. Las decorativas pueden quedarse sin descripción.

## 5. Encabezados elegidos por su tamaño

En Elementor puedes elegir la etiqueta de cada encabezado (H1, H2, H3…) independientemente de su aspecto. Lo habitual es elegirla por cómo se ve: un H1 porque "queda grande", un H4 porque "queda pequeño".

Aquí conviene desmontar un mito: Google explica en su [guía de SEO](https://developers.google.com/search/docs/fundamentals/seo-starter-guide) que, para su buscador, no importa el orden de los encabezados y no hay un número ideal. El problema real es otro: una estructura desordenada dificulta la lectura a las personas, sobre todo a quien usa un lector de pantalla.

**Cómo corregirlo:** elige la etiqueta por su función (un H1 con el tema de la página, H2 para las secciones) y ajusta el tamaño visual con el estilo, no con la etiqueta.

## 6. Demasiados complementos de widgets

Cada paquete de widgets extra para Elementor suele añadir su propio CSS y JavaScript, y muchos lo cargan en todas las páginas aunque solo uses uno de sus widgets. Acumular varios es una causa habitual de webs lentas y de mala respuesta al tocar, que es lo que mide el INP.

**Cómo corregirlo:** haz inventario de qué widgets usas de verdad y de qué paquete sale cada uno. A menudo se pueden sustituir por los nativos de Elementor y desinstalar el complemento entero.

## 7. URLs que nadie revisó

WordPress genera la URL a partir del título: con la estructura de enlaces por "nombre de la entrada", el [título se convierte en la URL](https://wordpress.org/documentation/article/customize-permalinks/). Si publicas con un título provisional ("pagina-nueva-2") y luego lo cambias, la URL se queda como estaba.

Google recomienda [URLs con palabras descriptivas](https://developers.google.com/search/docs/crawling-indexing/url-structure), en el idioma de tu público.

**Cómo corregirlo:** revisa la URL antes de publicar. Si cambias una que ya tiene visitas, pon una redirección 301 a la nueva; lo explico en [cómo migrar tu web sin perder el SEO](/blog/como-migrar-tu-web-a-wordpress-sin-perder-seo/).

## Cómo revisar tu web en una tarde

1. Pasa las páginas principales por PageSpeed Insights y mira qué elemento marca como LCP.
2. Revisa la biblioteca de medios: peso de las imágenes y texto alternativo.
3. Recorre cada página con el inspector del navegador para ver la estructura de encabezados.
4. Haz inventario de plugins y complementos, y quita lo que no uses.
5. Repasa las URLs de las páginas importantes.

## Preguntas frecuentes

### ¿Elementor es malo para el SEO?

No. Se puede tener una web rápida y bien posicionada con Elementor. Los problemas vienen de cómo se usa: imágenes, animaciones y complementos acumulados. Si te planteas el cambio, comparo opciones en [WordPress con Elementor o código a medida](/blog/wordpress-elementor-vs-codigo-a-medida/).

### ¿Tengo que rehacer mi web para corregir esto?

Casi nunca. Todos estos errores se corrigen sobre la web existente sin cambiar el diseño que ves.

### ¿Cada cuánto conviene revisarlo?

Cada vez que añades páginas o plugins. Con el tiempo, las webs tienden a acumular peso si nadie las vigila.

## Conclusión

Elementor no es el problema: lo son las imágenes sin optimizar, las animaciones en lo más visible, los complementos que se acumulan y los detalles que nadie revisa. Corregirlos no exige rehacer tu web y suele notarse enseguida en la velocidad y en cómo Google entiende tus páginas.

### ¿Tu web de Elementor tiene alguno de estos problemas?

Reviso tu web, corrijo estos errores y la dejo más rápida sin tocar el diseño que ya te gusta. [Contáctame](/#contacto).
