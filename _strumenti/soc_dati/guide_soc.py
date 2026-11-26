# -*- coding: utf-8 -*-
"""26 Guide Operative e Checklist Forensi di Diritto Societario, Modello 231 e Crisi d'Impresa (GSOC-01 -> GSOC-26)."""

GUIDE_SOC = [
    {
        "cod": "GSOC-01",
        "slug": "guida-adeguati-assetti-organizzativi-art-2086-cc",
        "pilastro": "diritto-societario-governance-srl-spa",
        "titolo": "Guida agli adeguati assetti organizzativi, amministrativi e contabili (art. 2086 c.c. e art. 3 CCII)",
        "seo_title": "Guida Adeguati Assetti Art. 2086 c.c. e Art. 3 CCII | Checklist PMI",
        "desc": "Come implementare in modo concreto e documentabile gli adeguati assetti in S.r.l. e S.p.A., rispettando l'art. 3 CCII ed evitando denunce ex art. 2409 c.c.",
        "norme": ["Art. 2086 co. 2 c.c.", "Art. 3 CCII", "Art. 2409 c.c."],
        "intro": "Ogni societa', anche una piccola S.r.l., ha l'obbligo di legge di dotarsi di assetti organizzativi, amministrativi e contabili adeguati a rilevare tempestivamente squilibri patrimoniali o di cassa e a preservare la continuita' aziendale.",
        "sezioni": [
            ("1. Cosa controllano davvero i Tribunali delle Imprese", "I giudici verificano l'esistenza di organigramma e deleghe, di una contabilita' aggiornata in tempo reale e di un budget di tesoreria prospettico a 6-12 mesi capace di misurare la sostenibilita' dei debiti (DSCR)."),
            ("2. I segnali di allerta dell'art. 3 comma 4 CCII", "Gli assetti devono intercettare subito ritardi nelle retribuzioni (>30 giorni), debiti verso fornitori scaduti (>90 giorni), esposizioni bancarie scadute (>60 giorni) e superamento delle soglie INPS, INAIL, AdE e AdER."),
            ("3. Documentazione nei verbali di CdA", "Non basta avere gli strumenti: occorre verbalizzare periodicamente l'esame degli indici di cassa e le decisioni correttive assunte, a tutela personale degli amministratori.")
        ],
        "checklist": [
            "Approvare in CdA organigramma, deleghe di firma e matrice dei poteri.",
            "Attivare chiusure contabili infrannuali almeno trimestrali.",
            "Predisporre un budget di cassa forward-looking a 6-12 mesi con monitoraggio scostamenti.",
            "Controllare mensilmente le soglie di allerta dell'art. 3 co. 4 e art. 25-novies CCII.",
            "Verbalizzare ogni trimestre l'esito del monitoraggio con l'organo di controllo."
        ],
        "faqs": [
            ("Gli adeguati assetti sono obbligatori anche per le micro-S.r.l.?", "Si', l'art. 2086 co. 2 c.c. si applica a tutte le societa', con strumenti proporzionati alla dimensione aziendale."),
            ("Qual e' la conseguenza piu' immediata se mancano?", "La denuncia al Tribunale ex art. 2409 c.c. con possibile ispezione giudiziale e revoca degli amministratori.")
        ]
    },
    {
        "cod": "GSOC-02",
        "slug": "guida-redazione-aggiornamento-modello-231-esimente",
        "pilastro": "modello-231-responsabilita-enti-odv",
        "titolo": "Guida pratica alla redazione e all'aggiornamento del Modello 231 realmente esimente",
        "seo_title": "Guida Modello 231 Esimente: Risk Assessment, Protocolli e OdV",
        "desc": "Come costruire un Modello Organizzativo ex D.Lgs. 231/2001 su misura (evitando i modelli di cartapesta) aggiornato ai reati tributari, ambientali, sicurezza, whistleblowing e L. 90/2024.",
        "norme": ["D.Lgs. 231/2001", "Artt. 6-7 D.Lgs. 231/2001", "D.Lgs. 24/2023", "L. 90/2024"],
        "intro": "Un Modello 231 protegge davvero la societa' solo se costruito sui rischi reali dell'azienda, dotato di controlli verificabili e vigilato da un OdV autonomo.",
        "sezioni": [
            ("1. Risk Assessment e mappatura processi sensibili", "Si parte dalle interviste ai responsabili di area per individuare dove possono nascere reati presupposto: appalti e PA, sicurezza lavoro (D.Lgs. 81/2008), fisco e fatture, ambiente, IT/cyber (art. 24-bis L. 90/2024), finanza e bilanci."),
            ("2. Protocolli operativi, segregazione e sistema disciplinare", "Ogni processo a rischio deve prevedere segregazione tra chi autorizza, chi esegue e chi controlla, tracciabilita' scritta e un sistema sanzionatorio realmente applicato."),
            ("3. Aggiornamento continuo e formazione certificata", "Il modello deve essere aggiornato a ogni novita' normativa o cambio organizzativo, con formazione periodica documentata per amministratori e dipendenti.")
        ],
        "checklist": [
            "Eseguire mappatura rischi su misura e gap analysis sui processi aziendali.",
            "Redigere Parte Generale, Parti Speciali mirate, Codice Etico e Sistema Disciplinare.",
            "Integrare il canale Whistleblowing crittografato conforme al D.Lgs. 24/2023.",
            "Nominare un Organismo di Vigilanza autonomo con budget dedicato.",
            "Adottare il MOG con delibera CdA e avviare formazione e audit periodici."
        ],
        "faqs": [
            ("Quanto spesso va aggiornato il Modello 231?", "Ogni volta che cambiano le norme sui reati presupposto (es. L. 90/2024), la struttura aziendale o a seguito di rilievi dell'OdV."),
            ("Il Modello 231 serve anche alle PMI?", "Si', anzi nelle PMI l'interdizione o un sequestro 231 possono chiudere l'azienda in pochi giorni.")
        ]
    },
    {
        "cod": "GSOC-03",
        "slug": "guida-organismo-vigilanza-odv-nomina-poteri-verbali",
        "pilastro": "modello-231-responsabilita-enti-odv",
        "titolo": "Guida all'Organismo di Vigilanza (OdV): composizione, poteri, flussi informativi e verbali",
        "seo_title": "Guida Organismo di Vigilanza OdV 231: Nomina, Poteri e Verbali",
        "desc": "Come istituire e far funzionare un OdV autonomo ed efficace ex art. 6 D.Lgs. 231/2001: requisiti di indipendenza, budget, piano audit e flussi informativi.",
        "norme": ["Art. 6 co. 1 lett. b D.Lgs. 231/2001", "Art. 6 co. 4-bis D.Lgs. 231/2001"],
        "intro": "Senza un Organismo di Vigilanza autonomo, indipendente e attivo, anche il miglior Modello 231 viene giudicato inefficace in sede penale.",
        "sezioni": [
            ("1. Composizione e requisiti di indipendenza", "L'OdV puo' essere monocratico (nelle PMI) o collegiale, preferibilmente con professionisti esterni privi di ruoli operativi o dipendenza gerarchica dagli amministratori."),
            ("2. Budget autonomo e piano annuale di verifiche", "Il CdA deve attribuire all'OdV una dotazione finanziaria spendibile autonomamente per consulenze tecniche o verifiche ispettive a sorpresa."),
            ("3. Flussi informativi periodici e ad evento", "Le funzioni aziendali devono inviare all'OdV flussi programmati (sicurezza, gare, consulenze, contenziosi) e segnalazioni immediate ad evento (ispezioni GdF/ASL/ARPA, infortuni, data breach).")
        ],
        "checklist": [
            "Verificare assenza di cause di incompatibilita' dei componenti OdV.",
            "Approvare regolamento interno OdV e budget annuo autonomo.",
            "Attivare casella dedicata OdV e calendario dei flussi informativi.",
            "Eseguire e verbalizzare almeno 3-4 audit l'anno con verifiche documentali a campione.",
            "Trasmettere relazione semestrale o annuale al CdA e al Collegio Sindacale."
        ],
        "faqs": [
            ("Il Collegio Sindacale puo' svolgere le funzioni di OdV?", "Si', l'art. 6 co. 4-bis D.Lgs. 231/2001 lo consente nelle societa' di capitali, valutando attentamente competenze e carichi di lavoro."),
            ("L'OdV ha poteri disciplinari diretti?", "No: l'OdV segnala le violazioni agli organi competenti affinche' applichino il sistema disciplinare.")
        ]
    },
    {
        "cod": "GSOC-04",
        "slug": "guida-whistleblowing-aziendale-dlgs-24-2023-modello-231",
        "pilastro": "modello-231-responsabilita-enti-odv",
        "titolo": "Guida al Whistleblowing aziendale (D.Lgs. 24/2023) integrato col Modello 231",
        "seo_title": "Guida Whistleblowing D.Lgs. 24/2023 e Modello 231: Checklist ANAC",
        "desc": "Adempimenti obbligatori per canale interno di segnalazione, riservatezza crittografata, scadenze 7 giorni e 3 mesi, DPIA privacy e prevenzione sanzioni ANAC.",
        "norme": ["D.Lgs. 24/2023", "Art. 6 co. 2-bis D.Lgs. 231/2001", "Linee Guida ANAC"],
        "intro": "Tutte le aziende con almeno 50 dipendenti e tutte le societa' dotate di Modello 231 (a prescindere dal numero di dipendenti) devono avere un canale whistleblowing conforme al D.Lgs. 24/2023.",
        "sezioni": [
            ("1. Canale crittografato e gestore autonomo", "Occorre un canale informatico crittografato (piu' modalita' orale su richiesta) gestito da un soggetto interno o esterno autonomo e formato (spesso l'OdV)."),
            ("2. Tempistiche tassative di gestione", "Entro 7 giorni dalla segnalazione va rilasciato avviso di ricevimento; entro 3 mesi va fornito riscontro motivato sull'esito o stato dell'istruttoria."),
            ("3. Tutela assoluta da ritorsioni e privacy", "L'identita' del segnalante e' protetta da rigoroso obbligo di riservatezza; ogni misura ritorsiva (licenziamento, demansionamento) e' nulla e sanzionata da ANAC fino a 50.000 euro.")
        ],
        "checklist": [
            "Attivare piattaforma whistleblowing crittografata (vietata l'email ordinaria).",
            "Consultare le rappresentanze sindacali e nominare formalmente il gestore.",
            "Redigere la DPIA GDPR e le informative privacy dedicate.",
            "Aggiornare il Modello 231 e il sistema disciplinare con sanzioni per violazione riservatezza o ritorsioni.",
            "Pubblicare istruzioni chiare per dipendenti e terzi anche sul sito aziendale."
        ],
        "faqs": [
            ("Vale anche per S.r.l. con meno di 50 dipendenti che hanno il Modello 231?", "Si': l'adozione del Modello 231 fa scattare l'obbligo del canale interno per le segnalazioni 231 a prescindere dal numero di dipendenti."),
            ("Cosa succede se arriva una segnalazione anonima?", "Se adeguatamente circostanziata e documentabile, va gestita e conservata secondo le regole delle segnalazioni ordinarie/whistleblowing.")
        ]
    },
    {
        "cod": "GSOC-05",
        "slug": "guida-difesa-urgenza-sequestro-preventivo-misure-interdittive-231",
        "pilastro": "sequestri-231-misure-interdittive-confisca",
        "titolo": "Guida alla difesa d'urgenza dell'ente da sequestro preventivo (art. 53) e misure interdittive (art. 45)",
        "seo_title": "Guida Difesa Urgenza 231: Sequestro Art. 53 e Interdizione Art. 45",
        "desc": "Protocollo operativo nelle prime 48 ore e nei 10 giorni perentori per impugnare sequestri sui conti aziendali e richieste cautelari interdittive 231.",
        "norme": ["Art. 39 D.Lgs. 231/2001", "Art. 45 D.Lgs. 231/2001", "Art. 49 D.Lgs. 231/2001", "Art. 53 D.Lgs. 231/2001"],
        "intro": "Quando la Procura colpisce l'azienda con un sequestro preventivo o chiede una misura interdittiva cautelare, ogni errore procedurale nei primi 10 giorni puo' essere irreversibile.",
        "sezioni": [
            ("1. Prima mossa: nomina valida del difensore senza conflitto (art. 39)", "Se il legale rappresentante e' indagato per il reato presupposto, non puo' nominare il difensore della societa': va nominato subito con delibera un procuratore speciale non indagato."),
            ("2. Riesame e appello cautelare entro 10 giorni", "Si impugnano sia i presupposti (fumus, interesse/vantaggio, esigenze cautelari) sia la quantificazione del profitto confiscabile con perizia contabile."),
            ("3. Sospensione riparatoria (art. 49) e Commissario (art. 15)", "Per salvare subito l'operativita', si attiva la sospensione ex art. 49 con piano di riparazione e adozione MOG 231, o in subordine la nomina di commissario giudiziale.")
        ],
        "checklist": [
            "Verificare subito se il legale rappresentante e' indagato e nominare procuratore speciale art. 39.",
            "Estrarre copia integrale del decreto/richiesta cautelare e calcolare i 10 giorni perentori.",
            "Affidare perizia contabile urgente sul profitto netto reale.",
            "Avviare subito discontinuità gestoria e piano di adeguamento Modello 231 ex art. 49.",
            "Documentare numero dipendenti e commesse pubbliche/essenziali per eventuale art. 15."
        ],
        "faqs": [
            ("Cosa succede se il legale rappresentante indagato firma la nomina dell'avvocato dell'ente?", "Il Tribunale dichiara inammissibile il Riesame o l'appello cautelare per difetto di legittimazione (art. 39 D.Lgs. 231/2001)."),
            ("Si possono sbloccare i conti sequestrati per pagare gli stipendi?", "Occorre agire con Riesame sul calcolo del profitto o istanze mirate di sostituzione/riduzione del sequestro.")
        ]
    },
    {
        "cod": "GSOC-06",
        "slug": "guida-condotte-riparatorie-art-17-49-dlgs-231",
        "pilastro": "modello-231-responsabilita-enti-odv",
        "titolo": "Guida alle condotte riparatorie ex artt. 17, 49 e 65 D.Lgs. 231/2001",
        "seo_title": "Guida Condotte Riparatorie Art. 17 D.Lgs. 231/2001: Evitare Interdizioni",
        "desc": "Come realizzare tempestivamente risarcimento, adozione del Modello 231 idoneo e messa a disposizione del profitto per evitare le sanzioni interdittive e dimezzare la sanzione pecuniaria.",
        "norme": ["Art. 12 D.Lgs. 231/2001", "Art. 17 D.Lgs. 231/2001", "Art. 49 D.Lgs. 231/2001", "Art. 65 D.Lgs. 231/2001"],
        "intro": "Il sistema 231 premia in modo decisivo l'ente che si riorganizza e ripara prima dell'apertura del dibattimento di primo grado.",
        "sezioni": [
            ("1. Le tre condizioni cumulative dell'art. 17", "Occorre: (a) risarcire integralmente il danno ed eliminare le conseguenze dannose; (b) adottare e attuare un Modello 231 idoneo a prevenire reati della stessa specie; (c) mettere a disposizione il profitto ai fini della confisca."),
            ("2. Sospensione del processo ex art. 65", "Se l'ente dimostra di non aver potuto completare gli adempimenti prima dell'apertura del dibattimento, puo' chiedere la sospensione del processo con prestazione di cauzione."),
            ("3. Effetti premiali su sanzioni pecuniarie e interdittive", "L'esito positivo esclude totalmente le sanzioni interdittive (art. 17) e riduce da un terzo alla meta' la sanzione pecuniaria (art. 12 co. 2).")
        ],
        "checklist": [
            "Quantificare danno risarcibile e profitto netto del reato.",
            "Rimuovere le carenze organizzative che hanno reso possibile l'illecito.",
            "Adottare e attuare realmente il Modello 231 con audit documentati dell'OdV.",
            "Depositare quietanze di risarcimento e messa a disposizione del profitto prima del dibattimento.",
            "In caso di tempi stretti, presentare istanza di sospensione ex art. 49 (cautelare) o art. 65 (dibattimento)."
        ],
        "faqs": [
            ("Basta adottare il Modello 231 senza risarcire il danno?", "No: per escludere le sanzioni interdittive ex art. 17 servono tutte e tre le condizioni cumulative; la sola adozione del MOG consente comunque la riduzione pecuniaria ex art. 12."),
            ("Entro quando va completato il percorso riparatorio?", "Prima della dichiarazione di apertura del dibattimento di primo grado.")
        ]
    },
    {
        "cod": "GSOC-07",
        "slug": "guida-composizione-negoziata-crisi-misure-protettive-ccii",
        "pilastro": "crisi-impresa-composizione-negoziata-ccii",
        "titolo": "Guida alla Composizione Negoziata della Crisi e alle misure protettive (artt. 12-25 CCII)",
        "seo_title": "Guida Composizione Negoziata Crisi CCII e Correttivo-ter D.Lgs. 136/2024",
        "desc": "Procedura completa passo passo per accedere alla Composizione Negoziata, ottenere misure protettive contro pignoramenti e fallimento e chiudere accordi con banche e Fisco.",
        "norme": ["Artt. 12-25-quinquies CCII", "Art. 18-19 CCII", "D.Lgs. 136/2024"],
        "intro": "La Composizione Negoziata e' lo strumento piu' rapido e riservato per salvare l'impresa in crisi mantenendo la gestione nelle mani dell'imprenditore.",
        "sezioni": [
            ("1. Preparazione del dossier e piattaforma CCIAA", "Prima del deposito si eseguono il test pratico, il piano finanziario a 6 mesi, il progetto di piano di risanamento e si raccolgono i certificati fiscali, previdenziali e Centrale Rischi."),
            ("2. Misure protettive e udienza di conferma", "Con la pubblicazione nel Registro Imprese scatta lo scudo contro pignoramenti e liquidazione giudiziale, da confermare in Tribunale con ricorso entro il giorno successivo (durata fino a 120 giorni, prorogabili a 240)."),
            ("3. Sbocchi positivi e transazione fiscale", "Il Correttivo-ter (D.Lgs. 136/2024) consente anche l'accordo transattivo con l'Agenzia delle Entrate (art. 23 co. 2-bis), cessione d'azienda senza debiti (art. 22) e, in caso di mancato accordo in buona fede, il concordato semplificato.")
        ],
        "checklist": [
            "Compilare test pratico di risanabilita' e piano finanziario a 6 mesi.",
            "Acquisire certificati unici AdE, AdER, INPS, INAIL e Centrale Rischi.",
            "Depositare istanza sulla piattaforma camerale con richiesta misure protettive e art. 20 CCII.",
            "Depositare il giorno successivo il ricorso di conferma in Tribunale ex art. 19 CCII.",
            "Condurre trattative trasparenti con Esperto, banche, Fisco e fornitori."
        ],
        "faqs": [
            ("Puo' accedere anche un'impresa gia' insolvente?", "Si', purche' sussista una concreta prospettiva di risanamento anche indiretto (es. cessione d'azienda in continuita')."),
            ("I fornitori possono risolvere i contratti per il solo accesso alla Composizione Negoziata?", "No, l'art. 18 co. 5 CCII vieta la risoluzione o sospensione di contratti essenziali per il solo mancato pagamento di crediti anteriori o per l'accesso alla procedura.")
        ]
    },
    {
        "cod": "GSOC-08",
        "slug": "guida-concordato-semplificato-liquidazione-patrimonio-art-25-sexies",
        "pilastro": "crisi-impresa-composizione-negoziata-ccii",
        "titolo": "Guida al Concordato Semplificato per la liquidazione del patrimonio (art. 25-sexies CCII)",
        "seo_title": "Guida Concordato Semplificato Art. 25-sexies CCII: Termini e Procedura",
        "desc": "Come accedere entro 60 giorni dalla chiusura negativa della Composizione Negoziata al concordato liquidatorio senza voto dei creditori e senza soglia del 20%.",
        "norme": ["Art. 25-sexies CCII", "Art. 25-septies CCII", "D.Lgs. 136/2024"],
        "intro": "Quando le trattative in Composizione Negoziata non approdano a un accordo nonostante la correttezza dell'imprenditore, il concordato semplificato consente una liquidazione ordinata senza voto dei creditori.",
        "sezioni": [
            ("1. Il presupposto decisivo: la relazione finale dell'Esperto", "L'Esperto deve attestare che le trattative si sono svolte secondo correttezza e buona fede e che le soluzioni ex art. 23 non sono praticabili."),
            ("2. Termine perentorio di 60 giorni e contenuto del piano", "Entro 60 giorni dalla comunicazione della relazione finale va depositato il ricorso con piano di cessione dei beni che assicuri un'utilita' a ciascun creditore senza arrecare pregiudizio rispetto alla liquidazione giudiziale."),
            ("3. Omologazione senza voto e vendite competitive", "I creditori non votano ma possono proporre opposizione all'omologazione; il Tribunale nomina un ausiliario e poi un liquidatore per la vendita competitiva dei beni.")
        ],
        "checklist": [
            "Verificare la doppia attestazione positiva nella relazione finale dell'Esperto.",
            "Rispettare tassativamente il termine di 60 giorni per il deposito del ricorso.",
            "Preparare perizie di stima e comparazione con lo scenario di liquidazione giudiziale.",
            "Verificare che ogni creditore riceva un'utilita' (anche non monetaria o minima ma effettiva).",
            "Predisporre eventuali offerte irrevocabili di acquisto cauzionate."
        ],
        "faqs": [
            ("Nel concordato semplificato serve il 20% ai chirografari?", "No: non si applicano le soglie del concordato preventivo liquidatorio ordinario."),
            ("Si puo' fare il concordato semplificato senza essere passati dalla Composizione Negoziata?", "No: e' accessibile solo come sbocco della Composizione Negoziata.")
        ]
    },
    {
        "cod": "GSOC-09",
        "slug": "guida-concordato-preventivo-continuita-vs-liquidatorio-ccii",
        "pilastro": "concordato-preventivo-accordi-ristrutturazione",
        "titolo": "Guida al Concordato Preventivo: continuita' aziendale diretta/indiretta vs liquidatorio",
        "seo_title": "Guida Concordato Preventivo CCII: Continuita' vs Liquidatorio",
        "desc": "Differenze operative, soglie, formazione delle classi, regola di priorita' relativa e cross-class cram-down nel concordato preventivo del Codice della Crisi.",
        "norme": ["Artt. 84-120-quinquies CCII", "D.Lgs. 136/2024"],
        "intro": "Il Codice della Crisi favorisce nettamente il concordato in continuita' aziendale rispetto a quello liquidatorio, introducendo regole molto diverse su soglie, distribuzione del valore e maggioranze.",
        "sezioni": [
            ("1. Concordato in continuita' (diretta o indiretta)", "Nessuna soglia minima fissa ai chirografari; classamento obbligatorio; valore di liquidazione distribuito con priorita' assoluta (APR) e surplus da continuita' con priorita' relativa (RPR)."),
            ("2. Concordato liquidatorio", "Richiede un apporto di risorse esterne che incrementi di almeno il 10% l'attivo disponibile e garantisca almeno il 20% ai creditori chirografari."),
            ("3. Voto dei creditori e cross-class cram-down", "In continuita' serve l'unanimita' delle classi oppure l'omologazione trasversale ex art. 112 co. 2 CCII; nel liquidatorio serve la maggioranza dei crediti (e della maggioranza delle classi se formate).")
        ],
        "checklist": [
            "Scegliere tra continuita' diretta, continuita' indiretta (affitto/cessione) o liquidatorio.",
            "Valutare il deposito con riserva ex art. 44 CCII se pendono pignoramenti o istanze.",
            "Incaricare advisor finanziario e attestatore indipendente.",
            "Costruire classi omogenee rispettando i casi obbligatori dell'art. 85 CCII.",
            "Integrare la proposta con transazione fiscale/previdenziale ex art. 88 CCII."
        ],
        "faqs": [
            ("Quale percentuale di crediti e' necessaria per approvare il concordato in continuita'?", "In ogni classe vota a favore la maggioranza dei crediti ammessi al voto (o i 2/3 dei votanti se vota almeno la meta'); con dissenso di alcune classi opera il cross-class cram-down ex art. 112 co. 2."),
            ("Durante il concordato l'imprenditore resta in azienda?", "Si', conserva l'amministrazione ordinaria sotto la vigilanza del commissario giudiziale.")
        ]
    },
    {
        "cod": "GSOC-10",
        "slug": "guida-transazione-fiscale-cram-down-agenzia-entrate-inps",
        "pilastro": "concordato-preventivo-accordi-ristrutturazione",
        "titolo": "Guida alla Transazione Fiscale e al cram-down contro Agenzia Entrate e INPS (artt. 63 e 88 CCII)",
        "seo_title": "Guida Transazione Fiscale e Cram-Down Art. 63 e 88 CCII",
        "desc": "Come strutturare lo stralcio e la dilazione di IVA, imposte e contributi INPS e ottenere l'omologazione forzosa (cram-down) dopo il Correttivo-ter D.Lgs. 136/2024.",
        "norme": ["Art. 63 CCII", "Art. 88 CCII", "Art. 23 co. 2-bis CCII", "D.Lgs. 136/2024"],
        "intro": "La transazione fiscale e previdenziale consente di falcidiare anche IVA e ritenute (capitale, sanzioni e interessi) e di superare il dissenso o il silenzio del Fisco tramite il cram-down giudiziale.",
        "sezioni": [
            ("1. Dove si puo' usare la transazione fiscale", "Negli Accordi di Ristrutturazione (art. 63), nel Concordato Preventivo (art. 88), nel PRO (art. 64-bis) e, senza cram-down giudiziale, nella Composizione Negoziata (art. 23 co. 2-bis)."),
            ("2. Requisiti del cram-down dopo il Correttivo-ter D.Lgs. 136/2024", "Il Tribunale puo' omologare forzatamente solo se la proposta e' piu' conveniente della liquidazione giudiziale, determinante per le maggioranze e rispetta le nuove soglie minime di soddisfacimento e di non liquidatorieta' previste per gli ARD."),
            ("3. La perizia di convenienza comparativa", "E' il documento decisivo: deve dimostrare con dati inoppugnabili che nella liquidazione giudiziale Erario e INPS incasserebbero di meno.")
        ],
        "checklist": [
            "Acquisire certificati unici aggiornati da AdE, AdER, INPS e INAIL.",
            "Far redigere l'attestazione di convenienza comparativa rispetto alla liquidazione giudiziale.",
            "Verificare il rispetto delle soglie anti-abuso del D.Lgs. 136/2024 per il cram-down.",
            "Notificare la proposta agli uffici competenti rispettando il termine di 90 giorni negli ARD.",
            "Presentare istanza motivata di cram-down in caso di diniego o mancata risposta."
        ],
        "faqs": [
            ("Oggi si puo' falcidiare anche l'IVA?", "Si', nel rispetto della convenienza rispetto alla liquidazione giudiziale e delle regole di distribuzione."),
            ("Quanto tempo ha l'Agenzia delle Entrate per rispondere negli ARD?", "90 giorni dal deposito della proposta completa ex art. 63 CCII.")
        ]
    },
    {
        "cod": "GSOC-11",
        "slug": "guida-accordi-ristrutturazione-debiti-pro-ccii",
        "pilastro": "concordato-preventivo-accordi-ristrutturazione",
        "titolo": "Guida agli Accordi di Ristrutturazione dei Debiti (ARD) e al PRO (artt. 57-64-bis CCII)",
        "seo_title": "Guida Accordi Ristrutturazione Debiti (ARD) e PRO Art. 64-bis CCII",
        "desc": "Confronto operativo tra ARD ordinari (60%), agevolati (30%), ad efficacia estesa (75%) e Piano di Ristrutturazione soggetto ad Omologazione (PRO).",
        "norme": ["Artt. 57-61 CCII", "Art. 64-bis CCII", "Art. 48 CCII"],
        "intro": "Gli Accordi di Ristrutturazione e il PRO offrono flessibilita' negoziale superiore al concordato preventivo quando l'impresa ha un tavolo creditori concentrato.",
        "sezioni": [
            ("1. Le tre varianti degli Accordi di Ristrutturazione", "Ordinari (60% adesioni, 120 giorni di moratoria sugli estranei), Agevolati (30% adesioni, nessuna moratoria ne' misure protettive), Efficacia Estesa (75% nella categoria omogenea per vincolare i dissenzienti)."),
            ("2. Il PRO (art. 64-bis CCII)", "Consente di distribuire il valore derogando liberamente all'ordine dei privilegi (salvi i lavoratori pagati al 100% entro 30 giorni), ma richiede il voto favorevole di tutte le classi."),
            ("3. Protezioni e vantaggi fiscali", "Esenzione da revocatoria e bancarotta (artt. 166 e 324 CCII), detassazione sopravvenienze attive (art. 88 TUIR) e misure protettive durante le trattative.")
        ],
        "checklist": [
            "Mappare la concentrazione del passivo per scegliere tra ARD 60%, 30%, 75% o PRO.",
            "Chiedere misure protettive nelle trattative ex art. 54 co. 3 CCII se necessario.",
            "Ottenere attestazione di veridicita' e fattibilita' (e integrale pagamento estranei per ARD).",
            "Pubblicare gli accordi nel Registro Imprese e depositare ricorso di omologazione.",
            "Prevedere piano B di conversione in concordato se nel PRO una classe dissente (art. 64-quater)."
        ],
        "faqs": [
            ("Negli ARD devo pagare al 100% chi non firma?", "Si', salvo che scatti l'efficacia estesa ex art. 61 CCII o il cram-down fiscale ex art. 63 CCII."),
            ("Il PRO prevede un commissario giudiziale?", "Si', il Tribunale nomina un commissario con funzioni di vigilanza, ma l'imprenditore conserva gestione ordinaria e straordinaria.")
        ]
    },
    {
        "cod": "GSOC-12",
        "slug": "guida-difesa-istanza-liquidazione-giudiziale-soglie-impresa-minore",
        "pilastro": "liquidazione-giudiziale-fallimento-opposizioni",
        "titolo": "Guida alla difesa dall'istanza di Liquidazione Giudiziale e verifica delle soglie",
        "seo_title": "Guida Difesa Istanza Liquidazione Giudiziale: Soglie e Udienza",
        "desc": "Checklist d'urgenza quando arriva la notifica di un ricorso per liquidazione giudiziale: memoria 7 giorni prima, soglie impresa minore (300k/200k/500k), soglia 30.000 euro e desistenza.",
        "norme": ["Art. 2 co. 1 lett. d CCII", "Art. 41 CCII", "Art. 49 co. 5 CCII"],
        "intro": "Una difesa prefallimentare tempestiva e documentata puo' evitare l'apertura della liquidazione giudiziale salvando azienda e amministratori.",
        "sezioni": [
            ("1. Verifica immediata delle soglie oggettive e soggettive", "Si controllano subito le tre soglie di impresa minore (attivo <= 300.000, ricavi <= 200.000, debiti <= 500.000 euro) e la soglia di 30.000 euro di debiti scaduti."),
            ("2. Costituzione almeno 7 giorni prima dell'udienza", "Vanno depositati obbligatoriamente i bilanci degli ultimi 3 esercizi, la situazione patrimoniale aggiornata e tutte le eccezioni su inesistenza del credito o dell'insolvenza."),
            ("3. Trattativa per desistenza o accesso a strumento CCII", "In parallelo si tratta con il creditore istante per il deposito della desistenza oppure si presenta domanda di accesso a uno strumento di regolazione della crisi (trattazione prioritaria ex art. 7 CCII).")
        ],
        "checklist": [
            "Controllare data udienza e termine di costituzione (7 giorni prima ex art. 41 co. 4 CCII).",
            "Accedere al fascicolo telematico per verificare le informative d'ufficio AdE/AdER/INPS.",
            "Raccogliere bilanci ultimi 3 esercizi e verificare le tre soglie di impresa minore.",
            "Contattare il creditore istante per eventuale saldo e stralcio con desistenza formale.",
            "Valutare in alternativa l'accesso a Composizione Negoziata o concordato con riserva."
        ],
        "faqs": [
            ("Chi deve provare che l'azienda e' sotto le soglie di non fallibilita'?", "L'onere della prova grava integralmente sul debitore resistente."),
            ("Basta pagare il creditore istante per chiudere il procedimento?", "Si', se il creditore deposita formale desistenza e non vi sono altri creditori intervenuti ne' istanza del PM.")
        ]
    },
    {
        "cod": "GSOC-13",
        "slug": "guida-reclamo-corte-appello-liquidazione-giudiziale-art-51",
        "pilastro": "liquidazione-giudiziale-fallimento-opposizioni",
        "titolo": "Guida al reclamo in Corte d'Appello contro la sentenza di Liquidazione Giudiziale (art. 51 CCII)",
        "seo_title": "Guida Reclamo Liquidazione Giudiziale Art. 51 CCII: 30 Giorni",
        "desc": "Come impugnare entro 30 giorni la sentenza di apertura della liquidazione giudiziale e ottenere la sospensione della vendita dei beni ex art. 52 CCII.",
        "norme": ["Art. 51 CCII", "Art. 52 CCII", "Art. 53 CCII"],
        "intro": "Contro la sentenza di apertura della liquidazione giudiziale il debitore e ogni interessato possono proporre reclamo alla Corte d'Appello entro 30 giorni.",
        "sezioni": [
            ("1. Termine perentorio di 30 giorni e natura del giudizio", "I 30 giorni decorrono dalla notificazione della sentenza al debitore (o dall'iscrizione al Registro Imprese per terzi). Il reclamo consente anche nuove deduzioni e documenti decisivi."),
            ("2. Istanza urgente di sospensione della liquidazione (art. 52)", "Il reclamo non sospende automaticamente gli effetti della sentenza: occorre chiedere subito alla Corte la sospensione della vendita dell'attivo per gravi e fondati motivi."),
            ("3. Effetti della revoca", "La revoca restituisce i beni al debitore, ma restano salvi gli atti legalmente compiuti dagli organi della procedura nel frattempo (art. 53 CCII).")
        ],
        "checklist": [
            "Verificare la data di notifica della sentenza e fissare la scadenza dei 30 giorni.",
            "Esaminare vizi di notifica del ricorso introduttivo, soglie art. 2 CCII e stato di solvibilita'.",
            "Inserire nel reclamo l'istanza urgente di sospensione della liquidazione dell'attivo ex art. 52.",
            "Notificare il reclamo sia al curatore sia al creditore istante (e al PM se istante).",
            "Produrre tutta la documentazione contabile e probatoria a supporto."
        ],
        "faqs": [
            ("Posso produrre in Corte d'Appello i bilanci che non avevo depositato in Tribunale?", "Si', nel reclamo ex art. 51 CCII e' ammessa la produzione di nuovi documenti decisivi per provare la non fallibilita' o la solvibilita'."),
            ("Il reclamo blocca automaticamente il curatore?", "No, serve un espresso provvedimento di sospensione ex art. 52 CCII.")
        ]
    },
    {
        "cod": "GSOC-14",
        "slug": "guida-insinuazione-stato-passivo-opposizione-art-206-ccii",
        "pilastro": "liquidazione-giudiziale-fallimento-opposizioni",
        "titolo": "Guida all'insinuazione allo stato passivo (tempestiva/tardiva) e all'opposizione (art. 206 CCII)",
        "seo_title": "Guida Insinuazione Stato Passivo e Opposizione Art. 206 CCII",
        "desc": "Procedura completa per fornitori, professionisti, banche e lavoratori: data certa, privilegi, osservazioni al progetto di stato passivo e ricorso in opposizione entro 30 giorni.",
        "norme": ["Art. 201 CCII", "Art. 206 CCII", "Art. 208 CCII", "Art. 2704 c.c."],
        "intro": "Per recuperare un credito verso una societa' in liquidazione giudiziale, la precisione della domanda di ammissione al passivo fa la differenza tra incassare ed essere esclusi.",
        "sezioni": [
            ("1. Domanda tempestiva (30 giorni prima) e prova della data certa", "La domanda si invia via PEC al curatore senza ministero obbligatorio di avvocato (ma l'assistenza legale e' decisiva per privilegi e data certa ex art. 2704 c.c., oggi provata dalle ricevute SDI)."),
            ("2. Osservazioni al progetto del curatore e domanda tardiva (6 mesi)", "Fino a 5 giorni prima dell'udienza si possono inviare osservazioni scritte e documenti integrativi; le tardive vanno presentate entro 6 mesi dall'esecutivita'."),
            ("3. Opposizione allo stato passivo (30 giorni, con avvocato)", "Contro l'esclusione o il declassamento del privilegio va depositato ricorso collegiale ex art. 206 CCII entro 30 giorni dalla PEC del curatore, indicando a pena di decadenza tutte le prove.")
        ],
        "checklist": [
            "Controllare la data dell'udienza di verifica nella PEC del curatore (scadenza -30 giorni).",
            "Allegare fatture elettroniche con ricevuta SDI, contratti, DDT e prova dell'adempimento.",
            "Specificare esattamente la norma del privilegio invocato (es. art. 2751-bis c.c.).",
            "Verificare il progetto di stato passivo del curatore e inviare osservazioni fino a -5 giorni.",
            "In caso di esclusione, proporre opposizione ex art. 206 CCII entro 30 giorni."
        ],
        "faqs": [
            ("Le fatture elettroniche hanno data certa opponibile al curatore?", "Si', la ricevuta di consegna/messa a disposizione del Sistema di Interscambio (SDI) fornisce prova certa dell'anteriorita'."),
            ("Per l'opposizione allo stato passivo serve l'avvocato?", "Si', l'opposizione ex art. 206 CCII e' un vero giudizio collegiale che richiede difesa tecnica.")
        ]
    },
    {
        "cod": "GSOC-15",
        "slug": "guida-difesa-azioni-revocatorie-concorsuali-ordinarie-ccii",
        "pilastro": "liquidazione-giudiziale-fallimento-opposizioni",
        "titolo": "Guida alla difesa da azioni revocatorie concorsuali e ordinarie (artt. 165-166 CCII)",
        "seo_title": "Guida Difesa Azioni Revocatorie Art. 165 e 166 CCII",
        "desc": "Come difendere fornitori, acquirenti e banche dalle richieste restitutorie del curatore: periodo sospetto, esenzione termini d'uso, decadenza 3 anni e revocatoria ordinaria 5 anni.",
        "norme": ["Art. 165 CCII", "Art. 166 CCII", "Art. 170 CCII", "Art. 2901 c.c."],
        "intro": "Le azioni revocatorie del curatore colpiscono spesso fornitori e acquirenti in buona fede che avevano concluso normali affari mesi o anni prima della crisi.",
        "sezioni": [
            ("1. Verifica preliminare di decadenza e periodo sospetto", "La revocatoria concorsuale decade in 3 anni dall'apertura (e 5 dall'atto ex art. 170 CCII); il periodo sospetto (6 mesi o 1 anno) decorre a ritroso dalla domanda di liquidazione giudiziale."),
            ("2. Le esenzioni assolute dell'art. 166 co. 3 CCII", "Sono esenti i pagamenti nei termini d'uso, le rimesse bancarie senza riduzione durevole, le vendite a giusto prezzo di prima casa e gli atti in esecuzione di piani attestati, ARD o concordati."),
            ("3. Scientia decoctionis e revocatoria ordinaria", "Per i pagamenti di debiti scaduti (art. 166 co. 2) il curatore deve provare la conoscenza effettiva dell'insolvenza; nell'ordinaria (art. 165, fino a 5 anni) i pagamenti di debiti scaduti sono esenti ex art. 2901 co. 3 c.c.")
        ],
        "checklist": [
            "Calcolare esattamente periodo sospetto e termine di decadenza/prescrizione.",
            "Verificare subito le esenzioni assolute dell'art. 166 co. 3 (specie 'termini d'uso').",
            "Produrre storico pagamenti, bilanci pubblici e visure negative per escludere la scientia decoctionis.",
            "Per le banche, calcolare la riduzione durevole e il tetto del massimo scoperto (art. 171 co. 3).",
            "Valutare un'eventuale transazione vantaggiosa col curatore se il rischio e' concreto."
        ],
        "faqs": [
            ("Se restituisco i soldi al curatore per revocatoria, li perdo del tutto?", "Il revocato ha diritto di insinuarsi al passivo per l'importo restituito ex art. 171 co. 2 CCII (ma di regola in chirografo)."),
            ("I pagamenti di forniture regolari degli ultimi 6 mesi sono sempre revocabili?", "No: se effettuati con modalita' e tempi abituali tra le parti rientrano nell'esenzione 'termini d'uso' (art. 166 co. 3 lett. a).")
        ]
    },
    {
        "cod": "GSOC-16",
        "slug": "guida-difesa-penale-bancarotta-fraudolenta-semplice-ccii",
        "pilastro": "bancarotta-reati-fallimentari-societari",
        "titolo": "Guida alla difesa penale per bancarotta fraudolenta, semplice e impropria (artt. 322-329 CCII)",
        "seo_title": "Guida Difesa Penale Bancarotta Fraudolenta e Semplice Art. 322 CCII",
        "desc": "Strategia difensiva completa per amministratori, sindaci e prestanome: analisi relazione curatore, perizia contabile di parte, bancarotta riparata e riqualificazione.",
        "norme": ["Artt. 322-329 CCII", "Artt. 216-223 L.F."],
        "intro": "Nei processi per bancarotta la difesa si vince unendo tecnica penalistica e ricostruzione contabile analitica fin dal primo atto di indagine.",
        "sezioni": [
            ("1. La relazione del curatore (art. 130 CCII / 33 L.F.)", "E' la fonte primaria dell'accusa: va acquisita e sezionata voce per voce con un consulente tecnico contabile per smentire distrazioni apparenti o ammanchi di cassa meramente contabili."),
            ("2. Linea di difesa per tipologia di contestazione", "Sulla patrimoniale: prova della destinazione aziendale o bancarotta riparata; sulla documentale: assenza di dolo specifico e ricostruibilita' via SDI/banche; sull'impropria: assenza di nesso causale col dissesto."),
            ("3. Posizioni differenziate (prestanome, amministratore di fatto, sindaci)", "Ogni posizione richiede una difesa autonoma e priva di conflitto di interessi per evitare che le colpe di un soggetto ricadano sugli altri.")
        ],
        "checklist": [
            "Acquisire la relazione del curatore e tutti gli atti del fascicolo fallimentare e penale.",
            "Nominare un consulente tecnico contabile di parte per l'analisi dei flussi bancari.",
            "Verificare la legittimita' di eventuali sequestri preventivi (Riesame entro 10 giorni).",
            "Valutare memorie difensive ex art. 415-bis c.p.p. e riti alternativi o messa alla prova (per semplice).",
            "Separare le difese tra amministratore di diritto, amministratore di fatto e sindaci."
        ],
        "faqs": [
            ("Puo' esserci bancarotta senza sentenza di liquidazione giudiziale?", "No: la sentenza di apertura della liquidazione giudiziale (o fallimento) e' condizione indispensabile per la punibilita' della bancarotta."),
            ("La bancarotta semplice consente la messa alla prova?", "Si', rientrando nei limiti edittali dell'art. 168-bis c.p. (pena fino a 2 anni).")
        ]
    },
    {
        "cod": "GSOC-17",
        "slug": "guida-false-comunicazioni-sociali-reati-societari-codice-civile",
        "pilastro": "bancarotta-reati-fallimentari-societari",
        "titolo": "Guida alle false comunicazioni sociali (artt. 2621-2622 c.c.) e ai reati societari",
        "seo_title": "Guida False Comunicazioni Sociali Art. 2621 c.c. e Reati Societari",
        "desc": "Quadro completo dei reati societari nel Codice Civile: falso in bilancio, lieve entita' e querela per imprese non fallibili (art. 2621-bis), infedelta' patrimoniale e impedito controllo.",
        "norme": ["Artt. 2621-2622 c.c.", "Artt. 2621-bis e 2621-ter c.c.", "Artt. 2625-2635 c.c."],
        "intro": "I reati societari colpiscono sia gli amministratori sia la societa' (art. 25-ter D.Lgs. 231/2001) e richiedono una difesa che padroneggi principi contabili OIC/IAS e diritto penale.",
        "sezioni": [
            ("1. Falso in bilancio: fatti materiali rilevanti e valutazioni", "La condotta deve riguardare fatti materiali rilevanti idonei a indurre in errore, con dolo specifico di ingiusto profitto. Le valutazioni estimative rilevano solo se si discostano scientemente dai criteri legali dichiarati."),
            ("2. Le valvole di sicurezza: artt. 2621-bis e 2621-ter c.c.", "Per fatti di lieve entita' la pena scende (6 mesi - 3 anni); per le societa' non fallibili (sotto soglie art. 2 CCII) il reato e' procedibile SOLO a querela; per la particolare tenuita' opera la non punibilita'."),
            ("3. Altri reati societari ricorrenti", "Impedito controllo (art. 2625), indebita restituzione conferimenti e utili (artt. 2626-2627), infedelta' patrimoniale (art. 2634) e corruzione tra privati (art. 2635).")
        ],
        "checklist": [
            "Verificare le soglie di impresa minore per l'eventuale procedibilita' a querela (art. 2621-bis co. 2).",
            "Far verificare da CTP la conformita' delle poste ai principi contabili OIC/IAS.",
            "Controllare la sussistenza del dolo specifico e della concreta idoneita' decettiva.",
            "Verificare l'eventuale estinzione per ricostituzione riserve ex art. 2627 co. 2.",
            "Coordinare la difesa personale con quella dell'ente ex art. 25-ter D.Lgs. 231/2001."
        ],
        "faqs": [
            ("Un errore involontario in bilancio e' reato?", "No: le false comunicazioni sociali richiedono il dolo specifico e la consapevole esposizione di fatti non rispondenti al vero."),
            ("Il falso in bilancio comporta responsabilita' 231 della societa'?", "Si', rientra tra i reati presupposto dell'art. 25-ter D.Lgs. 231/2001 se commesso nell'interesse della societa'.")
        ]
    },
    {
        "cod": "GSOC-18",
        "slug": "guida-difesa-amministratori-azioni-responsabilita-art-2486",
        "pilastro": "responsabilita-amministratori-sindaci-azioni",
        "titolo": "Guida alla difesa degli amministratori da azioni di responsabilita' e dal calcolo ex art. 2486 c.c.",
        "seo_title": "Guida Difesa Amministratori Azioni Responsabilita' e Art. 2486 c.c.",
        "desc": "Strategia completa davanti al Tribunale delle Imprese: prescrizione quinquennale, business judgment rule, polizze D&O e contestazione del criterio dei netti patrimoniali.",
        "norme": ["Artt. 2392-2395 c.c.", "Art. 2476 c.c.", "Art. 2486 co. 3 c.c.", "Art. 255 CCII"],
        "intro": "Quando un curatore o un socio agisce in responsabilita' contro un amministratore, il patrimonio personale del convenuto va protetto con una strategia giuridica e contabile integrata.",
        "sezioni": [
            ("1. Eccezioni preliminari: prescrizione e legittimazione", "L'azione si prescrive in 5 anni: per i creditori/curatore il termine decorre dal momento in cui l'insufficienza patrimoniale era oggettivamente percepibile dai bilanci pubblici."),
            ("2. Difesa nel merito: business judgment rule e deleghe", "Il giudice non puo' sindacare la convenienza economica di scelte imprenditoriali ragionevoli ex ante; per i consiglieri senza deleghe vale il limite dell'art. 2381 c.c."),
            ("3. Demolizione del quantum (art. 2486 co. 3 c.c.)", "Il criterio dei netti patrimoniali ammette prova contraria: vanno confrontati patrimoni netti omogenei e detratti i costi inevitabili di una liquidazione ordinata.")
        ],
        "checklist": [
            "Denunciare subito il sinistro alla polizza D&O (clausola claims-made).",
            "Verificare la data di oggettiva manifesta insufficienza patrimoniale per eccepire la prescrizione.",
            "Raccogliere verbali di CdA, deleghe e documenti che provano la diligenza ex ante.",
            "Affidare a un CTP la rielaborazione omogenea dei netti patrimoniali ex art. 2486 co. 3.",
            "Preparare la difesa cautelare contro eventuali richieste di sequestro conservativo."
        ],
        "faqs": [
            ("Il criterio del deficit fallimentare si applica sempre?", "No: solo quando mancano le scritture contabili o per irregolarita' delle stesse non e' possibile ricostruire i netti patrimoniali."),
            ("Una polizza D&O copre anche il dolo?", "No, copre di regola colpa e spese di difesa, salvo esclusioni contrattuali da verificare subito.")
        ]
    },
    {
        "cod": "GSOC-19",
        "slug": "guida-nuova-responsabilita-collegio-sindacale-legge-35-2025",
        "pilastro": "responsabilita-amministratori-sindaci-azioni",
        "titolo": "Guida alla nuova responsabilita' del Collegio Sindacale dopo la Legge 35/2025 (art. 2407 c.c.)",
        "seo_title": "Guida Nuova Responsabilita' Sindaci Legge 35/2025 Art. 2407 c.c.",
        "desc": "Tutto sulla riforma dell'art. 2407 c.c. entrata in vigore il 12 aprile 2025: tetto risarcitorio 15x/12x/10x, prescrizione 5 anni dal deposito relazione art. 2429 e regole transitorie.",
        "norme": ["Art. 2407 c.c.", "L. 14 marzo 2025, n. 35", "Art. 2429 c.c.", "Art. 25-octies CCII"],
        "intro": "La Legge 35/2025 ha rivoluzionato il regime risarcitorio dei sindaci delle societa' di capitali, sostituendo la responsabilita' illimitata per colpa con un tetto proporzionale al compenso.",
        "sezioni": [
            ("1. Il tetto quantitativo sui tre scaglioni", "Salvo dolo, la responsabilita' dei sindaci (anche se incaricati della revisione legale) e' limitata a 15 volte il compenso annuo fino a 10.000 euro, 12 volte tra 10.000 e 50.000 euro e 10 volte oltre 50.000 euro."),
            ("2. Prescrizione certa di 5 anni", "Il nuovo quarto comma fissa la prescrizione in 5 anni dal deposito della relazione ex art. 2429 c.c. relativa all'esercizio in cui si e' verificato il danno."),
            ("3. Applicazione temporale e difesa sui fatti anteriori", "Per i fatti anteriori al 12 aprile 2025 la giurisprudenza esclude la retroattivita' del tetto: occorre quindi combinare le difese tradizionali (nesso causale, segnalazioni tempestive, assenza di segnali d'allarme) con i nuovi principi.")
        ],
        "checklist": [
            "Verificare la data esatta dei fatti contestati rispetto al 12 aprile 2025.",
            "Documentare il compenso annuo deliberato per calcolare lo scaglione 15x/12x/10x.",
            "Controllare le date di deposito delle relazioni ex art. 2429 c.c. ai fini della prescrizione.",
            "Produrre tutti i verbali trimestrali e le segnalazioni ex art. 25-octies CCII.",
            "Attivare tempestivamente la polizza RC professionale del sindaco."
        ],
        "faqs": [
            ("Il tetto della L. 35/2025 vale se il sindaco ha agito con dolo?", "No: la norma esclude espressamente le ipotesi di dolo."),
            ("Il tetto vale anche quando il collegio sindacale fa la revisione legale?", "Si', lo prevede espressamente il nuovo art. 2407 co. 2 c.c.")
        ]
    },
    {
        "cod": "GSOC-20",
        "slug": "guida-impugnazione-delibere-assembleari-bilancio-tribunale-imprese",
        "pilastro": "contenzioso-soci-patti-parasociali-recesso",
        "titolo": "Guida all'impugnazione delle delibere assembleari e di bilancio davanti al Tribunale delle Imprese",
        "seo_title": "Guida Impugnazione Delibere Assembleari e Bilancio: 90 Giorni e 3 Anni",
        "desc": "Come distinguere delibere annullabili (90 giorni) e nulle (3 anni), ottenere la sospensione cautelare e impugnare bilanci irregolari prima dell'esercizio successivo.",
        "norme": ["Artt. 2377-2379 c.c.", "Art. 2434-bis c.c.", "Art. 2479-ter c.c."],
        "intro": "Impugnare tempestivamente una delibera illegittima o in abuso di maggioranza e' lo strumento principale per fermare operazioni lesive dei diritti dei soci.",
        "sezioni": [
            ("1. Annullabilita' (90 giorni) vs Nullita' (3 anni o imprescrittibile)", "I vizi di convocazione, conflitto di interessi e abuso di maggioranza si impugnano in 90 giorni; l'assoluta mancanza di informazione o l'oggetto illecito/impossibile in 3 anni (o senza limiti per oggetto illecito)."),
            ("2. Sospensione cautelare ex art. 2378 co. 3 c.c.", "Con ricorso contestuale alla citazione si chiede al giudice di sospendere subito l'esecuzione della delibera dimostrando il pregiudizio comparato."),
            ("3. Limite speciale per i bilanci (art. 2434-bis c.c.)", "Il bilancio non puo' piu' essere impugnato una volta approvato il bilancio dell'esercizio successivo: la rapidita' e' decisiva.")
        ],
        "checklist": [
            "Verificare statuto (eventuale clausola arbitrale) e data di trascrizione/iscrizione della delibera.",
            "Accertare la legittimazione (voto contrario, astenuto o assente; quorum 5% in S.p.A. chiuse).",
            "Notificare la citazione entro i 90 giorni (o prima del bilancio successivo).",
            "Depositare contestuale ricorso cautelare di sospensione se la delibera e' esecutiva.",
            "Allegare perizia contabile in caso di impugnazione di bilancio."
        ],
        "faqs": [
            ("Chi ha votato a favore puo' impugnare la delibera?", "No per le delibere annullabili; per le delibere nulle la legittimazione spetta a chiunque vi abbia interesse."),
            ("Qual e' il giudice competente?", "La Sezione Specializzata in materia di Impresa (Tribunale delle Imprese) del luogo della sede legale, salva clausola arbitrale statutaria.")
        ]
    },
    {
        "cod": "GSOC-21",
        "slug": "guida-diritto-controllo-socio-srl-art-2476-denuncia-2409",
        "pilastro": "contenzioso-soci-patti-parasociali-recesso",
        "titolo": "Guida al diritto di controllo del socio di S.r.l. (art. 2476 c.c.) e alla denuncia ex art. 2409 c.c.",
        "seo_title": "Guida Controllo Socio S.r.l. Art. 2476 c.c. e Denuncia Art. 2409 c.c.",
        "desc": "I due strumenti piu' potenti del socio di minoranza: accesso a tutti i documenti aziendali anche con ricorso ex art. 700 c.p.c. e denuncia al Tribunale per gravi irregolarita'.",
        "norme": ["Art. 2476 co. 2-3 c.c.", "Art. 2409 c.c.", "Art. 2477 co. 6 c.c.", "Art. 700 c.p.c."],
        "intro": "Il socio di minoranza non e' privo di difese: la legge gli attribuisce poteri penetranti di ispezione contabile e di attivazione del controllo giudiziario.",
        "sezioni": [
            ("1. Accesso integrale ai documenti (art. 2476 co. 2 c.c.)", "Ogni socio non amministratore di S.r.l. (anche con quota minima) puo' consultare ed estrarre copia di libri sociali, fatture, contratti ed estratti conto, anche tramite professionisti di fiducia."),
            ("2. Ricorso d'urgenza ex art. 700 c.p.c. con penale giornaliera", "Se l'amministratore oppone rifiuti o ritardi, il Tribunale delle Imprese ordina l'esibizione in via d'urgenza fissando una penale (astreinte) per ogni giorno di inottemperanza."),
            ("3. Denuncia al Tribunale ex art. 2409 c.c.", "Con almeno il 10% del capitale, in presenza di fondato sospetto di gravi irregolarita' potenzialmente dannose (inclusa l'assenza di adeguati assetti), si ottiene l'ispezione giudiziale fino alla nomina di un amministratore giudiziario.")
        ],
        "checklist": [
            "Inviare PEC di richiesta accesso atti dettagliata indicando il professionista delegato.",
            "In caso di rifiuto o silenzio dopo 10-15 giorni, depositare ricorso ex art. 700 c.p.c.",
            "Analizzare con un commercialista estratti conto, contratti e compensi acquisiti.",
            "Se emergono gravi irregolarita', valutare revoca cautelare (art. 2476 co. 3) o ricorso art. 2409 c.c.",
            "Valutare la trattativa di uscita (way-out) da posizione di forza documentale."
        ],
        "faqs": [
            ("L'amministratore puo' negare gli estratti conto per motivi di privacy?", "No: il diritto di controllo del socio prevale, salvo limiti mirati solo in caso di provata concorrenza sleale del socio."),
            ("L'art. 2409 c.c. vale anche per le S.r.l. senza collegio sindacale?", "Si', dopo la riforma del CCII l'art. 2477 co. 6 c.c. rende applicabile l'art. 2409 a tutte le S.r.l.")
        ]
    },
    {
        "cod": "GSOC-22",
        "slug": "guida-recesso-socio-valutazione-liquidazione-quota-art-2473",
        "pilastro": "contenzioso-soci-patti-parasociali-recesso",
        "titolo": "Guida al recesso del socio e alla liquidazione della quota a valore di mercato (art. 2473 c.c.)",
        "seo_title": "Guida Recesso Socio S.r.l. Art. 2473 c.c.: Calcolo Valore Quota",
        "desc": "Cause legali e statutarie di recesso, termini di comunicazione, contestazione del valore contabile, nomina dell'esperto del Tribunale e pagamento entro 180 giorni.",
        "norme": ["Art. 2473 c.c.", "Art. 2437 c.c.", "Art. 2437-ter c.c."],
        "intro": "Il recesso consente al socio di uscire dalla societa' ottenendo la liquidazione della propria partecipazione al valore effettivo di mercato, non al valore nominale.",
        "sezioni": [
            ("1. Quando spetta il diritto di recesso", "Cause legali inderogabili (cambio oggetto sociale, trasformazione, fusione/scissione, trasferimento sede all'estero, societa' a tempo indeterminato con preavviso 180 giorni) piu' le cause previste dallo statuto."),
            ("2. Determinazione del valore di mercato", "La quota va stimata tenendo conto del valore di mercato del patrimonio sociale (inclusi avviamento e valori reali degli immobili); in caso di disaccordo decide un esperto nominato dal Tribunale."),
            ("3. Modalita' e tempi di pagamento (180 giorni)", "Il rimborso deve avvenire entro 180 giorni dalla comunicazione di recesso tramite acquisto da parte degli altri soci, di un terzo o utilizzando riserve disponibili/riduzione capitale.")
        ],
        "checklist": [
            "Verificare causa legittimante nello statuto e nel codice civile.",
            "Inviare la dichiarazione di recesso via PEC entro i termini perentori.",
            "Far predisporre una perizia di parte sul valore reale di mercato dell'azienda.",
            "In caso di stima al ribasso degli amministratori, ricorrere al Tribunale per nomina esperto.",
            "Monitorare la scadenza dei 180 giorni e agire per il recupero del credito liquido."
        ],
        "faqs": [
            ("Posso recedere in qualsiasi momento da una S.r.l. a tempo indeterminato?", "Si', dando un preavviso di almeno 180 giorni (o il maggior termine statutario fino a 1 anno)."),
            ("La societa' puo' bloccare il recesso revocando la delibera contestata?", "Si', se revoca la delibera che ha legittimato il recesso o delibera lo scioglimento della societa'.")
        ]
    },
    {
        "cod": "GSOC-23",
        "slug": "guida-cessione-azienda-due-diligence-ma-debiti-fiscali-lavoro",
        "pilastro": "ma-cessione-azienda-fusioni-scissioni",
        "titolo": "Guida alla cessione d'azienda e alla due diligence M&A (art. 2560 c.c. e art. 14 D.Lgs. 472/97)",
        "seo_title": "Guida Cessione d'Azienda e M&A: Due Diligence, Debiti e Contratti",
        "desc": "Checklist operativa completa per comprare o vendere un'azienda o quote societarie senza sorprese: LOI, due diligence, certificato fiscale art. 14, procedura sindacale e garanzie R&W.",
        "norme": ["Artt. 2555-2560 c.c.", "Art. 14 D.Lgs. 472/1997", "Art. 2112 c.c.", "Art. 47 L. 428/1990"],
        "intro": "Un'acquisizione aziendale sicura si costruisce prima del rogito: due diligence accurata, certificato fiscale liberatorio e garanzie contrattuali blindate.",
        "sezioni": [
            ("1. Asset Deal (cessione azienda) vs Share Deal (cessione quote)", "L'asset deal isola il perimetro dei beni ma attiva gli artt. 2560 c.c., 2112 c.c. e 14 D.Lgs. 472/97; lo share deal mantiene intatta la societa' ma trasferisce tutte le passivita' pregresse, richiedendo R&W ed escrow."),
            ("2. I tre pilastri anti-sorpresa nella cessione d'azienda", "Certificato carichi pendenti fiscali ex art. 14 D.Lgs. 472/97 (40 giorni), verifica puntuale del libro giornale (art. 2560 co. 2 c.c.) e procedura sindacale 25 giorni prima (art. 47 L. 428/90)."),
            ("3. Garanzie contrattuali, escrow e patto di non concorrenza", "Inserire sempre deposito a garanzia sul prezzo, indennizzi analitici, meccanismi chiari di earn-out e rispetto del divieto di concorrenza quinquennale (art. 2557 c.c.).")
        ],
        "checklist": [
            "Firmare NDA e Lettera d'Intenti (LOI) con esclusiva e condizioni sospensive.",
            "Svolgere due diligence legale, fiscale, lavoro, contratti e rischi 231.",
            "Richiedere il certificato carichi pendenti fiscali ex art. 14 D.Lgs. 472/97 almeno 40 giorni prima.",
            "Avviare la procedura sindacale ex art. 47 L. 428/90 almeno 25 giorni prima (se >15 dipendenti).",
            "Negoziare contratto definitivo (SPA/APA) con R&W, cap, escrow e patto di non concorrenza."
        ],
        "faqs": [
            ("Cosa rischia chi compra un'azienda senza il certificato art. 14 D.Lgs. 472/97?", "Risponde solidalmente (nei limiti del valore dell'azienda) dei debiti fiscali del venditore dell'anno in corso e dei due precedenti."),
            ("Il contratto di locazione commerciale passa automaticamente all'acquirente?", "Si', l'art. 36 L. 392/1978 consente di cedere il contratto di locazione insieme all'azienda senza consenso del locatore, dandogliene comunicazione.")
        ]
    },
    {
        "cod": "GSOC-24",
        "slug": "guida-concordato-minore-liquidazione-controllata-sotto-soglia",
        "pilastro": "sovraindebitamento-esdebitazione-imprenditore",
        "titolo": "Guida al Concordato Minore e alla Liquidazione Controllata per imprese sotto soglia",
        "seo_title": "Guida Concordato Minore e Liquidazione Controllata (CCII)",
        "desc": "Come scegliere lo strumento giusto di sovraindebitamento tra concordato minore (art. 74), liquidazione controllata (art. 268) e procedura familiare (art. 66).",
        "norme": ["Art. 66 CCII", "Art. 74 CCII", "Art. 268 CCII", "D.Lgs. 136/2024"],
        "intro": "Imprese minori, professionisti, ditte individuali e soci garanti hanno accesso a procedure snelle davanti al Tribunale tramite l'OCC per bloccare i pignoramenti e ristrutturare i debiti.",
        "sezioni": [
            ("1. Quando scegliere il Concordato Minore", "Quando l'attivita' e' ancora in esercizio e genera flussi per proseguire (continuita'), oppure c'e' finanza esterna apprezzabile di terzi/familiari."),
            ("2. Quando scegliere la Liquidazione Controllata", "Quando l'attivita' e' cessata o non e' piu' sostenibile: si liquidano i beni (o si mette a disposizione una quota di reddito eccedente il mantenimento per 3 anni) e poi scatta l'esdebitazione di diritto."),
            ("3. Procedura familiare unitaria (art. 66 CCII)", "I membri della stessa famiglia conviventi (o con indebitamento di origine comune, es. coniugi garanti) possono presentare un unico progetto risparmiando tempi e costi.")
        ],
        "checklist": [
            "Verificare il mancato superamento delle soglie di impresa minore (art. 2 CCII).",
            "Raccogliere estratti di ruolo AdER, Centrale Rischi, CRIF e elenco completo creditori.",
            "Presentare istanza di nomina Gestore all'OCC del Tribunale competente.",
            "Scegliere tra Concordato Minore, Liquidazione Controllata o Procedura Familiare.",
            "Richiedere subito la sospensione delle procedure esecutive in corso."
        ],
        "faqs": [
            ("Posso salvare la casa di abitazione nel concordato minore?", "Si', l'art. 75 co. 3 CCII consente di continuare a pagare regolarmente le rate del mutuo ipotecario sulla prima casa se in regola o previa autorizzazione."),
            ("Serve l'avvocato per accedere al sovraindebitamento?", "La presenza dell'avvocato e' fondamentale per costruire un ricorso inattaccabile, gestire le misure protettive e replicare alle opposizioni di banche e Fisco.")
        ]
    },
    {
        "cod": "GSOC-25",
        "slug": "guida-esdebitazione-ex-imprenditore-debitore-incapiente-ccii",
        "pilastro": "sovraindebitamento-esdebitazione-imprenditore",
        "titolo": "Guida all'Esdebitazione dell'ex imprenditore e del debitore incapiente (artt. 278-283 CCII)",
        "seo_title": "Guida Esdebitazione Art. 278-283 CCII: Come Azzerare i Debiti Residui",
        "desc": "Percorso legale completo per ottenere il decreto di esdebitazione (fresh start) dopo la liquidazione giudiziale, dopo la liquidazione controllata o a costo zero per il debitore incapiente.",
        "norme": ["Artt. 278-283 CCII", "D.Lgs. 136/2024"],
        "intro": "Il Codice della Crisi sancisce il diritto alla seconda opportunita' (fresh start): chi ha affrontato un dissesto senza frode puo' cancellare definitivamente i debiti residui.",
        "sezioni": [
            ("1. Esdebitazione nella liquidazione giudiziale e controllata (3 anni)", "Decorsi 3 anni dall'apertura (o alla chiusura se anteriore), il debitore meritevole ottiene l'inesigibilita' di tutti i debiti non soddisfatti, inclusi quelli fiscali e previdenziali."),
            ("2. Esdebitazione del debitore incapiente (art. 283 CCII)", "Riservata alla persona fisica meritevole che non puo' offrire alcuna utilita' ai creditori: cancella tutti i debiti a costo zero, con obbligo di comunicare eventuali sopravvenienze rilevanti per 3 anni (ridotti dal D.Lgs. 136/2024)."),
            ("3. Debiti esclusi e posizione dei coobbligati", "Restano esclusi solo obblighi di mantenimento/alimenti e debiti da risarcimento illecito extracontrattuale o sanzioni penali/amministrative; l'esdebitazione non libera i fideiussori terzi.")
        ],
        "checklist": [
            "Verificare l'assenza di condanne per bancarotta fraudolenta o atti in frode (art. 280 CCII).",
            "Documentare la collaborazione leale con gli organi della procedura (o con l'OCC).",
            "Per l'incapiente, calcolare esattamente la soglia reddituale ex art. 283 co. 2 CCII.",
            "Depositare l'istanza di esdebitazione al Tribunale e difendersi da eventuali reclami.",
            "Rispettare gli obblighi informativi post-decreto per evitare la revoca."
        ],
        "faqs": [
            ("L'esdebitazione cancella anche le cartelle di Agenzia Entrate Riscossione?", "Si', i debiti tributari e contributivi rientrano pienamente nell'effetto esdebitatorio."),
            ("Quante volte si puo' chiedere l'esdebitazione dell'incapiente?", "Una sola volta nella vita (art. 283 co. 1 CCII).")
        ]
    },
    {
        "cod": "GSOC-26",
        "slug": "guida-nullita-fideiussioni-abi-decadenza-1957-centrale-rischi",
        "pilastro": "finanziamenti-soci-garanzie-fideiussioni-banche",
        "titolo": "Guida alla nullita' delle fideiussioni omnibus ABI, decadenza art. 1957 c.c. e Centrale Rischi",
        "seo_title": "Guida Fideiussioni Nulle ABI, Art. 1957 c.c. e Centrale Rischi",
        "desc": "Come difendere i soci fideiussori da decreti ingiuntivi bancari e cessionari NPL, azionare la decadenza semestrale e cancellare segnalazioni illegittime in Centrale Rischi.",
        "norme": ["Art. 2 L. 287/1990", "Art. 1957 c.c.", "Art. 1956 c.c.", "Art. 700 c.p.c."],
        "intro": "Le fideiussioni personali dei soci rappresentano il principale punto di vulnerabilita' patrimoniale delle famiglie imprenditoriali: conoscerne i vizi consente spesso di liberare il garante.",
        "sezioni": [
            ("1. Verifica delle clausole 2, 6 e 8 dello schema ABI", "La presenza delle tre clausole anticoncorrenziali censurate da Banca d'Italia determina la nullita' parziale della deroga all'art. 1957 c.c. (Sezioni Unite n. 41994/2021)."),
            ("2. Decadenza della banca dopo 6 mesi (art. 1957 c.c.)", "Se la banca non ha promosso un'azione giudiziale entro 6 mesi dalla scadenza/revoca del debito principale, la fideiussione si estingue definitivamente."),
            ("3. Cancellazione urgente Centrale Rischi e difese accessorie", "Si abbinano sempre il controllo ex art. 1956 c.c., la verifica della legittimazione del cessionario NPL (art. 58 TUB) e il ricorso ex art. 700 c.p.c. contro segnalazioni a sofferenza illegittime.")
        ],
        "checklist": [
            "Recuperare copia integrale di tutte le fideiussioni firmate e delle lettere di revoca fidi.",
            "Confrontare il testo con le clausole 2, 6 e 8 dello schema ABI 2003.",
            "Calcolare se sono trascorsi piu' di 6 mesi senza azione giudiziale della banca.",
            "In caso di decreto ingiuntivo, proporre opposizione entro 40 giorni.",
            "Acquisire la visura Centrale Rischi e diffidare/agire ex art. 700 c.p.c. se illegittima."
        ],
        "faqs": [
            ("Basta una raccomandata della banca entro 6 mesi per evitare la decadenza ex art. 1957 c.c.?", "No: salvo patto valido contrario, occorre una vera istanza giudiziale (decreto ingiuntivo, citazione o insinuazione al passivo)."),
            ("La nullita' ABI si applica anche alle fideiussioni firmate dopo il 2005?", "Si', dimostrando l'applicazione uniforme e persistente dello schema anticoncorrenziale anche negli anni successivi.")
        ]
    }
]
