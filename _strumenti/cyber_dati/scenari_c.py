# -*- coding: utf-8 -*-
"""Scenari operativi e protocolli di difesa 71-110 (Crypto, SPID/PEC, AI/Deepfake, Lavoro/Segreti, Sanita', PA, E-commerce, Minori)."""

SCENARI_C = [
    # ═══════════════════ TRUFFA CRYPTO, WALLET & FINTECH (71-78) ═══════════════════
    {
        "cod": "CYB-71", "slug": "wallet-drainer-svuotamento-criptovalute-metamask",
        "cat": "truffe-banche", "cat_lbl": "Truffe & Banche", "pilastro": "truffe-online-phishing-sim-swap-banche",
        "titolo": "Wallet drainer e svuotamento di criptovalute su MetaMask o Ledger",
        "seo_title": "Wallet Drainer Criptovalute: Denuncia, Tracing e Recupero",
        "desc": "Protocollo legale immediato dopo lo svuotamento di un wallet crypto: preservazione TXID, querela ex art. 640-ter c.p., tracciamento on-chain e richiesta sequestro su exchange.",
        "keywords": ["wallet drainer criptovalute", "truffa metamask denuncia", "recupero criptovalute rubate", "art 640-ter cp crypto"],
        "norme": ["Art. 640-ter c.p.", "Art. 615-ter c.p.", "Art. 321 c.p.p."],
        "scenario": "L'utente firma inconsapevolmente uno smart contract malevolo su un sito clone che svuota in pochi secondi token, USDT o NFT dal wallet non-custodial.",
        "rischio": "I fondi vengono rapidamente instradati su bridge o exchange centralizzati: senza blocco immediato e tracciamento forense la dispersione diventa irreversibile.",
        "protocollo": [
            "Revocare subito tutte le approvazioni attive sul wallet e non effettuare ulteriori transazioni dal dispositivo compromesso.",
            "Estrarre e conservare gli hash delle transazioni (TXID), gli indirizzi di destinazione e gli screenshot del sito clone.",
            "Attivare un tracciamento on-chain per individuare l'eventuale approdo dei fondi su un exchange centralizzato soggetto a KYC.",
            "Depositare querela urgente con istanza di sequestro preventivo d'urgenza e segnalazione compliance all'exchange di destinazione."
        ],
        "prove": ["Hash TXID e indirizzi blockchain", "URL e certificato del sito phishing", "Log wallet e revoche approvazioni", "Report preliminare di tracing on-chain"],
        "errori": ["Pagare falsi recuperatori online che promettono sblocchi istantanei", "Ritardare la querela lasciando tempo al prelievo fiat sugli exchange", "Formattare il PC o cancellare la cronologia browser prima dell'acquisizione"]
    },
    {
        "cod": "CYB-72", "slug": "falso-broker-trading-online-criptovalute-blocco-prelievi",
        "cat": "truffe-banche", "cat_lbl": "Truffe & Banche", "pilastro": "truffe-online-phishing-sim-swap-banche",
        "titolo": "Falso broker di trading online e piattaforma crypto che blocca i prelievi",
        "seo_title": "Truffa Trading Online e Falso Broker: Difesa e Recupero",
        "desc": "Come difendersi da piattaforme abusive di trading e crypto che chiedono tasse fittizie per sbloccare i prelievi: querela, verifica CONSOB e profili bancari.",
        "keywords": ["truffa trading online", "falso broker criptovalute", "piattaforma blocca prelievi", "recupero soldi truffa trading"],
        "norme": ["Art. 640 c.p.", "Art. 166 D.Lgs. 58/1998 (TUF)", "Art. 640-ter c.p."],
        "scenario": "Un investitore versa somme tramite bonifici SEPA o carte su una piattaforma non autorizzata che simula profitti elevati e pretende ulteriori versamenti per sbloccare il capitale.",
        "rischio": "La vittima subisce una doppia perdita se cede alla richiesta di imposte fittizie o commissioni di sblocco, mentre i conti beneficiari vengono svuotati.",
        "protocollo": [
            "Interrompere immediatamente ogni ulteriore versamento e bloccare l'accesso remoto (AnyDesk o TeamViewer) eventualmente concesso.",
            "Verificare lo stato autorizzativo dell'intermediario negli elenchi CONSOB e raccogliere tutti gli IBAN beneficiari.",
            "Inviare formale reclamo e richiesta di recall dei bonifici agli istituti di credito coinvolti, valutando la responsabilita' dell'intermediario.",
            "Presentare querela circostanziata per truffa aggravata e abusivismo finanziario con richiesta di sequestro dei conti di transito."
        ],
        "prove": ["Contabili bonifici SEPA e ricevute carte", "Chat WhatsApp e Telegram con i finti consulenti", "Log di accesso AnyDesk/TeamViewer", "Screenshot dashboard falsa e richieste di sblocco"],
        "errori": ["Versare presunte tasse o spese di sblocco per recuperare il saldo mostrato", "Lasciare installati software di controllo remoto sul proprio dispositivo", "Cancellare le conversazioni con i sedicenti account manager"]
    },
    {
        "cod": "CYB-73", "slug": "sim-swapping-clonazione-scheda-telefonica-otp-banca",
        "cat": "truffe-banche", "cat_lbl": "Truffe & Banche", "pilastro": "truffe-online-phishing-sim-swap-banche",
        "titolo": "SIM swapping e clonazione della SIM per intercettare gli OTP bancari",
        "seo_title": "SIM Swapping e Furto OTP Bancari: Rimborso Banca e Operatore",
        "desc": "Responsabilita' concorrente di banca e operatore telefonico in caso di SIM swap: disconoscimento PSD2, reclamo AGCOM e ricorso ABF per il recupero delle somme.",
        "keywords": ["sim swapping rimborso banca", "clonazione sim otp", "responsabilita operatore telefonico sim swap", "ricorso abf sim swap"],
        "norme": ["Art. 10 D.Lgs. 11/2010", "Art. 12 D.Lgs. 11/2010", "Art. 2050 c.c.", "Delibere AGCOM su portabilita' SIM"],
        "scenario": "Il cellulare perde improvvisamente segnale perche' un terzo ha ottenuto la sostituzione o la portabilita' della SIM con documenti falsi, intercettando gli SMS bancari.",
        "rischio": "In poche decine di minuti vengono svuotati conti correnti, modificate password email e attivati finanziamenti online a nome della vittima.",
        "protocollo": [
            "Contattare subito l'operatore telefonico e la banca per bloccare SIM, home banking e carte, annotando data e numero di ticket.",
            "Presentare denuncia querela allegando la prova dell'improvvisa disattivazione della rete e delle operazioni non autorizzate.",
            "Inviare doppio reclamo formale: alla banca ex D.Lgs. 11/2010 per il rimborso immediato e all'operatore telefonico per il rilascio indebito della SIM.",
            "In caso di diniego, attivare il ricorso all'Arbitro Bancario Finanziario (ABF) e la procedura di conciliazione Co.Re.Com / ConciliaWeb."
        ],
        "prove": ["Attestazione operatore su data e punto vendita della sostituzione SIM", "Estratto conto con operazioni disconosciute", "Denuncia querela", "Reclami PEC inviati a banca e operatore"],
        "errori": ["Limitarsi a una segnalazione telefonica senza reclamo scritto via PEC", "Non richiedere all'operatore copia della documentazione usata per la sostituzione SIM", "Trascurare il controllo della propria casella email e dello SPID compromessi"]
    },
    {
        "cod": "CYB-74", "slug": "chargeback-clonazione-carta-credito-acquisti-esteri",
        "cat": "truffe-banche", "cat_lbl": "Truffe & Banche", "pilastro": "truffe-online-phishing-sim-swap-banche",
        "titolo": "Clonazione carta di credito e addebiti non autorizzati su siti esteri",
        "seo_title": "Clonazione Carta di Credito: Disconoscimento e Rimborso PSD2",
        "desc": "Come ottenere il rimborso integrale dopo addebiti fraudolenti su carta di credito o debito: termini di disconoscimento, prova SCA e ricorso ABF.",
        "keywords": ["clonazione carta di credito rimborso", "addebiti non autorizzati carta", "disconoscimento operazioni carta psd2", "ricorso abf carta clonata"],
        "norme": ["Art. 7 D.Lgs. 11/2010", "Art. 10 D.Lgs. 11/2010", "Art. 11 D.Lgs. 11/2010"],
        "scenario": "Sull'estratto conto compaiono pagamenti ripetuti verso esercenti esteri o piattaforme digitali mai effettuati dal titolare, spesso senza richiesta di autenticazione forte.",
        "rischio": "La banca puo' tentare di respingere il rimborso invocando una presunta negligenza nella custodia del PIN o ritardi nel disconoscimento.",
        "protocollo": [
            "Bloccare subito la carta tramite numero verde dedicato e conservare il codice identificativo del blocco.",
            "Compilare e inviare il modulo di disconoscimento formale allegando la denuncia querela alle autorita' competenti.",
            "Richiedere alla banca i log tecnici completi dell'autenticazione forte (3D Secure / SCA) per ogni singola operazione contestata.",
            "Se il rimborso non arriva o e' parziale, proporre reclamo PEC e successivo ricorso ABF contestando la carenza di prova tecnica della banca."
        ],
        "prove": ["Estratto conto e lista movimenti", "Codice blocco carta", "Denuncia alle forze dell'ordine", "Eventuali alert SMS o app ricevuti"],
        "errori": ["Attendere la chiusura dell'estratto conto mensile prima di bloccare la carta", "Accettare un rimborso parziale con franchigie non dovute per legge", "Non conservare la prova dell'invio del reclamo PEC"]
    },
    {
        "cod": "CYB-75", "slug": "apertura-finanziamento-prestito-online-furto-identita",
        "cat": "truffe-banche", "cat_lbl": "Truffe & Banche", "pilastro": "truffe-online-phishing-sim-swap-banche",
        "titolo": "Finanziamento o prestito online aperto da ignoti con furto d'identita'",
        "seo_title": "Prestito Online con Furto d'Identita': Cancellazione CRIF e Difesa",
        "desc": "Difesa urgente contro finanziamenti fraudolenti accesi a proprio nome con documenti rubati o SPID clonato: disconoscimento, blocco rate e cancellazione CRIF/CTC.",
        "keywords": ["prestito online furto identita", "cancellazione crif truffa", "finanziamento mai richiesto difesa", "art 494 cp furto identita"],
        "norme": ["Art. 494 c.p.", "Art. 640 c.p.", "Art. 17 GDPR", "Codice di condotta SIC (CRIF/CTC)"],
        "scenario": "Un cittadino scopre tramite una lettera di recupero crediti o una visura CRIF che una finanziaria ha erogato un prestito a suo nome usando una copia del documento trafugata.",
        "rischio": "Segnalazione a sofferenza nelle banche dati creditizie (CRIF, Experian, CTC), blocco dell'accesso al credito e possibili decreti ingiuntivi.",
        "protocollo": [
            "Richiedere subito visura integrale a CRIF, Experian, CTC e Centrale Rischi Banca d'Italia per censire tutti i rapporti anomali.",
            "Presentare querela per sostituzione di persona e truffa, allegando la prova della sottrazione documentale o dell'estraneita' all'IBAN beneficiario.",
            "Notificare via PEC alla finanziaria la diffida di disconoscimento del contratto, blocco di ogni addebito e cancellazione immediata dai SIC ex art. 17 GDPR.",
            "In caso di inerzia, agire d'urgenza avanti all'ABF, al Garante Privacy o con ricorso cautelare ex art. 700 c.p.c."
        ],
        "prove": ["Visure SIC aggiornate", "Copia del contratto disconosciuto chiesta ex art. 119 TUB", "Denuncia querela", "Diffide PEC a finanziaria e SIC"],
        "errori": ["Pagare anche una sola rata per evitare la segnalazione (rischia di valere come riconoscimento)", "Non richiedere copia integrale del fascicolo istruttorio ex art. 119 TUB", "Trascurare il controllo di altri finanziamenti aperti in parallelo"]
    },
    {
        "cod": "CYB-76", "slug": "bonifico-istantaneo-fraudolento-spoofing-numero-banca",
        "cat": "truffe-banche", "cat_lbl": "Truffe & Banche", "pilastro": "truffe-online-phishing-sim-swap-banche",
        "titolo": "Bonifico istantaneo eseguito dopo chiamata con numero spoofato della banca",
        "seo_title": "Truffa Bonifico Istantaneo con Numero Banca Spoofato: Rimborso ABF",
        "desc": "Quando il truffatore chiama dallo stesso numero ufficiale della banca (caller ID spoofing): tutela PSD2, orientamenti ABF e responsabilita' degli intermediari.",
        "keywords": ["caller id spoofing banca", "truffa bonifico istantaneo rimborso", "chiamata finto operatore banca", "abf spoofing telefonico"],
        "norme": ["Art. 10 D.Lgs. 11/2010", "Art. 12 D.Lgs. 11/2010", "Art. 1176 comma 2 c.c."],
        "scenario": "Un cliente riceve una chiamata proveniente apparentemente dal numero verde ufficiale della propria banca e un SMS inserito nella stessa chat autentica dell'istituto, venendo indotto a confermare un'operazione.",
        "rischio": "La banca eccepisce l'autorizzazione formale dell'operazione o la colpa grave del cliente per negare il rimborso.",
        "protocollo": [
            "Documentare immediatamente la cronologia chiamate e lo screenshot della chat SMS in cui il messaggio truffaldino si e' accodato a quelli reali della banca.",
            "Presentare denuncia querela dettagliando la sofisticazione tecnica dello spoofing telefonico e dell'SMS spoofing.",
            "Inviare reclamo PEC circostanziato evidenziando l'assenza di colpa grave e l'inadeguatezza dei sistemi antifrode bancari su importi anomali.",
            "Proporre ricorso ABF o azione giudiziaria allegando l'intera prova tecnica della frode sofisticata."
        ],
        "prove": ["Screenshot registro chiamate con numero ufficiale banca", "Screenshot thread SMS autentico contaminato", "Contabile bonifico istantaneo", "Denuncia e reclamo PEC"],
        "errori": ["Cancellare la chat SMS o il registro chiamate", "Ammettere genericamente di aver autorizzato il pagamento senza spiegare l'inganno tecnico", "Far decorrere inutilmente i termini di reclamo"]
    },
    {
        "cod": "CYB-77", "slug": "truffa-pos-virtuale-ecommerce-falso-storno-rimborso",
        "cat": "truffe-banche", "cat_lbl": "Truffe & Banche", "pilastro": "truffe-online-phishing-sim-swap-banche",
        "titolo": "Truffa su e-commerce o mercatini online con falso link di accredito",
        "seo_title": "Truffa Link Accredito su Marketplace: Difesa e Recupero Somme",
        "desc": "Come reagire alla truffa del falso corriere o falso link di incasso su piattaforme di compravendita: blocco carta, querela e disconoscimento.",
        "keywords": ["truffa falso link accredito", "truffa vinted subito corriere", "recupero soldi link phishing carta"],
        "norme": ["Art. 640 c.p.", "Art. 640-ter c.p.", "Art. 10 D.Lgs. 11/2010"],
        "scenario": "Un venditore su una piattaforma di annunci riceve un link contraffatto che imita il corriere o il marketplace per accreditare il prezzo, ma in realta' addebita la carta inserita.",
        "rischio": "Addebiti multipli in valuta estera o trasferimenti su carte prepagate estere non immediatamente stornabili.",
        "protocollo": [
            "Bloccare subito la carta e cambiare le credenziali di accesso all'home banking e alla piattaforma di annunci.",
            "Salvare l'URL esatto del link truffaldino, la chat con il finto acquirente e la ricevuta degli addebiti.",
            "Depositare denuncia querela e inviare formale disconoscimento alla banca verificando la regolarita' della procedura SCA.",
            "Valutare il reclamo ABF qualora la banca abbia autorizzato transazioni anomale prive di avvisi chiari sull'addebito."
        ],
        "prove": ["Chat completa sul marketplace", "URL e screenshot pagina clone", "Estratto movimenti e notifiche app", "Denuncia querela"],
        "errori": ["Seguire ulteriori istruzioni del truffatore per presunti storni", "Non segnalare l'account truffaldino alla piattaforma per preservare i log", "Rinunciare al disconoscimento senza far verificare i log SCA"]
    },
    {
        "cod": "CYB-78", "slug": "blocco-ingiustificato-conto-corrente-fintech-revolut-paypal",
        "cat": "truffe-banche", "cat_lbl": "Truffe & Banche", "pilastro": "truffe-online-phishing-sim-swap-banche",
        "titolo": "Blocco improvviso di conto fintech, PayPal o wallet con fondi congelati",
        "seo_title": "Conto Fintech o PayPal Bloccato: Diffida Legale e Sblocco Fondi",
        "desc": "Tutela legale per privati e aziende contro il blocco prolungato di conti fintech o processori di pagamento: diffida, accesso ai dati GDPR e azione di sblocco.",
        "keywords": ["conto paypal bloccato avvocato", "conto fintech bloccato fondi", "sblocco conto corrente online diffida"],
        "norme": ["Art. 1175 e 1375 c.c.", "Art. 126-septies TUB", "Art. 15 GDPR"],
        "scenario": "Un'impresa o un professionista subisce il congelamento improvviso del conto fintech o del gateway di pagamento e-commerce per controlli automatici privi di motivazione chiara.",
        "rischio": "Crisi di liquidita' immediata, impossibilita' di pagare fornitori e imposte e trattenuta arbitraria delle somme per mesi.",
        "protocollo": [
            "Raccogliere subito la documentazione di provenienza lecita dei fondi (fatture, contratti, estratti conto, documenti KYC).",
            "Inviare formale diffida via PEC all'intermediario chiedendo la motivazione specifica del blocco e lo svincolo immediato delle somme.",
            "Contestualmente esercitare il diritto di accesso ex art. 15 GDPR rispetto alle decisioni automatizzate che hanno generato la limitazione.",
            "In mancanza di sblocco tempestivo, attivare il ricorso ABF o il ricorso d'urgenza ex art. 700 c.p.c. per il danno grave e irreparabile."
        ],
        "prove": ["Contratti e fatture a giustificazione dei flussi", "Screenshot limitazione account e ticket assistenza", "PEC di diffida e messa in mora", "Prova del pregiudizio di liquidita'"],
        "errori": ["Aprire nuovi account duplicati per aggirare il blocco (aggrava la sospensione)", "Limitarsi a chat automatiche con bot senza diffida legale PEC", "Non documentare l'urgenza economica per un eventuale ricorso cautelare"]
    },

    # ═══════════════════ SPID, PEC, IDENTITA' DIGITALE & PA (79-86) ═══════════════════
    {
        "cod": "CYB-79", "slug": "violazione-spid-attivazione-abusiva-identita-digitale",
        "cat": "penale-cyber", "cat_lbl": "Reati Informatici", "pilastro": "reati-informatici-difesa-penale",
        "titolo": "Attivazione abusiva di un secondo SPID a proprio nome",
        "seo_title": "Furto Identita' SPID: Revoca, Denuncia e Risarcimento",
        "desc": "Come intervenire se terzi attivano un'identita' SPID abusiva a tuo nome per deviare rimborsi INPS, bonus o aprire conti: revoca AgID, querela e risarcimento.",
        "keywords": ["spid clonato cosa fare", "attivazione abusiva spid", "furto identita spid inps", "responsabilita identity provider spid"],
        "norme": ["Art. 494 c.p.", "Art. 615-ter c.p.", "Art. 640-ter c.p.", "Art. 82 GDPR"],
        "scenario": "Un cittadino scopre che ignoti hanno creato un secondo SPID presso un altro Identity Provider usando documenti contraffatti, modificando l'IBAN su INPS o Agenzia delle Entrate.",
        "rischio": "Deviazione di pensioni, stipendi, rimborsi fiscali e sottoscrizione fraudolenta di contratti o finanziamenti.",
        "protocollo": [
            "Contattare immediatamente l'Identity Provider emittente per ottenere la sospensione e revoca d'urgenza dello SPID abusivo.",
            "Verificare subito gli accessi e gli IBAN registrati sui portali INPS, NoiPA, Agenzia delle Entrate e fascicolo sanitario.",
            "Presentare querela alla Polizia Postale chiedendo il sequestro dei log di registrazione e identificazione dell'Identity Provider.",
            "Valutare l'azione risarcitoria verso l'Identity Provider per omessa verifica rigorosa dell'identita' in fase di rilascio."
        ],
        "prove": ["Email o SMS di attivazione SPID non richiesta", "Log accessi portali PA", "Conferma revoca Identity Provider", "Denuncia querela"],
        "errori": ["Non controllare gli IBAN su INPS e Agenzia delle Entrate dopo la revoca", "Dimenticare di segnalare l'accaduto ad AgID", "Non chiedere copia del dossier di identificazione usato per emettere lo SPID falso"]
    },
    {
        "cod": "CYB-80", "slug": "accesso-abusivo-casella-pec-aziendale-professionale",
        "cat": "penale-cyber", "cat_lbl": "Reati Informatici", "pilastro": "reati-informatici-difesa-penale",
        "titolo": "Accesso abusivo alla casella PEC aziendale o di uno studio professionale",
        "seo_title": "Violazione Casella PEC Aziendale: Prove, Denuncia e Garante",
        "desc": "Gestione legale della compromissione di una casella PEC: conservazione log di accesso del gestore, denuncia ex art. 615-ter e 616 c.p., data breach GDPR.",
        "keywords": ["accesso abusivo pec", "casella pec hackerata", "violazione corrispondenza pec art 616 cp", "data breach casella pec"],
        "norme": ["Art. 615-ter c.p.", "Art. 616 c.p.", "Art. 33 GDPR"],
        "scenario": "Un'azienda o un professionista rileva accessi da IP esteri o la cancellazione/invio di messaggi nella propria casella PEC legale, contenente notifiche giudiziarie e atti riservati.",
        "rischio": "Sottrazione di atti giudiziari, manipolazione di notifiche legali, frodi verso clienti e violazione di dati personali.",
        "protocollo": [
            "Cambiare immediatamente password, abilitare 2FA sulla PEC e verificare l'assenza di regole di inoltro o filtri nascosti.",
            "Richiedere subito al gestore PEC la conservazione certificata dei log di accesso, IP e dispositivi degli ultimi mesi.",
            "Valutare entro 72 ore la notifica di data breach al Garante Privacy per i dati personali contenuti nei messaggi esposti.",
            "Presentare querela per accesso abusivo e violazione di corrispondenza informatica chiedendo l'acquisizione dei log."
        ],
        "prove": ["Log accessi e IP forniti dal gestore PEC", "Messaggi inviati o eliminati abusivamente", "Screenshot regole di inoltro trovate", "Ricevute di cambio credenziali"],
        "errori": ["Cambiare gestore chiudendo la vecchia casella prima di aver estratto i log", "Non avvisare i clienti se dalla PEC sono partiti messaggi contraffatti", "Ignorare la verifica delle notifiche giudiziarie eventualmente spostate nel cestino"]
    },
    {
        "cod": "CYB-81", "slug": "falsa-firma-digitale-disconoscimento-documento-p7m",
        "cat": "penale-cyber", "cat_lbl": "Reati Informatici", "pilastro": "ex-dipendenti-sottrazione-dati-segreti-aziendali",
        "titolo": "Uso abusivo di firma digitale o dispositivo CNS e disconoscimento file .p7m",
        "seo_title": "Uso Abusivo Firma Digitale: Disconoscimento e Querela di Falso",
        "desc": "Come contestare un documento firmato digitalmente a propria insaputa: onere della prova art. 20 CAD, revoca certificato, denuncia penale e querela di falso.",
        "keywords": ["disconoscimento firma digitale", "uso abusivo token firma digitale", "art 20 cad firma qualificata", "querela di falso documento informatico"],
        "norme": ["Art. 20 D.Lgs. 82/2005 (CAD)", "Art. 21 CAD", "Art. 491-bis c.p.", "Art. 221 c.p.c."],
        "scenario": "Un amministratore o un privato scopre un contratto, una fideiussione o una delibera sottoscritta con la propria firma digitale remota o smart card in modo abusivo.",
        "rischio": "Il documento con firma qualificata si presume riconducibile al titolare salvo prova contraria rigorosa: l'inerzia consolida obbligazioni gravissime.",
        "protocollo": [
            "Revocare immediatamente il certificato di firma digitale presso il prestatore qualificato (QTSP) annotando l'ora esatta.",
            "Richiedere al certificatore i log integrali di emissione OTP, IP di firma e timestamp della sottoscrizione contestata.",
            "Presentare querela penale per falso informatico e accesso abusivo per acquisire gli elementi tecnici sull'autore materiale.",
            "Proporre tempestivamente l'azione civile di disconoscimento o querela di falso allegando perizia informatica forense."
        ],
        "prove": ["File originale .p7m o PAdES contestato", "Log QTSP su OTP e indirizzo IP", "Certificato di revoca firma digitale", "Prova dell'impossibilita' fisica o tecnica del titolare"],
        "errori": ["Limitarsi a una contestazione generica senza vincere la presunzione legale dell'art. 20 CAD", "Non revocare subito il certificato compromesso", "Dimenticare di conservare i tabulati del telefono associato agli OTP"]
    },
    {
        "cod": "CYB-82", "slug": "attacco-informatico-fornitore-pubblica-amministrazione-acn",
        "cat": "ransomware-nis2", "cat_lbl": "Ransomware & NIS2", "pilastro": "direttiva-nis2-acn-legge-90-2024",
        "titolo": "Incidente cyber presso un fornitore IT della Pubblica Amministrazione",
        "seo_title": "Incidente Cyber Fornitore PA: Obblighi ACN, NIS2 e Contratti",
        "desc": "Protocollo legale per software house e fornitori PA colpiti da incidente informatico: notifiche NIS2/ACN, L. 90/2024, gestione penali contrattuali e Garante.",
        "keywords": ["incidente cyber fornitore pa", "obblighi acn fornitori pubblica amministrazione", "legge 90 2024 notifica 24 ore", "nis2 supply chain pa"],
        "norme": ["D.Lgs. 138/2024 (NIS2)", "Art. 1 L. 90/2024", "Art. 28 e 33 GDPR"],
        "scenario": "Un fornitore di servizi cloud o applicativi per enti pubblici subisce un'intrusione che rischia di propagarsi agli enti clienti.",
        "rischio": "Doppia esposizione: obblighi stringenti di notifica verso gli enti e ACN in 24 ore, rischio risoluzione contrattuale, penali e responsabilita' da data breach.",
        "protocollo": [
            "Isolare subito i tenant degli enti pubblici e attivare il team di incident response con tracciamento cronologico rigoroso.",
            "Inviare la pre-notifica tempestiva agli enti clienti (per consentire loro il rispetto delle 24 ore verso CSIRT Italia) e ad ACN se soggetto NIS2.",
            "Coordinare le comunicazioni tecniche per evitare dichiarazioni contraddittorie tra ACN, Garante Privacy e stazioni appaltanti.",
            "Documentare tutte le misure di sicurezza preesistenti (certificazioni ISO 27001 / ACN Cloud) per limitare penali e responsabilita' civile."
        ],
        "prove": ["Cronologia scoperta e contenimento", "Certificazioni sicurezza e audit pre-incidente", "Comunicazioni ufficiali agli enti clienti", "Contratti di appalto e DPA art. 28"],
        "errori": ["Tardare ad avvisare l'ente pubblico facendogli sforare il termine di 24 ore", "Diffondere ipotesi tecniche non confermate prima dell'analisi forense", "Non verificare la copertura della polizza cyber per responsabilita' verso terzi"]
    },
    {
        "cod": "CYB-83", "slug": "mancata-registrazione-portale-acn-nis2-sanzioni",
        "cat": "ransomware-nis2", "cat_lbl": "Ransomware & NIS2", "pilastro": "direttiva-nis2-acn-legge-90-2024",
        "titolo": "Omessa registrazione sul portale ACN per aziende soggette a NIS2",
        "seo_title": "Omessa Registrazione Portale ACN NIS2: Sanzioni e Rimedio",
        "desc": "Cosa rischia un'impresa che rientra nel D.Lgs. 138/2024 e non si e' registrata sulla piattaforma ACN: regolarizzazione, difesa sanzionatoria e responsabilita' CdA.",
        "keywords": ["mancata registrazione acn nis2", "sanzioni acn dlgs 138 2024", "portale acn soggetti essenziali importanti", "responsabilita amministratori nis2"],
        "norme": ["Art. 7 D.Lgs. 138/2024", "Art. 23 D.Lgs. 138/2024", "Art. 38 D.Lgs. 138/2024"],
        "scenario": "Un'azienda media o grande in un settore NIS2 scopre di non aver completato la registrazione o l'aggiornamento annuale sulla piattaforma dell'Agenzia per la Cybersicurezza Nazionale.",
        "rischio": "Sanzioni amministrative specifiche fino allo 0,1% del fatturato mondiale annuo, ispezioni ACN e responsabilita' diretta degli organi di amministrazione.",
        "protocollo": [
            "Eseguire subito la verifica giuridica di applicabilita' (settore Allegati I/II, soglie dimensionali, imprese collegate).",
            "Nominare formalmente il Punto di Contatto NIS2 e procedere senza indugio alla regolarizzazione sulla piattaforma ACN.",
            "Far deliberare dal Consiglio di Amministrazione il piano di adeguamento alle misure di sicurezza e formazione obbligatoria.",
            "In caso di contestazione ACN, predisporre memoria difensiva valorizzando la regolarizzazione spontanea e le misure gia' adottate."
        ],
        "prove": ["Visura camerale e bilanci per calcolo soglie", "Delibera CdA nomina Punto di Contatto", "Ricevuta registrazione portale ACN", "Gap analysis e roadmap tecnica"],
        "errori": ["Ignorare la normativa ritenendo erroneamente di essere esclusi per dimensioni", "Non considerare le imprese collegate nel calcolo del fatturato e dipendenti", "Lasciare il CdA privo di delibere e formazione documentata"]
    },
    {
        "cod": "CYB-84", "slug": "violazione-fascicolo-sanitario-elettronico-accesso-indebito",
        "cat": "data-breach", "cat_lbl": "Data Breach & GDPR", "pilastro": "data-breach-garante-privacy",
        "titolo": "Accesso indebito al Fascicolo Sanitario Elettronico o a cartelle ospedaliere",
        "seo_title": "Accesso Abusivo Fascicolo Sanitario: Tutela Paziente e Azienda",
        "desc": "Difesa del paziente vittima di consultazione abusiva dei propri dati sanitari e protocollo per strutture sanitarie: art. 615-ter c.p., Garante Privacy e risarcimento.",
        "keywords": ["accesso abusivo fascicolo sanitario", "violazione privacy cartella clinica", "risarcimento dati sanitari art 82 gdpr"],
        "norme": ["Art. 9 GDPR", "Art. 82 GDPR", "Art. 615-ter c.p.", "Art. 167 D.Lgs. 196/2003"],
        "scenario": "Un operatore sanitario o un terzo consulta senza motivo di cura i referti clinici di un paziente accedendo al Fascicolo Sanitario Elettronico o al gestionale ospedaliero.",
        "rischio": "Grave lesione della riservatezza medica per il paziente, reato penale di accesso abusivo aggravato per l'operatore e pesante sanzione GDPR per la struttura.",
        "protocollo": [
            "Per il paziente: richiedere subito all'ASL o alla Regione l'estratto completo dei log di accesso al proprio Fascicolo Sanitario.",
            "Presentare querela per accesso abusivo a sistema informatico e reclamo al Garante Privacy chiedendo l'accertamento dell'illecito.",
            "Per la struttura sanitaria: sospendere le credenziali coinvolte, avviare audit degli accessi e valutare notifica al Garante entro 72 ore.",
            "Quantificare il danno non patrimoniale risarcibile ai sensi dell'art. 82 GDPR."
        ],
        "prove": ["Log di tracciamento accessi FSE con codice operatore e data", "Assenza di rapporto di cura con l'operatore", "Reclamo al Garante e querela", "Documentazione disciplinare interna"],
        "errori": ["Non richiedere l'estratto dei log prima della scadenza del periodo di conservazione", "Confondere la responsabilita' disciplinare interna con quella penale e GDPR", "Omettere la comunicazione al paziente in caso di rischio elevato"]
    },
    {
        "cod": "CYB-85", "slug": "violazione-privacy-condominio-telecamere-chat-morosi",
        "cat": "data-breach", "cat_lbl": "Data Breach & GDPR", "pilastro": "compliance-gdpr-dpo-privacy",
        "titolo": "Violazione privacy in condominio: telecamere abusive e dati morosi in bacheca o chat",
        "seo_title": "Privacy Condominio: Telecamere Abusive e Morosi in Chat WhatsApp",
        "desc": "Tutela legale contro telecamere che riprendono spazi privati o diffusione dei nomi dei condomini morosi in bacheca o su WhatsApp: diffida, Garante e risarcimento.",
        "keywords": ["privacy condominio telecamere", "condomini morosi chat whatsapp privacy", "diffida amministratore condominio gdpr"],
        "norme": ["Art. 5 e 6 GDPR", "Art. 1122-ter c.c.", "Art. 615-bis c.p.", "Art. 82 GDPR"],
        "scenario": "Un vicino installa una telecamera che inquadra l'ingresso altrui oppure l'amministratore pubblica in bacheca o nel gruppo WhatsApp l'elenco dei condomini morosi.",
        "rischio": "Lesione della riservatezza domestica (fino al reato di interferenze illecite ex art. 615-bis c.p.) e responsabilita' risarcitoria del condominio o del singolo.",
        "protocollo": [
            "Documentare con foto, video o screenshot l'angolo di ripresa della telecamera o i messaggi diffusi nelle chat/bacheche.",
            "Inviare diffida formale via PEC all'amministratore o al condomino intimando la rimozione immediata o l'oscuramento dell'area privata.",
            "Verificare la presenza di valida delibera assembleare (art. 1122-ter c.c.) e di corretta cartellonistica informativa.",
            "In caso di mancato adeguamento, proporre reclamo al Garante Privacy, azione civile inibitoria/risarcitoria o querela ex art. 615-bis c.p."
        ],
        "prove": ["Foto posizionamento telecamera e area ripresa", "Screenshot chat WhatsApp o bacheca condominiale", "Verbali assembleari", "Diffida PEC con termine di adempimento"],
        "errori": ["Manomettere o oscurare fisicamente la telecamera altrui (integra esercizio arbitrario o danneggiamento)", "Agire senza aver prima documentato la violazione con data certa", "Confondere il diritto del singolo condomino di sapere i conti con la diffusione a terzi"]
    },
    {
        "cod": "CYB-86", "slug": "web-scraping-abusivo-banca-dati-aziendale-concorrenza-sleale",
        "cat": "compliance-231-ai", "cat_lbl": "231, DPO & AI Act", "pilastro": "contratti-it-cloud-saas-ai-act",
        "titolo": "Web scraping abusivo di listini, cataloghi o banche dati da parte di concorrenti",
        "seo_title": "Web Scraping Abusivo e Furto Banche Dati: Tutela Legale",
        "desc": "Come bloccare bot e concorrenti che copiano automaticamente cataloghi, prezzi o database online: tutela banca dati sui generis, concorrenza sleale e GDPR.",
        "keywords": ["web scraping illegale italia", "tutela banca dati sui generis", "concorrenza sleale scraping", "gdpr web scraping"],
        "norme": ["Art. 102-bis L. 633/1941", "Art. 2598 c.c.", "Art. 615-ter c.p.", "Art. 6 GDPR"],
        "scenario": "Un concorrente o una societa' di data broker utilizza script automatici per estrarre in massa il catalogo prodotti, i prezzi dinamici o i profili utenti di un portale aziendale.",
        "rischio": "Svuotamento dell'investimento aziendale, perdita di vantaggio competitivo, sovraccarico dei server e raccolta illecita di dati personali.",
        "protocollo": [
            "Raccogliere i log del Web Application Firewall (WAF), gli IP sorgente, gli User-Agent e i picchi di richieste anomale.",
            "Verificare i Termini di Servizio, il file robots.txt e l'eventuale elusione di misure tecniche di protezione o login.",
            "Inviare diffida legale di cessazione immediata e cancellazione dei dati estratti con riserva di azione cautelare.",
            "Promuovere ricorso cautelare d'urgenza avanti alla Sezione Specializzata Impresa per violazione del diritto sui generis e concorrenza sleale."
        ],
        "prove": ["Log WAF/CDN e volumi di estrazione", "Copia forense delle pagine copiate sul sito concorrente", "Termini d'uso e prove dell'investimento nella banca dati", "Diffida PEC"],
        "errori": ["Bloccare gli IP senza prima acquisire i log in forma forense", "Non avere clausole anti-scraping chiare nei Termini di Servizio", "Ignorare i profili GDPR se i dati estratti riguardano persone fisiche"]
    },

    # ═══════════════════ AI, DEEPFAKE, REPUTAZIONE & SOCIAL (87-95) ═══════════════════
    {
        "cod": "CYB-87", "slug": "truffa-deepfake-vocale-clonazione-voce-amministratore",
        "cat": "compliance-231-ai", "cat_lbl": "231, DPO & AI Act", "pilastro": "contratti-it-cloud-saas-ai-act",
        "titolo": "Truffa con deepfake vocale o video (clonazione voce del CEO o di un familiare)",
        "seo_title": "Truffa Deepfake Vocale e Clonazione Voce AI: Difesa Legale",
        "desc": "Come reagire a una truffa realizzata clonando con l'AI la voce dell'amministratore o di un familiare: querela, recall bancario, prove forensi e tutela ex L. 132/2025 e AI Act.",
        "keywords": ["truffa deepfake vocale", "clonazione voce ai truffa", "deepfake ceo fraud", "difesa legale deepfake"],
        "norme": ["Art. 640 c.p.", "Art. 494 c.p.", "Art. 612-quater c.p. (se intimo)", "Reg. UE 2024/1689 (AI Act)"],
        "scenario": "Un dipendente amministrativo o un familiare riceve una telefonata o una videochiamata generata con intelligenza artificiale che riproduce fedelmente voce e volto del titolare per ordinare un bonifico urgente.",
        "rischio": "Trasferimento immediato di somme ingenti su conti esteri e grave trauma psicologico o danno d'immagine.",
        "protocollo": [
            "Attivare immediatamente la procedura di recall del bonifico presso la banca e allertare la Polizia Postale nelle prime ore.",
            "Conservare ogni registrazione vocale, messaggio WhatsApp, metadato della chiamata e file audio/video originale.",
            "Presentare querela dettagliata chiedendo il sequestro d'urgenza dell'IBAN beneficiario e l'analisi forense dei file sintetici.",
            "In azienda, aggiornare subito le procedure di verifica a doppio canale (call-back su numero certificato) per i pagamenti."
        ],
        "prove": ["File audio/video originali con metadati", "Contabile bonifico e richiesta recall", "Log chiamate e chat", "Eventuale perizia acustica/forense"],
        "errori": ["Inoltrare i file audio ricomprimendoli e perdendo i metadati originali", "Attendere giorni prima di chiedere il blocco del bonifico", "Non verificare la responsabilita' interna o le procedure 231/antifrode"]
    },
    {
        "cod": "CYB-88", "slug": "diffamazione-recensioni-false-google-trustpilot-azienda",
        "cat": "reputazione-social", "cat_lbl": "Reputazione & Social", "pilastro": "reputazione-online-deepfake-revenge-porn",
        "titolo": "Campagna di recensioni false e diffamatorie su Google Maps o Trustpilot",
        "seo_title": "Recensioni False Google e Trustpilot: Rimozione e Risarcimento",
        "desc": "Protocollo operativo per rimuovere recensioni false o di concorrenti sleali su Google e Trustpilot: copia forense, diffida DSA, querela ex art. 595 c.p. e risarcimento.",
        "keywords": ["rimuovere recensioni false google", "diffamazione recensioni trustpilot", "querela recensione falsa", "risarcimento recensioni false azienda"],
        "norme": ["Art. 595 comma 3 c.p.", "Art. 2598 c.c.", "Art. 16 Reg. UE 2022/2065 (DSA)", "Art. 2043 c.c."],
        "scenario": "Un'impresa, uno studio o un ristorante subisce un attacco coordinato di recensioni a una stella pubblicate da profili falsi o da ex dipendenti/concorrenti.",
        "rischio": "Crollo immediato del punteggio medio su Google, perdita diretta di clienti e danno reputazionale duraturo.",
        "protocollo": [
            "Cristallizzare tutte le recensioni con acquisizione forense certificata prima che vengano modificate o eliminate.",
            "Inviare segnalazione legale motivata alle piattaforme richiamando la violazione delle policy e il Regolamento DSA.",
            "Depositare querela per diffamazione aggravata chiedendo alla Procura l'identificazione dei titolari degli account tramite IP e dati di registrazione.",
            "Avviare azione civile di rimozione cautelare e risarcimento del danno patrimoniale e all'immagine aziendale."
        ],
        "prove": ["Acquisizione forense certificata delle recensioni e profili", "Assenza di riscontro fiscale/prenotazione del recensore", "Calo prenotazioni o fatturato", "Segnalazioni inviate a Google/Trustpilot"],
        "errori": ["Rispondere pubblicamente con insulti o rivelando dati personali del cliente", "Fare solo screenshot semplici senza certificazione forense", "Lasciare scadere i 3 mesi per la querela penale"]
    },
    {
        "cod": "CYB-89", "slug": "diffamazione-video-tiktok-instagram-reels-virale",
        "cat": "reputazione-social", "cat_lbl": "Reputazione & Social", "pilastro": "reputazione-online-deepfake-revenge-porn",
        "titolo": "Diffamazione virale tramite video su TikTok, Instagram Reels o YouTube Shorts",
        "seo_title": "Diffamazione su TikTok e Instagram Reels: Rimozione Urgente",
        "desc": "Come bloccare un video diffamatorio virale su TikTok o Instagram: preservazione forense video, notice DSA, ricorso ex art. 700 c.p.c. e querela penale.",
        "keywords": ["diffamazione su tiktok", "rimozione video diffamatorio instagram", "querela tiktok avvocato", "art 700 cpc rimozione video"],
        "norme": ["Art. 595 comma 3 c.p.", "Art. 10 c.c.", "Art. 700 c.p.c.", "Reg. UE 2022/2065 (DSA)"],
        "scenario": "Un creator o un utente pubblica un video breve che accusa falsamente un professionista, un'azienda o un privato, generando migliaia di visualizzazioni e commenti offensivi.",
        "rischio": "La viralita' moltiplica il danno in poche ore e i video vengono spesso ricaricati da altri profili rendendo vani gli interventi tardivi.",
        "protocollo": [
            "Effettuare subito il salvataggio forense integrale del video, dell'audio, dell'URL, del profilo autore e dei commenti.",
            "Notificare una diffida legale immediata all'autore e una richiesta formale di rimozione (notice-and-action DSA) alla piattaforma.",
            "Se il video resta online, valutare un ricorso d'urgenza ex art. 700 c.p.c. per ottenere l'ordine giudiziale di rimozione.",
            "Presentare querela penale entro 3 mesi per diffamazione aggravata e valutare la richiesta di risarcimento danni."
        ],
        "prove": ["Copia forense del video con hash SHA-256", "Conteggio visualizzazioni, condivisioni e commenti", "Identificativo univoco URL e ID account", "Diffida PEC o raccomandata"],
        "errori": ["Aspettare che il video si spenga da solo mentre viene ricondiviso", "Pubblicare video di replica offensivi che espongono a controquerele", "Non salvare il video prima che l'autore lo cancelli dopo la diffida"]
    },
    {
        "cod": "CYB-90", "slug": "clonazione-profilo-social-azienda-truffa-follower",
        "cat": "reputazione-social", "cat_lbl": "Reputazione & Social", "pilastro": "reputazione-online-deepfake-revenge-porn",
        "titolo": "Clonazione di profilo Instagram, Facebook o LinkedIn aziendale per truffare clienti",
        "seo_title": "Profilo Social Aziendale Clonato: Rimozione e Tutela Legale",
        "desc": "Intervento rapido contro account clone che usano nome, logo e foto di un'azienda o professionista per adescare clienti: segnalazione IP/impersonation e denuncia.",
        "keywords": ["profilo instagram clonato azienda", "account falso linkedin difesa", "sostituzione di persona social art 494 cp"],
        "norme": ["Art. 494 c.p.", "Art. 20 Codice Proprieta' Industriale", "Art. 10 c.c."],
        "scenario": "Ignoti creano un profilo identico a quello di un'azienda o di un professionista contattando i follower per vendere falsi servizi o chiedere pagamenti.",
        "rischio": "Danno diretto ai clienti truffati, compromissione della fiducia nel marchio e rischio di segnalazioni ingiuste verso il profilo autentico.",
        "protocollo": [
            "Acquisire prova forense dell'account clone, dei messaggi inviati ai clienti e dell'uso indebito di marchio e fotografie.",
            "Avviare la procedura accelerata di rimozione per impersonation e violazione di marchio/copyright presso Meta o LinkedIn.",
            "Pubblicare un avviso ufficiale sui canali reali per proteggere i clienti senza diffondere dati riservati.",
            "Presentare denuncia per sostituzione di persona e tentata truffa."
        ],
        "prove": ["Acquisizione forense profilo clone e URL", "Screenshot messaggi truffaldini inviati ai follower", "Attestato registrazione marchio o titolarita' immagine", "Ticket segnalazione piattaforma"],
        "errori": ["Limitarsi alla segnalazione standard utente senza canale legale IP/impersonation", "Negoziare con chi gestisce l'account clone", "Non documentare i tentativi di truffa verso i clienti"]
    },
    {
        "cod": "CYB-91", "slug": "doxxing-pubblicazione-indirizzo-telefono-privato-online",
        "cat": "reputazione-social", "cat_lbl": "Reputazione & Social", "pilastro": "reputazione-online-deepfake-revenge-porn",
        "titolo": "Doxxing: pubblicazione online di indirizzo di casa, telefono o dati familiari",
        "seo_title": "Doxxing in Italia: Reato, Rimozione Immediata e Garante Privacy",
        "desc": "Come difendersi dal doxxing (diffusione online di dati privati per intimidire o esporre a molestie): intervento d'urgenza Garante, art. 167 Codice Privacy e art. 612-bis c.p.",
        "keywords": ["doxxing reato italia", "pubblicazione indirizzo casa online difesa", "art 167 codice privacy doxxing", "rimozione dati personali telegram"],
        "norme": ["Art. 167 D.Lgs. 196/2003", "Art. 612-bis c.p.", "Art. 17 GDPR"],
        "scenario": "Un soggetto pubblica su social, forum o canali Telegram l'indirizzo di abitazione, il numero personale o la scuola dei figli della vittima incitando molestie.",
        "rischio": "Pericolo concreto per l'incolumita' fisica, stalking digitale e replicazione incontrollata dei dati personali.",
        "protocollo": [
            "Acquisire subito copia forense dei post, dei canali Telegram e dei messaggi intimidatori.",
            "Attivare richieste urgenti di rimozione alle piattaforme e ai motori di ricerca (Google/Bing) per esposizione di dati personali sensibili.",
            "Presentare denuncia querela urgente alle forze dell'ordine segnalando l'eventuale rischio per la sicurezza personale (anche ai fini di misure cautelari o ammonimento).",
            "Depositare segnalazione d'urgenza al Garante Privacy ex art. 144-bis / art. 167 Codice Privacy."
        ],
        "prove": ["Acquisizione forense post e profili", "Screenshot commenti minatori o molestie ricevute", "Tabulati chiamate o messaggi molesti", "Richieste di rimozione inviate"],
        "errori": ["Rispondere pubblicamente alimentando l'attenzione sul post", "Attendere giorni prima di denunciare quando ci sono minacce all'incolumita'", "Dimenticare di richiedere la deindicizzazione dai motori di ricerca"]
    },
    {
        "cod": "CYB-92", "slug": "diritto-all-oblio-articoli-cronaca-giudiziaria-assoluzione",
        "cat": "reputazione-social", "cat_lbl": "Reputazione & Social", "pilastro": "reputazione-online-deepfake-revenge-porn",
        "titolo": "Diritto all'oblio e deindicizzazione di vecchi articoli dopo assoluzione o archiviazione",
        "seo_title": "Diritto all'Oblio dopo Assoluzione: Deindicizzazione Google",
        "desc": "Come ottenere la deindicizzazione da Google e l'aggiornamento o rimozione di articoli di cronaca giudiziaria dopo archiviazione o assoluzione (art. 64-ter disp. att. c.p.p. e art. 17 GDPR).",
        "keywords": ["diritto all oblio assoluzione", "deindicizzazione google articoli vecchi", "art 64-ter disp att cpp", "rimozione notizie archiviazione"],
        "norme": ["Art. 64-ter disp. att. c.p.p.", "Art. 17 GDPR", "Linee guida EDPB su deindicizzazione"],
        "scenario": "Digitando il nome di una persona o di un imprenditore su Google compaiono ancora in prima pagina articoli su un vecchio procedimento penale concluso con archiviazione o assoluzione.",
        "rischio": "Danno permanente alla reputazione personale, professionale e bancaria (controlli KYC e reputazionali).",
        "protocollo": [
            "Recuperare copia autentica del decreto di archiviazione o della sentenza di assoluzione definitiva.",
            "In caso di assoluzione/archiviazione, attivare l'istanza di deindicizzazione ex art. 64-ter disp. att. c.p.p. presso la cancelleria del giudice.",
            "Inviare contestualmente istanza formale di deindicizzazione ai motori di ricerca (Google, Bing) e richiesta di aggiornamento/anonimizzazione alle testate.",
            "In caso di rigetto, proporre reclamo al Garante Privacy o ricorso giudiziale ex art. 152 Codice Privacy."
        ],
        "prove": ["Provvedimento giudiziario definitivo (assoluzione/archiviazione)", "Elenco completo degli URL indicizzati", "Prove del pregiudizio lavorativo o personale", "Istanze PEC inviate"],
        "errori": ["Chiedere la cancellazione senza allegare il provvedimento definitivo", "Inviare richieste generiche prive di bilanciamento giuridico con il diritto di cronaca", "Dimenticare le testate locali che replicano la stessa notizia"]
    },
    {
        "cod": "CYB-93", "slug": "cyberbullismo-minori-oscuramento-rapido-legge-71-2017",
        "cat": "reputazione-social", "cat_lbl": "Reputazione & Social", "pilastro": "reputazione-online-deepfake-revenge-porn",
        "titolo": "Cyberbullismo contro minori: oscuramento rapido in 48 ore ex L. 71/2017",
        "seo_title": "Cyberbullismo Minori: Oscuramento 48 Ore Legge 71/2017",
        "desc": "Procedura d'urgenza per tutelare un minore vittima di cyberbullismo, insulti o foto rubate online: istanza al gestore in 24/48 ore, Garante Privacy e ammonimento Questore.",
        "keywords": ["cyberbullismo legge 71 2017", "oscuramento contenuti cyberbullismo 48 ore", "ammonimento questore cyberbullismo", "tutela minore social"],
        "norme": ["Art. 2 L. 71/2017", "Art. 7 L. 71/2017", "Art. 612-bis c.p."],
        "scenario": "Un minore subisce umiliazioni, diffusione di video o fotomontaggi denigratori in chat scolastiche o sui social network.",
        "rischio": "Rapida diffusione tra i coetanei con gravi ripercussioni psicologiche per il minore.",
        "protocollo": [
            "Preservare integralmente chat, profili, video e gruppi prima di bloccare gli account aggressori.",
            "Inviare subito l'istanza di oscuramento o rimozione al gestore del sito/social ai sensi dell'art. 2 L. 71/2017 (risposta entro 24 ore, rimozione entro 48 ore).",
            "In caso di mancata rimozione entro 48 ore, attivare l'intervento d'urgenza del Garante Privacy che provvede nelle successive 48 ore.",
            "Valutare con il legale la richiesta di ammonimento del Questore (art. 7 L. 71/2017) o la querela penale se sussistono reati gravi."
        ],
        "prove": ["Acquisizione forense chat e post", "Dati degli account e dei gruppi", "Istanza inviata al gestore con ricevuta", "Eventuali certificazioni mediche o scolastiche"],
        "errori": ["Cancellare la chat o il profilo del minore distruggendo le prove", "Affrontare personalmente i genitori degli altri minori con toni minacciosi", "Non attivare il canale dedicato al Garante dopo le 48 ore"]
    },
    {
        "cod": "CYB-94", "slug": "sextortion-ricatto-video-intimo-chat-online",
        "cat": "reputazione-social", "cat_lbl": "Reputazione & Social", "pilastro": "reputazione-online-deepfake-revenge-porn",
        "titolo": "Sextortion: ricatto online con minaccia di diffondere video o chat intime",
        "seo_title": "Sextortion e Ricatto Video Online: Cosa Fare Subito",
        "desc": "Protocollo immediato di difesa in caso di sextortion: perche' non pagare mai, conservazione prove, querela ex art. 629 e 612-ter c.p. e blocco diffusione.",
        "keywords": ["sextortion cosa fare", "ricatto video intimo online", "art 612-ter cp revenge porn", "denuncia estorsione sessuale online"],
        "norme": ["Art. 629 c.p.", "Art. 612-ter c.p.", "Art. 144-bis D.Lgs. 196/2003"],
        "scenario": "Un truffatore, dopo aver carpito un video o immagini intime in videochiamata, minaccia di inviarli ai contatti social o lavorativi della vittima se non paga denaro o criptovalute.",
        "rischio": "Pagare non ferma mai il ricatto ma genera richieste economiche crescenti; la diffusione illecita puo' danneggiare la vita privata e professionale.",
        "protocollo": [
            "Non pagare alcuna somma e non cedere al ricatto, interrompendo ogni trattativa ma senza cancellare le prove.",
            "Salvare immediatamente screenshot della chat, profili, numeri di telefono, richieste di pagamento e IBAN/wallet indicati.",
            "Impostare subito i propri profili social su privato e nascondere la lista amici/follower.",
            "Depositare denuncia querela alla Polizia Postale per estorsione e attivare la segnalazione preventiva al Garante Privacy ex art. 144-bis Codice Privacy."
        ],
        "prove": ["Chat integrali con le minacce", "Profili e numeri dell'estorsore", "Coordinate di pagamento richieste", "Eventuale codice hash dei file per blocco preventivo piattaforme"],
        "errori": ["Pagare sperando che il ricattatore cancelli il video", "Cancellare le conversazioni per vergogna impedendo le indagini", "Non mettere in sicurezza le liste contatti sui social"]
    },
    {
        "cod": "CYB-95", "slug": "uso-ai-generativa-azienda-fuga-dati-riservati-dipendenti",
        "cat": "compliance-231-ai", "cat_lbl": "231, DPO & AI Act", "pilastro": "contratti-it-cloud-saas-ai-act",
        "titolo": "Dipendenti che caricano dati clienti o segreti aziendali su AI pubbliche (Shadow AI)",
        "seo_title": "Shadow AI in Azienda: Rischi GDPR, AI Act e Policy Legale",
        "desc": "Come governare l'uso non autorizzato di strumenti di AI generativa in azienda: rischio data breach, perdita segreto industriale, policy aziendale e conformita' AI Act.",
        "keywords": ["shadow ai azienda gdpr", "policy intelligenza artificiale aziendale", "ai act obblighi azienda", "fuga dati chatgpt azienda"],
        "norme": ["Reg. UE 2024/1689 (AI Act)", "Art. 5 e 32 GDPR", "Art. 98-99 Codice Proprieta' Industriale"],
        "scenario": "Il personale utilizza versioni gratuite di chatbot AI caricando contratti riservati, codici sorgente o dati personali dei clienti che possono essere usati per l'addestramento del modello.",
        "rischio": "Violazione del GDPR per trasferimento illecito di dati, decadenza della tutela sui segreti commerciali e sanzioni AI Act per mancata alfabetizzazione AI (art. 4).",
        "protocollo": [
            "Mappare gli strumenti di AI effettivamente usati nei reparti e valutare se siano stati caricati dati personali o segreti industriali.",
            "Adottare una Policy AI aziendale vincolante che vieti l'uso di account gratuiti con dati riservati e definisca gli strumenti enterprise approvati.",
            "Sottoscrivere contratti DPA conformi (zero data retention / no training) con i fornitori AI selezionati ed eseguire una DPIA.",
            "Attivare la formazione obbligatoria di alfabetizzazione AI prevista dall'art. 4 dell'AI Act."
        ],
        "prove": ["Policy AI approvata e comunicata ai dipendenti", "Contratti enterprise AI con clausole no-training", "DPIA sui flussi AI", "Attestati di formazione AI literacy"],
        "errori": ["Vietare formalmente l'AI senza fornire strumenti aziendali sicuri", "Usare versioni consumer per elaborare atti sanitari, bancari o giudiziari", "Trascurare l'obbligo di alfabetizzazione AI gia' in vigore"]
    },

    # ═══════════════════ LAVORO, EX DIPENDENTI, SEGRETI & 231 (96-103) ═══════════════════
    {
        "cod": "CYB-96", "slug": "ex-dipendente-copia-portafoglio-clienti-segreti-industriali",
        "cat": "lavoro-forense", "cat_lbl": "Lavoro & Prove Digitali", "pilastro": "ex-dipendenti-sottrazione-dati-segreti-aziendali",
        "titolo": "Ex dipendente che copia il portafoglio clienti o il know-how prima delle dimissioni",
        "seo_title": "Furto Dati Clienti Ex Dipendente: Prove Forensi e Azione Legale",
        "desc": "Come agire quando un dipendente dimissionario scarica database clienti, preventivi o progetti su chiavetta USB o cloud personale: copia forense, art. 623 c.p. e sequestro civile.",
        "keywords": ["ex dipendente ruba clienti", "furto segreti industriali art 623 cp", "copia forense pc aziendale dipendente", "descrizione industriale art 129 cpi"],
        "norme": ["Art. 623 c.p.", "Art. 615-ter c.p.", "Art. 2105 c.c.", "Art. 98-99 e 129 CPI"],
        "scenario": "Nei giorni precedenti alle dimissioni, un commerciale o un tecnico scarica l'intero CRM clienti, listini riservati e disegni tecnici su un disco esterno o li inoltra alla mail privata.",
        "rischio": "Sviamento immediato della clientela verso un concorrente e perdita del vantaggio competitivo se le prove sul PC aziendale vengono alterate.",
        "protocollo": [
            "Non accendere ne' usare il PC riconsegnato dall'ex dipendente: affidarlo subito a un consulente forense per creare una copia bit-stream certificata.",
            "Estrarre i log del cloud aziendale, della posta e del CRM per documentare download massivi e inoltri esterni.",
            "Verificare la liceita' dei controlli aziendali ai sensi dell'art. 4 Statuto dei Lavoratori (controlli difensivi in senso stretto).",
            "Agire con ricorso cautelare di descrizione e inibitoria avanti alla Sezione Impresa e valutare la querela penale ex art. 623 e 615-ter c.p."
        ],
        "prove": ["Immagine forense certificata del PC aziendale", "Log USB, cloud ed email in uscita", "Policy IT aziendale e clausole di riservatezza", "Prova delle misure di segretezza adottate"],
        "errori": ["Far accedere il reparto IT interno al PC alterando date e metadati dei file", "Riassegnare subito il laptop a un altro dipendente sovrascrivendo le prove", "Effettuare controlli massivi generalizzati in violazione dell'art. 4 Statuto Lavoratori"]
    },
    {
        "cod": "CYB-97", "slug": "sabotaggio-informatico-cancellazione-file-ex-collaboratore",
        "cat": "penale-cyber", "cat_lbl": "Reati Informatici", "pilastro": "reati-informatici-difesa-penale",
        "titolo": "Sabotaggio informatico o cancellazione di archivi da parte di ex dipendente o fornitore IT",
        "seo_title": "Sabotaggio Informatico Ex Dipendente: Art. 635-bis c.p. e Difesa",
        "desc": "Tutela penale e civile in caso di cancellazione dolosa di database, siti web o backup da parte di ex collaboratori o fornitori IT: danneggiamento informatico e risarcimento.",
        "keywords": ["sabotaggio informatico ex dipendente", "cancellazione dati aziendali reato", "art 635-bis cp danneggiamento informatico", "fornitore it blocca sito web"],
        "norme": ["Art. 635-bis c.p.", "Art. 635-quater c.p.", "Art. 615-ter c.p.", "L. 90/2024"],
        "scenario": "A seguito di una lite contrattuale o di un licenziamento, un ex amministratore di sistema o un fornitore web cancella database, modifica le password o spegne il sito aziendale.",
        "rischio": "Blocco operativo immediato, perdita di fatturato e distruzione di dati storici essenziali.",
        "protocollo": [
            "Revocare ogni residuo accesso amministrativo, recuperare i backup offline e congelare i log di server, hosting e pannelli di controllo.",
            "Far certificare lo stato del danno e i log di cancellazione tramite perizia informatica forense.",
            "Inviare diffida immediata per la riconsegna di credenziali e domini e valutare un ricorso ex art. 700 c.p.c.",
            "Presentare querela penale per danneggiamento di informazioni e sistemi informatici (pene inasprite dalla L. 90/2024)."
        ],
        "prove": ["Log di eliminazione con IP e account utilizzato", "Contratti di lavoro o fornitura IT", "Stima documentata dei costi di ripristino e fermo aziendale", "Perizia informatica"],
        "errori": ["Reinstallare subito il server cancellando i log dell'intrusione", "Lasciare i domini aziendali intestati personalmente al fornitore IT", "Trattare il sabotaggio come un semplice inadempimento contrattuale"]
    },
    {
        "cod": "CYB-98", "slug": "controllo-email-dipendenti-art-4-statuto-lavoratori-garante",
        "cat": "lavoro-forense", "cat_lbl": "Lavoro & Prove Digitali", "pilastro": "compliance-gdpr-dpo-privacy",
        "titolo": "Controllo della posta elettronica aziendale e dei metadati email dei dipendenti",
        "seo_title": "Controllo Email Dipendenti: Art. 4 Statuto Lavoratori e Garante",
        "desc": "Come gestire legalmente email aziendali, metadati di posta e account di ex dipendenti secondo i provvedimenti del Garante Privacy e l'art. 4 Statuto dei Lavoratori.",
        "keywords": ["controllo email dipendenti art 4", "metadati email garante privacy", "account email ex dipendente gdpr", "inutilizzabilita prove controllo illecito"],
        "norme": ["Art. 4 L. 300/1970", "Art. 5 e 13 GDPR", "Provvedimento Garante su metadati email 2024"],
        "scenario": "Un'azienda conserva per mesi i metadati della posta elettronica o mantiene attiva la casella email di un dipendente cessato per controllare eventuali illeciti.",
        "rischio": "Sanzioni pesanti del Garante Privacy, responsabilita' penale ex art. 171 Codice Privacy e totale inutilizzabilita' delle prove raccolte in giudizio di licenziamento.",
        "protocollo": [
            "Verificare i tempi di conservazione dei metadati email sul server (limite ordinario di pochi giorni, estendibile solo con accordo sindacale o autorizzazione ITL).",
            "Alla cessazione del rapporto di lavoro, disattivare tempestivamente l'account nominativo impostando un risponditore automatico con indirizzo aziendale alternativo.",
            "Adottare e consegnare un disciplinare IT trasparente conforme all'art. 4 comma 3 Statuto dei Lavoratori e all'art. 13 GDPR.",
            "In caso di fondato sospetto di illecito, limitare l'accertamento ai soli controlli difensivi mirati e proporzionati successivi all'indizio."
        ],
        "prove": ["Disciplinare IT firmato per presa visione", "Configurazione tempi retention metadati", "Eventuale accordo sindacale o autorizzazione ITL", "Documentazione disattivazione account ex dipendenti"],
        "errori": ["Tenere aperta la casella dell'ex dipendente con inoltro automatico nascosto", "Conservare i log email per anni senza accordo sindacale", "Usare prove raccolte violando l'art. 4 per contestare un licenziamento"]
    },
    {
        "cod": "CYB-99", "slug": "videosorveglianza-aziendale-senza-accordo-sindacale-itl",
        "cat": "lavoro-forense", "cat_lbl": "Lavoro & Prove Digitali", "pilastro": "compliance-gdpr-dpo-privacy",
        "titolo": "Videosorveglianza in azienda senza accordo sindacale o autorizzazione Ispettorato",
        "seo_title": "Telecamere in Azienda senza Autorizzazione ITL: Sanzioni e Difesa",
        "desc": "Rischi penali e sanzioni GDPR per impianti di videosorveglianza aziendali non autorizzati ex art. 4 Statuto Lavoratori: regolarizzazione, difesa ispettiva e cartellonistica.",
        "keywords": ["telecamere azienda senza autorizzazione itl", "art 4 statuto lavoratori videosorveglianza", "sanzioni garante telecamere lavoro"],
        "norme": ["Art. 4 L. 300/1970", "Art. 171 D.Lgs. 196/2003", "Art. 38 L. 300/1970", "Linee guida EDPB 3/2019"],
        "scenario": "Durante un controllo dell'Ispettorato del Lavoro o della Guardia di Finanza emerge la presenza di telecamere attive (o anche solo installate) in luoghi di lavoro prive di autorizzazione.",
        "rischio": "Contravvenzione penale a carico del legale rappresentante, prescrizione obbligatoria, sanzione GDPR e divieto di utilizzo delle immagini.",
        "protocollo": [
            "Disattivare immediatamente l'impianto non autorizzato (non basta il consenso firmato dai singoli dipendenti, che la giurisprudenza ritiene invalido).",
            "Predisporre subito l'istanza telematica all'Ispettorato Territoriale del Lavoro (ITL) o l'accordo con le RSA/RSU.",
            "Installare cartellonistica conforme di primo livello e mettere a disposizione l'informativa estesa con tempi di conservazione (24-48 ore ordinarie).",
            "In caso di verbale ispettivo, gestire la procedura di estinzione della contravvenzione e le memorie difensive verso il Garante."
        ],
        "prove": ["Planimetria con angoli di ripresa", "Accordo sindacale o provvedimento autorizzativo ITL", "Cartellonistica e informativa completa", "Nomina a responsabile del fornitore vigilanza"],
        "errori": ["Raccogliere firme di consenso dei lavoratori al posto dell'autorizzazione ITL", "Installare telecamere finte o spente senza rimuoverle (spesso comunque contestate)", "Conservare le registrazioni per settimane senza giustificazione documentata"]
    },
    {
        "cod": "CYB-100", "slug": "modello-231-reati-informatici-art-24-bis-legge-90-2024",
        "cat": "compliance-231-ai", "cat_lbl": "231, DPO & AI Act", "pilastro": "modello-231-reati-informatici",
        "titolo": "Aggiornamento Modello 231 per reati informatici e art. 24-bis dopo la L. 90/2024",
        "seo_title": "Modello 231 Art. 24-bis e Legge 90/2024: Difesa dell'Ente",
        "desc": "Come adeguare il Modello di Organizzazione 231 ai nuovi reati informatici e all'estorsione informatica (L. 90/2024) per evitare sanzioni pecuniarie e interdittive alla societa'.",
        "keywords": ["modello 231 art 24-bis", "legge 90 2024 modello 231", "responsabilita ente reati informatici", "sanzioni interdittive 231 cyber"],
        "norme": ["Art. 24-bis D.Lgs. 231/2001", "L. 90/2024", "Art. 6 D.Lgs. 231/2001"],
        "scenario": "Un dipendente o un dirigente commette un accesso abusivo, un danneggiamento informatico o una falsita' digitale nell'interesse o a vantaggio della societa'.",
        "rischio": "La societa' rischia sanzioni pecuniarie elevate (aumentate dalla L. 90/2024) e sanzioni interdittive come il divieto di contrattare con la PA.",
        "protocollo": [
            "Eseguire una mappatura dei rischi informatici (risk assessment 231) su accessi amministrativi, gare telematiche, software e fornitori IT.",
            "Aggiornare la Parte Speciale del Modello 231 integrando i reati introdotti o aggravati dalla Legge 90/2024.",
            "Collegare i protocolli 231 alle misure tecniche reali (segregazione privilegi, log immutabili, procedure NIS2/GDPR) e ai flussi verso l'OdV.",
            "In caso di indagine sull'ente, costruire subito la difesa sulla prova dell'elusione fraudolenta del Modello e attivare condotte riparatorie ex art. 17 D.Lgs. 231/2001."
        ],
        "prove": ["Modello 231 aggiornato e delibera di adozione", "Verbali di verifica dell'Organismo di Vigilanza", "Log tecnici e policy sicurezza IT", "Attestati formazione personale"],
        "errori": ["Tenere un Modello 231 copia-incolla privo di controlli IT reali", "Non aggiornare l'art. 24-bis dopo le modifiche del 2024", "Dimenticare i flussi informativi obbligatori verso l'OdV su incidenti cyber"]
    },
    {
        "cod": "CYB-101", "slug": "sequestro-probatorio-smartphone-pc-indagini-penali",
        "cat": "lavoro-forense", "cat_lbl": "Lavoro & Prove Digitali", "pilastro": "ex-dipendenti-sottrazione-dati-segreti-aziendali",
        "titolo": "Sequestro probatorio di smartphone, computer e server: riesame e dissequestro",
        "seo_title": "Sequestro Smartphone e PC in Indagini Penali: Riesame e Difesa",
        "desc": "Come impugnare il sequestro sproporzionato dell'intero smartphone o PC aziendale: principio di proporzionalita', copia forense selettiva e ricorso al Riesame.",
        "keywords": ["sequestro smartphone indagini penali", "riesame sequestro probatorio pc", "dissequestro cellulare copia forense", "art 254 cpp sequestro informatico"],
        "norme": ["Art. 254 e 254-bis c.p.p.", "Art. 257 c.p.p.", "Art. 324 c.p.p.", "Principio di proporzionalita' Cassazione"],
        "scenario": "Durante una perquisizione, la Polizia Giudiziaria sequestra integralmente lo smartphone personale, i laptop e i server dell'indagato o di un terzo estraneo per mesi.",
        "rischio": "Paralisi dell'attivita' lavorativa, esposizione indiscriminata dell'intera vita privata e compressione sproporzionata dei diritti di difesa.",
        "protocollo": [
            "Verificare subito la motivazione del decreto di perquisizione e sequestro del PM rispetto al nesso pertinenziale con il reato ipotizzato.",
            "Proporre entro 10 giorni istanza di riesame del sequestro probatorio (art. 324 c.p.p.) contestando l'apprensione massiva e indiscriminata.",
            "Nominare un consulente tecnico informatico di parte per presenziare agli accertamenti irripetibili ex art. 360 c.p.p. e chiedere selezione per parole chiave.",
            "Depositare istanza di restituzione immediata dei dispositivi originali previa estrazione della sola copia forense pertinente."
        ],
        "prove": ["Decreto di perquisizione e verbale di sequestro", "Elenco dispositivi sequestrati con sigilli", "Prova del danno lavorativo da fermo dispositivi", "Nomina CTP informatico"],
        "errori": ["Far decorrere il termine perentorio di 10 giorni per il riesame", "Consegnare password senza aver prima consultato il difensore sui limiti del decreto", "Non partecipare tramite CTP alle operazioni di estrazione forense"]
    },
    {
        "cod": "CYB-102", "slug": "acquisizione-forense-chat-whatsapp-email-processo-civile",
        "cat": "lavoro-forense", "cat_lbl": "Lavoro & Prove Digitali", "pilastro": "ex-dipendenti-sottrazione-dati-segreti-aziendali",
        "titolo": "Valore probatorio di chat WhatsApp, SMS ed email nel processo civile e penale",
        "seo_title": "Prove WhatsApp ed Email in Tribunale: Acquisizione Forense",
        "desc": "Come evitare che screenshot di WhatsApp o email vengano disconosciuti in causa: copia forense certificata, hash SHA-256, art. 2712 c.c. e conservazione dispositivo.",
        "keywords": ["valore legale screenshot whatsapp", "acquisizione forense chat whatsapp", "disconoscimento email art 2712 cc", "perizia informatica chat processo"],
        "norme": ["Art. 2712 c.c.", "Art. 23-quater CAD", "Art. 234 c.p.p."],
        "scenario": "In una causa civile, di lavoro o penale una parte produce semplici screenshot di WhatsApp o stampe di email, che la controparte disconosce contestandone l'autenticita'.",
        "rischio": "Perdita di efficacia della prova decisiva se il dispositivo originale viene cambiato o se l'acquisizione non rispetta la catena di custodia.",
        "protocollo": [
            "Conservare intatto il dispositivo originale con la chat o la casella email senza cancellare messaggi o disinstallare l'app.",
            "Far eseguire un'acquisizione forense certificata con calcolo dell'impronta crittografica (hash SHA-256) e marca temporale.",
            "Per le email, depositare i file originali completi di header tecnici (.eml / .msg) e, per le PEC, le ricevute originali di accettazione e consegna.",
            "In giudizio, replicare a eventuali disconoscimenti generici dimostrando l'integrita' tecnica della riproduzione informatica."
        ],
        "prove": ["Dispositivo originale integro", "Relazione di acquisizione forense con hash SHA-256", "File .eml originali con header SMTP", "Marca temporale qualificata"],
        "errori": ["Depositare foto fatte con un altro telefono senza salvare il dispositivo sorgente", "Cambiare smartphone eliminando la chat originale prima della perizia", "Stampare una PEC in PDF omettendo i file .eml di accettazione e consegna"]
    },
    {
        "cod": "CYB-103", "slug": "polizza-cyber-assicurazione-rifiuto-indennizzo-sinistro",
        "cat": "ransomware-nis2", "cat_lbl": "Ransomware & NIS2", "pilastro": "ransomware-estorsione-informatica",
        "titolo": "Rifiuto di indennizzo della polizza cyber dopo un attacco ransomware o frode",
        "seo_title": "Polizza Cyber Negata dall'Assicurazione: Difesa e Contenzioso",
        "desc": "Come contestare il diniego dell'assicurazione cyber dopo un sinistro informatico: analisi clausole di esclusione, questionario assuntivo, denuncia tempestiva e azione civile.",
        "keywords": ["polizza cyber rifiuto indennizzo", "assicurazione ransomware esclusione", "contenzioso polizza cyber avvocato"],
        "norme": ["Art. 1892-1893 c.c.", "Art. 1913 c.c.", "Art. 1370 c.c.", "Codice delle Assicurazioni"],
        "scenario": "Dopo un attacco ransomware o una frode BEC, la compagnia assicurativa nega la copertura sostenendo dichiarazioni inesatte nel questionario IT o l'operativita' di clausole di esclusione.",
        "rischio": "L'azienda resta scoperta proprio nel momento di massima esposizione per costi di ripristino, fermo attivita' e richieste terzi.",
        "protocollo": [
            "Notificare il sinistro alla compagnia entro i termini stretti di polizza (spesso 24-72 ore) usando i canali di emergenza previsti.",
            "Esaminare integralmente condizioni generali, appendici di esclusione (es. guerra cyber, social engineering) e questionario pre-contrattuale.",
            "Contestare via PEC eventuali eccezioni strumentali della compagnia richiamando l'interpretazione contro il predisponente (art. 1370 c.c.).",
            "Avviare negoziazione assistita, mediazione o giudizio civile per ottenere la liquidazione integrale dell'indennizzo."
        ],
        "prove": ["Contratto di polizza completo e questionario assuntivo", "Denuncia di sinistro tempestiva", "Report forense dell'incidente", "Fatture costi di ripristino e calcolo danno da interruzione"],
        "errori": ["Ingaggiare fornitori di incident response esterni senza previo consenso della compagnia quando richiesto", "Pagare riscatti o transazioni senza autorizzazione assicurativa", "Compilare il questionario di rinnovo senza verifica tecnica reale"]
    },

    # ═══════════════════ E-COMMERCE, MARKETING, CLOUD & COOKIE (104-110) ═══════════════════
    {
        "cod": "CYB-104", "slug": "sanzione-garante-cookie-banner-tracciamento-ecommerce",
        "cat": "data-breach", "cat_lbl": "Data Breach & GDPR", "pilastro": "compliance-gdpr-dpo-privacy",
        "titolo": "Contestazione Garante su cookie banner irregolare e pixel di tracciamento",
        "seo_title": "Cookie Banner Irregolare e Sanzioni Garante: Adeguamento e Difesa",
        "desc": "Come mettere a norma siti web ed e-commerce secondo le Linee guida cookie del Garante Privacy ed evitare sanzioni su dark patterns, pixel Meta/Google e consenso.",
        "keywords": ["cookie banner irregolare sanzione garante", "linee guida cookie garante privacy", "pixel facebook gdpr consenso"],
        "norme": ["Art. 122 D.Lgs. 196/2003", "Art. 7 GDPR", "Linee guida cookie Garante 10 giugno 2021"],
        "scenario": "Un sito e-commerce attiva cookie di profilazione o pixel pubblicitari prima del consenso dell'utente oppure manca il tasto X di chiusura/rifiuto paritario sul banner.",
        "rischio": "Istruttoria del Garante su segnalazione di utenti o concorrenti con sanzioni pecuniarie e blocco dei trattamenti pubblicitari.",
        "protocollo": [
            "Eseguire un audit tecnico del sito verificando che nessun cookie non tecnico o pixel venga caricato prima del clic di accettazione.",
            "Configurare il banner con pulsante di rifiuto/chiusura X paritario, link alla cookie policy e possibilita' di revoca permanente nel footer.",
            "Conservare i log tecnici di registrazione dei consensi (CMP) per dimostrare l'accountability in caso di controllo.",
            "In caso di contestazione gia' notificata, attuare subito la messa a norma e depositare memorie difensive ex art. 166 Codice Privacy."
        ],
        "prove": ["Report scansione cookie pre-consenso", "Log della Consent Management Platform", "Screenshot banner aggiornato e cookie policy", "Memorie difensive al Garante"],
        "errori": ["Usare banner estetici che non bloccano realmente gli script pubblicitari", "Inserire il tasto accetta enorme nascondendo il rifiuto (dark pattern)", "Ripropporre il banner a ogni visita dopo il rifiuto dell'utente"]
    },
    {
        "cod": "CYB-105", "slug": "telemarketing-selvaggio-lista-contatti-senza-consenso",
        "cat": "data-breach", "cat_lbl": "Data Breach & GDPR", "pilastro": "compliance-gdpr-dpo-privacy",
        "titolo": "Campagne email marketing o telemarketing con liste acquistate senza consenso valido",
        "seo_title": "Email Marketing e Telemarketing GDPR: Difesa da Sanzioni Garante",
        "desc": "Responsabilita' dell'azienda committente per campagne DEM, SMS o call center basate su liste prive di consenso documentato: audit fornitori, art. 130 Codice Privacy e difesa.",
        "keywords": ["sanzioni garante telemarketing", "email marketing senza consenso gdpr", "art 130 codice privacy spam", "acquisto liste contatti legale"],
        "norme": ["Art. 130 D.Lgs. 196/2003", "Art. 6 e 7 GDPR", "Codice di condotta telemarketing"],
        "scenario": "Un'azienda affida una campagna promozionale a un'agenzia o acquista una lista di contatti, ma alcuni destinatari presentano reclamo al Garante lamentando assenza di consenso.",
        "rischio": "Il Garante sanziona anche il committente che non ha verificato la filiera dei consensi e il rispetto del Registro Pubblico delle Opposizioni.",
        "protocollo": [
            "Sospendere immediatamente la campagna contestata e inserire i reclamanti in black-list permanente.",
            "Verificare se esistono log verificabili (data, ora, IP, testo informativa) del consenso specifico al marketing e alla cessione a terzi.",
            "Controllare il contratto con l'agenzia/list broker per verificare garanzie e manleve sulla liceita' della banca dati.",
            "Rispondere tempestivamente alle richieste del Garante dimostrando le misure di bonifica e la revisione della filiera commerciale."
        ],
        "prove": ["Log consenso double opt-in", "Contratto con agenzia marketing e DPA art. 28", "Registro black-list e verifiche RPO", "Riscontri forniti agli interessati"],
        "errori": ["Acquistare elenchi di contatti senza prova tecnica del consenso alla cessione", "Usare indirizzi presi da internet per inviare newsletter commerciali (vietato)", "Ignorare le richieste di cancellazione degli utenti"]
    },
    {
        "cod": "CYB-106", "slug": "trasferimento-dati-extra-ue-cloud-usa-scc-dpf",
        "cat": "compliance-231-ai", "cat_lbl": "231, DPO & AI Act", "pilastro": "compliance-gdpr-dpo-privacy",
        "titolo": "Trasferimento di dati personali verso fornitori cloud USA o extra-UE",
        "seo_title": "Trasferimento Dati Extra-UE e Cloud USA: GDPR, DPF e SCC",
        "desc": "Come rendere lecito l'uso di piattaforme SaaS, CRM e cloud statunitensi o extra-UE: verifica EU-US Data Privacy Framework, Standard Contractual Clauses e TIA.",
        "keywords": ["trasferimento dati extra ue gdpr", "cloud usa data privacy framework", "clausole contrattuali tipo scc", "transfer impact assessment tia"],
        "norme": ["Artt. 44-49 GDPR", "Decisione adeguatezza EU-US Data Privacy Framework", "Clausole Contrattuali Tipo (SCC) UE"],
        "scenario": "Un'impresa utilizza software CRM, analytics o cloud con sede negli Stati Uniti o in Paesi terzi privi di decisione di adeguatezza.",
        "rischio": "Ordine di sospensione del flusso dati da parte del Garante e sanzioni fino al 4% del fatturato globale ex art. 83 par. 5 GDPR.",
        "protocollo": [
            "Censire tutti i fornitori SaaS e i relativi sub-responsabili per individuare la reale localizzazione dei server e degli accessi di supporto.",
            "Verificare se il fornitore USA e' attivamente certificato nell'elenco ufficiale EU-US Data Privacy Framework (DPF).",
            "In assenza di decisione di adeguatezza, stipulare le Standard Contractual Clauses (SCC) aggiornate e redigere un Transfer Impact Assessment (TIA).",
            "Adottare misure supplementari tecniche (cifratura con chiavi gestite in UE) e aggiornare le informative privacy."
        ],
        "prove": ["Mappa flussi dati extra-UE", "Verifica certificazione DPF del fornitore", "SCC firmate e documento TIA", "Configurazione data residency UE"],
        "errori": ["Dare per scontato che un server in Europa escluda il trasferimento se il supporto tecnico accede da Paesi terzi", "Non aggiornare l'informativa indicando i trasferimenti extra-UE", "Usare vecchie clausole SCC abrogate"]
    },
    {
        "cod": "CYB-107", "slug": "violazione-canale-whistleblowing-identita-segnalante",
        "cat": "compliance-231-ai", "cat_lbl": "231, DPO & AI Act", "pilastro": "compliance-gdpr-dpo-privacy",
        "titolo": "Violazione della riservatezza sul canale whistleblowing (D.Lgs. 24/2023)",
        "seo_title": "Sicurezza Canale Whistleblowing e Data Breach: D.Lgs. 24/2023",
        "desc": "Gestione di falle di sicurezza o rivelazione dell'identita' del segnalante nei canali whistleblowing: obblighi cifratura, DPIA, ANAC e Garante Privacy.",
        "keywords": ["whistleblowing violazione riservatezza", "sicurezza piattaforma whistleblowing gdpr", "sanzioni anac garante whistleblowing"],
        "norme": ["D.Lgs. 24/2023", "Art. 32 e 35 GDPR", "Linee guida ANAC whistleblowing"],
        "scenario": "Una piattaforma whistleblowing mal configurata o l'uso improprio di una semplice casella email espone l'identita' di un dipendente segnalante o il contenuto della segnalazione.",
        "rischio": "Doppia esposizione sanzionatoria verso ANAC (fino a 50.000 euro) e Garante Privacy, oltre a contenzioso di lavoro per ritorsioni.",
        "protocollo": [
            "Mettere immediatamente in sicurezza il canale revocando gli accessi indebiti e valutando la notifica di data breach al Garante entro 72 ore.",
            "Sostituire canali insicuri (email ordinarie) con una piattaforma dedicata dotata di crittografia end-to-end e accesso ristretto al solo gestore.",
            "Redigere o aggiornare la DPIA dedicata al trattamento whistleblowing e il contratto art. 28 con il fornitore della piattaforma.",
            "Proteggere formalmente il segnalante da qualsiasi misura pregiudizievole documentando l'autonomia del gestore."
        ],
        "prove": ["DPIA whistleblowing", "Specifiche tecniche di crittografia della piattaforma", "Nomina formale del gestore delle segnalazioni", "Registro accessi e misure di contenimento"],
        "errori": ["Gestire il whistleblowing tramite un indirizzo email aziendale visibile all'IT", "Non tracciare i log di accesso alla piattaforma", "Conservare le segnalazioni oltre il termine massimo di 5 anni"]
    },
    {
        "cod": "CYB-108", "slug": "attacco-ddos-blocco-sito-ecommerce-stagione-vendite",
        "cat": "ransomware-nis2", "cat_lbl": "Ransomware & NIS2", "pilastro": "reati-informatici-difesa-penale",
        "titolo": "Attacco DDoS che blocca il sito e-commerce o i portali aziendali",
        "seo_title": "Attacco DDoS su E-commerce: Difesa Penale e Responsabilita'",
        "desc": "Protocollo operativo contro attacchi DDoS ed estorsioni DDoS (RDoS): mitigazione, preservazione log, querela ex art. 635-quater e 629 c.p. e verifica SLA hosting.",
        "keywords": ["attacco ddos reato italia", "art 635-quater cp ddos", "estorsione ddos azienda", "sito ecommerce bloccato attacco"],
        "norme": ["Art. 635-quater c.p.", "Art. 629 comma 3 c.p.", "D.Lgs. 138/2024 (se soggetto NIS2)"],
        "scenario": "Un e-commerce o un portale di prenotazioni viene reso irraggiungibile durante un picco commerciale da milioni di richieste malevole, spesso accompagnate da richiesta di riscatto.",
        "rischio": "Perdita diretta di vendite, penalizzazione SEO e interruzione di servizi essenziali.",
        "protocollo": [
            "Attivare subito filtri anti-DDoS / CDN con il provider e conservare i log completi del traffico anomalo e delle eventuali email estorsive.",
            "Verificare se l'interruzione supera le soglie di incidente significativo NIS2 (notifica ACN entro 24 ore).",
            "Depositare querela penale per danneggiamento di sistemi informatici e, se vi e' richiesta di denaro, estorsione informatica (L. 90/2024).",
            "Verificare gli SLA contrattuali del provider hosting e la copertura per interruzione di attivita' nella polizza cyber."
        ],
        "prove": ["Log traffico anomalo CDN/firewall", "Email o richieste di riscatto RDoS", "Dati di perdita fatturato nel periodo di blocco", "Contratto SLA con hosting/provider"],
        "errori": ["Pagare il riscatto RDoS (non garantisce la cessazione dell'attacco)", "Non raccogliere la prova economica del mancato guadagno", "Omettere di verificare se il DDoS copre un tentativo parallelo di furto dati"]
    },
    {
        "cod": "CYB-109", "slug": "furto-account-whatsapp-business-aziendale-clienti",
        "cat": "penale-cyber", "cat_lbl": "Reati Informatici", "pilastro": "reati-informatici-difesa-penale",
        "titolo": "Furto dell'account WhatsApp Business aziendale usato per truffare i clienti",
        "seo_title": "WhatsApp Business Hackerato: Recupero, Denuncia e GDPR",
        "desc": "Come reagire al furto dell'account WhatsApp aziendale: recupero immediato, avviso ai clienti per evitare truffe, valutazione data breach 72 ore e denuncia.",
        "keywords": ["whatsapp business hackerato azienda", "furto account whatsapp truffa clienti", "whatsapp rubato data breach gdpr"],
        "norme": ["Art. 615-ter c.p.", "Art. 494 c.p.", "Art. 33 GDPR"],
        "scenario": "Ignoti sottraggono il controllo del numero WhatsApp Business dell'azienda tramite codice SMS carpito e inviano richieste di bonifico o link malevoli a tutta la rubrica clienti.",
        "rischio": "Truffe dirette ai clienti a nome dell'azienda, grave danno d'immagine ed esposizione della rubrica e delle chat commerciali.",
        "protocollo": [
            "Avviare immediatamente la procedura di blocco e recupero dell'account tramite supporto ufficiale WhatsApp e verificare la sicurezza della SIM.",
            "Avvisare tempestivamente clienti e fornitori tramite canali alternativi (PEC, email, sito, social) di non eseguire pagamenti richiesti via WhatsApp.",
            "Valutare entro 72 ore la notifica di data breach al Garante Privacy se nelle chat o nei backup erano presenti dati personali sensibili.",
            "Sporgere querela alla Polizia Postale per accesso abusivo e sostituzione di persona, poi attivare la verifica in due passaggi (PIN)."
        ],
        "prove": ["Screenshot avvisi di disconnessione e richieste truffaldine ricevute dai clienti", "Comunicazioni ufficiali di allerta inviate", "Ticket supporto WhatsApp", "Denuncia querela"],
        "errori": ["Non avvisare subito la rubrica esponendo i clienti a bonifici fraudolenti", "Pagare somme a chi ha sottratto l'account", "Non abilitare la verifica in due passaggi dopo il recupero"]
    },
    {
        "cod": "CYB-110", "slug": "clonazione-sito-ecommerce-brand-contraffatto-online",
        "cat": "reputazione-social", "cat_lbl": "Reputazione & Social", "pilastro": "reputazione-online-deepfake-revenge-porn",
        "titolo": "Sito e-commerce clone che copia marchio, foto e prodotti aziendali per truffare utenti",
        "seo_title": "Sito E-commerce Clonato: Takedown Dominio, Difesa Marchio e Penale",
        "desc": "Azioni legali rapide contro siti web clone che vendono finti prodotti usando il marchio e le foto di un'azienda italiana: takedown hosting, riassegnazione dominio e denuncia.",
        "keywords": ["sito ecommerce clonato cosa fare", "takedown dominio truffa", "contraffazione marchio online difesa", "udrp riassegnazione dominio"],
        "norme": ["Art. 473 e 640 c.p.", "Art. 20 Codice Proprieta' Industriale", "Procedure UDRP / riassegnazione .it", "Reg. UE 2022/2065 (DSA)"],
        "scenario": "Un sito estero replica integralmente grafica, logo, partita IVA e catalogo di un e-commerce italiano proponendo sconti irreali per incassare pagamenti fraudolenti.",
        "rischio": "Clienti truffati che segnalano l'azienda reale alle autorita' o lasciano recensioni negative, oltre alla violazione del marchio e del copyright.",
        "protocollo": [
            "Effettuare acquisizione forense certificata del sito clone, dei dati WHOIS/DNS, del provider hosting e del gateway di pagamento usato.",
            "Inviare formale notice di takedown per phishing/contraffazione al registrar del dominio, all'hosting provider, a Cloudflare e ai motori di ricerca.",
            "Pubblicare un banner di avviso sul sito ufficiale e depositare denuncia alla Polizia Postale tutelando la propria estraneita' ai pagamenti.",
            "Avviare la procedura di riassegnazione o cancellazione del dominio (UDRP / Registro .it) e l'eventuale azione civile per contraffazione."
        ],
        "prove": ["Acquisizione forense del sito clone", "Dati WHOIS, IP e provider hosting", "Certificato di registrazione marchio e titolarita' foto", "Segnalazioni clienti truffati"],
        "errori": ["Limitarsi a una segnalazione informale senza attivare registrar e hosting", "Non pubblicare un avviso chiaro per proteggere i clienti e la propria reputazione", "Trascurare l'uso illecito della propria Partita IVA sul sito truffaldino"]
    },
]
