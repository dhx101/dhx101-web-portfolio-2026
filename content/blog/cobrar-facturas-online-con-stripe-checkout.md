---
title: Cobrar facturas online con Stripe Checkout
description: Cómo integré Stripe Checkout en un panel interno para que los clientes paguen sus facturas online, con verificación de firma del webhook e idempotencia real.
date: 2026-07-03
updated: 2026-09-18
image: /assets/blog/cobrar-facturas-online-con-stripe-checkout.webp
image_alt: Pago online con tarjeta representando un cobro con Stripe Checkout
---

Añadir un botón de "pagar online" a un panel de facturación parece sencillo hasta que piensas en los casos límite: ¿qué pasa si el cliente cierra el navegador justo después de pagar? ¿Y si la confirmación de Stripe llega dos veces? En este post te cuento cómo integré Stripe Checkout en el [Web Client Portal](/proyectos/) resolviendo esos casos desde el diseño, qué dice la documentación de Stripe y cómo lo pruebo.

## Cómo funciona el flujo

1. El cliente pulsa "Pagar ahora" en una factura pendiente.
2. El servidor crea una sesión de Stripe Checkout en modo pago y guarda en ella el identificador de la factura.
3. El cliente paga en la página de Stripe, que se encarga de la tarjeta y de la autenticación bancaria.
4. Stripe devuelve al cliente al panel y, por separado, avisa al servidor mediante un webhook.
5. Solo ese aviso marca la factura como pagada.

El paso 5 es el importante, y es donde se equivoca mucha gente.

## La regla de oro: el navegador no es la fuente de verdad

Es tentador marcar la factura como pagada cuando Stripe devuelve al cliente al panel. Pero esa vuelta solo demuestra que el navegador volvió, no que el pago se completó. Y al revés: el cliente puede pagar y cerrar la pestaña antes de volver.

La propia Stripe lo dice en su guía de [gestión de pedidos con Checkout](https://docs.stripe.com/checkout/fulfillment): no puedes fiarte solo de la página de vuelta, porque no está garantizado que el cliente la visite, y los webhooks son necesarios para asegurarte de procesar todos los pagos.

Por eso, la única fuente de verdad en el portal es el webhook `checkout.session.completed`, que Stripe envía a un endpoint del servidor, pase lo que pase en el navegador. La vuelta del cliente al panel no cambia nada: el estado de la factura solo cambia cuando llega el webhook.

## Verificación de firma: no aceptar cualquier petición

El endpoint del webhook no puede aceptar cualquier petición que diga "este pago se completó". Stripe firma cada evento con un secreto, y su documentación sobre [webhooks](https://docs.stripe.com/webhooks) insiste en verificar esa firma para confirmar que el evento no lo ha enviado ni modificado un tercero. En el portal se hace con la librería oficial, sobre el cuerpo de la petición sin procesar:

```ts
const event = stripe.webhooks.constructEvent(body, signature, webhookSecret)
```

Si la firma no es válida, el endpoint responde con un error y no toca nada. Sin esta comprobación, cualquiera que conociera la URL podría simular pagos.

## Idempotencia: el mismo evento puede llegar dos veces

Stripe avisa de que un endpoint puede recibir ocasionalmente el mismo evento más de una vez. Así que el webhook tiene que ser idempotente: procesar dos veces el mismo evento debe dar el mismo resultado que procesarlo una.

En el portal, antes de actualizar, se comprueba el estado de la factura: si ya está pagada, el evento repetido no hace nada. Además, el identificador de la sesión de Checkout se guarda con restricción de unicidad en la base de datos, así que una misma sesión no puede asociarse a dos facturas.

## Pagos online y pagos manuales, sin conflictos

No todos los clientes pagan con tarjeta. La agencia puede seguir marcando una factura como pagada a mano cuando cobra por transferencia o en efectivo. Los campos de Stripe en la factura son opcionales precisamente por eso: una factura pagada a mano nunca tiene sesión de Checkout, y ambos caminos terminan en el mismo estado.

## Integración opcional: sin clave, sin botón

Stripe solo se activa si existe la clave secreta en las variables de entorno. Sin ella, el botón de pagar no aparece y el resto del panel funciona igual. Es el mismo criterio que sigue el envío de emails, que explico en [la cola de emails con reintentos](/blog/cola-de-emails-con-reintentos-en-nextjs/): ninguna integración externa debería ser obligatoria para que la aplicación arranque.

## Cómo lo pruebo

El webhook tiene pruebas de integración que cubren los cuatro casos que importan:

- Rechaza una petición con firma inválida.
- Marca la factura como pagada con un evento firmado correctamente.
- No hace nada si llega de nuevo un evento de una factura ya pagada.
- Ignora los tipos de evento que no gestiona.

## Lo que mejoraría

Stripe indica que los webhooks a veces llegan con retraso, y sugiere que, cuando el cliente está presente, también se pueda procesar el pedido desde la página de vuelta, con la misma lógica idempotente. Para facturas no es crítico, porque unos segundos de retraso en marcar una factura como pagada no afectan a nadie. En una tienda que entrega algo al instante, sí lo haría.

## Preguntas frecuentes

### ¿Por qué Stripe Checkout y no un formulario de pago propio?

Porque Stripe se encarga de los datos de la tarjeta y de la autenticación bancaria. El portal nunca toca un número de tarjeta, y eso simplifica mucho la seguridad.

### ¿Qué pasa si el webhook falla?

Stripe reintenta el envío automáticamente durante un máximo de tres días, con esperas cada vez más largas. Como el endpoint es idempotente, los reintentos no causan duplicados.

### ¿Esto sirve para una tienda WooCommerce?

La idea sí, pero en WooCommerce lo resuelven los plugins de pasarela. Lo comparo en [WooCommerce o Shopify](/blog/woocommerce-vs-shopify/).

## Conclusión

Cobrar online de forma fiable se reduce a tres reglas: la confirmación la da el servidor mediante el webhook, la firma siempre se verifica y el procesamiento es idempotente. Con eso, un cliente puede pagar su factura desde el propio panel sin depender de que su navegador vuelva correctamente. Tienes el resto del proyecto en [el portal de clientes](/blog/portal-de-clientes-para-agencia-wordpress/).

### ¿Necesitas cobros online en tu propia herramienta?

Integro pagos con Stripe en paneles y aplicaciones, con webhooks verificados y probados. [Contáctame](/#contacto).
