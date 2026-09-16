/**
 * Eventos de Umami (stats.davidhuangxie.com).
 *
 * Un único listener de clics para toda la página, en vez de atributos enlace a
 * enlace: así cubre también los enlaces que generan los scripts (el "Contáctame"
 * de cada post) y los que se añadan en el futuro.
 *
 * Si Umami no ha cargado (bloqueador, entorno local o el arnés de render, que el
 * data-domains del script excluye) no se envía nada.
 */
(function() {
  function track(name, data) {
    if (window.umami && typeof window.umami.track === 'function') {
      window.umami.track(name, data);
    }
  }

  document.addEventListener('click', function(e) {
    var el = e.target.closest ? e.target.closest('a, .dhx-lang-opt') : null;
    if (!el) { return; }
    var pagina = location.pathname;

    if (el.classList.contains('dhx-lang-opt')) {
      track('idioma', { idioma: el.getAttribute('data-lang'), pagina: pagina });
      return;
    }

    var href = el.getAttribute('href') || '';
    if (/#contacto$/.test(href)) {
      track('contacto-clic', { texto: (el.textContent || '').trim().slice(0, 60), pagina: pagina });
    } else if (href.indexOf('mailto:') === 0) {
      track('email-clic', { pagina: pagina });
    } else if (href.indexOf('linkedin.com') !== -1) {
      track('linkedin-clic', { pagina: pagina });
    } else if (href.indexOf('cv-david-huang-xie') !== -1) {
      track('cv-descarga', { idioma: /-en\.pdf/.test(href) ? 'en' : 'es', pagina: pagina });
    } else if (/^https?:\/\//.test(href) && el.hostname !== location.hostname) {
      track('enlace-externo', { destino: el.hostname, pagina: pagina });
    }
  }, true);

  // Para los scripts que registran eventos propios (formulario de contacto).
  window.dhxTrack = track;
})();
