/* ============================================
   Energia Group — Interactions
   ============================================ */
(function () {
  'use strict';

  // --- Année du footer ---
  var yearEl = document.getElementById('year');
  if (yearEl) yearEl.textContent = new Date().getFullYear();

  // --- Header au scroll ---
  var header = document.getElementById('header');
  var onScroll = function () {
    if (window.scrollY > 10) header.classList.add('scrolled');
    else header.classList.remove('scrolled');
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
    });
    nav.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () {
        nav.classList.remove('open');
        toggle.setAttribute('aria-expanded', 'false');
      });
    });
  }

  // --- Animations au défilement ---
  var revealTargets = document.querySelectorAll(
    '.card, .step, .quote, .about-content, .about-media, .section-head, .stat'
  );
  revealTargets.forEach(function (el) { el.classList.add('reveal'); });

  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries, observer) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.15 });
    revealTargets.forEach(function (el) { io.observe(el); });
  } else {
    revealTargets.forEach(function (el) { el.classList.add('visible'); });
  }

  // --- Compteurs animés ---
  var counters = document.querySelectorAll('.stat-num');
  var animateCount = function (el) {
    var target = parseInt(el.getAttribute('data-target'), 10) || 0;
    var suffix = el.getAttribute('data-suffix') || '';
    var duration = 1600;
    var start = null;
    var step = function (ts) {
      if (!start) start = ts;
      var progress = Math.min((ts - start) / duration, 1);
      var eased = 1 - Math.pow(1 - progress, 3);
      el.textContent = Math.round(eased * target) + suffix;
      if (progress < 1) requestAnimationFrame(step);
    };
    requestAnimationFrame(step);
  };

  if ('IntersectionObserver' in window && counters.length) {
    var co = new IntersectionObserver(function (entries, observer) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          animateCount(entry.target);
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.5 });
    counters.forEach(function (el) { co.observe(el); });
  } else {
    counters.forEach(function (el) {
      el.textContent = (el.getAttribute('data-target') || '') + (el.getAttribute('data-suffix') || '');
    });
  }

  // --- Validation & envoi du formulaire ---
  var form = document.getElementById('contactForm');
  var status = document.getElementById('formStatus');
  if (form) {
    var emailRe = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      status.textContent = '';
      status.className = 'form-status';

      var name = form.name;
      var email = form.email;
      var valid = true;

      [name, email].forEach(function (f) { f.classList.remove('invalid'); });

      if (!name.value.trim()) { name.classList.add('invalid'); valid = false; }
      if (!emailRe.test(email.value.trim())) { email.classList.add('invalid'); valid = false; }

      if (!valid) {
        status.textContent = 'Merci de renseigner un nom et un email valide.';
        status.classList.add('error');
        return;
      }

      // Simulation d'envoi (à connecter à un backend / service d'emailing)
      var btn = form.querySelector('button[type="submit"]');
      var original = btn.textContent;
      btn.disabled = true;
      btn.textContent = 'Envoi en cours…';

      setTimeout(function () {
        btn.disabled = false;
        btn.textContent = original;
        form.reset();
        status.textContent = 'Merci ! Votre demande a bien été envoyée, nous vous recontactons sous 48h.';
        status.classList.add('success');
      }, 900);
    });
  }
})();
