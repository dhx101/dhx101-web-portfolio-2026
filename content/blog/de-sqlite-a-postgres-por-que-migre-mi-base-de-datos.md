---
title: De SQLite a Postgres: por qué migré la base de datos
description: Por qué migré de SQLite a PostgreSQL antes de desplegar mi portal de clientes en Vercel, qué dice la documentación oficial y qué tuve que cambiar en Prisma.
date: 2026-07-09
updated: 2026-09-18
image: /assets/blog/de-sqlite-a-postgres-por-que-migre-mi-base-de-datos.webp
image_alt: Servidores de base de datos representando una migración de base de datos
---

Empecé a construir el [Web Client Portal](/proyectos/) con SQLite porque, para desarrollar en local, es lo más simple que existe: un único archivo, sin servidor que levantar y sin configuración. Pero antes de desplegarlo en producción en Vercel tuve que migrarlo a PostgreSQL. En este post te cuento por qué, qué dicen la documentación de SQLite, de Vercel y de Prisma, y qué cambios concretos hice.

## Por qué SQLite es perfecto para empezar

SQLite no es una base de datos "de juguete". Su propia documentación explica que [no compite con las bases de datos cliente/servidor, sino con `fopen()`](https://www.sqlite.org/whentouse.html): está pensada como almacenamiento local para una aplicación, no como un repositorio compartido.

Para la primera fase del portal eso encajaba perfectamente:

- **Cero infraestructura:** la base de datos es un archivo junto al proyecto.
- **Arranque instantáneo,** ideal para iterar rápido en local.
- **Perfecta para prototipar** el modelo de datos antes de comprometerse con nada.

## Por qué no sirve en producción en Vercel

El problema no es SQLite, sino dónde se ejecuta el código. En Vercel, cada petición la atiende una función serverless, y la documentación de Vercel es clara: esas funciones tienen [un sistema de archivos de solo lectura, con un espacio temporal escribible en `/tmp`](https://vercel.com/docs/functions/runtimes). Un archivo de base de datos necesita escribirse de forma duradera, y ahí no puede.

Además, Vercel escala creando varias instancias de la función a la vez. La lista de comprobación de SQLite para elegir motor lo deja claro: si los datos están separados de la aplicación por una red, o si hay muchos procesos escribiendo a la vez, conviene una base de datos cliente/servidor. Un entorno serverless cumple las dos condiciones.

PostgreSQL, en cambio, es un servidor independiente al que cualquier instancia de la función se conecta por red, da igual dónde se ejecute.

## Qué cambié con Prisma

El proyecto usa Prisma como ORM (la capa que traduce el código a consultas de base de datos), y eso hizo la migración mucho menos dolorosa que reescribir SQL a mano. Pero no fue cambiar una línea y listo:

- **Cambiar el proveedor** del `datasource` de `sqlite` a `postgresql` en el esquema.
- **Empezar un historial de migraciones nuevo.** La documentación de Prisma avisa de que [no se puede cambiar de proveedor de base de datos automáticamente](https://www.prisma.io/docs/orm/prisma-migrate/understanding-prisma-migrate/limitations-and-known-issues): las migraciones son archivos SQL específicos de cada motor, así que hay que borrar las antiguas y generar un historial nuevo.
- **Revisar los tipos.** SQLite es más permisivo con los tipos que Postgres, así que conviene repasar fechas, booleanos y valores por defecto.
- **Conectar con el adaptador de Postgres** (`@prisma/adapter-pg`) usando la cadena de conexión de la base de datos gestionada.

Como el proyecto todavía no tenía datos reales de clientes, no hubo que migrar datos, solo la estructura. Ese es precisamente el momento barato para hacerlo.

## Qué más hizo falta para desplegar

Además del esquema, el cambio a Postgres tocó otras piezas del proyecto:

- **Una sola migración inicial.** Las cuatro migraciones que había acumulado con SQLite se sustituyeron por una migración inicial nueva para Postgres.
- **Los datos de ejemplo.** El script que carga los datos de prueba (el *seed*) necesitó ajustes para el motor nuevo.
- **Migraciones automáticas en cada despliegue.** Añadí un script de build para Vercel que aplica las migraciones pendientes antes de cada compilación, para que la base de datos de producción nunca quede por detrás del código.
- **Variables de entorno.** El ejemplo de configuración pasó de apuntar a un archivo (`file:./dev.db`) a una cadena de conexión de PostgreSQL.

## La lección general

Elegir la base de datos más cómoda para desarrollar rápido en local es una decisión razonable, siempre que sepas desde el principio que no es la misma decisión que la de producción. Lo importante es planificar el cambio antes de que el proyecto dependa de datos reales de clientes, no después, cuando ya hay que migrar información que no se puede perder.

Si estás empezando un proyecto parecido, mi recomendación es sencilla: si vas a desplegar en serverless, empieza directamente con la base de datos de producción o, como mínimo, con el mismo motor en local.

## Preguntas frecuentes

### ¿Entonces SQLite no sirve para una web?

Sí sirve, en el contexto adecuado. La propia documentación de SQLite dice que funciona bien como base de datos de muchas webs, pero recomienda una cliente/servidor si la web tiene mucha escritura o necesita varios servidores.

### ¿Hay que borrar las migraciones antiguas?

Si cambias de motor, sí: Prisma no puede reutilizarlas porque son SQL específico de cada base de datos. Por eso es mucho más fácil hacerlo antes de tener datos en producción.

### ¿Qué pasa si ya tienes datos en SQLite?

Entonces, además de la estructura, hay que exportar y transformar los datos, y comprobar que nada se pierde por el camino. Es más trabajo, y por eso conviene decidirlo pronto.

## Conclusión

SQLite fue la herramienta adecuada para arrancar y Postgres la adecuada para producción en Vercel. El cambio fue sencillo porque lo hice antes de tener datos reales y porque Prisma abstrae buena parte del trabajo, aunque obliga a empezar un historial de migraciones nuevo. Lo que construí después sobre esa base lo cuento en [la cola de emails con reintentos](/blog/cola-de-emails-con-reintentos-en-nextjs/), [el cobro de facturas con Stripe](/blog/cobrar-facturas-online-con-stripe-checkout/) y [el portal de clientes](/blog/portal-de-clientes-para-agencia-wordpress/).

### ¿Estás construyendo algo que vas a desplegar en serverless?

Te ayudo a elegir la base de datos y la arquitectura adecuadas desde el principio, antes de que cambiarlas sea caro. [Contáctame](/#contacto).
