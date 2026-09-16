#!/usr/bin/env node
/**
 * Compara los estilos computados de dos versiones del sitio y falla si difieren.
 *
 * Existe porque durante el refactor de 2026 dos cambios de CSS rompieron la web
 * en silencio: una regla de @media promovida a global (tiró el menú de
 * escritorio) y una propiedad declarada dos veces en la misma regla, donde
 * extraer la ganadora a una clase le devolvió la cascada a la perdedora.
 * Razonar sobre la especificidad a mano no basta. Un navegador sí.
 *
 *   node scripts/verify_render.js <dirAntes> <dirDespues> [pagina.html ...]
 *
 * Requiere: npm install playwright && npx playwright install chromium
 * Sale con código 1 si encuentra cualquier diferencia.
 */
const { chromium } = require('playwright');
const path = require('path');

const PROPS = ['display','flex-direction','flex-wrap','align-items','justify-content','gap','row-gap',
  'column-gap','width','height','position','top','left','right','bottom','text-align','text-transform',
  'font-weight','font-size','line-height','color','background-color','padding','margin','order',
  'flex-grow','flex-shrink','grid-template-columns','opacity','fill','border-radius','z-index'];

const VIEWPORTS = [[1440, 900], [768, 1024], [390, 844]];

async function snapshot(page, file, [w, h]) {
  await page.setViewportSize({ width: w, height: h });
  await page.goto('file://' + path.resolve(file), { waitUntil: 'networkidle' });
  // Las imágenes lazy sin width/height cambian la altura de su contenedor según
  // si Chromium llegó a cargarlas: se fuerzan todas y se espera a que terminen.
  await page.evaluate(() => Promise.all([...document.images].map(img => {
    img.loading = 'eager';
    return img.complete ? null : new Promise(r => { img.onload = img.onerror = r; });
  })));
  await page.waitForTimeout(400);           // dejar acabar las transiciones
  return page.evaluate((PROPS) => {
    const out = {};
    const walk = (el, p) => {
      const cs = getComputedStyle(el), o = {};
      for (const prop of PROPS) o[prop] = cs.getPropertyValue(prop);
      out[p] = o;
      // Se ignoran los elementos que no pintan nada: así mover un <script> de
      // inline a externo no desplaza los índices de todo el árbol.
      const NO_PINTAN = new Set(['SCRIPT','STYLE','LINK','NOSCRIPT','TEMPLATE','META','TITLE']);
      [...el.children].filter(c => !NO_PINTAN.has(c.tagName))
        .forEach((c, i) => walk(c, `${p}/${c.tagName.toLowerCase()}[${i}]`));
    };
    walk(document.body, 'body');
    return out;
  }, PROPS);
}

(async () => {
  const [dirA, dirB, ...pages] = process.argv.slice(2);
  if (!dirA || !dirB) { console.error('uso: verify_render.js <dirAntes> <dirDespues> [paginas...]'); process.exit(2); }
  const targets = pages.length ? pages : ['index.html'];

  const browser = await chromium.launch();
  // Sin esto el arnés no es determinista: las animaciones de entrada de GSAP
  // siguen a medias a los 400 ms y dos copias idénticas dan cientos de
  // diferencias de opacity. animations.js no anima con reduced motion.
  const page = await browser.newPage({ reducedMotion: 'reduce' });
  let total = 0;

  for (const file of targets) {
    for (const vp of VIEWPORTS) {
      const A = await snapshot(page, path.join(dirA, file), vp);
      const B = await snapshot(page, path.join(dirB, file), vp);
      const diffs = [];
      const ka = Object.keys(A), kb = Object.keys(B);
      if (ka.length !== kb.length) diffs.push(`ESTRUCTURA: ${ka.length} vs ${kb.length} elementos`);
      for (const k of ka) {
        if (!B[k]) { diffs.push(`FALTA: ${k}`); continue; }
        for (const p of PROPS) if (A[k][p] !== B[k][p]) diffs.push(`${k}  ${p}: ${A[k][p]} -> ${B[k][p]}`);
      }
      const tag = `${file} @${vp[0]}x${vp[1]}`;
      if (diffs.length) {
        console.log(`FALLO  ${tag}  (${ka.length} elementos, ${diffs.length} diferencias)`);
        diffs.slice(0, 20).forEach(d => console.log('       ' + d));
        if (diffs.length > 20) console.log(`       ... y ${diffs.length - 20} más`);
      } else {
        console.log(`OK     ${tag}  (${ka.length} elementos)`);
      }
      total += diffs.length;
    }
  }
  await browser.close();
  console.log(total ? `\n${total} diferencias en total` : '\nSin diferencias.');
  process.exit(total ? 1 : 0);
})();
