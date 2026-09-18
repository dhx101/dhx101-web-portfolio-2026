---
title: Cómo elegir hosting y dominio para tu negocio
description: Guía sin jerga para elegir dominio y hosting para tu negocio: quién debe ser el titular, qué exigir a un hosting y qué errores te pueden costar la web.
date: 2026-05-13
updated: 2026-09-18
image: /assets/blog/como-elegir-hosting-y-dominio.webp
image_alt: Servidores de un centro de datos representando el hosting web
---

Casi todos los negocios con los que hablo llegan con la misma duda: "¿qué hosting contrato?". O ya tienen uno contratado sin saber muy bien por qué ni a nombre de quién está. En este post te explico qué importa de verdad al elegir dominio y hosting, sin jerga, y cuáles son los errores que pueden dejarte sin web el día menos pensado.

## Dominio y hosting son cosas distintas

- **Dominio:** el nombre de tu web (`tunegocio.es`). No se compra para siempre: se registra por periodos y se renueva.
- **Hosting:** el servidor donde vive tu web. Es un contrato aparte, aunque muchos proveedores venden los dos juntos.

Puedes tener el dominio en un proveedor y el hosting en otro sin ningún problema. A veces incluso conviene, para no depender de una sola empresa para todo.

Si eliges un `.es`, el registro lo gestiona [Red.es](https://www.dominios.es/es), la entidad pública del Ministerio para la Transformación Digital. Tú lo contratas a través de un agente registrador, que es quien te cobra y con quien gestionas la renovación.

## Lo más importante: quién es el titular

Antes de fijarte en gigas o en velocidad, asegúrate de una cosa: **el dominio debe estar a tu nombre, no al de la agencia o el desarrollador que te lo gestiona.**

Para dominios como `.com`, la ICANN, el organismo que los coordina, lo deja claro en sus [derechos y responsabilidades del titular](https://www.icann.org/resources/pages/benefits-2013-09-16-en): quien registra el dominio es el único responsable de él, debe mantener sus datos de contacto correctos y actualizados, y responder a su registrador en un plazo de quince días. El `.es` tiene sus propias normas, pero la idea es la misma: si el titular es otra persona, el control del dominio queda en sus manos.

Lo que recomiendo siempre:

- Que el titular del dominio seas tú o tu empresa.
- Que tengas acceso al panel del registrador, aunque no vayas a tocarlo nunca.
- Que la renovación sea automática y con una forma de pago que no caduque sin que te enteres.

## Qué mirar en un hosting

### 1. Que cumpla lo que pide tu web

Si tu web es WordPress, su propia documentación recomienda un servidor con [PHP 8.3 o superior, MySQL 8.0 o MariaDB 10.11 y soporte HTTPS](https://wordpress.org/about/requirements/). Pregúntalo antes de contratar: un hosting con versiones antiguas funciona, pero sin parches de seguridad.

### 2. Certificado HTTPS incluido

Hoy debería venir incluido sin coste. Existen autoridades como [Let's Encrypt](https://letsencrypt.org/about/) que emiten certificados gratuitos y automáticos para cualquier persona que tenga un dominio, y la mayoría de hostings los instalan con un clic. Si un proveedor te cobra aparte por un certificado básico, pregunta por qué.

### 3. Copias de seguridad automáticas y fuera del servidor

No todos los planes incluyen copias, y las que incluyen a veces se guardan en el mismo servidor. La documentación de WordPress recomienda [guardar varias copias en lugares distintos](https://developer.wordpress.org/advanced-administration/security/backup/), no solo en el hosting. Pregunta con qué frecuencia se hacen, cuántas se guardan y cómo se restauran.

### 4. Ubicación y velocidad del servidor

Si tus clientes están en España, un servidor en Europa suele responder más rápido que uno en otro continente. La velocidad del servidor influye en cuánto tarda en aparecer tu web, que es lo que miden los [Core Web Vitals](/blog/core-web-vitals-que-son/).

### 5. Soporte que te atienda

Cuando algo falla a las once de la noche, importa poder hablar con alguien, y en tu idioma si lo necesitas.

## Errores comunes

- **Contratar lo más barato sin mirar qué incluye:** sin copias, con versiones antiguas de PHP o con límites que se quedan cortos en cuanto tu web crece.
- **No saber cuándo caduca el dominio.** Si no se renueva, puedes perderlo, y con él tu web y tu correo.
- **Dejar que un tercero sea el único con acceso** al dominio y al hosting.
- **Tener el correo del negocio en el mismo sitio que todo lo demás sin copias.** Si falla el proveedor, te quedas sin web y sin email a la vez.

## Si ya tienes hosting y quieres cambiar

Cambiar de hosting es habitual y no tiene por qué afectar a tu posicionamiento si mantienes las mismas direcciones de tus páginas. Si además cambian las URLs, necesitarás redirecciones: lo explico en [cómo migrar tu web sin perder el SEO](/blog/como-migrar-tu-web-a-wordpress-sin-perder-seo/).

## Preguntas frecuentes

### ¿Es mejor un .es o un .com?

Si tu clientela es de España, un `.es` es una opción natural y reconocible. Lo más importante es que sea corto, fácil de decir y que esté a tu nombre.

### ¿Cuánto debería costar un hosting para una web pequeña?

Depende de lo que incluya: copias, soporte y recursos. Más que el precio, compara lo que incluye. Hablo de los costes de una web en [cuánto cuesta una página web](/blog/cuanto-cuesta-una-pagina-web-negocio-local/).

### ¿El hosting se encarga del mantenimiento de mi web?

Normalmente mantiene el servidor, no tu WordPress ni tus plugins. Te explico la diferencia en [mantenimiento web](/blog/mantenimiento-web-por-que-es-necesario/).

## Conclusión

No hace falta entender de servidores para elegir bien: hace falta saber qué preguntar y asegurarte de que el control es tuyo. Dominio a tu nombre, hosting con versiones actuales, HTTPS incluido y copias fuera del servidor. El resto importa menos de lo que suelen vender los proveedores.

### ¿Quieres que revise tu hosting y tu dominio?

Reviso a nombre de quién está tu dominio, qué incluye tu hosting y si tus copias sirven de verdad. [Contáctame](/#contacto).
