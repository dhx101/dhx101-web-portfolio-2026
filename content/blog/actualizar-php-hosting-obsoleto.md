---
title: Actualizar PHP WordPress seguro
description: Descubre el paso a paso para actualizar PHP en WordPress de forma segura, evitando errores comunes tras la actualización: activa el modo de depuración, revisa.
date: 2026-09-19
---

¿Qué hacer cuando tu hosting te avisa de que tu versión de PHP está obsoleta? Si recibes este mensaje, no es solo un recordatorio técnico: es una señal clara de que tu sitio web puede estar más lento, menos seguro y peor posicionado en Google. No todos los servicios de hosting explican qué significa exactamente "obsoleta", pero el problema se resuelve con pasos claros. Lo primero que reviso cuando un cliente me avisa de esto es si su WordPress está actualizado, porque una versión desactualizada del núcleo puede hacer que la compatibilidad con PHP sea más frágil.

## Revisa tu versión de WordPress y sus componentes

Antes de tocar nada en el servidor, asegúrate de que estás usando la última versión estable de WordPress. Las versiones antiguas pueden tener dependencias que ya no funcionan con PHP 8.x o incluso con PHP 7.4. [La documentación oficial](https://make.wordpress.org/core/2026/05/22/php-support-clarification-2026/) indica que desde WordPress 6.4 en adelante, el soporte para PHP 8.3 está garantizado; y a partir de WordPress 6.8, también lo es para PHP 8.4. Si estás usando una versión anterior, actualízala primero. También verifica que todos tus plugins y temas estén actualizados. Muchos desarrolladores aún no han optimizado sus productos para las últimas versiones de PHP, especialmente si usan funciones antiguas o sintaxis desactualizada.

## Comprueba qué versión de PHP estás usando

El hosting te puede avisar sin especificar exactamente cuál es tu versión actual. En el panel de control (como cPanel), busca una sección llamada "PHP Configuration" o "Versión de PHP". Si ves algo como 7.3, 7.2 o incluso 5.6, estás en riesgo. Según [la documentación del equipo de WordPress](https://make.wordpress.org/core/2026/01/09/dropping-support-for-php-7-2-and-7-3/), a partir de abril de 2026 (WordPress 7.0), se dejará de soportar PHP 7.2 y 7.3. El mínimo soportado será 7.4, aunque el recomendado sigue siendo PHP 8.3 o superior.

## Prueba la compatibilidad antes de actualizar

Actualizar PHP directamente puede romper tu sitio si hay incompatibilidades en plugins o temas. Lo primero que hago es instalar el plugin [PHP Compatibility Checker](https://wordpress.org/documentation/update-php/), que escanea automáticamente tus extensiones y te muestra posibles errores. No es infalible —puede generar falsos positivos— pero funciona bien para detectar problemas comunes, como uso de funciones obsoletas o sintaxis no compatible con PHP 8.x.

Si el plugin detecta fallos, lo que sigue es simple: contacta al desarrollador del tema o plugin. En muchos casos, los creadores ya han actualizado sus productos; en otros, pueden ofrecer una versión beta o un parche temporal. Si no recibes respuesta, busca alternativas en [WordPress.org](/blog/como-elegir-hosting-y-dominio/) con funciones similares. No te quedes atrapado por un componente que no se mantiene.

## Actualiza PHP con precaución

Una vez verificado el estado de tu sitio, puedes proceder a cambiar la versión de PHP. En muchos hosts, esto es tan simple como elegir una opción en un menú desplegable. Si no tienes acceso directo, contacta al soporte técnico y pide ayuda para actualizar a PHP 8.3 o superior.

No olvides hacer una copia de seguridad completa del sitio antes de cualquier cambio. [La documentación oficial recomienda](https://wordpress.org/documentation/update-php/) hacer esto como medida preventiva. Algunos hosts ofrecen herramientas automáticas de backup, pero si no es así, usa un plugin como UpdraftPlus o BackupBuddy.

## ¿Qué pasa si algo falla tras la actualización?

Si tu sitio deja de cargar o aparecen errores en pantalla, lo primero que debes hacer es volver a PHP 7.4 (o la versión anterior funcional). Esto suele ser posible desde el panel de control del hosting, siempre que hayas hecho una copia de seguridad. Si no puedes revertir, contacta al soporte técnico: muchos hosts tienen políticas de ayuda en estos casos.

También es útil revisar los logs de errores (en `wp-content/debug.log` si está activado) para entender qué falló. A menudo el problema viene de un plugin que aún no se ha actualizado, o de una función del tema que usa sintaxis obsoleta.

## Preguntas frecuentes

### ¿Por qué mi hosting me avisa de PHP obsoleto si mi sitio funciona?

Aunque tu sitio funcione ahora mismo, usar una versión antigua de PHP aumenta el riesgo de vulnerabilidades. Las versiones como 7.2 o 7.3 ya no reciben actualizaciones de seguridad desde 2021. Esto significa que cualquier fallo descubierto en esas versiones puede ser explotado sin corrección oficial.

### ¿Es seguro actualizar PHP si tengo plugins antiguos?

No hay garantía absoluta, pero el riesgo se reduce mucho si primero compruebas la compatibilidad. [El equipo de WordPress](https://make.wordpress.org/core/2026/05/22/php-support-clarification-2026/) ha eliminado la etiqueta "beta" en las versiones modernas de PHP porque los problemas reales son mínimos. Además, muchos plugins han sido actualizados para soportar PHP 8.x.

### ¿Qué ganaría al actualizar a PHP 8.3 o superior?

Según [la documentación oficial](https://wordpress.org/documentation/update-php/), las mejoras de rendimiento pueden llegar hasta un 300% en sitios con versiones antiguas. También hay mejoras en seguridad, compatibilidad con nuevas funciones y soporte para herramientas modernas como IA integrada en plugins.

Si quieres seguir leyendo sobre esto, te recomiendo [mantenimiento web: por qué tu página lo necesita](/blog/mantenimiento-web-por-que-es-necesario/) y [de sqlite a postgres: por qué migré la base de datos](/blog/de-sqlite-a-postgres-por-que-migre-mi-base-de-datos/).

## Conclusión
Actualizar PHP no es una opción opcional si quieres mantener tu sitio seguro, rápido y bien posicionado. El aviso de tu hosting no es un trámite burocrático: es una advertencia técnica real que debe tomarse en serio. Lo primero es asegurarte de que WordPress y todos sus componentes estén actualizados, luego probar la compatibilidad con herramientas como el plugin [PHP Compatibility Checker](https://wordpress.org/documentation/update-php/), hacer una copia de seguridad y proceder a actualizar solo si todo está preparado.

### ¿Qué hago si no sé por dónde empezar?

Te ayudo paso a paso. [Contáctame](/#contacto).
