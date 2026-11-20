/* ═══════════════════════════════════════════════
   STUDIO LEGALE AVV. FRANCESCO IACCARINO
   Main JavaScript v3.0 — Marzo 2026

   ISTRUZIONI PENDENTI:
   1. Sostituire "G-XXXXXXXXXX" con il vero ID di Google Analytics GA4
   2. Sostituire "AW-XXXXXXXXXX/XXXXXXXXXX" con i veri ID di Google Ads
   3. Al primo invio del form, Formsubmit.co invierà un'email di verifica
      a studiolegalefrancescoiaccarino@outlook.com — cliccare il link
      per attivare la ricezione dei messaggi.
   ═══════════════════════════════════════════════ */

'use strict';

/* ─── NAVIGAZIONE MOBILE ─── */
(function initMobileNav() {
  var toggle = document.querySelector('.nav-mobile-toggle');
  var links  = document.querySelector('.nav-links');
  if (!toggle || !links) return;

  toggle.addEventListener('click', function () {
    var isOpen = links.classList.toggle('open');
    toggle.classList.toggle('open', isOpen);
    toggle.setAttribute('aria-expanded', String(isOpen));
    document.body.style.overflow = isOpen ? 'hidden' : '';
  });

  links.querySelectorAll('a').forEach(function (a) {
    a.addEventListener('click', function () {
      links.classList.remove('open');
      toggle.classList.remove('open');
      toggle.setAttribute('aria-expanded', 'false');
      document.body.style.overflow = '';
    });
  });

  document.addEventListener('click', function (e) {
    if (!toggle.contains(e.target) && !links.contains(e.target)) {
      links.classList.remove('open');
      toggle.classList.remove('open');
      document.body.style.overflow = '';
    }
  });
}());

/* ─── OMBRA NAV ALLO SCROLL ─── */
(function initNavShadow() {
  var nav = document.querySelector('.nav');
  if (!nav) return;
  window.addEventListener('scroll', function () {
    nav.classList.toggle('scrolled', window.scrollY > 60);
  }, { passive: true });
}());

/* ─── AREA SWIPER (Mobile) ─── */
(function initAreaSwiper() {
  var swiper = document.getElementById('area-swiper');
  var dots = document.querySelectorAll('.swiper-dot');
  if (!swiper || !dots.length) return;

  /* Aggiorna dots in base alla posizione di scroll */
  var lastIndex = 0;
  swiper.addEventListener('scroll', function () {
    var scrollLeft = swiper.scrollLeft;
    var cardWidth = swiper.offsetWidth;
    var index = Math.round(scrollLeft / cardWidth);
    if (index !== lastIndex) {
      lastIndex = index;
      dots.forEach(function (dot, i) {
        dot.classList.toggle('active', i === index);
      });
    }
  }, { passive: true });

  /* Click su dot per navigare */
  dots.forEach(function (dot, i) {
    dot.addEventListener('click', function () {
      swiper.scrollTo({
        left: i * swiper.offsetWidth,
        behavior: 'smooth'
      });
    });
  });

  /* Auto-advance: avanza ogni 3 secondi, SEMPRE, non si ferma mai */
  var autoTimer = null;

  function startAuto() {
    if (window.innerWidth >= 900) return; /* Solo mobile */
    autoTimer = setInterval(function () {
      var next = (lastIndex + 1) % 4;
      swiper.scrollTo({
        left: next * swiper.offsetWidth,
        behavior: 'smooth'
      });
    }, 6000);
  }

  startAuto();
}());

/* ─── COOKIE BANNER ─── */
(function initCookie() {
  var banner = document.querySelector('.cookie-banner');
  if (!banner) return;
  if (localStorage.getItem('sli-cookie') === '1') return;

  setTimeout(function () {
    banner.classList.add('visible');
  }, 1800);

  var btn = banner.querySelector('.cookie-accept');
  if (btn) {
    btn.addEventListener('click', function () {
      localStorage.setItem('sli-cookie', '1');
      banner.classList.remove('visible');
      setTimeout(function () {
        var hero = document.querySelector('.hero, .hero-landing');
        var cta  = document.querySelector('.mobile-sticky-cta');
        if (cta && hero && !isInViewport(hero)) {
          cta.classList.add('visible');
        }
      }, 500);
    });
  }
}());

/* ─── MOBILE STICKY CTA ─── */
(function initStickyCta() {
  var cta    = document.querySelector('.mobile-sticky-cta');
  var cookie = document.querySelector('.cookie-banner');
  var hero   = document.querySelector('.hero, .hero-landing');
  if (!cta || !hero) return;

  var observer = new IntersectionObserver(function (entries) {
    var heroGone      = !entries[0].isIntersecting;
    var cookieVisible = cookie && cookie.classList.contains('visible');
    cta.classList.toggle('visible', heroGone && !cookieVisible);
  }, { threshold: 0.1 });

  observer.observe(hero);
}());

function isInViewport(el) {
  var r = el.getBoundingClientRect();
  return r.bottom > 0 && r.top < window.innerHeight;
}

/* ─── GESTIONE FORM (Formsubmit + AJAX) ─── */
function initForm(formEl) {
  if (!formEl) return;

  formEl.addEventListener('submit', async function (e) {
    e.preventDefault();

    var btn          = formEl.querySelector('.form-submit');
    var originalText = btn.textContent;
    var area         = formEl.dataset.area || 'Generale';

    btn.textContent = 'යවමින් පවතී…';
    btn.disabled = true;

    var prevErr = formEl.querySelector('.form-error');
    if (prevErr) prevErr.remove();

    try {
      var response = await fetch(formEl.action, {
        method:  'POST',
        body:    new FormData(formEl),
        headers: { 'Accept': 'application/json' }
      });

      var data = {};
      try { data = await response.json(); } catch (e) {}

      var ok = response.ok && (data.success === 'true' || data.success === true || data.ok);

      if (ok) {
        if (typeof gtag === 'function') {
          gtag('event', 'conversion', { send_to: 'AW-XXXXXXXXXX/XXXXXXXXXX' });
          gtag('event', 'form_submit', { event_category: 'Lead', event_label: area });
        }

        var container = formEl.closest('.form-container') || formEl.closest('.contatti-form-wrap') || formEl.parentElement;
        container.innerHTML = [
          '<div class="form-success">',
          '  <div class="form-success-icon">\u2713</div>',
          '  <h3>ඉල්ලීම සාර්ථකව යවන ලදී</h3>',
          '  <p>උපදේශනය සඳහා වන ඔබගේ ඉල්ලීම ලැබිණි.<br>',
          '  වේලාව තහවුරු කිරීම සඳහා පැය කිහිපයක් ඇතුළත අපි ඔබව නැවත සම්බන්ධ කර ගන්නෙමු.</p>',
          '</div>'
        ].join('');
      } else {
        throw new Error(data && data.message ? data.message : 'Errore invio');
      }

    } catch (err) {
      btn.textContent = originalText;
      btn.disabled = false;

      var errEl = document.createElement('p');
      errEl.className = 'form-error';
      errEl.textContent = 'දෝෂයක් සිදු විය. කරුණාකර studiolegalefrancescoiaccarino@outlook.com වෙත පණිවිඩයක් එවන්න';
      formEl.appendChild(errEl);
    }
  });
}

document.querySelectorAll('form[data-form]').forEach(initForm);

/* ─── ANIMAZIONI SCROLL (Intersection Observer) ─── */
(function initScrollAnimations() {
  if (!('IntersectionObserver' in window)) return;

  var targets = document.querySelectorAll('.area-card, .competenza, .perche-item, .caso, .step, .credential, .reato-card');

  var observer = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) {
        entry.target.style.opacity    = '1';
        entry.target.style.transform  = 'translateY(0)';
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });

  targets.forEach(function (el) {
    el.style.opacity   = '0';
    el.style.transform = 'translateY(20px)';
    el.style.transition = 'opacity 0.55s ease, transform 0.55s ease';
    observer.observe(el);
  });
}());
