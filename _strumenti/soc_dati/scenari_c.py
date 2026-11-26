# -*- coding: utf-8 -*-
"""Scenari operativi e protocolli di difesa SOC-101 -> SOC-150 (Liquidazione 5, Penale Societario/Bancarotta 20, Amministratori & M&A 15, Sovraindebitamento & Banche 10)."""

SCENARI_C = [
    # ═══════════════════ 5. LIQUIDAZIONE GIUDIZIALE (continuazione 101-105) ═══════════════════
    {
        "cod": "SOC-101", "slug": "sorte-contratti-pendenti-scioglimento-art-172-ccii",
        "cat": "liquidazione-giudiziale", "cat_lbl": "Liquidazione Giudiziale", "pilastro": "liquidazione-giudiziale-fallimento-opposizioni",
        "titolo": "Sorte dei contratti pendenti nella liquidazione giudiziale: sospensione e scioglimento (art. 172 CCII)",
        "seo_title": "Contratti Pendenti Liquidazione Giudiziale Art. 172 CCII",
        "desc": "Come tutelare la controparte in bonis (fornitore, locatore, appaltatore) quando il cliente va in liquidazione giudiziale: messa in mora del curatore entro 60 giorni e subentro.",
        "keywords": ["contratti pendenti art 172 ccii", "messa in mora curatore 60 giorni", "subentro scioglimento contratti fallimento"],
        "norme": ["Art. 172 CCII", "Art. 177 CCII", "Art. 185 CCII"],
        "scenario": "Un contraente in bonis ha un contratto di appalto, fornitura continuativa, leasing o locazione ancora ineseguito con una societa' appena sottoposta a liquidazione giudiziale.",
        "rischio": "Il contratto resta sospeso a tempo indeterminato finche' il curatore non decide se subentrare (assumendo debiti in prededuzione) o sciogliersi.",
        "protocollo": [
            "Notificare subito istanza al giudice delegato per assegnare al curatore un termine non superiore a 60 giorni entro il quale dichiarare se subentra o si scioglie (art. 172 co. 2 CCII).",
            "In caso di silenzio del curatore allo scadere dei 60 giorni, il contratto si intende sciolto di diritto.",
            "Se il curatore subentra, pretendere il pagamento integrale in prededuzione delle prestazioni successive (e dei corrispettivi gia' consegnati nei contratti di durata ex art. 172 co. 3).",
            "In caso di scioglimento, insinuare al passivo l'eventuale credito anteriore per prestazioni gia' eseguite (escluso il risarcimento del danno da scioglimento)."
        ],
        "prove": ["Contratto originale con data certa anteriore", "Stato di avanzamento delle prestazioni gia' rese", "Istanza di messa in mora ex art. 172 co. 2 CCII", "Comunicazione PEC di subentro o scioglimento del curatore"],
        "errori": ["Continuare a eseguire forniture dopo la sentenza senza dichiarazione scritta di subentro del curatore", "Chiedere il risarcimento del danno per lo scioglimento ex art. 172 (escluso per legge)", "Dimenticare le regole speciali per appalto (art. 186), locazione (art. 185) e leasing (art. 177)"]
    },
    {
        "cod": "SOC-102", "slug": "rapporti-lavoro-licenziamenti-liquidazione-giudiziale-art-189",
        "cat": "liquidazione-giudiziale", "cat_lbl": "Liquidazione Giudiziale", "pilastro": "liquidazione-giudiziale-fallimento-opposizioni",
        "titolo": "Rapporti di lavoro e licenziamenti nella liquidazione giudiziale (art. 189 CCII riformato D.Lgs. 136/2024)",
        "seo_title": "Rapporti di Lavoro Liquidazione Giudiziale Art. 189 CCII e Correttivo-ter",
        "desc": "Sospensione dei contratti di lavoro fino a 4 mesi, recesso del curatore, risoluzione di diritto, NASpI, Fondo di Garanzia INPS TFR e novita' del D.Lgs. 136/2024.",
        "keywords": ["art 189 ccii rapporti lavoro liquidazione giudiziale", "recesso curatore dipendenti", "fondo garanzia inps tfr liquidazione"],
        "norme": ["Art. 189 CCII", "D.Lgs. 136/2024", "Art. 2 L. 297/1982"],
        "scenario": "All'apertura della liquidazione giudiziale i contratti di lavoro subordinato restano sospesi in attesa che il curatore decida tra subentro (esercizio provvisorio/cessione) o recesso.",
        "rischio": "Errori nei termini di sospensione (4 mesi prorogabili fino a 8) o nella domanda al passivo ritardano l'accesso a NASpI e Fondo di Garanzia INPS per TFR e ultime tre mensilita'.",
        "protocollo": [
            "Monitorare il periodo di sospensione di 4 mesi (prorogabile dal giudice delegato fino a un massimo di 8 mesi ex art. 189 CCII come riformato dal D.Lgs. 136/2024).",
            "Verificare la legittimita' della comunicazione di recesso del curatore (o della risoluzione di diritto allo scadere del termine) e dell'indennita' di mancato preavviso.",
            "Presentare tempestivamente la domanda di insinuazione allo stato passivo in privilegio art. 2751-bis n. 1 c.c. per retribuzioni arretrate, TFR e preavviso.",
            "Ottenuto il decreto di esecutivita' dello stato passivo, attivare subito la domanda al Fondo di Garanzia INPS per l'incasso di TFR e ultime tre mensilita'."
        ],
        "prove": ["Contratto di lavoro, CUD e buste paga integrali", "Comunicazione di sospensione e recesso del curatore", "Domanda di insinuazione al passivo e decreto di esecutivita'", "Istanza telematica al Fondo di Garanzia INPS"],
        "errori": ["Dare dimissioni volontarie senza giusta causa perdendo l'indennita' di mancato preavviso", "Sbagliare il calcolo del privilegio di lavoro nella domanda al passivo", "Attendere la chiusura della procedura invece di attivare subito il Fondo di Garanzia INPS"]
    },
    {
        "cod": "SOC-103", "slug": "affitto-azienda-liquidazione-giudiziale-art-212-ccii",
        "cat": "liquidazione-giudiziale", "cat_lbl": "Liquidazione Giudiziale", "pilastro": "liquidazione-giudiziale-fallimento-opposizioni",
        "titolo": "Affitto d'azienda in liquidazione giudiziale e diritto di prelazione (art. 212 CCII)",
        "seo_title": "Affitto Azienda Liquidazione Giudiziale Art. 212 CCII: Gara e Prelazione",
        "desc": "Come acquisire in affitto (e poi in proprieta') un'azienda da una liquidazione giudiziale con esonero dai debiti pregressi e procedura competitiva.",
        "keywords": ["affitto azienda liquidazione giudiziale art 212", "acquisto azienda da fallimento senza debiti", "prelazione affittuario art 212 ccii"],
        "norme": ["Art. 212 CCII", "Art. 214 CCII", "Art. 2560 c.c."],
        "scenario": "Un imprenditore o investitore vuole rilevare lo stabilimento, il marchio o il ramo operativo di una societa' in liquidazione giudiziale senza ereditare i debiti pregressi.",
        "rischio": "Senza gara competitiva autorizzata e clausole corrette su prelazione e personale, l'affittuario puo' perdere l'azienda all'asta finale o subire contenziosi sindacali.",
        "protocollo": [
            "Presentare al curatore una manifestazione d'interesse seria corredata da piano industriale, garanzie fideiussorie e mantenimento livelli occupazionali.",
            "Partecipare alla procedura competitiva ex art. 212 CCII negoziando la durata, il canone e il diritto di prelazione convenzionale (autorizzabile dal giudice delegato ex art. 212 co. 5).",
            "Svolgere la consultazione sindacale ex art. 47 L. 428/1990 per modulare il passaggio dei lavoratori.",
            "Alla vendita definitiva ex art. 214 CCII, beneficiare dell'esclusione di responsabilita' per i debiti pregressi dell'azienda (art. 214 co. 3 CCII)."
        ],
        "prove": ["Manifestazione di interesse e piano industriale di rilancio", "Bando competitivo del curatore e contratto di affitto notarile", "Autorizzazione del giudice delegato e parere del comitato creditori", "Verbale di accordo sindacale ex art. 47 L. 428/1990"],
        "errori": ["Stipulare un affitto privo di prelazione senza valutare il rischio di rilanci d'asta futuri", "Trascurare gli obblighi ambientali o di sicurezza sugli impianti affittati", "Omettere l'accordo sindacale sul passaggio dei dipendenti"]
    },
    {
        "cod": "SOC-104", "slug": "concordato-nella-liquidazione-giudiziale-art-240-ccii",
        "cat": "liquidazione-giudiziale", "cat_lbl": "Liquidazione Giudiziale", "pilastro": "liquidazione-giudiziale-fallimento-opposizioni",
        "titolo": "Concordato nella liquidazione giudiziale (ex concordato fallimentare) art. 240 CCII",
        "seo_title": "Concordato nella Liquidazione Giudiziale Art. 240 CCII: Assuntore",
        "desc": "Come chiudere anticipatamente la liquidazione giudiziale rilevando tutto l'attivo (e le azioni risarcitorie) tramite un terzo assuntore o proposta del debitore.",
        "keywords": ["concordato liquidazione giudiziale art 240", "concordato fallimentare assuntore", "chiusura anticipata liquidazione giudiziale"],
        "norme": ["Art. 240 CCII", "Art. 241 CCII", "Art. 245 CCII"],
        "scenario": "Un investitore terzo (assuntore) o un creditore vuole rilevare in blocco immobili, crediti e asset della liquidazione giudiziale proponendo un pagamento immediato ai creditori.",
        "rischio": "Il debitore e le societa' a lui riconducibili non possono presentare la proposta prima di 1 anno dall'apertura e comunque devono apportare risorse che incrementino l'attivo almeno del 10% (art. 240 co. 1 CCII).",
        "protocollo": [
            "Verificare la legittimazione: un terzo o un creditore puo' presentare la proposta anche subito (prima del decreto di esecutivita' dello stato passivo se i dati contabili consentono l'elenco provvisorio).",
            "Strutturare la proposta con assuntore, eventuale suddivisione in classi, falcidia dei privilegiati incapienti e cessione delle azioni di massa gia' autorizzate.",
            "Acquisire il parere favorevole del curatore e del comitato dei creditori per accedere al voto (silenzio-assenso ex art. 244 CCII).",
            "Ottenere l'omologazione dal Tribunale con immediata chiusura della liquidazione giudiziale e trasferimento dei beni all'assuntore."
        ],
        "prove": ["Ricorso con proposta di concordato nella liquidazione giudiziale", "Garanzie bancarie o deposito vincolato dell'assuntore", "Perizia ex art. 240 co. 4 CCII in caso di falcidia dei privilegiati", "Pareri di curatore e comitato creditori"],
        "errori": ["Presentare la proposta direttamente come debitore prima del decorso di 1 anno o senza l'incremento del 10% di risorse esterne", "Non valutare la convenienza del silenzio-assenso dei creditori nel voto", "Trascurare le azioni risarcitorie o revocatorie gia' pendenti"]
    },
    {
        "cod": "SOC-105", "slug": "chiusura-liquidazione-giudiziale-riparto-finale-art-233",
        "cat": "liquidazione-giudiziale", "cat_lbl": "Liquidazione Giudiziale", "pilastro": "liquidazione-giudiziale-fallimento-opposizioni",
        "titolo": "Chiusura della liquidazione giudiziale, rendiconto del curatore e riparto finale (artt. 231-233 CCII)",
        "seo_title": "Chiusura Liquidazione Giudiziale Art. 233 CCII e Osservazioni Rendiconto",
        "desc": "Come contestare il rendiconto finale del curatore o il piano di riparto, tutelare i creditori in chiusura in pendenza di giudizi e attivare l'esdebitazione.",
        "keywords": ["chiusura liquidazione giudiziale art 233", "contestazione rendiconto curatore art 231", "reclamo piano riparto art 220 ccii"],
        "norme": ["Art. 231 CCII", "Art. 233 CCII", "Art. 234 CCII"],
        "scenario": "La liquidazione giudiziale giunge al rendiconto del curatore e al riparto finale, ma emergono contestazioni su spese di gestione, compensi, ordine dei privilegi o giudizi ancora pendenti.",
        "rischio": "La mancata presentazione di osservazioni al rendiconto o di reclamo al progetto di riparto entro 15 giorni rende definitive le distribuzioni.",
        "protocollo": [
            "Esaminare analiticamente il rendiconto di gestione del curatore e depositare osservazioni scritte prima dell'udienza ex art. 231 CCII in caso di irregolarita' o spese ingiustificate.",
            "Verificare il progetto di riparto finale (rispetto rigoroso dell'ordine di prededuzione, privilegi speciali/generali e chirografi) e proporre eventuale reclamo entro 15 giorni ex art. 220 CCII.",
            "In caso di chiusura in pendenza di giudizi (art. 234 CCII), verificare gli accantonamenti obbligatori a tutela dei creditori.",
            "Per la persona fisica o societa', attivare tempestivamente il percorso di esdebitazione (artt. 278-281 CCII)."
        ],
        "prove": ["Rendiconto di gestione del curatore e conto economico della procedura", "Progetto di riparto finale e PEC di comunicazione", "Osservazioni scritte o reclamo entro 15 giorni", "Decreto di chiusura ex art. 233 CCII"],
        "errori": ["Far scadere i 15 giorni per il reclamo contro il progetto di riparto", "Non verificare la corretta graduazione delle prededuzioni e dei privilegi", "Dimenticare di chiedere l'esdebitazione alla chiusura o allo scadere del triennio"]
    },

    # ═══════════════════ 6. PENALE SOCIETARIO & BANCAROTTA (106-125) ═══════════════════
    {
        "cod": "SOC-106", "slug": "bancarotta-fraudolenta-patrimoniale-distrazione-art-322-ccii",
        "cat": "penale-societario", "cat_lbl": "Bancarotta & Reati", "pilastro": "bancarotta-reati-fallimentari-societari",
        "titolo": "Difesa penale per bancarotta fraudolenta patrimoniale per distrazione (art. 322 CCII)",
        "seo_title": "Bancarotta Fraudolenta Patrimoniale Art. 322 CCII: Difesa Penale",
        "desc": "Come difendere l'amministratore dall'accusa di distrazione di beni, cassa o rami d'azienda (pene 3-10 anni): perizia contabile, prova della destinazione aziendale e bancarotta riparata.",
        "keywords": ["bancarotta fraudolenta patrimoniale art 322", "difesa distrazione beni fallimento", "bancarotta riparata restituzione"],
        "norme": ["Art. 322 co. 1 n. 1 CCII", "Art. 329 CCII", "Art. 216 L.F."],
        "scenario": "La relazione del curatore segnala ammanchi di cassa, vendite di beni a prezzo ritenuto vile o mancato rinvenimento di macchinari e merci, portando all'imputazione per bancarotta fraudolenta patrimoniale.",
        "rischio": "Reclusione da 3 a 10 anni, inabilitazione all'esercizio d'impresa fino a 10 anni e misure cautelari personali o reali.",
        "protocollo": [
            "Acquisire integralmente la relazione del curatore, gli estratti conto e i mastrini per ricostruire con un consulente tecnico contabile la reale destinazione di ogni singolo euro contestato.",
            "Dimostrare che le somme o i beni sono stati impiegati per pagare debiti aziendali, fornitori o lavoratori (escludendo la distrazione o riqualificando al piu' in preferenziale).",
            "Verificare se i beni non rinvenuti erano obsoleti, rottamati, invendibili o di valore nullo (mancanza di concreta offensivita' / zona di rischio penale).",
            "Valutare la 'bancarotta riparata' (restituzione integrale prima della sentenza di liquidazione giudiziale) o la riqualificazione in bancarotta semplice."
        ],
        "prove": ["Relazione ex art. 130 CCII / 33 L.F. e inventario del curatore", "Perizia contabile di parte su estratti conto e flussi di cassa", "Fatture, bonifici, quietanze fornitori e verbali di rottamazione/obsolescenza", "Prove di restituzione anteriore alla procedura (bancarotta riparata)"],
        "errori": ["Rendere interrogatorio senza aver prima ricostruito i flussi bancari con un consulente contabile", "Confondere un saldo contabile di cassa fittizio con una reale sottrazione di denaro", "Trascurare il requisito della concreta messa in pericolo della garanzia patrimoniale"]
    },
    {
        "cod": "SOC-107", "slug": "bancarotta-fraudolenta-documentale-scritture-contabili-art-322",
        "cat": "penale-societario", "cat_lbl": "Bancarotta & Reati", "pilastro": "bancarotta-reati-fallimentari-societari",
        "titolo": "Difesa per bancarotta fraudolenta documentale: omessa o irregolare tenuta scritture (art. 322 CCII)",
        "seo_title": "Bancarotta Fraudolenta Documentale Art. 322 CCII: Dolo Specifico vs Semplice",
        "desc": "Come smontare l'imputazione di bancarotta fraudolenta documentale (generica o specifica) e ottenere l'assoluzione o la riqualificazione in bancarotta semplice documentale (art. 323).",
        "keywords": ["bancarotta fraudolenta documentale art 322", "differenza bancarotta documentale semplice", "dolo specifico omessa tenuta scritture"],
        "norme": ["Art. 322 co. 1 n. 2 CCII", "Art. 323 co. 2 CCII", "Art. 329 CCII"],
        "scenario": "Il curatore riferisce che l'amministratore non ha consegnato i libri contabili oppure che la contabilita' e' tenuta in modo incompleto o confuso.",
        "rischio": "La Procura contesta quasi automaticamente la bancarotta fraudolenta documentale (3-10 anni) invece della ben piu' lieve bancarotta semplice documentale (6 mesi - 2 anni).",
        "protocollo": [
            "Verificare se il curatore e' comunque riuscito a ricostruire il patrimonio e il movimento degli affari tramite fatture elettroniche SDI, estratti conto bancari e cassetto fiscale.",
            "Contestare l'assenza del dolo specifico (scopo di recare pregiudizio ai creditori o procurare ingiusto profitto) richiesto per l'ipotesi di sottrazione/occultamento/omessa tenuta delle scritture.",
            "Dimostrare che la mancata consegna o l'incompletezza dipende da negligenza, mancato pagamento del commercialista o caos organizzativo (riqualificazione in bancarotta semplice ex art. 323 co. 2 CCII).",
            "Recuperare subito presso commercialisti, banche o server cloud ogni documento contabile residuo e consegnarlo formalmente al curatore."
        ],
        "prove": ["Verbali di consegna documentazione al curatore e PEC al commercialista", "Estratti conto, fatture SDI e dichiarazioni fiscali che consentono la ricostruzione degli affari", "Corrispondenza che prova la trattenuta dei libri o l'interruzione del rapporto col consulente", "Consulenza tecnica sulla ricostruibilita' contabile"],
        "errori": ["Non consegnare la contabilita' al curatore per paura o inerzia", "Accettare la contestazione di dolo specifico quando mancano del tutto fatti distrattivi sottostanti", "Dimenticare che oggi con la fatturazione elettronica SDI quasi tutto il movimento d'affari e' ricostruibile"]
    },
    {
        "cod": "SOC-108", "slug": "bancarotta-preferenziale-pagamenti-selettivi-art-322-co-3",
        "cat": "penale-societario", "cat_lbl": "Bancarotta & Reati", "pilastro": "bancarotta-reati-fallimentari-societari",
        "titolo": "Bancarotta preferenziale per pagamenti selettivi o rimborso finanziamento soci (art. 322 co. 3 CCII)",
        "seo_title": "Bancarotta Preferenziale Art. 322 co. 3 CCII: Difesa e Dolo Specifico",
        "desc": "Difesa penale per pagamenti eseguiti in stato di insolvenza a favore di singoli creditori (o dello stesso amministratore): esclusione del dolo specifico e continuita' aziendale.",
        "keywords": ["bancarotta preferenziale art 322 comma 3", "rimborso finanziamento soci bancarotta", "pagamenti selettivi in crisi"],
        "norme": ["Art. 322 co. 3 CCII", "Art. 324 CCII", "Art. 2467 c.c."],
        "scenario": "Prima della liquidazione giudiziale l'amministratore ha pagato alcuni fornitori strategici, dipendenti o banche garantite da fideiussione personale, oppure ha rimborsato un finanziamento soci.",
        "rischio": "Reclusione da 1 a 5 anni per bancarotta preferenziale (o fino a 10 anni se il PM riqualifica il rimborso al socio come distrazione).",
        "protocollo": [
            "Dimostrare che il pagamento aveva come finalita' esclusiva o prevalente il salvataggio dell'impresa e la continuazione dell'attivita' (pagamenti a fornitori essenziali o lavoratori), il che esclude il dolo specifico di favorire un creditore a danno degli altri.",
            "Verificare se i pagamenti rientrano nelle esenzioni penali dell'art. 324 CCII (atti compiuti in esecuzione di piano attestato, ARD, concordato o Composizione Negoziata).",
            "Distinguere nettamente la bancarotta preferenziale (credito reale preesistente, pena 1-5 anni) dalla distrazione (credito inesistente, pena 3-10 anni).",
            "Verificare se il credito pagato godeva comunque di privilegio di grado superiore o uguale."
        ],
        "prove": ["Fatture, contratti e prova dell'esistenza reale e anteriorita' del credito pagato", "Documentazione del piano di salvataggio o della essenzialita' del fornitore per la continuita'", "Prove dell'assenza di insolvenza conclamata alla data del pagamento", "Esenzioni ex art. 324 CCII ove presenti"],
        "errori": ["Rimborsare i propri finanziamenti soci quando la societa' e' gia' insolvente", "Pagare solo le banche per liberare le proprie fideiussioni personali trascurando gli altri creditori", "Non distinguere la preferenziale dalla distrattiva nella strategia difensiva"]
    },
    {
        "cod": "SOC-109", "slug": "bancarotta-semplice-aggravamento-dissesto-art-323-ccii",
        "cat": "penale-societario", "cat_lbl": "Bancarotta & Reati", "pilastro": "bancarotta-reati-fallimentari-societari",
        "titolo": "Bancarotta semplice per aggravamento del dissesto o ritardo nell'istanza (art. 323 CCII)",
        "seo_title": "Bancarotta Semplice Art. 323 CCII: Colpa Grave e Difesa",
        "desc": "Difesa penale per aggravamento del dissesto, operazioni gravemente imprudenti o irregolare tenuta dei libri nei tre anni anteriori: esclusione colpa grave, prescrizione e riti premiali.",
        "keywords": ["bancarotta semplice art 323 ccii", "aggravamento dissesto colpa grave", "ritardo istanza fallimento bancarotta"],
        "norme": ["Art. 323 CCII", "Art. 330 CCII", "Art. 131-bis c.p."],
        "scenario": "La Procura contesta all'amministratore di aver aggravato il dissesto astenendosi dal richiedere la liquidazione giudiziale o compiendo operazioni imprudenti con colpa grave.",
        "rischio": "Reclusione da 6 mesi a 2 anni e inabilitazione fino a 2 anni, oltre a condanna risarcitoria verso la curatela costituita parte civile.",
        "protocollo": [
            "Dimostrare che la prosecuzione dell'attivita' rispondeva a una ragionevole prospettiva di risanamento (es. trattative con banche, commesse in arrivo, advisor incaricati), escludendo la 'colpa grave'.",
            "Quantificare con perizia contabile se vi e' stato realmente un aggravamento imputabile alla gestione o solo il maturare fisiologico di interessi e sanzioni.",
            "Verificare la causa di non punibilita' per particolare tenuita' del fatto (art. 131-bis c.p.) o la messa alla prova (art. 168-bis c.p.) applicabile alla bancarotta semplice.",
            "Verificare l'eventuale estinzione per prescrizione."
        ],
        "prove": ["Verbali CdA, lettere di incarico ad advisor e trattative bancarie", "Perizia contabile sulla dinamica del passivo", "Assenza di condotte fraudolente o speculative", "Eventuale risarcimento o accordo con la curatela"],
        "errori": ["Sottovalutare la bancarotta semplice pensando che non comporti conseguenze penali o interdittive", "Non valutare la sospensione con messa alla prova (che estingue il reato)", "Non contestare la sussistenza della colpa grave"]
    },
    {
        "cod": "SOC-110", "slug": "bancarotta-impropria-reato-societario-falso-bilancio-art-329",
        "cat": "penale-societario", "cat_lbl": "Bancarotta & Reati", "pilastro": "bancarotta-reati-fallimentari-societari",
        "titolo": "Bancarotta impropria da reato societario (falso in bilancio) ex art. 329 co. 2 n. 1 CCII",
        "seo_title": "Bancarotta Impropria da Falso in Bilancio Art. 329 co. 2 CCII",
        "desc": "Difesa penale per amministratori e sindaci accusati di aver cagionato o aggravato il dissesto tramite false comunicazioni sociali: prova rigorosa del nesso causale.",
        "keywords": ["bancarotta impropria reato societario art 329", "falso in bilancio aggravamento dissesto", "nesso causale bancarotta impropria"],
        "norme": ["Art. 329 co. 2 n. 1 CCII", "Artt. 2621-2622 c.c."],
        "scenario": "L'accusa sostiene che l'esposizione in bilancio di crediti inesigibili, rimanenze gonfiate o perdite occultate abbia nascosto il dissesto consentendo la prosecuzione in perdita fino alla liquidazione giudiziale.",
        "rischio": "Pena edittale da 3 a 10 anni di reclusione, estesa frequentemente anche a sindaci e direttori generali.",
        "protocollo": [
            "Esigere la prova rigorosa del nesso causale effettivo: il reato societario (falso in bilancio) deve aver cagionato o concretamente concorso a cagionare il dissesto (non basta la mera coesistenza cronologica).",
            "Dimostrare con perizia contabile la correttezza o ragionevolezza delle stime di bilancio secondo i principi OIC vigenti al momento della redazione (no giudizio 'col senno di poi').",
            "Verificare il dolo intenzionale del reato societario presupposto (escludendo errori valutativi o colpa).",
            "Per gli amministratori senza deleghe e i sindaci, dimostrare l'assenza di segnali d'allarme inequivoci e la buona fede."
        ],
        "prove": ["Bilanci contestati, relazioni del revisore e principi contabili OIC applicati", "Perizia tecnica di parte sulla valutazione di rimanenze e crediti ex ante", "Documentazione di cause esogene del dissesto (crisi mercato, insolvenza clienti, pandemia)", "Verbali di CdA e collegio sindacale"],
        "errori": ["Accettare la valutazione del curatore fatta col senno di poi anziche' ex ante", "Non contestare la mancanza di prova del nesso causale tra posta di bilancio e dissesto", "Trascurare la difesa tecnica contabile sin dalle indagini preliminari"]
    },
    {
        "cod": "SOC-111", "slug": "bancarotta-impropria-operazioni-dolose-omesso-versamento-imposte",
        "cat": "penale-societario", "cat_lbl": "Bancarotta & Reati", "pilastro": "bancarotta-reati-fallimentari-societari",
        "titolo": "Bancarotta impropria da operazioni dolose: sistematico omesso versamento di imposte e contributi (art. 329 co. 2 n. 2 CCII)",
        "seo_title": "Bancarotta da Operazioni Dolose e Debiti Fiscali Art. 329 CCII",
        "desc": "Come difendere l'imprenditore accusato di aver causato il fallimento omettendo sistematicamente di pagare IVA, IRES e contributi INPS per autofinanziare l'impresa.",
        "keywords": ["bancarotta operazioni dolose omesso versamento imposte", "art 329 comma 2 n 2 ccii", "sistematico inadempimento fiscale bancarotta"],
        "norme": ["Art. 329 co. 2 n. 2 CCII", "Art. 223 co. 2 n. 2 L.F."],
        "scenario": "Un'impresa in difficolta' paga fornitori e stipendi ma accumula per anni ingenti debiti verso Erario e INPS fino alla liquidazione giudiziale, portando la Procura a contestare la bancarotta da operazioni dolose.",
        "rischio": "Pena da 3 a 10 anni anche in assenza di qualsiasi distrazione personale di denaro da parte dell'amministratore.",
        "protocollo": [
            "Dimostrare che l'inadempimento tributario non era una deliberata strategia di autofinanziamento illecito ma l'effetto di una crisi di liquidita' esterna e improvvisa (es. mancati incassi da clienti o PA).",
            "Produrre istanze di rateazione, rottamazioni, pagamenti parziali e tentativi documentati di riequilibrio che escludono il dolo e la prevedibilita' del dissesto.",
            "Verificare il nesso causale: dimostrare se il dissesto era gia' irreversibile per altre cause o se i debiti fiscali non ne sono stati la causa determinante.",
            "Chiedere in subordine la riqualificazione in bancarotta semplice per aggravamento colposo del dissesto (art. 323 CCII)."
        ],
        "prove": ["Piani di rateazione AdER/INPS, pagamenti eseguiti e crediti inesigibili verso clienti/PA", "Perizia contabile sulla genesi della crisi e sulle cause reali del dissesto", "Documentazione di apporti personali dell'amministratore a sostegno dell'azienda", "Assenza di prelievi personali o distrazioni"],
        "errori": ["Accumulare debiti fiscali per anni senza mai presentare istanze di rateazione ne' accedere a strumenti di composizione della crisi", "Confondere l'omesso versamento isolato con la bancarotta da operazioni dolose", "Non dimostrare gli apporti di capitale proprio effettuati dall'imprenditore per salvare l'impresa"]
    },
    {
        "cod": "SOC-112", "slug": "ricorso-abusivo-credito-art-325-ccii-difesa",
        "cat": "penale-societario", "cat_lbl": "Bancarotta & Reati", "pilastro": "bancarotta-reati-fallimentari-societari",
        "titolo": "Ricorso abusivo al credito (art. 325 CCII) e responsabilita' concorrente",
        "seo_title": "Ricorso Abusivo al Credito Art. 325 CCII: Difesa Imprenditore",
        "desc": "Difesa penale dall'accusa di aver ottenuto finanziamenti bancari o forniture a credito dissimulando il dissesto della societa'.",
        "keywords": ["ricorso abusivo al credito art 325 ccii", "dissimulazione dissesto banche", "difesa art 325 codice crisi"],
        "norme": ["Art. 325 CCII", "Art. 218 L.F."],
        "scenario": "L'accusa contesta all'amministratore di aver continuato a ottenere linee di credito bancarie o forniture dilazionate nascondendo ai creditori lo stato di dissesto dell'azienda.",
        "rischio": "Reclusione da 6 mesi a 3 anni (e rischio di assorbimento o cumulo con la bancarotta impropria) oltre a richieste risarcitorie delle banche.",
        "protocollo": [
            "Dimostrare la mancanza di qualsiasi condotta artificiosa di 'dissimulazione': i bilanci erano pubblici, la Centrale Rischi era visibile e la banca conosceva pienamente la situazione finanziaria.",
            "Provare che all'epoca del finanziamento l'impresa versava in temporanea tensione finanziaria e non in dissesto irreversibile.",
            "Verificare l'eventuale concorso della banca per concessione abusiva di credito (che spezza il quadro dell'inganno unilaterale).",
            "Valutare riti alternativi o estinzione/tenuita' ove ne ricorrano i presupposti."
        ],
        "prove": ["Bilanci depositati e documenti consegnati alla banca in istruttoria fidi", "Centrale Rischi Banca d'Italia dell'epoca", "Corrispondenza trasparente con istituti di credito e fornitori", "Perizia sullo stato finanziario al momento dell'erogazione"],
        "errori": ["Presentare situazioni contabili provvisorie alterate alle banche per ottenere fidi", "Non eccepire la piena conoscibilita' dei dati aziendali da parte della banca", "Trascurare il raccordo tra difesa penale e azioni civili bancarie"]
    },
    {
        "cod": "SOC-113", "slug": "denuncia-creditori-inesistenti-art-327-ccii",
        "cat": "penale-societario", "cat_lbl": "Bancarotta & Reati", "pilastro": "bancarotta-reati-fallimentari-societari",
        "titolo": "Denuncia di creditori inesistenti o inosservanza obblighi del debitore (art. 327 CCII)",
        "seo_title": "Denuncia Creditori Inesistenti Art. 327 CCII: Difesa Penale",
        "desc": "Difesa penale per contestazioni su omissione di beni dall'inventario, indicazione di crediti fittizi o mancata presentazione davanti al curatore.",
        "keywords": ["denuncia creditori inesistenti art 327 ccii", "omissione beni inventario fallimento", "inosservanza obblighi debitore ccii"],
        "norme": ["Art. 327 CCII", "Art. 220 L.F."],
        "scenario": "Il curatore segnala alla Procura che nell'elenco consegnato dall'amministratore mancano alcuni beni aziendali, compaiono creditori contestati oppure il debitore non si e' presentato alla convocazione.",
        "rischio": "Condanna fino a 18 mesi (o fino a 6 mesi per ipotesi colpose) e aggravamento del sospetto investigativo per bancarotta fraudolenta.",
        "protocollo": [
            "Verificare subito se l'omissione o l'inesattezza e' dovuta a mero errore contabile o disallineamento temporale privo di dolo.",
            "Integrare immediatamente e spontaneamente l'elenco beni/creditori collaborando formalmente con il curatore tramite difensore.",
            "Dimostrare la giustificata impossibilita' o mancata ricezione della convocazione in caso di contestata assenza.",
            "Richiedere la non punibilita' per particolare tenuita' (art. 131-bis c.p.) o l'assoluzione per difetto di elemento soggettivo."
        ],
        "prove": ["Comunicazioni PEC di integrazione e collaborazione col curatore", "Documentazione giustificativa di eventuali crediti contestati", "Prove di impedimento o vizi di notifica della convocazione", "Ricostruzione contabile dei beni segnalati"],
        "errori": ["Non rispondere alle PEC del curatore o disertare l'audizione senza giustificazione", "Fornire elenchi approssimativi senza controllo del commercialista", "Sottovalutare come la mancata collaborazione inneschi l'indagine per bancarotta"]
    },
    {
        "cod": "SOC-114", "slug": "difesa-amministratore-di-fatto-bancarotta-art-2639-cc",
        "cat": "penale-societario", "cat_lbl": "Bancarotta & Reati", "pilastro": "bancarotta-reati-fallimentari-societari",
        "titolo": "Difesa del presunto amministratore di fatto nella bancarotta (art. 2639 c.c.)",
        "seo_title": "Difesa Amministratore di Fatto nella Bancarotta Art. 2639 c.c.",
        "desc": "Come smontare la qualifica di amministratore di fatto: prova della continuita' e significativita' dei poteri gestori vs singole ingerenze, consulenze o ruoli familiari.",
        "keywords": ["amministratore di fatto bancarotta art 2639", "difesa amministratore di fatto", "poteri gestori continuativi significativi"],
        "norme": ["Art. 2639 c.c.", "Art. 322 CCII", "Art. 329 CCII"],
        "scenario": "Un ex amministratore, un socio di maggioranza, un familiare o un consulente viene imputato di bancarotta come 'amministratore di fatto' pur non ricoprendo alcuna carica formale.",
        "rischio": "Equiparazione totale all'amministratore di diritto con esposizione a pene fino a 10 anni e sequestri personali.",
        "protocollo": [
            "Richiamare i requisiti rigorosi dell'art. 2639 c.c.: la qualifica di amministratore di fatto richiede l'esercizio 'in modo continuativo e significativo' dei poteri tipici della funzione gestoria, non singoli atti isolati o pareri.",
            "Dimostrare tramite testimoni (dipendenti, banche, fornitori), deleghe bancarie e corrispondenza chi prendeva realmente le decisioni operative e firmava i pagamenti.",
            "Distinguere nettamente l'attivita' di supporto tecnico/commerciale o di mero socio dalla gestione effettiva della societa'.",
            "Contestare l'uso di dichiarazioni interessate e non riscontrate dell'amministratore di diritto che tenta di scaricare le proprie colpe."
        ],
        "prove": ["Firme depositate in banca, home banking e deleghe operative", "Testimonianze di dipendenti, fornitori, clienti e commercialista", "Corrispondenza email/PEC che individua il reale decisore aziendale", "Contratti di consulenza o ruolo meramente esecutivo/familiare"],
        "errori": ["Dare per scontata la qualifica di amministratore di fatto senza demolire i riscontri", "Non chiamare a testimoniare dipendenti e fornitori sui reali rapporti gerarchici", "Sottovalutare le dichiarazioni auto-difensive dell'amministratore formale"]
    },
    {
        "cod": "SOC-115", "slug": "difesa-prestanome-testa-di-legno-bancarotta-fraudolenta",
        "cat": "penale-societario", "cat_lbl": "Bancarotta & Reati", "pilastro": "bancarotta-reati-fallimentari-societari",
        "titolo": "Difesa dell'amministratore prestanome ('testa di legno') nei processi per bancarotta",
        "seo_title": "Difesa Amministratore Prestanome (Testa di Legno) in Bancarotta",
        "desc": "Come difendere l'amministratore meramente formale: esclusione del dolo rispetto alle distrazioni commesse dal gestore occulto e mitigazione sulla bancarotta documentale.",
        "keywords": ["difesa prestanome bancarotta", "testa di legno bancarotta fraudolenta", "dolo eventuale amministratore formale"],
        "norme": ["Art. 40 co. 2 c.p.", "Art. 322 CCII", "Art. 2392 c.c."],
        "scenario": "Un soggetto privo di reali poteri (spesso un familiare, un dipendente o una persona in difficolta') ha accettato la carica formale di amministratore mentre un altro gestiva integralmente la societa' svuotandola.",
        "rischio": "Condanna per concorso omissivo ex art. 40 co. 2 c.p. in bancarotta fraudolenta patrimoniale e documentale se non si smonta l'elemento psicologico.",
        "protocollo": [
            "Contestare ogni automatismo sulla bancarotta patrimoniale: per condannare il prestanome per distrazioni altrui serve la prova della concreta consapevolezza dello stato delle scritture e di segnali perspicui e peculiari delle condotte distrattive (non basta la mera accettazione della carica).",
            "Dimostrare la totale estraneita' a conti correnti, token bancari, sede operativa e decisioni, provando che il prestanome non ha percepito alcun profitto.",
            "Sulla bancarotta documentale, lavorare per escludere il dolo specifico e riqualificare nella bancarotta semplice documentale (art. 323 co. 2 CCII).",
            "Valutare il contributo collaborativo per identificare il reale dominus e ottenere le attenuanti o la riduzione di pena."
        ],
        "prove": ["Prova che token bancari, PEC e contabilita' erano gestiti esclusivamente dal dominus occulto", "Estratti conto personali del prestanome privi di accrediti o tenore di vita anomalo", "Testimonianze e messaggi che provano la totale estromissione gestionale", "Eventuale disconoscimento di firme apocrife"],
        "errori": ["Assumersi colpe altrui in interrogatorio per timore o sudditanza verso il gestore occulto", "Condividere lo stesso difensore dell'amministratore di fatto (conflitto di interessi insanabile)", "Non distinguere la difesa sulla bancarotta patrimoniale da quella sulla documentale"]
    },
    {
        "cod": "SOC-116", "slug": "concorso-extraneus-commercialista-professionista-bancarotta",
        "cat": "penale-societario", "cat_lbl": "Bancarotta & Reati", "pilastro": "bancarotta-reati-fallimentari-societari",
        "titolo": "Difesa del commercialista, consulente o terzo (extraneus) accusato di concorso in bancarotta",
        "seo_title": "Concorso dell'Extraneus e Commercialista in Bancarotta: Difesa",
        "desc": "Limiti alla responsabilita' penale del professionista o terzo contraente ex art. 110 c.p. nella bancarotta: distinzione tra consulenza lecita e contributo causale doloso.",
        "keywords": ["concorso extraneus bancarotta", "commercialista concorso bancarotta fraudolenta", "difesa professionista art 110 cp"],
        "norme": ["Art. 110 c.p.", "Art. 117 c.p.", "Art. 322 CCII"],
        "scenario": "Un commercialista, consulente finanziario o acquirente di un ramo d'azienda viene indagato per concorso esterno in bancarotta fraudolenta insieme agli amministratori della societa' fallita.",
        "rischio": "Esposizione alle stesse pene dell'amministratore (3-10 anni), radiazione dall'albo professionale e sequestri sul patrimonio personale.",
        "protocollo": [
            "Dimostrare che l'attivita' professionale si e' svolta nell'ambito della consulenza tecnica fisiologica (es. redazione bilanci sui dati forniti dal cliente o assistenza a un tentativo serio di risanamento).",
            "Contestare l'assenza del contributo causale efficiente e soprattutto della consapevolezza certa dello stato di dissesto e del proposito distrattivo dell'amministratore.",
            "Produrre mandati professionali, email di raccomandazione/diffida al cliente e perizie di congruita' delle operazioni.",
            "Escludere qualsiasi cointeressenza economica anomala oltre al normale onorario professionale."
        ],
        "prove": ["Lettera di incarico professionale e fatture dei compensi ordinari", "Email e pareri scritti inviati all'amministratore con raccomandazioni di regolarita'", "Perizie di stima a supporto delle operazioni straordinarie contestate", "Assenza di poteri gestori o vantaggi personali indebiti"],
        "errori": ["Non conservare traccia scritta delle raccomandazioni e dei pareri resi al cliente", "Farsi coinvolgere operativamente nella gestione di cassa o nella creazione di societa' schermo", "Non separare immediatamente la propria difesa da quella dell'imprenditore"]
    },
    {
        "cod": "SOC-117", "slug": "bancarotta-infragruppo-vantaggi-compensativi-art-2634",
        "cat": "penale-societario", "cat_lbl": "Bancarotta & Reati", "pilastro": "bancarotta-reati-fallimentari-societari",
        "titolo": "Bancarotta infragruppo e scriminante dei vantaggi compensativi (art. 2634 co. 3 c.c.)",
        "seo_title": "Bancarotta Infragruppo e Vantaggi Compensativi: Difesa Holding",
        "desc": "Come difendere i trasferimenti di liquidita', garanzie o beni tra societa' dello stesso gruppo dimostrando i vantaggi compensativi reali o ragionevolmente prevedibili.",
        "keywords": ["bancarotta infragruppo vantaggi compensativi", "trasferimenti infragruppo fallimento", "art 2634 comma 3 codice civile"],
        "norme": ["Art. 2634 co. 3 c.c.", "Art. 2497 c.c.", "Art. 322 CCII"],
        "scenario": "Una societa' del gruppo va in liquidazione giudiziale e la Procura contesta come distrazione i finanziamenti, il cash pooling o le garanzie prestate a favore della holding o di societa' sorelle.",
        "rischio": "Qualificazione dei flussi infragruppo come bancarotta fraudolenta patrimoniale per gli amministratori di entrambe le societa'.",
        "protocollo": [
            "Dimostrare con perizia economico-aziendale l'esistenza di un vero gruppo e di vantaggi compensativi concreti, gia' conseguiti o fondatamente prevedibili ex ante, a beneficio della societa' disponente.",
            "Produrre contratti di cash pooling, service agreements e garanzie reciproche con condizioni trasparenti e remunerazioni congrue.",
            "Dimostrare che al momento dell'operazione infragruppo la societa' non versava in stato di insolvenza conclamata.",
            "Quantificare i flussi in dare e avere per provare il saldo equilibrato o favorevole nel medio periodo."
        ],
        "prove": ["Contratti infragruppo e accordi di cash pooling con data certa", "Bilanci consolidati e prospetti dare/avere tra le societa' del gruppo", "Perizia industriale sui vantaggi sinergici e compensativi (es. accesso al credito, commesse condivise)", "Delibere motivate dei CdA ai sensi dell'art. 2497-ter c.c."],
        "errori": ["Spostare cassa da una societa' gia' decotta a una sorella sana senza alcuna contropartita", "Non redigere contratti scritti ne' delibere motivate ex art. 2497-ter c.c.", "Invocare genericamente 'l'interesse di gruppo' senza provare il vantaggio compensativo per la singola societa'"]
    },
    {
        "cod": "SOC-118", "slug": "compensi-amministratore-prelievi-soci-contestati-distrazione",
        "cat": "penale-societario", "cat_lbl": "Bancarotta & Reati", "pilastro": "bancarotta-reati-fallimentari-societari",
        "titolo": "Compensi dell'amministratore e prelievi dei soci contestati come bancarotta per distrazione",
        "seo_title": "Compensi Amministratore e Bancarotta per Distrazione: Difesa",
        "desc": "Quando il prelievo di compensi dell'amministratore integra bancarotta distrattiva vs preferenziale vs condotta lecita: delibera assembleare, congruita' e lavoro effettivo.",
        "keywords": ["compensi amministratore bancarotta distrazione", "prelievi amministratore senza delibera", "bancarotta preferenziale compensi"],
        "norme": ["Art. 322 CCII", "Art. 2389 c.c."],
        "scenario": "Il curatore e la Procura contestano come distrazione i bonifici incassati dall'amministratore a titolo di compenso, rimborsi spese o prelievi soci negli anni anteriori alla liquidazione.",
        "rischio": "Trattamento di compensi per lavoro effettivamente svolto come reato di bancarotta fraudolenta patrimoniale (3-10 anni).",
        "protocollo": [
            "Produrre le delibere assembleari di attribuzione del compenso, i cedolini/fatture e le certificazioni fiscali (CU) che provano la piena legittimita' e trasparenza del titolo.",
            "Anche in assenza di delibera formale, dimostrare l'effettiva attivita' lavorativa quotidiana svolta dall'amministratore e la congruita' dell'importo rispetto ai parametri di mercato (escludendo la natura distrattiva o riqualificando al piu' in bancarotta preferenziale se in stato di insolvenza).",
            "Documentare la reale inerenza aziendale di rimborsi spese, carte aziendali e trasferte.",
            "Dimostrare eventuali versamenti personali eseguiti dallo stesso amministratore in favore della societa' (saldo netto positivo)."
        ],
        "prove": ["Delibere assembleari di determinazione compensi e buste paga/CU", "Documentazione dell'attivita' lavorativa quotidiana svolta in azienda", "Giustificativi di rimborsi spese e trasferte aziendali", "Estratti conto dei versamenti personali dell'amministratore nella societa'"],
        "errori": ["Prelevare somme tonde dalla cassa senza delibera ne' cedolino ne' giustificativo", "Confondere la cassa aziendale con il conto personale", "Non far emergere la compensazione con finanziamenti o spese anticipate dall'amministratore"]
    },
    {
        "cod": "SOC-119", "slug": "sequestro-preventivo-per-equivalente-bancarotta-difesa",
        "cat": "penale-societario", "cat_lbl": "Bancarotta & Reati", "pilastro": "bancarotta-reati-fallimentari-societari",
        "titolo": "Difesa contro il sequestro preventivo e per equivalente nei procedimenti di bancarotta",
        "seo_title": "Sequestro Preventivo nella Bancarotta: Limiti e Riesame in 10 Giorni",
        "desc": "Limiti rigorosi al sequestro preventivo per equivalente nella bancarotta (dove la confisca per equivalente non opera in via generale salvo ipotesi specifiche) e difesa al Riesame.",
        "keywords": ["sequestro preventivo bancarotta", "sequestro per equivalente bancarotta illegittimo", "riesame sequestro curatela"],
        "norme": ["Art. 321 c.p.p.", "Art. 240 c.p.", "Art. 322 CCII"],
        "scenario": "Il GIP dispone un sequestro preventivo (o conservativo) su immobili e conti personali dell'amministratore indagato per bancarotta fraudolenta.",
        "rischio": "Blocco immediato di tutti i beni personali e familiari dell'indagato per anni prima ancora del giudizio.",
        "protocollo": [
            "Verificare subito se e' stato disposto un sequestro 'per equivalente' (di regola non consentito per il solo reato di bancarotta pura, salvo concorso con reati tributari o riciclaggio/autoriciclaggio).",
            "Impugnare il decreto davanti al Tribunale del Riesame entro 10 giorni contestando l'assenza del periculum in mora concreto e attuale (motivazione rigorosa richiesta dalle Sezioni Unite) e il nesso di pertinenzialita' diretta.",
            "Dimostrare la provenienza lecita e anteriore dei beni sequestrati rispetto alle condotte contestate.",
            "Verificare eventuali sovrapposizioni con azioni civili o sequestri gia' ottenuti dalla curatela."
        ],
        "prove": ["Decreto di sequestro del GIP e verbali di esecuzione", "Atti di acquisto anteriori o prova di provenienza lecita dei beni personali", "Memoria tecnica sul difetto di pertinenzialita' e di periculum in mora", "Istanza di Riesame entro 10 giorni ex art. 324 c.p.p."],
        "errori": ["Lasciar decorrere i 10 giorni senza proporre Riesame", "Accettare un sequestro per equivalente su beni estranei al reato quando si contesta solo bancarotta pura", "Non contestare la mancanza di autonoma motivazione sul periculum in mora"]
    },
    {
        "cod": "SOC-120", "slug": "false-comunicazioni-sociali-non-quotate-art-2621-cc",
        "cat": "penale-societario", "cat_lbl": "Bancarotta & Reati", "pilastro": "bancarotta-reati-fallimentari-societari",
        "titolo": "False comunicazioni sociali in societa' non quotate (art. 2621 c.c.): difesa e lieve entita'",
        "seo_title": "False Comunicazioni Sociali Art. 2621 c.c.: Difesa Falso in Bilancio",
        "desc": "Difesa penale per falso in bilancio (art. 2621 c.c.): fatti materiali rilevanti, valutazioni estimative, attenuante della lieve entita' (art. 2621-bis) e particolare tenuita' (art. 2621-ter).",
        "keywords": ["false comunicazioni sociali art 2621 cc", "falso in bilancio difesa penale", "art 2621 bis lieve entita"],
        "norme": ["Art. 2621 c.c.", "Art. 2621-bis c.c.", "Art. 2621-ter c.c."],
        "scenario": "Amministratori, direttori generali o sindaci di una S.r.l. o S.p.A. non quotata sono indagati per l'esposizione di fatti materiali rilevanti non rispondenti al vero nel bilancio d'esercizio.",
        "rischio": "Reclusione da 1 a 5 anni (oltre alla responsabilita' 231 dell'ente ex art. 25-ter) e rischio di aggravamento in bancarotta impropria se sopraggiunge la liquidazione giudiziale.",
        "protocollo": [
            "Verificare la rilevanza e la concreta idoneita' decettiva delle poste contestate rispetto al complesso del bilancio tramite consulenza tecnica contabile.",
            "Sulle poste valutative (crediti, rimanenze, avviamento), dimostrare il rispetto dei criteri OIC e l'assenza di deviazione palese e fraudolenta dai criteri legali dichiarati in nota integrativa.",
            "Contestare il dolo specifico (fine di conseguire per se' o per altri un ingiusto profitto) e la consapevolezza dell'inganno.",
            "Valutare l'applicazione dell'art. 2621-bis c.c. (fatti di lieve entita' o imprese sotto soglia non fallibili, procedibili solo a querela!) e dell'art. 2621-ter c.c. (non punibilita' per particolare tenuita')."
        ],
        "prove": ["Bilanci, nota integrativa e carte di lavoro contabili", "Verifica soglie di impresa minore per l'applicabilita' della procedibilita' a querela ex art. 2621-bis co. 2 c.c.", "Perizia contabile di parte sui criteri OIC", "Assenza di danno concreto a soci e creditori"],
        "errori": ["Dimenticare che per le societa' non fallibili (sotto soglie art. 2 CCII) l'art. 2621-bis co. 2 prevede la procedibilita' solo a querela", "Confondere un errore contabile colposo con il falso in bilancio doloso", "Non valutare il riflesso sull'art. 25-ter D.Lgs. 231/2001"]
    },
    {
        "cod": "SOC-121", "slug": "false-comunicazioni-sociali-societa-quotate-art-2622-cc",
        "cat": "penale-societario", "cat_lbl": "Bancarotta & Reati", "pilastro": "bancarotta-reati-fallimentari-societari",
        "titolo": "False comunicazioni sociali di societa' quotate o emittenti strumenti finanziari (art. 2622 c.c.)",
        "seo_title": "False Comunicazioni Sociali Quotate Art. 2622 c.c.: Difesa Penale",
        "desc": "Difesa penale ad alta complessita' per emittenti quotati, dirigenti preposti alla redazione dei documenti contabili e revisori: principi IAS/IFRS, Consob e art. 25-ter D.Lgs. 231/2001.",
        "keywords": ["false comunicazioni sociali quotate art 2622", "dirigente preposto documenti contabili", "difesa penale bilancio ias ifrs"],
        "norme": ["Art. 2622 c.c.", "D.Lgs. 58/1998 (TUF)", "Art. 25-ter D.Lgs. 231/2001"],
        "scenario": "A seguito di segnalazione Consob o indagine della Procura, vengono contestate irregolarita' nei bilanci consolidati o nelle relazioni semestrali di una societa' quotata o emittente.",
        "rischio": "Reclusione da 3 a 8 anni, sanzioni amministrative Consob pesantissime e responsabilita' 231 dell'ente.",
        "protocollo": [
            "Affiancare alla difesa penale esperti di principi contabili internazionali IAS/IFRS per valutare la correttezza di impairment test, fair value e consolidamento.",
            "Verificare la concreta idoneita' delle poste contestate a indurre in errore i destinatari qualificati del mercato.",
            "Coordinare rigorosamente il procedimento penale con l'eventuale procedimento sanzionatorio Consob (anche sotto il profilo del ne bis in idem).",
            "Distinguere le posizioni di amministratori esecutivi, amministratori indipendenti, dirigente preposto e sindaci."
        ],
        "prove": ["Bilanci consolidati, relazioni finanziarie e pareri di revisori/consulenti IAS/IFRS", "Verbali del comitato controllo e rischi e del collegio sindacale", "Atti del procedimento Consob", "Perizia tecnico-contabile internazionale"],
        "errori": ["Gestire senza coordinamento la difesa davanti a Consob e alla Procura", "Trascurare la distinzione tra ruoli esecutivi e non esecutivi", "Non verificare la conformita' tecnica delle valutazioni IAS/IFRS ex ante"]
    },
    {
        "cod": "SOC-122", "slug": "impedito-controllo-soci-sindaci-art-2625-cc",
        "cat": "penale-societario", "cat_lbl": "Bancarotta & Reati", "pilastro": "bancarotta-reati-fallimentari-societari",
        "titolo": "Impedito controllo ai soci o al collegio sindacale (art. 2625 c.c.): illecito amministrativo e reato",
        "seo_title": "Impedito Controllo Art. 2625 c.c.: Tutela Soci e Difesa Amministratori",
        "desc": "Quando l'occultamento di documenti o l'ostruzionismo verso soci e sindaci integra illecito amministrativo oppure delitto procedibile a querela (art. 2625 co. 2 c.c.).",
        "keywords": ["impedito controllo art 2625 cc", "occultamento documenti ai soci reato", "querela impedito controllo"],
        "norme": ["Art. 2625 c.c.", "Art. 2476 co. 2 c.c."],
        "scenario": "Gli amministratori occultano documenti o ostacolano con artifici le attivita' di controllo legalmente attribuite ai soci (es. art. 2476 co. 2 c.c.) o al collegio sindacale.",
        "rischio": "Sanzione amministrativa pecuniaria (fino a 10.329 euro) e, se la condotta ha cagionato un danno ai soci, reclusione fino a 1 anno (a querela della persona offesa).",
        "protocollo": [
            "Per chi difende l'amministratore: dimostrare che non vi e' stato occultamento doloso ma semplice ritardo tecnico, richiesta generica/abusiva o tutela di segreti industriali contro un socio concorrente, e rimediare subito mettendo a disposizione i documenti.",
            "Per chi assiste il socio o il sindaco: documentare via PEC le richieste circostanziate, i rifiuti reiterati e il danno economico concreto subito.",
            "Verificare il termine di 3 mesi per la querela nell'ipotesi delittuosa dell'art. 2625 co. 2 c.c.",
            "Coordinare l'azione penale con il ricorso civile d'urgenza ex art. 700 c.p.c. per ottenere materialmente i documenti."
        ],
        "prove": ["PEC di richiesta documenti e risposte o silenzi dell'amministratore", "Prova di eventuali artifici o occultamenti documentali", "Quantificazione del danno cagionato al socio ai fini del co. 2", "Verbali di ispezione o accesso in sede"],
        "errori": ["Ostruire deliberatamente l'accesso ai documenti al socio di S.r.l. che ne ha pieno diritto per legge", "Sporgere querela ex art. 2625 co. 2 senza provare il danno concreto subito dal socio", "Non attivare in parallelo il rimedio civile d'urgenza"]
    },
    {
        "cod": "SOC-123", "slug": "indebita-restituzione-conferimenti-ripartizione-utili-artt-2626-2627",
        "cat": "penale-societario", "cat_lbl": "Bancarotta & Reati", "pilastro": "bancarotta-reati-fallimentari-societari",
        "titolo": "Indebita restituzione dei conferimenti e illegale ripartizione di utili o riserve (artt. 2626-2627 c.c.)",
        "seo_title": "Indebita Restituzione Conferimenti e Utili Fittizi Artt. 2626-2627 c.c.",
        "desc": "Difesa penale degli amministratori per operazioni che intaccano il capitale sociale o distribuiscono utili non conseguiti, e causa estintiva della restituzione prima del bilancio.",
        "keywords": ["indebita restituzione conferimenti art 2626", "illegale ripartizione utili art 2627", "tutela penale capitale sociale"],
        "norme": ["Art. 2626 c.c.", "Art. 2627 c.c.", "Art. 2629 c.c."],
        "scenario": "Viene contestato agli amministratori di aver restituito conferimenti ai soci (anche in forma simulata) o distribuito utili fittizi e riserve indisponibili erodendo il capitale sociale.",
        "rischio": "Reclusione fino a 1 anno (art. 2626) o arresto fino a 1 anno (art. 2627), responsabilita' 231 ex art. 25-ter e rischio bancarotta impropria in caso di dissesto.",
        "protocollo": [
            "Verificare immediatamente se e' ancora possibile attivare la causa di estinzione del reato prevista dall'art. 2627 co. 2 c.c. (restituzione degli utili o ricostituzione delle riserve prima del termine previsto per l'approvazione del bilancio).",
            "Dimostrare con perizia contabile che le riserve distribuite erano effettivamente disponibili e che l'utile era reale secondo i principi OIC.",
            "Verificare la sussistenza del dolo (escludendo errori materiali di riclassificazione delle riserve).",
            "In sede preventiva, sottoporre sempre a verifica legale-contabile ogni operazione su capitale, riserve e riduzione."
        ],
        "prove": ["Bilanci, prospetto analitico della disponibilita' delle riserve e delibere assembleari", "Prova dell'eventuale ricostituzione delle riserve nei termini di estinzione ex art. 2627 co. 2", "Perizia contabile sulla reale sussistenza di utili distribuibili", "Tracciabilita' dei movimenti verso i soci"],
        "errori": ["Distribuire acconti su dividendi in S.r.l. dove non sono ammessi o in assenza di riserve disponibili", "Non sfruttare la causa di estinzione della ricostituzione tempestiva prima dell'approvazione del bilancio", "Mascherare restituzioni di capitale con operazioni simulate prive di sostanza economica"]
    },
    {
        "cod": "SOC-124", "slug": "infedelta-patrimoniale-amministratori-art-2634-cc",
        "cat": "penale-societario", "cat_lbl": "Bancarotta & Reati", "pilastro": "bancarotta-reati-fallimentari-societari",
        "titolo": "Infedelta' patrimoniale degli amministratori e direttori generali (art. 2634 c.c.)",
        "seo_title": "Infedelta' Patrimoniale Art. 2634 c.c.: Querela, Conflitto e Difesa",
        "desc": "Presupposti del reato di infedelta' patrimoniale (conflitto di interessi, danno intenzionale, ingiusto profitto, querela entro 3 mesi) e scriminante dei vantaggi compensativi.",
        "keywords": ["infedelta patrimoniale art 2634 cc", "conflitto interessi penale amministratore", "querela infedelta patrimoniale"],
        "norme": ["Art. 2634 c.c.", "Art. 124 c.p."],
        "scenario": "Un amministratore compie atti di disposizione dei beni sociali (es. svendita di asset, contratti gonfiati con societa' proprie) in conflitto di interessi cagionando intenzionalmente un danno patrimoniale alla societa'.",
        "rischio": "Reclusione da 6 mesi a 3 anni (procedibile a querela della persona offesa), oltre a risarcimento civile e revoca dalla carica.",
        "protocollo": [
            "Per la difesa dell'amministratore: contestare il dolo intenzionale del danno alla societa', dimostrare la congruita' economica dell'atto tramite perizia e invocare i vantaggi compensativi di gruppo (art. 2634 co. 3 c.c.) o la tardivita' della querela (oltre 3 mesi).",
            "Per la tutela della societa' o del socio leso: verificare la legittimazione alla querela entro 3 mesi dalla conoscenza piena del fatto e documentare sia il conflitto di interessi sia il danno patrimoniale certo.",
            "Coordinare l'azione penale con l'azione civile di annullamento del contratto (art. 2475-ter c.c.) e risarcimento danni.",
            "Valutare il risarcimento integrale per remissione di querela."
        ],
        "prove": ["Contratti e visure che dimostrano o escludono il conflitto di interessi", "Perizia di valutazione economica dell'operazione rispetto ai valori di mercato", "Data certa di conoscenza del fatto ai fini della tempestivita' della querela (3 mesi)", "Delibere sociali e vantaggi compensativi"],
        "errori": ["Confondere una cattiva scelta imprenditoriale (coperta dalla business judgment rule) con l'infedelta' patrimoniale", "Depositare querela oltre il termine perentorio di 3 mesi", "Omettere la prova del danno patrimoniale effettivo per la societa'"]
    },
    {
        "cod": "SOC-125", "slug": "corruzione-tra-privati-art-2635-cc-difesa-impresa",
        "cat": "penale-societario", "cat_lbl": "Bancarotta & Reati", "pilastro": "bancarotta-reati-fallimentari-societari",
        "titolo": "Corruzione tra privati (art. 2635 c.c.) e istigazione alla corruzione tra privati (art. 2635-bis)",
        "seo_title": "Corruzione tra Privati Art. 2635 c.c.: Difesa Manager e 231",
        "desc": "Difesa penale per dirigenti, responsabili acquisti e societa' (art. 25-ter D.Lgs. 231/2001) accusati di dazione o promessa di denaro/utilita' in violazione di obblighi d'ufficio o fedelta'.",
        "keywords": ["corruzione tra privati art 2635 cc", "istigazione corruzione privati art 2635 bis", "procedibilita ufficio corruzione privati"],
        "norme": ["Art. 2635 c.c.", "Art. 2635-bis c.c.", "Art. 25-ter co. 1 lett. s-bis D.Lgs. 231/2001"],
        "scenario": "Un direttore acquisti o commerciale viene accusato di aver ricevuto (o promesso a un dirigente di altra impresa) provvigioni occulte o utilita' per far aggiudicare contratti privati.",
        "rischio": "Reclusione da 1 a 3 anni (procedibile d'ufficio dal 2019), sanzioni pecuniarie e interdittive 231 per la societa' corruttiva e licenziamento per giusta causa.",
        "protocollo": [
            "Verificare se vi e' stata effettiva violazione degli obblighi inerenti all'ufficio o degli obblighi di fedelta' (elemento costitutivo necessario).",
            "Dimostrare che la fornitura o la consulenza contestata era reale, documentata e a prezzi di mercato.",
            "Per la societa' del corruttore, verificare subito l'idoneita' del Modello 231 su ciclo attivo/passivo, gare private, omaggi e provvigioni per invocare l'elusione fraudolenta.",
            "Per la societa' danneggiata dal proprio dirigente infedele, costituirsi parte civile e agire per il risarcimento."
        ],
        "prove": ["Contratti di fornitura/agenzia e comparazione con offerte concorrenti", "Procedure 231 su acquisti, vendite, omaggi e qualificazione fornitori", "Documentazione dei pagamenti e dell'effettivita' delle prestazioni", "Prove dell'eventuale elusione fraudolenta dei controlli aziendali"],
        "errori": ["Credere che la corruzione tra privati sia ancora procedibile solo a querela (e' procedibile d'ufficio dalla L. 3/2019)", "Tollerare retrocessioni o regali di valore elevato nella forza vendite", "Non prevedere una segregazione tra chi seleziona il fornitore e chi approva il pagamento"]
    },

    # ═══════════════════ 7. AMMINISTRATORI, SINDACI & M&A (126-140) ═══════════════════
    {
        "cod": "SOC-126", "slug": "azione-responsabilita-curatore-art-255-ccii-difesa-amministratori",
        "cat": "amministratori-ma", "cat_lbl": "Amministratori & M&A", "pilastro": "responsabilita-amministratori-sindaci-azioni",
        "titolo": "Difesa degli amministratori dall'azione di responsabilita' del curatore (art. 255 CCII)",
        "seo_title": "Azione di Responsabilita' del Curatore Art. 255 CCII: Difesa",
        "desc": "Come difendere il patrimonio personale di amministratori e liquidatori citati dal curatore davanti al Tribunale delle Imprese: prescrizione, nesso causale e business judgment rule.",
        "keywords": ["azione responsabilita curatore art 255 ccii", "difesa amministratori tribunale imprese", "prescrizione azione responsabilita curatore"],
        "norme": ["Art. 255 CCII", "Artt. 2393-2394 c.c.", "Art. 2476 c.c."],
        "scenario": "Il curatore della liquidazione giudiziale notifica atto di citazione (o ricorso per sequestro conservativo) chiedendo agli ex amministratori il risarcimento di milioni di euro.",
        "rischio": "Aggressione diretta di casa, conti correnti, quote societarie e pensione/stipendio dell'amministratore.",
        "protocollo": [
            "Verificare subito la prescrizione quinquennale (sia per l'azione sociale dalla cessazione della carica, sia per l'azione dei creditori dal momento di oggettiva manifesta insufficienza patrimoniale, spesso anteriore alla sentenza).",
            "Contestare l'insindacabilita' nel merito delle scelte gestorie ragionevoli ex ante (business judgment rule) e l'assenza di nesso causale tra condotta e singolo danno.",
            "Attivare immediatamente eventuali polizze assicurative D&O rispettando i termini contrattuali di denuncia sinistro (clausole claims-made).",
            "Smontare con CTU/CTP contabile i criteri presuntivi di calcolo del danno (art. 2486 co. 3 c.c.) e valutare una transazione tombale sostenibile."
        ],
        "prove": ["Bilanci storici per provare l'anteriorita' dell'insufficienza patrimoniale (prescrizione)", "Verbali CdA, deleghe e studi di fattibilita' ex ante (business judgment rule)", "Polizza assicurativa D&O e PEC di denuncia sinistro", "Perizia contabile di parte sul danno effettivo"],
        "errori": ["Non denunciare subito il sinistro alla compagnia D&O perdendo la copertura", "Non eccepire la prescrizione dell'azione dei creditori quando il deficit era noto nei bilanci da oltre 5 anni", "Sottovalutare il rischio di sequestro conservativo ante causam"]
    },
    {
        "cod": "SOC-127", "slug": "quantificazione-danno-netti-patrimoniali-deficit-art-2486-co-3",
        "cat": "amministratori-ma", "cat_lbl": "Amministratori & M&A", "pilastro": "responsabilita-amministratori-sindaci-azioni",
        "titolo": "Contestare il calcolo del danno da netti patrimoniali e deficit fallimentare (art. 2486 co. 3 c.c.)",
        "seo_title": "Calcolo Danno Netti Patrimoniali Art. 2486 co. 3 c.c.: Difesa CTP",
        "desc": "Come ribaltare la presunzione di danno dell'art. 2486 co. 3 c.c. (differenza dei netti patrimoniali o deficit concorsuale) tramite prova del minor danno effettivo e rettifiche contabili.",
        "keywords": ["art 2486 comma 3 netti patrimoniali", "criterio deficit concorsuale danno amministratori", "difesa quantificazione danno curatore"],
        "norme": ["Art. 2486 co. 3 c.c.", "Art. 1223 c.c."],
        "scenario": "Il curatore quantifica il danno richiesto agli amministratori applicando meccanicamente la differenza tra il patrimonio netto alla data della perdita del capitale e quello alla data della liquidazione giudiziale (o addirittura l'intero deficit).",
        "rischio": "Addebito all'amministratore di perdite che si sarebbero comunque verificate anche in caso di liquidazione tempestiva (costi fissi, svalutazioni liquidatorie, crisi esogene).",
        "protocollo": [
            "Ricordare che il criterio dei netti patrimoniali dell'art. 2486 co. 3 c.c. e' una presunzione relativa: la difesa puo' e deve fornire la prova di un diverso e minore ammontare del danno effettivo.",
            "Far eseguire da un CTP contabile la rettifica omogenea dei due patrimoni netti (entrambi vanno valutati con criteri omogenei di liquidazione, non uno in continuita' e l'altro in liquidazione!).",
            "Detrarre tassativamente i costi che la societa' avrebbe comunque sostenuto durante una normale liquidazione (stipendi in preavviso, TFR, affitti, oneri di dismissione) come prevede la lettera stessa dell'art. 2486 co. 3.",
            "Contestare il ricorso al criterio del deficit (differenza attivo/passivo) quando le scritture contabili sono comunque disponibili e ricostruibili."
        ],
        "prove": ["Bilanci riclassificati con criteri omogenei di liquidazione dal CTP", "Prospetto analitico dei costi fissi inevitabili in scenario liquidatorio", "Scritture contabili che impediscono l'uso del criterio del deficit", "Documentazione delle perdite derivanti da eventi esterni non imputabili"],
        "errori": ["Accettare il confronto disomogeneo tra un patrimonio netto in continuita' e uno in liquidazione", "Non dedurre i costi inevitabili di una liquidazione ordinata", "Non nominare un consulente tecnico contabile di parte prima della CTU"]
    },
    {
        "cod": "SOC-128", "slug": "sequestro-conservativo-beni-personali-amministratore-difesa",
        "cat": "amministratori-ma", "cat_lbl": "Amministratori & M&A", "pilastro": "responsabilita-amministratori-sindaci-azioni",
        "titolo": "Difesa urgente contro il sequestro conservativo sui beni personali dell'amministratore",
        "seo_title": "Sequestro Conservativo Beni Amministratore Art. 671 c.p.c.: Difesa",
        "desc": "Come opporsi in udienza cautelare e in sede di reclamo al sequestro conservativo chiesto dal curatore o dai soci su immobili, conti e quote dell'amministratore.",
        "keywords": ["sequestro conservativo amministratore", "difesa periculum in mora art 671 cpc", "reclamo sequestro conservativo tribunale imprese"],
        "norme": ["Art. 671 c.p.c.", "Art. 669-terdecies c.p.c.", "Art. 255 CCII"],
        "scenario": "Prima o durante la causa di responsabilita', il curatore o un socio chiede il sequestro conservativo sui beni immobili e sui conti personali dell'amministratore fino a concorrenza di somme ingenti.",
        "rischio": "Blocco totale del patrimonio personale e familiare per tutta la durata pluriennale della causa di merito.",
        "protocollo": [
            "Contestare sia il fumus boni iuris (infondatezza o prescrizione dell'azione, errato calcolo art. 2486) sia il periculum in mora (assenza di atti di spoliazione o depauperamento del patrimonio personale).",
            "Dimostrare la stabilita' del patrimonio, la presenza di polizza D&O capiente e l'assenza di condotte elusive.",
            "Chiedere in via subordinata la forte riduzione del quantum sequestrabile (spesso gonfiato dal ricorrente) o la revoca previa prestazione di idonea cauzione (art. 684 c.p.c.).",
            "In caso di accoglimento, proporre reclamo al collegio entro il termine perentorio di 15 giorni ex art. 669-terdecies c.p.c."
        ],
        "prove": ["Ricorso cautelare e decreto di fissazione udienza", "Visure immobiliari che dimostrano l'assenza di atti dispositivi in frode", "Polizza assicurativa D&O con massimale capiente", "Perizia contabile di ridimensionamento del fumus e del quantum"],
        "errori": ["Compiere donazioni o atti di vendita di immobili personali dopo la crisi (creano subito il periculum in mora e rischiano revocatoria)", "Non proporre reclamo entro 15 giorni dall'ordinanza cautelare", "Non eccepire la copertura assicurativa D&O esistente"]
    },
    {
        "cod": "SOC-129", "slug": "azione-sociale-responsabilita-soci-art-2393-2476-cc",
        "cat": "amministratori-ma", "cat_lbl": "Amministratori & M&A", "pilastro": "responsabilita-amministratori-sindaci-azioni",
        "titolo": "Azione sociale di responsabilita' promossa dalla societa' o dal singolo socio (artt. 2393 e 2476 c.c.)",
        "seo_title": "Azione Sociale di Responsabilita' Art. 2393 e 2476 c.c.",
        "desc": "Come promuovere (o resistere a) l'azione risarcitoria contro l'amministratore in bonis: delibera assembleare in S.p.A., legittimazione del singolo socio in S.r.l. e rinuncia/transazione.",
        "keywords": ["azione sociale responsabilita art 2393", "azione socio srl art 2476 comma 3", "transazione azione responsabilita"],
        "norme": ["Art. 2393 c.c.", "Art. 2393-bis c.c.", "Art. 2476 co. 3-5 c.c."],
        "scenario": "A seguito di cambio di controllo o di gravi errori gestori, la societa' (o un singolo socio di S.r.l. anche con l'1% del capitale) agisce contro l'amministratore per ottenere il risarcimento a favore della societa'.",
        "rischio": "La delibera in S.p.A. con il voto di almeno 1/5 del capitale comporta la revoca automatica dell'amministratore; nella S.r.l. anche il socio di minoranza puo' agire in autonomia.",
        "protocollo": [
            "Verificare i requisiti di legittimazione: delibera assembleare (anche in occasione della discussione del bilancio ex art. 2393 co. 2) o minoranza qualificata (art. 2393-bis) nelle S.p.A.; legittimazione individuale di ciascun socio nelle S.r.l. (art. 2476 co. 3).",
            "Articolare puntualmente gli specifici inadempimenti ai doveri di legge o statuto, il danno certo subito dal patrimonio sociale e il nesso di causalita'.",
            "In caso di difesa, far valere l'eventuale manleva o transazione regolarmente deliberata dall'assemblea (rispettando il veto delle minoranze ex artt. 2393 co. 6 e 2476 co. 5).",
            "Gestire il regime del rimborso spese legali del socio vittorioso a carico della societa' ex art. 2476 co. 4 c.c."
        ],
        "prove": ["Delibera assembleare di promozione dell'azione (o visura socio S.r.l.)", "Documentazione contabile degli inadempimenti e perizia del danno", "Eventuali delibere di rinuncia o transazione e relativi quorum", "Polizza D&O"],
        "errori": ["Deliberare la rinuncia all'azione senza rispettare il quorum di opposizione della minoranza (1/5 in S.p.A., 1/10 in S.r.l.)", "Confondere il danno subito dalla societa' con il danno diretto al singolo socio", "Omettere la chiamata della societa' come litisconsorte necessario nell'azione del socio di S.r.l."]
    },
    {
        "cod": "SOC-130", "slug": "azione-diretta-socio-terzo-danneggiato-art-2395-cc",
        "cat": "amministratori-ma", "cat_lbl": "Amministratori & M&A", "pilastro": "responsabilita-amministratori-sindaci-azioni",
        "titolo": "Azione individuale di responsabilita' del socio o del terzo danneggiato direttamente (art. 2395 c.c.)",
        "seo_title": "Azione Individuale Socio o Terzo Art. 2395 c.c.: Danno Diretto",
        "desc": "Quando un fornitore, una banca o un socio puo' chiedere personalmente i danni all'amministratore ex art. 2395 c.c. (danno diretto vs danno riflesso) e come difendersi.",
        "keywords": ["azione individuale art 2395 cc", "danno diretto vs danno riflesso socio", "responsabilita amministratore verso terzi"],
        "norme": ["Art. 2395 c.c.", "Art. 2476 co. 7 c.c."],
        "scenario": "Un terzo (es. acquirente di quote indotto in errore da un bilancio falso, o fornitore raggirato con false assicurazioni) cita personalmente l'amministratore per il risarcimento del danno.",
        "rischio": "Questa azione spetta individualmente al singolo danneggiato (non e' assorbita dal curatore in liquidazione giudiziale) ed e' soggetta a prescrizione quinquennale dal compimento dell'atto.",
        "protocollo": [
            "Distinguere nettamente il 'danno diretto' al patrimonio del socio/terzo (risarcibile ex art. 2395, es. acquisto di quote a prezzo gonfiato da bilanci falsi) dal 'danno riflesso' (mero deprezzamento della quota o mancato pagamento di un debito sociale, non risarcibile ex art. 2395).",
            "Provare (o contestare) l'illecito doloso o colposo specifico dell'amministratore e il nesso causale immediato con la decisione economica del danneggiato.",
            "Verificare il termine di prescrizione di 5 anni dal compimento dell'atto pregiudizievole.",
            "Radicare la causa davanti alla Sezione Specializzata in materia di Impresa competente."
        ],
        "prove": ["Documenti o bilanci falsi consegnati direttamente al terzo/socio", "Prova del nesso causale tra l'inganno e l'esborso economico del danneggiato", "Data esatta del compimento dell'atto ai fini della prescrizione quinquennale", "Quantificazione del danno diretto"],
        "errori": ["Usare l'art. 2395 c.c. per chiedere il semplice pagamento di fatture insolute della societa' (viene rigettato perche' danno riflesso)", "Ignorare che l'azione ex art. 2395 resta proponibile anche dopo la liquidazione giudiziale della societa'", "Sbagliare la competenza territoriale del Tribunale delle Imprese"]
    },
    {
        "cod": "SOC-131", "slug": "responsabilita-amministratore-non-esecutivo-senza-deleghe-art-2381",
        "cat": "amministratori-ma", "cat_lbl": "Amministratori & M&A", "pilastro": "responsabilita-amministratori-sindaci-azioni",
        "titolo": "Difesa dell'amministratore senza deleghe (non esecutivo) ex artt. 2381 e 2392 c.c.",
        "seo_title": "Responsabilita' Amministratore Senza Deleghe Art. 2381 c.c.: Difesa",
        "desc": "Come difendere i consiglieri non esecutivi dalle azioni di responsabilita' solidale: dovere di agire informati, segnali d'allarme e annotazione del dissenso ex art. 2392 co. 3 c.c.",
        "keywords": ["amministratore senza deleghe art 2381", "responsabilita consigliere non esecutivo", "dissenso amministratore art 2392"],
        "norme": ["Art. 2381 c.c.", "Art. 2392 c.c."],
        "scenario": "Un consigliere di amministrazione privo di deleghe operative viene convenuto in solido con l'amministratore delegato per operazioni irregolari compiute da quest'ultimo.",
        "rischio": "Estensione automatica di responsabilita' solidali milionarie a consiglieri che non avevano alcun potere di firma ne' gestione quotidiana.",
        "protocollo": [
            "Richiamare la riforma degli artt. 2381 e 2392 c.c.: non esiste piu' un obbligo generale e indiscriminato di vigilanza sull'andamento quotidiano della gestione delegata.",
            "Dimostrare che il consigliere ha agito in modo informato valutando le relazioni periodiche fornite dagli organi delegati e che non erano emersi segnali di allarme anomali e percepibili.",
            "Se vi erano scelte contestate, produrre i verbali di CdA con il dissenso formalmente annotato e comunicato per iscritto al presidente del collegio sindacale (esimente art. 2392 co. 3 c.c.).",
            "Verificare le specifiche deleghe iscritte nel Registro delle Imprese per perimetrare la responsabilita'."
        ],
        "prove": ["Delibera di attribuzione deleghe e visura storica", "Verbali di CdA con richieste di informazioni e relazioni ricevute dall'AD", "Eventuale annotazione di dissenso e PEC al presidente del collegio sindacale ex art. 2392 co. 3", "Dimostrazione dell'occultamento delle irregolarita' da parte dell'AD"],
        "errori": ["Restare passivi in CdA senza mai chiedere informazioni scritte quando emergono perdite o ritardi", "Limitarsi a votare contro senza far annotare il dissenso nel libro CdA ne' avvisare il collegio sindacale", "Rassegnare dimissioni tardive senza motivarle a verbale"]
    },
    {
        "cod": "SOC-132", "slug": "responsabilita-collegio-sindacale-riforma-legge-35-2025-art-2407",
        "cat": "amministratori-ma", "cat_lbl": "Amministratori & M&A", "pilastro": "responsabilita-amministratori-sindaci-azioni",
        "titolo": "Responsabilita' del Collegio Sindacale e nuovi limiti quantitativi della Legge 35/2025 (art. 2407 c.c.)",
        "seo_title": "Responsabilita' Sindaci Art. 2407 c.c. e Legge 35/2025: Tetto 15x/12x/10x",
        "desc": "Applicazione della riforma dell'art. 2407 c.c. (L. 14 marzo 2025, n. 35): tetto risarcitorio a multipli del compenso (15x, 12x, 10x), prescrizione 5 anni dalla relazione art. 2429 e profili intertemporali.",
        "keywords": ["riforma art 2407 cc legge 35 2025", "tetto responsabilita sindaci multiplo compenso", "prescrizione azione sindaci 5 anni"],
        "norme": ["Art. 2407 c.c. (mod. L. 35/2025)", "Art. 2429 c.c.", "Art. 25-octies CCII"],
        "scenario": "I componenti del collegio sindacale (o il sindaco unico) sono citati in giudizio dal curatore o dai soci per omessa vigilanza (culpa in vigilando) sulle condotte degli amministratori.",
        "rischio": "Prima della riforma i sindaci rispondevano in solido e senza limiti dell'intero dissesto; oggi la difesa deve applicare con rigore i nuovi limiti e verificare i profili temporali.",
        "protocollo": [
            "Invocare per i fatti successivi all'entrata in vigore della L. 35/2025 (12 aprile 2025), in assenza di dolo, il tetto risarcitorio inderogabile: 15 volte il compenso annuo fino a 10.000 euro, 12 volte tra 10.000 e 50.000 euro, 10 volte oltre 50.000 euro (anche se il collegio svolge la revisione legale).",
            "Eccepire la prescrizione di 5 anni decorrenti dal deposito della relazione ex art. 2429 c.c. concernente l'esercizio in cui si e' verificato il danno (nuovo art. 2407 co. 4 c.c.).",
            "Per i fatti anteriori al 12 aprile 2025 (dove la giurisprudenza esclude la retroattivita' del tetto), difendersi su assenza di nesso causale, tempestiva attivazione dei poteri di controllo (segnalazioni art. 25-octies CCII, verbali trimestrali) e polizza RC professionale.",
            "Valutare il concorso di colpa e la graduazione interna rispetto agli amministratori."
        ],
        "prove": ["Delibera di determinazione del compenso annuo dei sindaci", "Relazioni ex art. 2429 c.c. con data di deposito al Registro Imprese", "Verbali di verifica trimestrale del collegio e segnalazioni PEC al CdA (art. 25-octies CCII)", "Polizza assicurativa RC professionale sindaci"],
        "errori": ["Dare per scontata l'applicazione retroattiva del tetto L. 35/2025 ai giudizi pendenti su fatti anteriori al 2025 senza preparare le difese di merito", "Non conservare i verbali di segnalazione tempestiva al CdA", "Trascurare la nuova decorrenza certa della prescrizione quinquennale"]
    },
    {
        "cod": "SOC-133", "slug": "responsabilita-revisore-legale-conti-art-15-dlgs-39-2010",
        "cat": "amministratori-ma", "cat_lbl": "Amministratori & M&A", "pilastro": "responsabilita-amministratori-sindaci-azioni",
        "titolo": "Responsabilita' del revisore legale e della societa' di revisione (art. 15 D.Lgs. 39/2010)",
        "seo_title": "Responsabilita' Revisore Legale Art. 15 D.Lgs. 39/2010: Difesa",
        "desc": "Difesa del revisore legale dei conti citato in giudizio da societa', curatore o terzi: responsabilita' nei limiti del contributo effettivo al danno, principi ISA Italia e prescrizione 5 anni.",
        "keywords": ["responsabilita revisore legale art 15 dlgs 39 2010", "principi isa italia difesa revisore", "prescrizione 5 anni relazione revisione"],
        "norme": ["Art. 15 D.Lgs. 39/2010", "Art. 25-octies CCII (mod. D.Lgs. 136/2024)"],
        "scenario": "Un revisore legale o una societa' di revisione viene convenuto in solido con gli amministratori per aver rilasciato un giudizio positivo su bilanci poi rivelatisi inattendibili.",
        "rischio": "Richieste risarcitorie elevate da parte di curatori, banche o acquirenti di partecipazioni che hanno fatto affidamento sul bilancio certificato.",
        "protocollo": [
            "Eccepire la prescrizione quinquennale che decorre dalla data della relazione di revisione sul bilancio (art. 15 co. 3 D.Lgs. 39/2010).",
            "Far valere il principio legale per cui nei rapporti interni e nella graduazione il revisore risponde solo nei limiti del proprio contributo effettivo al danno cagionato.",
            "Dimostrare attraverso le carte di lavoro (working papers) la piena conformita' delle verifiche ai principi di revisione ISA Italia e l'eventuale frode collusiva degli amministratori non rilevabile con diligenza professionale.",
            "Verificare le nuove regole sulla segnalazione della crisi da parte del revisore introdotte dal Correttivo-ter D.Lgs. 136/2024 (art. 25-octies CCII)."
        ],
        "prove": ["Carte di lavoro (working papers) e piano di revisione ISA Italia", "Lettere di attestazione (management representation letters) firmate dagli amministratori", "Relazioni di revisione con data di emissione", "Polizza RC professionale"],
        "errori": ["Non documentare analiticamente i campionamenti e le verifiche nelle carte di lavoro", "Omettere le lettere di attestazione firmate dalla direzione", "Ignorare l'estensione al revisore dell'obbligo di segnalazione tempestiva ex art. 25-octies CCII"]
    },
    {
        "cod": "SOC-134", "slug": "responsabilita-liquidatore-societa-cancellata-art-2495-cc",
        "cat": "amministratori-ma", "cat_lbl": "Amministratori & M&A", "pilastro": "responsabilita-amministratori-sindaci-azioni",
        "titolo": "Responsabilita' del liquidatore e dei soci dopo la cancellazione della societa' (art. 2495 c.c. e art. 36 DPR 602/73)",
        "seo_title": "Responsabilita' Liquidatore e Soci Societa' Cancellata Art. 2495 c.c.",
        "desc": "Difesa di liquidatori e soci chiamati a rispondere di debiti civili e fiscali dopo la chiusura della liquidazione e la cancellazione dal Registro delle Imprese.",
        "keywords": ["responsabilita liquidatore art 2495 cc", "art 36 dpr 602 1973 debiti fiscali liquidatore", "societa cancellata debiti soci"],
        "norme": ["Art. 2495 c.c.", "Art. 36 DPR 602/1973", "Art. 28 co. 4 D.Lgs. 175/2014"],
        "scenario": "Dopo la cancellazione della S.r.l., creditori rimasti insoddisfatti o l'Agenzia delle Entrate agiscono personalmente contro il liquidatore e i soci per recuperare i crediti residui.",
        "rischio": "I soci rispondono nei limiti di quanto riscosso in base al bilancio finale di liquidazione, mentre il liquidatore risponde personalmente se ha violato l'ordine dei privilegi pagando creditori inferiori o soci prima del Fisco.",
        "protocollo": [
            "Per i soci: verificare che non vi sia stata alcuna distribuzione di attivo nel bilancio finale di liquidazione (in tal caso non rispondono dei debiti sociali, salvo prova contraria di assegnazioni di fatto).",
            "Per il liquidatore: dimostrare che la liquidazione si e' chiusa senza attivo distribuibile oppure rispettando rigorosamente l'ordine delle cause legittime di prelazione.",
            "Sul fronte fiscale (art. 36 DPR 602/1973), contestare atti impositivi privi di autonomo avviso motivato sul presupposto specifico della responsabilita' del liquidatore.",
            "Verificare il termine annuale dalla cancellazione entro cui e' ancora ammissibile la liquidazione giudiziale (art. 33 CCII)."
        ],
        "prove": ["Bilancio finale di liquidazione e piano di riparto depositati", "Estratti conto della fase di liquidazione che provano l'assenza di attivo o il rispetto dei privilegi", "Avvisi motivati ex art. 36 DPR 602/1973", "Visura storica con data esatta di cancellazione"],
        "errori": ["Pagare creditori chirografari o distribuire beni ai soci lasciando scoperti debiti privilegiati o fiscali", "Cancellare la societa' con contenziosi aperti senza accantonamenti ne' trasparenza", "Non impugnare nei 60 giorni l'avviso di accertamento notificato al liquidatore ex art. 36"]
    },
    {
        "cod": "SOC-135", "slug": "responsabilita-cessionario-debiti-aziendali-art-2560-cc",
        "cat": "amministratori-ma", "cat_lbl": "Amministratori & M&A", "pilastro": "ma-cessione-azienda-fusioni-scissioni",
        "titolo": "Cessione d'azienda e responsabilita' dell'acquirente per i debiti pregressi (art. 2560 c.c.)",
        "seo_title": "Cessione d'Azienda e Debiti Pregressi Art. 2560 c.c.: Tutela Acquirente",
        "desc": "Quando l'acquirente dell'azienda risponde solidalmente dei debiti del venditore risultanti dai libri contabili obbligatori e come proteggersi contrattualmente in sede di M&A.",
        "keywords": ["cessione azienda debiti art 2560 cc", "libri contabili obbligatori cessione azienda", "manleva debiti acquisto azienda"],
        "norme": ["Art. 2560 c.c.", "Art. 2558 c.c.", "Art. 2559 c.c."],
        "scenario": "Dopo aver comprato un'azienda o un ramo d'azienda, l'acquirente riceve richieste di pagamento e decreti ingiuntivi da vecchi fornitori del venditore che invocano l'art. 2560 co. 2 c.c.",
        "rischio": "La responsabilita' solidale dell'acquirente per i debiti risultanti dalle scritture contabili obbligatorie e' inderogabile verso i terzi (gli accordi tra venditore e compratore valgono solo nei rapporti interni).",
        "protocollo": [
            "In sede di difesa dell'acquirente: verificare rigorosamente che il debito risulti effettivamente dai libri contabili obbligatori (libro giornale, libro inventari) regolarmente tenuti al momento del trasferimento (condizione costitutiva dell'art. 2560 co. 2).",
            "In sede di acquisto (preventiva): eseguire due diligence contabile completa, inserire robuste clausole di manleva, trattenere parte del prezzo in deposito escrow o chiedere fideiussione bancaria al venditore.",
            "Se l'azienda e' in crisi, valutare l'acquisto protetto in deroga all'art. 2560 co. 2 c.c. tramite Composizione Negoziata (art. 22 CCII) o procedura concorsuale.",
            "Attivare subito la rivalsa contrattuale contro il cedente per ogni somma eventualmente pagata ai terzi."
        ],
        "prove": ["Atto notarile di cessione d'azienda con clausole di manleva ed escrow", "Libri contabili obbligatori del cedente alla data del rogito", "Situazione debitoria allegata al contratto", "PEC di contestazione e chiamata in manleva del venditore"],
        "errori": ["Pensare che la clausola 'i debiti restano a carico del venditore' impedisca ai creditori di aggredire l'acquirente", "Comprare l'azienda senza controllare il libro giornale del cedente", "Pagare tutto il prezzo al rogito senza trattenere garanzie per passivita' latenti"]
    },
    {
        "cod": "SOC-136", "slug": "certificato-carichi-pendenti-fiscali-cessione-azienda-art-14",
        "cat": "amministratori-ma", "cat_lbl": "Amministratori & M&A", "pilastro": "ma-cessione-azienda-fusioni-scissioni",
        "titolo": "Cessione d'azienda e debiti fiscali: il certificato liberatorio ex art. 14 D.Lgs. 472/1997",
        "seo_title": "Certificato Carichi Pendenti Fiscali Cessione Azienda Art. 14 D.Lgs. 472/97",
        "desc": "Come blindare l'acquisto di un'azienda dai debiti tributari del venditore chiedendo il certificato all'Agenzia delle Entrate prima del rogito (effetto liberatorio in 40 giorni).",
        "keywords": ["certificato carichi pendenti cessione azienda", "art 14 dlgs 472 1997", "responsabilita solidale debiti fiscali acquirente"],
        "norme": ["Art. 14 D.Lgs. 472/1997", "Art. 2560 c.c."],
        "scenario": "Un imprenditore acquista un'azienda senza aver richiesto il certificato dei carichi pendenti fiscali (oppure sta per firmare il rogito) e rischia la responsabilita' solidale per imposte e sanzioni del venditore.",
        "rischio": "Senza certificato negativo, l'acquirente risponde solidalmente (nei limiti del valore dell'azienda) delle imposte e sanzioni relative all'anno della cessione e ai due precedenti, anche se non risultavano dalle scritture contabili.",
        "protocollo": [
            "Richiedere OBBLIGATORIAMENTE prima del rogito il certificato dei carichi pendenti risultanti al sistema informativo dell'Anagrafe Tributaria (art. 14 co. 3 D.Lgs. 472/1997) con il consenso del cedente.",
            "Attendere il rilascio negativo oppure il decorso dei 40 giorni dalla richiesta (silenzio con pieno effetto liberatorio per il cessionario).",
            "Se emergono pendenze sul certificato, decurtare l'importo dal prezzo o vincolarlo in escrow per il pagamento diretto all'Erario.",
            "In caso di contestazione fiscale post-rogito, eccepire il beneficio di preventiva escussione del cedente, il limite del valore dell'azienda e l'esclusione dell'intento fraudolento (art. 14 co. 4-5)."
        ],
        "prove": ["Istanza protocollata all'Agenzia delle Entrate ex art. 14 co. 3 D.Lgs. 472/97", "Certificato negativo rilasciato o prova del decorso dei 40 giorni", "Perizia di valore dell'azienda ceduta (tetto di responsabilita')", "Prova della genuinita' commerciale dell'operazione (no frode)"],
        "errori": ["Firmare il rogito di cessione d'azienda senza attendere il certificato art. 14 (errore costosissimo)", "Confondere il certificato AdE con il solo estratto di ruolo AdER", "Compiere una cessione tra societa' riconducibili agli stessi soggetti in frode al Fisco (dove i limiti decadono ex art. 14 co. 4)"]
    },
    {
        "cod": "SOC-137", "slug": "trasferimento-lavoratori-cessione-ramo-azienda-art-2112-cc",
        "cat": "amministratori-ma", "cat_lbl": "Amministratori & M&A", "pilastro": "ma-cessione-azienda-fusioni-scissioni",
        "titolo": "Trasferimento dei lavoratori nella cessione di ramo d'azienda (art. 2112 c.c. e art. 47 L. 428/90)",
        "seo_title": "Cessione Ramo d'Azienda e Dipendenti Art. 2112 c.c.: Procedura Sindacale",
        "desc": "Gestione giuridica del passaggio dei dipendenti in M&A: autonomia funzionale del ramo, informativa sindacale 25 giorni prima, responsabilita' solidale TFR e accordi in deroga.",
        "keywords": ["cessione ramo azienda art 2112 cc", "procedura sindacale art 47 legge 428", "responsabilita solidale tfr cessione azienda"],
        "norme": ["Art. 2112 c.c.", "Art. 47 L. 428/1990"],
        "scenario": "Nella cessione o affitto di un ramo d'azienda (con piu' di 15 dipendenti nell'azienda cedente), venditore e acquirente devono gestire la continuita' dei contratti di lavoro e i debiti pregressi per TFR e retribuzioni.",
        "rischio": "La mancata informativa sindacale 25 giorni prima integra condotta antisindacale (art. 28 Stat. Lav.); inoltre l'acquirente risponde in solido con il venditore per tutti i crediti di lavoro esistenti al trasferimento.",
        "protocollo": [
            "Verificare che il ramo ceduto abbia reale autonomia funzionale preesistente per evitare impugnazioni dei lavoratori sul trasferimento.",
            "Inviare la comunicazione scritta alle RSU/RSA e ai sindacati territoriali almeno 25 giorni prima del perfezionamento dell'atto (o dell'intesa vincolante) ex art. 47 L. 428/1990.",
            "Quantificare esattamente TFR, ferie maturate, ratei e contenziosi pendenti regolandoli nel prezzo di vendita con apposita manleva e conciliazioni individuali in sede protetta (art. 411 c.p.c.).",
            "Se l'impresa cedente e' in stato di crisi accertata o procedura concorsuale, utilizzare le deroghe consentite dall'art. 47 co. 4-bis e 5 L. 428/1990."
        ],
        "prove": ["Comunicazione sindacale PEC inviata almeno 25 giorni prima del closing", "Verbali di esame congiunto con le organizzazioni sindacali", "Prospetto analitico TFR e debiti di lavoro allegato al contratto M&A", "Verbali di conciliazione sindacale ex art. 411 c.p.c. se stipulati"],
        "errori": ["Saltare la procedura sindacale dei 25 giorni quando l'azienda ha oltre 15 dipendenti", "Dimenticare di scomputare dal prezzo il TFR maturato che gravera' solidalmente sull'acquirente", "Creare un 'ramo fittizio' privo di autonomia solo per esternalizzare personale"]
    },
    {
        "cod": "SOC-138", "slug": "contenzioso-post-closing-ma-violazione-garanzie-earn-out",
        "cat": "amministratori-ma", "cat_lbl": "Amministratori & M&A", "pilastro": "ma-cessione-azienda-fusioni-scissioni",
        "titolo": "Contenzioso post-closing M&A: violazione garanzie (R&W), indennizzi ed earn-out",
        "seo_title": "Contenzioso Post-Closing M&A: Garanzie R&W, Indennizzi ed Earn-Out",
        "desc": "Come agire (o difendersi) dopo il closing di una compravendita di quote per passivita' occulte emerse successivamente, violazione di Representations & Warranties o manovre sull'earn-out.",
        "keywords": ["contenzioso post closing ma", "violazione garanzie cessione quote", "contenzioso earn out acquisizione"],
        "norme": ["Art. 1495 c.c.", "Art. 1375 c.c.", "Art. 1218 c.c."],
        "scenario": "Dopo l'acquisto delle quote di una S.r.l. emergono debiti fiscali, cause di lavoro o irregolarita' non dichiarate dal venditore, oppure l'acquirente gestisce l'azienda in modo da azzerare l'earn-out dovuto al venditore.",
        "rischio": "Decadenza dal diritto all'indennizzo per mancata notifica della claim notice nei termini contrattuali, oppure escussione indebita dell'escrow.",
        "protocollo": [
            "Controllare subito nel contratto SPA i termini perentori di denuncia (claim notice), le franchigie (de minimis / basket), il tetto massimo (cap) e la procedura di gestione delle difese verso terzi (third-party claims).",
            "Notificare formalmente via PEC la richiesta di indennizzo con quantificazione provvisoria e bloccare lo svincolo del conto escrow o delle garanzie.",
            "In tema di earn-out, verificare con perizia contabile se i parametri (EBITDA/ricavi) sono stati alterati in violazione del dovere di buona fede esecutiva (art. 1375 c.c.).",
            "Verificare se il contratto prevede clausola arbitrale o competenza del Tribunale delle Imprese."
        ],
        "prove": ["Contratto SPA integrale e disclosure letter allegata al closing", "Documentazione delle passivita' sopravvenute (accertamenti, citazioni, difetti)", "Claim notice tempestivamente notificata secondo le forme del contratto", "Bilanci post-closing e perizia contabile sul calcolo earn-out"],
        "errori": ["Applicare i termini dell'art. 1495 c.c. (8 giorni / 1 anno) senza verificare la natura autonoma delle clausole di indennizzo nel SPA", "Transigere una lite col Fisco o con terzi senza coinvolgere il venditore garante come imposto dal contratto", "Lasciar svincolare l'escrow prima di notificare il claim"]
    },
    {
        "cod": "SOC-139", "slug": "violazione-divieto-concorrenza-cedente-azienda-art-2557-cc",
        "cat": "amministratori-ma", "cat_lbl": "Amministratori & M&A", "pilastro": "ma-cessione-azienda-fusioni-scissioni",
        "titolo": "Violazione del divieto legale di concorrenza del venditore d'azienda o quote (art. 2557 c.c.)",
        "seo_title": "Divieto di Concorrenza Cessione Azienda Art. 2557 c.c.: Ricorso 700",
        "desc": "Come fermare in via d'urgenza il venditore che apre un'attivita' concorrente (anche tramite prestanome o familiari) entro 5 anni dalla cessione di azienda o quote di controllo.",
        "keywords": ["divieto concorrenza cessione azienda art 2557", "venditore apre attivita concorrente", "ricorso 700 art 2557 codice civile"],
        "norme": ["Art. 2557 c.c.", "Art. 2598 c.c.", "Art. 700 c.p.c."],
        "scenario": "Poco dopo aver venduto l'azienda (o il pacchetto di controllo della S.r.l.) incassando l'avviamento, il cedente apre una nuova attivita' simile nelle vicinanze, anche intestandola a un familiare, stornando i vecchi clienti.",
        "rischio": "Svuotamento rapido dell'avviamento appena pagato dall'acquirente.",
        "protocollo": [
            "Raccogliere prove concrete dello sviamento di clientela e dell'effettiva riconducibilita' della nuova attivita' al cedente (visure, social, testimonianze, email ai clienti, presenza fisica in negozio/ufficio).",
            "Ricordare che la giurisprudenza estende l'art. 2557 c.c. (divieto per 5 anni) anche alla cessione di quote societarie quando comporta sostanzialmente la sostituzione nella titolarita' dell'azienda.",
            "Depositare ricorso cautelare d'urgenza ex art. 700 c.p.c. davanti al Tribunale delle Imprese chiedendo l'inibitoria immediata dell'attivita' concorrente con penale per ogni giorno di violazione (art. 614-bis c.p.c.).",
            "Agire nel merito per il risarcimento del danno da perdita di avviamento e sviamento di clientela."
        ],
        "prove": ["Atto di cessione d'azienda o quote e prezzo pagato per l'avviamento", "Visure della nuova societa' concorrente e legami familiari/operativi col cedente", "Email, messaggi, fatture o testimonianze di clienti contattati dal cedente", "Quantificazione del calo di fatturato post-apertura concorrente"],
        "errori": ["Pensare che intestando la nuova ditta alla moglie o al figlio si aggiri l'art. 2557 c.c. (e' vietata anche la concorrenza per interposta persona)", "Inserire un patto di non concorrenza superiore a 5 anni (si riduce automaticamente a 5 anni ex art. 2557 co. 3)", "Attendere mesi prima di chiedere l'inibitoria urgente"]
    },
    {
        "cod": "SOC-140", "slug": "responsabilita-holding-abuso-direzione-coordinamento-art-2497",
        "cat": "amministratori-ma", "cat_lbl": "Amministratori & M&A", "pilastro": "finanziamenti-soci-garanzie-fideiussioni-banche",
        "titolo": "Responsabilita' della holding per abuso di direzione e coordinamento (art. 2497 c.c.)",
        "seo_title": "Responsabilita' Holding Direzione e Coordinamento Art. 2497 c.c.",
        "desc": "Tutela di soci di minoranza, creditori e curatori contro la capogruppo che svuota la controllata violando i principi di corretta gestione societaria e imprenditoriale.",
        "keywords": ["responsabilita holding art 2497 cc", "abuso direzione e coordinamento", "vantaggi compensativi gruppo art 2497"],
        "norme": ["Art. 2497 c.c.", "Art. 2497-bis c.c.", "Art. 2497-ter c.c."],
        "scenario": "La societa' capogruppo impone alla controllata operazioni svantaggiose (prezzi di trasferimento squilibrati, garanzie gratuite, drenaggio di liquidita') nell'interesse esclusivo della holding.",
        "rischio": "La holding (e chi ha partecipato al fatto lesivo, inclusi gli amministratori della capogruppo) risponde direttamente verso i soci esterni e i creditori sociali della controllata.",
        "protocollo": [
            "Accertare l'esercizio effettivo dell'attivita' di direzione e coordinamento (presunta ex art. 2497-sexies in presenza di consolidamento o controllo, ma provabile anche di fatto per holding personali).",
            "Dimostrare la violazione dei principi di corretta gestione societaria e imprenditoriale e l'assenza di vantaggi compensativi complessivi (art. 2497 co. 1 ult. periodo).",
            "Verificare il rispetto della condizione di sussidiarieta' (art. 2497 co. 3: richiesta preventiva o incapienza della controllata).",
            "In caso di difesa della holding, documentare le delibere motivate ex art. 2497-ter c.c. e i reali vantaggi sinergici ricevuti dalla controllata."
        ],
        "prove": ["Bilanci consolidati, pubblicita' ex art. 2497-bis e direttive impartite dalla capogruppo", "Contratti infragruppo e analisi dei prezzi di trasferimento", "Perizia contabile sul pregiudizio alla redditivita' e all'integrita' patrimoniale", "Delibere motivate o assenza di motivazione ex art. 2497-ter c.c."],
        "errori": ["Agire contro la holding senza verificare la condizione di mancata soddisfazione da parte della controllata (art. 2497 co. 3)", "Dimenticare che in caso di liquidazione giudiziale della controllata l'azione dei creditori spetta al curatore (art. 2497 co. 4)", "Non motivare analiticamente le decisioni influenzate dalla capogruppo"]
    },

    # ═══════════════════ 8. SOVRAINDEBITAMENTO & BANCHE (141-150) ═══════════════════
    {
        "cod": "SOC-141", "slug": "concordato-minore-imprenditore-sotto-soglia-art-74-ccii",
        "cat": "sovraindebitamento-banche", "cat_lbl": "Sovraindebitamento & Banche", "pilastro": "sovraindebitamento-esdebitazione-imprenditore",
        "titolo": "Concordato minore per impresa sotto soglia, ditta individuale e professionista (art. 74 CCII)",
        "seo_title": "Concordato Minore Art. 74 CCII: Ristrutturazione Impresa Minore",
        "desc": "Come ristrutturare e stralciare debiti fiscali, bancari e commerciali per imprese minori, agricoli e professionisti tramite l'OCC con cram-down fiscale e stop pignoramenti.",
        "keywords": ["concordato minore art 74 ccii", "sovraindebitamento impresa minore", "stralcio debiti fisco concordato minore"],
        "norme": ["Art. 74 CCII", "Art. 78 CCII", "Art. 80 CCII", "D.Lgs. 136/2024"],
        "scenario": "Una piccola S.r.l. sotto le soglie dell'art. 2 CCII, una ditta individuale, un'azienda agricola o un professionista non riesce piu' a pagare AdER, INPS e banche ma vuole proseguire l'attivita'.",
        "rischio": "Pignoramenti su conti, automezzi e crediti bloccano il lavoro quotidiano se non si attiva subito la protezione del Tribunale.",
        "protocollo": [
            "Presentare istanza all'OCC competente per la nomina del Gestore della Crisi e predisporre una proposta di concordato minore in continuita' (o liquidatorio con apporto di risorse esterne apprezzabili).",
            "Chiedere al giudice nel decreto di apertura le misure protettive ex art. 78 co. 2 lett. d CCII per bloccare immediatamente tutte le azioni esecutive e cautelari.",
            "Sottoporre la proposta al voto dei creditori (maggioranza del 50% dei crediti ammessi al voto; silenzio-assenso ex art. 79 co. 3 CCII).",
            "In caso di mancata adesione di Agenzia delle Entrate o INPS, chiedere il cram-down fiscale ex art. 80 co. 3 CCII dimostrando la convenienza rispetto alla liquidazione controllata."
        ],
        "prove": ["Bilanci/dichiarazioni fiscali attestanti il rispetto delle soglie di impresa minore", "Elenco completo debiti e attivo + relazione particolareggiata dell'OCC", "Piano di continuita' o impegno di finanza esterna", "Decreto di apertura con misure protettive"],
        "errori": ["Proporre un concordato minore meramente liquidatorio senza alcun apporto di risorse esterne apprezzabili (inammissibile ex art. 74 co. 2)", "Presentare la domanda per un'impresa gia' cancellata dal Registro Imprese (esclusa dal concordato minore ex art. 33 co. 4 CCII)", "Omettere crediti fiscali o atti in frode compiuti negli ultimi 5 anni"]
    },
    {
        "cod": "SOC-142", "slug": "liquidazione-controllata-sovraindebitato-art-268-ccii",
        "cat": "sovraindebitamento-banche", "cat_lbl": "Sovraindebitamento & Banche", "pilastro": "sovraindebitamento-esdebitazione-imprenditore",
        "titolo": "Liquidazione controllata del sovraindebitato (art. 268 CCII): stop pignoramenti e durata 3 anni",
        "seo_title": "Liquidazione Controllata Art. 268 CCII: Requisiti e 3 Anni",
        "desc": "Come accedere alla liquidazione controllata per imprese minori, ex imprenditori cessati e soci garanti, mettendo a disposizione i beni/eccedenze per 3 anni e azzerando i debiti residui.",
        "keywords": ["liquidazione controllata art 268 ccii", "sovraindebitamento ex imprenditore", "blocco pignoramenti liquidazione controllata"],
        "norme": ["Art. 268 CCII", "Art. 270 CCII", "Art. 282 CCII", "D.Lgs. 136/2024"],
        "scenario": "Un ex imprenditore, un piccolo artigiano o un socio garante e' oppresso da debiti enormi (cartelle AdER, banche, fornitori) e non ha la possibilita' di proporre un concordato minore.",
        "rischio": "Pignoramenti a vita su stipendi, pensioni e conti correnti che impediscono qualunque ripartenza lavorativa.",
        "protocollo": [
            "Attivare l'OCC per acquisire la relazione che attesta la completezza della documentazione e la sussistenza di un attivo acquisibile (anche solo quote di reddito futuro oltre il necessario per il mantenimento familiare).",
            "Depositare ricorso di apertura della liquidazione controllata ex art. 268 CCII: dalla sentenza operano il divieto di azioni esecutive individuali e la sospensione del corso degli interessi chirografari.",
            "Far determinare al giudice la quota di stipendio/reddito esclusa dalla liquidazione per il dignitoso mantenimento del debitore e della famiglia (art. 268 co. 4 lett. b).",
            "Decorsi 3 anni dall'apertura, ottenere l'esdebitazione di diritto ex art. 282 CCII per tutti i debiti non soddisfatti."
        ],
        "prove": ["Relazione dell'OCC ex art. 269 co. 2 CCII", "Elenco integrale dei debiti, visure e spese essenziali del nucleo familiare", "Dichiarazioni dei redditi ultimi tre anni", "Sentenza di apertura della liquidazione controllata"],
        "errori": ["Chiedere la liquidazione controllata senza alcun bene ne' quota di reddito disponibile (in quel caso lo strumento corretto e' l'esdebitazione dell'incapiente ex art. 283 CCII)", "Occultare beni o redditi durante il triennio (fa perdere l'esdebitazione)", "Non far determinare subito la soglia di reddito necessaria al mantenimento familiare"]
    },
    {
        "cod": "SOC-143", "slug": "esdebitazione-di-diritto-dopo-3-anni-art-282-ccii",
        "cat": "sovraindebitamento-banche", "cat_lbl": "Sovraindebitamento & Banche", "pilastro": "sovraindebitamento-esdebitazione-imprenditore",
        "titolo": "Esdebitazione dell'imprenditore e del sovraindebitato dopo 3 anni (artt. 278-282 CCII)",
        "seo_title": "Esdebitazione dopo 3 Anni Art. 278 e 282 CCII: Cancellazione Debiti",
        "desc": "Come ottenere la liberazione definitiva da tutti i debiti residui (incluse cartelle esattoriali e banche) decorsi 3 anni dall'apertura della liquidazione giudiziale o controllata.",
        "keywords": ["esdebitazione 3 anni art 282 ccii", "cancellazione debiti residui fallimento", "condizioni esdebitazione art 280 ccii"],
        "norme": ["Art. 278 CCII", "Art. 280 CCII", "Art. 282 CCII"],
        "scenario": "Un imprenditore o un sovraindebitato sottoposto a liquidazione giudiziale o controllata raggiunge i 3 anni dall'apertura (o la chiusura anticipata) e vuole la cancellazione legale dei debiti non pagati.",
        "rischio": "La presenza di condanne per bancarotta fraudolenta, atti in frode ai creditori o mancata collaborazione con gli organi della procedura puo' ostacolare l'esdebitazione.",
        "protocollo": [
            "Verificare tutte le condizioni soggettive dell'art. 280 CCII (assenza condanne definitive per bancarotta fraudolenta o delitti contro l'economia, assenza di distrazioni o frodi, collaborazione leale col curatore/liquidatore, nessuna esdebitazione nei 5 anni precedenti).",
            "Ricordare che l'esdebitazione oggi non richiede piu' il soddisfacimento parziale minimo dei creditori e si applica anche ai debiti tributari e previdenziali (restano esclusi solo mantenimento, alimenti e risarcimenti da illecito extracontrattuale/sanzioni penali).",
            "Presentare istanza o sollecitare il decreto di esdebitazione del Tribunale allo scadere del triennio ex artt. 281-282 CCII.",
            "In caso di opposizione di creditori, difendere in udienza la piena meritevolezza del debitore."
        ],
        "prove": ["Sentenza di apertura della liquidazione con decorso del triennio", "Casellario giudiziale pulito da reati ostativi", "Relazione del curatore/liquidatore attestante la piena collaborazione", "Decreto di esdebitazione"],
        "errori": ["Credere che i debiti verso Agenzia delle Entrate o INPS non siano esdebitabili (sono esdebitabili)", "Non collaborare con il curatore o il liquidatore durante la procedura", "Dimenticare che i coobbligati e fideiussori restano comunque obbligati verso i creditori (art. 278 co. 6)"]
    },
    {
        "cod": "SOC-144", "slug": "esdebitazione-debitore-incapiente-zero-art-283-ccii",
        "cat": "sovraindebitamento-banche", "cat_lbl": "Sovraindebitamento & Banche", "pilastro": "sovraindebitamento-esdebitazione-imprenditore",
        "titolo": "Esdebitazione del debitore incapiente (a costo zero) ex art. 283 CCII",
        "seo_title": "Esdebitazione Debitore Incapiente Art. 283 CCII: Azzerare Debiti",
        "desc": "Come cancellare integralmente i debiti residui di una persona fisica (anche ex socio o ex imprenditore) meritevole priva di beni e con reddito appena sufficiente al sostentamento.",
        "keywords": ["esdebitazione debitore incapiente art 283 ccii", "cancellazione debiti senza beni", "fresh start art 283 ccii"],
        "norme": ["Art. 283 CCII", "D.Lgs. 136/2024"],
        "scenario": "Una persona fisica meritevole (spesso un ex imprenditore o socio fideiussore travolto dalla chiusura della propria attivita') non possiede immobili ne' risparmi e percepisce un reddito appena sufficiente a mantenere la famiglia.",
        "rischio": "Senza l'esdebitazione ex art. 283 CCII, il soggetto resta escluso per sempre dal circuito economico e bancario.",
        "protocollo": [
            "Verificare il parametro oggettivo di incapienza dell'art. 283 co. 2 CCII (reddito annuo al netto delle spese necessarie al mantenimento non superiore all'assegno sociale moltiplicato per la scala di equivalenza ISEE).",
            "Dimostrare la meritevolezza attraverso la relazione particolareggiata dell'OCC (assenza di atti in frode, dolo o colpa grave nella formazione dell'indebitamento).",
            "Depositare ricorso al Tribunale tramite OCC per ottenere il decreto di esdebitazione dell'incapiente (concedibile una sola volta nella vita).",
            "Rispettare nei 3 anni successivi (ridotti da 4 a 3 dal D.Lgs. 136/2024) l'obbligo annuale di dichiarare eventuali sopravvenienze rilevanti (> 10% dei debiti)."
        ],
        "prove": ["Relazione particolareggiata dell'OCC sulla meritevolezza e sulle cause della crisi", "ISEE, stato di famiglia, dichiarazioni redditi e spese documentate", "Visure catastali e PRA negative", "Elenco completo di tutti i creditori"],
        "errori": ["Omettere la dichiarazione annuale delle sopravvenienze nei 3 anni successivi (causa revoca del beneficio)", "Presentare la domanda in presenza di colpa grave provata o atti in frode", "Confondere la durata del monitoraggio post-decreto (3 anni dopo il Correttivo-ter D.Lgs. 136/2024)"]
    },
    {
        "cod": "SOC-145", "slug": "ristrutturazione-debiti-socio-fideiussore-art-2-correttivo-ter",
        "cat": "sovraindebitamento-banche", "cat_lbl": "Sovraindebitamento & Banche", "pilastro": "sovraindebitamento-esdebitazione-imprenditore",
        "titolo": "Tutela del socio fideiussore e dell'ex socio di S.n.c./S.a.s. nel sovraindebitamento (D.Lgs. 136/2024)",
        "seo_title": "Sovraindebitamento Socio Fideiussore e Socio S.n.c. dopo D.Lgs. 136/2024",
        "desc": "Come il socio illimitatamente responsabile o il socio fideiussore puo' accedere alle procedure di sovraindebitamento del CCII per i debiti personali e per le garanzie prestate.",
        "keywords": ["sovraindebitamento socio fideiussore", "art 2 comma 1 lettera e ccii correttivo ter", "ristrutturazione debiti socio snc"],
        "norme": ["Art. 2 co. 1 lett. e CCII", "D.Lgs. 136/2024", "Artt. 67 e 268 CCII"],
        "scenario": "Un socio di S.n.c., S.a.s. o S.r.l. che ha prestato fideiussioni personali alle banche viene aggredito sul proprio patrimonio familiare dopo il dissesto della societa'.",
        "rischio": "Pignoramento della casa familiare e dello stipendio del socio garante anche dopo la chiusura della societa'.",
        "protocollo": [
            "Verificare la natura dei debiti: per i debiti estranei all'attivita' d'impresa del socio illimitatamente responsabile, il D.Lgs. 136/2024 ha confermato l'accesso alla ristrutturazione dei debiti del consumatore (art. 67 CCII).",
            "Per i debiti misti o derivanti da fideiussioni prestate a favore della societa' (debiti d'impresa), valutare la nullita' delle fideiussioni ABI (per ridurre o azzerare il debito) e l'accesso alla liquidazione controllata (art. 268 CCII) o alla procedura familiare (art. 66 CCII).",
            "Chiedere la sospensione urgente delle aste immobiliari sulla casa di abitazione.",
            "Coordinare la difesa del socio garante con la procedura concorsuale della societa'."
        ],
        "prove": ["Contratti di fideiussione firmati dal socio", "Elenco separato dei debiti personali/familiari e dei debiti da garanzie societarie", "Visure immobiliari e atti di pignoramento in corso", "Relazione OCC e valutazione meritevolezza"],
        "errori": ["Presentare un piano del consumatore per sole fideiussioni imprenditoriali (rischio inammissibilita')", "Non verificare prima se le fideiussioni bancarie sono nulle ex schema ABI o estinte ex art. 1957 c.c.", "Attendere l'aggiudicazione dell'asta immobiliare prima di attivare l'OCC"]
    },
    {
        "cod": "SOC-146", "slug": "nullita-fideiussione-omnibus-schema-abi-decadenza-art-1957",
        "cat": "sovraindebitamento-banche", "cat_lbl": "Sovraindebitamento & Banche", "pilastro": "finanziamenti-soci-garanzie-fideiussioni-banche",
        "titolo": "Nullita' della fideiussione omnibus conforme allo schema ABI e decadenza della banca (art. 1957 c.c.)",
        "seo_title": "Nullita' Fideiussione Omnibus Schema ABI e Decadenza Art. 1957 c.c.",
        "desc": "Come liberare il socio garante dal decreto ingiuntivo o precetto della banca: nullita' parziale delle clausole 2, 6 e 8 ABI (Sezioni Unite 41994/2021) ed estinzione della garanzia dopo 6 mesi.",
        "keywords": ["nullita fideiussione omnibus schema abi", "decadenza banca art 1957 cc", "opposizione decreto ingiuntivo fideiussore"],
        "norme": ["Art. 2 L. 287/1990", "Art. 1957 c.c.", "Provv. Banca d'Italia n. 55/2005"],
        "scenario": "Una banca o una societa' cessionaria di NPL notifica decreto ingiuntivo o atto di precetto al socio/amministratore che anni prima aveva firmato una fideiussione omnibus a favore della societa'.",
        "rischio": "Pignoramento del patrimonio personale del garante per centinaia di migliaia di euro, se non si propone opposizione tempestiva entro 40 giorni.",
        "protocollo": [
            "Confrontare parola per parola il testo della fideiussione firmata con le clausole 2 (reviviscenza), 6 (deroga all'art. 1957 c.c.) e 8 (sopravvivenza) dello schema ABI censurato da Banca d'Italia.",
            "Eccepire la nullita' parziale della clausola 6 di deroga all'art. 1957 c.c. (principio delle Sezioni Unite n. 41994/2021) con conseguente reviviscenza del termine semestrale di decadenza.",
            "Verificare se la banca ha agito GIUDIZIALMENTE (non basta una semplice lettera stragiudiziale!) contro il debitore principale o il garante entro 6 mesi dalla scadenza/revoca dell'obbligazione principale.",
            "Proporre opposizione a decreto ingiuntivo (entro 40 giorni) o azione di accertamento negativo della garanzia davanti al Tribunale competente (verificando anche la competenza della Sezione Imprese per l'azione antitrust autonoma)."
        ],
        "prove": ["Copia integrale del contratto di fideiussione omnibus firmato", "Provvedimento Banca d'Italia n. 55/2005 e schema ABI 2003", "Lettera di revoca affidamenti/decadenza dal beneficio del termine e data della prima azione giudiziale bancaria", "Eventuali cessioni in blocco NPL (verifica legittimazione ex art. 58 TUB)"],
        "errori": ["Far decorrere i 40 giorni dalla notifica del decreto ingiuntivo (il decreto diventa definitivo)", "Confondere la fideiussione specifica con la fideiussione omnibus senza verificare la prova dell'intesa anticoncorrenziale", "Dimenticare di verificare anche la legittimazione attiva del cessionario NPL"]
    },
    {
        "cod": "SOC-147", "slug": "liberazione-fideiussore-nuovo-credito-art-1956-cc",
        "cat": "sovraindebitamento-banche", "cat_lbl": "Sovraindebitamento & Banche", "pilastro": "finanziamenti-soci-garanzie-fideiussioni-banche",
        "titolo": "Liberazione del fideiussore per concessione di nuovo credito a societa' gia' in crisi (art. 1956 c.c.)",
        "seo_title": "Liberazione Fideiussore Art. 1956 c.c.: Credito a Societa' in Crisi",
        "desc": "Quando il socio garante (specie se estraneo alla gestione) e' liberato ex lege dalla fideiussione perche' la banca ha continuato a fare credito alla societa' pur conoscendone il peggioramento patrimoniale.",
        "keywords": ["liberazione fideiussore art 1956 cc", "concessione credito peggioramento patrimonio", "fideiussore estraneo gestione"],
        "norme": ["Art. 1956 c.c.", "Art. 1375 c.c."],
        "scenario": "Un socio di minoranza, un familiare o un ex amministratore uscito dalla societa' viene escusso dalla banca per nuovi utilizzi o aumenti di fido concessi quando la societa' era gia' in grave dissesto.",
        "rischio": "Rispondere di debiti contratti da altri amministratori quando il garante non aveva piu' controllo sulla societa'.",
        "protocollo": [
            "Dimostrare due presupposti oggettivi: (1) la banca ha fatto nuovo credito dopo il sensibile peggioramento delle condizioni patrimoniali della societa' (visibile da bilanci, sconfini, Centrale Rischi); (2) manca una speciale autorizzazione del fideiussore.",
            "Verificare che la rinuncia preventiva alla liberazione ex art. 1956 co. 2 c.c. e' nulla per espressa previsione di legge.",
            "Dimostrare l'estraneita' del fideiussore alla gestione (es. ex amministratore dimesso o familiare non gestore) per superare l'eccezione della banca sulla presunta conoscenza della crisi.",
            "Eccepire la liberazione totale o parziale in sede di opposizione a decreto ingiuntivo o giudizio di merito."
        ],
        "prove": ["Visura storica che attesta le dimissioni o la posizione di mero socio/familiare", "Estratti conto e Centrale Rischi che provano il peggioramento noto alla banca prima del nuovo credito", "Contratti di aumento fidi o nuovi finanziamenti senza autorizzazione del garante", "Eventuale lettera di recesso dalla fideiussione"],
        "errori": ["Non inviare formale recesso dalla fideiussione omnibus quando si esce dalla societa' o ci si dimette da amministratore", "Invocare l'art. 1956 se il garante era egli stesso l'amministratore unico che ha chiesto il nuovo fido", "Non provare il momento esatto del peggioramento patrimoniale"]
    },
    {
        "cod": "SOC-148", "slug": "cancellazione-urgente-segnalazione-centrale-rischi-art-700",
        "cat": "sovraindebitamento-banche", "cat_lbl": "Sovraindebitamento & Banche", "pilastro": "finanziamenti-soci-garanzie-fideiussioni-banche",
        "titolo": "Cancellazione urgente di segnalazione illegittima a sofferenza in Centrale Rischi (art. 700 c.p.c.)",
        "seo_title": "Cancellazione Centrale Rischi Art. 700 c.p.c.: Difesa Imprese",
        "desc": "Come ottenere in poche settimane dal Tribunale la cancellazione di una segnalazione a sofferenza in Centrale Rischi Banca d'Italia fatta senza reale insolvenza o senza preavviso.",
        "keywords": ["cancellazione centrale rischi art 700", "segnalazione sofferenza illegittima banca", "risarcimento danno segnalazione centrale rischi"],
        "norme": ["Art. 700 c.p.c.", "Circolare Banca d'Italia n. 139/1991", "Art. 125 TUB"],
        "scenario": "Una banca segnala 'a sofferenza' in Centrale Rischi un'azienda (o un socio garante) per un singolo credito contestato o un ritardo temporaneo, provocando la revoca immediata dei fidi da parte di tutte le altre banche.",
        "rischio": "Effetto domino mortale sul credito bancario (asfissia finanziaria) anche per aziende patrimonialmente sane.",
        "protocollo": [
            "Acquisire subito la visura integrale della Centrale Rischi Banca d'Italia e verificare l'assenza dei presupposti di legge: la 'sofferenza' richiede una valutazione complessiva di grave e non transitoria insolvenza (non basta un semplice ritardo o una contestazione fondata del credito).",
            "Verificare la violazione dell'obbligo di preavviso scritto e di corretta istruttoria da parte dell'intermediario.",
            "Inviare diffida PEC con termine di 48-72 ore alla banca per l'immediata rettifica/cancellazione.",
            "In difetto, depositare ricorso cautelare d'urgenza ex art. 700 c.p.c. per ottenere l'ordine immediato di cancellazione (oltre al risarcimento del danno patrimoniale e reputazionale nel merito)."
        ],
        "prove": ["Visura Centrale Rischi Banca d'Italia aggiornata", "Bilanci, patrimonio e linee regolari presso altre banche che smentiscono l'insolvenza", "Documentazione della contestazione sul credito (es. anatocismo, nullita' fideiussione)", "Diffida PEC inviata alla banca e lettere di revoca fidi ricevute da altri istituti"],
        "errori": ["Aspettare mesi prima di reagire mentre tutte le altre banche chiudono i castelletti", "Confondere la segnalazione in Centrale Rischi (Banca d'Italia, > 30.000 euro o sofferenze) con i SIC privati (CRIF/Experian)", "Non documentare il periculum in mora (revoca fidi e danno all'operativita')"]
    },
    {
        "cod": "SOC-149", "slug": "difesa-escussione-garanzia-pubblica-mcc-mediocredito-centrale",
        "cat": "sovraindebitamento-banche", "cat_lbl": "Sovraindebitamento & Banche", "pilastro": "finanziamenti-soci-garanzie-fideiussioni-banche",
        "titolo": "Difesa da escussione della garanzia pubblica MCC (Mediocredito Centrale) e cartella esattoriale",
        "seo_title": "Escussione Garanzia MCC Mediocredito Centrale e Cartella: Difesa",
        "desc": "Come difendere l'impresa e i garanti quando la banca escute la garanzia del Fondo PMI (MCC) e il credito diventa privilegiato riscosso tramite cartella AdER.",
        "keywords": ["escussione garanzia mcc mediocredito centrale", "privilegio rivalsa mcc ccii", "difesa cartella esattoriale garanzia mcc"],
        "norme": ["Art. 9 co. 5 D.Lgs. 123/1998", "L. 662/1996", "Art. 13 D.L. 23/2020"],
        "scenario": "A seguito dell'inadempimento su un finanziamento COVID o PMI garantito all'80-90% dal Fondo di Garanzia MCC, la banca escute il Fondo e Mediocredito Centrale attiva la rivalsa esattoriale con privilegio generale.",
        "rischio": "Un debito bancario chirografario si trasforma in debito pubblico privilegiato riscosso via ruolo da AdER, complicando concordati e accordi e colpendo i garanti.",
        "protocollo": [
            "Verificare prima dell'escussione la possibilita' di rimodulare il mutuo o accedere a Composizione Negoziata/concordato prevenendo l'attivazione della garanzia (e gestendo correttamente la classe dedicata ai creditori garantiti da terzi).",
            "Verificare la legittimita' dell'istruttoria bancaria iniziale di merito creditizio e il rispetto delle disposizioni operative del Fondo MCC (eventuale inefficacia della garanzia o responsabilita' della banca per concessione abusiva).",
            "Contestare eventuali vizi della cartella esattoriale o dell'iscrizione a ruolo (notifica, motivazione, calcolo interessi e sanzioni).",
            "Negoziare la rateazione con AdER o inserire il credito di rivalsa MCC nel piano di ristrutturazione/concordato."
        ],
        "prove": ["Contratto di finanziamento e delibera di ammissione al Fondo di Garanzia MCC", "Comunicazioni di decadenza dal beneficio del termine ed escussione del Fondo", "Cartella di pagamento AdER o avviso di addebito MCC", "Documentazione dell'istruttoria bancaria originaria"],
        "errori": ["Sottovalutare la natura privilegiata del credito di rivalsa MCC nei piani di ristrutturazione", "Ignorare la lettera di avvio procedimento di revoca/escussione di MCC", "Non verificare se la banca ha concesso il finanziamento garantito per ripianare propri scoperti pregressi (operazione illegittima)"]
    },
    {
        "cod": "SOC-150", "slug": "postergazione-finanziamenti-soci-art-2467-cc-revocatoria",
        "cat": "sovraindebitamento-banche", "cat_lbl": "Sovraindebitamento & Banche", "pilastro": "finanziamenti-soci-garanzie-fideiussioni-banche",
        "titolo": "Postergazione dei finanziamenti soci (art. 2467 c.c.) e difesa da restituzione o revocatoria",
        "seo_title": "Finanziamenti Soci Art. 2467 c.c.: Postergazione e Revocatoria",
        "desc": "Quando il rimborso di un prestito del socio e' postergato rispetto agli altri creditori, quando scatta l'obbligo di restituzione al curatore (art. 164 co. 2 CCII) e come strutturare correttamente i versamenti.",
        "keywords": ["postergazione finanziamenti soci art 2467", "restituzione rimborso finanziamento soci art 164 ccii", "versamento conto capitale vs finanziamento"],
        "norme": ["Art. 2467 c.c.", "Art. 164 co. 2 CCII", "Art. 102 CCII"],
        "scenario": "Un socio ha finanziato la S.r.l. in un momento di squilibrio finanziario e si e' fatto rimborsare il prestito nell'anno anteriore alla liquidazione giudiziale, oppure chiede l'ammissione al passivo.",
        "rischio": "I rimborsi eseguiti nell'anno anteriore alla domanda di liquidazione giudiziale sono privi di effetto di diritto ex art. 164 co. 2 CCII e il socio deve restituire integralmente i soldi al curatore (oltre a rischi penali di bancarotta preferenziale).",
        "protocollo": [
            "In sede di difesa del socio: dimostrare con perizia contabile che al momento della concessione del finanziamento NON sussisteva eccessivo squilibrio tra indebitamento e patrimonio netto ne' una situazione in cui fosse ragionevole un conferimento (onere di analisi ex ante).",
            "Verificare che il rimborso sia avvenuto oltre l'anno anteriore al deposito della domanda di liquidazione giudiziale (art. 164 co. 2 CCII).",
            "In sede preventiva durante la crisi: canalizzare la nuova finanza dei soci SOLO tramite autorizzazione del Tribunale in Composizione Negoziata (art. 22 CCII) o in concordato/ARD (art. 102 CCII) per ottenere la prededuzione anziche' la postergazione.",
            "Distinguere chiaramente nei verbali e nella contabilita' i versamenti in conto capitale/copertura perdite dai finanziamenti fruttiferi/infruttiferi con diritto al rimborso."
        ],
        "prove": ["Bilanci e indici di squilibrio finanziario alla data di erogazione del finanziamento", "Delibere sociali e contratti di finanziamento soci con data certa", "Contabili bancarie dei versamenti e degli eventuali rimborsi", "Eventuali autorizzazioni giudiziali ex artt. 22 o 102 CCII"],
        "errori": ["Farsi rimborsare un finanziamento soci mentre l'azienda e' gia' in stato di crisi o insolvenza", "Confondere un finanziamento soci con un versamento in conto futuro aumento capitale", "Erogare nuova liquidita' dei soci in crisi senza sfruttare la prededuzione autorizzata dal Tribunale"]
    }
]
