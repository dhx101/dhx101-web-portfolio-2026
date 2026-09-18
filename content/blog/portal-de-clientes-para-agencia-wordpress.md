---
title: Por qué construí un portal para una agencia WordPress
description: Por qué desarrollé un portal donde los clientes de una agencia WordPress ven el estado de su web y pagan sus facturas online, y qué lo hizo fiable.
date: 2026-07-24
updated: 2026-09-18
image: /assets/blog/portal-de-clientes-para-agencia-wordpress.webp
image_alt: Panel de control con métricas representando un portal de clientes
---

Cualquiera que gestione varias webs WordPress para clientes conoce el problema: la información sobre cada una (si está caída, si tiene actualizaciones pendientes, si la factura del mes está pagada) acaba repartida entre el correo, una hoja de cálculo y la memoria de quien lleva la cuenta. Funciona con dos o tres clientes y deja de funcionar en cuanto hay diez. Lo viví como único perfil técnico de una agencia, y por eso construí el [Web Client Portal](/proyectos/). En este post te cuento qué problema resuelve, cómo está hecho y las decisiones que lo hicieron fiable.

## El problema concreto

Una agencia que mantiene WordPress para varios clientes necesita responder cada día a preguntas como:

- ¿Qué webs tienen actualizaciones de WordPress, plugins o temas pendientes?
- ¿Alguna ha dejado de responder?
- ¿Qué facturas siguen sin pagar?
- ¿Hay tickets de soporte abiertos que llevan días sin respuesta?

Sin una herramienta que lo centralice, cada pregunta obliga a entrar web por web o a confiar en que alguien se acuerde de mirar. Ninguna de las dos opciones escala.

## Qué hace el portal

El portal tiene dos tipos de usuario, administrador y cliente, y cada uno ve cosas distintas.

**La agencia** ve un panel de webs que necesitan atención: no la lista completa, sino solo las que tienen un problema real. Desde ahí gestiona sitios, tickets de soporte, facturas y accesos de sus clientes, y puede consultar un registro de quién hizo cada cambio.

**Cada cliente** entra a su propio panel y ve el estado de su web, sus tickets y su historial de facturas, que puede **pagar online con Stripe** sin tener que pedir un número de cuenta por email. Si tiene tienda, recibe además un resumen semanal por email.

## Cómo sabe el estado de cada web

El portal se conecta con cada WordPress a través de un plugin propio, WP Admin Desk, que ofrece un pequeño API con la versión de WordPress, los plugins y temas con actualizaciones pendientes y, si la web usa WooCommerce, los pedidos pendientes y los productos con poco stock.

Un proceso programado sincroniza esos datos cada día, así que el panel refleja el estado real y no lo que alguien recuerde. Y aquí hay una decisión que marca la diferencia: **el portal solo avisa por email cuando una web empeora**, no en cada sincronización mientras el mismo problema sigue ahí. Guarda el último estado sobre el que avisó y compara. Eso evita la fatiga de alertas, que es lo que hace que la gente deje de leer los avisos.

## Las decisiones técnicas que más importaron

### El navegador nunca confirma un pago

Una factura se marca como pagada solo cuando Stripe lo confirma mediante un webhook firmado, nunca cuando el cliente vuelve del pago. El webhook es idempotente, porque Stripe avisa en su [documentación de webhooks](https://docs.stripe.com/webhooks) de que un mismo evento puede llegar más de una vez. Lo cuento en detalle en [cómo cobrar facturas con Stripe Checkout](/blog/cobrar-facturas-online-con-stripe-checkout/).

### Un email fallido no es un email perdido

Si el proveedor de correo falla, el email se queda en una cola con reintentos espaciados en lugar de perderse. Te lo explico, con sus límites, en [la cola de emails con reintentos](/blog/cola-de-emails-con-reintentos-en-nextjs/).

### Saber quién hizo qué

Cada acción administrativa relevante queda en un [registro de auditoría](/blog/que-es-un-registro-de-auditoria/), escrito sin poner en riesgo la acción principal.

### Una base de datos preparada para producción

El proyecto empezó con SQLite y pasó a PostgreSQL antes de desplegarse en Vercel. Te cuento por qué en [de SQLite a Postgres](/blog/de-sqlite-a-postgres-por-que-migre-mi-base-de-datos/).

## Seguridad

Un portal con facturas y datos de clientes tiene que cuidar el acceso:

- **Bloqueo tras intentos fallidos:** 15 minutos de bloqueo después de 5 intentos de acceso erróneos.
- **Recuperación de contraseña segura:** un enlace de un solo uso que caduca en una hora y que siempre muestra el mismo mensaje, exista o no la cuenta, para que nadie pueda usarlo para averiguar qué emails están registrados. Es lo que recomienda la [guía de OWASP sobre recuperación de contraseñas](https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html).
- **Contraseñas cifradas** con bcrypt y sesiones en cookies protegidas.
- **Procesos programados protegidos** con una clave secreta, para que nadie pueda lanzarlos desde fuera.

## Cómo está hecho

Next.js 16, TypeScript, Prisma y PostgreSQL, con Stripe para los pagos y Resend para el correo, desplegado en Vercel. Tiene pruebas automáticas de tres tipos: unitarias, de integración (pagos, cola de emails y auditoría) y de extremo a extremo con Playwright, que recorren el acceso, el panel del cliente y la gestión de facturas como lo haría un usuario real.

## Preguntas frecuentes

### ¿Por qué no usar una herramienta existente de gestión de webs?

Es una opción válida para muchas agencias. El objetivo aquí era juntar en un mismo sitio el estado de cada web, el soporte, la facturación con pago online y un acceso propio para cada cliente. Es un proceso de negocio concreto, y ese es justo el caso en el que compensa hacer algo a medida, como explico en [WordPress o código a medida](/blog/wordpress-elementor-vs-codigo-a-medida/).

### ¿Sirve para cualquier agencia?

La idea sí. Los detalles, como qué datos sincronizar o cuándo avisar, dependen de cómo trabaje cada agencia.

## Conclusión

El portal nació de un problema real: demasiadas webs, demasiada información dispersa y avisos que llegaban tarde o no llegaban. La solución fue centralizarlo todo, avisar solo cuando importa y cuidar los detalles que hacen fiable una herramienta: pagos confirmados por el servidor, emails que no se pierden y un registro de quién hizo qué.

### ¿Gestionas WordPress para varios clientes y te suena este problema?

Construyo herramientas a medida para agencias y negocios, pensadas para su forma de trabajar. [Contáctame](/#contacto).
