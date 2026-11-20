/* ═══════════════════════════════════════════════
   STUDIO LEGALE IACCARINO — AI CHAT WIDGET
   Assistente virtuale per pre-qualificazione clienti
   ═══════════════════════════════════════════════ */

(function () {
  'use strict';

  // ─── Configurazione ───
  var CONFIG = {
    apiEndpoint: '/api/chat',
    studioName: 'Studio Legale Iaccarino',
    greeting: 'Здравствуйте! Я виртуальный ассистент Studio Legale Iaccarino. Расскажите о вашей ситуации, и мы с готовностью вам поможем.',
    quickReplies: [
      'Вопрос в сфере уголовного права',
      'Вопрос в сфере гражданского права',
      'Вопрос в сфере налогового права',
      'Вопрос в сфере иммиграционного права'
    ],
    emailEndpoint: 'https://formsubmit.co/ajax/studiolegalefrancescoiaccarino@outlook.com',
    consultaUrl: '/ru/consulenza.html',
    whatsappUrl: 'https://wa.me/393335684659'
  };

  // ─── Rileva path base per risorse ───
  var scripts = document.getElementsByTagName('script');
  var basePath = '';
  for (var i = 0; i < scripts.length; i++) {
    if (scripts[i].src && scripts[i].src.indexOf('chat-widget') !== -1) {
      basePath = scripts[i].src.replace(/js\/chat-widget\.js.*$/, '');
      break;
    }
  }
  var logoUrl = '/img/chat-logo.jpg';

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
      '<span class="acw-btn-text">Задайте вопрос, и мы решим Вашу проблему</span>' +
      '<span class="acw-btn-dot"></span>' +
      '</div>' +
      '<div class="acw-window" id="acw-window" role="dialog" aria-label="Chat assistente virtuale">' +
      '<div class="acw-header">' +
      '<div class="acw-header-info">' +
      '<div class="acw-avatar"><img src="' + logoUrl + '" alt="Logo" style="width:100%;height:100%;object-fit:contain;border-radius:50%;" /></div>' +
      '<div><div class="acw-header-name">Studio Legale Iaccarino</div>' +
      '<div class="acw-header-status"><span class="acw-status-dot"></span>ИИ-ассистент активен</div></div>' +
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
      addBotMessage('Выберите интересующую вас сферу или опишите вашу ситуацию напрямую:');
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
    msgDiv.innerHTML = '<div class="acw-msg-avatar"><img src="' + logoUrl + '" alt="" style="width:100%;height:100%;object-fit:contain;border-radius:50%;" /></div>' +
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
    typingDiv.innerHTML = '<div class="acw-msg-avatar"><img src="' + logoUrl + '" alt="" style="width:100%;height:100%;object-fit:contain;border-radius:50%;" /></div>' +
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

  // ─── Invia all'AI (Netlify Function) ───
  function sendToAI(text) {
    showTyping();

    var endpoint = CONFIG.apiEndpoint;

    fetch(endpoint, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        lang: 'ru', message: text,
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
          // Se c'è un follow-up (dopo |||), mostralo dopo 15 secondi
          if (data.followUp) {
            setTimeout(function () {
              showTyping();
              setTimeout(function () {
                hideTyping();
                addBotMessage(data.followUp);
                // Dopo 20s senza risposta, mostra i contatti dello studio
                var msgCountNow = state.userMessageCount;
                state.contactTimer = setTimeout(function () {
                  if (state.userMessageCount === msgCountNow) {
                    showTyping();
                    setTimeout(function () {
                      hideTyping();
                      addBotMessage('При желании вы можете связаться напрямую с адвокатом Avv. Iaccarino по телефону +39 333 568 4659 (доступен также в WhatsApp). Вы также можете забронировать онлайн-консультацию &mdash; стоимость первичного приема составляет 200 евро и в полном объеме засчитывается в счет последующего поручения на ведение дела.');
                      showActionButtons();
                    }, 2000);
                  }
                }, 18000); // 18s + 2s typing = 20s totali
              }, 2000); // 2s di "typing" per naturalezza
            }, 13000); // 13s + 2s typing = 15s totali
          } else if (data.showConsulta) {
            showActionButtons();
          }
        }
      })
      .catch(function () {
        hideTyping();
        handleFallback(text);
      });
  }

  // ─── Fallback senza API ───
  function handleFallback(text) {
    var lowerText = text.toLowerCase();
    var areaLabels = {
      'penale': 'уголовное право',
      'civile': 'гражданское право и возмещение ущерба',
      'tributario': 'налоговое право',
      'immigrazione': 'миграционное право'
    };

    if (state.area && !state._fallbackAreaDone) {
      state._fallbackAreaDone = true;
      var areaName = areaLabels[state.area] || 'интересующая вас отрасль права';
      addBotMessage('Опишите подробно, что произошло. Наша юридическая фирма обладает большим опытом в сфере ' + areaName + ' и я смогу указать вам на аналогичное дело из нашей практики, которое мы успешно разрешили.');
      return;
    }

    if (lowerText.indexOf('consult') !== -1 || lowerText.indexOf('prenot') !== -1 || lowerText.indexOf('appuntamento') !== -1) {
      addBotMessage('Отлично! Вы можете забронировать консультацию непосредственно на сайте или связаться с нами через WhatsApp для согласования встречи.');
      showActionButtons();
      return;
    }

    if (lowerText.indexOf('costo') !== -1 || lowerText.indexOf('prezzo') !== -1 || lowerText.indexOf('quanto') !== -1) {
      addBotMessage('Стоимость первичной консультации составляет 200 евро и включает детальный анализ дела и определение возможных стратегий защиты. Данная сумма засчитывается в стоимость услуг в случае заключения договора на ведение дела.');
      showActionButtons();
      return;
    }

    if (lowerText.indexOf('orari') !== -1 || lowerText.indexOf('dove') !== -1 || lowerText.indexOf('indirizzo') !== -1 || lowerText.indexOf('sede') !== -1) {
      addBotMessage('Офис юридической фирмы расположен в Palazzo di Domenico Barbaja в Неаполе. Мы работаем с понедельника по пятницу с 9:00 до 13:00 и с 15:00 до 19:00. Оказываем юридическую помощь на всей территории Италии.');
      return;
    }

    addBotMessage('Понимаю. Опишите подробнее вашу ситуацию: что произошло и когда? Так я смогу привести пример аналогичного дела, которое мы успешно разрешили, и объяснить, как мы можем вам помочь.');
  }

  // ─── Mostra bottoni azione ───
  function showActionButtons() {
    var container = document.getElementById('acw-quick');
    container.innerHTML = '';

    var areaParam = state.area ? '?area=' + state.area : '';

    var btnConsulta = document.createElement('a');
    btnConsulta.href = CONFIG.consultaUrl + areaParam;
    btnConsulta.className = 'acw-action-btn acw-action-primary';
    btnConsulta.textContent = 'Записаться на консультацию &mdash; 200 €';

    var btnWhatsapp = document.createElement('a');
    btnWhatsapp.href = CONFIG.whatsappUrl;
    btnWhatsapp.target = '_blank';
    btnWhatsapp.rel = 'noopener noreferrer';
    btnWhatsapp.className = 'acw-action-btn acw-action-whatsapp';
    btnWhatsapp.textContent = 'Написать в WhatsApp';

    var btnTel = document.createElement('a');
    btnTel.href = 'tel:+393335684659';
    btnTel.className = 'acw-action-btn acw-action-tel';
    btnTel.textContent = 'Позвонить сейчас';

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
