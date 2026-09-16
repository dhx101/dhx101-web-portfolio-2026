/**
 * Comportamiento de la cabecera: scroll suave de los enlaces ancla, botón de
 * "volver arriba", menú móvil y submenús.
 */
document.querySelectorAll('a[href^="#"]').forEach(function(link) {
  link.addEventListener('click', function(e) {
    var target = document.querySelector(this.getAttribute('href'));
    if (!target) { return; }
    e.preventDefault();
    var offset = window.innerHeight / 2 - target.offsetHeight / 2;
    var top = target.getBoundingClientRect().top + window.scrollY - offset;
    window.scrollTo({ top: top, behavior: 'smooth' });
  });
});
document.querySelector('#brxe-rviltc').addEventListener('click', function() {
  console.log("scroll")
  window.scrollTo({ top: 0, behavior: 'smooth' });
});
var dhxMenuToggle = document.querySelector('#dhx-menu-toggle');
var dhxHeader = document.querySelector('#brx-header');
dhxMenuToggle.addEventListener('click', function() {
  var isOpen = dhxHeader.classList.toggle('dhx-menu-open');
  dhxMenuToggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
});
document.querySelectorAll('#brxe-vzunlc a, #brxe-uklerk').forEach(function(link) {
  link.addEventListener('click', function() {
    dhxHeader.classList.remove('dhx-menu-open');
    dhxMenuToggle.setAttribute('aria-expanded', 'false');
  });
});

// Submenús y selector de idioma. El hover lo resuelve nav.css; esto añade la
// apertura con clic (pantallas táctiles grandes) y teclado, el cierre al pulsar
// fuera o con Escape, y aria-expanded para lectores de pantalla.
var dhxSubToggles = document.querySelectorAll('#brx-header .nav-sub-toggle');
function dhxCloseSubs(except) {
  dhxSubToggles.forEach(function(t) {
    if (t === except) { return; }
    t.setAttribute('aria-expanded', 'false');
    t.parentElement.classList.remove('is-open');
  });
}
dhxSubToggles.forEach(function(toggle) {
  toggle.addEventListener('click', function(e) {
    e.stopPropagation();
    var open = !toggle.parentElement.classList.contains('is-open');
    dhxCloseSubs(toggle);
    toggle.parentElement.classList.toggle('is-open', open);
    toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
  });
});
// Al elegir una opción se cierra: sin el blur, :focus-within lo mantendría abierto.
document.querySelectorAll('#brx-header .nav-sub-link').forEach(function(link) {
  link.addEventListener('click', function() {
    dhxCloseSubs();
    link.blur();
  });
});
document.addEventListener('click', function(e) {
  if (!e.target.closest('#brx-header .nav-item')) { dhxCloseSubs(); }
});
document.addEventListener('keydown', function(e) {
  if (e.key === 'Escape') { dhxCloseSubs(); }
});
