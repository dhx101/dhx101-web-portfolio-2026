---
title: Tu hosting avisa de que PHP está obsoleto: qué hacer
description: Qué significa el aviso de PHP obsoleto, qué versión elegir para WordPress y el paso a paso para actualizarla de forma segura, sin romper tu web.
date: 2026-09-19
---

Te llega un correo del hosting, o un aviso en el escritorio de WordPress: tu versión de PHP está obsoleta. Suena a tecnicismo que se puede dejar para otro día, pero no conviene. PHP es el lenguaje en el que está hecho WordPress, y su versión la decide el servidor, no tu web. Si se queda atrás, tu web va más lenta, es menos segura y llega un momento en que ni siquiera puede actualizarse. La buena noticia es que el cambio suele ser sencillo si sigues un orden.

## Qué significa que PHP esté obsoleto

Cada versión de PHP tiene una vida limitada: las nuevas traen mejoras de rendimiento y de seguridad que las antiguas no tienen, y con el tiempo WordPress deja de soportar las más viejas. Es lo que acaba de pasar con PHP 7.2 y 7.3: el equipo de WordPress anunció que [WordPress 7.0 deja de ser compatible con PHP 7.2 y 7.3](https://make.wordpress.org/core/2026/01/09/dropping-support-for-php-7-2-and-7-3/), y la versión mínima pasa a ser PHP 7.4.

Esto tiene una consecuencia que mucha gente no ve venir: las webs que siguen en PHP 7.2 o 7.3 se quedan en la rama 6.9 de WordPress y no pueden pasar a la 7.0. Según ese mismo anuncio, los arreglos de seguridad se llevan a ramas antiguas solo como cortesía y cuando es posible, así que es un camino limitado, no una solución.

## Qué versión de PHP elegir

La versión mínima que recomienda WordPress es PHP 8.3. En [la aclaración sobre el soporte de PHP](https://make.wordpress.org/core/2026/05/22/php-support-clarification-2026/) el equipo de WordPress detalla qué versiones funcionan con cada una:

- WordPress 6.4 y posteriores soportan por completo PHP 8.3.
- WordPress 6.8 y posteriores soportan por completo PHP 8.4.
- WordPress 6.9 y 7.0 soportan por completo PHP 8.5.

En esa misma nota retiran la etiqueta "beta" que antes ponían a las versiones nuevas de PHP. Explican que asustaba a usuarios y hostings y les hacía retrasar la actualización sin motivo real. Si tu hosting te ofrece 8.3 o superior y tu WordPress está al día, esa es la opción que te recomiendo.

## Por qué merece la pena actualizar

[La guía oficial de WordPress para actualizar PHP](https://wordpress.org/documentation/update-php/) resume dos beneficios directos. El primero es la velocidad: pasar a una versión actual puede hacer tu web hasta 3 o 4 veces más rápida si vienes de una versión antigua. El segundo es la seguridad: las versiones antiguas no tienen las protecciones de las nuevas, y PHP es un objetivo habitual de ataques precisamente por lo popular que es.

De ahí salen otros dos beneficios que sí se notan en el negocio: una web más rápida retiene mejor a las visitas y los buscadores la premian. Si te interesa medir esa velocidad, te lo explico en [qué son las Core Web Vitals y cómo afectan a tu SEO](/blog/core-web-vitals-que-son/). Y si tu web ya va lenta, es una de las [señales de que tu web te hace perder clientes](/blog/senales-de-que-tu-web-te-hace-perder-clientes/).

## Antes de tocar nada: copia de seguridad y actualizaciones

La guía oficial es clara en que el cambio no debería dar problemas, pero no lo garantiza: WordPress funciona con versiones nuevas de PHP, pero cada tema y cada plugin es un mundo. Por eso recomienda dos pasos antes de cambiar la versión:

1. **Haz una copia de seguridad completa.** Si algo falla, es lo que te permite volver al punto de partida. La propia guía recuerda que hay muchos plugins de copias gratuitos si no tienes ya un sistema.
2. **Actualiza WordPress, el tema y los plugins.** Desde el escritorio, en "Actualizaciones", actualízalo todo y comprueba que la web sigue funcionando. Así partes de versiones que ya están preparadas para PHP moderno.

Este es el tipo de tarea que conviene tener resuelta de antemano. Si nadie se ocupa de las actualizaciones de tu web, te explico por qué es importante en [mantenimiento web: por qué tu página lo necesita](/blog/mantenimiento-web-por-que-es-necesario/).

## Comprueba la compatibilidad de tus plugins

El siguiente paso que propone la guía es instalar [el plugin PHP Compatibility Checker](https://wordpress.org/plugins/php-compatibility-checker/), que revisa tu tema y tus plugins en busca de problemas con la versión nueva. No es perfecto: puede dejarse cosas o marcar falsos positivos, pero funciona en la mayoría de los casos y te da una lista por la que empezar.

Si encuentra algún problema, escribe al autor del tema o del plugin y pregúntale. Si no responde o no puede arreglarlo, la recomendación oficial es buscar una alternativa con funciones parecidas en el directorio de WordPress.org. Te recomiendo no quedarte atascado por un plugin que ya nadie mantiene: si hoy te bloquea la actualización de PHP, mañana será otra cosa.

## Cómo cambiar la versión de PHP

La versión de PHP se configura en el servidor, así que el cambio depende de tu hosting. Muchos paneles de control tienen una opción para elegirla. Si no la encuentras, [la guía de WordPress](https://wordpress.org/documentation/update-php/) enlaza una lista de hostings con instrucciones propias y sugiere algo muy práctico: escribir al soporte y pedirles que te digan qué pasos seguir para usar la última versión de PHP.

Es buen momento también para valorar si tu hosting está a la altura. Si no te deja elegir versiones actuales de PHP, es una señal a tener en cuenta cuando revises [cómo elegir hosting y dominio para tu negocio](/blog/como-elegir-hosting-y-dominio/).

## Si algo falla después de actualizar

Si después del cambio algo deja de funcionar, la guía oficial da un orden claro: vuelve tú mismo a la versión anterior de PHP desde el panel, o pide al hosting que lo haga. Si además necesitas restaurar la copia de seguridad, primero tienen que devolver el servidor a la versión de PHP que tenías y después puedes restaurarla. Por eso la copia de seguridad es el paso que nunca me saltaría.

## Preguntas frecuentes

### ¿Por qué me avisa el hosting si mi web funciona bien?

Porque que funcione hoy no significa que esté protegida. Las versiones antiguas de PHP no tienen las protecciones de seguridad de las actuales, y a partir de WordPress 7.0 las webs en PHP 7.2 o 7.3 ya no pueden actualizarse a la última versión de WordPress.

### ¿Puedo romper la web al actualizar PHP?

Puede pasar si algún tema o plugin no es compatible, aunque con los populares y bien mantenidos es poco probable. Con una copia de seguridad, todo actualizado y la comprobación de compatibilidad hecha, el riesgo es bajo y siempre puedes volver atrás.

### ¿Qué versión de PHP pongo?

La recomendada por WordPress es PHP 8.3 como mínimo. Si tu WordPress es 6.8 o posterior también puedes usar 8.4, y con 6.9 o 7.0, PHP 8.5.

## Conclusión

El aviso de PHP obsoleto no es una alarma, pero tampoco algo para ignorar. Con una copia de seguridad, WordPress y plugins al día, una comprobación de compatibilidad y el cambio de versión desde el panel del hosting, la mayoría de las webs pasan a PHP 8.3 o superior sin incidencias, y ganan velocidad y seguridad por el camino.

### ¿Prefieres que lo haga yo?

Reviso tu web, hago la copia, compruebo la compatibilidad y actualizo PHP sin que tengas que tocar nada. [Contáctame](/#contacto).
