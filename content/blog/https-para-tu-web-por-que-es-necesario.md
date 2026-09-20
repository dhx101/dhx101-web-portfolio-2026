---
title: HTTPS para tu web
description: Descubre por qué necesitas HTTPS en tu sitio web para proteger datos, ganar confianza del usuario y mejorar tu posicionamiento en buscadores.
date: 2026-09-20
image: /assets/blog/https-para-tu-web-por-que-es-necesario.webp
image_alt: Portátil con icono de candado representando la seguridad de una web con HTTPS
---

¿Por qué mi web necesita HTTPS? Es una pregunta que me llega a menudo de dueños de negocios locales con una web que lleva años en línea y funciona. La respuesta no es solo técnica: va de seguridad, de confianza y de posicionamiento. Si tu sitio sigue en HTTP, el navegador ya está avisando a tus visitantes de que no es seguro, aunque no manejes datos bancarios.

## Qué es HTTPS y por qué debería importarte

HTTPS (HyperText Transfer Protocol Secure) cifra la comunicación entre el navegador del usuario y tu servidor. Sin él, cualquiera que comparta red con tu visitante —el Wi-Fi de una cafetería, por ejemplo— puede escuchar esa conversación: HTTPS «impide que los intrusos escuchen de forma pasiva las comunicaciones entre tu web y tus usuarios» ([web.dev](https://web.dev/articles/why-https-matters)).

El mito más extendido es que HTTPS solo hace falta si cobras pagos o pides contraseñas. La documentación de Google lo desmonta: cada petición HTTP sin proteger puede revelar información sobre el comportamiento y la identidad de tus usuarios ([web.dev](https://web.dev/articles/why-https-matters)). Leer un artículo sobre una dolencia en una web sin cifrar ya expone algo privado, aunque no se rellene ningún formulario.

Además, las funciones modernas del navegador —grabar audio o usar la cámara con `getUserMedia()`, funcionar sin conexión con service workers— solo están disponibles bajo HTTPS ([web.dev](https://web.dev/articles/why-https-matters)). Si algún día quieres cualquiera de ellas, el punto de partida es este.

## Cómo saber si tu web tiene HTTPS

La comprobación rápida son dos cosas en la barra del navegador:

1. Que la dirección empiece por `https://`.
2. Que no aparezca el aviso «No es seguro» junto a ella.

Pero que la página cargue por HTTPS no significa que esté bien. Lo que suele fallar es el **contenido mixto**.

> **Importante:** el contenido mixto (recursos HTTP dentro de una página HTTPS) es el error más común al migrar. Si una imagen, un script o una hoja de estilos se cargan por HTTP, el navegador los bloquea o avisa al usuario, y la página se ve rota.

Para detectarlo, abre las herramientas de desarrollador (F12), ve a la pestaña **Console** y busca errores que contengan *Mixed Content*. Si gestionas el SEO del sitio, conviene además repasar la indexación después del cambio: lo cuento en [cómo migrar tu web a WordPress sin perder SEO](/blog/como-migrar-tu-web-a-wordpress-sin-perder-seo/).

## Cómo configurar HTTPS correctamente

No basta con instalar un certificado. Una implementación a medias empeora la experiencia y complica el SEO. El proceso, según la guía de Google ([web.dev](https://web.dev/articles/enable-https)), es este:

1. Genera un par de claves RSA de 2048 bits: `openssl genrsa -out www.ejemplo.com.key 2048`.
2. Crea la solicitud de firma de certificado (CSR) con los metadatos correctos, incluyendo el nombre de dominio exacto.
3. Envía la CSR a una autoridad de certificación. Let's Encrypt emite certificados gratuitos, válidos por defecto 90 días y renovables de forma automática ([Let's Encrypt](https://letsencrypt.org/docs/faq/)).
4. Instala el certificado firmado en el servidor, fuera del directorio público.
5. Redirige de HTTP a HTTPS con un **301 (Moved Permanently)**, para indicar a buscadores y navegadores que la versión segura es la canónica ([web.dev](https://web.dev/articles/enable-https)).
6. Activa la cabecera **Strict-Transport-Security** (HSTS) para que el navegador use HTTPS siempre, sin pasar por la redirección.
7. Marca todas las cookies con la bandera `Secure`.

> **Importante:** el punto 7 no es opcional. Si una cookie de sesión viaja en texto plano por HTTP, la seguridad de toda la sesión del usuario se pierde ([web.dev](https://web.dev/articles/enable-https)).

## Qué pasa si tu web sigue en HTTP

El coste va más allá de lo técnico:

- **El navegador marca tu sitio como «no seguro»**, y eso lo ve cualquier cliente que llegue desde Google.
- **Google usa HTTPS como señal positiva de calidad** en los resultados de búsqueda, y lo anunció en agosto de 2014 ([Google Search Central](https://developers.google.com/search/blog/2014/08/https-as-ranking-signal)). No te va a colocar el primero, pero es una desventaja gratuita frente a tu competencia.
- Te quedas fuera de las funciones modernas del navegador mencionadas arriba.
- Cada visita revela a terceros qué está leyendo tu cliente en tu web.

## Tabla comparativa: HTTP frente a HTTPS

| Característica | HTTP | HTTPS |
|----------------|------|-------|
| Cifrado de datos | No | Sí |
| Aviso del navegador | «No es seguro» | Sin aviso |
| APIs modernas (cámara, service workers) | No disponibles | Disponibles |
| Señal de calidad para Google | No la tiene | Sí, desde 2014 |
| Cookies de sesión | Viajan en texto plano | Protegidas con `Secure` |

## Preguntas frecuentes

### ¿Es necesario pagar por un certificado HTTPS?

No. Let's Encrypt emite certificados gratuitos y automatizables ([Let's Encrypt](https://letsencrypt.org/docs/faq/)), y Google lleva años recomendando ese camino a quien aún no ha migrado ([Google Search Central](https://developers.google.com/search/blog/2018/12/why-how-to-secure-your-website-https?hl=es-419)). El precio ya no es una excusa.

### ¿Cambiar a HTTPS perjudica mi SEO?

No, si lo haces bien. Google trata HTTPS como señal positiva desde 2014 ([Google Search Central](https://developers.google.com/search/blog/2014/08/https-as-ranking-signal)) y la propia guía de migración pide redirecciones 301 hacia la versión segura, que es la canónica ([web.dev](https://web.dev/articles/enable-https)). El riesgo no está en el cambio, sino en hacerlo sin redirigir.

### ¿Puedo tener HTTPS sin cambiar de hosting?

Casi siempre sí. La mayoría de proveedores con cPanel, y plataformas como Cloudflare, Vercel o Netlify, activan el certificado desde el panel en unos minutos. Si el tuyo te lo cobra aparte o no lo ofrece, es señal de que toca moverse: lo explico en [cómo elegir hosting y dominio para tu negocio](/blog/como-elegir-hosting-y-dominio/).

### ¿Y si mi web tiene enlaces internos mal escritos?

Ahí es donde aparece el contenido mixto. Si tienes URLs absolutas del tipo `http://tudominio.com/imagen.jpg` escritas en el contenido o en la plantilla, cámbialas por rutas relativas (`/imagen.jpg`) o por su versión `https://`. Revisarlo entra dentro del [mantenimiento web](/blog/mantenimiento-web-por-que-es-necesario/) que todo sitio necesita.

## Conclusión

HTTPS no es una mejora opcional: es el mínimo que se le pide hoy a cualquier web. Protege a quien te visita, evita que el navegador espante a tus clientes con un aviso y suma una señal de calidad para Google. Si tu sitio sigue en HTTP, es de las cosas más baratas y rápidas que puedes arreglar.

### ¿Quieres migrar a HTTPS sin romper tu posicionamiento?

Me encargo del certificado, de las redirecciones 301 y de dejar limpio el contenido mixto para que no pierdas tráfico por el camino. [Contáctame](/#contacto).
