/**
 * Scroll suave para los enlaces ancla de la cabecera, y el botón de "volver arriba".
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
