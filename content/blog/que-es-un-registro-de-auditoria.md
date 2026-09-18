---
title: Qué es un registro de auditoría y por qué lo necesitas
description: Qué es un registro de auditoría, qué debe guardar según OWASP, por qué conviene que no bloquee la acción real y cómo lo implementé en un panel interno.
date: 2026-07-06
updated: 2026-09-18
image: /assets/blog/que-es-un-registro-de-auditoria.webp
image_alt: Documentos y registros representando un log de auditoría
---

"¿Quién marcó esta factura como pagada?" Es la típica pregunta que, en un panel con varios administradores, no tiene respuesta si nadie la ha previsto. Un registro de auditoría la responde en segundos. En este post te explico qué es, qué debería guardar según la guía de OWASP, la decisión de diseño que más importa y cómo lo implementé en el [Web Client Portal](https://dhx101-web-client-portal.vercel.app).

## Qué es un registro de auditoría

Es un historial de las acciones relevantes que hacen las personas dentro de una aplicación: quién hizo qué, sobre qué elemento y cuándo. Por ejemplo, crear una factura, cambiar su estado, dar de alta o de baja el acceso de un cliente, o cambiar la conexión de un sitio.

No hay que confundirlo con los registros de errores. Estos cuentan qué ha fallado en el sistema; el de auditoría cuenta qué han decidido las personas. Uno sirve para depurar y el otro para responder preguntas de negocio, resolver dudas con un cliente o detectar un uso indebido.

## Qué debería guardar

La guía de registros de [OWASP](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html), la fundación de referencia en seguridad de aplicaciones web, resume lo esencial: cada evento debe registrar **cuándo, dónde, quién y qué**. En el portal, cada entrada guarda:

- **Quién:** el identificador del usuario que hizo la acción y una copia de su nombre en ese momento.
- **Qué:** una acción concreta con un nombre fijo, como `invoice.status_changed` o `client_access.deleted`, no un texto libre.
- **Sobre qué:** el tipo de elemento (factura, ticket, sitio o usuario) y su identificador.
- **Detalle:** cuando aporta algo, por ejemplo el estado anterior y el nuevo (`PENDING -> PAID`).
- **Cuándo:** la fecha y hora, que la base de datos pone automáticamente.

### Lo que nunca debe guardar

OWASP también enumera lo que no debería acabar en un registro: tokens de acceso, identificadores de sesión, contraseñas o datos personales sensibles. En el portal, cuando se cambia la conexión con el WordPress de un cliente, se registra que se cambió, pero nunca la clave nueva.

## La decisión de diseño más importante: que no bloquee la acción real

El primer instinto al implementarlo es escribir la entrada de auditoría dentro de la misma transacción que la acción, para "garantizar" que nunca se pierde un registro. Es justo lo que decidí no hacer.

Si la auditoría formara parte de la transacción, un problema pasajero al escribirla (una conexión lenta, un fallo puntual) desharía también la acción real. Por ejemplo, una factura que se acaba de marcar como pagada volvería a pendiente solo porque su registro no pudo escribirse. Eso es mucho peor que perder una línea del historial.

Por eso, en el portal la entrada se escribe **después** de que la acción ha tenido éxito, y cualquier error al escribirla se captura sin propagarse:

```ts
await db.invoice.update({ where: { id }, data: { status } })
// la factura ya está actualizada, pase lo que pase después
await logAudit({ actorId, action: 'invoice.status_changed', targetType: 'Invoice', targetId: id, detail: `${previous.status} -> ${status}` })
```

La propia función de auditoría envuelve la escritura en un `try/catch`: si falla, lo anota en los registros de errores y sigue. Perder una entrada pierde "quién lo hizo", no "qué pasó": la factura sigue correctamente pagada.

Es un compromiso consciente. En una aplicación financiera o regulada, donde la trazabilidad es una obligación, lo correcto sería lo contrario. En una herramienta interna de una agencia, que la acción nunca falle por culpa del historial es más importante.

## Detalles que marcan la diferencia

- **Una copia del nombre del autor.** Si luego se elimina esa cuenta, el registro sigue diciendo quién fue. El enlace al usuario se vacía, pero el nombre se conserva.
- **Acciones como texto, no como lista cerrada.** Añadir un tipo de acción nuevo no obliga a cambiar la estructura de la base de datos.
- **Índices pensados para consultar:** por elemento y por fecha, que son las dos preguntas habituales ("qué le ha pasado a esta factura" y "qué ha pasado esta semana").
- **Acceso restringido.** OWASP recomienda limitar quién puede leer los registros. En el portal, la página de auditoría solo la ven los administradores, con paginación.
- **Pruebas:** que se guarden actor, acción, elemento y detalle, que un fallo al escribir nunca lance un error, y que el nombre del autor se conserve aunque se borre su cuenta.

## Preguntas frecuentes

### ¿No basta con los registros del servidor?

No. Los del servidor cuentan peticiones técnicas, no decisiones de negocio, y suelen borrarse al cabo de poco tiempo. El de auditoría vive en la base de datos y se puede consultar desde la propia aplicación.

### ¿Cuánto tiempo hay que guardarlo?

Depende de tus obligaciones y de si guarda datos personales. Lo sensato es decidirlo desde el principio en lugar de guardarlo todo para siempre.

### ¿Tiene sentido en una aplicación pequeña?

Sí. Con dos administradores ya aparecen preguntas de "quién cambió esto". Añadirlo al principio cuesta poco.

## Conclusión

Un registro de auditoría no necesita ser complejo para ser útil: cuándo, quién, qué y sobre qué, sin datos sensibles y con acceso restringido. La decisión clave es su nivel de garantía. En la mayoría de herramientas internas, escribirlo después de la acción y sin poder deshacerla es lo correcto. Es la misma filosofía que sigo con [la cola de emails](/blog/cola-de-emails-con-reintentos-en-nextjs/) y con [los pagos con Stripe](/blog/cobrar-facturas-online-con-stripe-checkout/); tienes el conjunto en [el portal de clientes](/blog/portal-de-clientes-para-agencia-wordpress/).

### ¿Tu panel interno necesita saber quién hace qué?

Diseño registros de auditoría útiles, seguros y que no ponen en riesgo tus operaciones. [Contáctame](/#contacto).
