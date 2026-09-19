// Índice de los posts: marca la sección que se está leyendo y, en móvil,
// cierra el desplegable al elegir una sección.
(function () {
  var headings = Array.prototype.slice.call(document.querySelectorAll('.blog-post-body h2[id]'));
  var links = Array.prototype.slice.call(document.querySelectorAll('.blog-toc a, .blog-toc-mobile a'));
  if (!headings.length || !links.length) return;

  function marcar(id) {
    links.forEach(function (a) {
      if (a.getAttribute('href') === '#' + id) a.setAttribute('aria-current', 'true');
      else a.removeAttribute('aria-current');
    });
  }

  if ('IntersectionObserver' in window) {
    var observer = new IntersectionObserver(function () {
      // La sección activa es la última cuyo título ya ha pasado por la parte alta de la pantalla.
      var activa = headings[0].id;
      headings.forEach(function (h) {
        if (h.getBoundingClientRect().top < window.innerHeight * 0.35) activa = h.id;
      });
      marcar(activa);
    }, { rootMargin: '0px 0px -60% 0px' });
    headings.forEach(function (h) { observer.observe(h); });
  }

  var movil = document.querySelector('.blog-toc-mobile');
  if (movil) {
    movil.addEventListener('click', function (e) {
      if (e.target.closest('a')) movil.removeAttribute('open');
    });
  }
})();
