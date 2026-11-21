/* ═══════════════════════════════════════════════
   STUDIO LEGALE IACCARINO — AI CHAT WIDGET
   Assistente virtuale per pre-qualificazione clienti
   ═══════════════════════════════════════════════ */

(function () {
  'use strict';

  // ─── Configurazione ───
  var CONFIG = {
    apiEndpoint: null,
    studioName: 'Studio Legale Iaccarino',
    greeting: 'Buongiorno! Sono l\'assistente virtuale dello Studio Legale Iaccarino. Mi racconti il suo problema: saremo felici di aiutarla.',
    quickReplies: [
      'Ho un problema penale',
      'Ho un problema civile',
      'Ho un problema tributario',
      'Ho un problema di immigrazione'
    ],
    emailEndpoint: 'https://formsubmit.co/ajax/studiolegalefrancescoiaccarino@outlook.com',
    consultaUrl: '/consulenza.html',
    whatsappUrl: 'https://wa.me/393335684659'
  };

  var logoUrl = '/img/foto-avvocato-profilo.jpg';

  // ─── Stato ───
  var state = {
    isOpen: false,
    messages: [],
    history: [],
    isTyping: false,
    step: 'greeting',
    area: null,
    useAI: true,
    userMessageCount: 0,
    emailSent: false
  };

  // ─── Crea il widget ───
  function createWidget() {
    var widget = document.createElement('div');
    widget.id = 'ai-chat-widget';
    widget.innerHTML = '<div class="acw-btn" id="acw-btn" role="button" tabindex="0" aria-label="Apri assistente virtuale">' +
      '<img class="acw-btn-logo" src="' + logoUrl + '" alt="Studio Legale Iaccarino" />' +
      '<span class="acw-btn-text">Chiedi e risolviamo il tuo problema</span>' +
      '<span class="acw-btn-dot"></span>' +
      '</div>' +
      '<div class="acw-window" id="acw-window" role="dialog" aria-label="Chat assistente virtuale">' +
      '<div class="acw-header">' +
      '<div class="acw-header-info">' +
      '<div class="acw-avatar"><img src="' + logoUrl + '" alt="Logo" style="width:100%;height:100%;object-fit:cover;border-radius:50%;" /></div>' +
      '<div><div class="acw-header-name">Studio Legale Iaccarino</div>' +
      '<div class="acw-header-status"><span class="acw-status-dot"></span> Assistente AI attivo</div></div>' +
      '</div>' +
      '<button class="acw-close" id="acw-close" aria-label="Chiudi chat">&times;</button>' +
      '</div>' +
      '<div class="acw-messages" id="acw-messages"></div>' +
      '<div class="acw-quick-replies" id="acw-quick"></div>' +
      '<div class="acw-input-wrap" id="acw-input-wrap">' +
      '<textarea class="acw-input" id="acw-input" placeholder="Descriva qui il suo problema..." rows="1"></textarea>' +
      '<button class="acw-send" id="acw-send" aria-label="Invia messaggio">' +
      '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">' +
      '<line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/></svg>' +
      '</button>' +
      '</div>' +
      '</div>';
    document.body.appendChild(widget);

    // Event listeners
    var btn = document.getElementById('acw-btn');
    var closeBtn = document.getElementById('acw-close');
    var input = document.getElementById('acw-input');
    var sendBtn = document.getElementById('acw-send');

    btn.addEventListener('click', openChat);
    btn.addEventListener('keydown', function (e) { if (e.key === 'Enter') openChat(); });
    closeBtn.addEventListener('click', closeChat);
    sendBtn.addEventListener('click', sendMessage);
    input.addEventListener('keydown', function (e) {
      if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); sendMessage(); }
    });
    input.addEventListener('input', autoResize);

    // ─── Tasto indietro mobile: chiude la chat invece di uscire dal sito ───
    window.addEventListener('popstate', function () {
      if (state.isOpen) {
        closeChat();
      }
    });

    // ─── Invio email anche se il cliente chiude il browser/tab ───
    window.addEventListener('beforeunload', function () {
      if (state.userMessageCount > 0 && !state.emailSent) {
        sendConversationEmailSync();
      }
    });
  }

  // ─── Apri chat ───
  function openChat() {
    if (state.isOpen) return;
    state.isOpen = true;
    var widget = document.getElementById('ai-chat-widget');
    widget.classList.add('acw-open');
    if (state.messages.length === 0) showGreeting();
    setTimeout(function () { document.getElementById('acw-input').focus(); }, 300);
    // Pusho stato nella history del browser per intercettare il tasto indietro
    history.pushState({ chatOpen: true }, '');
  }

  // ─── Chiudi chat e invia email ───
  function closeChat() {
    if (!state.isOpen) return;
    state.isOpen = false;
    document.getElementById('ai-chat-widget').classList.remove('acw-open');
    // Invia email con la conversazione se ci sono messaggi dell'utente
    if (state.userMessageCount > 0 && !state.emailSent) {
      sendConversationEmail();
    }
  }

  // ─── Invia conversazione via email (async, per chiusura chat / tasto indietro) ───
  function sendConversationEmail() {
    state.emailSent = true;
    var payload = buildEmailPayload();

    fetch(CONFIG.emailEndpoint, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
      body: JSON.stringify(payload)
    }).catch(function () { /* silenzioso */ });
  }

  // ─── Invia conversazione via email (sync, per beforeunload) ───
  function sendConversationEmailSync() {
    state.emailSent = true;
    var payload = buildEmailPayload();
    var blob = new Blob([JSON.stringify(payload)], { type: 'application/json' });
    navigator.sendBeacon(CONFIG.emailEndpoint, blob);
  }

  // ─── Estrai numero di telefono dai messaggi ───
  function extractPhoneNumber() {
    var phoneRegex = /(?:\+?\d{1,3}[\s.-]?)?\(?\d{2,4}\)?[\s.-]?\d{3,4}[\s.-]?\d{3,4}/g;
    for (var i = state.messages.length - 1; i >= 0; i--) {
      if (state.messages[i].role === 'user') {
        var matches = state.messages[i].text.match(phoneRegex);
        if (matches) {
          // Prendi il match più lungo (più probabile sia un numero completo)
          var best = matches.sort(function (a, b) { return b.length - a.length; })[0];
          // Controlla che abbia almeno 8 cifre
          var digits = best.replace(/\D/g, '');
          if (digits.length >= 8) return best.trim();
        }
      }
    }
    return 'Non fornito';
  }

  // ─── Costruisci il payload email ───
  function buildEmailPayload() {
    var conversationText = '';
    var userMessages = [];
    state.messages.forEach(function (msg) {
      var prefix = msg.role === 'user' ? 'CLIENTE' : 'ASSISTENTE AI';
      conversationText += prefix + ': ' + msg.text + '\n\n';
      if (msg.role === 'user') userMessages.push(msg.text);
    });

    var area = state.area ? state.area.toUpperCase() : 'Non specificata';
    var phone = extractPhoneNumber();
    var now = new Date();
    var timestamp = now.toLocaleDateString('it-IT') + ' ' + now.toLocaleTimeString('it-IT');
    var pagina = window.location.href;

    return {
      _subject: 'Chatbot AI — Nuova conversazione (' + area + ') — Tel: ' + phone,
      'Telefono cliente': phone,
      'Area legale': area,
      'Data e ora': timestamp,
      'Pagina': pagina,
      'Riepilogo messaggi cliente': userMessages.join(' | '),
      'Conversazione completa': conversationText,
      _template: 'table'
    };
  }

  // ─── Mostra saluto iniziale ───
  function showGreeting() {
    addBotMessage(CONFIG.greeting);
    setTimeout(function () {
      addBotMessage('Scelga pure l\'area che la riguarda, oppure mi descriva direttamente la sua situazione:');
      showQuickReplies(CONFIG.quickReplies);
    }, 800);
  }

  // ─── Aggiungi messaggio bot ───
  function addBotMessage(text) {
    state.messages.push({ role: 'assistant', text: text });
    state.history.push({ role: 'assistant', content: text });
    var container = document.getElementById('acw-messages');
    var msgDiv = document.createElement('div');
    msgDiv.className = 'acw-msg acw-msg-bot acw-msg-enter';
    msgDiv.innerHTML = '<div class="acw-msg-avatar"><img src="' + logoUrl + '" alt="" style="width:100%;height:100%;object-fit:cover;border-radius:50%;" /></div>' +
      '<div class="acw-msg-bubble">' + formatText(text) + '</div>';
    container.appendChild(msgDiv);
    scrollToBottom();
  }

  // ─── Aggiungi messaggio utente ───
  function addUserMessage(text) {
    state.messages.push({ role: 'user', text: text });
    state.history.push({ role: 'user', content: text });
    state.userMessageCount++;
    var container = document.getElementById('acw-messages');
    var msgDiv = document.createElement('div');
    msgDiv.className = 'acw-msg acw-msg-user acw-msg-enter';
    msgDiv.innerHTML = '<div class="acw-msg-bubble">' + escapeHtml(text) + '</div>';
    container.appendChild(msgDiv);
    scrollToBottom();
  }

  // ─── Quick replies ───
  function showQuickReplies(options) {
    var container = document.getElementById('acw-quick');
    container.innerHTML = '';
    options.forEach(function (opt) {
      var btn = document.createElement('button');
      btn.className = 'acw-qr';
      btn.textContent = opt;
      btn.addEventListener('click', function () {
        container.innerHTML = '';
        handleUserInput(opt);
      });
      container.appendChild(btn);
    });
    scrollToBottom();
  }

  // ─── Mostra indicatore di digitazione ───
  function showTyping() {
    state.isTyping = true;
    var container = document.getElementById('acw-messages');
    var typingDiv = document.createElement('div');
    typingDiv.id = 'acw-typing';
    typingDiv.className = 'acw-msg acw-msg-bot acw-msg-enter';
    typingDiv.innerHTML = '<div class="acw-msg-avatar"><img src="' + logoUrl + '" alt="" style="width:100%;height:100%;object-fit:cover;border-radius:50%;" /></div>' +
      '<div class="acw-msg-bubble acw-typing"><span></span><span></span><span></span></div>';
    container.appendChild(typingDiv);
    scrollToBottom();
  }

  function hideTyping() {
    state.isTyping = false;
    var el = document.getElementById('acw-typing');
    if (el) el.remove();
  }

  // ─── Invia messaggio ───
  function sendMessage() {
    var input = document.getElementById('acw-input');
    var text = input.value.trim();
    if (!text) return;
    input.value = '';
    input.style.height = 'auto';
    handleUserInput(text);
  }

  // ─── Gestisci input utente ───
  function handleUserInput(text) {
    addUserMessage(text);
    document.getElementById('acw-quick').innerHTML = '';
    // Cancella il timer dei contatti se l'utente risponde
    if (state.contactTimer) {
      clearTimeout(state.contactTimer);
      state.contactTimer = null;
    }

    // Determina area dalla risposta
    var lowerText = text.toLowerCase();

    if (state.step === 'greeting') {
      if (lowerText.indexOf('penale') !== -1) state.area = 'penale';
      else if (lowerText.indexOf('civile') !== -1 || lowerText.indexOf('risarcimento') !== -1 || lowerText.indexOf('causa') !== -1) state.area = 'civile';
      else if (lowerText.indexOf('cartella') !== -1 || lowerText.indexOf('tributar') !== -1 || lowerText.indexOf('fiscal') !== -1 || lowerText.indexOf('esattorial') !== -1 || lowerText.indexOf('agenzia entrate') !== -1) state.area = 'tributario';
      else if (lowerText.indexOf('immigra') !== -1 || lowerText.indexOf('permesso') !== -1 || lowerText.indexOf('soggiorno') !== -1 || lowerText.indexOf('cittadinanza') !== -1) state.area = 'immigrazione';

      state.step = 'chat';
      sendToAI(text);
      return;
    }

    // Se siamo in modalita chat libera, invia all'AI
    sendToAI(text);
  }

  // ─── Invia all'AI (API esterna se configurata, altrimenti motore guidato integrato) ───
  function sendToAI(text) {
    showTyping();

    var endpoint = CONFIG.apiEndpoint;
    if (!endpoint) {
      setTimeout(function () {
        hideTyping();
        handleSmartFlow(text);
      }, 650);
      return;
    }

    fetch(endpoint, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        message: text,
        history: state.history.slice(0, -1),
        area: state.area
      })
    })
      .then(function (res) {
        if (!res.ok) throw new Error('API non disponibile');
        return res.json();
      })
      .then(function (data) {
        hideTyping();
        if (data.reply) {
          addBotMessage(data.reply);
          if (data.followUp) {
            scheduleFollowUp(data.followUp);
          } else if (data.showConsulta) {
            showActionButtons();
          }
        }
      })
      .catch(function () {
        hideTyping();
        handleSmartFlow(text);
      });
  }

  function scheduleFollowUp(followUpText) {
    setTimeout(function () {
      showTyping();
      setTimeout(function () {
        hideTyping();
        addBotMessage(followUpText);
        showActionButtons();
        var msgCountNow = state.userMessageCount;
        state.contactTimer = setTimeout(function () {
          if (state.userMessageCount === msgCountNow) {
            showTyping();
            setTimeout(function () {
              hideTyping();
              addBotMessage('Se preferisce, può contattare direttamente l\'Avv. Iaccarino al +39 333 568 4659, disponibile anche su WhatsApp. La prima consulenza ha un costo di €200, interamente deducibili dal mandato professionale.');
              showActionButtons();
            }, 1500);
          }
        }, 18000);
      }, 1500);
    }, 3500);
  }

  // ─── Motore conversazionale a 3 fasi con casi reali dello Studio ───
  function detectArea(lowerText) {
    if (/(penal|arrest|carcer|denunc|querel|avviso|garanzia|sequestr|misura|cautelar|truff|frode|stupefac|droga|maltratt|stalking|processo|imputat)/.test(lowerText)) return 'penale';
    if (/(tribut|cartell|agenzia entrate|fisco|esattorial|accertament|redditometro|fermo amministrativo|ipoteca|cgt|rottamazione|pignorament)/.test(lowerText)) return 'tributario';
    if (/(immigra|permess|soggiorn|cittadinanz|espulsion|questura|prefettura|visto|ricongiung|iure sanguinis|decreto flussi)/.test(lowerText)) return 'immigrazione';
    if (/(civil|divorz|separaz|affidament|manteniment|lavor|licenziament|risarciment|incident|sinistr|condomini|contrat|credit|eredit|casa)/.test(lowerText)) return 'civile';
    return state.area || null;
  }

  function pickRealCase(area, lowerText) {
    if (area === 'penale') {
      if (/(truff|frode|informatic|edile|assicur)/.test(lowerText)) {
        return 'Abbiamo affrontato una situazione simile alla sua: in un caso di truffa vendita online da €4.800 al Tribunale di Napoli abbiamo ottenuto l\'assoluzione piena, così come l\'assoluzione per frode informatica da €12.500 al Tribunale di Milano.';
      }
      if (/(tenuit|querela|liev|telefon)/.test(lowerText)) {
        return 'Abbiamo affrontato una situazione simile alla sua: al Tribunale di Salerno abbiamo ottenuto la non punibilità per particolare tenuità del fatto, e al Tribunale di Napoli Nord la chiusura con remissione di querela.';
      }
      return 'Abbiamo affrontato situazioni simili alla sua in ambito penale: lo Studio assiste quotidianamente indagati e imputati davanti ai Tribunali di Napoli, Roma e Milano, ottenendo assoluzioni piene e archiviazioni.';
    }
    if (area === 'civile') {
      if (/(divorz|separaz|assegno|casa|affidament|figl|matrimon)/.test(lowerText)) {
        return 'Abbiamo affrontato una situazione simile alla sua: in un divorzio con patrimonio occulto al Tribunale di Napoli (2023) abbiamo ottenuto l\'assegno pieno e l\'assegnazione della casa, e in Corte d\'Appello di Napoli (2024) una revisione dell\'assegno da €1.400 a €400.';
      }
      return 'Abbiamo affrontato situazioni simili alla sua in diritto civile e del lavoro: lo Studio tutela clienti in tutta Italia su famiglia, risarcimenti, licenziamenti e recupero crediti.';
    }
    if (area === 'tributario') {
      if (/(redditometro|induttivo|accertament|ricavi)/.test(lowerText)) {
        return 'Abbiamo affrontato una situazione simile alla sua: davanti alla CGT di Napoli (2024) abbiamo ottenuto l\'annullamento di un redditometro da €87.400 e la riduzione dell\'80% di un accertamento induttivo da €142.000 a €28.600.';
      }
      return 'Abbiamo affrontato una situazione simile alla sua: davanti alla CGT di Napoli (2023) abbiamo ottenuto l\'annullamento per decadenza dei termini su una pretesa da €53.800 e in mediazione una riduzione da €38.400 a €9.800.';
    }
    if (area === 'immigrazione') {
      if (/(cittadinanz|iure sanguinis|silenzio|ritard|1100|tar)/.test(lowerText)) {
        return 'Abbiamo affrontato una situazione simile alla sua: davanti al TAR Lazio (2024) abbiamo vinto un ricorso contro il silenzio-inadempimento dopo 1.100 giorni ottenendo la cittadinanza, e al Tribunale di Roma (2024) il passaporto iure sanguinis.';
      }
      return 'Abbiamo affrontato una situazione simile alla sua: al Tribunale di Roma (2023) abbiamo ottenuto l\'annullamento di un diniego per precedente estinto e nel 2024 la revoca di un diniego per interruzione della residenza.';
    }
    return 'Lo Studio Legale Iaccarino tratta abitualmente questa materia su tutto il territorio nazionale con difesa dedicata in sede giudiziale e stragiudiziale.';
  }

  function handleSmartFlow(text) {
    var lowerText = text.toLowerCase();
    var phoneDigits = text.replace(/\D/g, '');

    if (phoneDigits.length >= 8) {
      if (!state.emailSent) sendConversationEmail();
      addBotMessage('Grazie, abbiamo registrato il suo recapito. L\'Avv. Francesco Iaccarino la ricontatterà al più presto. Se il caso è urgente può chiamare subito il +39 333 568 4659.');
      showActionButtons();
      return;
    }

    var detected = detectArea(lowerText);
    if (detected) state.area = detected;

    if (/(costo|prezzo|quanto costa|onorario|parcel)/.test(lowerText)) {
      addBotMessage('La prima consulenza legale, in studio a Via Toledo 205 (Palazzo Barbaja, Napoli) oppure al telefono o in videochiamata, ha un costo fisso di €200, interamente deducibili dal compenso in caso di conferimento del mandato.');
      showActionButtons();
      return;
    }

    if (/(orari|dove|indirizzo|sede|palazzo|toledo)/.test(lowerText)) {
      addBotMessage('Lo Studio si trova a Napoli in Via Toledo 205 (Palazzo di Domenico Barbaja). Riceviamo dal lunedì al venerdì dalle 9:00 alle 13:00 e dalle 15:00 alle 19:00, e assistiamo clienti in tutta Italia.');
      showActionButtons();
      return;
    }

    if (/(urgen|arrest|ferm|sequestr|perquisiz|subito)/.test(lowerText)) {
      addBotMessage(pickRealCase(state.area, lowerText));
      addBotMessage('Trattandosi di una situazione urgente, le consiglio di chiamare subito il +39 333 568 4659 oppure di lasciarmi qui il suo numero di telefono per essere richiamata immediatamente.');
      showActionButtons();
      return;
    }

    var isGenericAreaOnly = /^(ho un problema|problema)\s+(penale|civile|tributario|di immigrazione)\.?$/i.test(text.trim());
    if (isGenericAreaOnly && !state._askedDetails) {
      state._askedDetails = true;
      var areaLabels = {
        'penale': 'diritto penale',
        'civile': 'diritto civile e del lavoro',
        'tributario': 'diritto tributario',
        'immigrazione': 'diritto dell\'immigrazione'
      };
      addBotMessage('Capisco, si tratta di ' + (areaLabels[state.area] || 'una questione legale') + '. Mi racconti brevemente cosa è successo e quando, così posso indicarle subito un caso simile già risolto dallo Studio.');
      return;
    }

    if (!state._casePresented) {
      state._casePresented = true;
      addBotMessage(pickRealCase(state.area, lowerText));
      scheduleFollowUp('Per poterla ricontattare e valutare i documenti, mi lasci il suo recapito telefonico. La prima consulenza costa €200 ed è interamente deducibile dal mandato.');
      return;
    }

    addBotMessage('Ho annotato anche questi dettagli. Mi lasci pure il suo numero di telefono qui in chat, oppure utilizzi i pulsanti qui sotto per prenotare la consulenza (€200 deducibili) o scrivere su WhatsApp.');
    showActionButtons();
  }

  // ─── Mostra bottoni azione ───
  function showActionButtons() {
    var container = document.getElementById('acw-quick');
    container.innerHTML = '';

    var areaParam = state.area ? '?area=' + state.area : '';

    var btnConsulta = document.createElement('a');
    btnConsulta.href = CONFIG.consultaUrl + areaParam;
    btnConsulta.className = 'acw-action-btn acw-action-primary';
    btnConsulta.textContent = 'Prenota Consulenza — \u20AC 200';

    var btnWhatsapp = document.createElement('a');
    btnWhatsapp.href = CONFIG.whatsappUrl;
    btnWhatsapp.target = '_blank';
    btnWhatsapp.rel = 'noopener noreferrer';
    btnWhatsapp.className = 'acw-action-btn acw-action-whatsapp';
    btnWhatsapp.textContent = 'Scrivi su WhatsApp';

    var btnTel = document.createElement('a');
    btnTel.href = 'tel:+393335684659';
    btnTel.className = 'acw-action-btn acw-action-tel';
    btnTel.textContent = 'Chiama ora';

    container.appendChild(btnConsulta);
    container.appendChild(btnWhatsapp);
    container.appendChild(btnTel);
    scrollToBottom();
  }

  // ─── Utilità ───
  function scrollToBottom() {
    var container = document.getElementById('acw-messages');
    setTimeout(function () { container.scrollTop = container.scrollHeight; }, 100);
  }

  function autoResize() {
    this.style.height = 'auto';
    this.style.height = Math.min(this.scrollHeight, 100) + 'px';
  }

  function escapeHtml(text) {
    var div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
  }

  function formatText(text) {
    return escapeHtml(text)
      .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
      .replace(/\n/g, '<br>');
  }

  // ─── Inizializza ───
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', createWidget);
  } else {
    createWidget();
  }

})();
