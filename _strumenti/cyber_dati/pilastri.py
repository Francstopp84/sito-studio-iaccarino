# -*- coding: utf-8 -*-
"""Dati strutturati: 10 Pilastri Cybersicurezza, Bussola Emergenza e 9 Lingue Estere."""

PILASTRI = [
    {
        "num": "01",
        "slug": "data-breach-garante-privacy",
        "titolo": "Data Breach e Notifica al Garante Privacy",
        "h1": "Data Breach: Gestione Crisi e Notifica al Garante entro 72 Ore",
        "seo_title": "Avvocato Data Breach 72 Ore Garante Privacy | Studio Iaccarino",
        "description": "Assistenza legale urgente in caso di data breach: valutazione rischio, notifica al Garante Privacy ex art. 33 GDPR entro 72 ore, comunicazione interessati ex art. 34 e difesa da sanzioni.",
        "sintesi": "Gestione legale immediata di violazioni di dati personali, valutazione del rischio, notifica al Garante entro 72 ore e registro interno.",
        "norme": ["Art. 33 GDPR", "Art. 34 GDPR", "Art. 83 GDPR", "D.Lgs. 196/2003"],
        "cat_scenari": "data-breach",
        "icona": '<path d="M12 2L3 7v6c0 5.5 3.8 10.7 9 12 5.2-1.3 9-6.5 9-12V7l-9-5z"/><path d="M12 8v4"/><circle cx="12" cy="16" r="0.7" fill="currentColor"/>',
        "urgenza": "Scadenza critica: 72 ore (art. 33 GDPR)",
        "intro": [
            "Una violazione dei dati personali (data breach) non riguarda solo gli attacchi hacker: scatta anche per uno smarrimento di computer non cifrato, un invio massivo di email in copia conoscenza visibile, un accesso abusivo di un dipendente o il blocco dei sistemi di un fornitore cloud. Dal momento in cui il titolare ne viene a conoscenza decorre il termine di 72 ore previsto dall'articolo 33 del Regolamento (UE) 2016/679 (GDPR).",
            "Sbagliare la qualificazione dell'incidente espone l'organizzazione a due errori opposti ma ugualmente costosi: omettere una notifica dovuta (con sanzioni amministrative fino a 10 milioni di euro o al 2% del fatturato mondiale annuo ex art. 83 par. 4 GDPR) oppure trasmettere al Garante una comunicazione frettolosa e priva di misure tecniche documentate, innescando un'istruttoria ispettiva.",
            "Lo Studio Legale Avv. Francesco Iaccarino affianca imprese, studi professionali, enti e DPO secondo lo standard internazionale di Breach Coaching: analisi giuridica congiunta con i tecnici IT, redazione della notifica al Garante e dell'eventuale comunicazione agli interessati (art. 34 GDPR), compilazione del registro interno delle violazioni e difesa nel procedimento sanzionatorio."
        ],
        "azioni": [
            "Isolamento dei sistemi coinvolti e blocco delle credenziali compromesse senza cancellare i log di sistema.",
            "Valutazione giuridica del livello di rischio per i diritti e le liberta' degli interessati (rischio improbabile, probabile o elevato).",
            "Verifica dei contratti con responsabili del trattamento e fornitori IT (art. 28 GDPR) e attivazione della polizza cyber.",
            "Predisposizione della notifica al Garante entro 72 ore (anche per fasi successive se l'indagine forense e' in corso) e del registro interno ex art. 33 par. 5 GDPR."
        ],
        "prove": [
            "Log di accesso, firewall, mail server e sistemi EDR con marcatura temporale integra.",
            "Inventario dei database o file esposti e verifica tecnica dell'eventuale cifratura a riposo.",
            "Cronologia esatta della scoperta dell'incidente e delle misure di contenimento adottate.",
            "Nomine a responsabile del trattamento (DPA) e registro dei trattamenti ex art. 30 GDPR."
        ],
        "faq": [
            ("Quando e' obbligatoria la notifica del data breach al Garante Privacy?", "La notifica ex art. 33 GDPR e' obbligatoria senza ingiustificato ritardo e, ove possibile, entro 72 ore dalla conoscenza della violazione, salvo che sia improbabile che l'evento presenti un rischio per i diritti e le liberta' delle persone fisiche."),
            ("Se non ho tutti i dettagli tecnici entro 72 ore cosa devo fare?", "L'articolo 33 par. 4 GDPR consente la notifica per fasi: si invia una prima comunicazione tempestiva entro le 72 ore e si integrano gli esiti forensi successivamente, motivando l'eventuale ritardo."),
            ("Quando devo avvisare anche i clienti o i dipendenti colpiti?", "Solo quando la violazione presenta un rischio elevato per i diritti e le liberta' degli interessati (art. 34 GDPR), salvo che i dati fossero resi incomprensibili tramite cifratura adeguata o che misure successive abbiano eliminato il rischio elevato."),
            ("Cosa succede se non notifico ma annoto tutto nel registro interno?", "La decisione di non notificare va motivata rigorosamente per iscritto nel registro delle violazioni ex art. 33 par. 5 GDPR: in caso di reclamo o ispezione, il Garante verifica la tenuta logica e tecnica di quella valutazione.")
        ]
    },
    {
        "num": "02",
        "slug": "ransomware-estorsione-informatica",
        "titolo": "Ransomware, Estorsione Informatica e Crisi Aziendale",
        "h1": "Attacco Ransomware ed Estorsione Informatica: Difesa Legale e Gestione Crisi",
        "seo_title": "Avvocato Attacco Ransomware e Estorsione Informatica | Napoli Italia",
        "description": "Difesa legale immediata contro attacchi ransomware e doppia estorsione: art. 629 comma 3 c.p. (Legge 90/2024), denunce Polizia Postale, ACN, Garante Privacy e tutela amministratori.",
        "sintesi": "Protocollo legale anti-ransomware: gestione ricatto digitale, art. 629 co. 3 c.p., notifiche ACN e Garante, rapporti con assicurazioni e clienti.",
        "norme": ["Art. 629 co. 3 c.p.", "L. 90/2024", "D.Lgs. 138/2024", "Art. 635-quater c.p."],
        "cat_scenari": "ransomware-nis2",
        "icona": '<rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0110 0v4"/><path d="M12 15v3"/>',
        "urgenza": "Preallarme ACN 24h + Denuncia immediata",
        "intro": [
            "Un attacco ransomware moderno raramente si limita a cifrare server e gestionali: quasi sempre combina il blocco operativo con l'esfiltrazione di archivi riservati e la minaccia di pubblicazione sul dark web (doppia o tripla estorsione). In poche ore l'imprenditore deve governare contemporaneamente fermo produttivo, Polizia Postale, Garante Privacy, Agenzia per la Cybersicurezza Nazionale (ACN), clienti, banche e compagnie assicurative.",
            "Con la Legge 28 giugno 2024, n. 90 il legislatore italiano ha introdotto la fattispecie autonoma di estorsione informatica all'articolo 629, comma 3, del codice penale, inasprendo le pene per i reati informatici presupposti e collegandoli direttamente alla responsabilita' degli enti ex art. 24-bis D.Lgs. 231/2001.",
            "Il nostro intervento coordina il lato legale della sala crisi fin dalla prima ora: preserva la catena di custodia informatica per la denuncia alla Polizia Postale, gestisce il perimetro giuridico rispetto alla richiesta di riscatto e ai rischi sanzionatori internazionali, redige le notifiche ad ACN (24h/72h) e Garante (72h) e protegge gli amministratori da azioni di responsabilita' e contestazioni contrattuali dei clienti."
        ],
        "azioni": [
            "Attivazione della sala crisi legale-tecnica e disconnessione controllata senza spegnere brutalmente macchine con prove in memoria volatile.",
            "Deposito urgente di denuncia-querela presso Polizia Postale / Procura per estorsione informatica (art. 629 co. 3 c.p.), accesso abusivo (art. 615-ter) e danneggiamento (art. 635-bis/quater).",
            "Gestione delle comunicazioni formali a clienti, fornitori, assicurazione cyber e autorita' (ACN entro 24 ore per soggetti NIS2; Garante Privacy entro 72 ore).",
            "Valutazione legale rigorosa sulle richieste estorsive, sulle clausole di forza maggiore nei contratti B2B e sulla difesa del consiglio di amministrazione."
        ],
        "prove": [
            "Copia forense certificata dei file di riscatto (ransom note), indirizzi wallet, chat estorsive e campioni malware.",
            "Log del domain controller, VPN, firewall e tracciati di esfiltrazione dati.",
            "Polizza assicurativa cyber (termini di denuncia sinistro e obblighi di autorizzazione preventiva).",
            "Contratti con fornitori IT / MSP per verificare eventuali profili di inadempimento o rivalsa."
        ],
        "faq": [
            ("Conviene pagare il riscatto in caso di ransomware?", "Pagare il riscatto non garantisce il recupero dei dati ne' la cancellazione degli archivi rubati, ed espone a rischi legali severi (inclusi profili di riciclaggio o sanzioni internazionali se il gruppo e' inserito in liste restrittive). Ogni decisione va valutata con il difensore e le autorita'."),
            ("La denuncia alla Polizia Postale e' obbligatoria?", "E' fortemente raccomandata e spesso indispensabile per attivare la polizza assicurativa, documentare la causa di forza maggiore verso i clienti e tutelare gli amministratori."),
            ("In caso di ransomware devo avvisare sia il Garante Privacy sia l'ACN?", "Se i dati personali sono stati compromessi o esfiltrati scatta l'analisi ex art. 33 GDPR (72 ore al Garante). Se l'azienda rientra nel perimetro NIS2 (D.Lgs. 138/2024) o PA scatta anche il preallarme ACN entro 24 ore."),
            ("Il fornitore IT che gestiva i backup puo' essere responsabile?", "Si', se il contratto di manutenzione o cloud prevedeva obblighi specifici di sicurezza, backup isolati o aggiornamento dei sistemi che sono rimasti inadempiuti.")
        ]
    },
    {
        "num": "03",
        "slug": "direttiva-nis2-acn-legge-90-2024",
        "titolo": "Direttiva NIS2, ACN e Legge Cybersicurezza 90/2024",
        "h1": "Direttiva NIS2 (D.Lgs. 138/2024), ACN e Legge 90/2024: Adeguamento Imprese",
        "seo_title": "Avvocato Direttiva NIS2 D.Lgs. 138/2024 e ACN | Studio Iaccarino",
        "description": "Consulenza legale per adeguamento Direttiva NIS2 (D.Lgs. 138/2024) e Legge 90/2024: verifica perimetro soggetti essenziali e importanti, registrazione portale ACN, governance CdA e notifiche 24h/72h.",
        "sintesi": "Verifica perimetro NIS2, adempimenti portale ACN, responsabilita' personale degli amministratori, catena di fornitura e notifiche 24h/72h.",
        "norme": ["D.Lgs. 138/2024", "Dir. UE 2022/2555", "L. 90/2024", "Art. 25 D.Lgs. 138/2024"],
        "cat_scenari": "ransomware-nis2",
        "icona": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18"/><path d="M12 3a14 14 0 010 18M12 3a14 14 0 000 18"/>',
        "urgenza": "Governance CdA e sanzioni ACN milionarie",
        "intro": [
            "Il Decreto Legislativo 4 settembre 2024, n. 138 ha recepito in Italia la Direttiva europea NIS2 (2022/2555), estendendo obblighi stringenti di sicurezza informatica a migliaia di medie e grandi imprese (soggetti essenziali e soggetti importanti) nei settori critici, manifatturieri, logistici, sanitari, alimentari, digitali e di fornitura ICT.",
            "La vera rivoluzione del D.Lgs. 138/2024 riguarda la governance: gli organi di amministrazione rispondono in prima persona dell'approvazione delle misure di gestione del rischio cyber, della formazione obbligatoria e della sorveglianza sull'attuazione, con potere di ACN di comminare sanzioni amministrative fino a 10 milioni di euro o al 2% del fatturato globale per i soggetti essenziali (e fino a 7 milioni o 1,4% per i soggetti importanti).",
            "Assistiamo le imprese dalla valutazione iniziale di applicabilita' fino alla registrazione sul portale ACN, alla redazione delle policy di incident response (preallarme 24 ore, notifica 72 ore, relazione finale entro 1 mese ex art. 25), alla revisione dei contratti di supply chain e alla difesa in caso di ispezioni o contestazioni dell'Autorita'."
        ],
        "azioni": [
            "Assessment legale di inclusione nel perimetro NIS2 (soggetto essenziale, soggetto importante o fornitore critico di filiera).",
            "Assistenza alla registrazione e aggiornamento annuale sul portale dell'Agenzia per la Cybersicurezza Nazionale (ACN).",
            "Redazione del pacchetto governance CdA, deleghe di funzione, policy di gestione incidenti 24h/72h/30gg e clausole contrattuali per i fornitori ICT.",
            "Raccordo operativo tra adempimenti NIS2, GDPR, Modello 231 e Legge 90/2024."
        ],
        "prove": [
            "Visura camerale, codici ATECO, organigramma societario e dati dimensionali (dipendenti e fatturato/bilancio).",
            "Mappatura dei sistemi informativi critici e dei fornitori esterni della catena digitale.",
            "Delibere del Consiglio di Amministrazione su budget, policy di sicurezza e piani di formazione.",
            "Procedure interne di escalation verso il CSIRT Italia e il punto di contatto ACN."
        ],
        "faq": [
            ("Come so se la mia azienda rientra nella Direttiva NIS2?", "L'inclusione dipende dal settore di attivita' (Allegati I e II del D.Lgs. 138/2024), dalla dimensione aziendale (in linea generale medie e grandi imprese, salvo eccezioni indipendenti dalla dimensione) e dal ruolo nella catena di fornitura di soggetti critici."),
            ("Quali sono i termini di notifica degli incidenti all'ACN?", "L'articolo 25 del D.Lgs. 138/2024 prevede tre passaggi: preallarme entro 24 ore dalla conoscenza dell'incidente significativo, notifica completa entro 72 ore e relazione finale entro 1 mese."),
            ("Gli amministratori rischiano responsabilita' personale con la NIS2?", "Si': il decreto impone agli organi di amministrazione di approvare le misure di gestione dei rischi, sovrintendere alla loro attuazione e seguire formazione specifica, prevedendo responsabilita' per le violazioni."),
            ("Anche le piccole imprese possono essere coinvolte indirettamente?", "Si', per effetto degli obblighi di sicurezza sulla catena di fornitura: i clienti soggetti a NIS2 impongono contrattualmente requisiti di cybersicurezza e audit ai propri fornitori anche di minori dimensioni.")
        ]
    },
    {
        "num": "04",
        "slug": "compliance-gdpr-dpo-privacy",
        "titolo": "Compliance GDPR, Audit Privacy e DPO Esterno",
        "h1": "Compliance GDPR, Audit Privacy Aziendale e Difesa davanti al Garante",
        "seo_title": "Avvocato Privacy GDPR e DPO Esterno | Studio Legale Iaccarino",
        "description": "Consulenza legale GDPR per aziende, studi medici, e-commerce e PA: registro trattamenti, informative, DPIA, nomine art. 28, videosorveglianza, DPO esterno e ricorsi contro sanzioni del Garante.",
        "sintesi": "Adeguamento GDPR sostanziale, valutazioni d'impatto (DPIA), nomine responsabili, videosorveglianza, telemarketing e difesa in ispezioni Garante/GdF.",
        "norme": ["Reg. UE 2016/679", "Artt. 24-39 GDPR", "Art. 83 GDPR", "D.Lgs. 196/2003"],
        "cat_scenari": "data-breach",
        "icona": '<path d="M9 11l3 3L22 4"/><path d="M21 12v7a2 2 0 01-2 2H5a2 2 0 01-2-2V5a2 2 0 012-2h11"/>',
        "urgenza": "Ispezioni GdF / Garante: difesa tecnica immediata",
        "intro": [
            "La protezione dei dati non e' un raccoglitore di moduli fotocopiati in un cassetto: il principio di responsabilizzazione (accountability, artt. 5 e 24 GDPR) impone al titolare di dimostrare in concreto che ogni trattamento e' lecito, proporzionato, sicuro e documentato. Nelle ispezioni del Nucleo Speciale Tutela Privacy e Frodi Tecnologiche della Guardia di Finanza, i modelli generici scaricati da internet crollano alla prima verifica.",
            "Costruiamo sistemi privacy su misura per aziende, cliniche e studi medici, e-commerce, societa' di marketing, condomini e professionisti: mappatura dei flussi, registro dei trattamenti (art. 30), valutazioni d'impatto DPIA (art. 35), accordi di nomina a responsabile del trattamento (art. 28), policy per videosorveglianza, geolocalizzazione, cookie e gestione delle richieste di esercizio dei diritti degli interessati.",
            "In caso di reclamo al Garante, richiesta di informazioni ex art. 157 Codice Privacy o ordinanza ingiunzione sanzionatoria, predisponiamo memorie difensive tecniche e opposizioni giudiziarie davanti al Tribunale competente."
        ],
        "azioni": [
            "Audit iniziale dei trattamenti reali, dei sistemi informativi, dei siti web/app e dei fornitori cloud.",
            "Redazione del pacchetto GDPR su misura: informative, registro art. 30, DPIA art. 35, DPA art. 28, istruzioni agli autorizzati e policy data retention.",
            "Assistenza continuativa o affiancamento al DPO (artt. 37-39 GDPR) e gestione dei reclami degli interessati entro 30 giorni.",
            "Difesa nel procedimento amministrativo davanti al Garante e opposizione giudiziaria contro sanzioni ex art. 152 D.Lgs. 196/2003."
        ],
        "prove": [
            "Registro dei trattamenti aggiornato, organigramma privacy e lettere di designazione degli autorizzati.",
            "Log dei consensi raccolti online (marketing, profilazione, cookie banner) con prova della granularita'.",
            "Accordi art. 28 GDPR firmati con software house, commercialisti, consulenti del lavoro e provider.",
            "Documentazione delle misure tecniche ex art. 32 GDPR (autenticazione forte, backup, cifratura, controllo accessi)."
        ],
        "faq": [
            ("Quando e' obbligatorio nominare un DPO (Responsabile Protezione Dati)?", "L'art. 37 GDPR impone la nomina a enti pubblici e ai soggetti privati la cui attivita' principale consiste nel monitoraggio regolare e sistematico su larga scala o nel trattamento su larga scala di dati particolari (es. sanitari) o giudiziari."),
            ("Quanto tempo ha un'azienda per rispondere a una richiesta di accesso o cancellazione dati?", "L'art. 12 par. 3 GDPR fissa il termine di un mese dal ricevimento della richiesta, prorogabile di ulteriori due mesi solo in casi di particolare complessita' dandone avviso motivato all'interessato."),
            ("Posso contestare una sanzione del Garante Privacy?", "Si': prima in sede procedimentale con memorie difensive e audizione entro i termini fissati dall'Autorita', e poi con ricorso in opposizione davanti al Tribunale ordinario entro 30 giorni dalla notifica dell'ordinanza ingiunzione."),
            ("Le telecamere aziendali richiedono solo il cartello?", "No: oltre all'informativa breve e completa, se riprendono lavoratori o aree di passaggio lavorativo occorre l'accordo sindacale o l'autorizzazione dell'Ispettorato del Lavoro ex art. 4 Statuto dei Lavoratori.")
        ]
    },
    {
        "num": "05",
        "slug": "reati-informatici-difesa-penale",
        "titolo": "Reati Informatici, Polizia Postale e Difesa Penale",
        "h1": "Reati Informatici (Artt. 615-ter, 635-bis, 640-ter c.p.): Difesa Penale e Costituzione Parte Civile",
        "seo_title": "Avvocato Reati Informatici e Cybercrime | Studio Legale Iaccarino",
        "description": "Difesa penale e tutela delle vittime per reati informatici post Legge 90/2024: accesso abusivo 615-ter, frode informatica 640-ter, danneggiamento dati 635-bis/quater, sequestro PC e copia forense.",
        "sintesi": "Difesa di indagati e persone offese per accesso abusivo, frode informatica, danneggiamento sistemi, intercettazioni telematiche e sequestri digitali.",
        "norme": ["Art. 615-ter c.p.", "Art. 635-bis/quater c.p.", "Art. 640-ter c.p.", "L. 90/2024"],
        "cat_scenari": "penale-informatico",
        "icona": '<path d="M12 2L3 7v6c0 5.5 3.8 10.7 9 12 5.2-1.3 9-6.5 9-12V7l-9-5z"/><path d="M9 12l2 2 4-4"/>',
        "urgenza": "Pene aggravate fino a 10-12 anni post L. 90/2024",
        "intro": [
            "La Legge 28 giugno 2024, n. 90 ha impresso una svolta severissima al diritto penale dell'informatica: l'accesso abusivo aggravato a sistemi informatici (art. 615-ter comma 2 c.p.) e' oggi punito con la reclusione da 2 a 10 anni (e fino a 12 anni sui sistemi di interesse pubblico), mentre il danneggiamento di dati e sistemi (artt. 635-bis e 635-quater c.p.) prevede pene base da 2 a 6 anni.",
            "In questo tipo di procedimenti la causa si vince o si perde sulla prova digitale: integrita' della copia forense (hash crittografico), correttezza della catena di custodia, attribuzione reale di un indirizzo IP, log di autenticazione, sequestri probatori di smartphone e server, e garanzie difensive negli accertamenti tecnici irripetibili ex art. 360 c.p.p.",
            "Assistiamo sia chi riceve un avviso di garanzia o subisce una perquisizione informatica della Polizia Postale (anche con ricorso al Tribunale del Riesame contro sequestri indiscriminati di dispositivi aziendali o personali), sia le imprese e i privati vittime di intrusioni che intendono sporgere querela tecnicamente blindata e costituirsi parte civile."
        ],
        "azioni": [
            "Intervento urgente in caso di perquisizione informatica e sequestro di PC, smartphone, server o account cloud.",
            "Verifica della legittimita' del sequestro probatorio e proposizione di riesame per il dissequestro dei dati non pertinenti.",
            "Nomina di consulente tecnico informatico forense di parte per partecipare ad accertamenti irripetibili (art. 360 c.p.p.) e verificare hash, log e attribuzione IP.",
            "Redazione di querele penali tecniche con acquisizione forense certificata delle prove digitali per evitare l'archiviazione."
        ],
        "prove": [
            "Verbale di perquisizione e sequestro informatico, codici hash SHA-256 della copia bit-stream.",
            "Log del provider internet (conservazione dati traffico ex art. 132 D.Lgs. 196/2003), log server e intestazioni email complete (header).",
            "Perizia informatica forense su dispositivi, cloud, cronologia accessi e metadati dei file.",
            "Documentazione della quantificazione del danno economico da fermo sistemi o sottrazione dati."
        ],
        "faq": [
            ("La Polizia Postale puo' sequestrarmi tutto il computer o il telefono aziendale?", "Il sequestro probatorio deve rispettare il principio di proporzionalita' e pertinenza: se vengono sequestrati interi archivi o dispositivi indispensabili al lavoro senza estrazione mirata, e' possibile proporre istanza di riesame entro 10 giorni."),
            ("Quanto tempo ho per sporgere querela per un reato informatico?", "Per i reati procedibili a querela (come l'art. 615-ter comma 1 o l'art. 640-ter comma 1 c.p.) il termine e' di 3 mesi dalla notizia del fatto. Per l'art. 612-ter c.p. (revenge porn) il termine e' di 6 mesi. Molte ipotesi aggravate sono procedibili d'ufficio."),
            ("Un indirizzo IP basta da solo a condannare l'intestatario della linea?", "No: l'indirizzo IP identifica la connessione di rete, non automaticamente la persona fisica seduta alla tastiera. La difesa tecnica verifica Wi-Fi condivisi, dispositivi collegati, log di accesso e alibi digitali."),
            ("Come funziona la nuova attenuante introdotta dalla Legge 90/2024?", "La riforma ha introdotto una riduzione di pena fino a due terzi per chi si adopera concretamente per evitare conseguenze ulteriori dell'attacco o favorire il recupero dei dati e dei proventi.")
        ]
    },
    {
        "num": "06",
        "slug": "truffe-online-phishing-sim-swap-banche",
        "titolo": "Truffe Online, Phishing, SIM Swap e Rimborso Banche / ABF",
        "h1": "Phishing, Smishing, SIM Swap e Frodi Bancarie: Recupero Somme e Responsabilita' della Banca",
        "seo_title": "Avvocato Phishing, Truffe Online e Rimborso Banca ABF | Studio Iaccarino",
        "description": "Recupero soldi da phishing, smishing, spoofing bancario, SIM swap, frode BEC e truffe crypto: disconoscimento operazioni D.Lgs. 11/2010, reclamo banca, ricorso ABF e azione giudiziaria.",
        "sintesi": "Tutela contro svuotamento conto corrente, falsi SMS bancari, SIM swap, bonifici deviati (frode BEC) e piattaforme truffaldine di trading/crypto.",
        "norme": ["D.Lgs. 11/2010 artt. 10-12", "PSD2", "Art. 640-ter c.p.", "Ricorso ABF"],
        "cat_scenari": "truffe-banche",
        "icona": '<rect x="2" y="5" width="20" height="14" rx="2"/><line x1="2" y1="10" x2="22" y2="10"/><path d="M7 15h4"/>',
        "urgenza": "Disconoscimento immediato e blocco bonifici",
        "intro": [
            "Quando un conto corrente viene svuotato tramite falsi SMS della banca (spoofing/smishing), finte telefonate dell'ufficio antifrode (vishing), clonazione della SIM (SIM swap) o intrusione nell'home banking, le banche tendono quasi sempre a respingere il rimborso scaricando la colpa sul cliente.",
            "La legge pero' dice altro: ai sensi degli articoli 10 e 12 del D.Lgs. 11/2010 (recepimento PSD2), spetta alla banca provare in modo rigoroso che l'operazione e' stata autenticata con autenticazione forte (SCA), correttamente registrata e contabilizzata e non affetta da malfunzionamenti, nonche' dimostrare il dolo o la colpa grave del correntista. La colpa grave non si presume mai.",
            "Assistiamo privati e aziende dal disconoscimento immediato delle operazioni alla denuncia penale, dal reclamo formale alla banca al ricorso davanti all'Arbitro Bancario Finanziario (ABF) o al Tribunale civile, includendo le frodi aziendali su fatture modificate via email (frode BEC) e le truffe su false piattaforme di investimento e criptovalute."
        ],
        "azioni": [
            "Blocco immediato di carte, credenziali e richiesta di recall dei bonifici appena disposti.",
            "Disconoscimento formale delle operazioni non autorizzate e denuncia dettagliata a Polizia Postale / Carabinieri.",
            "Reclamo motivato alla banca con richiesta integrale dei log di autenticazione SCA ex art. 10 D.Lgs. 11/2010.",
            "Ricorso all'Arbitro Bancario Finanziario (ABF) o causa civile per il rimborso integrale delle somme sottratte e del danno."
        ],
        "prove": [
            "Screenshot integrali di SMS spoofing (inseriti nella stessa chat della banca), chiamate ricevute, email e notifiche push.",
            "Estratti conto, ricevute di bonifici/pagamenti disconosciuti e cronologia esatta degli orari.",
            "Denuncia alle forze dell'ordine e reclamo scritto con PEC o raccomandata alla banca.",
            "Risposta della banca e log tecnici di autenticazione forniti dall'intermediario."
        ],
        "faq": [
            ("Se ho ricevuto un falso SMS dentro la chat ufficiale della mia banca ho diritto al rimborso?", "Lo spoofing del mittente SMS e' una tecnica molto insidiosa: se la banca non dimostra una colpa grave effettiva del cliente e non produce log tecnici completi sull'autenticazione forte (SCA), l'ABF e i Tribunali riconoscono spesso il diritto al rimborso."),
            ("Quanto tempo ho per disconoscere un'operazione bancaria non autorizzata?", "Il disconoscimento va fatto senza indugio appena scoperta l'anomalia e comunque entro il limite massimo di 13 mesi dalla data di addebito (art. 9 D.Lgs. 11/2010). Agire nelle prime ore e' decisivo anche per tentare il recall."),
            ("La banca puo' rifiutare il rimborso dicendo solo che sono stati usati i miei codici OTP?", "No: l'art. 10 comma 2 del D.Lgs. 11/2010 stabilisce espressamente che l'utilizzo dello strumento di pagamento registrato dalla banca non e' di per se' necessariamente sufficiente a dimostrare che l'operazione sia stata autorizzata o che il cliente abbia agito con colpa grave."),
            ("Cosa fare in caso di SIM swap (scheda telefonica clonata)?", "Oltre alla banca, si contesta la responsabilita' dell'operatore telefonico che ha eseguito la sostituzione della SIM senza controlli idonei, agendo in sede civile e davanti al Co.Re.Com. / AGCOM.")
        ]
    },
    {
        "num": "07",
        "slug": "ex-dipendenti-sottrazione-dati-segreti-aziendali",
        "titolo": "Ex Dipendenti Infedeli, Furto Database e Segreti Industriali",
        "h1": "Ex Dipendente Ruba Clienti, Database o Segreti Aziendali: Azioni Penali e Cautelari",
        "seo_title": "Ex Dipendente Ruba Database Clienti e Segreti | Avvocato Napoli Italia",
        "description": "Tutela urgente per imprese contro ex dipendenti infedeli: sottrazione liste clienti, segreti commerciali artt. 98-99 CPI, art. 615-ter e 623 c.p., concorrenza sleale, ricorso d'urgenza art. 700 c.p.c.",
        "sintesi": "Azioni d'urgenza per sottrazione di database clienti, listini, codice sorgente, know-how, controlli difensivi ex art. 4 Statuto Lavoratori e concorrenza sleale.",
        "norme": ["Artt. 98-99 CPI", "Art. 2105 c.c.", "Art. 2598 c.c.", "Art. 4 L. 300/1970"],
        "cat_scenari": "lavoro-segreti",
        "icona": '<path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 11l-4 4m0-4l4 4"/>',
        "urgenza": "Sequestro/inibitoria urgente prima dello sviamento clienti",
        "intro": [
            "Una delle minacce informatiche piu' dannose per le PMI italiane arriva dall'interno: dipendenti, collaboratori o ex soci che prima delle dimissioni scaricano su chiavetta USB o cloud personale il CRM clienti, i listini riservati, i progetti tecnici o il codice sorgente per passarli a un concorrente o avviare un'attivita' parallela.",
            "Agire in modo scomposto (per esempio frugando nella posta privata del dipendente senza rispettare l'articolo 4 dello Statuto dei Lavoratori) rischia pero' di rendere inutilizzabili le prove in giudizio e di trasformare l'azienda da vittima a sanzionata dal Garante Privacy.",
            "Costruiamo un intervento chirurgico su doppio binario: acquisizione forense legittima dei log e dei dispositivi aziendali (controlli difensivi mirati ex post), azione cautelare d'urgenza davanti alla Sezione Specializzata Impresa (descrizione, inibitoria, sequestro ex artt. 129-131 CPI e art. 700 c.p.c.), licenziamento per giusta causa e denuncia penale ex artt. 615-ter e 623 c.p."
        ],
        "azioni": [
            "Revoca immediata delle credenziali e cristallizzazione forense di PC aziendale, log cloud, email aziendali e tracciati USB.",
            "Verifica della legittimita' dei controlli difensivi secondo l'art. 4 L. 300/1970 e le linee guida del Garante Privacy.",
            "Ricorso cautelare urgente (descrizione/inibitoria/sequestro) per bloccare l'uso dei segreti commerciali e lo sviamento di clientela.",
            "Contestazione disciplinare / licenziamento per giusta causa, richiesta risarcitoria civile e querela penale (artt. 615-ter, 623 c.p.)."
        ],
        "prove": [
            "Log di download massivo da CRM/SharePoint/Drive, collegamenti dispositivi USB, inoltri email a caselle private.",
            "Policy IT aziendale consegnata al lavoratore sull'uso degli strumenti aziendali e sulla riservatezza.",
            "Accordi di riservatezza (NDA), patti di non concorrenza (art. 2125 c.c.) e prova delle misure di segretezza ex art. 98 CPI.",
            "Segnalazioni di clienti contattati impropriamente con dati o offerte riservate."
        ],
        "faq": [
            ("Posso leggere le email aziendali di un dipendente sospettato di rubare dati?", "Solo nel rispetto rigoroso delle condizioni dell'art. 4 Statuto dei Lavoratori e dei principi sui controlli difensivi mirati: servono una policy IT preventiva, un fondato sospetto di illecito e un'acquisizione proporzionata e tracciata."),
            ("Una lista clienti e' protetta come segreto commerciale?", "Si', se soddisfa i requisiti dell'art. 98 del Codice della Proprieta' Industriale (D.Lgs. 30/2005): informazioni non generalmente note, dotate di valore economico in quanto segrete e sottoposte a misure ragionevolmente adeguate a mantenerle segrete."),
            ("Quanto velocemente si puo' bloccare l'ex dipendente che contatta i miei clienti?", "Con un ricorso cautelare d'urgenza (anche inaudita altera parte nei casi piu' gravi) si puo' chiedere al Tribunale l'inibitoria immediata e la descrizione/sequestro dei file sottratti."),
            ("Se il dipendente aveva le password per lavoro, e' comunque accesso abusivo art. 615-ter c.p.?", "Si': chi e' abilitato all'accesso ma si trattiene o accede per finalita' ontologicamente estranee e contrarie alle condizioni stabilite dal titolare del sistema integra l'accesso abusivo aggravato.")
        ]
    },
    {
        "num": "08",
        "slug": "modello-231-reati-informatici",
        "titolo": "Modello 231 e Responsabilita' Enti per Reati Informatici",
        "h1": "Modello 231 e Art. 24-bis D.Lgs. 231/2001: Aggiornamento Post Legge 90/2024",
        "seo_title": "Avvocato Modello 231 Reati Informatici Art. 24-bis | Studio Iaccarino",
        "description": "Aggiornamento Modelli Organizzativi 231 per delitti informatici (art. 24-bis D.Lgs. 231/2001), estorsione informatica L. 90/2024, protocolli cyber per OdV e difesa penale dell'ente.",
        "sintesi": "Aggiornamento MOG 231 all'art. 24-bis dopo la L. 90/2024, inclusione del reato di estorsione informatica, flussi verso l'OdV e difesa dell'ente.",
        "norme": ["Art. 24-bis D.Lgs. 231/2001", "L. 90/2024", "Art. 629 co. 3 c.p.", "D.Lgs. 138/2024"],
        "cat_scenari": "contratti-231",
        "icona": '<path d="M3 21h18"/><path d="M5 21V7l7-4 7 4v14"/><path d="M9 21v-6h6v6"/>',
        "urgenza": "Sanzioni pecuniarie innalzate e interdittive fino a 2+ anni",
        "intro": [
            "La Legge 28 giugno 2024, n. 90 ha profondamente riformato l'articolo 24-bis del D.Lgs. 231/2001 sui delitti informatici e trattamento illecito di dati: ha innalzato le sanzioni pecuniarie a carico delle societa' e ha inserito il nuovo reato presupposto dell'estorsione informatica (art. 629 comma 3 c.p.), prevedendo anche pesanti sanzioni interdittive (come l'esclusione da appalti, finanziamenti o la sospensione dell'attivita').",
            "Un Modello Organizzativo 231 non aggiornato dopo luglio 2024 espone la societa' e il suo management a una vulnerabilita' gravissima, sia in sede penale sia nelle gare d'appalto pubbliche e nei rapporti con grandi committenti soggetti a NIS2.",
            "Affianchiamo societa' e Organismi di Vigilanza (OdV) nella mappatura dei rischi informatici (risk assessment cyber 231), nell'aggiornamento della Parte Speciale Reati Informatici, nell'integrazione con le procedure GDPR e NIS2, e nella difesa giudiziale dell'ente indagato."
        ],
        "azioni": [
            "Gap analysis del Modello 231 esistente rispetto alla Legge 90/2024 e ai nuovi reati presupposto cyber.",
            "Redazione e aggiornamento della Parte Speciale art. 24-bis D.Lgs. 231/2001 e dei protocolli di gestione credenziali, privilegi admin e incident response.",
            "Definizione dei flussi informativi periodici e ad evento verso l'Organismo di Vigilanza (OdV).",
            "Difesa penale dell'ente nei procedimenti ex D.Lgs. 231/2001 e strategie di esenzione da responsabilita' ex artt. 6 e 7."
        ],
        "prove": [
            "Modello 231 vigente, codice etico, sistema disciplinare e verbali dell'Organismo di Vigilanza.",
            "Mappatura dei processi aziendali sensibili (IT, appalti, gestione dati clienti/fornitori, sviluppo software).",
            "Evidenze di formazione periodica del personale e test tecnici di sicurezza (vulnerability assessment / audit).",
            "Procedure di segregazione dei compiti e gestione degli accessi amministrativi."
        ],
        "faq": [
            ("E' obbligatorio aggiornare il Modello 231 dopo la Legge 90/2024?", "Pur essendo l'adozione del Modello 231 una facolta' e non un obbligo di legge generale, un modello non aggiornato ai nuovi reati e alle nuove soglie dell'art. 24-bis perde efficacia esimente davanti al giudice penale."),
            ("Che cosa rischia un'azienda coinvolta in un procedimento ex art. 24-bis D.Lgs. 231/2001?", "Rischia sanzioni pecuniarie calcolate per quote fortemente aumentate dalla L. 90/2024, la confisca del profitto e sanzioni interdittive che possono paralizzare l'operativita' aziendale."),
            ("Il Modello 231 puo' integrarsi con GDPR e NIS2?", "Si', ed e' la soluzione piu' efficiente: un sistema integrato evita duplicazioni documentali e rende i presidi di sicurezza coerenti davanti a Garante, ACN e giudice penale."),
            ("L'Organismo di Vigilanza deve essere informato di un attacco informatico?", "Si', i flussi informativi ad evento devono prevedere la segnalazione immediata all'OdV di ogni incidente significativo o violazione dei protocolli IT.")
        ]
    },
    {
        "num": "09",
        "slug": "reputazione-online-deepfake-revenge-porn",
        "titolo": "Reputazione Digitale, Deepfake, Furto d'Identita' e Revenge Porn",
        "h1": "Reputazione Online, Deepfake, Furto d'Identita' e Rimozione Contenuti Illeciti",
        "seo_title": "Avvocato Reputazione Online, Deepfake e Revenge Porn | Studio Iaccarino",
        "description": "Intervento urgente per rimozione foto/video intimi (art. 612-ter c.p.), deepfake IA, furto d'identita' social, diffamazione online art. 595 co. 3 c.p. e diritto all'oblio ex art. 17 GDPR.",
        "sintesi": "Rimozione urgente di contenuti illeciti, deepfake, sextortion, account clonati, recensioni diffamatorie e deindicizzazione da Google.",
        "norme": ["Art. 612-ter c.p.", "Art. 17 GDPR", "Art. 595 co. 3 c.p.", "Art. 494 c.p."],
        "cat_scenari": "identita-reputazione-ai",
        "icona": '<circle cx="12" cy="12" r="3"/><path d="M2 12s4-7 10-7 10 7 10 7-4 7-10 7-10-7-10-7z"/>',
        "urgenza": "Rimozione d'urgenza e reclamo Garante Privacy",
        "intro": [
            "Oggi bastano pochi minuti per distruggere la reputazione personale o professionale di qualcuno: video o immagini intime diffuse senza consenso (revenge porn, art. 612-ter c.p.), falsi video o audio generati con intelligenza artificiale (deepfake), profili social clonati (art. 494 c.p.), recensioni false orchestrate su Google o vecchi articoli di cronaca che continuano a comparire in prima pagina.",
            "In questi casi la rapidita' e la precisione tecnica fanno la differenza tra una diffusione virale incontrollabile e la rimozione immediata. Cancellare solo lo screenshot o scrivere messaggi informali ai social quasi mai basta.",
            "Interveniamo con protocollo d'urgenza: acquisizione forense certificata delle pagine web e dei metadati, istanze legali dirette alle piattaforme e ai motori di ricerca, procedura d'urgenza davanti al Garante Privacy per la rimozione di contenuti intimi e il diritto all'oblio (art. 17 GDPR), ricorso cautelare civile art. 700 c.p.c. e querela penale mirata."
        ],
        "azioni": [
            "Cristallizzazione forense certificata (data certa, URL, hash, sorgente pagina) prima che l'autore cancelli le tracce.",
            "Attivazione immediata delle procedure di rimozione verso piattaforme social, motori di ricerca e hosting provider.",
            "Istanza urgente al Garante per la protezione dei dati personali (incluso il canale dedicato ai contenuti sessualmente espliciti e deepfake) e richiesta di deindicizzazione ex art. 17 GDPR.",
            "Querela penale (artt. 612-ter, 595 co. 3, 494 c.p.) e ricorso civile d'urgenza art. 700 c.p.c. per la rimozione e il risarcimento."
        ],
        "prove": [
            "Acquisizione forense certificata delle pagine web, profili, commenti, URL e conversazioni originali.",
            "Chat, email o richieste estorsive (sextortion) conservate integralmente sul dispositivo originale.",
            "Documentazione della perdita di clienti, incarichi o del danno reputazionale e morale subito.",
            "Esiti delle segnalazioni gia' inviate alle piattaforme o ai motori di ricerca."
        ],
        "faq": [
            ("Come faccio a far rimuovere subito foto o video intimi pubblicati senza il mio consenso?", "Oltre alla querela ex art. 612-ter c.p. (termine 6 mesi), si puo' attivare subito la procedura d'urgenza presso il Garante Privacy (art. 144-bis Codice Privacy) che interviene rapidamente verso le piattaforme per bloccare la diffusione."),
            ("Posso far cancellare da Google un vecchio articolo di giornale su un processo finito con assoluzione?", "Si': l'articolo 17 GDPR riconosce il diritto alla deindicizzazione (diritto all'oblio) quando la notizia non e' piu' attuale, completa o aggiornata rispetto all'esito favorevole del procedimento."),
            ("Un video o audio deepfake creato con IA contro di me e' reato?", "A seconda del contenuto e dello scopo, integra gravi fattispecie penali (diffamazione aggravata, sostituzione di persona, estorsione, diffusione illecita di contenuti intimi) oltre a dare diritto a rimozione immediata e risarcimento civile."),
            ("Basta fare uno screenshot dal telefono come prova in tribunale?", "Uno screenshot semplice puo' essere contestato dalla controparte. Prima di agire e' sempre consigliabile un'acquisizione forense certificata che garantisca autenticita', URL, codice sorgente e data certa.")
        ]
    },
    {
        "num": "10",
        "slug": "contratti-it-cloud-saas-ai-act",
        "titolo": "Contratti IT, Cloud, SaaS, E-Commerce e AI Act",
        "h1": "Contratti IT, Cloud, SaaS, E-Commerce e Compliance AI Act (Reg. UE 2024/1689)",
        "seo_title": "Avvocato Contratti IT, Cloud, SaaS e AI Act | Studio Legale Iaccarino",
        "description": "Redazione e revisione legale di contratti software, Cloud, SaaS, DPA art. 28 GDPR, SLA di cybersicurezza, termini e-commerce e adeguamento al Regolamento Europeo AI Act (UE 2024/1689).",
        "sintesi": "Contrattualistica tecnologica blindata: sviluppo software, SLA sicurezza, DPA fornitori cloud, trasferimenti dati extra-UE e governance AI Act.",
        "norme": ["Reg. UE 2024/1689", "Art. 28 GDPR", "Artt. 44-49 GDPR", "D.Lgs. 70/2003"],
        "cat_scenari": "contratti-231",
        "icona": '<path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="8" y1="13" x2="16" y2="13"/><line x1="8" y1="17" x2="13" y2="17"/>',
        "urgenza": "AI Act pienamente operativo 2025-2026",
        "intro": [
            "Gran parte del contenzioso tecnologico nasce da contratti IT firmati di fretta: software consegnati in ritardo o pieni di vulnerabilita', fornitori cloud che limitano la propria responsabilita' a pochi euro in caso di perdita dati, clausole di lock-in che impediscono di recuperare il proprio database o strumenti di intelligenza artificiale introdotti in azienda senza regole.",
            "Con l'entrata in applicazione scaglionata del Regolamento Europeo sull'Intelligenza Artificiale (AI Act, Reg. UE 2024/1689) tra il 2025 e il 2026, le imprese devono classificare i sistemi IA utilizzati (rischio inaccettabile, alto rischio, trasparenza, GPAI), adempiere agli obblighi di alfabetizzazione IA (AI literacy) e aggiornare policy interne e contratti con i fornitori.",
            "Redigiamo e negoziamo contratti tecnologici su misura per software house, startup, PMI e grandi committenti: sviluppo software e licenze SaaS, Data Processing Agreement (DPA ex art. 28 GDPR), clausole di cybersicurezza NIS2, trasferimenti di dati extra-UE, compliance e-commerce e governance contrattuale dell'intelligenza artificiale."
        ],
        "azioni": [
            "Redazione e negoziazione di contratti di sviluppo software, licenza SaaS, manutenzione evolutiva, cloud e outsourcing IT.",
            "Inserimento di SLA di sicurezza, obblighi di notifica incidenti in 12/24 ore, clausole di exit/portabilita' dati e limiti di responsabilita' equilibrati.",
            "Verifica legale dei trasferimenti di dati extra-UE (decisioni di adeguatezza, SCC, TIA) e accordi art. 28 GDPR.",
            "Mappatura dei sistemi di intelligenza artificiale aziendali, policy dipendenti sull'uso di IA generativa e adeguamento al Reg. UE 2024/1689."
        ],
        "prove": [
            "Contratti IT/Cloud vigenti, offerte commerciali, capitolati tecnici e allegati SLA.",
            "Elenco dei software, API e strumenti di intelligenza artificiale utilizzati dai reparti aziendali.",
            "Accordi DPA e sub-responsabili dichiarati dai fornitori tecnologici.",
            "Termini e condizioni e-commerce, privacy policy e flussi di checkout/consenso."
        ],
        "faq": [
            ("Quali clausole non possono mancare in un contratto cloud o SaaS aziendale?", "Sono essenziali: livelli di servizio (SLA) con penali, misure tecniche di sicurezza, obbligo del fornitore di notificare un data breach entro poche ore, proprieta' esclusiva dei dati del cliente e clausola di restituzione/exit senza ostacoli."),
            ("Cosa cambia per le aziende con l'AI Act nel 2025-2026?", "Sono gia' vietate le pratiche di IA a rischio inaccettabile e vigono obblighi di alfabetizzazione del personale (AI literacy), regole sui modelli GPAI e requisiti rigorosi per i sistemi IA ad alto rischio (es. selezione del personale, credito, sanita')."),
            ("I dipendenti possono caricare contratti o dati clienti su strumenti di IA pubblica?", "Senza una policy aziendale e un account enterprise con garanzie contrattuali ex art. 28 GDPR, caricare dati personali o segreti aziendali su piattaforme IA pubbliche puo' configurare una violazione GDPR e perdita di segretezza."),
            ("Come tutelarmi se una software house non consegna o blocca il gestionale?", "Si interviene con diffida tecnica ad adempiere, accertamento tecnico preventivo sullo stato del codice e, se necessario, azione cautelare per il rilascio dei dati aziendali e risarcimento del danno.")
        ]
    }
]

COMPASS_DATA = {
    "ransomware": {
        "title": "Attacco Ransomware o Blocco Sistemi in Corso",
        "desc": "Ogni minuto conta per evitare la propagazione, preservare le prove digitali e rispettare le scadenze di legge verso ACN e Garante Privacy.",
        "steps": [
            "1. Isola la rete dei dispositivi colpiti senza formattare o cancellare log e ransom note.",
            "2. Attiva subito il difensore e il tecnico forense per la copia certificata delle prove prima del ripristino.",
            "3. Avvia il conteggio legale: 24 ore per preallarme ACN (se soggetto NIS2/PA) e 72 ore per notifica Garante (art. 33 GDPR) + denuncia Polizia Postale (art. 629 co. 3 c.p.)."
        ],
        "deadline": "24 ore (ACN/NIS2) / 72 ore (Garante GDPR)",
        "norm": "Art. 629 co. 3 c.p., L. 90/2024, D.Lgs. 138/2024, Art. 33 GDPR",
        "auth": "Polizia Postale, ACN / CSIRT Italia, Garante Privacy",
        "href": "/cybersicurezza/ransomware-estorsione-informatica.html",
        "cta": "Apri protocollo Ransomware completo"
    },
    "databreach": {
        "title": "Data Breach / Furto o Perdita di Dati Personali",
        "desc": "Che si tratti di un attacco esterno, di un PC smarrito o di un invio email errato, serve subito una valutazione giuridica del rischio documentata.",
        "steps": [
            "1. Ferma la fuoriuscita dei dati (revoca password, token, link condivisi) e salva tutti i log di accesso.",
            "2. Classifica tipologie e volumi di dati coinvolti (dati comuni, bancari, sanitari ex art. 9 GDPR) e verifica la cifratura.",
            "3. Decidi col legale entro 72 ore se notificare al Garante (art. 33) e agli interessati (art. 34) e compila il registro interno."
        ],
        "deadline": "72 ore dalla conoscenza dell'evento",
        "norm": "Artt. 32, 33, 34, 83 GDPR; D.Lgs. 196/2003",
        "auth": "Garante per la protezione dei dati personali",
        "href": "/cybersicurezza/data-breach-garante-privacy.html",
        "cta": "Apri guida Data Breach 72 ore"
    },
    "phishing": {
        "title": "Conto Svuotato, Phishing, SIM Swap o Frode BEC",
        "desc": "La banca spesso nega il rimborso al primo reclamo, ma l'onere della prova su autenticazione forte e colpa grave grava sull'istituto.",
        "steps": [
            "1. Blocca carte e home banking e chiedi subito il recall urgente dei bonifici non autorizzati.",
            "2. Conserva SMS spoofing, chiamate, email e notifiche senza cancellare nulla e sporgi denuncia dettagliata.",
            "3. Invia disconoscimento e reclamo tecnico alla banca ex artt. 10-12 D.Lgs. 11/2010 preparando il ricorso ABF o civile."
        ],
        "deadline": "Immediato per recall / Reclamo formale prima di ABF",
        "norm": "D.Lgs. 11/2010 artt. 10, 11, 12 (PSD2); Art. 640-ter c.p.",
        "auth": "Banca, Polizia Postale, Arbitro Bancario Finanziario (ABF), Tribunale",
        "href": "/cybersicurezza/truffe-online-phishing-sim-swap-banche.html",
        "cta": "Apri protocollo Rimborso Banche / ABF"
    },
    "dipendente": {
        "title": "Ex Dipendente o Socio Sottrae Database Clienti e Segreti",
        "desc": "Occorre bloccare subito lo sviamento di clientela ma senza violare l'art. 4 dello Statuto dei Lavoratori durante la raccolta prove.",
        "steps": [
            "1. Revoca accessi VPN, CRM, cloud ed email e metti in sicurezza il PC aziendale con copia forense tracciata.",
            "2. Verifica policy IT aziendale e limiti dei controlli difensivi per non rendere inutilizzabili le prove.",
            "3. Valuta ricorso cautelare urgente (descrizione/inibitoria ex artt. 98-99 CPI e 700 c.p.c.) e querela art. 615-ter / 623 c.p."
        ],
        "deadline": "Urgenza cautelare (giorni) / Querela entro 3 mesi",
        "norm": "Artt. 98-99 CPI, Art. 2105 e 2598 c.c., Art. 4 L. 300/1970, Art. 615-ter c.p.",
        "auth": "Tribunale Sezione Impresa, Giudice del Lavoro, Procura",
        "href": "/cybersicurezza/ex-dipendenti-sottrazione-dati-segreti-aziendali.html",
        "cta": "Apri protocollo Difesa Segreti Aziendali"
    },
    "nis2": {
        "title": "Adeguamento Direttiva NIS2, ACN e Governance Aziendale",
        "desc": "Il D.Lgs. 138/2024 coinvolge direttamente la responsabilita' del CdA e impone registrazione ACN, misure di sicurezza e filiera controllata.",
        "steps": [
            "1. Verifica l'inclusione nei settori Allegati I e II del D.Lgs. 138/2024 (soggetto essenziale, importante o fornitore critico).",
            "2. Completa la registrazione sul portale ACN e designa il punto di contatto e il referente CSIRT.",
            "3. Approva in CdA il piano di gestione rischi, la policy di notifica 24h/72h/30gg e le clausole per i fornitori ICT."
        ],
        "deadline": "Scadenze annuali portale ACN e notifiche 24h/72h",
        "norm": "D.Lgs. 138/2024 (NIS2), Dir. UE 2022/2555, L. 90/2024",
        "auth": "Agenzia per la Cybersicurezza Nazionale (ACN)",
        "href": "/cybersicurezza/direttiva-nis2-acn-legge-90-2024.html",
        "cta": "Apri guida Adeguamento NIS2"
    },
    "penale": {
        "title": "Avviso di Garanzia, Perquisizione o Sequestro Informatico",
        "desc": "Con la Legge 90/2024 le pene per i reati informatici arrivano fino a 10-12 anni: la difesa tecnica sulle prove digitali va attivata subito.",
        "steps": [
            "1. Non rilasciare dichiarazioni spontanee affrettate e chiedi immediatamente l'assistenza del difensore.",
            "2. Verifica il verbale di sequestro e i codici hash dei dispositivi prelevati per valutare il riesame entro 10 giorni.",
            "3. Nomina un consulente tecnico informatico di parte per partecipare agli accertamenti irripetibili ex art. 360 c.p.p."
        ],
        "deadline": "10 giorni per Riesame sequestro (art. 324 c.p.p.)",
        "norm": "Artt. 615-ter, 635-bis/quater, 640-ter c.p.; Art. 360 c.p.p.",
        "auth": "Procura della Repubblica, Polizia Postale, Tribunale del Riesame",
        "href": "/cybersicurezza/reati-informatici-difesa-penale.html",
        "cta": "Apri guida Difesa Penale Informatica"
    },
    "reputazione": {
        "title": "Deepfake, Revenge Porn, Account Clonato o Diffamazione Online",
        "desc": "Per fermare la diffusione virale servono acquisizione forense immediata e canali legali d'urgenza verso piattaforme e Garante.",
        "steps": [
            "1. Non pagare ricatti (sextortion) e non cancellare le chat originali: fai cristallizzare URL e prove in copia forense.",
            "2. Attiva subito le procedure d'urgenza presso le piattaforme e il Garante Privacy (art. 144-bis Codice Privacy / art. 17 GDPR).",
            "3. Deposita querela mirata (art. 612-ter, 595 co. 3 o 494 c.p.) e valuta il ricorso civile art. 700 c.p.c."
        ],
        "deadline": "Urgenza immediata / Querela 3 mesi (6 mesi per art. 612-ter)",
        "norm": "Artt. 612-ter, 595 co. 3, 494 c.p.; Art. 17 GDPR",
        "auth": "Garante Privacy, Polizia Postale, Tribunale Civile e Penale",
        "href": "/cybersicurezza/reputazione-online-deepfake-revenge-porn.html",
        "cta": "Apri protocollo Rimozione Urgente"
    },
    "ai231": {
        "title": "Contratti IT, Cloud, AI Act e Modello 231 Cyber",
        "desc": "Blindare oggi contratti cloud/SaaS, uso aziendale dell'intelligenza artificiale e Modello 231 evita sanzioni e contenziosi milionari domani.",
        "steps": [
            "1. Mappa software critici, fornitori cloud (DPA art. 28) e strumenti di IA usati in azienda secondo il Reg. UE 2024/1689.",
            "2. Aggiorna la Parte Speciale art. 24-bis del Modello 231 includendo l'estorsione informatica (L. 90/2024).",
            "3. Inserisci SLA di sicurezza, obblighi di notifica incidenti in 12/24h e clausole di portabilita' dati nei contratti IT."
        ],
        "deadline": "Obblighi AI Act 2025-2026 e aggiornamento continuo 231",
        "norm": "Reg. UE 2024/1689 (AI Act), Art. 24-bis D.Lgs. 231/2001, Art. 28 GDPR",
        "auth": "Organismo di Vigilanza, Garante Privacy, ACN, Autorita' IA",
        "href": "/cybersicurezza/contratti-it-cloud-saas-ai-act.html",
        "cta": "Apri guida Contratti IT & AI Act"
    }
}

CATEGORIE_SCENARI = [
    ("tutti", "Tutti i 70 protocolli"),
    ("data-breach", "Data Breach & GDPR (10)"),
    ("ransomware-nis2", "Ransomware & NIS2/ACN (10)"),
    ("truffe-banche", "Phishing, Banche & Crypto (10)"),
    ("penale-informatico", "Penale Informatico & Forensics (10)"),
    ("lavoro-segreti", "Lavoro, Ex Dipendenti & Segreti (10)"),
    ("identita-reputazione-ai", "Identita', Deepfake & Reputazione (10)"),
    ("contratti-231", "Contratti IT, Cloud, AI & 231 (10)")
]

# Traduzioni per le 9 lingue estere gia' presenti nel sito
LINGUE_ESTERE = {
    "en": {
        "name": "English", "dir": "ltr", "locale": "en",
        "title": "Cybersecurity, Data Protection & GDPR Lawyer Italy | Studio Legale Iaccarino",
        "desc": "Italian cybersecurity and data privacy law firm in Naples operating nationwide: 72-hour GDPR data breach response, ransomware defense, NIS2 (D.Lgs. 138/2024), cybercrime litigation and AI Act compliance.",
        "eyebrow": "CYBERSECURITY, DATA PRIVACY & INCIDENT RESPONSE — ITALY & EU",
        "h1": "Cybersecurity &amp; <em>Data Protection</em> Law Firm in Italy",
        "lead": "Urgent legal response to data breaches, ransomware, NIS2/ACN compliance, GDPR investigations, banking fraud and cybercrime across Italy. Combining US top-tier incident response standards with Italian and EU law.",
        "alert_tag": "24H / 72H CYBER CRISIS DESK",
        "alert_text": "Active ransomware attack, data breach or unauthorized bank transfer? Statutory deadlines under NIS2 (24h) and GDPR (72h) run immediately.",
        "cta_urgent": "Urgent WhatsApp Desk",
        "cta_book": "Book Legal Consultation",
        "cta_it": "Explore Full Italian Hub & 70 Operational Protocols",
        "pillars_title": "Core Cybersecurity & Data Protection Practice Areas",
        "pillars_sub": "Comprehensive legal protection for businesses, boards of directors, professionals and individuals facing digital threats or regulatory audits in Italy.",
        "pillars": [
            ("01", "Data Breach & 72-Hour GDPR Notification", "Risk assessment, Garante Privacy filing under Art. 33 GDPR, data subject notices under Art. 34 and administrative defense."),
            ("02", "Ransomware & Cyber Extortion Crisis Response", "Legal war-room coordination, Art. 629(3) Italian Criminal Code (Law 90/2024), Postal Police filings and board protection."),
            ("03", "NIS2 Directive (D.Lgs. 138/2024) & ACN Compliance", "Scope assessment for essential/important entities, ACN portal registration, 24h/72h/30-day incident reporting and supply chain clauses."),
            ("04", "GDPR Governance, Audits & External DPO", "Tailored privacy frameworks, DPIAs, Art. 28 DPAs, employee monitoring compliance and defense against Garante/GdF inspections."),
            ("05", "Cybercrime Criminal Defense & Digital Forensics", "Defense and victim representation for Art. 615-ter, 635-bis/quater and 640-ter c.p., device seizures and forensic hash challenges."),
            ("06", "Phishing, SIM Swap, BEC Fraud & Bank Recovery", "Unauthorized payment claims under PSD2 / D.Lgs. 11/2010 (Arts. 10-12), ABF arbitration and civil litigation against banks."),
            ("07", "Departing Employees & Trade Secret Theft", "Lawful defensive monitoring (Art. 4 Workers' Statute), urgent injunctions under Arts. 98-99 Industrial Property Code and criminal complaints."),
            ("08", "Corporate Liability Model 231 (Art. 24-bis)", "Updating compliance programs after Law 90/2024, Supervisory Body (OdV) reporting flows and corporate criminal defense."),
            ("09", "Online Reputation, Deepfakes & Right to Be Forgotten", "Urgent takedowns for non-consensual intimate content (Art. 612-ter c.p.), AI deepfakes, impersonation and Google de-indexing (Art. 17 GDPR)."),
            ("10", "IT/Cloud/SaaS Contracts & EU AI Act Compliance", "Software agreements, security SLAs, extra-EU data transfers and compliance with Regulation (EU) 2024/1689 (AI Act).")
        ],
        "nav_cyber": "Cybersecurity", "nav_home": "Home", "nav_penale": "Criminal", "nav_civile": "Civil", "nav_trib": "Tax", "nav_imm": "Immigration", "nav_cta": "Request Consultation"
    },
    "es": {
        "name": "Español", "dir": "ltr", "locale": "es",
        "title": "Abogado de Ciberseguridad, GDPR y Datos en Italia | Studio Legale Iaccarino",
        "desc": "Asistencia legal urgente en Italia en ciberseguridad, data breach 72 horas GDPR, ransomware, Directiva NIS2 (D.Lgs. 138/2024), delitos informaticos, phishing bancario e IA.",
        "eyebrow": "CIBERSEGURIDAD, PROTECCION DE DATOS Y RESPUESTA A INCIDENTES — ITALIA Y UE",
        "h1": "Abogados de <em>Ciberseguridad</em> y Proteccion de Datos en Italia",
        "lead": "Respuesta legal inmediata frente a brechas de datos, ransomware, cumplimiento NIS2 y GDPR, fraudes bancarios y delitos informaticos en toda Italia.",
        "alert_tag": "EMERGENCIA CIBER 24H / 72H",
        "alert_text": "Ataque ransomware, robo de datos o estafa bancaria en curso? Los plazos legales NIS2 (24h) y GDPR (72h) corren de inmediato.",
        "cta_urgent": "WhatsApp de Urgencia",
        "cta_book": "Solicitar Consulta",
        "cta_it": "Ver Portal Completo y 70 Protocolos Operativos (IT)",
        "pillars_title": "10 Areas Clave en Ciberseguridad y Privacidad",
        "pillars_sub": "Defensa penal, civil y regulatoria para empresas, directivos y particulares en Italia.",
        "pillars": [
            ("01", "Data Breach y Notificacion 72h al Garante GDPR", "Evaluacion de riesgos, notificacion art. 33 GDPR, comunicacion a afectados art. 34 y defensa sancionadora."),
            ("02", "Ransomware y Extorsion Informatica", "Gestion de crisis, denuncia por art. 629 co. 3 c.p. (Ley 90/2024), notificaciones ACN y proteccion societaria."),
            ("03", "Directiva NIS2 (D.Lgs. 138/2024) y ACN", "Registro en el portal ACN, gobernanza del consejo, cadena de suministro y reportes en 24h/72h."),
            ("04", "Cumplimiento GDPR, Auditorias y DPO Externo", "Registros, DPIA, contratos art. 28 GDPR, videovigilancia y defensa en inspecciones."),
            ("05", "Delitos Informaticos y Defensa Penal", "Defensa y acusacion en acceso ilicito (615-ter), fraude informatico (640-ter) y peritajes forenses."),
            ("06", "Phishing, SIM Swap y Reembolso Bancario", "Reclamaciones bajo PSD2 (D.Lgs. 11/2010), recurso ABF y recuperacion judicial de fondos."),
            ("07", "Ex Empleados y Robo de Secretos Comerciales", "Medidas cautelares urgentes (arts. 98-99 CPI), controles defensivos licitos y competencia desleal."),
            ("08", "Modelo 231 y Delitos Informaticos (Art. 24-bis)", "Actualizacion tras la Ley 90/2024, protocolos de seguridad y defensa penal de la entidad."),
            ("09", "Reputacion Digital, Deepfakes y Derecho al Olvido", "Retirada urgente de contenidos ilicitos (art. 612-ter c.p.), deepfakes y desindexacion art. 17 GDPR."),
            ("10", "Contratos IT, Cloud, SaaS y AI Act", "Negociacion de SLA de seguridad, transferencias internacionales y cumplimiento Reg. UE 2024/1689.")
        ],
        "nav_cyber": "Ciberseguridad", "nav_home": "Inicio", "nav_penale": "Penal", "nav_civile": "Civil", "nav_trib": "Tributario", "nav_imm": "Inmigracion", "nav_cta": "Solicitar Consulta"
    },
    "pt": {
        "name": "Português", "dir": "ltr", "locale": "pt",
        "title": "Advogado de Ciberseguranca e Protecao de Dados na Italia | Studio Iaccarino",
        "desc": "Assistencia juridica urgente na Italia para data breach 72h GDPR, ransomware, Diretiva NIS2 (D.Lgs. 138/2024), crimes ciberneticos, phishing bancario e AI Act.",
        "eyebrow": "CIBERSEGURANCA, PRIVACIDADE E RESPOSTA A INCIDENTES — ITALIA E UE",
        "h1": "Advocacia em <em>Ciberseguranca</em> e Protecao de Dados na Italia",
        "lead": "Atuacao juridica imediata em vazamentos de dados, ransomware, conformidade NIS2 e GDPR, fraudes bancarias e crimes digitais em toda a Italia.",
        "alert_tag": "EMERGENCIA CIBER 24H / 72H",
        "alert_text": "Ataque ransomware ou vazamento de dados em andamento? Os prazos legais NIS2 (24h) e GDPR (72h) comecam imediatamente.",
        "cta_urgent": "WhatsApp de Urgencia",
        "cta_book": "Agendar Consulta",
        "cta_it": "Explorar Portal Completo e 70 Protocolos (IT)",
        "pillars_title": "10 Pilares de Ciberseguranca e Protecao de Dados",
        "pillars_sub": "Protecao juridica completa para empresas, administradores e pessoas fisicas na Italia.",
        "pillars": [
            ("01", "Data Breach e Notificacao 72h GDPR", "Analise de risco, notificacao ao Garante (art. 33 GDPR) e defesa contra sancoes."),
            ("02", "Ransomware e Extorsao Informatica", "Gestao de crise, art. 629 co. 3 c.p. (Lei 90/2024), denuncia e tutela dos administradores."),
            ("03", "Diretiva NIS2 (D.Lgs. 138/2024) e ACN", "Registro no portal ACN, governanca corporativa e notificacoes em 24h/72h."),
            ("04", "Conformidade GDPR e DPO Externo", "Auditoria, DPIA, contratos art. 28 GDPR e defesa em inspecoes."),
            ("05", "Crimes Informaticos e Defesa Penal", "Defesa e representacao em invasao de sistemas (615-ter), fraude informatica (640-ter) e pericia forense."),
            ("06", "Phishing, SIM Swap e Reembolso Bancario", "Acoes com base no D.Lgs. 11/2010 (PSD2), recurso ABF e acoes judiciais contra bancos."),
            ("07", "Ex-Funcionarios e Furto de Dados", "Medidas cautelares urgentes (arts. 98-99 CPI) e controles defensivos licitos."),
            ("08", "Modelo 231 e Crimes Ciberneticos", "Atualizacao do art. 24-bis pos Lei 90/2024 e defesa penal societaria."),
            ("09", "Reputacao Online, Deepfake e Direito ao Esquecimento", "Remocao urgente de conteudos ilicitos (art. 612-ter c.p.) e desindexacao art. 17 GDPR."),
            ("10", "Contratos de TI, Cloud, SaaS e AI Act", "SLA de seguranca, transferencias de dados e conformidade com o Reg. UE 2024/1689.")
        ],
        "nav_cyber": "Ciberseguranca", "nav_home": "Inicio", "nav_penale": "Penal", "nav_civile": "Civil", "nav_trib": "Tributario", "nav_imm": "Imigracao", "nav_cta": "Solicitar Consulta"
    },
    "ru": {
        "name": "Русский", "dir": "ltr", "locale": "ru",
        "title": "Юрист по кибербезопасности и GDPR в Италии | Studio Legale Iaccarino",
        "desc": "Срочная юридическая помощь в Италии: утечки данных GDPR (72 часа), атаки ransomware, директива NIS2 (D.Lgs. 138/2024), киберпреступления, банковское мошенничество и AI Act.",
        "eyebrow": "КИБЕРБЕЗОПАСНОСТЬ И ЗАЩИТА ДАННЫХ — ИТАЛИЯ И ЕС",
        "h1": "Юридическая защита в сфере <em>кибербезопасности</em> и данных",
        "lead": "Оперативная правовая помощь компаниям и частным лицам по всей Италии при кибератаках, утечках данных GDPR, требованиях NIS2/ACN, фишинге и уголовных делах в сфере IT.",
        "alert_tag": "СРОЧНОЕ РЕАГИРОВАНИЕ 24Ч / 72Ч",
        "alert_text": "Атака ransomware, утечка данных или списание средств? Законные сроки уведомления NIS2 (24ч) и GDPR (72ч) уже идут.",
        "cta_urgent": "Срочный WhatsApp",
        "cta_book": "Записаться на консультацию",
        "cta_it": "Открыть полный раздел и 70 протоколов (IT)",
        "pillars_title": "10 ключевых направлений киберправа",
        "pillars_sub": "Комплексная защита бизнеса, руководства и граждан в Италии и ЕС.",
        "pillars": [
            ("01", "Data Breach и уведомление Garante за 72 часа", "Оценка рисков, уведомление по ст. 33 GDPR и защита от штрафов."),
            ("02", "Ransomware и кибервымогательство", "Антикризисное сопровождение, ст. 629 ч. 3 УК Италии (Закон 90/2024) и подача заявлений."),
            ("03", "Директива NIS2 (D.Lgs. 138/2024) и ACN", "Регистрация в ACN, ответственность совета директоров и отчетность за 24ч/72ч."),
            ("04", "Соответствие GDPR и внешний DPO", "Аудит, DPIA, договоры по ст. 28 GDPR и защита при проверках."),
            ("05", "Киберпреступления и уголовная защита", "Защита по ст. 615-ter, 635-bis, 640-ter УК Италии, оспаривание изъятий и форензика."),
            ("06", "Фишинг, SIM Swap и возврат средств от банков", "Претензии по D.Lgs. 11/2010 (PSD2), жалобы в ABF и судебные иски."),
            ("07", "Кража баз данных бывшими сотрудниками", "Срочные обеспечительные меры (ст. 98-99 CPI) и защита коммерческой тайны."),
            ("08", "Модель 231 и киберриски компаний", "Обновление ст. 24-bis D.Lgs. 231/2001 после Закона 90/2024."),
            ("09", "Репутация в сети, дипфейки и право на забвение", "Срочное удаление контента (ст. 612-ter УК) и деиндексация по ст. 17 GDPR."),
            ("10", "IT/Cloud/SaaS контракты и AI Act", "SLA безопасности и соответствие Регламенту ЕС 2024/1689 (AI Act).")
        ],
        "nav_cyber": "Киберправо", "nav_home": "Главная", "nav_penale": "Уголовное", "nav_civile": "Гражданское", "nav_trib": "Налоговое", "nav_imm": "Иммиграция", "nav_cta": "Консультация"
    },
    "ar": {
        "name": "العربية", "dir": "rtl", "locale": "ar",
        "title": "محامي الأمن السيبراني وحماية البيانات في إيطاليا | Studio Legale Iaccarino",
        "desc": "استشارات ودفاع قانوني عاجل في إيطاليا: خرق البيانات GDPR خلال 72 ساعة، هجمات الفدية، توجيه NIS2، الجرائم الإلكترونية، الاحتيال البنكي وقانون الذكاء الاصطناعي.",
        "eyebrow": "الأمن السيبراني وحماية البيانات والاستجابة للحوادث — إيطاليا والاتحاد الأوروبي",
        "h1": "مكتب محاماة متخصص في <em>الأمن السيبراني</em> وحماية البيانات",
        "lead": "استجابة قانونية فورية للشركات والأفراد في جميع أنحاء إيطاليا لحالات خرق البيانات، هجمات الفدية، الامتثال لقواعد GDPR وNIS2، والاحتيال المصرفي الإلكتروني.",
        "alert_tag": "طوارئ سيبرانية 24 / 72 ساعة",
        "alert_text": "هل تتعرض لهجوم فدية أو تسريب بيانات أو احتيال بنكي؟ المواعيد القانونية بموجب NIS2 (24 ساعة) وGDPR (72 ساعة) تبدأ فوراً.",
        "cta_urgent": "واتساب الطوارئ",
        "cta_book": "احجز استشارة قانونية",
        "cta_it": "استعرض الدليل الكامل و70 بروتوكولاً عملياً (بالإيطالية)",
        "pillars_title": "10 مجالات رئيسية في القانون السيبراني وحماية البيانات",
        "pillars_sub": "حماية قانونية متكاملة للشركات ومجالس الإدارة والأفراد في إيطاليا.",
        "pillars": [
            ("01", "خرق البيانات والإبلاغ خلال 72 ساعة (GDPR)", "تقييم المخاطر، الإبلاغ لهيئة حماية البيانات وفق المادة 33 والدفاع ضد الغرامات."),
            ("02", "هجمات الفدية والابتزاز الإلكتروني", "إدارة الأزمة قانونياً وفق المادة 629 فقرة 3 من قانون العقوبات (قانون 90/2024)."),
            ("03", "توجيه NIS2 والهيئة الوطنية للأمن السيبراني ACN", "التسجيل في بوابة ACN، حوكمة الإدارة والتبليغ خلال 24 و72 ساعة."),
            ("04", "الامتثال للائحة GDPR ومسؤول حماية البيانات DPO", "التدقيق القانوني، تقييم الأثر DPIA، وعقود المعالجة وفق المادة 28."),
            ("05", "الجرائم الإلكترونية والدفاع الجنائي", "الدفاع والادعاء في جرائم الدخول غير المشروع والاحتيال المعلوماتي والأدلة الرقمية."),
            ("06", "التصيد الاحتيالي واسترداد الأموال من البنوك", "مطالبات المعاملات غير المصرح بها وفق المرسوم 11/2010 والتحكيم البنكي ABF."),
            ("07", "سرقة قواعد البيانات والأسرار التجارية", "إجراءات تحفظية عاجلة ضد الموظفين السابقين والمنافسة غير المشروعة."),
            ("08", "المسؤولية المؤسسية النموذج 231 (المادة 24-bis)", "تحديث برامج الامتثال بعد القانون 90/2024 والدفاع عن الشركات."),
            ("09", "السمعة الرقمية والتزييف العميق وحق النسيان", "إزالة عاجلة للمحتوى غير المشروع وإلغاء الفهرسة وفق المادة 17 GDPR."),
            ("10", "عقود تكنولوجيا المعلومات والسحابة وقانون الذكاء الاصطناعي", "صياغة عقود SaaS والامتثال للائحة الأوروبية AI Act (2024/1689).")
        ],
        "nav_cyber": "الأمن السيبراني", "nav_home": "الرئيسية", "nav_penale": "جنائي", "nav_civile": "مدني", "nav_trib": "ضرائب", "nav_imm": "هجرة", "nav_cta": "طلب استشارة"
    },
    "zh": {
        "name": "中文", "dir": "ltr", "locale": "zh-Hans",
        "title": "意大利网络安全、数据保护与GDPR律师 | Studio Legale Iaccarino",
        "desc": "意大利全境紧急网络安全与数据合规法律服务：GDPR 72小时数据泄露通报、勒索软件危机应对、NIS2指令(D.Lgs. 138/2024)、网络犯罪辩护、银行钓鱼维权与欧盟AI法案。",
        "eyebrow": "网络安全、数据隐私与应急响应 — 意大利及欧盟",
        "h1": "意大利<em>网络安全</em>与数据保护律师事务所",
        "lead": "为意大利全境企业、董事会及个人提供数据泄露72小时应对、勒索软件处置、NIS2/GDPR合规、银行欺诈维权与网络犯罪辩护。",
        "alert_tag": "24小时 / 72小时 网络危机热线",
        "alert_text": "正在遭遇勒索软件攻击、数据泄露或网银盗刷？NIS2（24小时）与GDPR（72小时）法定通报期限立即起算。",
        "cta_urgent": "紧急 WhatsApp 联系",
        "cta_book": "预约法律咨询",
        "cta_it": "查看完整意大利语门户与70项实务应对方案",
        "pillars_title": "网络安全与数据保护十大核心业务",
        "pillars_sub": "结合国际顶尖应急标准与意大利及欧盟现行法律，全面守护企业与个人数字资产。",
        "pillars": [
            ("01", "数据泄露与GDPR 72小时通报", "风险评估、依GDPR第33条向隐私监管局通报及行政处罚抗辩。"),
            ("02", "勒索软件与网络敲诈危机应对", "依据意大利刑法第629条第3款（第90/2024号法）报案与企业危机法务协调。"),
            ("03", "NIS2指令(D.Lgs. 138/2024)与ACN合规", "适用范围评估、ACN门户注册、24/72小时事件通报及董事会合规治理。"),
            ("04", "GDPR合规审计与外部DPO服务", "处理记录、DPIA影响评估、第28条数据处理协议及监管检查应对。"),
            ("05", "网络犯罪刑事辩护与数字取证", "针对非法侵入系统(615-ter)、网络诈骗(640-ter)的辩护及电子扣押复议。"),
            ("06", "网络钓鱼、SIM卡劫持与银行索赔", "依据D.Lgs. 11/2010(PSD2)主张银行举证责任，提起ABF仲裁与民事诉讼。"),
            ("07", "离职员工窃取客户数据与商业秘密", "依据工业产权法第98-99条申请紧急禁令与合法防御性取证。"),
            ("08", "企业231合规模型(第24-bis条)", "依据第90/2024号法更新网络犯罪防控合规体系与企业刑事辩护。"),
            ("09", "网络声誉、深度伪造(Deepfake)与被遗忘权", "紧急下架非法影像(第612-ter条)、应对AI换脸及申请Google除名(GDPR第17条)。"),
            ("10", "IT/云/SaaS合同与欧盟AI法案合规", "审定安全SLA、跨境数据传输及欧盟AI法案(2024/1689)合规落地。")
        ],
        "nav_cyber": "网络安全", "nav_home": "首页", "nav_penale": "刑事", "nav_civile": "民事", "nav_trib": "税务", "nav_imm": "移民", "nav_cta": "预约咨询"
    },
    "hi": {
        "name": "हिन्दी", "dir": "ltr", "locale": "hi",
        "title": "इटली में साइबर सुरक्षा और डेटा संरक्षण वकील | Studio Legale Iaccarino",
        "desc": "इटली में साइबर सुरक्षा, 72 घंटे GDPR डेटा ब्रीच, रैंसमवेयर, NIS2 (D.Lgs. 138/2024), साइबर अपराध और ऑनलाइन बैंकिंग धोखाधड़ी के लिए त्वरित कानूनी सहायता।",
        "eyebrow": "साइबर सुरक्षा और डेटा संरक्षण — इटली और यूरोपीय संघ",
        "h1": "इटली में <em>साइबर सुरक्षा</em> और डेटा संरक्षण कानूनी सेवाएँ",
        "lead": "डेटा ब्रीच, रैंसमवेयर, NIS2/GDPR अनुपालन, बैंक फ़िशिंग वसूली और साइबर अपराधों के लिए पूरे इटली में तत्काल कानूनी रक्षा।",
        "alert_tag": "24 / 72 घंटे साइबर आपातकाल",
        "alert_text": "क्या रैंसमवेयर हमला, डेटा चोरी या बैंक धोखाधड़ी हुई है? NIS2 (24 घंटे) और GDPR (72 घंटे) की समय-सीमा तुरंत शुरू होती है।",
        "cta_urgent": "तत्काल WhatsApp सहायता",
        "cta_book": "कानूनी परामर्श बुक करें",
        "cta_it": "पूर्ण इतालवी पोर्टल और 70 प्रोटोकॉल देखें",
        "pillars_title": "साइबर सुरक्षा के 10 प्रमुख कानूनी क्षेत्र",
        "pillars_sub": "कंपनियों, निदेशकों और व्यक्तियों के लिए संपूर्ण डिजिटल सुरक्षा।",
        "pillars": [
            ("01", "डेटा ब्रीच और 72 घंटे GDPR सूचना", "जोखिम मूल्यांकन, अनुच्छेद 33 GDPR सूचना और जुर्माने से बचाव।"),
            ("02", "रैंसमवेयर और साइबर जबरन वसूली", "कानून 90/2024 (अनुच्छेद 629(3)) के तहत संकट प्रबंधन और पुलिस शिकायत।"),
            ("03", "NIS2 निर्देश (D.Lgs. 138/2024) और ACN", "ACN पंजीकरण, 24/72 घंटे घटना रिपोर्टिंग और कॉर्पोरेट अनुपालन।"),
            ("04", "GDPR अनुपालन और बाहरी DPO", "ऑडिट, DPIA, अनुच्छेद 28 अनुबंध और निरीक्षण में बचाव।"),
            ("05", "साइबर अपराध आपराधिक बचाव", "अनुच्छेद 615-ter और 640-ter के मामलों में बचाव और डिजिटल फोरेंसिक।"),
            ("06", "फ़िशिंग, SIM स्वैप और बैंक रिफंड", "D.Lgs. 11/2010 (PSD2) और ABF के माध्यम से धन की वसूली।"),
            ("07", "पूर्व कर्मचारी और डेटा चोरी सुरक्षा", "व्यापार रहस्य (अनुच्छेद 98-99 CPI) और तत्काल निषेधाज्ञा।"),
            ("08", "मॉडल 231 और कॉर्पोरेट साइबर दायित्व", "कानून 90/2024 के अनुसार अनुच्छेद 24-bis अद्यतन।"),
            ("09", "ऑनलाइन प्रतिष्ठा और डीपफेक हटाना", "अवैध सामग्री हटाना और अनुच्छेद 17 GDPR के तहत डी-इंडेक्सिंग।"),
            ("10", "IT/क्लाउड अनुबंध और EU AI Act", "सुरक्षा SLA और विनियमन (EU) 2024/1689 अनुपालन।")
        ],
        "nav_cyber": "साइबर सुरक्षा", "nav_home": "होम", "nav_penale": "आपराधिक", "nav_civile": "सिविल", "nav_trib": "कर", "nav_imm": "आप्रवासन", "nav_cta": "परामर्श लें"
    },
    "bn": {
        "name": "বাংলা", "dir": "ltr", "locale": "bn",
        "title": "ইতালিতে সাইবার নিরাপত্তা ও ডেটা সুরক্ষা আইনজীবী | Studio Legale Iaccarino",
        "desc": "ইতালিতে সাইবার নিরাপত্তা, ৭২ ঘণ্টার GDPR ডেটা ব্রিচ, র‍্যানসমওয়্যার, NIS2 (D.Lgs. 138/2024), সাইবার অপরাধ এবং ব্যাংক ফিশিং প্রতিকারের জন্য জরুরি আইনি সহায়তা।",
        "eyebrow": "সাইবার নিরাপত্তা ও ডেটা সুরক্ষা — ইতালি ও ইউরোপীয় ইউনিয়ন",
        "h1": "ইতালিতে <em>সাইবার নিরাপত্তা</em> ও ডেটা সুরক্ষা আইনি সহায়তা",
        "lead": "ডেটা ব্রিচ, র‍্যানসমওয়্যার, NIS2/GDPR কমপ্লায়েন্স, ব্যাংক জালিয়াতি এবং সাইবার অপরাধে পুরো ইতালিতে তাৎক্ষণিক আইনি প্রতিরক্ষা।",
        "alert_tag": "২৪ / ৭২ ঘণ্টা সাইবার জরুরি ডেস্ক",
        "alert_text": "র‍্যানসমওয়্যার আক্রমণ বা ডেটা ফাঁস হয়েছে? NIS2 (২৪ ঘণ্টা) এবং GDPR (৭২ ঘণ্টা) আইনি সময়সীমা সঙ্গে সঙ্গে শুরু হয়।",
        "cta_urgent": "জরুরি WhatsApp",
        "cta_book": "পরামর্শ বুক করুন",
        "cta_it": "সম্পূর্ণ ইতালীয় পোর্টাল ও ৭০টি প্রোটোকল দেখুন",
        "pillars_title": "সাইবার নিরাপত্তা ও ডেটা আইনের ১০টি মূল ক্ষেত্র",
        "pillars_sub": "ব্যবসা প্রতিষ্ঠান এবং ব্যক্তিদের জন্য পূর্ণাঙ্গ ডিজিটাল আইনি সুরক্ষা।",
        "pillars": [
            ("01", "ডেটা ব্রিচ ও ৭২ ঘণ্টায় GDPR নোটিফিকেশন", "ঝুঁকি মূল্যায়ন, অনুচ্ছেদ ৩৩ GDPR রিপোর্টিং এবং জরিমানা প্রতিরোধ।"),
            ("02", "র‍্যানসমওয়্যার ও সাইবার চাঁদাবাজি", "আইন ৯০/২০২৪ (ধারা ৬২৯(৩)) অনুযায়ী জরুরি আইনি পদক্ষেপ ও পুলিশ রিপোর্ট।"),
            ("03", "NIS2 নির্দেশিকা (D.Lgs. 138/2024) ও ACN", "ACN পোর্টাল নিবন্ধন এবং ২৪/৭২ ঘণ্টার ঘটনা প্রতিবেদন।"),
            ("04", "GDPR কমপ্লায়েন্স ও বাহ্যিক DPO", "অডিট, DPIA, ধারা ২৮ চুক্তি এবং নিয়ন্ত্রক পরিদর্শনে প্রতিরক্ষা।"),
            ("05", "সাইবার অপরাধ ও ফৌজদারি প্রতিরক্ষা", "ধারা ৬১৫-ter ও ৬৪০-ter মামলায় আইনি প্রতিরক্ষা ও ডিজিটাল ফরেনসিক।"),
            ("06", "ফিশিং, সিম সোয়াপ ও ব্যাংক রিফান্ড", "D.Lgs. 11/2010 (PSD2) ও ABF-এর মাধ্যমে অর্থ পুনরুদ্ধার।"),
            ("07", "প্রাক্তন কর্মী ও ডেটা চুরি প্রতিরোধ", "ব্যবসায়িক গোপনীয়তা রক্ষা (ধারা ৯৮-৯৯ CPI) এবং জরুরি নিষেধাজ্ঞা।"),
            ("08", "মডেল ২৩১ ও কর্পোরেট সাইবার দায়", "আইন ৯০/২০২৪ অনুযায়ী ধারা ২৪-bis হালনাগাদ।"),
            ("09", "অনলাইন সুনাম, ডিপফেক ও অপসারণ", "অবৈধ কনটেন্ট অপসারণ এবং GDPR ধারা ১৭ অনুযায়ী ডি-ইনডেক্সিং।"),
            ("10", "IT/ক্লাউড চুক্তি ও EU AI Act", "সিকিউরিটি SLA এবং EU AI Act (2024/1689) কমপ্লায়েন্স।")
        ],
        "nav_cyber": "সাইবার নিরাপত্তা", "nav_home": "হোম", "nav_penale": "ফৌজদারি", "nav_civile": "দেওয়ানি", "nav_trib": "কর", "nav_imm": "অভিবাসন", "nav_cta": "পরামর্শ নিন"
    },
    "si": {
        "name": "සිංහල", "dir": "ltr", "locale": "si",
        "title": "ඉතාලියේ සයිබර් ආරක්ෂණ සහ දත්ත නීතිඥ | Studio Legale Iaccarino",
        "desc": "ඉතාලියේ සයිබර් ආරක්ෂණය, පැය 72 GDPR දත්ත කඩවීම්, රැන්සම්වෙයාර්, NIS2 (D.Lgs. 138/2024), සයිබර් අපරාධ සහ බැංකු වංචා සඳහා හදිසි නීති සහාය.",
        "eyebrow": "සයිබර් ආරක්ෂණය සහ දත්ත සුරැකීම — ඉතාලිය සහ යුරෝපා සංගමය",
        "h1": "ඉතාලියේ <em>සයිබර් ආරක්ෂණ</em> සහ දත්ත සුරැකීමේ නීති සේවා",
        "lead": "දත්ත කඩවීම්, රැන්සම්වෙයාර්, NIS2/GDPR අනුකූලතාව, බැංකු වංචා සහ සයිබර් අපරාධ සඳහා ඉතාලිය පුරා ක්ෂණික නීති ආරක්ෂාව.",
        "alert_tag": "පැය 24 / 72 සයිබර් හදිසි සහාය",
        "alert_text": "රැන්සම්වෙයාර් ප්‍රහාරයක් හෝ දත්ත කඩවීමක් සිදුවී ඇත්ද? NIS2 (පැය 24) සහ GDPR (පැය 72) නීතිමය කාලසීමා වහාම ආරම්භ වේ.",
        "cta_urgent": "හදිසි WhatsApp",
        "cta_book": "නීති උපදෙස් වෙන්කරවා ගන්න",
        "cta_it": "සම්පූර්ණ ඉතාලි පිටුව සහ ප්‍රොටෝකෝල 70 බලන්න",
        "pillars_title": "සයිබර් ආරක්ෂණයේ ප්‍රධාන නීති අංශ 10",
        "pillars_sub": "ව්‍යාපාර සහ පුද්ගලයන් සඳහා සම්පූර්ණ ඩිජිටල් නීති ආරක්ෂාව.",
        "pillars": [
            ("01", "දත්ත කඩවීම් සහ පැය 72 GDPR දැනුම්දීම", "අවදානම් තක්සේරුව, GDPR 33 වගන්තිය යටතේ දැනුම්දීම සහ දඩ මුදල් වලින් ආරක්ෂාව."),
            ("02", "රැන්සම්වෙයාර් සහ සයිබර් කප්පම්", "90/2024 නීතිය යටතේ හදිසි නීති ක්‍රියාමාර්ග සහ පොලිස් පැමිණිලි."),
            ("03", "NIS2 නියෝගය (D.Lgs. 138/2024) සහ ACN", "ACN ලියාපදිංචිය සහ පැය 24/72 සිදුවීම් වාර්තාකරණය."),
            ("04", "GDPR අනුකූලතාව සහ බාහිර DPO", "විගණන, DPIA, 28 වගන්තියේ ගිවිසුම් සහ පරීක්ෂණ ආරක්ෂාව."),
            ("05", "සයිබර් අපරාධ සහ අපරාධ ආරක්ෂාව", "615-ter සහ 640-ter වගන්ති යටතේ නීතිමය ආරක්ෂාව සහ ඩිජිටල් සාක්ෂි."),
            ("06", "ෆිෂින්, SIM Swap සහ බැංකු මුදල් ආපසු ගැනීම", "D.Lgs. 11/2010 (PSD2) සහ ABF හරහා මුදල් නැවත ලබා ගැනීම."),
            ("07", "හිටපු සේවකයින් සහ දත්ත සොරකම", "ව්‍යාපාරික රහස් සුරැකීම (98-99 CPI) සහ හදිසි තහනම් නියෝග."),
            ("08", "231 ආකෘතිය සහ ආයතනික වගකීම", "90/2024 නීතියෙන් පසු 24-bis යාවත්කාලීන කිරීම."),
            ("09", "ඔන්ලයින් කීර්තිනාමය සහ Deepfake ඉවත් කිරීම", "නීතිවිරෝධී අන්තර්ගත ඉවත් කිරීම සහ GDPR 17 වගන්තිය."),
            ("10", "IT/Cloud ගිවිසුම් සහ EU AI Act", "ආරක්ෂක SLA සහ EU AI Act (2024/1689) අනුකූලතාව.")
        ],
        "nav_cyber": "සයිබර් ආරක්ෂණය", "nav_home": "මුල් පිටුව", "nav_penale": "අපරාධ", "nav_civile": "සිවිල්", "nav_trib": "බදු", "nav_imm": "ආගමන", "nav_cta": "උපදෙස් ලබා ගන්න"
    }
}
