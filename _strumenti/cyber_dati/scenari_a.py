# -*- coding: utf-8 -*-
"""Scenari operativi e protocolli di difesa 01-35 (Data Breach/GDPR, Ransomware/NIS2, Truffe/Banche, Penale parte 1)."""

SCENARI_A = [
    # ═══════════════════ 1. DATA BREACH & GDPR (01-10) ═══════════════════
    {
        "cod": "CYB-01", "slug": "notifica-data-breach-garante-72-ore-azienda",
        "cat": "data-breach", "cat_lbl": "Data Breach & GDPR", "pilastro": "data-breach-garante-privacy",
        "titolo": "Data breach su database clienti: notifica al Garante entro 72 ore",
        "seo_title": "Data Breach Database Clienti: Notifica Garante 72 Ore",
        "desc": "Protocollo operativo per violazione di database clienti: valutazione rischio, notifica al Garante Privacy ex art. 33 GDPR entro 72 ore e registro interno.",
        "keywords": ["data breach database clienti", "notifica garante privacy 72 ore", "art 33 gdpr", "furto dati clienti azienda"],
        "norme": ["Art. 33 GDPR", "Art. 34 GDPR", "Art. 83 par. 4 GDPR"],
        "scenario": "Un'azienda rileva l'esportazione non autorizzata dell'archivio anagrafico e fiscale dei clienti da un portale web o da un gestionale interno.",
        "rischio": "Esposizione a sanzioni fino a 10 milioni di euro o al 2% del fatturato globale per omessa notifica, oltre a richieste risarcitorie ex art. 82 GDPR.",
        "protocollo": [
            "Bloccare immediatamente l'endpoint vulnerabile e revocare le sessioni attive conservando i log integrali.",
            "Quantificare record e categorie di dati esposti (comuni, bancari, sanitari) per misurare il rischio sugli interessati.",
            "Inviare la notifica telematica al Garante entro 72 ore (anche in prima fase provvisoria ex art. 33 par. 4 GDPR).",
            "Valutare se il rischio e' elevato per inviare la comunicazione trasparente ai clienti ex art. 34 GDPR."
        ],
        "prove": ["Log di accesso applicativo e firewall", "Elenco campi esportati", "Cronologia scoperta incidente", "Evidenza patch di sicurezza"],
        "errori": ["Cancellare o sovrascrivere i log riavviando il server senza copia forense", "Aspettare la fine completa delle indagini IT superando le 72 ore senza prima notifica", "Sottovalutare l'obbligo di annotazione nel registro interno ex art. 33 par. 5 GDPR"]
    },
    {
        "cod": "CYB-02", "slug": "email-inviata-cc-invece-ccn-violazione-privacy",
        "cat": "data-breach", "cat_lbl": "Data Breach & GDPR", "pilastro": "data-breach-garante-privacy",
        "titolo": "Invio email massiva in CC invece che CCN: quando e' data breach",
        "seo_title": "Email in CC invece di CCN: Data Breach e Garante Privacy",
        "desc": "Quando l'invio errato di indirizzi email in campo CC integra una violazione GDPR, come valutare il rischio e se occorre notificare al Garante.",
        "keywords": ["email cc invece ccn gdpr", "data breach email errata", "violazione privacy indirizzo email"],
        "norme": ["Art. 4 n. 12 GDPR", "Art. 33 GDPR", "Art. 32 GDPR"],
        "scenario": "Un operatore invia una comunicazione commerciale, sanitaria o sindacale inserendo centinaia di destinatari nel campo CC visibile anziche' in CCN.",
        "rischio": "Rivelazione indebita di dati personali o addirittura di dati particolari ex art. 9 GDPR (es. appartenenza a pazienti di una clinica o iscritti a un sindacato).",
        "protocollo": [
            "Verificare subito se l'oggetto o il mittente dell'email rivela categorie particolari di dati (salute, contenziosi, debito).",
            "Richiedere ai destinatari la cancellazione immediata del messaggio e documentare la misura di mitigazione.",
            "Se sono coinvolti dati sensibili o soggetti vulnerabili, procedere con notifica al Garante entro 72 ore.",
            "Aggiornare le procedure interne e configurare blocchi tecnici sul client di posta per invii multipli."
        ],
        "prove": ["Copia dell'email inviata con intestazioni complete", "Numero esatto di destinatari", "Email di rettifica e richiesta cancellazione", "Scheda di valutazione rischio nel registro breach"],
        "errori": ["Ignorare l'accaduto sperando che nessuno segnali al Garante", "Inviare una seconda email di scuse ancora in CC ripetendo la violazione", "Non formare il personale dopo l'errore umano"]
    },
    {
        "cod": "CYB-03", "slug": "smarrimento-furto-pc-smartphone-aziendale-non-cifrato",
        "cat": "data-breach", "cat_lbl": "Data Breach & GDPR", "pilastro": "data-breach-garante-privacy",
        "titolo": "Furto o smarrimento di laptop o smartphone aziendale con dati clienti",
        "seo_title": "Furto PC Aziendale con Dati Clienti: Obblighi GDPR 72 Ore",
        "desc": "Cosa fare in caso di furto di computer o telefono aziendale: differenza tra dispositivo cifrato e non cifrato, remote wipe, denuncia e notifica Garante.",
        "keywords": ["furto pc aziendale gdpr", "smarrimento smartphone aziendale data breach", "cifratura disco art 34 gdpr"],
        "norme": ["Art. 32 GDPR", "Art. 33 GDPR", "Art. 34 par. 3 lett. a GDPR"],
        "scenario": "Un dipendente o un professionista subisce il furto in auto o in treno del portatile aziendale contenente contratti, buste paga o cartelle cliniche.",
        "rischio": "Se il disco non e' cifrato, chiunque puo' accedere ai file locali rendendo obbligatoria la notifica al Garante e spesso la comunicazione ai singoli interessati.",
        "protocollo": [
            "Attivare immediatamente il comando di blocco e cancellazione da remoto (MDM / remote wipe) e revocare token email e VPN.",
            "Verificare tecnicamente se il disco era protetto da cifratura integrale (es. BitLocker / FileVault) e password robusta.",
            "Sporgere denuncia di furto indicando matricola del dispositivo e attivare l'analisi legale sulle 72 ore.",
            "Se il dispositivo era cifrato in modo certificabile, documentare l'esenzione nel registro interno; se non cifrato, preparare la notifica."
        ],
        "prove": ["Log MDM che attestano cifratura attiva e comando remote wipe", "Denuncia alle forze dell'ordine", "Inventario dei file sincronizzati in locale", "Revoca credenziali Active Directory / cloud"],
        "errori": ["Dichiarare al Garante che il PC era cifrato senza prova tecnica", "Dimenticare di revocare i token di accesso alle app cloud", "Non avere una policy BYOD o MDM sui dispositivi mobili"]
    },
    {
        "cod": "CYB-04", "slug": "data-breach-fornitore-cloud-software-house-art-28",
        "cat": "data-breach", "cat_lbl": "Data Breach & GDPR", "pilastro": "data-breach-garante-privacy",
        "titolo": "Violazione dati presso un fornitore cloud o gestionale in SaaS",
        "seo_title": "Data Breach Fornitore Cloud SaaS: Responsabilita' Art. 28 GDPR",
        "desc": "Come gestire un incidente informatico subito dal fornitore gestionale o cloud: obblighi di informativa del responsabile, notifica del titolare e rivalsa contrattuale.",
        "keywords": ["data breach fornitore cloud", "responsabile trattamento art 28 gdpr", "rivalsa software house violazione dati"],
        "norme": ["Art. 28 GDPR", "Art. 33 par. 2 GDPR", "Art. 82 GDPR"],
        "scenario": "La software house o il provider cloud che ospita il gestionale aziendale comunica di aver subito un'intrusione con esposizione dei dati dei propri clienti.",
        "rischio": "L'obbligo di notifica al Garante resta in capo al titolare del trattamento (l'azienda cliente), che rischia sanzioni se rimane inerte aspettando il fornitore.",
        "protocollo": [
            "Esigere subito dal fornitore un report tecnico scritto con data della scoperta, dati coinvolti e misure di contenimento.",
            "Calcolare il termine di 72 ore dal momento in cui il titolare riceve la notizia certa dal responsabile.",
            "Verificare il Data Processing Agreement (art. 28 GDPR) e il contratto SLA per contestare eventuali ritardi o carenze di sicurezza.",
            "Notificare al Garante e riservare formalmente ogni azione di manleva e risarcimento verso il fornitore."
        ],
        "prove": ["Comunicazione ufficiale del fornitore con data e ora", "Contratto SaaS e DPA art. 28 GDPR", "Report forense del provider", "Eventuali penali o limiti di responsabilita'"],
        "errori": ["Pensare che basti la notifica fatta dal fornitore", "Accettare risposte vaghe del provider senza tracciarle via PEC", "Non verificare se il fornitore usava sub-responsabili non autorizzati"]
    },
    {
        "cod": "CYB-05", "slug": "cartelle-cliniche-dati-sanitari-esposti-studio-medico",
        "cat": "data-breach", "cat_lbl": "Data Breach & GDPR", "pilastro": "data-breach-garante-privacy",
        "titolo": "Esposizione o invio errato di referti e cartelle cliniche (dati sanitari)",
        "seo_title": "Data Breach Referti Medici e Dati Sanitari: Protocollo GDPR",
        "desc": "Gestione urgente di violazioni di dati sanitari in cliniche, laboratori e studi medici: rischio elevato, art. 9 e 34 GDPR, DPO e prevenzione sanzioni Garante.",
        "keywords": ["data breach dati sanitari", "referto medico inviato paziente sbagliato gdpr", "sanzioni garante clinica privacy"],
        "norme": ["Art. 9 GDPR", "Art. 33 GDPR", "Art. 34 GDPR", "Art. 167 D.Lgs. 196/2003"],
        "scenario": "Un laboratorio di analisi o uno studio medico consegna o rende accessibile sul portale online il referto clinico di un paziente a un altro utente.",
        "rischio": "I dati relativi alla salute sono categorie particolari ex art. 9 GDPR: il Garante applica criteri molto severi su referti online e consegna erronea.",
        "protocollo": [
            "Disabilitare subito l'accesso anomalo al portale referti e recuperare o far cancellare il documento consegnato per errore.",
            "Coinvolgere immediatamente il DPO (obbligatorio per strutture sanitarie su larga scala) e il legale privacy.",
            "Valutare la notifica al Garante entro 72 ore e la comunicazione mirata al paziente interessato ex art. 34 GDPR.",
            "Introdurre misure correttive strutturali (doppia verifica codice fiscale/OTP sul portale referti) prima della chiusura dell'istruttoria."
        ],
        "prove": ["Log del portale referti", "Copia del ticket di correzione tecnica", "Comunicazione al paziente", "Procedure interne di consegna referti"],
        "errori": ["Minimizzare l'errore su un singolo referto con diagnosi sensibile", "Usare password deboli o date di nascita per proteggere i PDF dei referti", "Non aggiornare la DPIA sanitaria"]
    },
    {
        "cod": "CYB-06", "slug": "ispezione-guardia-di-finanza-garante-privacy-azienda",
        "cat": "data-breach", "cat_lbl": "Data Breach & GDPR", "pilastro": "compliance-gdpr-dpo-privacy",
        "titolo": "Ispezione del Garante Privacy o Guardia di Finanza in azienda",
        "seo_title": "Ispezione Garante Privacy e Guardia di Finanza: Difesa Legale",
        "desc": "Come comportarsi durante un'ispezione privacy del Nucleo Speciale Guardia di Finanza: diritti del titolare, verbale, riserva di produzione e memorie difensive.",
        "keywords": ["ispezione garante privacy guardia di finanza", "verbale ispezione gdpr", "difesa sanzioni garante privacy"],
        "norme": ["Art. 58 GDPR", "Art. 157 D.Lgs. 196/2003", "Art. 166 D.Lgs. 196/2003"],
        "scenario": "Il Nucleo Speciale Tutela Privacy e Frodi Tecnologiche della Guardia di Finanza si presenta in sede su delega del Garante per verificare banche dati, marketing o videosorveglianza.",
        "rischio": "Dichiarazioni imprecise a verbale o consegna disordinata di file possono aggravare la posizione e condurre a sanzioni pecuniarie pesanti.",
        "protocollo": [
            "Accogliere gli operanti in modo collaborativo, chiedere l'esibizione della delega del Garante e contattare subito il legale e il DPO.",
            "Rilasciare solo dichiarazioni verificate, chiedendo di avvalersi della riserva di produzione documentale entro i termini concessi.",
            "Verificare attentamente ogni riga del verbale di operazioni compiute prima della sottoscrizione.",
            "Predisporre memorie difensive tecniche e piano di rientro correttivo per ridurre o azzerare l'eventuale sanzione ex art. 83 GDPR."
        ],
        "prove": ["Delega ispettiva e verbale GdF", "Registro trattamenti art. 30", "Log consensi e nomine art. 28", "Documentazione misure correttive immediate"],
        "errori": ["Ostacolare l'ispezione (comporta sanzioni autonome)", "Improvvisare risposte tecniche a memoria senza consultare i sistemisti", "Ignorare la richiesta di informazioni ex art. 157 Codice Privacy"]
    },
    {
        "cod": "CYB-07", "slug": "reclamo-cliente-garante-privacy-telemarketing-spam",
        "cat": "data-breach", "cat_lbl": "Data Breach & GDPR", "pilastro": "compliance-gdpr-dpo-privacy",
        "titolo": "Reclamo al Garante per telemarketing, email promozionali o liste contatti",
        "seo_title": "Reclamo Garante Privacy Telemarketing e Newsletter: Difesa",
        "desc": "Difesa dell'azienda contro reclami al Garante per chiamate commerciali, SMS o email marketing: prova del consenso, Registro Opposizioni e soft spam.",
        "keywords": ["reclamo garante privacy telemarketing", "sanzioni email marketing gdpr", "soft spam art 130 codice privacy"],
        "norme": ["Art. 130 D.Lgs. 196/2003", "Art. 6 e 7 GDPR", "Art. 77 GDPR"],
        "scenario": "Un utente presenta reclamo al Garante lamentando telefonate promozionali o newsletter ricevute senza consenso valido o dopo aver chiesto la cancellazione.",
        "rischio": "Il Garante indaga spesso sull'intera banca dati commerciale dell'azienda e sui call center esterni, arrivando al blocco del trattamento.",
        "protocollo": [
            "Estrarre subito il log del consenso (data, ora, IP, testo dell'informativa, doppia spunta) o verificare i presupposti del soft spam ex art. 130 co. 4.",
            "Inserire immediatamente il reclamante in blacklist certificata per impedire ulteriori contatti.",
            "Verificare i contratti con eventuali agenzie di lead generation o call center e la consultazione del Registro Pubblico delle Opposizioni.",
            "Rispondere al Garante con memoria documentata dimostrando la liceita' della fonte o le misure correttive adottate."
        ],
        "prove": ["Log tecnico raccolta consenso", "Contratto con fornitore liste/call center", "Tracciato opt-out / blacklist", "Screenshot form di iscrizione"],
        "errori": ["Acquistare liste contatti senza prova documentale del consenso specifico alla cessione a terzi", "Continuare a inviare comunicazioni dopo la richiesta di opposizione ex art. 21 GDPR", "Confondere il consenso contrattuale con quello marketing"]
    },
    {
        "cod": "CYB-08", "slug": "cookie-banner-analytics-tracciamento-sito-web-sanzioni",
        "cat": "data-breach", "cat_lbl": "Data Breach & GDPR", "pilastro": "compliance-gdpr-dpo-privacy",
        "titolo": "Contestazioni su cookie banner, pixel pubblicitari e tracciamento online",
        "seo_title": "Cookie Banner e Pixel Tracciamento GDPR: Adeguamento e Difesa",
        "desc": "Come mettere a norma cookie banner, Google Analytics, Meta Pixel e profilazione sul sito web evitando reclami e sanzioni del Garante Privacy.",
        "keywords": ["cookie banner gdpr garante", "sanzioni google analytics pixel", "linee guida cookie garante privacy"],
        "norme": ["Art. 122 D.Lgs. 196/2003", "Art. 7 GDPR", "Linee guida Cookie Garante"],
        "scenario": "Un e-commerce o un portale aziendale riceve una diffida o un reclamo perche' installa cookie di profilazione e pixel di terze parti prima del consenso dell'utente o senza tasto di rifiuto equivalente.",
        "rischio": "Sanzioni amministrative per trattamento illecito di dati di navigazione e trasferimenti extra-UE non conformi.",
        "protocollo": [
            "Eseguire una scansione tecnica dei cookie e degli script caricati al primo accesso prima del clic sul banner.",
            "Configurare il blocco preventivo reale dei tag di marketing e inserire il comando di chiusura/rifiuto con pari evidenza grafica.",
            "Registrare la prova tecnica dei consensi espressi e aggiornare cookie policy e privacy policy.",
            "Rispondere formalmente alla contestazione allegando la prova dell'adeguamento tecnico immediato."
        ],
        "prove": ["Report scansione cookie pre-consenso", "Configurazione CMP (Consent Management Platform)", "Registro consensi utente", "Cookie policy aggiornata"],
        "errori": ["Usare un banner puramente estetico che carica comunque i pixel pubblicitari", "Nascondere il tasto rifiuta o usare dark pattern", "Riproporre il banner a ogni pagina a chi ha gia' rifiutato"]
    },
    {
        "cod": "CYB-09", "slug": "richiesta-accesso-cancellazione-dati-ex-cliente-art-15-17",
        "cat": "data-breach", "cat_lbl": "Data Breach & GDPR", "pilastro": "compliance-gdpr-dpo-privacy",
        "titolo": "Gestione di istanze strumentali di accesso o cancellazione dati (artt. 15-17 GDPR)",
        "seo_title": "Richiesta Accesso e Cancellazione Dati Art. 15 e 17 GDPR: Risposta",
        "desc": "Come rispondere correttamente entro 30 giorni a un ex cliente o ex dipendente che esercita il diritto di accesso o cancellazione dati in vista di una causa.",
        "keywords": ["risposta istanza art 15 gdpr", "richiesta cancellazione dati ex cliente", "termine 30 giorni gdpr"],
        "norme": ["Art. 12 GDPR", "Art. 15 GDPR", "Art. 17 par. 3 GDPR"],
        "scenario": "Un cliente in contenzioso o un ex lavoratore invia una PEC chiedendo copia di tutti i dati trattati e la cancellazione immediata di ogni documento che lo riguarda.",
        "rischio": "Ignorare la richiesta o superare i 30 giorni porta a un reclamo sicuro al Garante; cancellare tutto alla cieca puo' far perdere prove essenziali per la difesa in giudizio.",
        "protocollo": [
            "Identificare con certezza il richiedente e fissare la scadenza perentoria di 30 giorni ex art. 12 par. 3 GDPR.",
            "Fornire riscontro ordinato sui dati trattati senza esporre dati di terzi o segreti aziendali.",
            "Per la richiesta di cancellazione, opporre legittimamente l'eccezione dell'art. 17 par. 3 lett. b) ed e) GDPR per gli obblighi di legge fiscali e la difesa di un diritto in sede giudiziaria.",
            "Conservare la PEC di riscontro a prova dell'adempimento tempestivo."
        ],
        "prove": ["PEC di richiesta dell'interessato", "Verifica identita' del richiedente", "Lettera di riscontro motivata ex art. 17 par. 3", "Ricevuta consegna PEC entro 30 giorni"],
        "errori": ["Non rispondere entro un mese", "Cancellare fatture, contratti o email necessarie per una causa pendente", "Consegnare documenti contenenti dati riservati di altri clienti o dipendenti"]
    },
    {
        "cod": "CYB-10", "slug": "trattamento-illecito-dati-penale-art-167-codice-privacy",
        "cat": "data-breach", "cat_lbl": "Data Breach & GDPR", "pilastro": "data-breach-garante-privacy",
        "titolo": "Contestazione penale per trattamento illecito di dati (art. 167 Codice Privacy)",
        "seo_title": "Trattamento Illecito di Dati Art. 167 D.Lgs. 196/2003: Difesa",
        "desc": "Quando la violazione privacy diventa reato penale ex art. 167 D.Lgs. 196/2003: dolo specifico di profitto o danno, requisito del nocumento e difesa tecnica.",
        "keywords": ["art 167 codice privacy", "trattamento illecito dati reato", "nocumento art 167"],
        "norme": ["Art. 167 D.Lgs. 196/2003", "Art. 9 GDPR", "Art. 167-bis D.Lgs. 196/2003"],
        "scenario": "Un soggetto o un amministratore viene indagato per aver diffuso o sfruttato illecitamente banche dati sensibili o comunicazioni elettroniche a fini di profitto o per danneggiare un terzo.",
        "rischio": "Reclusione da 6 mesi a 1 anno e 6 mesi (comma 1) o da 1 a 3 anni se riguardante dati particolari ex artt. 9 e 10 GDPR (comma 2).",
        "protocollo": [
            "Analizzare la contestazione verificando la sussistenza effettiva del dolo specifico (fine di profitto o di danno).",
            "Verificare la prova del nocumento concreto, elemento costitutivo essenziale del reato nel testo vigente.",
            "Controllare l'eventuale concorso o assorbimento con altri reati informatici (art. 615-ter c.p.) e il principio del ne bis in idem rispetto a sanzioni del Garante.",
            "Impostare la difesa tecnica o, per la persona offesa, la costituzione di parte civile per il risarcimento."
        ],
        "prove": ["Atti di indagine e informativa Polizia Postale", "Prova dell'assenza o presenza del danno concreto (nocumento)", "Documentazione della base giuridica del trattamento", "Eventuali provvedimenti del Garante sullo stesso fatto"],
        "errori": ["Confondere la semplice irregolarita' amministrativa GDPR con il reato penale doloso", "Trascurare il collegamento tra procedimento penale e istruttoria del Garante", "Non verificare la competenza territoriale e i termini di prescrizione"]
    },

    # ═══════════════════ 2. RANSOMWARE & NIS2/ACN (11-20) ═══════════════════
    {
        "cod": "CYB-11", "slug": "attacco-ransomware-server-gestionale-aziendale",
        "cat": "ransomware-nis2", "cat_lbl": "Ransomware & NIS2/ACN", "pilastro": "ransomware-estorsione-informatica",
        "titolo": "Ransomware cifra server e gestionale aziendale: protocollo sala crisi",
        "seo_title": "Ransomware Server Aziendale: Protocollo Legale Sala Crisi",
        "desc": "Gestione legale passo-passo quando un ransomware paralizza server e gestionale aziendale: denuncia art. 629 co. 3 c.p., Polizia Postale, ACN, Garante e continuità.",
        "keywords": ["attacco ransomware azienda cosa fare", "server cifrato ransomware avvocato", "art 629 comma 3 cp"],
        "norme": ["Art. 629 co. 3 c.p.", "L. 90/2024", "Art. 635-quater c.p.", "Art. 33 GDPR"],
        "scenario": "All'apertura degli uffici i dipendenti trovano tutti i file del server cifrati con estensione anomala e una richiesta di riscatto in criptovalute.",
        "rischio": "Fermo totale della produzione, perdita di dati contabili e clienti, doppia estorsione, sanzioni per omesse notifiche e contenzioso con i clienti.",
        "protocollo": [
            "Disconnettere i segmenti di rete compromessi preservando prove forensi, log di firewall/VPN e copia integrale della ransom note.",
            "Attivare il difensore e il team DFIR (Digital Forensics & Incident Response) verificando subito se vi e' stata esfiltrazione dati.",
            "Depositare denuncia immediata alla Polizia Postale per estorsione informatica (art. 629 co. 3 c.p.) e danneggiamento sistemi.",
            "Gestire le notifiche di legge (24h ACN se in perimetro NIS2, 72h Garante Privacy) e le comunicazioni ai partner commerciali."
        ],
        "prove": ["Copia forense della nota di riscatto e degli indicatori di compromissione (IoC)", "Log di rete e traffico in uscita", "Verbale di denuncia Polizia Postale", "Stato dei backup offline"],
        "errori": ["Pagare il riscatto di impulso senza verifica legale e tecnica", "Formattare i server distruggendo le prove dell'intrusione", "Tacere l'incidente a clienti strategici violando clausole contrattuali"]
    },
    {
        "cod": "CYB-12", "slug": "doppia-estorsione-minaccia-pubblicazione-dati-dark-web",
        "cat": "ransomware-nis2", "cat_lbl": "Ransomware & NIS2/ACN", "pilastro": "ransomware-estorsione-informatica",
        "titolo": "Doppia estorsione: minaccia di pubblicare archivi aziendali sul dark web",
        "seo_title": "Doppia Estorsione Ransomware e Dati sul Dark Web: Difesa",
        "desc": "Come reagire legalmente quando un gruppo cybercriminale minaccia di pubblicare contratti, bilanci e dati personali sul dark web se non viene pagato il riscatto.",
        "keywords": ["doppia estorsione ransomware", "dati aziendali pubblicati dark web", "ricatto informatico azienda"],
        "norme": ["Art. 629 co. 3 c.p.", "Art. 33 e 34 GDPR", "Art. 615-ter co. 2 c.p."],
        "scenario": "Anche se i backup permettono di riavviare i server, gli attaccanti mostrano campioni di documenti riservati rubati e fissano un conto alla rovescia per la pubblicazione online.",
        "rischio": "Rischio elevato immediato per clienti, dipendenti e segreti industriali, con obbligo di comunicazione ex art. 34 GDPR e danno reputazionale.",
        "protocollo": [
            "Verificare con il team forense la reale portata del pacchetto dati esfiltrato rispetto a quanto millantato dagli estorsori.",
            "Integrare immediatamente la denuncia penale per estorsione informatica aggravata e accesso abusivo con sottrazione dati (art. 615-ter co. 2 n. 3 c.p.).",
            "Predisporre notifica al Garante (72h) e comunicazione chiara agli interessati (art. 34 GDPR) con consigli di protezione da phishing secondario.",
            "Coordinare una comunicazione istituzionale sobria per clienti, banche e stampa evitando ammissioni di colpa premature."
        ],
        "prove": ["Screenshot certificati dei campioni pubblicati e delle richieste estorsive", "Analisi forense dei volumi di dati usciti dalla rete", "Denuncia integrativa alla Polizia Postale", "Bozza approvata di comunicazione ex art. 34 GDPR"],
        "errori": ["Credere alla promessa criminale di cancellazione dopo il pagamento", "Ritardare l'avviso agli interessati quando i loro documenti d'identita' sono gia' online", "Gestire trattative dirette non tracciate senza tutela legale"]
    },
    {
        "cod": "CYB-13", "slug": "verifica-perimetro-nis2-soggetto-essenziale-importante",
        "cat": "ransomware-nis2", "cat_lbl": "Ransomware & NIS2/ACN", "pilastro": "direttiva-nis2-acn-legge-90-2024",
        "titolo": "Verifica inclusione NIS2 (D.Lgs. 138/2024): soggetto essenziale o importante",
        "seo_title": "Chi Rientra nella NIS2 D.Lgs. 138/2024: Verifica Aziende",
        "desc": "Come stabilire con certezza giuridica se un'impresa rientra nel perimetro NIS2 (D.Lgs. 138/2024), obbligo di registrazione sul portale ACN e gestione dei gruppi societari.",
        "keywords": ["chi rientra nella nis2", "soggetti essenziali e importanti dlgs 138 2024", "registrazione portale acn nis2"],
        "norme": ["D.Lgs. 138/2024 artt. 3-7", "Allegati I-IV D.Lgs. 138/2024"],
        "scenario": "Un'impresa manifatturiera, logistica, alimentare o digitale con piu' di 50 dipendenti (o parte di un gruppo) deve accertare se e' obbligata alla registrazione ACN e alle misure NIS2.",
        "rischio": "La mancata registrazione sul portale ACN costituisce violazione autonoma sanzionabile fino allo 0,1% del fatturato globale, oltre all'inadempimento delle misure di sicurezza.",
        "protocollo": [
            "Analizzare codici ATECO, attivita' effettivamente svolte e soglie dimensionali (anche rispetto a imprese collegate e associate).",
            "Verificare le ipotesi di inclusione indipendente dalla dimensione (es. fornitori critici, servizi fiduciari, infrastrutture digitali).",
            "Redigere un parere motivato di inclusione o esclusione da conservare agli atti societari in caso di controllo ACN.",
            "Se inclusa, eseguire la registrazione sul portale ACN designando il punto di contatto e avviando la roadmap di adeguamento."
        ],
        "prove": ["Visura camerale e bilanci degli ultimi due esercizi", "Mappa partecipazioni societarie del gruppo", "Parere legale di applicabilita' NIS2", "Ricevuta registrazione portale ACN"],
        "errori": ["Guardare solo il fatturato della singola SRL ignorando il perimetro di gruppo", "Basarsi su elenchi generici non aggiornati alle determinazioni ACN", "Saltare la finestra annuale di registrazione/aggiornamento"]
    },
    {
        "cod": "CYB-14", "slug": "notifica-incidente-acn-csirt-24-ore-72-ore-nis2",
        "cat": "ransomware-nis2", "cat_lbl": "Ransomware & NIS2/ACN", "pilastro": "direttiva-nis2-acn-legge-90-2024",
        "titolo": "Incidente significativo NIS2: preallarme ACN 24 ore, notifica 72 ore e relazione finale",
        "seo_title": "Notifica Incidente ACN 24 e 72 Ore NIS2: Procedura Art. 25",
        "desc": "Procedura legale per la notifica in tre fasi di un incidente informatico significativo al CSIRT Italia / ACN ai sensi dell'art. 25 D.Lgs. 138/2024.",
        "keywords": ["notifica incidente acn 24 ore", "art 25 dlgs 138 2024", "csirt italia notifica nis2"],
        "norme": ["Art. 25 D.Lgs. 138/2024", "Art. 33 GDPR"],
        "scenario": "Un soggetto essenziale o importante subisce un'interruzione grave dei servizi o un'intrusione con impatto operativo e deve attivare il flusso di notifica verso il CSIRT Italia.",
        "rischio": "Omessa o tardiva notifica espone a sanzioni ACN fino a 10 milioni di euro / 2% del fatturato (essenziali) o 7 milioni / 1,4% (importanti).",
        "protocollo": [
            "Entro 24 ore dalla conoscenza dell'incidente significativo: trasmettere il preallarme indicando sospetto carattere illecito ed eventuale impatto transfrontaliero.",
            "Entro 72 ore: inviare la notifica dell'incidente con valutazione iniziale di gravita', impatto e indicatori di compromissione (IoC).",
            "Coordinare in parallelo l'eventuale notifica al Garante Privacy se l'incidente coinvolge anche dati personali.",
            "Entro 1 mese: depositare la relazione finale completa con causa radice, misure di mitigazione e lezioni apprese."
        ],
        "prove": ["Timestamp della prima rilevazione dell'incidente", "Ricevute di invio preallarme 24h e notifica 72h su portale CSIRT", "Report tecnico cause radice", "Verbale di coordinamento con il CdA"],
        "errori": ["Confondere la notifica ACN (sicurezza sistemi) con quella al Garante (dati personali)", "Attendere l'analisi completa superando le 24 ore del preallarme", "Non avere designato prima il referente CSIRT abilitato al portale"]
    },
    {
        "cod": "CYB-15", "slug": "responsabilita-amministratori-cda-direttiva-nis2",
        "cat": "ransomware-nis2", "cat_lbl": "Ransomware & NIS2/ACN", "pilastro": "direttiva-nis2-acn-legge-90-2024",
        "titolo": "Responsabilita' degli amministratori e del CdA per violazioni NIS2",
        "seo_title": "Responsabilita' Amministratori e CdA NIS2 (D.Lgs. 138/2024)",
        "desc": "Obblighi personali del Consiglio di Amministrazione nella Direttiva NIS2: approvazione misure cyber, formazione obbligatoria, deleghe e tutela da azioni di responsabilita'.",
        "keywords": ["responsabilita amministratori nis2", "obblighi cda dlgs 138 2024", "formazione cda cybersicurezza"],
        "norme": ["Art. 23 D.Lgs. 138/2024", "Art. 2392 c.c.", "Art. 2086 c.c."],
        "scenario": "Il Consiglio di Amministrazione di una societa' in perimetro NIS2 deve dimostrare di aver istituito assetti organizzativi adeguati e di aver supervisionato il rischio informatico.",
        "rischio": "Responsabilita' personale degli amministratori per le violazioni NIS2, interdizione temporanea dalle funzioni dirigenziali nei casi piu' gravi e azioni civili ex art. 2392 c.c.",
        "protocollo": [
            "Inserire la cybersicurezza nell'ordine del giorno del CdA con approvazione formale del piano di gestione rischi e del relativo budget.",
            "Formalizzare deleghe chiare e dotate di autonomia di spesa al referente sicurezza / CISO senza svuotare il dovere di vigilanza del CdA.",
            "Pianificare e documentare la formazione periodica obbligatoria dei membri dell'organo di amministrazione.",
            "Integrare la cybersicurezza negli adeguati assetti organizzativi ex art. 2086 comma 2 c.c. e nelle polizze D&O."
        ],
        "prove": ["Verbali CdA di approvazione policy e budget cyber", "Attestati formazione cybersicurezza degli amministratori", "Reportistica periodica del CISO al CdA", "Polizza D&O verificata sui sinistri cyber"],
        "errori": ["Delegare tutto verbalmente al tecnico IT esterno senza verbali CdA", "Ignorare l'obbligo di formazione personale dei consiglieri", "Approvare policy senza stanziare risorse concrete"]
    },
    {
        "cod": "CYB-16", "slug": "catena-fornitura-nis2-clausole-fornitori-ict",
        "cat": "ransomware-nis2", "cat_lbl": "Ransomware & NIS2/ACN", "pilastro": "direttiva-nis2-acn-legge-90-2024",
        "titolo": "Sicurezza della catena di fornitura NIS2: clausole contrattuali per fornitori ICT",
        "seo_title": "Catena di Fornitura NIS2: Clausole Contrattuali Fornitori IT",
        "desc": "Come adeguare i contratti con fornitori IT, cloud e subappaltatori agli obblighi di supply chain security imposti dal D.Lgs. 138/2024.",
        "keywords": ["supply chain nis2 contratti", "clausole cybersicurezza fornitori it", "obblighi fornitori nis2"],
        "norme": ["Art. 24 D.Lgs. 138/2024", "Art. 28 GDPR"],
        "scenario": "Un'azienda soggetta a NIS2 deve dimostrare ad ACN di controllare la postura di sicurezza dei propri fornitori critici (o una PMI fornitrice riceve un addendum NIS2 da un grande cliente).",
        "rischio": "Un attacco che passa dal fornitore IT compromette il committente, generando responsabilita' regolatoria e risoluzioni contrattuali per inadempimento.",
        "protocollo": [
            "Classificare i fornitori per livello di criticita' operativa e accesso ai sistemi aziendali.",
            "Predisporre un Addendum Sicurezza NIS2 con requisiti minimi tecnici, obbligo di notifica incidenti in 12 ore e diritto di audit.",
            "Disciplinare chiaramente l'uso di sub-fornitori e le responsabilita' in caso di data breach o fermo servizio.",
            "Per i fornitori che ricevono addendum eccessivi dai clienti, negoziare clausole proporzionate e sostenibili."
        ],
        "prove": ["Albo fornitori critici classificati", "Addendum contrattuali NIS2 sottoscritti", "Questionari di qualifica sicurezza compilati", "Certificazioni o audit dei fornitori"],
        "errori": ["Firmare addendum NIS2 di grandi clienti con penali illimitate senza revisione legale", "Non prevedere tempi stretti di notifica incidente da parte del fornitore", "Dimenticare di verificare i subappaltatori cloud"]
    },
    {
        "cod": "CYB-17", "slug": "polizza-cyber-insurance-rifiuto-indennizzo-ransomware",
        "cat": "ransomware-nis2", "cat_lbl": "Ransomware & NIS2/ACN", "pilastro": "ransomware-estorsione-informatica",
        "titolo": "Polizza Cyber Insurance: gestione sinistro e contestazione del rifiuto di indennizzo",
        "seo_title": "Polizza Cyber Insurance: Rifiuto Indennizzo Ransomware e Difesa",
        "desc": "Assistenza legale nell'attivazione della polizza assicurativa cyber e nella contestazione di esclusioni o dinieghi della compagnia dopo un attacco informatico.",
        "keywords": ["polizza cyber rifiuto indennizzo", "assicurazione ransomware contestazione", "sinistro cyber insurance avvocato"],
        "norme": ["Artt. 1882-1917 c.c.", "Art. 1341 c.c.", "Codice delle Assicurazioni"],
        "scenario": "Dopo un attacco ransomware la compagnia assicurativa nega o riduce drasticamente l'indennizzo eccependo una mancata configurazione tecnica o una tardiva comunicazione.",
        "rischio": "Perdita della copertura sui costi di ripristino IT, consulenza forense, interruzione di esercizio e sanzioni/richieste di terzi.",
        "protocollo": [
            "Notificare il sinistro alla compagnia entro i termini di polizza chiedendo l'autorizzazione immediata per i consulenti DFIR e legali.",
            "Esaminare le clausole di esclusione, le dichiarazioni precontrattuali (questionario di assunzione) e l'eventuale vessatorieta' di limitazioni occulte.",
            "Documentare analiticamente il danno da fermo esercizio (business interruption) e i costi di bonifica e ricostruzione dati.",
            "In caso di diniego ingiustificato, inviare diffida tecnica e promuovere mediazione o azione giudiziaria contro l'assicuratore."
        ],
        "prove": ["Polizza integrale e questionario assuntivo", "Denuncia di sinistro e corrispondenza col liquidatore", "Fatture costi di bonifica e perizia sul lucro cessante", "Report forense sulle cause dell'attacco"],
        "errori": ["Affidarsi a fornitori non autorizzati violando la clausola di consenso preventivo della polizza", "Compilare con superficialita' il questionario di sicurezza al momento della sottoscrizione", "Non quantificare il danno da interruzione di esercizio"]
    },
    {
        "cod": "CYB-18", "slug": "attacco-informatico-pubblica-amministrazione-legge-90-2024",
        "cat": "ransomware-nis2", "cat_lbl": "Ransomware & NIS2/ACN", "pilastro": "direttiva-nis2-acn-legge-90-2024",
        "titolo": "Incidente cyber su Ente Pubblico o societa' partecipata: obblighi Legge 90/2024",
        "seo_title": "Attacco Cyber PA e Societa' Partecipate: Obblighi Legge 90/2024",
        "desc": "Adempimenti urgenti per Pubbliche Amministrazioni, Comuni, ASL e societa' in house colpiti da incidente informatico secondo la Legge 90/2024 e il D.Lgs. 138/2024.",
        "keywords": ["legge 90 2024 pubblica amministrazione cybersicurezza", "notifica acn 24 ore pa", "referente cybersicurezza pa"],
        "norme": ["L. 90/2024 artt. 1-8", "D.Lgs. 138/2024", "Art. 615-ter co. 3 c.p."],
        "scenario": "Un ente pubblico locale, una struttura sanitaria pubblica o una societa' partecipata subisce un'intrusione nei propri sistemi o servizi online al cittadino.",
        "rischio": "Pene penali fino a 12 anni per gli autori (sistemi di interesse pubblico), responsabilità dirigenziale ed erariale in caso di omessa adozione delle misure o ritardata notifica.",
        "protocollo": [
            "Attivare subito la struttura per la cybersicurezza e il referente unico per la cybersicurezza previsti dalla L. 90/2024.",
            "Eseguire la segnalazione ad ACN entro 24 ore e la notifica completa entro 72 ore secondo le procedure dedicate alla PA.",
            "Valutare in parallelo la notifica al Garante Privacy entro 72 ore e la denuncia d'ufficio all'Autorita' Giudiziaria.",
            "Documentare tutte le misure di ripristino per prevenire rilievi della Corte dei Conti o di ACN."
        ],
        "prove": ["Atto di nomina del referente cybersicurezza", "Ricevute di segnalazione ACN 24h/72h", "Relazione tecnica di contenimento", "Comunicazioni istituzionali ai cittadini"],
        "errori": ["Non aver designato preventivamente il referente per la cybersicurezza", "Sottovalutare l'obbligo di adozione degli interventi risolutivi indicati da ACN entro i termini", "Gestire l'incidente senza coordinamento tra DPO e ufficio legale"]
    },
    {
        "cod": "CYB-19", "slug": "blocco-produzione-forza-maggiore-clienti-dopo-cyberattacco",
        "cat": "ransomware-nis2", "cat_lbl": "Ransomware & NIS2/ACN", "pilastro": "ransomware-estorsione-informatica",
        "titolo": "Ritardi di consegna ai clienti dopo attacco informatico: forza maggiore e penali",
        "seo_title": "Ritardi Consegna da Cyberattacco: Forza Maggiore e Penali B2B",
        "desc": "Come gestire i contratti con i clienti durante un fermo aziendale da ransomware: invocazione della forza maggiore, prevenzione penali e difesa da risoluzioni.",
        "keywords": ["cyberattacco forza maggiore contratti", "penali ritardo consegna ransomware", "impossibilita sopravvenuta attacco hacker"],
        "norme": ["Art. 1218 c.c.", "Art. 1256 c.c.", "Art. 1463 c.c."],
        "scenario": "A causa di un attacco informatico che blocca magazzino e linee produttive per giorni, un'azienda non riesce a rispettare le consegne pattuite con grandi clienti che minacciano penali.",
        "rischio": "Applicazione automatica di penali contrattuali, risoluzione per inadempimento e richieste risarcitorie a catena.",
        "protocollo": [
            "Esaminare subito le clausole di forza maggiore e di notifica nei contratti di fornitura attivi.",
            "Inviare tempestivamente ai clienti una comunicazione formale PEC di sospensione temporanea documentando la natura criminosa dell'evento e la denuncia presentata.",
            "Dimostrare di aver adottato misure di sicurezza diligenti prima dell'attacco (essenziale per escludere la colpa ex art. 1218 c.c.).",
            "Negoziare piani di recupero consegne e accordi transattivi per salvaguardare la relazione commerciale."
        ],
        "prove": ["Contratti di fornitura e clausole di forza maggiore", "Denuncia Polizia Postale", "Documentazione misure di sicurezza preesistenti", "PEC di avviso tempestivo ai clienti"],
        "errori": ["Sparire per giorni senza avvisare formalmente i clienti", "Ammettere per iscritto carenze tecniche prima della verifica forense", "Confidare che l'attacco hacker esoneri automaticamente da colpa senza prova della diligenza"]
    },
    {
        "cod": "CYB-20", "slug": "attacco-supply-chain-fornitore-software-gestionale",
        "cat": "ransomware-nis2", "cat_lbl": "Ransomware & NIS2/ACN", "pilastro": "ransomware-estorsione-informatica",
        "titolo": "Ransomware diffuso tramite accesso remoto del fornitore IT (MSP)",
        "seo_title": "Ransomware da Accesso Remoto Fornitore IT: Rivalsa e Difesa",
        "desc": "Cosa fare quando gli attaccanti entrano in azienda sfruttando le credenziali compromesse del manutentore IT esterno: profili di responsabilita' e risarcimento.",
        "keywords": ["ransomware fornitore it responsabile", "attacco da accesso remoto msp", "risarcimento danni manutentore informatico"],
        "norme": ["Art. 1218 c.c.", "Art. 1176 co. 2 c.c.", "Art. 28 GDPR"],
        "scenario": "L'indagine forense scopre che l'attacco ransomware e' entrato attraverso la VPN o il software di assistenza remota del fornitore IT esterno privo di autenticazione a due fattori.",
        "rischio": "Danni ingenti di fermo aziendale e ricostruzione dati a carico dell'azienda cliente, che deve far valere la responsabilita' professionale del fornitore.",
        "protocollo": [
            "Cristallizzare subito in copia forense i log che provano il punto di ingresso riconducibile alle credenziali del fornitore.",
            "Inviare formale contestazione di inadempimento e messa in mora al fornitore IT (e alla sua assicurazione RC professionale).",
            "Valutare l'eventuale accertamento tecnico preventivo (art. 696 c.p.c.) prima di alterare lo stato dei sistemi.",
            "Quantificare danni emergenti, costi di ripristino, lucro cessante ed eventuali sanzioni per l'azione risarcitoria."
        ],
        "prove": ["Report DFIR sul vettore d'ingresso", "Log VPN/RDP dell'utenza del fornitore", "Contratto di manutenzione IT e SLA", "Perizia contabile sui danni subiti"],
        "errori": ["Affidare l'indagine forense allo stesso fornitore IT sospettato della falla", "Sovrascrivere i log di accesso remoto", "Sottoscrivere liberatorie per ottenere un ripristino piu' veloce"]
    },

    # ═══════════════════ 3. PHISHING, BANCHE & CRYPTO (21-30) ═══════════════════
    {
        "cod": "CYB-21", "slug": "phishing-sms-spoofing-banca-rimborso-abf",
        "cat": "truffe-banche", "cat_lbl": "Phishing, Banche & Crypto", "pilastro": "truffe-online-phishing-sim-swap-banche",
        "titolo": "Conto svuotato con falso SMS dentro la chat della banca (spoofing)",
        "seo_title": "Falso SMS Banca (Spoofing) e Conto Svuotato: Rimborso ABF",
        "desc": "Come ottenere il rimborso dalla banca dopo un falso SMS inserito nella chat ufficiale dell'istituto: onere della prova SCA ex art. 10 D.Lgs. 11/2010 e ricorso ABF.",
        "keywords": ["falso sms banca rimborso", "spoofing sms conto svuotato abf", "art 10 dlgs 11 2010"],
        "norme": ["D.Lgs. 11/2010 artt. 10-12", "PSD2", "Art. 640-ter c.p."],
        "scenario": "Il correntista riceve un SMS con lo stesso mittente ufficiale della propria banca (all'interno della medesima conversazione di avvisi legittimi) seguito da una chiamata del finto operatore antifrode e subisce bonifici o pagamenti non autorizzati.",
        "rischio": "La banca rigetta il reclamo standard accusando il cliente di colpa grave per aver cliccato o fornito codici.",
        "protocollo": [
            "Disconoscere immediatamente tutte le operazioni fraudolente, bloccare gli strumenti e sporgere denuncia alla Polizia Postale.",
            "Inviare reclamo formale PEC chiedendo alla banca i log informatici integrali che dimostrino la corretta autenticazione forte (SCA).",
            "Analizzare le carenze di sicurezza della banca (assenza alert, limiti superati, operazioni anomale rispetto allo storico del cliente).",
            "Proporre ricorso all'Arbitro Bancario Finanziario (ABF) o citazione davanti al Tribunale per il rimborso integrale."
        ],
        "prove": ["Screenshot integrali della chat SMS con i messaggi legittimi precedenti", "Tabulato telefonico della chiamata spoofing", "Denuncia e disconoscimento", "Log SCA prodotti o omessi dalla banca"],
        "errori": ["Accettare il primo rifiuto della banca come definitivo", "Presentare ricorso ABF fai-da-te senza contestare i profili tecnici SCA e l'art. 10 D.Lgs. 11/2010", "Cancellare gli SMS o il registro chiamate"]
    },
    {
        "cod": "CYB-22", "slug": "truffa-sim-swap-clonazione-scheda-telefonica-conto",
        "cat": "truffe-banche", "cat_lbl": "Phishing, Banche & Crypto", "pilastro": "truffe-online-phishing-sim-swap-banche",
        "titolo": "SIM Swap (clonazione SIM telefonica) e svuotamento del conto corrente",
        "seo_title": "SIM Swap e Conto Svuotato: Rimborso da Banca e Operatore",
        "desc": "Tutela legale completa in caso di SIM swap fraudolento: responsabilita' solidale della banca e della compagnia telefonica per sostituzione SIM senza controlli.",
        "keywords": ["sim swap rimborso banca", "clonazione sim conto svuotato", "responsabilita operatore telefonico sim swap"],
        "norme": ["D.Lgs. 11/2010 artt. 10-12", "Art. 2043 c.c.", "Art. 1218 c.c.", "Art. 640-ter c.p."],
        "scenario": "Il telefono perde improvvisamente segnale perche' un truffatore ha ottenuto la sostituzione o portabilita' della SIM, intercettando cosi' gli SMS OTP e svuotando il conto.",
        "rischio": "Sottrazione in pochi minuti di decine di migliaia di euro mentre il titolare e' completamente ignaro e privo di linea.",
        "protocollo": [
            "Chiedere subito il blocco del conto e ottenere dall'operatore telefonico copia della documentazione usata per la sostituzione della SIM.",
            "Sporgere denuncia per frode informatica e sostituzione di persona (artt. 640-ter e 494 c.p.).",
            "Agire contro la banca ex D.Lgs. 11/2010 (qui la colpa grave del cliente e' radicalmente esclusa) e contestare in parallelo la responsabilita' dell'operatore telefonico.",
            "Attivare ricorso ABF e, per i profili telefonici e di maggior danno, azione civile risarcitoria."
        ],
        "prove": ["Documento di richiesta sostituzione SIM con firma/documento falso", "Tabulato disattivazione linea", "Estratti conto e orari bonifici", "Denuncia penale"],
        "errori": ["Agire solo contro l'operatore trascurando il diritto al rimborso rapido verso la banca", "Non chiedere subito copia del documento esibito nel negozio di telefonia", "Ritardare il disconoscimento formale"]
    },
    {
        "cod": "CYB-23", "slug": "frode-bec-fattura-modificata-iban-email-aziendale",
        "cat": "truffe-banche", "cat_lbl": "Phishing, Banche & Crypto", "pilastro": "truffe-online-phishing-sim-swap-banche",
        "titolo": "Frode BEC (Man-in-the-Middle): fattura fornitore modificata con IBAN falso",
        "seo_title": "Frode BEC Fattura con IBAN Falso: Recupero Somme e Difesa",
        "desc": "Come intervenire quando un hacker si inserisce nelle email aziendali e sostituisce l'IBAN di una fattura: blocco fondi, riparto di responsabilita' tra cliente e fornitore.",
        "keywords": ["frode bec iban falso", "fattura modificata hacker chi paga", "man in the middle email bonifico"],
        "norme": ["Art. 1189 c.c.", "Art. 1218 c.c.", "Art. 640-ter c.p.", "Art. 615-ter c.p."],
        "scenario": "Un criminale accede alla casella email del fornitore (o del cliente), intercetta una fattura di importo rilevante e invia un messaggio credibile comunicando un cambio IBAN su conto estero.",
        "rischio": "Il pagamento finisce ai truffatori e il fornitore pretende comunque un secondo pagamento sostenendo di non aver mai ricevuto i soldi.",
        "protocollo": [
            "Attivare entro poche ore la procedura bancaria di recall urgente e segnalare il conto beneficiario alla Polizia Postale per il sequestro preventivo.",
            "Eseguire un'analisi forense degli header email per accertare quale casella (del fornitore o del cliente) sia stata violata.",
            "Applicare la disciplina civilistica sul pagamento al creditore apparente (art. 1189 c.c.) e sul concorso di colpa nella custodia dei sistemi informatici.",
            "Impostare la trattativa o la difesa civile contro la pretesa di doppio pagamento del fornitore."
        ],
        "prove": ["Header integrali (.eml) delle email originali e manipolate", "Ordine di bonifico e richiesta di recall", "Perizia IT su quale server email e' stato compromesso", "Denuncia alla Polizia Postale"],
        "errori": ["Cancellare i file .eml originali salvando solo stampe PDF prive di intestazioni tecniche", "Pagare subito una seconda volta il fornitore senza aver verificato di chi fosse la falla", "Non attivare il recall bancario nella stessa giornata"]
    },
    {
        "cod": "CYB-24", "slug": "bonifico-istantaneo-truffa-blocco-recupero-somme",
        "cat": "truffe-banche", "cat_lbl": "Phishing, Banche & Crypto", "pilastro": "truffe-online-phishing-sim-swap-banche",
        "titolo": "Bonifico istantaneo disposto con inganno o accesso abusivo: recupero somme",
        "seo_title": "Bonifico Istantaneo Truffa: Come Tentare il Blocco e Rimborso",
        "desc": "Strategie legali e bancarie dopo un bonifico istantaneo fraudolento: limiti dell'irrevocabilita', verifica del beneficiario, denuncia e responsabilita' degli intermediari.",
        "keywords": ["bonifico istantaneo truffa recupero soldi", "rimborso bonifico istantaneo phishing", "responsabilita banca bonifico istantaneo"],
        "norme": ["D.Lgs. 11/2010 artt. 10-12", "Reg. UE 2024/886 (Bonifici istantanei)", "Art. 640-ter c.p."],
        "scenario": "Un cliente subisce l'esecuzione di uno o piu' bonifici istantanei ad alto importo verso conti sconosciuti in Italia o in area SEPA.",
        "rischio": "L'accredito in pochi secondi rende difficile lo storno ordinario, ma non elimina la responsabilita' della banca in caso di operazione non autorizzata o carenze antifrode.",
        "protocollo": [
            "Richiedere immediatamente alla propria banca l'invio di un messaggio di richiesta richiamo per frode alla banca beneficiaria.",
            "Depositare denuncia urgente indicando IBAN beneficiario e orario esatto per sollecitare il blocco/sequestro dei fondi residui.",
            "Verificare se la banca ha rispettato i presidi SCA, il controllo di coerenza beneficiario/IBAN e i sistemi di allerta su operazioni anomale.",
            "Promuovere reclamo motivato e ricorso ABF o azione giudiziaria."
        ],
        "prove": ["Contabile bonifico istantaneo con codice CRO/TRN", "Orario esatto e massimali applicati", "Log accessi home banking", "Denuncia e richiesta richiamo"],
        "errori": ["Rinunciare a priori perche' la banca dice che il bonifico istantaneo e' irrevocabile", "Non verificare se i massimali giornalieri sono stati alzati fraudolentemente", "Omettere la richiesta di accesso agli atti bancari"]
    },
    {
        "cod": "CYB-25", "slug": "truffa-trading-online-criptovalute-recupero-fondi",
        "cat": "truffe-banche", "cat_lbl": "Phishing, Banche & Crypto", "pilastro": "truffe-online-phishing-sim-swap-banche",
        "titolo": "Truffa trading online e false piattaforme criptovalute: denuncia e tracing",
        "seo_title": "Truffa Trading Online e Criptovalute: Recupero Fondi e Denuncia",
        "desc": "Cosa fare dopo una truffa su piattaforme di trading o criptovalute (pig butchering): tracciamento blockchain, querela tecnica, blocco exchange e difesa da finti recuperatori.",
        "keywords": ["truffa trading online recupero soldi", "truffa criptovalute denuncia", "falsa piattaforma investimenti avvocato"],
        "norme": ["Art. 640 c.p.", "Art. 640-ter c.p.", "Art. 166 TUF", "Art. 648-bis c.p."],
        "scenario": "Un risparmiatore versa somme tramite bonifici o exchange crypto su una piattaforma di trading online che mostra falsi profitti ma blocca i prelievi chiedendo ulteriori versamenti di 'tasse' o 'sblocco'.",
        "rischio": "Perdita di risparmi ingenti e rischio di cadere in una seconda truffa da parte di finte societa' di recupero fondi.",
        "protocollo": [
            "Interrompere immediatamente ogni ulteriore versamento e non installare software di controllo remoto (AnyDesk/TeamViewer) sul proprio dispositivo.",
            "Raccogliere tutti gli hash delle transazioni blockchain (TXID), indirizzi wallet, IBAN, chat e domini web.",
            "Affidare un'analisi di blockchain tracing per individuare gli exchange centralizzati (soggetti KYC) dove i fondi sono transitati.",
            "Depositare denuncia-querela tecnica in Procura chiedendo sequestro preventivo verso gli intermediari identificati e verificare eventuali profili di responsabilita' bancaria."
        ],
        "prove": ["Ricevute bonifici e acquisti su exchange", "TXID e indirizzi wallet di destinazione", "Chat WhatsApp/Telegram integrali", "Screenshot dashboard piattaforma e richieste di sblocco"],
        "errori": ["Pagare presunte tasse o commissioni di sblocco richieste dai truffatori", "Pagare finte agenzie online che promettono recupero garantito al 100%", "Presentare una denuncia generica senza TXID e tracciamento"]
    },
    {
        "cod": "CYB-26", "slug": "controllo-remoto-anydesk-finto-tecnico-conto-corrente",
        "cat": "truffe-banche", "cat_lbl": "Phishing, Banche & Crypto", "pilastro": "truffe-online-phishing-sim-swap-banche",
        "titolo": "Truffa con software di controllo remoto (AnyDesk/TeamViewer) sul conto",
        "seo_title": "Truffa AnyDesk e Controllo Remoto Banca: Difesa e Rimborso",
        "desc": "Tutela legale quando il truffatore convince la vittima a installare app di accesso remoto per svuotare il conto: profili di responsabilita', denuncia e valutazione ABF.",
        "keywords": ["truffa anydesk banca rimborso", "controllo remoto home banking truffa", "colpa grave abf anydesk"],
        "norme": ["D.Lgs. 11/2010 artt. 10-12", "Art. 640-ter c.p.", "Art. 615-ter c.p."],
        "scenario": "Un finto operatore di assistenza bancaria o tecnica induce l'utente a installare un programma di controllo remoto sullo smartphone o PC, prendendo il controllo della sessione di home banking.",
        "rischio": "Le banche eccepiscono regolarmente la colpa grave del cliente, ma occorre verificare l'effettiva tenuta dei sistemi antifrode e della SCA.",
        "protocollo": [
            "Disinstallare subito l'app di controllo remoto, cambiare tutte le password da un dispositivo pulito e bloccare il conto.",
            "Conservare i log di connessione dell'app di controllo remoto e i numeri telefonici usati dai truffatori.",
            "Sporgere denuncia penale e richiedere alla banca i log completi delle operazioni e dei dispositivi riconosciuti.",
            "Valutare con il legale la fattibilita' del ricorso ABF o civile verificando se la banca ha omesso controlli su anomalie palesi o dispositivi nuovi non censiti."
        ],
        "prove": ["Log di sessione dell'app remota", "Estratto conto e notifiche push ricevute", "Tabulato chiamate", "Log tecnici di autenticazione della banca"],
        "errori": ["Continuare a usare lo stesso smartphone senza bonifica", "Dichiarare inesattezze nella denuncia o nel disconoscimento", "Non verificare se la banca ha mancato di rilevare accessi da IP/dispositivi anomali"]
    },
    {
        "cod": "CYB-27", "slug": "carta-credito-clonata-pagamenti-online-non-autorizzati",
        "cat": "truffe-banche", "cat_lbl": "Phishing, Banche & Crypto", "pilastro": "truffe-online-phishing-sim-swap-banche",
        "titolo": "Carta di credito o debito clonata e addebiti online non autorizzati",
        "seo_title": "Carta Clonata e Addebiti Online Non Autorizzati: Rimborso",
        "desc": "Come ottenere il rimborso rapido per addebiti fraudolenti su carta di credito o prepagata senza 3D Secure: chargeback, art. 11-12 D.Lgs. 11/2010 e ricorso ABF.",
        "keywords": ["carta clonata rimborso banca", "addebiti non autorizzati carta online", "chargeback art 11 dlgs 11 2010"],
        "norme": ["D.Lgs. 11/2010 artt. 10, 11, 12", "PSD2 (3D Secure / SCA)"],
        "scenario": "Sull'estratto conto compaiono decine di addebiti ravvicinati su siti esteri o piattaforme digitali eseguiti senza autorizzazione del titolare della carta.",
        "rischio": "Rimborso ritardato o negato dall'emittente della carta con addebito definitivo sul conto corrente.",
        "protocollo": [
            "Bloccare immediatamente la carta annotando il codice di blocco e sporgere denuncia con l'elenco puntuale di ogni singolo addebito.",
            "Inviare disconoscimento formale e richiesta di chargeback all'emittente.",
            "Contestare l'eventuale esecuzione di transazioni prive di autenticazione forte (3D Secure / SCA): in assenza di SCA, l'art. 12 co. 2-bis D.Lgs. 11/2010 esclude la responsabilita' del cliente salvo frode.",
            "In caso di diniego o silenzio oltre 60 giorni, depositare ricorso ABF."
        ],
        "prove": ["Codice blocco carta", "Estratto conto con singole voci evidenziate", "Denuncia alle forze dell'ordine", "Modulo di disconoscimento e PEC di reclamo"],
        "errori": ["Dimenticare di controllare anche gli addebiti ricorrenti", "Superare il termine di disconoscimento", "Non invocare l'assenza di autenticazione forte (SCA) prevista dalla PSD2"]
    },
    {
        "cod": "CYB-28", "slug": "furto-identita-finanziamenti-prestiti-online-non-richiesti",
        "cat": "truffe-banche", "cat_lbl": "Phishing, Banche & Crypto", "pilastro": "truffe-online-phishing-sim-swap-banche",
        "titolo": "Furto d'identita' digitale: finanziamenti o conti aperti a tua insaputa",
        "seo_title": "Furto d'Identita' e Finanziamenti Online Non Richiesti: Difesa",
        "desc": "Come cancellare segnalazioni CRIF/Centrale Rischi e bloccare richieste di pagamento per prestiti online aperti da truffatori usando documenti rubati o SPID clonato.",
        "keywords": ["furto identita finanziamento non richiesto", "cancellazione crif furto identita", "spid clonato prestito online"],
        "norme": ["Art. 494 c.p.", "Art. 640-ter co. 3 c.p.", "D.Lgs. 141/2010", "Art. 17 GDPR"],
        "scenario": "Una persona scopre di essere segnalata come cattivo pagatore in CRIF o riceve solleciti per un prestito online o una carta revolving mai richiesti, aperti tramite furto di documenti o identita' SPID.",
        "rischio": "Blocco dell'accesso al credito, segnalazioni pregiudizievoli in banche dati finanziarie e decreti ingiuntivi ingiusti.",
        "protocollo": [
            "Sporgere denuncia per sostituzione di persona e frode informatica con furto d'identita' digitale (art. 640-ter co. 3 c.p.).",
            "Inviare diffida urgente alla finanziaria chiedendo copia integrale del contratto, dei documenti di identificazione e dei log di firma digitale/SPID.",
            "Chiedere la cancellazione immediata delle segnalazioni in CRIF, Experian, CTC e Centrale Rischi Banca d'Italia.",
            "In caso di inerzia, agire con ricorso ABF o ricorso cautelare d'urgenza art. 700 c.p.c. e richiesta di risarcimento danni."
        ],
        "prove": ["Visura CRIF / Centrale Rischi", "Denuncia penale", "Contratto di finanziamento disconosciuto", "Prova dell'estraneita' dell'IBAN e dei recapiti usati"],
        "errori": ["Ignorare i solleciti delle societa' di recupero crediti fino al pignoramento", "Non verificare se e' stato aperto uno SPID parallelo presso un altro identity provider", "Omettere la verifica su tutte le banche dati creditizie"]
    },
    {
        "cod": "CYB-29", "slug": "conto-corrente-bloccato-segnalazione-antiriciclaggio-crypto",
        "cat": "truffe-banche", "cat_lbl": "Phishing, Banche & Crypto", "pilastro": "truffe-online-phishing-sim-swap-banche",
        "titolo": "Blocco del conto corrente o chiusura rapporto dopo bonifici da exchange crypto",
        "seo_title": "Conto Bloccato per Bonifici Crypto: Tutela Legale e Sblocco",
        "desc": "Come difendersi se la banca blocca il conto corrente o recede dal contratto dopo trasferimenti da piattaforme di criptovalute: documentazione provenienza fondi e ricorso.",
        "keywords": ["conto bloccato bonifico criptovalute", "banca chiude conto crypto avvocato", "sblocco conto corrente antiriciclaggio"],
        "norme": ["D.Lgs. 231/2007 (Antiriciclaggio)", "Art. 1855 c.c.", "TUB art. 126-septies"],
        "scenario": "Un utente o un'impresa riceve un blocco improvviso dell'operativita' del conto corrente o un preavviso di recesso bancario dopo aver trasferito fondi da un exchange regolamentato.",
        "rischio": "Paralisi della liquidita' personale o aziendale e rischio di segnalazione di operazione sospetta non chiarita.",
        "protocollo": [
            "Raccogliere subito la catena documentale completa della provenienza lecita dei fondi (bonifici iniziali di acquisto, estratti exchange, dichiarazione quadro RW/RT).",
            "Inviare alla banca una memoria formale PEC con dossier documentale chiedendo l'immediato ripristino dell'operativita' o la liquidazione del saldo.",
            "Contestare l'eventuale recesso privo di preavviso legittimo o il trattenimento sine die delle somme.",
            "In caso di blocco illegittimo protratto, agire con ricorso ABF o ricorso d'urgenza art. 700 c.p.c."
        ],
        "prove": ["Storico completo transazioni exchange e bonifici originari", "Dichiarazioni fiscali quadro RW", "Comunicazioni della banca sul blocco/recesso", "PEC di messa in mora"],
        "errori": ["Fornire risposte frammentarie o contraddittorie alla compliance bancaria", "Non preparare la prova fiscale e di origine dei fondi", "Attendere mesi senza contestare formalmente il blocco"]
    },
    {
        "cod": "CYB-30", "slug": "spid-pec-firma-digitale-clonati-abuso-identita",
        "cat": "truffe-banche", "cat_lbl": "Phishing, Banche & Crypto", "pilastro": "truffe-online-phishing-sim-swap-banche",
        "titolo": "Furto o clonazione di SPID, PEC o Firma Digitale: revoca e tutela atti",
        "seo_title": "SPID o Firma Digitale Clonata: Revoca, Denuncia e Annullamento Atti",
        "desc": "Protocollo d'urgenza in caso di attivazione fraudolenta di SPID, casella PEC o firma digitale a proprio nome: revoca, denuncia e disconoscimento di atti e contratti.",
        "keywords": ["spid clonato cosa fare", "firma digitale rubata denuncia", "pec aperta a mia insaputa"],
        "norme": ["CAD D.Lgs. 82/2005", "Reg. eIDAS", "Art. 494 c.p.", "Art. 640-ter co. 3 c.p."],
        "scenario": "Un cittadino o un imprenditore scopre che un terzo ha attivato un secondo SPID, una PEC o un certificato di firma digitale a suo nome utilizzandoli per modificare IBAN su INPS/Agenzia Entrate o firmare contratti.",
        "rischio": "Deviazione di rimborsi fiscali, stipendi, pensioni o assunzione di obbligazioni contrattuali apparentemente valide.",
        "protocollo": [
            "Richiedere immediatamente la revoca del certificato SPID/PEC/firma digitale al gestore accreditato (Identity Provider / QTSP) e verificare gli accessi sul portale INPS e Agenzia Entrate.",
            "Sporgere denuncia alla Polizia Postale chiedendo l'acquisizione dei log di attivazione e della registrazione video di riconoscimento usata dai truffatori.",
            "Disconoscere formalmente ogni atto, delega o contratto sottoscritto con l'identita' clonata.",
            "Valutare l'azione risarcitoria verso il prestatore di servizi fiduciari che abbia rilasciato l'identita' senza controlli adeguati."
        ],
        "prove": ["Log di rilascio e utilizzo dello SPID/firma", "Notifiche di cambio IBAN su INPS o portali PA", "Denuncia penale", "Richiesta di revoca certificato al gestore"],
        "errori": ["Limitarsi a cambiare la password del proprio SPID senza controllare se ne esistono altri presso diversi provider", "Non controllare subito il cassetto fiscale e il portale INPS", "Ritardare il disconoscimento formale degli atti firmati"]
    },

    # ═══════════════════ 4. PENALE INFORMATICO & FORENSICS (31-35) ═══════════════════
    {
        "cod": "CYB-31", "slug": "avviso-garanzia-accesso-abusivo-sistema-informatico-615-ter",
        "cat": "penale-informatico", "cat_lbl": "Penale Informatico & Forensics", "pilastro": "reati-informatici-difesa-penale",
        "titolo": "Avviso di garanzia per accesso abusivo a sistema informatico (art. 615-ter c.p.)",
        "seo_title": "Avviso di Garanzia Art. 615-ter c.p.: Difesa Accesso Abusivo",
        "desc": "Come difendersi da un'accusa di accesso abusivo a sistema informatico (art. 615-ter c.p.) dopo la Legge 90/2024: pene fino a 10 anni, log IP, perizia forense e strategia penale.",
        "keywords": ["difesa art 615 ter cp", "avviso di garanzia accesso abusivo sistema informatico", "pena 615 ter legge 90 2024"],
        "norme": ["Art. 615-ter c.p.", "L. 90/2024", "Art. 360 c.p.p."],
        "scenario": "Un privato, un dipendente o un pubblico ufficiale riceve un avviso di garanzia o un decreto di perquisizione per presunto accesso abusivo a email, social, CRM aziendale o banca dati pubblica.",
        "rischio": "Pena base fino a 3 anni e pena aggravata da 2 a 10 anni (o da 4 a 12 anni su sistemi di interesse pubblico) dopo la riforma della Legge 90/2024.",
        "protocollo": [
            "Nominare subito il difensore di fiducia e non rendere dichiarazioni affrettate prima di aver esaminato gli atti e i log contestati.",
            "Verificare se il sistema fosse effettivamente protetto da misure di sicurezza e se esistesse un'autorizzazione o prassi di accesso.",
            "Affiancare un consulente informatico forense per analizzare indirizzi IP, dispositivi, Wi-Fi condivisi e orari di connessione.",
            "Verificare la tempestivita' della querela (3 mesi per l'ipotesi base) e le eventuali cause di inutilizzabilita' degli accertamenti."
        ],
        "prove": ["Log di accesso contestati dalla Procura", "Configurazione rete Wi-Fi e dispositivi presenti", "Prova dell'autorizzazione o delle credenziali condivise", "Consulenza tecnica informatica di parte"],
        "errori": ["Cancellare file o formattare dispositivi dopo la notizia d'indagine (rischio misure cautelari e aggravamento)", "Sottovalutare le aggravanti del comma 2 e 3", "Rinunciare al consulente tecnico durante gli accertamenti irripetibili"]
    },
    {
        "cod": "CYB-32", "slug": "perquisizione-informatica-sequestro-pc-smartphone-riesame",
        "cat": "penale-informatico", "cat_lbl": "Penale Informatico & Forensics", "pilastro": "reati-informatici-difesa-penale",
        "titolo": "Perquisizione informatica e sequestro di PC, smartphone e server: riesame",
        "seo_title": "Sequestro Informatico PC e Smartphone: Ricorso al Riesame",
        "desc": "Come ottenere il dissequestro di computer, telefoni e server sequestrati dalla Polizia Postale: proporzionalita', copia forense selettiva e riesame entro 10 giorni.",
        "keywords": ["sequestro pc smartphone riesame", "perquisizione informatica diritti", "dissequestro telefono polizia postale"],
        "norme": ["Art. 247 co. 1-bis c.p.p.", "Art. 254-bis c.p.p.", "Art. 324 c.p.p."],
        "scenario": "Durante una perquisizione domiciliare o in azienda, la polizia giudiziaria sequestra tutti i computer, gli smartphone e i server bloccando l'attivita' lavorativa.",
        "rischio": "Fermo operativo dell'azienda o del professionista per mesi e apprensione indiscriminata di dati privati o segreti estranei all'indagine.",
        "protocollo": [
            "Far verbalizzare durante la perquisizione la richiesta di copia forense selettiva o di restituzione tempestiva degli originali indispensabili al lavoro.",
            "Controllare il decreto di perquisizione e sequestro verificando la motivazione sul nesso di pertinenzialita' e proporzionalita'.",
            "Proporre ricorso al Tribunale del Riesame entro il termine perentorio di 10 giorni dal sequestro (art. 324 c.p.p.).",
            "Chiedere in parallelo al PM il dissequestro dei dispositivi previa estrazione mirata dei soli file pertinenti."
        ],
        "prove": ["Decreto di perquisizione e sequestro", "Verbale con elenco dispositivi e codici hash", "Documentazione del danno operativo da blocco PC/server", "Istanza di restituzione al PM"],
        "errori": ["Far scadere i 10 giorni per il riesame", "Consegnare password senza aver parlato con il difensore", "Non contestare il sequestro esplorativo di intere memorie di massa"]
    },
    {
        "cod": "CYB-33", "slug": "contestazione-copia-forense-catena-custodia-prova-digitale",
        "cat": "penale-informatico", "cat_lbl": "Penale Informatico & Forensics", "pilastro": "reati-informatici-difesa-penale",
        "titolo": "Nullita' o inattendibilita' della prova digitale: hash e catena di custodia",
        "seo_title": "Prova Digitale e Copia Forense: Contestare Hash e Catena Custodia",
        "desc": "Difesa tecnica nel processo penale informatico: verifica dell'integrita' della copia bit-stream, codici hash, best practice forensi e garanzie ex art. 360 c.p.p.",
        "keywords": ["catena di custodia prova digitale", "copia forense nulla art 360 cpp", "contestazione perizia informatica"],
        "norme": ["Art. 247 co. 1-bis c.p.p.", "Art. 354 c.p.p.", "Art. 360 c.p.p."],
        "scenario": "L'accusa penale si fonda su chat, file o log estratti da un dispositivo sequestrato senza garanzie tecniche adeguate o senza avviso al difensore.",
        "rischio": "Una prova digitale alterata o estratta in modo non ripetibile puo' condurre a una condanna ingiusta se non viene smontata sul piano tecnico-processuale.",
        "protocollo": [
            "Esaminare il verbale di acquisizione verificando se e' stata usata una procedura forense conforme (write blocker, copia bit-stream, calcolo hash SHA-256).",
            "Verificare se l'accertamento sul dispositivo era irripetibile e se il PM ha omesso l'avviso ex art. 360 c.p.p. (con conseguente inutilizzabilita').",
            "Controllare la continuita' della catena di custodia dal sequestro fino alla consulenza tecnica del PM.",
            "Depositare consulenza informatica forense di parte evidenziando alterazioni di metadati, date o assenza di corrispondenza hash."
        ],
        "prove": ["Verbali di sequestro e apertura plichi", "Report estrazione forense (es. Cellebrite/FTK) e codici hash", "Consulenza tecnica di parte", "Eccezioni processuali ex art. 360 c.p.p."],
        "errori": ["Accettare passivamente i risultati della perizia del PM", "Limitarsi a contestazioni generiche senza un consulente informatico", "Non verificare i log di accensione del dispositivo dopo il sequestro"]
    },
    {
        "cod": "CYB-34", "slug": "accusa-frode-informatica-640-ter-identita-digitale",
        "cat": "penale-informatico", "cat_lbl": "Penale Informatico & Forensics", "pilastro": "reati-informatici-difesa-penale",
        "titolo": "Difesa penale per frode informatica (art. 640-ter c.p.) e money muling",
        "seo_title": "Difesa Frode Informatica Art. 640-ter c.p. e Money Muling",
        "desc": "Difesa penale per chi e' indagato di frode informatica (art. 640-ter c.p.) o riciclaggio per aver prestato inconsapevolmente il proprio conto o carta (money mule).",
        "keywords": ["difesa frode informatica 640 ter", "money mule difesa penale", "carta intestata usata truffa"],
        "norme": ["Art. 640-ter c.p.", "Art. 648-bis c.p.", "Art. 42-43 c.p."],
        "scenario": "Un soggetto riceve un avviso di garanzia per frode informatica o riciclaggio perche' somme provento di phishing sono transitate su una sua carta prepagata o conto corrente aperto dopo una falsa offerta di lavoro online.",
        "rischio": "Condanna penale grave (da 2 a 6 anni per l'ipotesi aggravata ex art. 640-ter co. 3 o pene ancora piu' severe per riciclaggio) e sequestro dei beni.",
        "protocollo": [
            "Ricostruire integralmente le chat, gli annunci di lavoro falsi e i raggiri subiti dall'indagato per dimostrare l'assenza di dolo.",
            "Verificare se la carta o il conto siano stati aperti o gestiti a distanza da terzi mediante furto di documenti.",
            "Valutare la derubricazione dell'accusa, l'esclusione del concorso doloso o, ove opportuno, strategie riparatorie e riti alternativi.",
            "Impugnare eventuali sequestri preventivi sproporzionati rispetto al profitto effettivo."
        ],
        "prove": ["Annunci di lavoro o chat con i reclutatori truffaldini", "Log IP di accesso alla carta/conto", "Estratti conto dimostranti assenza di profitto personale", "Eventuale denuncia pregressa di furto documenti"],
        "errori": ["Non difendersi pensando di essere ovviamente innocente", "Cancellare le chat con chi ha richiesto l'apertura della carta", "Confondere la responsabilita' civile da custodia con il dolo penale"]
    },
    {
        "cod": "CYB-35", "slug": "danneggiamento-dati-sistemi-informatici-635-bis-quater",
        "cat": "penale-informatico", "cat_lbl": "Penale Informatico & Forensics", "pilastro": "reati-informatici-difesa-penale",
        "titolo": "Danneggiamento di dati, software o sistemi informatici (artt. 635-bis e 635-quater c.p.)",
        "seo_title": "Danneggiamento Dati e Sistemi Art. 635-bis e 635-quater c.p.",
        "desc": "Tutela penale per cancellazione di archivi aziendali, sabotaggio siti web, attacchi DDoS o alterazione di gestionali post Legge 90/2024 (pene da 2 a 6 anni).",
        "keywords": ["art 635 bis cp", "danneggiamento sistemi informatici 635 quater", "attacco ddos denuncia"],
        "norme": ["Art. 635-bis c.p.", "Art. 635-quater c.p.", "L. 90/2024"],
        "scenario": "Un ex collaboratore, un concorrente o un soggetto ignoto cancella archivi aziendali, sabota un e-commerce o lancia un attacco DDoS rendendo inaccessibili i server.",
        "rischio": "Pene detentive elevate (reclusione da 2 a 6 anni, fino a 8 anni nelle ipotesi aggravate) e gravi danni economici da fermo operativo.",
        "protocollo": [
            "Cristallizzare i log di sistema, i tracciati del traffico DDoS e le operazioni di cancellazione con copia forense certificata.",
            "Verificare la natura dell'alterazione (distruzione, deterioramento, cancellazione o ostacolo grave al funzionamento) per qualificare correttamente il reato.",
            "Depositare querela o denuncia d'ufficio (se ricorrono le aggravanti come l'abuso di qualita' di operatore del sistema) con richiesta di sequestro e acquisizione tabulati.",
            "In difesa dell'indagato, distinguere l'errore tecnico/colposo (non punibile penalmente) dalla condotta dolosa."
        ],
        "prove": ["Log di cancellazione e audit trail del gestionale", "Log firewall e provider anti-DDoS", "Perizia sui costi di ripristino e fermo sito", "Contratti di amministrazione di sistema"],
        "errori": ["Non distinguere un malfunzionamento o colpa professionale dal reato doloso", "Lasciar scadere i tempi di conservazione dei log presso il provider", "Omettere la quantificazione del danno per la parte civile"]
    }
]
