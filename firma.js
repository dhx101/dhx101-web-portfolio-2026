/*! Firma de autor en la consola · David Huang Xie · https://davidhuangxie.com
 *
 * Un solo archivo para dos usos:
 * - En davidhuangxie.com (y en local) muestra la firma del portfolio.
 * - En cualquier otro dominio (webs de clientes) muestra la firma de autor, con
 *   un enlace etiquetado con UTM para ver en Umami qué web trajo cada visita.
 *
 * Uso en una web de cliente:
 *   <script src="https://davidhuangxie.com/firma.js" defer></script>
 *
 * Solo escribe en la consola: no toca la página, no usa cookies ni carga nada.
 * Los textos van con escapes \u para verse bien aunque la web use otra codificación.
 */
(function () {
  if (window.__dhxFirma) { return; }
  window.__dhxFirma = true;

  var COLOR = '#8b5cf6';
  var ASCII = [
    "\u2588\u2588\u2588\u2588\u2588\u2588  \u2588\u2588   \u2588\u2588 \u2588\u2588   \u2588\u2588  \u2588\u2588  \u2588\u2588\u2588\u2588\u2588\u2588   \u2588\u2588",
    "\u2588\u2588   \u2588\u2588 \u2588\u2588   \u2588\u2588  \u2588\u2588 \u2588\u2588  \u2588\u2588\u2588 \u2588\u2588  \u2588\u2588\u2588\u2588 \u2588\u2588\u2588",
    "\u2588\u2588   \u2588\u2588 \u2588\u2588\u2588\u2588\u2588\u2588\u2588   \u2588\u2588\u2588    \u2588\u2588 \u2588\u2588 \u2588\u2588 \u2588\u2588  \u2588\u2588",
    "\u2588\u2588   \u2588\u2588 \u2588\u2588   \u2588\u2588  \u2588\u2588 \u2588\u2588   \u2588\u2588 \u2588\u2588\u2588\u2588  \u2588\u2588  \u2588\u2588",
    "\u2588\u2588\u2588\u2588\u2588\u2588  \u2588\u2588   \u2588\u2588 \u2588\u2588   \u2588\u2588  \u2588\u2588  \u2588\u2588\u2588\u2588\u2588\u2588   \u2588\u2588"
  ].join('\n');

  var host = location.hostname;
  var esPortfolio = !host || host === 'localhost' || host === '127.0.0.1' ||
    host === 'davidhuangxie.com' || host.slice(-18) === '.davidhuangxie.com';

  console.log('%c' + ASCII, 'font-family:monospace;line-height:1.15;color:' + COLOR);

  if (esPortfolio) {
    console.log(
      '%c' + "DHX101_OS // SYSTEM_ROOT\n> \u00bfCurioseando el c\u00f3digo? Buen instinto.\n> Desarrollo web, WordPress y automatizaci\u00f3n con IA.\n> Si tienes un proyecto en mente, hablemos:" + '\n%c  https://davidhuangxie.com/#contacto',
      'font-family:monospace;line-height:1.5',
      'font-family:monospace;line-height:1.5;color:' + COLOR
    );
  } else {
    var url = 'https://davidhuangxie.com/?utm_source=' + encodeURIComponent(host) +
      '&utm_medium=consola&utm_campaign=firma';
    console.log(
      '%c' + "Web desarrollada por " + '%c' + "David Huang Xie" + '%c' + "\nDesarrollo web \u00b7 WordPress \u00b7 Automatizaci\u00f3n con IA\n" + url,
      'font-family:monospace;line-height:1.5',
      'font-family:monospace;line-height:1.5;font-weight:bold;color:' + COLOR,
      'font-family:monospace;line-height:1.5;color:#868e96'
    );
  }
})();
