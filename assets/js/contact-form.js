/**
 * Envío del formulario de contacto a Formspree, con los mensajes de estado del terminal.
 */
window.addEventListener('load', function() {
  var form    = document.querySelector('#dhx-form');
  var btn     = document.querySelector('#dhx-btn');
  var btnText = document.querySelector('#dhx-btn-text');
  var status  = document.querySelector('#dhx-status');

  if (!form) { console.log('form no encontrado'); return; }
  console.log('form OK');

  form.addEventListener('submit', function(e) {
    e.preventDefault();
    console.log('submit disparado');

    var nombreVal  = document.querySelector('#dhx-nombre').value.trim();
    var emailVal   = document.querySelector('#dhx-email').value.trim();
    var mensajeVal = document.querySelector('#dhx-mensaje').value.trim();

    console.log('valores:', nombreVal, emailVal, mensajeVal);

    var msg = (window.DHX_MESSAGES && window.DHX_MESSAGES[window.DHX_LANG]) || {
      required: '> Error: campos obligatorios vacios.',
      sent: '> Transmision completada. Respondere pronto.',
      sendError: '> Error en la transmision. Intentalo de nuevo.',
      connError: '> Error de conexion. Comprueba tu red.'
    };

    if (!nombreVal || !emailVal || !mensajeVal) {
      showStatus('error', msg.required);
      return;
    }

    if (btnText) { btnText.textContent = '[ Sending... ]'; }
    if (btn)     { btn.disabled = true; }

    fetch('https://formspree.io/f/xzdlkjdy', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
      body: JSON.stringify({ nombre: nombreVal, email: emailVal, mensaje: mensajeVal })
    })
    .then(function(res) {
      console.log('status respuesta:', res.status);
      if (res.ok) {
        showStatus('success', msg.sent);
        form.reset();
      } else {
        showStatus('error', msg.sendError);
      }
    })
    .catch(function(err) {
      console.log('error fetch:', err);
      showStatus('error', msg.connError);
    })
    .finally(function() {
      if (btnText) { btnText.textContent = '[ Execute_Send ]'; }
      if (btn)     { btn.disabled = false; }
    });
  });

  function showStatus(type, msg) {
    if (!status) { return; }
    status.textContent = msg;
    status.style.color = type === 'success' ? '#00e639' : '#ffb4ab';
  }
});
