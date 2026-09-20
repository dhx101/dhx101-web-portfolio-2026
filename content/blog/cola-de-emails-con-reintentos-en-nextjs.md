---
title: Cola de emails con reintentos en Next.js: no pierdas avisos
description: Cómo monté una cola de emails con reintentos y espera exponencial en Next.js y Postgres para no perder notificaciones cuando falla el proveedor de correo.
date: 2026-06-29
updated: 2026-09-18
image: /assets/blog/cola-de-emails-con-reintentos-en-nextjs.webp
image_alt: Bandeja de entrada de correo representando el envío de notificaciones
---

Cuando un email de notificación falla en producción (el proveedor está caído, hay un límite de envíos temporal o la red tarda demasiado), lo más habitual es que ese email simplemente se pierda. En un panel donde el email es la forma en la que un cliente se entera de que tiene una factura nueva o de que su web tiene un problema, eso no es aceptable. En este post te cuento cómo lo resolví en el [Web Client Portal](/proyectos/), con sus decisiones, sus límites y lo que haría distinto.

## El problema concreto

Al principio, enviar un email era una llamada directa a la API del proveedor (Resend) en el momento de la acción: crear una factura, responder a un ticket, restablecer una contraseña. Si esa llamada fallaba, el email se perdía para siempre. La factura sí se había creado, pero el cliente no se enteraba.

## La solución: una cola de envío en la base de datos

Ahora, cada email se guarda primero como una fila en una tabla `EmailJob` de Postgres, con destinatario, asunto, texto, número de intentos, estado y fecha del próximo intento. A partir de ahí:

1. **Se intenta enviar en el momento.** Si Resend responde bien, el trabajo queda como `SENT` y listo. Es el caso normal.
2. **Si falla, se queda en la cola como `PENDING`** con una fecha para el siguiente intento.
3. **Un cron recorre la cola** y reintenta los trabajos pendientes cuya espera ya ha pasado.
4. **Tras 8 intentos fallidos, se rinde:** el trabajo pasa a `FAILED` y se registra para revisarlo a mano, en lugar de reintentar para siempre un email que nunca va a llegar.

La regla de oro: **la acción de negocio nunca depende del email.** Crear una factura no falla ni se deshace porque el correo no salga. Un fallo de email nunca debe bloquear algo que ya se ha hecho bien.

La idea se inspira en el [patrón outbox](https://microservices.io/patterns/data/transactional-outbox.html), aunque no es la versión transaccional clásica: en esta, el mensaje se guarda en la misma transacción que el cambio de negocio. Aquí se guarda justo después, que para notificaciones es suficiente.

## Espera exponencial, con límite

Cada fallo aumenta la espera antes del siguiente intento: 2 minutos, 4, 8, 16… La espera se dobla en cada intento, con un tope de 12 horas, para que una caída larga del proveedor no separe los intentos días enteros.

Esto evita dos problemas a la vez: no saturar a un proveedor que ya tiene problemas y no dejar un email esperando indefinidamente.

## Por qué no una cola externa

Para el volumen de este proyecto, montar infraestructura de colas aparte (SQS, RabbitMQ, Redis) era desproporcionado. Una tabla en la misma base de datos Postgres que ya usa la aplicación, más un cron, resuelve lo que importa, que es no perder emails ante fallos temporales, sin añadir otra pieza que mantener y vigilar.

## El límite real: el cron de Vercel

Aquí va la parte honesta. En el plan gratuito de Vercel, [los cron solo pueden ejecutarse una vez al día](https://vercel.com/docs/cron-jobs/usage-and-pricing), con una precisión de más o menos una hora, y el cron de la cola está programado así: una vez al día. Por eso, aunque la espera de un email fallido sea de minutos, su siguiente intento llega cuando se ejecuta el cron.

Funciona bien porque el primer intento se hace en el momento, así que en condiciones normales el email sale a la primera. Pero si Resend cae una hora, los emails afectados no se envían en cuanto vuelve: se envían en la siguiente ejecución del cron. Para reintentar más a menudo habría que subir de plan o llamar al endpoint del cron desde otro programador, como un flujo de n8n, con la misma clave secreta.

## Seguridad y pruebas

- **El cron está protegido:** el endpoint solo responde si la petición trae la clave secreta del cron. Nadie puede forzar reenvíos desde fuera.
- **Sin configurar, no rompe nada:** si no hay clave de Resend (por ejemplo, en local), los emails se escriben en la consola en lugar de enviarse, y la aplicación funciona igual.
- **Pruebas de integración** que cubren los casos importantes: envío correcto a la primera, fallo que se queda pendiente, trabajos cuya espera aún no ha pasado, reintento que acaba bien y el abandono tras el máximo de intentos.
- **Alertas sin ruido:** el sistema de errores solo avisa cuando un email se da por perdido, no en cada reintento.

## Preguntas frecuentes

### ¿Por qué no reintentar al momento varias veces seguidas?

Porque si el proveedor está caído, tres intentos en un segundo fallan los tres. Espaciar los intentos da tiempo a que el servicio se recupere.

### ¿Qué pasa con un email que llega a `FAILED`?

Queda registrado en la base de datos para revisarlo. Puede indicar un problema que no se arregla solo, como una dirección de correo mal escrita.

### ¿Sirve este patrón para algo más que emails?

Sí: cualquier llamada a un servicio externo que no deba bloquear la acción principal, como avisos por webhook o sincronizaciones.

## Conclusión

Guardar cada email en una cola antes de enviarlo convierte un fallo del proveedor en un retraso, no en un aviso perdido. Con un primer intento inmediato, reintentos espaciados y un límite claro, cubre lo importante sin infraestructura extra. Es la misma filosofía del [cobro de facturas con Stripe](/blog/cobrar-facturas-online-con-stripe-checkout/) y del [registro de auditoría](/blog/que-es-un-registro-de-auditoria/): los efectos secundarios nunca rompen la acción principal. Tienes el contexto del proyecto en [el portal de clientes](/blog/portal-de-clientes-para-agencia-wordpress/).

### ¿Tu aplicación pierde notificaciones cuando algo falla?

Te ayudo a diseñar colas, reintentos y alertas para que un fallo externo no se convierta en un cliente sin avisar. [Contáctame](/#contacto).
