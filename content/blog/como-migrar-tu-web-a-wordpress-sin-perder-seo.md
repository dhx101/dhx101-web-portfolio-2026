---
title: Cómo migrar tu web a WordPress sin perder el SEO
description: Cómo migrar una web antigua a WordPress sin perder posicionamiento: mapa de URLs, redirecciones 301, qué revisar antes y después y cuánto mantenerlas.
date: 2026-06-01
updated: 2026-09-18
image: /assets/blog/como-migrar-tu-web-a-wordpress-sin-perder-seo.webp
image_alt: Migración de datos representando el traspaso de una web a WordPress
---

Migrar una web antigua a WordPress es habitual cuando un negocio quiere modernizarse, pero también es uno de los momentos en los que más fácil es perder de golpe años de [SEO](/blog/que-es-el-seo/) acumulado. La web nueva puede ser más bonita y más rápida, y aun así dejar de recibir visitas porque Google no encuentra las páginas que ya conocía. En este post te explico cómo planifico una migración para que eso no pase, apoyándome en lo que recomienda Google.

## Por qué una migración puede hundir tus visitas

Google tiene indexadas las URLs de tu web actual, y cada una acumula señales: enlaces de otras webs, historial y posiciones. Si en la web nueva esas URLs desaparecen o cambian sin avisar, quien llega desde Google o desde un enlace externo se encuentra un error 404, y Google tiene que empezar a descubrir tus páginas casi desde cero.

La propia Google recomienda contar con ayuda de SEO [precisamente al rediseñar o lanzar una web](https://developers.google.com/search/docs/fundamentals/do-i-need-seo), y cuanto antes mejor. Es mucho más barato planificarlo que arreglarlo después.

## Antes de migrar: haz inventario

### 1. Lista todas las URLs de tu web actual

Necesitas saber qué existe antes de moverlo: páginas, entradas del blog, fichas de productos, PDFs e imágenes importantes. Google insiste en que [imágenes, vídeos y otros archivos también cambian de URL](https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes) en una migración y hay que tratarlos igual.

### 2. Identifica qué páginas traen tráfico

En el informe de rendimiento de Search Console verás qué páginas reciben clics desde Google. Esas son las que más cuidado necesitan: si solo pudieras revisar a mano diez URLs, serían esas.

### 3. Anota quién te enlaza

Search Console también te muestra qué webs enlazan a las tuyas. Esos enlaces apuntan a tus URLs antiguas, y la redirección es lo que evita que se pierdan.

### 4. Guarda títulos y descripciones actuales

Aunque vayas a mejorarlos, tenerlos como referencia te permite comparar si algo empeora tras la migración.

## El mapa de redirecciones: la pieza clave

Con el inventario hecho, el paso más importante es el que Google llama mapa de URLs: una tabla que dice, para cada URL antigua, a qué URL nueva debe ir. Su guía sobre [cambios de sitio con cambios de URL](https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes) recomienda redirecciones permanentes desde el servidor, de cada URL antigua a su equivalente nueva.

Lo que cuido en ese mapa:

- **Redirección 301, no 302.** Google explica que [una redirección permanente es una señal de que la página de destino debe ser la canónica](https://developers.google.com/search/docs/crawling-indexing/301-redirects), mientras que una temporal no lo es.
- **Cada URL a su equivalente real.** Mandarlo todo a la página de inicio es tentador, pero quien buscaba tu página de servicios no quiere aterrizar en la portada.
- **Sin cadenas.** Redirige directamente al destino final. Si no hay más remedio, Google recomienda que la cadena tenga idealmente tres saltos como mucho y nunca cinco o más.
- **Enlaces internos actualizados.** Los enlaces de la web nueva deben apuntar ya a las URLs nuevas, no depender de las redirecciones.

Si puedes mantener las mismas URLs en WordPress, mejor que mejor. Con la estructura de enlaces adecuada muchas veces se pueden conservar, y entonces no hay nada que redirigir.

## Durante la migración

- **Mantén lo que funcionaba.** Si una página posicionaba bien con cierto contenido y estructura, la versión nueva debería conservarlo. Cambiar el diseño no obliga a reescribir el contenido que ya funciona.
- **Vigila la velocidad.** Una migración es buen momento para optimizar imágenes y reducir plugins, y también el momento en el que más fácil es empeorarla. Tienes los detalles en [Core Web Vitals](/blog/core-web-vitals-que-son/).
- **Prueba antes de publicar.** Recorre la web nueva y prueba las redirecciones de las páginas importantes antes de abrir al público.

## Después de migrar

1. **Envía el nuevo sitemap XML** en Search Console.
2. **Comprueba a mano las páginas con más tráfico** y sus redirecciones.
3. **Vigila los errores 404** en Search Console durante las semanas siguientes y corrige los que aparezcan.
4. **Ten paciencia con las fluctuaciones.** Google avisa de que es normal que el posicionamiento fluctúe temporalmente mientras vuelve a rastrear e indexar la web. Una caída sostenida, en cambio, suele indicar redirecciones que faltan.
5. **No quites las redirecciones.** Google recomienda mantenerlas el mayor tiempo posible, en general al menos un año, para que pueda trasladar todas las señales a las URLs nuevas.

Si durante la migración también limpias el [SEO On-Page](/blog/seo-on-page/) (títulos, encabezados, imágenes), hazlo con la lista de URLs importantes delante para no romper lo que ya funcionaba.

## Preguntas frecuentes

### ¿Perderé posiciones aunque lo haga bien?

Puede haber fluctuaciones temporales mientras Google procesa los cambios; la propia Google lo advierte. Con un buen mapa de redirecciones, lo normal es recuperar la situación anterior. Los plazos de Google los explico en [cuánto tarda en verse el SEO](/blog/cuanto-tarda-en-verse-resultados-seo/).

### ¿Puedo borrar las redirecciones al cabo de unos meses?

Mejor no. Google recomienda mantenerlas al menos un año, y en la práctica no hay motivo para quitarlas: los enlaces externos antiguos seguirán apuntando a esas URLs.

### ¿Y si cambio también de dominio?

Entonces la planificación es aún más importante: todas las URLs cambian. Además de las redirecciones, Search Console tiene una herramienta de cambio de dirección para avisar a Google del traslado.

## Conclusión

Migrar a WordPress no tiene por qué costar posicionamiento. El error caro no suele ser elegir mal la plataforma, sino no hacer inventario y no mapear bien las redirecciones. Con redirecciones 301 directas, enlaces internos actualizados y un seguimiento de las semanas siguientes, la web nueva hereda lo que había ganado la antigua.

### ¿Vas a migrar tu web y no quieres perder tu SEO?

Hago el inventario de tu web actual y preparo el mapa completo de redirecciones antes de tocar una sola URL. [Contáctame](/#contacto).
