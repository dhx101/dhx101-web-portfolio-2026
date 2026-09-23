/**
 * Envío del formulario de contacto al webhook de n8n, con los mensajes de estado del terminal.
 * Si n8n no responde (caído, 5xx o más de 8 s), el mensaje se reenvía a Formspree para no perderlo.
 */
window.addEventListener('load', function() {
  var N8N_URL        = 'https://n8n.davidhuangxie.com/webhook/contacto-web';
  var FORMSPREE_URL  = 'https://formspree.io/f/xzdlkjdy';
  var CONTACT_EMAIL  = 'dhuangxie@gmail.com';
  var N8N_TIMEOUT_MS = 8000;

  var form    = document.querySelector('#dhx-form');
  var btn     = document.querySelector('#dhx-btn');
  var btnText = document.querySelector('#dhx-btn-text');
  var status  = document.querySelector('#dhx-status');

  if (!form) { return; }

  form.addEventListener('submit', function(e) {
    e.preventDefault();

    var nombreVal  = document.querySelector('#dhx-nombre').value.trim();
    var emailVal   = document.querySelector('#dhx-email').value.trim();
    var mensajeVal = document.querySelector('#dhx-mensaje').value.trim();
    var trampaEl   = document.querySelector('#dhx-empresa');
    var trampaVal  = trampaEl ? trampaEl.value.trim() : '';
    var paginaVal  = window.location.href;
    var idiomaVal  = window.DHX_LANG || 'es';

    var msg = (window.DHX_MESSAGES && window.DHX_MESSAGES[window.DHX_LANG]) || {
      required: '> Error: campos obligatorios vacios.',
      sent: '> Transmision completada. Respondere pronto.',
      sendError: '> Error en la transmision. Intentalo de nuevo.',
      connError: '> Error de conexion. Comprueba tu red.'
    };

    if (!nombreVal || !emailVal || !mensajeVal) {
      track('formulario-incompleto');
      showStatus('error', msg.required);
      return;
    }

    if (btnText) { btnText.textContent = '[ Sending... ]'; }
    if (btn)     { btn.disabled = true; }

    var controller = window.AbortController ? new AbortController() : null;
    var timer = controller ? setTimeout(function() { controller.abort(); }, N8N_TIMEOUT_MS) : null;

    fetch(N8N_URL, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
      body: JSON.stringify({
        nombre: nombreVal,
        email: emailVal,
        mensaje: mensajeVal,
        empresa: trampaVal,
        pagina: paginaVal,
        idioma: idiomaVal
      }),
      signal: controller ? controller.signal : undefined
    })
    .then(function(res) {
      clearTimeout(timer);
      if (res.ok) {
        onSent('n8n');
      } else if (res.status >= 400 && res.status < 500) {
        // Datos no válidos o spam: Formspree lo rechazaría igual, así que no se reintenta.
        track('formulario-error', { tipo: 'envio', estado: res.status });
        showStatus('error', msg.sendError);
      } else {
        return sendBackup({ motivo: 'estado', estado: res.status });
      }
    }, function(err) {
      clearTimeout(timer);
      return sendBackup({ motivo: err && err.name === 'AbortError' ? 'timeout' : 'conexion' });
    })
    .finally(function() {
      if (btnText) { btnText.textContent = '[ Execute_Send ]'; }
      if (btn)     { btn.disabled = false; }
    });

    function sendBackup(data) {
      track('formulario-respaldo', data);

      return fetch(FORMSPREE_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
        body: JSON.stringify({
          name: nombreVal,
          email: emailVal,
          message: mensajeVal,
          idioma: idiomaVal,
          pagina: paginaVal,
          _subject: 'Formulario web (respaldo, n8n no respondió) — ' + nombreVal,
          _gotcha: trampaVal
        })
      })
      .then(function(res) {
        if (res.ok) {
          onSent('respaldo');
        } else {
          track('formulario-error', { tipo: 'respaldo', estado: res.status });
          showFailure(msg.sendError);
        }
      }, function() {
        track('formulario-error', { tipo: 'respaldo-conexion' });
        showFailure(msg.connError);
      });
    }

    function onSent(via) {
      track('formulario-enviado', { via: via });
      showStatus('success', msg.sent);
      form.reset();
    }
  });

  function track(name, data) {
    if (window.dhxTrack) { window.dhxTrack(name, data); }
  }

  function showStatus(type, msg) {
    if (!status) { return; }
    status.textContent = msg;
    status.style.color = type === 'success' ? '#00e639' : '#ffb4ab';
  }

  // Último recurso: el error más un enlace para escribir directamente por email.
  function showFailure(msg) {
    showStatus('error', msg);
    if (!status) { return; }
    var link = document.createElement('a');
    link.href = 'mailto:' + CONTACT_EMAIL;
    link.textContent = CONTACT_EMAIL;
    link.className = 'underline';
    link.style.color = 'inherit';
    status.appendChild(document.createTextNode(' > '));
    status.appendChild(link);
  }
});
