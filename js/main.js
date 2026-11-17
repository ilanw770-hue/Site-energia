/* ============================================================
   Energia Group — Interactions
   ============================================================ */
(function () {
  'use strict';
  var CFG = window.ENERGIA_CONFIG || {};

  // --- Année du footer ---
  document.querySelectorAll('[data-year]').forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });

  // --- Coordonnées depuis la configuration ---
  document.querySelectorAll('[data-contact]').forEach(function (el) {
    var kind = el.getAttribute('data-contact');
    var val = CFG[kind];
    if (!val) return;
    var a = document.createElement('a');
    a.textContent = val;
    a.href = kind === 'phone' ? 'tel:' + val.replace(/\s/g, '') : 'mailto:' + val;
    el.textContent = '';
    el.appendChild(a);
  });

  // --- Réseaux sociaux ---
  var socialsEl = document.querySelector('[data-socials]');
  if (socialsEl && CFG.socials) {
    var labels = { facebook: 'Facebook', instagram: 'Instagram', linkedin: 'LinkedIn' };
    Object.keys(labels).forEach(function (k) {
      if (!CFG.socials[k]) return;
      var a = document.createElement('a');
      a.href = CFG.socials[k];
      a.target = '_blank';
      a.rel = 'noopener';
      a.textContent = labels[k];
      socialsEl.appendChild(a);
    });
  }

  // --- Header au scroll ---
  var header = document.getElementById('header');
  var onScroll = function () {
    header.classList.toggle('scrolled', window.scrollY > 10);
  };
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  // --- Menu mobile ---
  var toggle = document.getElementById('navToggle');
  var nav = document.getElementById('nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      toggle.setAttribute('aria-label', open ? 'Fermer le menu' : 'Ouvrir le menu');
      document.body.classList.toggle('nav-open', open);
    });
  }

  // --- Envoi des demandes ---
  function collect(form) {
    var data = { source: form.getAttribute('data-source') || 'Site', page: location.pathname };
    new FormData(form).forEach(function (v, k) { data[k] = v; });
    if (data.consentement) data.consentement = 'oui';
    return data;
  }

  function send(data) {
    if (CFG.formEndpoint) {
      return fetch(CFG.formEndpoint, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
        body: JSON.stringify(data)
      }).then(function (r) {
        if (!r.ok) throw new Error('HTTP ' + r.status);
      });
    }
    if (CFG.email) {
      var lines = Object.keys(data).map(function (k) { return k + ' : ' + data[k]; });
      location.href = 'mailto:' + CFG.email +
        '?subject=' + encodeURIComponent('Demande site — ' + data.source) +
        '&body=' + encodeURIComponent(lines.join('\n'));
      return Promise.resolve();
    }
    return Promise.reject(new Error('Aucun canal de réception configuré (js/config.js)'));
  }

  function validate(fields) {
    var ok = true;
    var firstBad = null;
    fields.forEach(function (f) {
      if (f.type === 'radio') {
        var group = f.form.querySelectorAll('input[name="' + f.name + '"]');
        var checked = Array.prototype.some.call(group, function (r) { return r.checked; });
        var box = f.closest('.choices');
        if (box) box.classList.toggle('invalid', !checked);
        if (!checked) { ok = false; firstBad = firstBad || f; }
        return;
      }
      var bad = !f.checkValidity() ||
        (f.name === 'telephone' && f.value.replace(/[^\d+]/g, '').length < 10);
      f.classList.toggle('invalid', bad);
      if (f.type === 'checkbox') f.closest('label').classList.toggle('invalid', bad);
      if (bad) { ok = false; firstBad = firstBad || f; }
    });
    if (firstBad && firstBad.focus) firstBad.focus();
    return ok;
  }

  function setStatus(form, msg, kind) {
    var st = form.querySelector('.form-status');
    if (!st) return;
    st.textContent = msg;
    st.className = 'form-status' + (kind ? ' ' + kind : '');
  }

  function requiredIn(scope) {
    return Array.prototype.slice.call(scope.querySelectorAll('input, select, textarea'))
      .filter(function (f) { return f.required; });
  }

  function submitForm(form, onDone) {
    var btn = form.querySelector('button[type="submit"]');
    var label = btn.innerHTML;
    btn.disabled = true;
    btn.textContent = 'Envoi en cours…';
    send(collect(form)).then(function () {
      onDone();
    }).catch(function (err) {
      console.error(err);
      setStatus(form, "L'envoi n'a pas abouti. Merci de réessayer ou de nous contacter directement.", 'error');
    }).then(function () {
      btn.disabled = false;
      btn.innerHTML = label;
    });
  }

  document.querySelectorAll('form.lead-form').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      setStatus(form, '');
      if (!validate(requiredIn(form))) {
        setStatus(form, 'Merci de compléter les champs indiqués.', 'error');
        return;
      }
      submitForm(form, function () {
        form.reset();
        setStatus(form, 'Merci ! Votre demande est bien enregistrée. Un conseiller vous recontacte sous 48 h.', 'success');
      });
    });
  });

  // --- Test d'éligibilité (formulaire en étapes) ---
  var wizard = document.getElementById('wizard');
  if (wizard) {
    var steps = Array.prototype.slice.call(wizard.querySelectorAll('[data-step]'));
    var done = wizard.querySelector('[data-done]');
    var prev = document.getElementById('wPrev');
    var next = document.getElementById('wNext');
    var submit = document.getElementById('wSubmit');
    var bar = document.getElementById('wizardBar');
    var count = document.getElementById('wizardCount');
    var i = 0;

    // Pré-remplissage depuis le mini-formulaire de l'accueil
    var params = new URLSearchParams(location.search);
    var ch = params.get('chauffage');
    if (ch) {
      var radio = wizard.querySelector('input[name="chauffage"][value="' + ch.replace(/[^a-z]/g, '') + '"]');
      if (radio) radio.checked = true;
    }
    var cp = params.get('cp');
    if (cp && /^\d{5}$/.test(cp)) wizard.querySelector('[name="code_postal"]').value = cp;

    var show = function () {
      steps.forEach(function (s, k) { s.hidden = k !== i; });
      prev.hidden = i === 0;
      next.hidden = i === steps.length - 1;
      submit.hidden = i !== steps.length - 1;
      bar.style.width = ((i + 1) / steps.length * 100) + '%';
      count.textContent = 'Étape ' + (i + 1) + ' sur ' + steps.length;
    };

    // Étapes à une seule question : avancer dès qu'un choix est fait
    steps.forEach(function (s) {
      if (s.querySelectorAll('.choices').length !== 1 || s.querySelector('select, input:not([type=radio])')) return;
      s.addEventListener('change', function () {
        setTimeout(function () { if (steps[i] === s) next.click(); }, 200);
      });
    });

    next.addEventListener('click', function () {
      setStatus(wizard, '');
      if (!validate(requiredIn(steps[i]))) {
        setStatus(wizard, 'Merci de répondre à toutes les questions de cette étape.', 'error');
        return;
      }
      i = Math.min(i + 1, steps.length - 1);
      show();
      var top = wizard.getBoundingClientRect().top + window.scrollY - 100;
      if (window.scrollY > top) window.scrollTo({ top: top, behavior: 'smooth' });
    });
    prev.addEventListener('click', function () {
      setStatus(wizard, '');
      i = Math.max(i - 1, 0);
      show();
    });
    wizard.addEventListener('submit', function (e) {
      e.preventDefault();
      setStatus(wizard, '');
      if (i !== steps.length - 1) { next.click(); return; }
      if (!validate(requiredIn(steps[i]))) {
        setStatus(wizard, 'Merci de compléter vos coordonnées.', 'error');
        return;
      }
      submitForm(wizard, function () {
        steps.forEach(function (s) { s.hidden = true; });
        wizard.querySelector('.wizard-nav').hidden = true;
        wizard.querySelector('.wizard-progress').hidden = true;
        count.hidden = true;
        done.hidden = false;
      });
    });
    show();
  }
})();
