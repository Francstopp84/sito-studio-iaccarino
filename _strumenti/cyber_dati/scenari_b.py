# -*- coding: utf-8 -*-
"""Scenari operativi e protocolli di difesa 36-70 (Penale parte 2, Lavoro/Segreti, Identita'/Deepfake/Reputazione, Contratti IT/AI/231)."""

SCENARI_B = [
    # ═══════════════════ 4. PENALE INFORMATICO & FORENSICS (36-40) ═══════════════════
    {
        "cod": "CYB-36", "slug": "detenzione-diffusione-codici-accesso-malware-615-quater-quinquies",
        "cat": "penale-informatico", "cat_lbl": "Penale Informatico & Forensics", "pilastro": "reati-informatici-difesa-penale",
        "titolo": "Detenzione o diffusione di codici di accesso e malware (artt. 615-quater e quinquies c.p.)",
        "seo_title": "Art. 615-quater e 615-quinquies c.p.: Difesa Codici e Malware",
        "desc": "Difesa penale e tutela delle aziende per traffico di credenziali rubate, stealer logs, exploit o programmi diretti a danneggiare sistemi informatici.",
        "keywords": ["art 615 quater cp", "art 615 quinquies cp malware", "credenziali rubate reato penale"],
        "norme": ["Art. 615-quater c.p.", "Art. 615-quinquies c.p.", "L. 90/2024"],
        "scenario": "Un soggetto e' accusato di aver detenuto, condiviso o venduto password, chiavi d'accesso o software dannosi (o un'azienda scopre le proprie credenziali in vendita su canali Telegram/forum).",
        "rischio": "Condanna penale aggravata dalla L. 90/2024 e rischio di contestazione di concorso nei successivi accessi abusivi o estorsioni informatiche.",
        "protocollo": [
            "Verificare il requisito del dolo specifico (fine di profitto o di arrecare danno) distinguendo gli strumenti di sicurezza/pentesting leciti dal malware illecito.",
            "Per le aziende vittime, revocare subito tutte le credenziali esposte, attivare MFA hardware e sporgere denuncia per tracciare i canali di rivendita.",
            "In difesa dell'indagato, accertare tramite perizia informatica l'origine dei file trovati sul dispositivo e l'assenza di finalita' illecite.",
            "Valutare eventuali profili di competenza distrettuale e la proporzionalita' di eventuali misure cautelari."
        ],
        "prove": ["Analisi forense dei file o script rinvenuti", "Contratti di consulenza sicurezza / autorizzazioni pentesting", "Log di revoca credenziali aziendali", "Acquisizione forense dei canali di diffusione"],
        "errori": ["Eseguire test di penetrazione (pentest) senza autorizzazione scritta dettagliata", "Non verificare l'elemento soggettivo richiesto dalla norma", "Lasciare attive credenziali segnalate da servizi di threat intelligence"]
    },
    {
        "cod": "CYB-37", "slug": "intercettazione-illecita-comunicazioni-informatiche-617-quater",
        "cat": "penale-informatico", "cat_lbl": "Penale Informatico & Forensics", "pilastro": "reati-informatici-difesa-penale",
        "titolo": "Spyware su smartphone, keylogger e intercettazione illecita (art. 617-quater c.p.)",
        "seo_title": "Spyware su Telefono e Art. 617-quater c.p.: Denuncia e Difesa",
        "desc": "Tutela penale quando uno smartphone o PC viene infettato con spyware o stalkerware per leggere chat, email e posizione: perizia forense e art. 617-quater c.p.",
        "keywords": ["spyware telefono denuncia", "art 617 quater cp", "stalkerware smartphone ex coniuge reato"],
        "norme": ["Art. 617-quater c.p.", "Art. 617-quinquies c.p.", "Art. 615-ter c.p."],
        "scenario": "Un imprenditore o un privato sospetta che sul proprio telefono o computer sia stato installato uno spyware o un'app di controllo nascosto (anche in contesti di separazione o spionaggio industriale).",
        "rischio": "Violazione continuativa di conversazioni riservate, segreti aziendali o difese legali, con pene severe per chi installa o usa il software spia.",
        "protocollo": [
            "NON resettare ai dati di fabbrica il telefono sospetto prima che un perito forense abbia acquisito la copia bit-stream e identificato lo spyware.",
            "Utilizzare un dispositivo pulito con SIM nuova per contattare il difensore.",
            "Depositare querela o denuncia dettagliata allegando la perizia forense con indicatori dell'app spia e server di destinazione dei dati.",
            "Chiedere il sequestro probatorio dei dispositivi del sospettato e valutare il raccordo con eventuali procedimenti civili o di famiglia."
        ],
        "prove": ["Copia forense certificata dello smartphone/PC infetto", "Report analisi pacchetti di rete e app nascoste", "Log di accesso all'account iCloud/Google", "Prove di conoscenza di informazioni riservate da parte del sospettato"],
        "errori": ["Formattare subito il telefono cancellando l'unica prova del reato", "Accusare senza una perizia tecnica preliminare", "Continuare a discutere strategie difensive sul dispositivo compromesso"]
    },
    {
        "cod": "CYB-38", "slug": "difesa-trojan-captatore-informatico-processo-penale",
        "cat": "penale-informatico", "cat_lbl": "Penale Informatico & Forensics", "pilastro": "reati-informatici-difesa-penale",
        "titolo": "Intercettazioni con captatore informatico (Trojan di Stato): verifica inutilizzabilita'",
        "seo_title": "Captatore Informatico (Trojan) Penale: Verifica Inutilizzabilita'",
        "desc": "Difesa tecnica sulle intercettazioni tramite captatore informatico (art. 266 co. 2 c.p.p.): controllo dei decreti autorizzativi, log di inoculo e inutilizzabilita' ex art. 271 c.p.p.",
        "keywords": ["captatore informatico trojan difesa", "inutilizzabilita intercettazioni trojan", "art 266 comma 2 cpp"],
        "norme": ["Art. 266 co. 2 c.p.p.", "Art. 267 c.p.p.", "Art. 271 c.p.p."],
        "scenario": "In un procedimento penale l'accusa si basa su captazioni ambientali e acquisizioni eseguite tramite trojan inoculato sullo smartphone dell'indagato.",
        "rischio": "Utilizzo di captazioni acquisite fuori dai limiti di legge, in luoghi di privata dimora senza i presupposti o con software non conforme ai requisiti tecnici ministeriali.",
        "protocollo": [
            "Richiedere l'accesso integrale ai decreti autorizzativi del GIP, ai verbali delle operazioni e ai log tecnici di inoculo, attivazione e disinstallazione del captatore.",
            "Verificare il rispetto dei limiti sui reati ammessi e sulle captazioni nel domicilio (luogo e tempo di attivazione del microfono).",
            "Far verificare a un consulente tecnico l'integrita' dei file audio, dei dati trasmessi ai server della Procura e la conformita' tecnica del software.",
            "Eccepire tempestivamente l'inutilizzabilita' patologica ex art. 271 c.p.p."
        ],
        "prove": ["Decreti GIP di autorizzazione e proroga", "Log tecnici del server di intercettazione", "Verbali di inoculo e disinstallazione", "Consulenza tecnica fonica e informatica"],
        "errori": ["Limitarsi a leggere i brogliacci senza ascoltare i file audio originali", "Non verificare i presupposti di attivazione in privata dimora", "Omettere la richiesta dei log tecnici di trasmissione dati"]
    },
    {
        "cod": "CYB-39", "slug": "acquisizione-tabulati-telefonici-log-ip-art-132-privacy",
        "cat": "penale-informatico", "cat_lbl": "Penale Informatico & Forensics", "pilastro": "reati-informatici-difesa-penale",
        "titolo": "Tabulati telefonici, celle e log IP nelle indagini penali (art. 132 Codice Privacy)",
        "seo_title": "Tabulati Telefonici e Log IP Penale: Art. 132 D.Lgs. 196/2003",
        "desc": "Come funzionano acquisizione e difesa su tabulati telefonici e log telematici dopo la riforma dell'art. 132 Codice Privacy: decreto motivato del giudice e termini di conservazione.",
        "keywords": ["art 132 codice privacy tabulati", "acquisizione log ip indagini penali", "inutilizzabilita tabulati telefonici"],
        "norme": ["Art. 132 D.Lgs. 196/2003", "Art. 391-quater c.p.p."],
        "scenario": "In un'indagine su reati informatici o truffe online la Procura acquisisce tabulati e log di connessione telematica, oppure il difensore deve ottenerli urgentemente prima della cancellazione.",
        "rischio": "I log telematici vengono conservati per tempi limitati (12 mesi per il traffico telematico, 24 mesi per quello telefonico); se acquisiti senza decreto motivato del giudice possono essere inutilizzabili.",
        "protocollo": [
            "Per la difesa dell'indagato, verificare che i tabulati siano stati acquisiti con decreto motivato del giudice (non del solo PM, salvo urgenza convalidata entro 48 ore) e per reati che rientrano nelle soglie di legge.",
            "Verificare il valore probatorio reale di celle telefoniche e indirizzi IP dinamici/NAT condivisi.",
            "Per la persona offesa o indagini difensive, sollecitare immediatamente l'ordine di conservazione (data preservation) prima che i provider cancellino i log.",
            "Integrare l'analisi con consulenza tecnica sulle reti e sulla geolocalizzazione."
        ],
        "prove": ["Decreto del giudice ex art. 132 co. 3 Codice Privacy", "Tabulati integrali in formato grezzo", "Dati tecnici IP / NAT del provider", "Istanza di conservazione urgente dei log"],
        "errori": ["Aspettare mesi per chiedere l'acquisizione di log telematici che scadono", "Non contestare l'acquisizione priva di decreto motivato del giudice", "Trattare una cella telefonica ampia come prova di presenza puntuale"]
    },
    {
        "cod": "CYB-40", "slug": "querela-tecnica-polizia-postale-contro-ignoti-cybercrime",
        "cat": "penale-informatico", "cat_lbl": "Penale Informatico & Forensics", "pilastro": "reati-informatici-difesa-penale",
        "titolo": "Come redigere una querela informatica che non finisca archiviata",
        "seo_title": "Querela Polizia Postale Contro Ignoti: Come Evitare Archiviazione",
        "desc": "Perche' le denunce generiche per reati informatici vengono archiviate e come depositare una querela tecnicamente blindata con prove forensi e piste d'indagine concrete.",
        "keywords": ["querela polizia postale come fare", "denuncia reato informatico archiviazione", "opposizione archiviazione reati informatici"],
        "norme": ["Art. 333-336 c.p.p.", "Art. 408-410 c.p.p.", "L. 90/2024"],
        "scenario": "Una vittima di intrusione, frode o estorsione informatica vuole sporgere querela (o ha appena ricevuto avviso di richiesta di archiviazione per essere ignoti gli autori).",
        "rischio": "Una denuncia priva di log tecnici, header email, IBAN, TXID o URL certificati rende quasi impossibile l'identificazione degli autori e porta all'archiviazione.",
        "protocollo": [
            "Allegare alla querela un fascicolo tecnico ordinato: acquisizioni forensi certificate, header .eml completi, log server, IBAN/wallet e cronologia esatta in formato UTC.",
            "Indicare espressamente al PM gli accertamenti urgenti da compiere (acquisizione log presso provider esteri/italiani, ordine europeo di indagine, sequestro conti).",
            "Chiedere l'avviso di eventuale richiesta di archiviazione ex art. 408 c.p.p.",
            "In caso di richiesta di archiviazione, proporre opposizione motivata ex art. 410 c.p.p. indicando le indagini suppletive precise ancora eseguibili."
        ],
        "prove": ["Fascicolo prove digitali con hash e data certa", "Elenco mirato di richieste istruttorie al PM", "Ricevuta deposito querela entro 3 mesi", "Eventuale atto di opposizione ex art. 410 c.p.p."],
        "errori": ["Presentare solo screenshot stampati su carta", "Attendere oltre 3 mesi per i reati procedibili a querela", "Dimenticare di chiedere l'avviso ex art. 408 c.p.p."]
    },

    # ═══════════════════ 5. LAVORO, EX DIPENDENTI & SEGRETI (41-50) ═══════════════════
    {
        "cod": "CYB-41", "slug": "ex-dipendente-copia-lista-clienti-crm-usb-cloud",
        "cat": "lavoro-segreti", "cat_lbl": "Lavoro, Ex Dipendenti & Segreti", "pilastro": "ex-dipendenti-sottrazione-dati-segreti-aziendali",
        "titolo": "Ex dipendente scarica lista clienti e listini su USB o cloud personale",
        "seo_title": "Ex Dipendente Ruba Lista Clienti su USB: Ricorso Urgente e Penale",
        "desc": "Protocollo immediato per bloccare l'ex dipendente che copia il database clienti prima delle dimissioni: ricorso cautelare artt. 98-99 CPI, concorrenza sleale e art. 615-ter c.p.",
        "keywords": ["ex dipendente ruba lista clienti", "sottrazione database clienti usb", "art 98 cpi segreti commerciali"],
        "norme": ["Artt. 98-99 D.Lgs. 30/2005 (CPI)", "Art. 2105 c.c.", "Art. 2598 c.c.", "Art. 615-ter c.p."],
        "scenario": "Nei giorni precedenti alle dimissioni un commerciale esporta dal CRM l'intera anagrafica clienti con margini e sconti, trasferendola su chiavetta USB o Google Drive privato.",
        "rischio": "Sviamento immediato del portafoglio clienti verso un concorrente o una nuova societa' costituita dall'ex dipendente.",
        "protocollo": [
            "Eseguire subito copia forense del PC aziendale e dei log CRM/cloud nel rispetto dei presupposti dei controlli difensivi.",
            "Verificare i requisiti di segretezza della banca dati (password, accessi profilati, NDA) richiesti dall'art. 98 CPI.",
            "Depositare ricorso cautelare urgente (descrizione e inibitoria ex artt. 129-131 CPI / art. 700 c.p.c.) davanti alla Sezione Specializzata Impresa.",
            "Affiancare diffida al nuovo datore di lavoro concorrente e querela penale ex art. 615-ter co. 2 n. 3 e 623 c.p."
        ],
        "prove": ["Log di esportazione CRM e inserimento chiavetta USB", "Copia forense PC aziendale", "Policy IT e accordi di riservatezza", "Email o testimonianze di clienti contattati"],
        "errori": ["Accedere alla casella privata del lavoratore senza titolo violando la privacy", "Aspettare mesi prima di chiedere l'inibitoria cautelare (fa venir meno il periculum in mora)", "Non avvisare formalmente la societa' concorrente che sfrutta i dati rubati"]
    },
    {
        "cod": "CYB-42", "slug": "controlli-difensivi-email-pc-dipendente-art-4-statuto",
        "cat": "lavoro-segreti", "cat_lbl": "Lavoro, Ex Dipendenti & Segreti", "pilastro": "ex-dipendenti-sottrazione-dati-segreti-aziendali",
        "titolo": "Controllo email e PC aziendale del dipendente: limiti art. 4 Statuto Lavoratori",
        "seo_title": "Controllo Email e PC Dipendente: Art. 4 Statuto Lavoratori e Privacy",
        "desc": "Quando il datore di lavoro puo' legittimamente controllare email, log e PC di un dipendente per provarne l'infedelta' senza subire sanzioni del Garante o nullita' del licenziamento.",
        "keywords": ["controllo email dipendente art 4 statuto lavoratori", "controlli difensivi legittimi", "licenziamento prova email aziendale"],
        "norme": ["Art. 4 L. 300/1970", "Art. 114 D.Lgs. 196/2003", "Art. 5 e 13 GDPR"],
        "scenario": "Un'azienda sospetta che un dipendente stia passando preventivi a un concorrente e vuole verificare la sua casella email aziendale e la cronologia del computer.",
        "rischio": "Un controllo preventivo generalizzato o privo di informativa IT rende le prove inutilizzabili nel processo del lavoro (annullando il licenziamento) e comporta sanzioni del Garante Privacy.",
        "protocollo": [
            "Verificare prima l'esistenza di una policy IT e informativa privacy gia' consegnata al lavoratore sull'uso degli strumenti di lavoro.",
            "Documentare per iscritto il fondato sospetto ex post sorto da elementi esterni (es. anomalia segnalata dal sistema o da un cliente) che legittima il controllo difensivo mirato.",
            "Limitare l'estrazione forense ai soli file/email pertinenti al sospetto e al periodo temporale interessato, evitando ogni controllo massivo o su cartelle personali.",
            "Redigere la contestazione disciplinare tempestiva ex art. 7 L. 300/1970 fondata su prove pienamente utilizzabili."
        ],
        "prove": ["Policy IT consegnata al dipendente", "Documento attestante l'insorgenza del fondato sospetto", "Verbale di estrazione forense mirata e selettiva", "Lettera di contestazione disciplinare"],
        "errori": ["Leggere abitualmente la posta dei dipendenti senza motivo ne' informativa", "Conservare i metadati email oltre i limiti indicati dal Garante senza accordo sindacale", "Usare prove raccolte in violazione dell'art. 4 in causa di licenziamento"]
    },
    {
        "cod": "CYB-43", "slug": "chiusura-account-email-ex-dipendente-garante-privacy",
        "cat": "lavoro-segreti", "cat_lbl": "Lavoro, Ex Dipendenti & Segreti", "pilastro": "ex-dipendenti-sottrazione-dati-segreti-aziendali",
        "titolo": "Gestione corretta della casella email aziendale dopo le dimissioni o il licenziamento",
        "seo_title": "Email Aziendale Ex Dipendente: Regole Garante Privacy e Sanzioni",
        "desc": "Come disattivare la casella email nominativa di un ex dipendente senza violare il GDPR: risposta automatica, divieto di accesso prolungato e conservazione legittima.",
        "keywords": ["email ex dipendente garante privacy", "disattivazione casella posta ex lavoratore", "sanzione garante email ex dipendente"],
        "norme": ["Art. 5 GDPR", "Art. 13 GDPR", "Provvedimenti Garante su posta elettronica"],
        "scenario": "Dopo le dimissioni di un dipendente, l'azienda mantiene attiva la sua casella email nominativa per mesi con inoltro automatico verso un collega, e l'ex lavoratore presenta reclamo al Garante.",
        "rischio": "Il Garante Privacy sanziona frequentemente le aziende che tengono aperte le caselle nominative degli ex dipendenti o ne leggono i messaggi in entrata.",
        "protocollo": [
            "Disattivare immediatamente l'account nominativo al termine del rapporto di lavoro, impostando un messaggio automatico di risposta che indichi un indirizzo aziendale alternativo.",
            "Rimuovere la casella dopo un breve periodo transitorio (salvo esigenze di conservazione in archivio blindato e non consultabile ordinariamente per contenziosi in atto).",
            "Se l'ex dipendente ha gia' presentato reclamo al Garante, disattivare subito l'account e predisporre memoria difensiva dimostrando la cessazione della condotta e la minimizzazione.",
            "Adottare una procedura standard di offboarding IT per tutte le future cessazioni."
        ],
        "prove": ["Log di disattivazione casella e configurazione auto-reply", "Procedura aziendale di offboarding IT", "Informativa lavoratori aggiornata", "Memoria difensiva al Garante"],
        "errori": ["Tenere attiva la mail nome.cognome@azienda.it per mesi con redirect silenzioso", "Leggere corrispondenza privata arrivata sull'account dell'ex dipendente", "Non predisporre account generici di reparto (info@, vendite@)"]
    },
    {
        "cod": "CYB-44", "slug": "sottrazione-codice-sorgente-software-sviluppatore",
        "cat": "lavoro-segreti", "cat_lbl": "Lavoro, Ex Dipendenti & Segreti", "pilastro": "ex-dipendenti-sottrazione-dati-segreti-aziendali",
        "titolo": "Sviluppatore o ex socio sottrae codice sorgente, repository Git o progetti tecnici",
        "seo_title": "Furto Codice Sorgente e Repository Git: Tutela Legale Software",
        "desc": "Azioni legali urgenti quando un programmatore o ex socio clona repository Git, codice sorgente o disegni CAD aziendali: diritto d'autore, segreti commerciali e sequestro.",
        "keywords": ["furto codice sorgente dipendente", "ex socio ruba software azienda", "tutela codice sorgente diritto autore"],
        "norme": ["L. 633/1941 art. 12-bis e 64-bis", "Artt. 98-99 CPI", "Art. 615-ter c.p.", "Art. 623 c.p."],
        "scenario": "Un programmatore o un socio uscente clona i repository privati del software proprietario aziendale e lancia un prodotto concorrente quasi identico.",
        "rischio": "Perdita del vantaggio tecnologico e del valore dell'intera impresa digitale.",
        "protocollo": [
            "Acquisire i log di GitHub/GitLab/Bitbucket (clone, commit, chiavi SSH) e cristallizzare la data certa del codice sorgente originario.",
            "Verificare i contratti di lavoro o collaborazione (per i dipendenti i diritti patrimoniali sul software creato nell'esercizio delle mansioni spettano al datore ex art. 12-bis L. 633/1941).",
            "Agire con ricorso cautelare urgente di descrizione e sequestro presso il Tribunale delle Imprese per comparare i codici sorgente tramite CTU.",
            "Valutare la querela penale per rivelazione di segreti industriali (art. 623 c.p.) e accesso abusivo aggravato."
        ],
        "prove": ["Audit log del repository Git", "Contratto di lavoro/sviluppo e clausole IP", "Deposito/marcatura temporale del codice aziendale", "Perizia comparativa informatica"],
        "errori": ["Far sviluppare software critico a freelance senza clausola scritta di cessione integrale dei diritti IP", "Non proteggere i repository con autenticazione forte e audit log", "Avvisare il concorrente prima della descrizione cautelare consentendogli di occultare il codice"]
    },
    {
        "cod": "CYB-45", "slug": "sabotaggio-informatico-ex-amministratore-sistema",
        "cat": "lavoro-segreti", "cat_lbl": "Lavoro, Ex Dipendenti & Segreti", "pilastro": "ex-dipendenti-sottrazione-dati-segreti-aziendali",
        "titolo": "Sabotaggio informatico o blocco password da parte di ex amministratore di sistema",
        "seo_title": "Sabotaggio Informatico Ex Dipendente IT o Admin: Azioni Urgenti",
        "desc": "Come intervenire se un ex responsabile IT o consulente cambia le password di dominio, cancella backup o blocca l'accesso ai server aziendali: penale aggravato e cautelare.",
        "keywords": ["ex dipendente it blocca password server", "sabotaggio informatico azienda denuncia", "abuso operatore sistema 635 bis"],
        "norme": ["Art. 615-ter co. 2 n. 1 e 3 c.p.", "Art. 635-bis e 635-quater c.p.", "Art. 700 c.p.c."],
        "scenario": "A seguito di contrasti economici o licenziamento, l'amministratore di sistema o il consulente IT rifiuta di consegnare le credenziali root/cloud, cambia le password o cancella configurazioni essenziali.",
        "rischio": "Blocco immediato dell'azienda e aggravanti penali pesantissime (abuso della qualita' di operatore del sistema, procedibilita' d'ufficio e pene fino a 8-10 anni).",
        "protocollo": [
            "Inviare diffida PEC con termine strettissimo (24 ore) per la consegna immediata di tutte le credenziali di proprieta' aziendale.",
            "Documentare in copia forense ogni modifica di password, revoca di amministratori o cancellazione di file/backup.",
            "Depositare denuncia immediata in Procura / Polizia Postale evidenziando l'aggravante dell'abuso della qualita' di operatore di sistema (procedibile d'ufficio).",
            "Promuovere ricorso d'urgenza art. 700 c.p.c. per l'ordine giudiziale di consegna immediata delle chiavi di accesso e risarcimento del danno."
        ],
        "prove": ["Audit log cloud/Microsoft 365/Google Workspace/server", "Contratti di intestazione domini e servizi all'azienda", "Diffida PEC rimasta inadempiuta", "Quantificazione giornaliera del danno da fermo"],
        "errori": ["Lasciare i domini o gli account cloud intestati personalmente al tecnico IT invece che all'azienda", "Non avere un secondo account amministratore di emergenza (break-glass)", "Cedere a richieste estorsive per riavere le password senza coinvolgere la Procura"]
    },
    {
        "cod": "CYB-46", "slug": "videosorveglianza-aziendale-telecamere-senza-autorizzazione-inl",
        "cat": "lavoro-segreti", "cat_lbl": "Lavoro, Ex Dipendenti & Segreti", "pilastro": "compliance-gdpr-dpo-privacy",
        "titolo": "Videosorveglianza aziendale senza accordo sindacale o autorizzazione Ispettorato",
        "seo_title": "Telecamere in Azienda senza Autorizzazione INL: Rischi e Difesa",
        "desc": "Come regolarizzare o difendersi da contestazioni dell'Ispettorato del Lavoro e del Garante Privacy per impianti di videosorveglianza aziendale ex art. 4 L. 300/1970.",
        "keywords": ["telecamere azienda senza autorizzazione ispettorato", "art 4 statuto lavoratori videosorveglianza", "sanzione garante telecamere lavoro"],
        "norme": ["Art. 4 L. 300/1970", "Art. 171 D.Lgs. 196/2003", "Art. 38 L. 300/1970", "Art. 13 GDPR"],
        "scenario": "Un'azienda installa telecamere di sicurezza che inquadrano anche aree di lavoro senza accordo sindacale ne' autorizzazione dell'Ispettorato Nazionale del Lavoro (INL), e riceve un'ispezione o denuncia.",
        "rischio": "Sanzione penale contravvenzionale ex art. 38 Statuto Lavoratori, sanzioni amministrative del Garante Privacy e inutilizzabilita' delle riprese.",
        "protocollo": [
            "Disattivare subito la registrazione o oscurare le aree lavorative non autorizzate in attesa del titolo legittimo.",
            "Presentare tempestivamente istanza di autorizzazione all'INL (o accordo con RSA/RSU) corredata da planimetria, scheda tecnica e tempi di conservazione immagini.",
            "Affiggere la cartellonistica di primo livello conforme al Garante e consegnare l'informativa completa ai lavoratori.",
            "In caso di verbale ispettivo gia' notificato, gestire la prescrizione obbligatoria per l'estinzione della contravvenzione e le memorie difensive al Garante."
        ],
        "prove": ["Planimetria coni di ripresa telecamere", "Istanza/autorizzazione INL o accordo sindacale", "Cartellonistica e informativa completa", "Nomina installatore/manutentore art. 28 GDPR"],
        "errori": ["Pensare che il consenso firmato dai singoli dipendenti sostituisca l'autorizzazione INL (e' nullo)", "Conservare le registrazioni per settimane senza giustificazione", "Accedere alle telecamere dallo smartphone del titolare senza regole"]
    },
    {
        "cod": "CYB-47", "slug": "geolocalizzazione-gps-veicoli-aziendali-privacy-lavoro",
        "cat": "lavoro-segreti", "cat_lbl": "Lavoro, Ex Dipendenti & Segreti", "pilastro": "compliance-gdpr-dpo-privacy",
        "titolo": "Geolocalizzazione GPS su furgoni e auto aziendali: regole lavoro e GDPR",
        "seo_title": "GPS Auto Aziendali: Autorizzazione INL, Privacy e Licenziamento",
        "desc": "Regole legali per installare sistemi GPS sui veicoli aziendali: autorizzazione INL, DPIA, conservazione dati e difesa da sanzioni o impugnazioni di licenziamento.",
        "keywords": ["gps furgoni aziendali autorizzazione ispettorato", "geolocalizzazione dipendenti garante privacy", "licenziamento tramite gps aziendale"],
        "norme": ["Art. 4 L. 300/1970", "Art. 35 GDPR (DPIA)", "Art. 13 GDPR"],
        "scenario": "Un'impresa di trasporti o manutenzione utilizza dispositivi satellitari GPS sui mezzi aziendali e intende usare i tracciati a fini organizzativi o disciplinari, oppure riceve un reclamo sindacale/privacy.",
        "rischio": "Sanzioni rilevanti del Garante per monitoraggio continuo non proporzionato e nullita' dei provvedimenti disciplinari basati su dati illeciti.",
        "protocollo": [
            "Ottenere preventivamente accordo sindacale o autorizzazione INL (salvo che lo strumento rientri nelle strette esenzioni di legge).",
            "Eseguire la Valutazione d'Impatto (DPIA ex art. 35 GDPR) e configurare il sistema con campionamento proporzionato, vetrofania sui veicoli e disattivazione nelle pause se uso promiscuo.",
            "Consegnare informativa dettagliata ai conducenti spiegando chiaramente se e come i dati possono essere usati a fini disciplinari.",
            "In caso di contenzioso, verificare l'osservanza di tutte le prescrizioni dell'autorizzazione INL e del Garante."
        ],
        "prove": ["Autorizzazione INL / accordo sindacale", "DPIA geolocalizzazione", "Informativa firmata dai dipendenti", "Contratto art. 28 GDPR con fornitore satellitare"],
        "errori": ["Monitorare in tempo reale continuativo i dipendenti senza necessita' operativa", "Conservare i tracciati GPS per anni", "Usare i dati GPS per contestazioni disciplinari senza informativa preventiva"]
    },
    {
        "cod": "CYB-48", "slug": "smart-working-sicurezza-dati-byod-policy-aziendale",
        "cat": "lavoro-segreti", "cat_lbl": "Lavoro, Ex Dipendenti & Segreti", "pilastro": "compliance-gdpr-dpo-privacy",
        "titolo": "Smart working e dispositivi personali (BYOD): sicurezza dati e responsabilita'",
        "seo_title": "Smart Working e Sicurezza Dati GDPR: Policy e Responsabilita'",
        "desc": "Come prevenire data breach e perdite di segreti aziendali nel lavoro agile: accordi di smart working, policy BYOD, VPN, cifratura e riparto di responsabilita'.",
        "keywords": ["smart working sicurezza dati gdpr", "policy byod azienda privacy", "data breach dipendente smart working"],
        "norme": ["L. 81/2017", "Art. 32 GDPR", "Art. 2105 c.c."],
        "scenario": "Un dipendente in lavoro agile usa il proprio computer di casa o una rete Wi-Fi pubblica senza VPN e provoca l'infezione della rete aziendale o la perdita di documenti riservati.",
        "rischio": "Responsabilita' del datore di lavoro verso il Garante per carenza di misure tecniche e organizzative adeguate ex art. 32 GDPR.",
        "protocollo": [
            "Integrare gli accordi individuali di smart working con un disciplinare vincolante di sicurezza informatica (obbligo VPN, divieto salvataggio su dispositivi personali, blocco schermo).",
            "Limitare o regolamentare rigorosamente il BYOD tramite containerizzazione/MDM e autenticazione a due fattori.",
            "Formare annualmente i lavoratori da remoto contro phishing e social engineering documentando la partecipazione.",
            "In caso di incidente da remoto, isolare subito l'utenza e gestire la procedura data breach."
        ],
        "prove": ["Accordo smart working con allegato sicurezza IT", "Attestati di formazione cybersecurity", "Log VPN e MFA", "Policy BYOD sottoscritta"],
        "errori": ["Consentire l'accesso diretto al gestionale aziendale da PC privati non protetti", "Non includere obblighi di segnalazione immediata di smarrimento o sospetto phishing", "Trascurare il diritto alla disconnessione"]
    },
    {
        "cod": "CYB-49", "slug": "whistleblowing-canale-informatico-crittografia-dlgs-24-2023",
        "cat": "lavoro-segreti", "cat_lbl": "Lavoro, Ex Dipendenti & Segreti", "pilastro": "compliance-gdpr-dpo-privacy",
        "titolo": "Canale informatico Whistleblowing (D.Lgs. 24/2023): crittografia e privacy",
        "seo_title": "Whistleblowing Informatico D.Lgs. 24/2023: Crittografia e GDPR",
        "desc": "Requisiti legali e informatici del canale interno di segnalazione whistleblowing: divieto di email ordinaria, crittografia, DPIA, termini di riscontro e tutela del segnalante.",
        "keywords": ["whistleblowing canale informatico crittografia", "dlgs 24 2023 privacy gdpr", "sanzioni anac whistleblowing"],
        "norme": ["D.Lgs. 24/2023", "Art. 32 e 35 GDPR", "Linee guida ANAC"],
        "scenario": "Un'azienda con oltre 50 dipendenti (o dotata di Modello 231) deve implementare o adeguare la piattaforma digitale di whistleblowing evitando sanzioni ANAC e Garante Privacy.",
        "rischio": "Sanzioni ANAC fino a 50.000 euro per mancata istituzione o gestione non conforme del canale, piu' sanzioni GDPR se l'identita' del segnalante viene esposta.",
        "protocollo": [
            "Adottare una piattaforma dedicata con crittografia end-to-end (evitando la semplice email o PEC aziendale non idonea a garantire riservatezza).",
            "Eseguire la DPIA dedicata al trattamento whistleblowing, nominare il fornitore della piattaforma ex art. 28 GDPR e limitare i log di rete (IP) che potrebbero rivelare il segnalante.",
            "Rispettare rigorosamente i termini di legge: avviso di ricevimento entro 7 giorni e riscontro entro 3 mesi.",
            "Integrare la procedura nel Modello 231 e nel sistema disciplinare aziendale."
        ],
        "prove": ["DPIA piattaforma whistleblowing", "Nomina gestore canale e DPA fornitore", "Procedura interna e informativa pubblicata", "Registro tracciato dei termini 7 giorni / 3 mesi"],
        "errori": ["Usare una casella email interna come canale whistleblowing", "Lasciare visibili gli indirizzi IP dei segnalanti nei log firewall aziendali", "Omettere la consultazione delle rappresentanze sindacali prima dell'attivazione"]
    },
    {
        "cod": "CYB-50", "slug": "concorrenza-sleale-digitale-scraping-ads-marchio-altrui",
        "cat": "lavoro-segreti", "cat_lbl": "Lavoro, Ex Dipendenti & Segreti", "pilastro": "ex-dipendenti-sottrazione-dati-segreti-aziendali",
        "titolo": "Concorrenza sleale digitale: scraping sito, copia catalogo e abuso marchio su Google Ads",
        "seo_title": "Concorrenza Sleale Online: Scraping, Copia Sito e Google Ads",
        "desc": "Tutela d'urgenza per aziende vittime di scraping automatico di cataloghi, clonazione sito web, cybersquatting o uso illecito del proprio marchio nelle campagne Google Ads.",
        "keywords": ["concorrenza sleale online avvocato", "copia sito web catalogo tutela", "concorrente usa mio marchio google ads"],
        "norme": ["Art. 2598 c.c.", "Art. 20 D.Lgs. 30/2005 (CPI)", "Art. 131 CPI", "Art. 700 c.p.c."],
        "scenario": "Un concorrente copia testi, foto e listini di un e-commerce mediante scraping, registra un dominio simile (typosquatting) o compra il marchio altrui su Google Ads creando confusione nei clienti.",
        "rischio": "Perdita di posizionamento SEO, dirottamento di clienti e danno d'immagine immediato.",
        "protocollo": [
            "Cristallizzare subito le pagine concorrenti, gli annunci Google Ads e il codice sorgente con acquisizione forense certificata.",
            "Inviare diffida legale formale con richiesta di rimozione immediata e attivare i canali takedown di Google / registri domini (procedura di riassegnazione .it / UDRP).",
            "In caso di persistenza, depositare ricorso cautelare urgente al Tribunale delle Imprese chiedendo inibitoria con penale per ogni giorno di ritardo.",
            "Chiedere il risarcimento del danno e la retroversione degli utili ex art. 125 CPI."
        ],
        "prove": ["Acquisizione forense certificata di annunci, domini e pagine clonate", "Certificato di registrazione marchio o prova di preuso", "Log server di scraping massivo", "Dati di calo traffico/vendite"],
        "errori": ["Fare semplici screenshot privi di data certa prima di inviare la diffida", "Attendere troppo prima di agire in sede cautelare", "Non verificare la titolarita' del marchio registrato"]
    },

    # ═══════════════════ 6. IDENTITA', DEEPFAKE, REPUTAZIONE & AI (51-60) ═══════════════════
    {
        "cod": "CYB-51", "slug": "revenge-porn-diffusione-foto-video-intimi-rimozione-urgente",
        "cat": "identita-reputazione-ai", "cat_lbl": "Identita', Deepfake & Reputazione", "pilastro": "reputazione-online-deepfake-revenge-porn",
        "titolo": "Revenge porn e diffusione illecita di foto o video intimi (art. 612-ter c.p.)",
        "seo_title": "Revenge Porn Art. 612-ter c.p.: Rimozione Urgente e Querela",
        "desc": "Intervento immediato per bloccare la diffusione di immagini o video sessualmente espliciti senza consenso: procedura urgente Garante Privacy e querela art. 612-ter c.p.",
        "keywords": ["revenge porn cosa fare subito", "art 612 ter cp querela", "rimozione urgente video intimi garante privacy"],
        "norme": ["Art. 612-ter c.p.", "Art. 144-bis D.Lgs. 196/2003", "Art. 17 GDPR"],
        "scenario": "Un ex partner o un terzo diffonde su chat Telegram, WhatsApp, social o siti web immagini o video intimi senza il consenso della persona ritratta.",
        "rischio": "Diffusione virale rapidissima e grave trauma personale e professionale; il reato e' punito con la reclusione da 1 a 6 anni (aumentata se commesso da ex coniuge/partner o con strumenti informatici).",
        "protocollo": [
            "Attivare nella stessa giornata la procedura d'urgenza presso il Garante Privacy (art. 144-bis Codice Privacy) per bloccare preventivamente la diffusione sulle piattaforme.",
            "Cristallizzare forensemente URL, profili, gruppi Telegram e chat senza alterare le prove originali.",
            "Depositare querela penale mirata (termine 6 mesi per l'art. 612-ter c.p.) con richiesta di sequestro preventivo dei dispositivi e dei siti.",
            "Attivare richieste di deindicizzazione urgente sui motori di ricerca e azione civile risarcitoria."
        ],
        "prove": ["Acquisizione forense certificata di URL, profili e chat", "Eventuali minacce di diffusione", "Istanza ex art. 144-bis al Garante", "Querela penale entro 6 mesi"],
        "errori": ["Cancellare le chat con il responsabile per vergogna perdendo le prove", "Cedere a ricatti o richieste di denaro", "Attendere settimane prima di attivare il Garante e la Polizia Postale"]
    },
    {
        "cod": "CYB-52", "slug": "sextortion-ricatto-online-video-chat-cosa-fare",
        "cat": "identita-reputazione-ai", "cat_lbl": "Identita', Deepfake & Reputazione", "pilastro": "reputazione-online-deepfake-revenge-porn",
        "titolo": "Sextortion (ricatto a sfondo sessuale online): come fermare gli estorsori",
        "seo_title": "Sextortion e Ricatto Online: Come Reagire e Difendersi",
        "desc": "Protocollo operativo contro la sextortion via social o videochiamata: perche' non pagare mai, come preservare le prove, bloccare i profili e sporgere denuncia.",
        "keywords": ["sextortion cosa fare", "ricatto video intimo instagram telegram", "estorsione online avvocato"],
        "norme": ["Art. 629 c.p.", "Art. 612-ter c.p.", "Art. 144-bis D.Lgs. 196/2003"],
        "scenario": "Un finto profilo sui social registra una videochiamata privata (o crea un fotomontaggio) e minaccia di inviarla a familiari, colleghi o contatti se non viene pagata subito una somma di denaro.",
        "rischio": "Pagare alimenta richieste estorsive infinite senza alcuna garanzia di cancellazione del materiale.",
        "protocollo": [
            "NON pagare alcuna somma e interrompere ogni dialogo con l'estorsore dopo aver acquisito le prove delle richieste.",
            "Salvare profili, ID numerici, IBAN/wallet/codici di pagamento richiesti e conversazioni integrali.",
            "Rendere privati gli elenchi amici/follower sui social, segnalare i profili estorsivi e attivare il Garante Privacy in caso di minaccia di diffusione.",
            "Sporgere denuncia immediata alla Polizia Postale per estorsione (art. 629 c.p.)."
        ],
        "prove": ["Chat integrali con richieste di denaro", "Estremi dei metodi di pagamento richiesti dall'estorsore", "URL e ID dei profili social usati", "Verbale denuncia Polizia Postale"],
        "errori": ["Pagare una prima tranche sperando che cancellino il video", "Cancellare la chat prima di aver raccolto gli identificativi del ricattatore", "Restare isolati nel panico senza attivare tutele legali"]
    },
    {
        "cod": "CYB-53", "slug": "deepfake-audio-video-intelligenza-artificiale-tutela-legale",
        "cat": "identita-reputazione-ai", "cat_lbl": "Identita', Deepfake & Reputazione", "pilastro": "reputazione-online-deepfake-revenge-porn",
        "titolo": "Deepfake audio o video generato con IA contro privati o dirigenti aziendali",
        "seo_title": "Deepfake Audio e Video IA: Rimozione Urgente e Tutela Penale",
        "desc": "Difesa legale urgente contro video manipolati, clonazione vocale (voice cloning) e deepfake diffamatori o fraudolenti: rimozione, perizia tecnica e azioni penali/civili.",
        "keywords": ["deepfake tutela legale", "clonazione voce truffa azienda", "rimozione video deepfake avvocato"],
        "norme": ["Art. 595 co. 3 c.p.", "Art. 494 c.p.", "Art. 612-ter c.p.", "Reg. UE 2024/1689 (AI Act)", "Art. 10 c.c."],
        "scenario": "Viene diffuso un falso video o audio sintetico creato con IA che ritrae una persona o un amministratore delegato in dichiarazioni false, truffe finanziarie o contesti lesivi della dignita'.",
        "rischio": "Danno reputazionale istantaneo, frodi ai danni di dipendenti/clienti (CEO fraud vocale) e diffusione incontrollata sui social.",
        "protocollo": [
            "Cristallizzare subito il file video/audio originale, i metadati e le pagine social dove e' stato caricato.",
            "Inviare diffide d'urgenza per rimozione immediata alle piattaforme, attivare il Garante Privacy per violazione dei dati biometrici/immagine e richiedere la deindicizzazione.",
            "Depositare querela penale (sostituzione di persona, diffamazione aggravata, truffa o diffusione illecita a seconda del caso) allegando perizia tecnica sulla natura sintetica del contenuto.",
            "Valutare il ricorso cautelare ex art. 700 c.p.c. per la rimozione coattiva e il risarcimento."
        ],
        "prove": ["File originale scaricato con hash", "Perizia tecnica di rilevazione manipolazione IA", "Acquisizione forense dei post/canali", "Prova del danno personale o aziendale"],
        "errori": ["Condividere a propria volta il deepfake aumentandone la viralita'", "Non salvare il file originale prima che venga rimosso (serve per risalire all'autore)", "Sottovalutare il rischio di frodi vocali verso l'amministrazione aziendale"]
    },
    {
        "cod": "CYB-54", "slug": "diritto-oblio-deindicizzazione-google-notizie-vecchie-processi",
        "cat": "identita-reputazione-ai", "cat_lbl": "Identita', Deepfake & Reputazione", "pilastro": "reputazione-online-deepfake-revenge-porn",
        "titolo": "Diritto all'oblio e deindicizzazione da Google di vecchi articoli di cronaca giudiziaria",
        "seo_title": "Diritto all'Oblio Google: Cancellare Vecchie Notizie (Art. 17 GDPR)",
        "desc": "Come ottenere la deindicizzazione da Google e l'aggiornamento o rimozione di vecchi articoli su indagini archiviate, assoluzioni o vicende non piu' attuali ex art. 17 GDPR.",
        "keywords": ["diritto all oblio google avvocato", "cancellare articolo giornale assoluzione", "deindicizzazione art 17 gdpr"],
        "norme": ["Art. 17 GDPR", "Art. 64-ter disp. att. c.p.p.", "Art. 77 GDPR"],
        "scenario": "Cercando il proprio nome su Google compaiono ancora in prima pagina articoli di anni prima relativi a un'indagine poi archiviata, a un'assoluzione o a un procedimento ormai definito e privo di interesse pubblico attuale.",
        "rischio": "Pregiudizio grave e permanente su lavoro, bandi, rapporti bancari e vita privata.",
        "protocollo": [
            "Mappare tutti gli URL esatti (articoli, aggregatori, risultati Google) e acquisire copia del provvedimento giudiziario definitivo (assoluzione, archiviazione, non luogo a procedere).",
            "Per i casi di assoluzione/archiviazione, avvalersi anche del diritto specifico alla deindicizzazione previsto dall'art. 64-ter disp. att. c.p.p.",
            "Presentare istanza giuridicamente motivata sia agli editori (cancellazione/anonimizzazione/aggiornamento) sia ai motori di ricerca (Google/Bing) ex art. 17 GDPR.",
            "In caso di rigetto, proporre reclamo formale al Garante Privacy o ricorso giudiziario."
        ],
        "prove": ["Elenco completo URL e query di ricerca su Google", "Copia sentenza di assoluzione o decreto di archiviazione", "Istanze PEC inviate agli editori e a Google", "Risposta di diniego per eventuale reclamo al Garante"],
        "errori": ["Compilare il modulo standard di Google in due righe senza argomentazione giuridica (spesso respinto)", "Dimenticare di agire anche verso gli editori per l'aggiornamento/deindicizzazione alla fonte", "Non allegare la prova dell'esito favorevole del processo"]
    },
    {
        "cod": "CYB-55", "slug": "account-instagram-facebook-whatsapp-hackerato-recupero",
        "cat": "identita-reputazione-ai", "cat_lbl": "Identita', Deepfake & Reputazione", "pilastro": "reputazione-online-deepfake-revenge-porn",
        "titolo": "Account Instagram, Facebook, LinkedIn o WhatsApp hackerato e usato per truffe",
        "seo_title": "Account Instagram o WhatsApp Hackerato: Recupero e Difesa Legale",
        "desc": "Come recuperare un profilo social aziendale o personale violato, fermare le truffe ai contatti e tutelarsi legalmente contro Meta o terzi in caso di blocco ingiustificato.",
        "keywords": ["account instagram hackerato avvocato", "profilo facebook aziendale rubato recupero", "whatsapp rubato denuncia"],
        "norme": ["Art. 615-ter c.p.", "Art. 494 c.p.", "Reg. UE 2022/2065 (DSA)", "Art. 700 c.p.c."],
        "scenario": "Un profilo social professionale con migliaia di follower o un account Business Manager viene sottratto con cambio email e usato per truffare clienti o addebitare campagne pubblicitarie non autorizzate.",
        "rischio": "Perdita di un asset commerciale rilevante, addebiti su carte collegate e danno d'immagine verso i follower truffati.",
        "protocollo": [
            "Bloccare subito le carte di pagamento collegate al Business Manager e contestare gli addebiti pubblicitari fraudolenti.",
            "Acquisire prove della titolarita' storica dell'account, degli avvisi di cambio email/password ricevuti e dei post truffaldini.",
            "Sporgere denuncia alla Polizia Postale (artt. 615-ter e 494 c.p.) e inviare diffida legale formale ai canali legali della piattaforma (Meta/LinkedIn/Google) invocando anche il Digital Services Act.",
            "Per account aziendali di rilevante valore economico, valutare il ricorso cautelare d'urgenza art. 700 c.p.c. per la restituzione."
        ],
        "prove": ["Email originali di creazione account e avvisi di accesso anomalo", "Fatture pubblicitarie e visura aziendale", "Denuncia Polizia Postale", "Ticket aperti senza esito verso la piattaforma"],
        "errori": ["Pagare finti 'hacker etici' sui social che promettono di recuperare il profilo (e' una truffa)", "Dimenticare di bloccare i metodi di pagamento collegati all'account pubblicitario", "Non avvisare subito i propri clienti/contatti del furto di identita'"]
    },
    {
        "cod": "CYB-56", "slug": "recensioni-false-diffamazione-google-maps-trustpilot",
        "cat": "identita-reputazione-ai", "cat_lbl": "Identita', Deepfake & Reputazione", "pilastro": "reputazione-online-deepfake-revenge-porn",
        "titolo": "Recensioni false e campagne diffamatorie su Google Maps o Trustpilot",
        "seo_title": "Recensioni False su Google e Trustpilot: Rimozione e Querela",
        "desc": "Come far rimuovere recensioni false o diffamatorie su Google Business Profile e portali di recensioni: acquisizione forense, diffida alla piattaforma e querela art. 595 co. 3 c.p.",
        "keywords": ["recensioni false google come rimuovere", "diffamazione recensioni google maps querela", "art 595 comma 3 cp"],
        "norme": ["Art. 595 co. 3 c.p.", "Art. 2598 c.c.", "Reg. UE 2022/2065 (DSA)", "Art. 2043 c.c."],
        "scenario": "Un'attivita' commerciale, un medico o un professionista subisce un attacco coordinato di recensioni a una stella con fatti falsi o offensivi da profili anonimi o concorrenti.",
        "rischio": "Crollo immediato del punteggio Google, perdita di clienti nuovi e danno reputazionale duraturo.",
        "protocollo": [
            "Cristallizzare subito le recensioni, i profili degli autori e le date con acquisizione forense certificata.",
            "Inviare segnalazione giuridicamente argomentata alla piattaforma (violazione policy, diffamazione, assenza di rapporto commerciale reale) ex Digital Services Act.",
            "Sporgere querela per diffamazione aggravata a mezzo internet (art. 595 co. 3 c.p.) entro 3 mesi chiedendo l'identificazione degli account Google/IP.",
            "Se la piattaforma rifiuta la rimozione di contenuti manifestamente illeciti, agire con diffida legale e tutela cautelare civile."
        ],
        "prove": ["Acquisizione forense delle recensioni e profili", "Prova che l'autore non e' mai stato cliente (registro fatture/appuntamenti)", "Calo di richieste/fatturato", "Segnalazioni inviate alla piattaforma"],
        "errori": ["Rispondere pubblicamente insultando il recensore o rivelando dati personali del cliente (violazione GDPR!)", "Attendere oltre 3 mesi perdendo il diritto di querela", "Comprare finte recensioni positive per compensare"]
    },
    {
        "cod": "CYB-57", "slug": "furto-identita-profilo-social-clonato-art-494-cp",
        "cat": "identita-reputazione-ai", "cat_lbl": "Identita', Deepfake & Reputazione", "pilastro": "reputazione-online-deepfake-revenge-porn",
        "titolo": "Profilo social clonato e furto d'identita' digitale (art. 494 c.p.)",
        "seo_title": "Profilo Social Clonato e Furto d'Identita' Art. 494 c.p.: Tutela",
        "desc": "Come far chiudere subito un profilo falso creato con il tuo nome e le tue foto su Instagram, Facebook, TikTok o app di incontri: querela art. 494 c.p. e Garante Privacy.",
        "keywords": ["profilo falso instagram denuncia", "sostituzione di persona art 494 cp", "furto identita social cosa fare"],
        "norme": ["Art. 494 c.p.", "Art. 17 GDPR", "Art. 10 c.c."],
        "scenario": "Qualcuno crea un account falso usando nome, cognome e fotografie di una persona reale per contattare estranei, molestare terzi o chiedere denaro.",
        "rischio": "Coinvolgimento della vittima in truffe, equivoci gravi sul lavoro e lesione del diritto all'immagine.",
        "protocollo": [
            "Acquisire in forma certificata l'URL del profilo clone, le foto rubate e gli eventuali messaggi inviati a terzi.",
            "Inviare segnalazione formale di impersonificazione alla piattaforma e, in caso di ritardo, reclamo al Garante Privacy.",
            "Sporgere denuncia per sostituzione di persona (art. 494 c.p., procedibile d'ufficio).",
            "Avvisare i propri contatti principali senza amplificare inutilmente la visibilita' del profilo falso."
        ],
        "prove": ["URL e ID del profilo falso", "Foto originali di cui si dimostra la titolarita'", "Messaggi ricevuti da terzi contattati dal profilo clone", "Verbale denuncia"],
        "errori": ["Segnalare solo con un clic dall'app senza raccogliere le prove prima della cancellazione", "Ignorare il profilo falso finche' non viene usato per truffare qualcuno", "Rispondere con minacce pubbliche"]
    },
    {
        "cod": "CYB-58", "slug": "uso-chatgpt-ia-generativa-dipendenti-data-breach-segreti",
        "cat": "identita-reputazione-ai", "cat_lbl": "Identita', Deepfake & Reputazione", "pilastro": "contratti-it-cloud-saas-ai-act",
        "titolo": "Dipendenti caricano dati clienti o contratti riservati su IA generative pubbliche",
        "seo_title": "Uso IA Generativa in Azienda: Rischi GDPR, Segreti e Policy AI",
        "desc": "Come prevenire e gestire la fuga di dati personali e segreti aziendali causata dall'uso non regolamentato di chatbot IA pubblici in azienda secondo GDPR e AI Act.",
        "keywords": ["chatgpt dipendenti privacy gdpr", "policy aziendale intelligenza artificiale", "ai literacy ai act 2025 2026"],
        "norme": ["Reg. UE 2024/1689 (AI Act art. 4)", "Art. 5 e 32 GDPR", "Art. 98 CPI"],
        "scenario": "I dipendenti inseriscono contratti riservati, elenchi clienti, bilanci o dati sanitari in versioni gratuite di chatbot IA per riassumerli o tradurli, esponendo l'azienda a data breach e perdita di segretezza.",
        "rischio": "Violazione GDPR per trasferimento dati senza base giuridica/DPA, perdita della tutela del segreto commerciale (art. 98 CPI) e inadempimento dell'obbligo di AI literacy ex art. 4 AI Act.",
        "protocollo": [
            "Mappare subito quali strumenti IA sono usati in azienda (shadow AI) e valutare se sono stati inseriti dati personali o riservati.",
            "Adottare una Policy Aziendale sull'Uso dell'Intelligenza Artificiale che vieti account gratuiti/pubblici per dati aziendali e autorizzi solo versioni enterprise con DPA art. 28 e zero-training.",
            "Avviare sessioni documentate di alfabetizzazione IA (AI literacy, obbligatoria dal 2025 ex art. 4 AI Act).",
            "In caso di esposizione gia' avvenuta di dati sensibili, eseguire la valutazione data breach."
        ],
        "prove": ["Policy aziendale uso IA approvata", "Contratti enterprise IA con clausola no-training e DPA", "Registro formazione AI literacy dipendenti", "Mappatura sistemi IA aziendali"],
        "errori": ["Vietare a parole l'IA senza offrire strumenti aziendali sicuri", "Usare account personali gratuiti per documenti coperti da NDA", "Ignorare l'obbligo di formazione AI literacy gia' vigente"]
    },
    {
        "cod": "CYB-59", "slug": "cyberbullismo-minori-scuola-rimozione-urgente-legge-71-2017",
        "cat": "identita-reputazione-ai", "cat_lbl": "Identita', Deepfake & Reputazione", "pilastro": "reputazione-online-deepfake-revenge-porn",
        "titolo": "Cyberbullismo su minori: oscuramento entro 48 ore e tutela legale (L. 71/2017)",
        "seo_title": "Cyberbullismo Minori Legge 71/2017: Rimozione 48 Ore e Tutela",
        "desc": "Strumenti legali rapidissimi per proteggere un minore vittima di cyberbullismo, gruppi social offensivi o diffusione di video: istanza oscuramento 48 ore, Garante e ammonimento Questore.",
        "keywords": ["cyberbullismo cosa fare subito legge 71 2017", "rimozione contenuti minore 48 ore garante", "ammonimento questore cyberbullismo"],
        "norme": ["L. 71/2017", "Art. 17 GDPR", "Art. 595 e 612-bis c.p."],
        "scenario": "Un minore subisce insulti ripetuti, esclusione coordinata, fotomontaggi o diffusione di video umilianti su WhatsApp, TikTok o Instagram da parte di coetanei.",
        "rischio": "Grave danno psicologico al minore e diffusione virale nella comunita' scolastica.",
        "protocollo": [
            "Acquisire in copia forense chat, profili e video senza allertare preventivamente gli autori.",
            "Inviare istanza di oscuramento/rimozione al gestore della piattaforma ai sensi della L. 71/2017 (che ha 24 ore per prendere in carico e 48 ore per provvedere), con intervento immediato del Garante Privacy in caso di inerzia.",
            "Valutare la richiesta di ammonimento del Questore (per autori minorenni tra 14 e 18 anni) o la querela penale e la segnalazione formale al dirigente scolastico.",
            "Agire civilmente per il risarcimento verso i responsabili e i genitori ex art. 2048 c.c. nei casi piu' gravi."
        ],
        "prove": ["Acquisizione forense chat e post", "Istanza di oscuramento L. 71/2017", "Segnalazione al referente scolastico cyberbullismo", "Referti medici/psicologici del danno subito"],
        "errori": ["Cancellare l'account del minore prima di salvare le prove", "Farsi giustizia da soli scrivendo offese ai genitori altrui", "Non attivare il canale rapido 48 ore previsto dalla Legge 71/2017"]
    },
    {
        "cod": "CYB-60", "slug": "violazione-privacy-condominio-telecamere-chat-whatsapp",
        "cat": "identita-reputazione-ai", "cat_lbl": "Identita', Deepfake & Reputazione", "pilastro": "compliance-gdpr-dpo-privacy",
        "titolo": "Privacy in condominio: telecamere private, bacheche morosi e chat WhatsApp",
        "seo_title": "Privacy Condominio: Telecamere Private, Morosi e Chat WhatsApp",
        "desc": "Tutela legale per telecamere condominiali o del vicino che riprendono spazi altrui, pubblicazione di elenchi morosi e diffamazione nella chat WhatsApp del condominio.",
        "keywords": ["telecamera vicino punta mia porta privacy", "elenco morosi bacheca condominio gdpr", "diffamazione chat whatsapp condominio"],
        "norme": ["Art. 1122-ter c.c.", "Art. 615-bis c.p.", "Art. 595 c.p.", "GDPR"],
        "scenario": "Un vicino installa una telecamera che inquadra l'ingresso altrui o le parti comuni, oppure l'amministratore espone i nomi dei morosi in bacheca o un condomino diffama nella chat del palazzo.",
        "rischio": "Violazione grave della riservatezza domestica (fino al reato di interferenze illecite ex art. 615-bis c.p.), sanzioni GDPR all'amministratore e diffamazione aggravata.",
        "protocollo": [
            "Documentare la posizione e l'angolo di ripresa della telecamera (o acquisire le chat/bacheche con data certa).",
            "Inviare diffida formale al vicino o all'amministratore per l'immediata rimozione/oscuramento dell'angolo illecito o la cessazione della diffusione dei dati.",
            "Attivare il reclamo al Garante Privacy o il ricorso giudiziario per la rimozione e il risarcimento.",
            "In caso di riprese dell'interno dell'abitazione o di offese gravi in chat condominiale, depositare querela penale (art. 615-bis o 595 c.p.)."
        ],
        "prove": ["Fotografie della telecamera e del campo inquadrato", "Screenshot certificati della chat WhatsApp o bacheca", "Delibere assembleari su videosorveglianza", "Diffida PEC"],
        "errori": ["Danneggiare fisicamente la telecamera del vicino (integra reato)", "Installare una telecamera privata che riprende il pianerottolo comune senza limitarla alla propria porta", "Pubblicare i nomi dei condomini morosi in spazi accessibili a estranei"]
    },

    # ═══════════════════ 7. CONTRATTI IT, CLOUD, AI & 231 (61-70) ═══════════════════
    {
        "cod": "CYB-61", "slug": "aggiornamento-modello-231-art-24-bis-legge-90-2024",
        "cat": "contratti-231", "cat_lbl": "Contratti IT, Cloud, AI & 231", "pilastro": "modello-231-reati-informatici",
        "titolo": "Aggiornamento Modello 231 (art. 24-bis) dopo Legge 90/2024 ed estorsione informatica",
        "seo_title": "Aggiornamento Modello 231 Art. 24-bis Post Legge 90/2024",
        "desc": "Come adeguare il Modello Organizzativo 231 ai nuovi reati informatici e all'estorsione informatica introdotti dalla Legge 90/2024 proteggendo la societa' da sanzioni interdittive.",
        "keywords": ["modello 231 art 24 bis legge 90 2024", "aggiornamento mog 231 reati informatici", "estorsione informatica 231"],
        "norme": ["Art. 24-bis D.Lgs. 231/2001", "L. 90/2024", "Art. 629 co. 3 c.p."],
        "scenario": "Una societa' dotata di Modello 231 ante-2024 deve aggiornarlo dopo l'entrata in vigore della Legge 90/2024 che ha inasprito le quote pecuniarie e aggiunto il comma 1-bis sull'estorsione informatica.",
        "rischio": "Un MOG obsoleto non offre piu' l'esimente penale in caso di procedimento 231, esponendo la societa' a sanzioni pecuniarie aumentate e interdittive superiori a 2 anni.",
        "protocollo": [
            "Eseguire una gap analysis mirata su tutti i processi aziendali a rischio reato informatico (gestione credenziali, appalti IT, software, sicurezza dati, gestione crisi).",
            "Riscrivere la Parte Speciale art. 24-bis includendo espressamente l'estorsione informatica e coordinandola con GDPR e NIS2.",
            "Aggiornare il sistema disciplinare e i flussi informativi obbligatori verso l'Organismo di Vigilanza (OdV).",
            "Far approvare formalmente il modello aggiornato dal Consiglio di Amministrazione con piano di formazione."
        ],
        "prove": ["Matrice risk assessment cyber 231", "Parte Speciale art. 24-bis aggiornata", "Delibera CdA di adozione", "Verbali di verifica dell'OdV"],
        "errori": ["Copiare una parte speciale generica slegata dall'infrastruttura IT reale dell'azienda", "Non aggiornare i flussi informativi all'OdV sugli incidenti informatici", "Lasciare il modello fermo al testo pre-2024"]
    },
    {
        "cod": "CYB-62", "slug": "difesa-ente-indagato-art-24-bis-dlgs-231-2001",
        "cat": "contratti-231", "cat_lbl": "Contratti IT, Cloud, AI & 231", "pilastro": "modello-231-reati-informatici",
        "titolo": "Difesa penale dell'azienda indagata ai sensi dell'art. 24-bis D.Lgs. 231/2001",
        "seo_title": "Difesa Azienda Indagata Art. 24-bis D.Lgs. 231/2001: Strategia",
        "desc": "Strategia difensiva quando una societa' riceve contestazione ex D.Lgs. 231/2001 per un reato informatico commesso da un dirigente o dipendente: elusione fraudolenta e misure riparatorie.",
        "keywords": ["difesa ente dlgs 231 reati informatici", "art 24 bis 231 difesa societa", "sanzioni interdittive 231 cyber"],
        "norme": ["Artt. 5, 6, 7, 17, 24-bis D.Lgs. 231/2001"],
        "scenario": "Una societa' viene iscritta nel registro degli illeciti amministrativi dipendenti da reato perche' un suo manager o tecnico IT e' indagato per accesso abusivo ai sistemi di un concorrente o alterazione di dati.",
        "rischio": "Sequestri preventivi di conti aziendali, sanzioni pecuniarie pesanti e misure cautelari interdittive che bloccano gare pubbliche e contratti.",
        "protocollo": [
            "Nominare un difensore autonomo per l'ente (evitando conflitti di interesse con il legale rappresentante eventualmente indagato).",
            "Dimostrare l'assenza di interesse o vantaggio dell'ente oppure l'elusione fraudolenta del Modello 231 da parte del singolo.",
            "Attivare tempestivamente le condotte riparatorie ex art. 17 D.Lgs. 231/2001 (risarcimento, eliminazione carenze organizzative, messa a disposizione del profitto) per evitare sanzioni interdittive.",
            "Impugnare eventuali misure cautelari interdittive o sequestri sproporzionati."
        ],
        "prove": ["Modello 231 e verbali OdV anteriori al fatto", "Log informatici che provano l'elusione delle restrizioni da parte del dipendente", "Piano di rimedio organizzativo post-fatto", "Documentazione ex art. 17 D.Lgs. 231/2001"],
        "errori": ["Far assistere ente e amministratore indagato dallo stesso legale in conflitto di interessi", "Attendere il rinvio a giudizio prima di adottare le condotte riparatorie", "Non produrre le evidenze di vigilanza dell'OdV"]
    },
    {
        "cod": "CYB-63", "slug": "contratto-sviluppo-software-inadempimento-consegna-codice",
        "cat": "contratti-231", "cat_lbl": "Contratti IT, Cloud, AI & 231", "pilastro": "contratti-it-cloud-saas-ai-act",
        "titolo": "Software house inadempiente: ritardi, bug gravi o blocco del codice sorgente",
        "seo_title": "Software House Inadempiente e Blocco Codice: Tutela Legale",
        "desc": "Come tutelare l'azienda quando il fornitore software consegna un gestionale pieno di errori, viola le scadenze o trattiene il codice sorgente e i dati.",
        "keywords": ["software house inadempiente risarcimento", "blocco gestionale fornitore it", "proprieta codice sorgente contratto"],
        "norme": ["Art. 1453 c.c.", "Art. 1218 c.c.", "Art. 696 c.p.c.", "L. 633/1941"],
        "scenario": "Un'impresa paga decine di migliaia di euro per lo sviluppo di un software o e-commerce su misura, ma la software house accumula mesi di ritardo, consegna un prodotto inutilizzabile o rifiuta di rilasciare il codice.",
        "rischio": "Blocco del lancio commerciale, perdita degli investimenti pubblicitari e ostaggio tecnologico (vendor lock-in).",
        "protocollo": [
            "Raccogliere contratto, offerte, specifiche tecniche, email di collaudo e ticket di segnalazione bug.",
            "Inviare formale diffida ad adempiere con termine essenziale (art. 1454 c.c.) contestando analiticamente gli inadempimenti tecnici.",
            "Valutare un Accertamento Tecnico Preventivo (ATP ex art. 696 / 696-bis c.p.c.) per cristallizzare lo stato del software tramite perito del Tribunale prima che venga modificato.",
            "Agire per risoluzione del contratto, restituzione dei compensi, rilascio dei dati/codice e risarcimento dei danni."
        ],
        "prove": ["Contratto e capitolato funzionale", "Storico ticket bug e corrispondenza di sollecito", "Perizia informatica di parte sul codice", "Fatture pagate e prova dei danni da ritardo"],
        "errori": ["Far mettere mano al codice da un terzo sviluppatore prima di aver cristallizzato lo stato dei difetti", "Pagare l'intero saldo prima del collaudo definitivo", "Firmare contratti di sviluppo senza clausola di proprieta' del codice sorgente"]
    },
    {
        "cod": "CYB-64", "slug": "contratto-cloud-saas-lock-in-perdita-dati-fornitore",
        "cat": "contratti-231", "cat_lbl": "Contratti IT, Cloud, AI & 231", "pilastro": "contratti-it-cloud-saas-ai-act",
        "titolo": "Fornitore Cloud/SaaS perde i dati o blocca l'esportazione (vendor lock-in)",
        "seo_title": "Perdita Dati Cloud e Vendor Lock-in SaaS: Azioni Legali e Data Act",
        "desc": "Tutela dell'impresa contro interruzioni gravi del cloud, perdita di archivi o rifiuto del fornitore SaaS di restituire i dati in formato leggibile: SLA, Data Act e azione d'urgenza.",
        "keywords": ["fornitore cloud perde dati risarcimento", "vendor lock in saas restituzione dati", "regolamento europeo data act cloud"],
        "norme": ["Reg. UE 2023/2854 (Data Act)", "Art. 1218 e 1229 c.c.", "Art. 28 GDPR"],
        "scenario": "Al termine di un contratto SaaS o a seguito di un contenzioso su fatture, il fornitore cloud minaccia di sospendere l'accesso bloccando l'operativita' aziendale o chiede somme spropositate per esportare i dati.",
        "rischio": "Paralisi dell'azienda e perdita irreversibile dello storico contabile e commerciale.",
        "protocollo": [
            "Verificare il contratto SaaS, il DPA art. 28 GDPR (che obbliga alla restituzione dei dati personali alla cessazione) e le nuove regole europee sul cambio fornitore (Data Act, Reg. UE 2023/2854).",
            "Inviare diffida urgente via PEC intimando la prosecuzione temporanea dell'accesso e la consegna integrale del database in formato standard aperto.",
            "In caso di blocco imminente, proporre ricorso cautelare d'urgenza art. 700 c.p.c. per impedire la cancellazione dei dati.",
            "Contestare eventuali clausole di esonero da responsabilita' nulle ex art. 1229 c.c. in presenza di dolo o colpa grave del provider."
        ],
        "prove": ["Contratto SaaS, SLA e DPA art. 28", "Comunicazioni di minaccia sospensione servizio", "Prova del danno irreparabile da fermo", "Diffida PEC con richiesta export"],
        "errori": ["Non avere mai una copia locale di backup dei dati caricati in SaaS", "Accettare clausole standard che limitano il risarcimento a un mese di canone senza negoziarle", "Attendere la scadenza del contratto prima di chiedere il formato di esportazione"]
    },
    {
        "cod": "CYB-65", "slug": "trasferimento-dati-extra-ue-usa-scc-tia-gdpr",
        "cat": "contratti-231", "cat_lbl": "Contratti IT, Cloud, AI & 231", "pilastro": "contratti-it-cloud-saas-ai-act",
        "titolo": "Trasferimento di dati personali verso USA e Paesi extra-UE: conformita' GDPR",
        "seo_title": "Trasferimento Dati Extra-UE e USA: GDPR, SCC e TIA",
        "desc": "Come trasferire legalmente dati di clienti e dipendenti verso software, CRM e server statunitensi o extra-UE: Data Privacy Framework, Standard Contractual Clauses e TIA.",
        "keywords": ["trasferimento dati usa gdpr", "clausole contrattuali tipo scc", "data privacy framework ue usa"],
        "norme": ["Artt. 44-49 GDPR", "Decisione di adeguatezza EU-US DPF"],
        "scenario": "Un'azienda italiana utilizza CRM, strumenti di marketing, cloud o servizi di supporto tecnico con sede negli Stati Uniti o in Paesi extra-UE e deve garantire la liceita' dei flussi di dati.",
        "rischio": "Violazione degli artt. 44-49 GDPR, sanzionata nella fascia massima fino a 20 milioni di euro o al 4% del fatturato globale (art. 83 par. 5 GDPR).",
        "protocollo": [
            "Mappare tutti i fornitori software e i loro sub-responsabili verificando dove risiedono fisicamente i server e gli accessi di supporto.",
            "Verificare se il fornitore statunitense e' certificato nell'elenco ufficiale dell'EU-US Data Privacy Framework (DPF).",
            "In mancanza di decisione di adeguatezza, sottoscrivere le Standard Contractual Clauses (SCC) aggiornate ed eseguire una Transfer Impact Assessment (TIA) con misure supplementari (cifratura).",
            "Aggiornare l'informativa privacy (art. 13 GDPR) indicando espressamente i trasferimenti extra-UE e le garanzie adottate."
        ],
        "prove": ["Mappa flussi dati e elenco sub-responsabili", "Verifica certificazione EU-US DPF", "SCC firmate e documento TIA", "Informativa privacy aggiornata"],
        "errori": ["Dare per scontato che un server in Europa escluda trasferimenti se l'assistenza tecnica accede dagli USA o dall'India", "Omettere l'indicazione dei trasferimenti extra-UE nell'informativa", "Non verificare i sub-responsabili di secondo livello"]
    },
    {
        "cod": "CYB-66", "slug": "adeguamento-ai-act-regolamento-ue-2024-1689-imprese",
        "cat": "contratti-231", "cat_lbl": "Contratti IT, Cloud, AI & 231", "pilastro": "contratti-it-cloud-saas-ai-act",
        "titolo": "Adeguamento aziendale all'AI Act (Reg. UE 2024/1689): sistemi ad alto rischio e GPAI",
        "seo_title": "Adeguamento AI Act Reg. UE 2024/1689 per Aziende: Guida Legale",
        "desc": "Come adeguare l'impresa al Regolamento Europeo sull'Intelligenza Artificiale (AI Act): divieti vigenti, classificazione alto rischio (HR, credito, sanita'), trasparenza e contratti.",
        "keywords": ["adeguamento ai act aziende", "regolamento ue 2024 1689 obblighi", "sistemi ia alto rischio sanzioni"],
        "norme": ["Reg. UE 2024/1689 (AI Act)", "Art. 22 GDPR"],
        "scenario": "Un'azienda sviluppa o utilizza software basati su intelligenza artificiale per selezione del personale, valutazione affidabilita' clienti, diagnostica, customer care o automazione decisionale.",
        "rischio": "Sanzioni amministrative pesantissime previste dall'AI Act (fino a 35 milioni di euro o 7% del fatturato per pratiche vietate, e fino a 15 milioni / 3% per altri obblighi).",
        "protocollo": [
            "Censire tutti i sistemi IA sviluppati (provider) o utilizzati (deployer) in azienda e classificarli secondo i 4 livelli di rischio dell'AI Act.",
            "Eliminare subito eventuali pratiche vietate (es. riconoscimento emotivo sul luogo di lavoro o manipolazione comportamentale).",
            "Per i sistemi ad alto rischio (es. screening CV, valutazione lavoratori, credit scoring), predisporre sorveglianza umana, gestione rischi, trasparenza e DPIA coordinata ex art. 22 e 35 GDPR.",
            "Aggiornare i contratti con i fornitori IA e documentare il programma di formazione AI literacy."
        ],
        "prove": ["Registro interno dei sistemi IA", "Schede di classificazione del rischio AI Act", "Informativa trasparenza utenti/lavoratori", "Contratti fornitori IA con garanzie di conformita'"],
        "errori": ["Utilizzare software di selezione CV automatizzati senza supervisione umana ne' informativa", "Confondere la compliance GDPR con la compliance AI Act (sono entrambe necessarie)", "Rimandare il censimento interno fino all'avvio delle ispezioni"]
    },
    {
        "cod": "CYB-67", "slug": "ecommerce-violazione-dati-carte-skimming-magecart",
        "cat": "contratti-231", "cat_lbl": "Contratti IT, Cloud, AI & 231", "pilastro": "data-breach-garante-privacy",
        "titolo": "Attacco skimming (Magecart) su sito e-commerce e furto dati di pagamento",
        "seo_title": "Attacco Skimming su E-Commerce e Furto Dati Carte: Protocollo",
        "desc": "Come gestire legalmente l'iniezione di codice malevolo nel checkout di un sito e-commerce: notifica Garante 72h, avviso clienti, PCI-DSS e rivalsa sulla web agency.",
        "keywords": ["e-commerce hackerato dati carte", "skimming magecart gdpr", "responsabilita web agency sito violato"],
        "norme": ["Art. 32, 33, 34 GDPR", "Art. 615-ter e 635-bis c.p.", "Art. 1218 c.c."],
        "scenario": "Un negozio online scopre che un codice JavaScript malevolo e' stato iniettato nella pagina di checkout sottraendo dati anagrafici e di pagamento dei clienti per diverse settimane.",
        "rischio": "Rischio elevato per migliaia di acquirenti, obbligo di notifica al Garante (72h) e comunicazione ai clienti (art. 34), penali dei circuiti di pagamento e reclami risarcitori.",
        "protocollo": [
            "Mettere subito offline il checkout compromesso conservando una copia forense integrale del codice e dei log server.",
            "Determinare l'intervallo esatto di permanenza dello script malevolo e l'elenco degli ordini coinvolti.",
            "Inviare notifica al Garante entro 72 ore, avvisare subito i clienti coinvolti affinche' blocchino le carte e sporgere denuncia alla Polizia Postale.",
            "Verificare il contratto con la web agency/manutentore per contestare eventuali mancate patch di sicurezza note."
        ],
        "prove": ["Copia forense dello script iniettato e log di modifica file", "Elenco transazioni nel periodo critico", "Contratto manutenzione sito web", "Notifiche Garante e clienti"],
        "errori": ["Ripulire il sito senza salvare la prova forense della falla", "Tacere l'accaduto ai clienti mentre le loro carte vengono svuotate", "Non verificare le vulnerabilita' di plugin/CMS obsoleti"]
    },
    {
        "cod": "CYB-68", "slug": "due-diligence-cyber-privacy-acquisizioni-ma-startup",
        "cat": "contratti-231", "cat_lbl": "Contratti IT, Cloud, AI & 231", "pilastro": "contratti-it-cloud-saas-ai-act",
        "titolo": "Due diligence Cybersecurity, GDPR e IP in acquisizioni aziendali (M&A) e investimenti",
        "seo_title": "Due Diligence Cybersecurity e GDPR in M&A: Tutela Acquirente",
        "desc": "Verifica legale preventiva di rischi privacy, data breach occulti, compliance NIS2, AI Act e titolarita' del software prima di comprare una societa' o investire in una startup.",
        "keywords": ["due diligence gdpr acquisizione azienda", "due diligence cybersecurity ma", "garanzie privacy cessione quote"],
        "norme": ["GDPR", "D.Lgs. 138/2024 (NIS2)", "Reg. UE 2024/1689", "Art. 1490 c.c."],
        "scenario": "Un imprenditore o un investitore sta acquisendo una societa' o un ramo d'azienda digitale e vuole evitare di ereditare sanzioni GDPR/NIS2 latenti, data breach non dichiarati o software con licenze irregolari.",
        "rischio": "Scoprire dopo il closing passivita' milionarie per violazioni privacy, cause IP sul codice sorgente o mancato adeguamento NIS2.",
        "protocollo": [
            "Eseguire una data room review mirata su registro trattamenti, storico incidenti/breach, contratti IT/cloud, licenze open source e perimetro NIS2/AI Act.",
            "Verificare la piena titolarita' della societa' target sul software, sui domini e sulle banche dati clienti.",
            "Tradurre i rischi rilevati in clausole contrattuali di SPA (dichiarazioni e garanzie specifiche, indennizzi dedicati, escrow o rettifica prezzo).",
            "Pianificare la roadmap di integrazione post-closing per allineare la societa' acquisita agli standard del gruppo."
        ],
        "prove": ["Checklist due diligence cyber/privacy/IP", "Report red-flag per la negoziazione prezzo", "Clausole di manleva cyber nello SPA", "Piano di adeguamento post-closing"],
        "errori": ["Comprare una societa' digitale verificando solo i bilanci e ignorando GDPR e titolarita' del software", "Accettare garanzie generiche prive di copertura sui data breach pregressi", "Non verificare la liceita' delle banche dati marketing acquisite"]
    },
    {
        "cod": "CYB-69", "slug": "dpo-esterno-responsabilita-conflitto-interessi-art-37-gdpr",
        "cat": "contratti-231", "cat_lbl": "Contratti IT, Cloud, AI & 231", "pilastro": "compliance-gdpr-dpo-privacy",
        "titolo": "Nomina del DPO (Responsabile Protezione Dati): conflitto d'interessi e requisiti",
        "seo_title": "Nomina DPO Esterno Art. 37 GDPR: Obblighi e Conflitto Interessi",
        "desc": "Come evitare sanzioni del Garante sulla nomina del DPO: chi e' obbligato, incompatibilita' del responsabile IT o amministratore, comunicazione al Garante e contratto DPO esterno.",
        "keywords": ["nomina dpo conflitto interessi garante", "quando e obbligatorio dpo art 37 gdpr", "dpo esterno avvocato"],
        "norme": ["Artt. 37, 38, 39 GDPR"],
        "scenario": "Un'azienda o un ente pubblico nomina come DPO il proprio direttore IT, il CFO o un soggetto privo di autonomia e subisce rilievi ispettivi o sanzioni per conflitto di interessi.",
        "rischio": "Violazione dell'art. 38 par. 6 GDPR con sanzioni fino a 10 milioni o 2% del fatturato e invalidazione dei presidi di vigilanza interna.",
        "protocollo": [
            "Verificare se la nomina del DPO e' obbligatoria ex art. 37 GDPR o comunque raccomandata su base volontaria.",
            "Escludere rigorosamente figure in conflitto di interessi (chi determina finalita' e mezzi del trattamento: amministratori, direttori IT, HR, marketing).",
            "Stipulare un contratto di DPO esterno con garanzie di indipendenza, budget dedicato, accesso diretto ai vertici e assenza di istruzioni sull'esercizio dei compiti.",
            "Comunicare i dati di contatto del DPO sul portale del Garante Privacy e pubblicarli sul sito web."
        ],
        "prove": ["Atto di designazione e contratto DPO", "Ricevuta comunicazione al Garante Privacy", "Verbali di audit periodici del DPO", "Pubblicazione recapito DPO nelle informative"],
        "errori": ["Nominare DPO il responsabile IT o l'amministratore delegato", "Dimenticare di comunicare la nomina o la variazione sul portale del Garante", "Coinvolgere il DPO solo dopo che il data breach e' gia' esploso"]
    },
    {
        "cod": "CYB-70", "slug": "audit-preventivo-simulazione-crisi-cyber-tabletop-exercise",
        "cat": "contratti-231", "cat_lbl": "Contratti IT, Cloud, AI & 231", "pilastro": "direttiva-nis2-acn-legge-90-2024",
        "titolo": "Simulazione di crisi cyber (Tabletop Exercise) e Piano Incident Response legale",
        "seo_title": "Piano Incident Response Legale e Simulazione Crisi Cyber Azienda",
        "desc": "Come preparare il management prima dell'attacco secondo lo standard dei migliori studi USA: piano di risposta 24h/72h, esercitazioni tabletop, ruoli legali e conservazione prove.",
        "keywords": ["piano incident response legale azienda", "tabletop exercise cybersicurezza cda", "preparazione attacco ransomware nis2"],
        "norme": ["Art. 32 GDPR", "Art. 24 D.Lgs. 138/2024 (NIS2)", "Art. 2086 c.c."],
        "scenario": "Un'impresa strutturata vuole evitare il caos decisionale delle prime ore di un attacco ransomware o data breach e dimostrare ad ACN, Garante e assicurazione di avere un piano testato.",
        "rischio": "Senza un piano legale-operativo gia' pronto, durante un attacco vero si perdono le prove forensi, si bucano le 24/72 ore e si commettono errori comunicativi irreversibili.",
        "protocollo": [
            "Redigere un Playbook Legale di Incident Response su misura (ruoli CdA, IT, DPO, legale esterno, forense, PR, assicurazione) conservato anche in copia cartacea offline.",
            "Predisporre i modelli pre-approvati di preallarme ACN (24h), notifica Garante (72h), comunicazione clienti e denuncia Polizia Postale.",
            "Svolgere almeno una volta l'anno una simulazione guidata di attacco (Tabletop Exercise) con il management e documentare il verbale.",
            "Aggiornare il piano dopo ogni simulazione o cambiamento dell'infrastruttura IT."
        ],
        "prove": ["Incident Response Plan approvato dal CdA", "Rubrica di emergenza offline", "Verbale annuale di Tabletop Exercise", "Check periodico di ripristino backup"],
        "errori": ["Tenere il piano di emergenza solo sul server aziendale che il ransomware cifrera'", "Non coinvolgere l'avvocato e il DPO nelle esercitazioni IT", "Non testare mai i tempi reali di attivazione della polizza cyber"]
    }
]
