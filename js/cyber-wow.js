/* Interazioni Executive Cyber-Legal: progress bar, spotlight, bussola 30 minuti, filtro 70 scenari */
(function () {
  // 1. Barra avanzamento lettura
  var bar = document.querySelector('.cy-progress');
  if (bar) {
    var upd = function () {
      var h = document.documentElement;
      var max = (h.scrollHeight - h.clientHeight) || 1;
      bar.style.width = Math.min(100, Math.max(0, (window.scrollY / max) * 100)) + '%';
    };
    window.addEventListener('scroll', upd, { passive: true });
    upd();
  }

  // 2. Effetto spotlight sulle card pilastro
  document.querySelectorAll('.cy-pillar-card').forEach(function (card) {
    card.addEventListener('mousemove', function (e) {
      var r = card.getBoundingClientRect();
      card.style.setProperty('--mx', (e.clientX - r.left) + 'px');
      card.style.setProperty('--my', (e.clientY - r.top) + 'px');
    });
  });

  // 3. Bussola Interattiva "Che cosa è successo?"
  var compassDataEl = document.getElementById('cy-compass-data');
  var compassBtns = document.querySelectorAll('.cy-compass-btn');
  if (compassDataEl && compassBtns.length) {
    try {
      var data = JSON.parse(compassDataEl.textContent);
      var titleEl = document.getElementById('cy-c-title');
      var descEl = document.getElementById('cy-c-desc');
      var stepsEl = document.getElementById('cy-c-steps');
      var deadlineEl = document.getElementById('cy-c-deadline');
      var normEl = document.getElementById('cy-c-norm');
      var authEl = document.getElementById('cy-c-auth');
      var linkEl = document.getElementById('cy-c-link');

      var renderCompass = function (key) {
        var item = data[key];
        if (!item) return;
        titleEl.textContent = item.title;
        descEl.textContent = item.desc;
        stepsEl.innerHTML = '';
        item.steps.forEach(function (s) {
          var li = document.createElement('li');
          li.textContent = s;
          stepsEl.appendChild(li);
        });
        deadlineEl.textContent = item.deadline;
        normEl.textContent = item.norm;
        authEl.textContent = item.auth;
        linkEl.setAttribute('href', item.href);
        linkEl.textContent = item.cta;
      };

      compassBtns.forEach(function (btn) {
        btn.addEventListener('click', function () {
          compassBtns.forEach(function (b) { b.classList.remove('active'); });
          btn.classList.add('active');
          renderCompass(btn.getAttribute('data-key'));
        });
      });
      renderCompass(compassBtns[0].getAttribute('data-key'));
    } catch (e) {}
  }

  // 4. Filtro istantaneo + ricerca live sui 70 scenari operativi
  var searchInput = document.getElementById('cy-scenario-search');
  var pills = document.querySelectorAll('.cy-filter-pill');
  var cards = document.querySelectorAll('.cy-scenario-card');
  var countEl = document.getElementById('cy-scenario-count');
  var showMoreBtn = document.getElementById('cy-show-all');
  var activeCat = 'tutti';
  var expanded = !showMoreBtn;

  if (cards.length) {
    var applyFilter = function () {
      var q = (searchInput ? searchInput.value : '').trim().toLowerCase();
      var visible = 0;
      var matched = 0;
      cards.forEach(function (c) {
        var cat = c.getAttribute('data-cat') || '';
        var txt = (c.getAttribute('data-search') || c.textContent || '').toLowerCase();
        var okCat = (activeCat === 'tutti' || cat === activeCat);
        var okQ = (!q || txt.indexOf(q) !== -1);
        if (okCat && okQ) {
          matched++;
          if (expanded || q || activeCat !== 'tutti' || matched <= 18) {
            c.style.display = '';
            visible++;
          } else {
            c.style.display = 'none';
          }
        } else {
          c.style.display = 'none';
        }
      });
      if (countEl) {
        countEl.textContent = 'Mostrati ' + visible + ' di ' + matched + ' scenari operativi corrispondenti (archivio completo: ' + cards.length + ' protocolli)';
      }
      if (showMoreBtn) {
        showMoreBtn.style.display = (!expanded && !q && activeCat === 'tutti' && matched > 18) ? 'inline-flex' : 'none';
      }
    };

    pills.forEach(function (p) {
      p.addEventListener('click', function () {
        pills.forEach(function (x) { x.classList.remove('active'); });
        p.classList.add('active');
        activeCat = p.getAttribute('data-cat') || 'tutti';
        applyFilter();
      });
    });
    if (searchInput) searchInput.addEventListener('input', applyFilter);
    if (showMoreBtn) {
      showMoreBtn.addEventListener('click', function () {
        expanded = true;
        applyFilter();
      });
    }
    applyFilter();
  }
})();
