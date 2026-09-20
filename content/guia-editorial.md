# Guía editorial del blog

Esta guía la usan tanto la automatización de n8n (al proponer temas y redactar
borradores) como cualquier revisión de posts existentes. Si cambias el tono o
las reglas, cámbialo aquí: es la única fuente.

## Quién escribe y para quién

- Escribe **David Huang Xie**, desarrollador web en Alicante: WordPress y Bricks
  Builder, automatización con n8n e IA, SEO técnico e infraestructura.
- Lectores: dueños de negocios locales y pymes que valoran rehacer o mejorar su
  web, y perfiles técnicos que llegan por los posts de desarrollo.
- Objetivo de cada post: resolver de verdad la duda de la búsqueda y, cuando
  encaje, que el lector contacte para un proyecto freelance.

## Voz y tono

- Primera persona, como David: "trabajo", "he visto", "lo que recomiendo".
- Directo y cercano, como un colega que sabe del tema. Sin relleno, sin frases
  de marketing vacías ("en el mundo digital de hoy…").
- Español de España, con gramática y puntuación correctas.
- **Nunca** signos de exclamación. **Nunca** emojis.
- Explica los términos técnicos la primera vez que aparecen, sin paternalismo.
- Usa ejemplos concretos (un restaurante, una clínica, una tienda WooCommerce)
  antes que generalidades.

## Datos y veracidad (no negociable)

- Todo dato, cifra, umbral o afirmación verificable (p. ej. "LCP por debajo de
  2,5 s", "Google sustituyó FID por INP en 2024") lleva **enlace a la fuente
  original**. Se prefiere la documentación oficial cuando existe (Google Search
  Central, web.dev, WordPress, MDN), y después estudios, fabricantes o medios
  solventes. Hay temas de negocio (precios, decisiones, procesos) que ningún
  manual cubre: ahí vale otra fuente, pero siempre la primaria, nunca quien la
  cita de segunda mano, y comprobando el dato en la propia página enlazada.
- Si no hay fuente fiable, no se incluye el dato.
- No inventar casos, clientes, resultados ni porcentajes de David.
- Experiencia real de David que se puede citar:
  - Ángulo Tres (enero–agosto 2026), único perfil técnico de la agencia: mejoró
    la velocidad de carga hasta un 60 % (Core Web Vitals), ahorró 80 €/mes
    sustituyendo ClickUp por Odoo y Brevo por Amazon SES, montó y mantuvo un
    servidor on-premise con Docker (Odoo, n8n, Nextcloud…), desplegó agentes de
    IA y automatizaciones con n8n.
  - Grupo Verko (desde septiembre 2026), desarrollador WordPress: desarrolla
    webs de clientes con WordPress y Bricks Builder y participa en plugins a
    medida. **Sin resultados ni métricas atribuibles todavía**: no inventarlos.
  - Proyectos: Makisu Sushi Petrer, Soleá Creativa, Web Client Portal, WP Admin Desk.
- Describir a David siempre como "desarrollador", nunca como "ingeniero".

## Estructura de un post

1. **Entradilla** (2–3 frases): el problema del lector y qué va a sacar del post.
   Sin encabezado.
2. **Cuerpo** con `##` para secciones y `###` para subsecciones. Párrafos cortos
   (2–4 frases). Listas cuando haya pasos u opciones.
3. **Conclusión** (`## Conclusión`): la idea principal en 2–3 frases, sin repetir
   todo el post.
4. **Cierre de contacto**, siempre con este formato:

   ```markdown
   ### ¿<Pregunta que conecte el tema con un servicio de David>?

   <Una frase sobre cómo lo resuelve David>. [Contáctame](/#contacto).
   ```

- Longitud: **mínimo 900 palabras**, sin máximo. Lo normal son 1.000–1.300; más
  solo si el tema lo exige de verdad, y nunca a base de relleno.
- **Que no sea solo texto**: al menos dos de estos elementos, donde encajen de verdad
  y no por cumplir:
  - una tabla en Markdown (comparativas, opciones con pros y contras, precios…);
  - un aviso en una línea que empiece por `> **Importante:**`;
  - una lista numerada cuando haya pasos que seguir en orden.
- **Portada**: todo post lleva `image` (1200×675, WebP, en `/assets/blog/<slug>.webp`)
  e `image_alt` con el formato "<lo que se ve> representando <la idea del post>".
- Si ayuda, una sección `## Preguntas frecuentes` con 3–4 preguntas reales que la
  gente busca sobre el tema (`###` por pregunta, respuesta de 2–3 frases).

## SEO

- Una **búsqueda objetivo** principal por post, con intención clara (informativa,
  comparativa…). Aparece de forma natural en el título, la entradilla y algún `##`.
- **Título** (`title`): máximo 60 caracteres, con la búsqueda principal al
  principio si es natural.
- **Descripción** (`description`): 140–160 caracteres, dice qué resuelve el post.
- **Enlaces internos**: 3–5 a otros posts del blog relacionados (`/blog/<slug>/`)
  y, si encaja, a `/proyectos/` o `/#contacto`. Con texto de enlace descriptivo,
  nunca "haz clic aquí".
- **Enlaces externos**: las fuentes de los datos (ver arriba).
- No repetir un tema ya cubierto por otro post: si se solapa, enfocar un ángulo
  distinto y enlazar al existente.

## Formato del archivo

Ruta: `content/blog/<slug>.md`. El slug es la URL (`/blog/<slug>/`): minúsculas,
sin tildes ni eñes, palabras separadas por guiones, corto y con la búsqueda
principal. **Nunca se cambia el slug de un post ya publicado.**

```markdown
---
title: Título del post
description: Descripción de 140-160 caracteres.
date: AAAA-MM-DD
image: /assets/blog/<slug>.webp
image_alt: Descripción de lo que se ve en la imagen
---

Entradilla…
```

- `date`: fecha de publicación. En un post ya publicado no se toca.
- `updated`: añadirla (AAAA-MM-DD) solo cuando se revisa el contenido de un post
  publicado; no por cambios menores de erratas.
- `image` e `image_alt` van juntos o no van. Imágenes de Pexels en `assets/blog/`,
  formato WebP, y su autor anotado en `assets/blog/CREDITS.md`.
- Markdown estándar. Bloques de código con triple acento grave y lenguaje.
