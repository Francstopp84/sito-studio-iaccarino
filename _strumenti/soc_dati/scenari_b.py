# -*- coding: utf-8 -*-
"""Scenari operativi e protocolli di difesa SOC-051 -> SOC-100 (Crisi 15, Concordato/Accordi 20, Liquidazione Giudiziale 15)."""

SCENARI_B = [
    # ═══════════════════ 3. CRISI & COMPOSIZIONE (continuazione 051-065) ═══════════════════
    {
        "cod": "SOC-051", "slug": "cessione-azienda-composizione-negoziata-senza-debiti-art-22",
        "cat": "crisi-composizione", "cat_lbl": "Crisi & Composizione", "pilastro": "crisi-impresa-composizione-negoziata-ccii",
        "titolo": "Cessione d'azienda in Composizione Negoziata senza accollo debiti (art. 22 CCII)",
        "seo_title": "Cessione Azienda in Composizione Negoziata Art. 22 CCII senza Debiti",
        "desc": "Come vendere l'azienda o un ramo d'azienda durante la Composizione Negoziata con autorizzazione del Tribunale e liberazione dell'acquirente dai debiti ex art. 2560 co. 2 c.c.",
        "keywords": ["cessione azienda composizione negoziata art 22", "deroga art 2560 cc ccii", "vendita ramo azienda crisi impresa"],
        "norme": ["Art. 22 co. 1 lett. d CCII", "Art. 2560 co. 2 c.c.", "Art. 2112 c.c."],
        "scenario": "Un investitore e' interessato ad acquistare l'azienda o un ramo operativo dell'impresa in crisi, ma rifiuta di esporsi alla responsabilita' solidale per i debiti pregressi risultanti dalla contabilita'.",
        "rischio": "Senza l'autorizzazione giudiziale ex art. 22 CCII, l'acquirente risponde solidalmente dei debiti aziendali ex art. 2560 co. 2 c.c. e l'operazione salta.",
        "protocollo": [
            "Strutturare un'offerta vincolante con perizia di stima del ramo d'azienda e rispetto del principio di competitivita' nella selezione dell'acquirente.",
            "Depositare ricorso al Tribunale ex art. 22 co. 1 lett. d CCII chiedendo l'autorizzazione al trasferimento in deroga all'art. 2560 co. 2 c.c.",
            "Acquisire il parere dell'Esperto sulla funzionalita' della cessione alla continuita' aziendale e alla migliore soddisfazione dei creditori.",
            "Gestire separatamente la consultazione sindacale e i debiti di lavoro ex art. 2112 c.c. (che restano esclusi dalla deroga automatica salvo accordo sindacale)."
        ],
        "prove": ["Offerta irrevocabile di acquisto e perizia di stima indipendente", "Documentazione della procedura competitiva di raccolta offerte", "Parere dell'Esperto e piano di destinazione del prezzo ai creditori", "Accordi sindacali per i dipendenti trasferiti"],
        "errori": ["Vendere l'azienda a parti correlate senza procedura competitiva ne' autorizzazione giudiziale (rischio bancarotta distrattiva)", "Credere che la deroga art. 2560 cancelli automaticamente anche i diritti dei lavoratori ex art. 2112 c.c.", "Omettere la valutazione dei debiti fiscali ex art. 14 D.Lgs. 472/97"]
    },
    {
        "cod": "SOC-052", "slug": "finanziamenti-prededucibili-composizione-negoziata-art-22",
        "cat": "crisi-composizione", "cat_lbl": "Crisi & Composizione", "pilastro": "crisi-impresa-composizione-negoziata-ccii",
        "titolo": "Finanziamenti prededucibili in Composizione Negoziata (art. 22 CCII): soci e banche",
        "seo_title": "Finanziamenti Prededucibili Composizione Negoziata Art. 22 CCII",
        "desc": "Come ottenere dal Tribunale l'autorizzazione a contrarre nuova finanza bancaria o dei soci in prededuzione per sostenere la liquidita' durante il risanamento.",
        "keywords": ["finanziamenti prededucibili art 22 ccii", "nuova finanza soci composizione negoziata", "prededuzione crisi impresa"],
        "norme": ["Art. 22 co. 1 lett. a-b CCII", "Art. 2467 c.c.", "Art. 6 CCII"],
        "scenario": "L'impresa in Composizione Negoziata necessita urgentemente di nuova liquidita' (da banche o dai soci stessi) per comprare materie prime e completare commesse redditizie.",
        "rischio": "Senza autorizzazione del Tribunale, il nuovo finanziamento dei soci sarebbe postergato (art. 2467 c.c.) e quello bancario rischierebbe di non avere tutela in caso di successiva liquidazione.",
        "protocollo": [
            "Dimostrare tramite piano di tesoreria e relazione dell'Esperto che la nuova finanza e' funzionale alla continuita' aziendale e alla migliore soddisfazione dei creditori.",
            "Chiedere al Tribunale l'autorizzazione ex art. 22 co. 1 lett. a o b CCII affinche' il credito goda della prededuzione anche in eventuale successiva procedura concorsuale.",
            "Disciplinare con precisione la destinazione vincolata delle somme erogate.",
            "Escludere l'applicazione della postergazione ex art. 2467 c.c. per i finanziamenti soci autorizzati."
        ],
        "prove": ["Budget di cassa con evidenza del fabbisogno di circolante", "Term sheet del finanziamento bancario o delibera di finanziamento soci", "Parere motivato dell'Esperto", "Ordinanza autorizzativa del Tribunale"],
        "errori": ["Erogare finanziamenti soci senza passare dal Tribunale perdendo la prededuzione", "Non dimostrare che la continuita' finanziata evita una distruzione di valore per i creditori", "Utilizzare la nuova finanza per pagare creditori anteriori non autorizzati"]
    },
    {
        "cod": "SOC-053", "slug": "transazione-fiscale-composizione-negoziata-art-23-correttivo-ter",
        "cat": "crisi-composizione", "cat_lbl": "Crisi & Composizione", "pilastro": "crisi-impresa-composizione-negoziata-ccii",
        "titolo": "Accordo transattivo con l'Agenzia delle Entrate in Composizione Negoziata (art. 23 co. 2-bis CCII)",
        "seo_title": "Transazione Fiscale in Composizione Negoziata Art. 23 co. 2-bis CCII",
        "desc": "La grande novita' del Correttivo-ter (D.Lgs. 136/2024): come proporre lo stralcio e la dilazione dei debiti tributari direttamente nella Composizione Negoziata con autorizzazione del Tribunale.",
        "keywords": ["transazione fiscale composizione negoziata", "art 23 comma 2 bis ccii", "stralcio debiti agenzia entrate correttivo ter"],
        "norme": ["Art. 23 co. 2-bis CCII", "D.Lgs. 136/2024", "Art. 25-bis CCII"],
        "scenario": "Un'impresa in Composizione Negoziata ha un debito fiscale pesante verso l'Agenzia delle Entrate e vuole proporre un pagamento parziale e/o dilazionato senza dover aprire un concordato preventivo.",
        "rischio": "Una proposta priva di relazione di convenienza comparativa rispetto alla liquidazione giudiziale viene respinta dall'Amministrazione Finanziaria.",
        "protocollo": [
            "Formulare una proposta di accordo transattivo ex art. 23 co. 2-bis CCII allegando la relazione di un professionista indipendente sulla convenienza rispetto alla liquidazione giudiziale.",
            "Acquisire la relazione dell'organo di controllo (o revisore) sulla completezza e veridicita' dei dati aziendali.",
            "Negoziare con la Direzione Regionale/Provinciale competente dell'Agenzia delle Entrate con il supporto dell'Esperto.",
            "Depositare l'accordo sottoscritto al Tribunale per l'autorizzazione all'esecuzione."
        ],
        "prove": ["Proposta transattiva fiscale con piano di pagamento", "Relazione del professionista indipendente sulla convenienza comparativa", "Relazione di veridicita' dei dati contabili", "Certificato unico debiti tributari aggiornato"],
        "errori": ["Includere nella proposta dell'art. 23 co. 2-bis tributi costituenti risorse proprie UE non falcidiabili se non nei limiti di legge", "Omettere l'attestazione di veridicita' dei dati", "Confondere la procedura con il cram-down giudiziale (che opera in ARD e concordato)"]
    },
    {
        "cod": "SOC-054", "slug": "concordato-semplificato-liquidatorio-art-25-sexies-ccii",
        "cat": "crisi-composizione", "cat_lbl": "Crisi & Composizione", "pilastro": "crisi-impresa-composizione-negoziata-ccii",
        "titolo": "Concordato semplificato per la liquidazione del patrimonio (art. 25-sexies CCII)",
        "seo_title": "Concordato Semplificato Art. 25-sexies CCII: Requisiti e 60 Giorni",
        "desc": "Quando le trattative in Composizione Negoziata falliscono nonostante la buona fede: accesso al concordato semplificato senza voto dei creditori entro 60 giorni dalla relazione finale.",
        "keywords": ["concordato semplificato art 25 sexies", "concordato senza voto creditori", "relazione finale esperto 60 giorni"],
        "norme": ["Art. 25-sexies CCII", "Art. 25-septies CCII", "D.Lgs. 136/2024"],
        "scenario": "La Composizione Negoziata si chiude senza accordo per l'indisponibilita' dei creditori, ma l'Esperto attesta nella relazione finale che le trattative si sono svolte secondo correttezza e buona fede.",
        "rischio": "Decorso il termine perentorio di 60 giorni dalla comunicazione della relazione finale dell'Esperto, si perde la possibilita' di accedere al concordato semplificato.",
        "protocollo": [
            "Verificare che la relazione finale dell'Esperto contenga la doppia attestazione positiva: trattative svolte secondo correttezza/buona fede e impraticabilita' delle soluzioni ex art. 23.",
            "Depositare entro 60 giorni il ricorso di concordato semplificato con proposta di cessione dei beni e piano di liquidazione (che assicuri un'utilita' a ciascun creditore e non arrechi pregiudizio rispetto alla liquidazione giudiziale).",
            "Difendere la proposta davanti al Tribunale in sede di omologazione contro eventuali opposizioni dei creditori (non e' previsto il voto).",
            "Eseguire la liquidazione tramite il liquidatore nominato dal Tribunale (anche su offerte gia' individuate ex art. 25-septies)."
        ],
        "prove": ["Relazione finale dell'Esperto con data certa di comunicazione", "Piano di liquidazione e perizie di stima dei beni", "Eventuale offerta irrevocabile di acquisto dell'azienda o dei cespiti", "Dimostrazione della convenienza rispetto alla liquidazione giudiziale"],
        "errori": ["Superare il termine perentorio di 60 giorni dalla relazione finale", "Condurre trattative meramente fittizie in Composizione Negoziata (il Tribunale dichiara l'inammissibilita')", "Non assicurare alcuna utilita' concreta a una classe di creditori"]
    },
    {
        "cod": "SOC-055", "slug": "misure-premiali-fiscali-composizione-negoziata-art-25-bis",
        "cat": "crisi-composizione", "cat_lbl": "Crisi & Composizione", "pilastro": "crisi-impresa-composizione-negoziata-ccii",
        "titolo": "Misure premiali fiscali nella Composizione Negoziata: interessi legali, sanzioni ridotte e 120 rate",
        "seo_title": "Misure Premiali Fiscali Art. 25-bis CCII: Sanzioni e Rateazione 120 Rate",
        "desc": "Come sfruttare gli sconti automatici su interessi e sanzioni tributarie e la rateazione straordinaria fino a 120 rate prevista dall'art. 25-bis CCII.",
        "keywords": ["misure premiali art 25 bis ccii", "rateazione 120 rate composizione negoziata", "riduzione sanzioni fiscali crisi"],
        "norme": ["Art. 25-bis CCII", "D.Lgs. 136/2024", "Art. 88 TUIR"],
        "scenario": "L'impresa ha avviato tempestivamente la Composizione Negoziata e vuole ridurre il peso di interessi, sanzioni tributarie e imposte sulle sopravvenienze attive da stralcio debiti.",
        "rischio": "Mancata fruizione di benefici fiscali decisivi per la tenuta del piano di cassa o decadenza dai benefici in caso di successiva liquidazione giudiziale.",
        "protocollo": [
            "Attivare la riduzione al tasso legale degli interessi sui debiti tributari dall'accettazione dell'Esperto fino alla chiusura.",
            "Richiedere la riduzione al minimo delle sanzioni tributarie e il dimezzamento delle sanzioni/interessi maturati prima dell'istanza in caso di esito positivo ex art. 23.",
            "Chiedere all'Agenzia delle Entrate il piano di rateazione fino a 72 rate (o fino a 120 rate in caso di comprovata grave situazione di difficolta') sulle somme non ancora iscritte a ruolo.",
            "Applicare la detassazione delle sopravvenienze attive da riduzione dei debiti (art. 88 co. 4-ter TUIR) previa pubblicazione del contratto/accordo nel Registro Imprese."
        ],
        "prove": ["Certificato di accettazione dell'Esperto e pubblicazione nel Registro Imprese", "Contratto o accordo concluso ex art. 23 CCII con relazione dell'Esperto", "Istanza di rateazione straordinaria ex art. 25-bis co. 4 CCII", "Prospetto fiscale delle sopravvenienze detassate"],
        "errori": ["Dimenticare di pubblicare il contratto ex art. 23 nel Registro Imprese (condizione per la detassazione sopravvenienze)", "Non calcolare la decadenza dalle premialita' se il piano fallisce", "Trascurare l'impatto fiscale dello stralcio debiti nel piano finanziario"]
    },
    {
        "cod": "SOC-056", "slug": "segnalazione-organo-controllo-interno-art-25-octies-ccii",
        "cat": "crisi-composizione", "cat_lbl": "Crisi & Composizione", "pilastro": "crisi-impresa-composizione-negoziata-ccii",
        "titolo": "Segnalazione di allerta dell'organo di controllo interno o revisore (art. 25-octies CCII)",
        "seo_title": "Segnalazione Organo di Controllo Art. 25-octies CCII: Risposta CdA",
        "desc": "Come deve reagire il CdA entro 30 giorni alla segnalazione scritta del collegio sindacale o del revisore legale (esteso dal Correttivo-ter D.Lgs. 136/2024) e come si tutelano i sindaci.",
        "keywords": ["segnalazione organo controllo art 25 octies", "risposta amministratori 30 giorni ccii", "revisore legale segnalazione crisi"],
        "norme": ["Art. 25-octies CCII", "D.Lgs. 136/2024", "Art. 2407 c.c."],
        "scenario": "Il collegio sindacale o il revisore legale trasmette via PEC all'organo amministrativo una segnalazione motivata sulla sussistenza dei presupposti per la Composizione Negoziata, assegnando un termine massimo di 30 giorni.",
        "rischio": "L'inerzia del CdA obbliga i sindaci a intensificare la vigilanza (fino alla denuncia ex art. 2409 c.c.) e costituisce prova grave contro gli amministratori; viceversa, la segnalazione tempestiva tutela i sindaci sulla responsabilita' ex art. 2407 c.c.",
        "protocollo": [
            "Rispondere per iscritto entro il termine assegnato (massimo 30 giorni) con una relazione analitica sulle soluzioni individuate e le iniziative gia' intraprese.",
            "Convocare un incontro congiunto tra CdA, collegio sindacale, revisore e advisor legale/finanziario.",
            "Se la crisi e' confermata, deliberare l'accesso alla Composizione Negoziata o a un piano di risanamento.",
            "Per i sindaci/revisori: conservare traccia certa della segnalazione e del monitoraggio successivo per beneficiare della valutazione di esenzione/attenuazione ex art. 25-octies co. 2 CCII."
        ],
        "prove": ["PEC di segnalazione ex art. 25-octies CCII", "Delibera del CdA e relazione di riscontro entro 30 giorni", "Verbali di verifica successiva dell'organo di controllo", "Piano di azione correttivo o istanza di accesso CCII"],
        "errori": ["Lasciare decorrere i 30 giorni senza una risposta scritta e documentata", "Considerare la segnalazione del sindaco un atto ostile anziche' un obbligo di legge", "Da parte del revisore/sindaco, tacere di fronte a perdite gravi perdendo la protezione dell'art. 25-octies co. 2"]
    },
    {
        "cod": "SOC-057", "slug": "sospensione-obblighi-ricapitalizzazione-perdite-art-20-ccii",
        "cat": "crisi-composizione", "cat_lbl": "Crisi & Composizione", "pilastro": "crisi-impresa-composizione-negoziata-ccii",
        "titolo": "Sospensione degli obblighi di ricapitalizzazione e scioglimento per perdite (art. 20 CCII)",
        "seo_title": "Sospensione Ricapitalizzazione Perdite Art. 20 CCII in Crisi",
        "desc": "Come congelare temporaneamente le cause di scioglimento per perdita del capitale sociale (art. 2484 n. 4 c.c.) durante le trattative di Composizione Negoziata.",
        "keywords": ["sospensione ricapitalizzazione art 20 ccii", "congelamento perdite capitale composizione negoziata", "art 2482 ter sospensione"],
        "norme": ["Art. 20 CCII", "Art. 2482-ter c.c.", "Art. 2484 co. 1 n. 4 c.c."],
        "scenario": "Durante la crisi, le perdite riducono il capitale sociale sotto il minimo legale e i soci non possono ancora ricapitalizzare finche' banche e creditori non accettano la ristrutturazione.",
        "rischio": "Senza la sospensione ex art. 20 CCII, gli amministratori dovrebbero mettere subito la societa' in liquidazione e fermare la gestione ordinaria.",
        "protocollo": [
            "Inserire nell'istanza di Composizione Negoziata (o in atto successivo) la dichiarazione espressa di avvalersi della sospensione ex art. 20 CCII.",
            "Iscrivere la dichiarazione nel Registro delle Imprese affinche' produca effetti fino alla conclusione delle trattative o all'archiviazione.",
            "Gestire comunque l'impresa in modo da non pregiudicare ingiustamente gli interessi dei creditori (art. 21 CCII).",
            "Al termine delle trattative, perfezionare l'aumento di capitale, la conversione debiti o il passaggio a uno strumento concorsuale (art. 89 CCII)."
        ],
        "prove": ["Dichiarazione ex art. 20 CCII pubblicata nel Registro delle Imprese", "Situazione patrimoniale aggiornata", "Verbali di gestione conforme all'art. 21 CCII", "Piano di ricapitalizzazione post-accordo"],
        "errori": ["Credere che la sospensione operi automaticamente senza dichiarazione e pubblicazione", "Compiere atti di straordinaria amministrazione senza avvisare l'Esperto", "Non ricapitalizzare ne' accedere a procedura concorsuale allo scadere della sospensione"]
    },
    {
        "cod": "SOC-058", "slug": "proroga-misure-protettive-fino-240-giorni-ccii",
        "cat": "crisi-composizione", "cat_lbl": "Crisi & Composizione", "pilastro": "crisi-impresa-composizione-negoziata-ccii",
        "titolo": "Proroga delle misure protettive fino a 240 giorni in Composizione Negoziata",
        "seo_title": "Proroga Misure Protettive fino a 240 Giorni Art. 19 co. 5 CCII",
        "desc": "Come ottenere dal Tribunale la proroga delle misure protettive oltre i primi 120 giorni fino al limite massimo di 240 giorni quando le trattative sono in fase avanzata.",
        "keywords": ["proroga misure protettive 240 giorni", "art 19 comma 5 ccii", "rinnovo protezione creditori"],
        "norme": ["Art. 19 co. 5 CCII", "Art. 17 co. 7 CCII"],
        "scenario": "I primi 120 giorni di misure protettive stanno per scadere, ma le trattative con banche, Agenzia delle Entrate o investitori richiedono altro tempo per formalizzare gli accordi.",
        "rischio": "La scadenza non prorogata delle misure riapre immediatamente pignoramenti e istanze di liquidazione giudiziale vanificando mesi di lavoro.",
        "protocollo": [
            "Depositare istanza di proroga prima della scadenza del termine originario (mai dopo).",
            "Ottenere il parere espressamente favorevole dell'Esperto sull'avanzamento concreto delle trattative e sulla necessita' della proroga.",
            "Allegare lettere di intenti, verbali di incontro con banche/Fisco e cronoprogramma serrato verso la chiusura.",
            "Coordinare la proroga delle misure protettive con l'eventuale proroga dell'incarico dell'Esperto (altri 180 giorni ex art. 17 co. 7 CCII)."
        ],
        "prove": ["Istanza tempestiva di proroga ex art. 19 co. 5 CCII", "Parere favorevole motivato dell'Esperto", "Verbali di trattativa, LOI o bozze avanzate di accordo", "Cronoprogramma al closing"],
        "errori": ["Chiedere la proroga dopo la scadenza del primo periodo", "Presentare un'istanza generica senza dimostrare progressi reali nelle trattative", "Superare il tetto massimo assoluto di 240 giorni"]
    },
    {
        "cod": "SOC-059", "slug": "piano-attestato-risanamento-art-56-ccii-esenzione-revocatoria",
        "cat": "crisi-composizione", "cat_lbl": "Crisi & Composizione", "pilastro": "crisi-impresa-composizione-negoziata-ccii",
        "titolo": "Piano Attestato di Risanamento (art. 56 CCII): ristrutturazione riservata ed esenzione revocatoria",
        "seo_title": "Piano Attestato di Risanamento Art. 56 CCII: Guida e Benefici",
        "desc": "Come ristrutturare il debito aziendale in totale riservatezza senza intervento del Tribunale, proteggendo pagamenti, garanzie e amministratori da revocatoria e bancarotta.",
        "keywords": ["piano attestato risanamento art 56 ccii", "esenzione revocatoria art 166", "esenzione bancarotta art 324 ccii"],
        "norme": ["Art. 56 CCII", "Art. 166 co. 3 lett. d CCII", "Art. 324 CCII"],
        "scenario": "Un'impresa in stato di crisi o insolvenza reversibile ha pochi creditori principali (soprattutto banche e fornitori chiave) disposti a rimodulare il debito senza pubblicita' negativa sul mercato.",
        "rischio": "Un accordo stragiudiziale privo di piano attestato con data certa e requisiti dell'art. 56 espone pagamenti e nuove garanzie a revocatoria e gli amministratori a rischi penali in caso di insuccesso.",
        "protocollo": [
            "Costruire un piano industriale e finanziario analitico con data certa contenente tutti gli elementi tassativi dell'art. 56 co. 2 CCII.",
            "Acquisire l'attestazione di un professionista indipendente sulla veridicita' dei dati aziendali e sulla fattibilita' economica del piano.",
            "Sottoscrivere accordi bilaterali o plurilaterali con banche e creditori coerenti con le previsioni del piano.",
            "Valutare la pubblicazione del piano nel Registro delle Imprese per ottenere anche la detassazione delle sopravvenienze attive (art. 88 TUIR)."
        ],
        "prove": ["Piano di risanamento con data certa conforme all'art. 56 CCII", "Attestazione di veridicita' e fattibilita' del professionista indipendente", "Accordi firmati con i creditori aderenti", "Monitoraggio periodico degli scostamenti in fase esecutiva"],
        "errori": ["Omettere la data certa sul piano e sugli atti esecutivi", "Scegliere un attestatore privo del requisito di indipendenza", "Compiere atti in esecuzione del piano con dolo o colpa grave (che fa cadere l'esenzione revocatoria)"]
    },
    {
        "cod": "SOC-060", "slug": "convenzione-moratoria-banche-art-62-ccii",
        "cat": "crisi-composizione", "cat_lbl": "Crisi & Composizione", "pilastro": "crisi-impresa-composizione-negoziata-ccii",
        "titolo": "Convenzione di moratoria estesa ai creditori dissenzienti (art. 62 CCII)",
        "seo_title": "Convenzione di Moratoria Art. 62 CCII: Standstill Banche e Creditori",
        "desc": "Come congelare scadenze e azioni esecutive di una categoria omogenea di creditori (es. banche o fornitori) estendendo la moratoria anche ai dissenzienti con il 75% di adesioni.",
        "keywords": ["convenzione moratoria art 62 ccii", "standstill bancario 75 per cento", "moratoria creditori dissenzienti"],
        "norme": ["Art. 62 CCII", "Art. 61 CCII"],
        "scenario": "La maggioranza delle banche (almeno il 75% dei crediti della categoria) accetta una moratoria provvisoria sulle rate dei mutui e sulle azioni esecutive, ma uno o due istituti minori rifiutano bloccando il risanamento.",
        "rischio": "L'iniziativa solitaria di una singola banca dissenziente puo' far crollare l'intero accordo di standstill.",
        "protocollo": [
            "Individuare correttamente la categoria omogenea di creditori e informare tutti i membri dell'avvio delle trattative in buona fede.",
            "Raggiungere l'adesione di almeno il 75% dei crediti della categoria e acquisire l'attestazione del professionista indipendente sulla convenienza rispetto alla liquidazione giudiziale.",
            "Notificare la convenzione e l'attestazione ai creditori non aderenti, i quali hanno 30 giorni per proporre opposizione davanti al Tribunale.",
            "Rispettare il divieto di imporre ai dissenzienti nuove prestazioni, concessione di affidamenti o erogazione di nuovi finanziamenti."
        ],
        "prove": ["Testo della convenzione di moratoria con adesioni >= 75%", "Prove dell'informativa tempestiva a tutti i creditori della categoria", "Relazione del professionista indipendente ex art. 62 co. 2 lett. d", "PEC di notifica ai creditori non aderenti"],
        "errori": ["Escludere alcuni creditori della categoria dalle trattative iniziali", "Pretendere di imporre nuove erogazioni di credito ai dissenzienti", "Dimenticare l'attestazione indipendente obbligatoria"]
    },
    {
        "cod": "SOC-061", "slug": "composizione-negoziata-gruppo-imprese-art-25-ccii",
        "cat": "crisi-composizione", "cat_lbl": "Crisi & Composizione", "pilastro": "crisi-impresa-composizione-negoziata-ccii",
        "titolo": "Composizione negoziata unitaria di gruppo di imprese (art. 25 CCII)",
        "seo_title": "Composizione Negoziata di Gruppo Art. 25 CCII: Gestione Unitaria",
        "desc": "Come gestire la crisi di piu' societa' appartenenti allo stesso gruppo con un unico Esperto, misure protettive coordinate e finanziamenti infragruppo tutelati.",
        "keywords": ["composizione negoziata di gruppo art 25", "crisi gruppo imprese ccii", "unico esperto gruppo societario"],
        "norme": ["Art. 25 CCII", "Art. 2 co. 1 lett. h CCII", "Art. 284 CCII"],
        "scenario": "Un gruppo familiare o industriale composto da holding e piu' S.r.l. operative entra in tensione finanziaria con garanzie incrociate e crediti/debiti infragruppo.",
        "rischio": "Gestire ogni societa' separatamente provoca iniziative scoordinate dei creditori e l'effetto domino da garanzie incrociate.",
        "protocollo": [
            "Presentare istanza unitaria presso la CCIAA competente per la societa' che esercita direzione e coordinamento (o con maggiore esposizione debitoria).",
            "Chiedere la nomina di un unico Esperto per tutto il gruppo e misure protettive coordinate davanti al medesimo Tribunale.",
            "Ricostruire analiticamente i rapporti di debito/credito e le fideiussioni infragruppo per evitare pregiudizi ai creditori delle singole societa'.",
            "Valutare lo sbocco in un accordo unitario di gruppo o in soluzioni differenziate per ciascuna societa' (es. continuita' per le sane, liquidazione per le decotte)."
        ],
        "prove": ["Organigramma del gruppo e legami partecipativi/direzione", "Bilanci consolidati e bilanci delle singole societa'", "Mappa delle garanzie incrociate e dei saldi infragruppo", "Piano unitario o coordinato di gruppo"],
        "errori": ["Mescolare gli attivi e i passivi delle singole societa' violando l'autonomia delle masse", "Dimenticare di estendere le misure protettive alle societa' garanti", "Non documentare i vantaggi compensativi nelle operazioni infragruppo"]
    },
    {
        "cod": "SOC-062", "slug": "rinegoziazione-contratti-onerosi-composizione-negoziata",
        "cat": "crisi-composizione", "cat_lbl": "Crisi & Composizione", "pilastro": "crisi-impresa-composizione-negoziata-ccii",
        "titolo": "Rinegoziazione dei contratti divenuti eccessivamente onerosi in Composizione Negoziata",
        "seo_title": "Rinegoziazione Contratti in Composizione Negoziata Art. 10 CCII",
        "desc": "Come rinegoziare canoni di locazione, forniture e appalti divenuti squilibrati avvalendosi dell'invito dell'Esperto e dei doveri di buona fede delle controparti.",
        "keywords": ["rinegoziazione contratti composizione negoziata", "art 10 ccii rideterminazione contratti", "locazione commerciale crisi impresa"],
        "norme": ["Art. 10 co. 2 CCII", "Art. 16 CCII", "Art. 1375 c.c."],
        "scenario": "Contratti di lunga durata (locazioni industriali/commerciali, leasing, forniture energetiche o appalti a prezzo fisso) sono divenuti insostenibili e impediscono il riequilibrio economico.",
        "rischio": "La prosecuzione a condizioni antieconomiche brucia cassa ogni mese e rende impossibile attestare la sostenibilita' del piano.",
        "protocollo": [
            "Individuare i contratti squilibrati e quantificare con precisione il margine negativo generato.",
            "Chiedere all'Esperto di invitare formalmente le controparti alla rinegoziazione secondo buona fede ex art. 10 co. 2 CCII.",
            "Formulare proposte realistiche (riduzione temporanea canone, dilazione arretrati, rimodulazione prezzi) dimostrando che l'alternativa sarebbe lo scioglimento in sede concorsuale.",
            "In caso di blocco, valutare il passaggio al concordato preventivo con facolta' di scioglimento/sospensione ex art. 97 CCII."
        ],
        "prove": ["Contratti originali e conteggio dello squilibrio economico", "Invito formale dell'Esperto alla rinegoziazione", "Proposta scritta e comparazione con scenario liquidatorio", "Verbali degli incontri con le controparti"],
        "errori": ["Sospendere unilateralmente i pagamenti senza ne' trattativa ne' misure protettive", "Non coinvolgere l'Esperto come mediatore istituzionale", "Trascurare il rischio di sfratto se non coperto da misure protettive/cautelari"]
    },
    {
        "cod": "SOC-063", "slug": "segnalazione-banche-intermediari-organo-controllo-art-25-decies",
        "cat": "crisi-composizione", "cat_lbl": "Crisi & Composizione", "pilastro": "crisi-impresa-composizione-negoziata-ccii",
        "titolo": "Segnalazione di banche e intermediari all'organo di controllo su variazione fidi (art. 25-decies CCII)",
        "seo_title": "Segnalazione Banche Art. 25-decies CCII: Revoca o Riduzione Fidi",
        "desc": "Obbligo delle banche di avvisare l'organo di controllo quando riducono o revocano affidamenti e come gestire subito la comunicazione per evitare escalation della crisi.",
        "keywords": ["segnalazione banche art 25 decies ccii", "riduzione affidamenti organo controllo", "revoca fidi collegio sindacale"],
        "norme": ["Art. 25-decies CCII", "Art. 25-octies CCII"],
        "scenario": "Una banca comunica contestualmente all'impresa e al collegio sindacale la variazione, revisione o revoca degli affidamenti ai sensi dell'art. 25-decies CCII.",
        "rischio": "La comunicazione innesca verifiche stringenti dell'organo di controllo e puo' anticipare segnalazioni a sofferenza o reazioni a catena delle altre banche.",
        "protocollo": [
            "Verificare subito la legittimita' contrattuale e il preavviso della riduzione/revoca del fido.",
            "Fornire all'organo di controllo un aggiornamento immediato della posizione finanziaria netta e del piano di tesoreria a 6 mesi.",
            "Aprire un tavolo di confronto con l'istituto bancario per concordare un rientro sostenibile o il mantenimento delle linee autoliquidanti.",
            "Se la tensione coinvolge piu' banche, attivare tempestivamente la Composizione Negoziata (art. 12 CCII)."
        ],
        "prove": ["Comunicazione bancaria ex art. 25-decies CCII", "Contratti di affidamento e Centrale Rischi aggiornata", "Prospetto di tesoreria e linee residue presso altri istituti", "Verbale di confronto con l'organo di controllo"],
        "errori": ["Nascondere l'entita' della tensione finanziaria al collegio sindacale", "Attendere lo sconfinamento prolungato che porta a segnalazione a sofferenza", "Non contestare una revoca brutale priva di giusta causa"]
    },
    {
        "cod": "SOC-064", "slug": "opposizione-creditori-misure-protettive-difesa-impresa",
        "cat": "crisi-composizione", "cat_lbl": "Crisi & Composizione", "pilastro": "crisi-impresa-composizione-negoziata-ccii",
        "titolo": "Difesa dell'impresa contro richieste di revoca o abbreviazione delle misure protettive",
        "seo_title": "Difesa da Revoca Misure Protettive Art. 19 co. 6 CCII",
        "desc": "Come resistere in Tribunale quando un creditore chiede la revoca o la riduzione della durata delle misure protettive durante la Composizione Negoziata.",
        "keywords": ["revoca misure protettive art 19 ccii", "opposizione creditore composizione negoziata", "abbreviazione misure protettive"],
        "norme": ["Art. 19 co. 6 CCII", "Art. 18 CCII"],
        "scenario": "Un creditore (spesso una banca o un fornitore munito di titolo esecutivo) chiede al Tribunale di revocare o abbreviare le misure protettive sostenendo che le trattative sono dilatorie.",
        "rischio": "La revoca anticipata riattiva immediatamente pignoramenti e aste facendo fallire il risanamento.",
        "protocollo": [
            "Dimostrare con verbali e corrispondenza che le trattative sono reali, attive e non meramente dilatorie.",
            "Produrre il parere aggiornato dell'Esperto che conferma la tenuta del percorso di risanamento e l'assenza di pregiudizio sproporzionato.",
            "Proporre, se utile, misure protettive mirate escludendo beni non strategici o offrendo garanzie informative periodiche.",
            "Contestare eventuali condotte ostruzionistiche del creditore istante contrarie al dovere di collaborazione ex art. 16 CCII."
        ],
        "prove": ["Istanza di revoca del creditore", "Verbali degli incontri di trattativa con l'Esperto e i creditori", "Relazione aggiornata sull'andamento corrente di cassa (nessun aggravamento del passivo)", "Parere favorevole dell'Esperto"],
        "errori": ["Lasciare trascorrere settimane senza convocare incontri con i creditori", "Generare nuove perdite correnti non coperte durante il periodo di protezione", "Non depositare memoria difensiva tempestiva prima dell'udienza"]
    },
    {
        "cod": "SOC-065", "slug": "gestione-impresa-pendente-composizione-negoziata-art-21",
        "cat": "crisi-composizione", "cat_lbl": "Crisi & Composizione", "pilastro": "crisi-impresa-composizione-negoziata-ccii",
        "titolo": "Atti di straordinaria amministrazione e gestione dell'impresa in Composizione Negoziata (art. 21 CCII)",
        "seo_title": "Gestione Impresa Art. 21 CCII: Atti Straordinari e Dissenso Esperto",
        "desc": "Limiti e doveri degli amministratori durante la Composizione Negoziata: informativa preventiva all'Esperto, dissenso iscritto al Registro Imprese e tutela da responsabilita'.",
        "keywords": ["gestione impresa art 21 ccii", "atti straordinaria amministrazione esperto", "dissenso esperto composizione negoziata"],
        "norme": ["Art. 21 CCII", "Art. 24 CCII"],
        "scenario": "Durante la Composizione Negoziata l'impresa deve compiere un atto di straordinaria amministrazione o un pagamento non coerente con le trattative.",
        "rischio": "Il compimento dell'atto senza informativa preventiva o contro il dissenso iscritto dell'Esperto elimina la protezione da revocatoria e bancarotta (art. 24 CCII) e puo' portare alla revoca delle misure protettive.",
        "protocollo": [
            "Comunicare preventivamente per iscritto all'Esperto ogni atto di straordinaria amministrazione o pagamento non ordinario.",
            "Valutare con l'Esperto eventuali modifiche dell'operazione per renderla pienamente coerente con il risanamento.",
            "Evitare categoricamente pagamenti preferenziali a creditori strategici senza coerenza con il piano e senza parere dell'Esperto.",
            "Conservare la tracciatura documentale della coerenza degli atti con la continuita' per godere della stabilita' ex art. 24 CCII."
        ],
        "prove": ["Informativa preventiva scritta inviata all'Esperto", "Valutazione positiva o mancato dissenso dell'Esperto", "Delibera del CdA motivata sull'utilita' dell'atto", "Rendicontazione flussi di cassa"],
        "errori": ["Compiere cessioni di beni o pagamenti anomali all'insaputa dell'Esperto", "Ignorare il dissenso dell'Esperto iscritto nel Registro Imprese", "Sottovalutare l'art. 24 co. 3 CCII che tutela gli atti coerenti solo se compiuti senza dissenso"]
    },

    # ═══════════════════ 4. CONCORDATO & ACCORDI (066-085) ═══════════════════
    {
        "cod": "SOC-066", "slug": "concordato-preventivo-continuita-diretta-art-84-ccii",
        "cat": "concordato-accordi", "cat_lbl": "Concordato & Accordi", "pilastro": "concordato-preventivo-accordi-ristrutturazione",
        "titolo": "Concordato preventivo in continuita' aziendale diretta (art. 84 CCII)",
        "seo_title": "Concordato Preventivo in Continuita' Diretta Art. 84 CCII",
        "desc": "Come ristrutturare l'impresa mantenendo la gestione diretta dell'azienda, senza soglia minima fissa per i chirografari e con la regola della priorita' relativa sul surplus.",
        "keywords": ["concordato preventivo continuita diretta", "art 84 ccii regola priorita relativa", "salvataggio azienda concordato"],
        "norme": ["Art. 84 CCII", "Art. 87 CCII", "Art. 112 CCII"],
        "scenario": "Un'impresa operativa con commesse, marchio e know-how validi e' schiacciata dai debiti storici ma genera margini positivi nella gestione corrente.",
        "rischio": "La liquidazione giudiziale distruggerebbe l'avviamento e i posti di lavoro pagando briciole ai creditori; un piano di continuita' mal costruito rischia pero' la revoca dell'ammissione.",
        "protocollo": [
            "Costruire un piano industriale e finanziario sostenibile che dimostri la capacita' dell'impresa di generare flussi per soddisfare i creditori in misura non inferiore alla liquidazione giudiziale.",
            "Suddividere obbligatoriamente i creditori in classi (nel concordato in continuita' il classamento e' sempre obbligatorio ex art. 85 co. 3 CCII).",
            "Distribuire il valore di liquidazione secondo la priorita' assoluta (APR) e il surplus da continuita' secondo la regola piu' flessibile della priorita' relativa (RPR).",
            "Acquisire l'attestazione del professionista indipendente su veridicita', fattibilita' e convenienza."
        ],
        "prove": ["Piano industriale-finanziario pluriennale e stima del valore di liquidazione", "Attestazione di professionista indipendente", "Prospetto di formazione classi e trattamento creditori", "Contratti e portafoglio ordini a supporto della continuita'"],
        "errori": ["Non suddividere i creditori in classi (obbligatorio in continuita')", "Sopravvalutare i flussi futuri senza stress-test", "Non tutelare i crediti dei lavoratori (che vanno soddisfatti integralmente entro 30 giorni dall'omologa per le retribuzioni ex art. 84 co. 8)"]
    },
    {
        "cod": "SOC-067", "slug": "concordato-preventivo-continuita-indiretta-affitto-cessione",
        "cat": "concordato-accordi", "cat_lbl": "Concordato & Accordi", "pilastro": "concordato-preventivo-accordi-ristrutturazione",
        "titolo": "Concordato preventivo in continuita' indiretta tramite affitto o cessione d'azienda",
        "seo_title": "Concordato in Continuita' Indiretta: Affitto e Cessione Azienda",
        "desc": "Come salvare l'azienda e i lavoratori trasferendo l'attivita' a una NewCo o a un terzo investitore tramite affitto ponte e cessione competitiva nel concordato preventivo.",
        "keywords": ["concordato continuita indiretta", "affitto azienda concordato preventivo", "newco concordato ccii"],
        "norme": ["Art. 84 co. 2 CCII", "Art. 91 CCII", "Art. 2112 c.c."],
        "scenario": "La societa' storica non puo' piu' operare direttamente per perdita di credibilita' bancaria o DURC irregolare, ma l'azienda puo' proseguire tramite un affittuario/acquirente.",
        "rischio": "Offerte chiuse senza procedura competitiva (art. 91 CCII) o canoni non congrui portano all'inammissibilita' o a contestazioni penali.",
        "protocollo": [
            "Strutturare un contratto di affitto d'azienda a canone di mercato periziato, accompagnato da offerta irrevocabile di acquisto cauzionata.",
            "Prevedere espressamente nel piano la procedura competitiva di gara ex art. 91 CCII per massimizzare il realizzo.",
            "Dimostrare la tutela, anche parziale, dei posti di lavoro e l'assenza di pregiudizio per i creditori rispetto alla liquidazione giudiziale.",
            "Gestire in modo trasparente l'eventuale partecipazione di parti correlate con rigorosa disclosure al commissario e al Tribunale."
        ],
        "prove": ["Contratto di affitto d'azienda e perizia di congruita' del canone e del prezzo", "Offerta irrevocabile di acquisto con fideiussione o deposito cauzionale", "Piano concordatario e attestazione indipendente", "Accordi sindacali per il mantenimento dell'occupazione"],
        "errori": ["Trasferire l'azienda a una NewCo dei soci a prezzo vile senza gara competitiva", "Non assicurare garanzie solide sull'adempimento dell'acquirente", "Trascurare il trattamento dei crediti da TFR e dei lavoratori"]
    },
    {
        "cod": "SOC-068", "slug": "concordato-preventivo-liquidatorio-soglia-20-finanza-esterna",
        "cat": "concordato-accordi", "cat_lbl": "Concordato & Accordi", "pilastro": "concordato-preventivo-accordi-ristrutturazione",
        "titolo": "Concordato preventivo liquidatorio: soglia minima del 20% e apporto di risorse esterne (10%)",
        "seo_title": "Concordato Preventivo Liquidatorio Art. 84 co. 4 CCII: Soglie 20% e 10%",
        "desc": "Requisiti rigorosi del concordato liquidatorio nel CCII: apporto esterno che incrementa l'attivo di almeno il 10% e soddisfacimento minimo del 20% dei creditori chirografari.",
        "keywords": ["concordato preventivo liquidatorio 20 per cento", "risorse esterne 10 per cento ccii", "art 84 comma 4 ccii"],
        "norme": ["Art. 84 co. 4 CCII", "Art. 114 CCII"],
        "scenario": "L'attivita' aziendale non e' piu' proseguibile, ma i soci o terzi sono disposti ad apportare risorse esterne per chiudere ordinatamente i debiti evitando la liquidazione giudiziale.",
        "rischio": "Senza l'apporto esterno minimo del 10% dell'attivo disponibile e senza il pagamento di almeno il 20% ai chirografari, il concordato liquidatorio e' inammissibile.",
        "protocollo": [
            "Far stimare analiticamente il valore di liquidazione dell'attivo disponibile al momento della domanda.",
            "Reperire risorse esterne certe e vincolate (finanza soci, terzi, rinuncia crediti o beni personali) che incrementino l'attivo di almeno il 10%.",
            "Verificare che la distribuzione delle risorse esterne (libere dal vincolo della priorita' assoluta) consenta di raggiungere almeno il 20% ai chirografari.",
            "In alternativa, valutare se ricorrono i presupposti del concordato semplificato (art. 25-sexies) che non ha tali soglie."
        ],
        "prove": ["Perizie di stima di immobili, macchinari e crediti", "Impegno irrevocabile e garantito all'apporto di finanza esterna", "Attestazione del professionista indipendente", "Prospetto di riparto che certifica la soglia >= 20%"],
        "errori": ["Confondere la finanza esterna con proventi derivanti da beni della societa' stessa", "Presentare impegni di finanza esterna privi di fideiussione o deposito vincolato", "Sottostimare le spese di procedura e i crediti in prededuzione"]
    },
    {
        "cod": "SOC-069", "slug": "domanda-concordato-con-riserva-in-bianco-art-44-ccii",
        "cat": "concordato-accordi", "cat_lbl": "Concordato & Accordi", "pilastro": "concordato-preventivo-accordi-ristrutturazione",
        "titolo": "Domanda di accesso con riserva (ex concordato in bianco) art. 44 CCII",
        "seo_title": "Domanda con Riserva Art. 44 CCII: Termini 30-60 Giorni e Protezione",
        "desc": "Come depositare la domanda prenotativa ex art. 44 CCII per ottenere tempo (30-60 giorni, prorogabili di 60) e misure protettive prima di depositare piano, proposta e attestazione.",
        "keywords": ["domanda con riserva art 44 ccii", "concordato in bianco ccii", "termine deposito piano concordato"],
        "norme": ["Art. 44 CCII", "Art. 54 CCII", "Art. 46 CCII"],
        "scenario": "Un'istanza di liquidazione giudiziale o un pignoramento imminente non lasciano il tempo materiale per completare subito il piano attestato di concordato o di accordo di ristrutturazione.",
        "rischio": "La domanda con riserva senza una strategia gia' abbozzata porta al rigetto della proroga e alla declaratoria di liquidazione giudiziale.",
        "protocollo": [
            "Depositare il ricorso ex art. 44 CCII con bilanci degli ultimi tre esercizi, elenco nominativo dei creditori e richiesta espressa di misure protettive (art. 54 co. 2 CCII).",
            "Rispettare scrupolosamente gli obblighi informativi periodici (almeno mensili) fissati dal Tribunale e collaborare con il commissario giudiziale nominato.",
            "Chiedere autorizzazione preventiva al Tribunale per ogni atto urgente di straordinaria amministrazione (art. 46 CCII).",
            "Entro il termine (30-60 giorni, prorogabili fino a ulteriori 60 giorni se non pende istanza di liquidazione giudiziale o per giustificati motivi), depositare il piano definitivo (concordato, ARD o PRO)."
        ],
        "prove": ["Bilanci ultimi tre esercizi e situazione economico-patrimoniale", "Elenco integrale creditori e relativi importi", "Relazioni informative mensili al Tribunale e al commissario", "Istanza di conferma misure protettive ex art. 55 CCII"],
        "errori": ["Pagare crediti anteriori senza autorizzazione del Tribunale durante la riserva", "Non versare il fondo spese fissato dal giudice nel decreto di concessione termini", "Arrivare a ridosso della scadenza senza aver individuato l'attestatore"]
    },
    {
        "cod": "SOC-070", "slug": "accordi-ristrutturazione-debiti-art-57-ccii-60-percento",
        "cat": "concordato-accordi", "cat_lbl": "Concordato & Accordi", "pilastro": "concordato-preventivo-accordi-ristrutturazione",
        "titolo": "Accordi di Ristrutturazione dei Debiti (ARD) ex art. 57 CCII con il 60% dei creditori",
        "seo_title": "Accordi di Ristrutturazione Debiti Art. 57 CCII: Omologa e 60%",
        "desc": "Come omologare un accordo negoziato con almeno il 60% dei crediti, pagando integralmente gli estranei entro 120 giorni e beneficiando di misure protettive e transazione fiscale.",
        "keywords": ["accordi ristrutturazione debiti art 57 ccii", "omologazione ard 60 per cento", "pagamento creditori estranei 120 giorni"],
        "norme": ["Art. 57 CCII", "Art. 48 CCII", "Art. 63 CCII"],
        "scenario": "L'impresa riesce a trovare un accordo di stralcio e dilazione con i principali creditori (banche, Fisco, fornitori maggiori) che rappresentano almeno il 60% del passivo complessivo.",
        "rischio": "Se il piano non dimostra la capacita' di pagare integralmente i creditori estranei entro 120 giorni dall'omologazione (o dalla scadenza), il Tribunale nega l'omologa.",
        "protocollo": [
            "Raccogliere le adesioni scritte (con firma autenticata o PEC/atto notarile) dei creditori pari ad almeno il 60% dei crediti totali.",
            "Far attestare dal professionista indipendente la veridicita' dei dati e l'idoneita' dell'accordo ad assicurare il pagamento integrale dei creditori estranei nei 120 giorni.",
            "Pubblicare l'accordo nel Registro delle Imprese e depositare ricorso di omologazione ex art. 48 CCII.",
            "Valutare l'abbinamento con la transazione fiscale ex art. 63 CCII per includere Agenzia delle Entrate e INPS."
        ],
        "prove": ["Accordi sottoscritti pari almeno al 60% del passivo", "Piano economico-finanziario con copertura integrale degli estranei a 120 giorni", "Attestazione indipendente ex art. 57 co. 4 CCII", "Pubblicazione nel Registro Imprese"],
        "errori": ["Sottostimare la massa dei creditori estranei che vanno pagati al 100%", "Non attivare le misure protettive durante le trattative ex art. 54 co. 3 CCII", "Dimenticare le modifiche sostanziali del piano in corso di esecuzione (art. 58 CCII)"]
    },
    {
        "cod": "SOC-071", "slug": "accordi-ristrutturazione-agevolati-art-60-ccii-30-percento",
        "cat": "concordato-accordi", "cat_lbl": "Concordato & Accordi", "pilastro": "concordato-preventivo-accordi-ristrutturazione",
        "titolo": "Accordi di ristrutturazione agevolati al 30% (art. 60 CCII)",
        "seo_title": "Accordi Ristrutturazione Agevolati Art. 60 CCII: Soglia 30%",
        "desc": "Quando e' sufficiente l'adesione del 30% dei crediti per omologare un accordo di ristrutturazione senza moratoria sugli estranei ne' misure protettive.",
        "keywords": ["accordi ristrutturazione agevolati art 60", "ard 30 per cento ccii", "ristrutturazione debiti senza moratoria"],
        "norme": ["Art. 60 CCII", "Art. 57 CCII"],
        "scenario": "Un'impresa ha un debito concentrato su pochi creditori (almeno il 30%) con cui ha gia' trovato un'intesa di stralcio/riscadenzamento ed e' in grado di pagare regolarmente tutti gli altri creditori a scadenza.",
        "rischio": "Rinunciare alla moratoria dei 120 giorni e alle misure protettive impone una liquidita' corrente impeccabile verso i creditori estranei.",
        "protocollo": [
            "Verificare il raggiungimento della soglia ridotta del 30% dei crediti totali.",
            "Rinunciare espressamente sia alla moratoria di 120 giorni per i creditori estranei sia alla richiesta di misure protettive temporanee.",
            "Ottenere l'attestazione del professionista indipendente sulla piena sostenibilita' dei pagamenti regolari agli estranei.",
            "Depositare il ricorso di omologazione in Tribunale beneficiando della protezione da revocatoria e della detassazione sopravvenienze."
        ],
        "prove": ["Accordi firmati con almeno il 30% dei creditori", "Piano di tesoreria che prova il pagamento puntuale di tutti gli estranei", "Attestazione indipendente ex art. 57 e 60 CCII", "Dichiarazione di rinuncia a moratoria e misure protettive"],
        "errori": ["Chiedere misure protettive (fa perdere l'accesso alla soglia agevolata del 30%)", "Avere creditori estranei gia' scaduti e impagabili subito", "Sottovalutare il rischio di opposizioni all'omologa"]
    },
    {
        "cod": "SOC-072", "slug": "accordi-ristrutturazione-efficacia-estesa-art-61-ccii",
        "cat": "concordato-accordi", "cat_lbl": "Concordato & Accordi", "pilastro": "concordato-preventivo-accordi-ristrutturazione",
        "titolo": "Accordi di ristrutturazione ad efficacia estesa (art. 61 CCII) anche ai creditori dissenzienti",
        "seo_title": "Accordi Efficacia Estesa Art. 61 CCII: Vincolare i Dissenzienti col 75%",
        "desc": "Come estendere gli effetti dell'accordo di ristrutturazione a banche o fornitori dissenzienti appartenenti alla stessa categoria omogenea quando aderisce il 75%.",
        "keywords": ["accordi efficacia estesa art 61 ccii", "estensione accordo creditori dissenzienti 75", "ristrutturazione banche ccii"],
        "norme": ["Art. 61 CCII", "Art. 57 CCII", "D.Lgs. 136/2024"],
        "scenario": "Nella ristrutturazione in continuita' aziendale, il 75% delle banche (o di una categoria omogenea di fornitori) firma l'accordo, ma una minoranza riottosa pretende il pagamento integrale.",
        "rischio": "La minoranza potrebbe far saltare l'accordo se non viene vincolata legalmente tramite il meccanismo dell'art. 61 CCII.",
        "protocollo": [
            "Formare categorie omogenee per posizione giuridica e interessi economici e informare tutti i creditori dell'avvio delle trattative.",
            "Ottenere l'adesione di almeno il 75% dei crediti in ciascuna categoria a cui si vuole estendere l'accordo (e il 60% complessivo).",
            "Dimostrare nell'attestazione che l'accordo ha carattere non liquidatorio (salvo il caso di debiti almeno al 50% verso banche/intermediari ex art. 61 co. 5) e che i dissenzienti ricevono non meno della liquidazione giudiziale.",
            "Notificare l'accordo e l'attestazione ai dissenzienti (che possono opporsi entro 30 giorni) e chiedere l'omologazione estesa al Tribunale."
        ],
        "prove": ["Informativa di avvio trattative a tutti i creditori della categoria", "Adesioni >= 75% nella categoria e >= 60% totale", "Attestazione di convenienza comparativa rispetto alla liquidazione giudiziale", "Notifiche PEC ai dissenzienti"],
        "errori": ["Non invitare alle trattative i creditori che si prevedono dissenzienti (vizio insanabile)", "Imporre ai dissenzienti nuovi finanziamenti o concessione di nuovi fidi", "Errata composizione delle categorie omogenee"]
    },
    {
        "cod": "SOC-073", "slug": "transazione-fiscale-cram-down-agenzia-entrate-inps-artt-63-88",
        "cat": "concordato-accordi", "cat_lbl": "Concordato & Accordi", "pilastro": "concordato-preventivo-accordi-ristrutturazione",
        "titolo": "Transazione fiscale e cram-down forzoso contro Agenzia delle Entrate e INPS (artt. 63 e 88 CCII)",
        "seo_title": "Transazione Fiscale e Cram-Down Fiscale Art. 63 e 88 CCII",
        "desc": "Come stralciare IVA, IRES, IRAP e contributi INPS negli accordi di ristrutturazione e nel concordato preventivo, ottenendo l'omologazione anche senza il consenso del Fisco.",
        "keywords": ["transazione fiscale art 63 ccii", "cram down fiscale inps art 88", "stralcio debiti agenzia entrate concordato"],
        "norme": ["Art. 63 CCII", "Art. 88 CCII", "D.Lgs. 136/2024"],
        "scenario": "Il debito verso Agenzia delle Entrate e INPS rappresenta la quota prevalente del passivo e gli enti pubblici rigettano la proposta di stralcio o non rispondono nei termini.",
        "rischio": "Senza la corretta applicazione dei requisiti rafforzati dal Correttivo-ter D.Lgs. 136/2024, il Tribunale non puo' pronunciare il cram-down fiscale.",
        "protocollo": [
            "Verificare le soglie e le condizioni aggiornate per il cram-down negli ARD (art. 63: adesione non liquidatoria, convenienza comparativa, soglie di soddisfacimento minimo 50% o 60% a seconda del peso degli altri creditori, assenza di precedenti inadempimenti ostativi) e nel concordato preventivo (art. 88 e 112).",
            "Far redigere una perizia di convenienza comparativa inattaccabile rispetto all'alternativa della liquidazione giudiziale.",
            "Depositare la proposta completa di tutta la documentazione fiscale/previdenziale agli uffici competenti rispettando i termini di legge (90 giorni per la risposta in ARD).",
            "In caso di dissenso o silenzio ingiustificato, chiedere formalmente al Tribunale l'omologazione forzosa (cram-down)."
        ],
        "prove": ["Proposta di transazione fiscale e previdenziale completa", "Relazione del professionista indipendente sulla convenienza comparativa", "Certificati unici debiti AdE/AdER/INPS", "Prove della convenienza e della determinanza del voto degli enti pubblici"],
        "errori": ["Dimenticare le nuove condizioni anti-abuso introdotte dal D.Lgs. 136/2024", "Non notificare la proposta anche all'Agente della Riscossione (AdER) oltre che ad Agenzia Entrate", "Presentare una stima liquidatoria non credibile facilmente smontabile dall'Avvocatura dello Stato"]
    },
    {
        "cod": "SOC-074", "slug": "piano-ristrutturazione-omologazione-pro-art-64-bis-ccii",
        "cat": "concordato-accordi", "cat_lbl": "Concordato & Accordi", "pilastro": "concordato-preventivo-accordi-ristrutturazione",
        "titolo": "Piano di Ristrutturazione soggetto ad Omologazione (PRO) ex art. 64-bis CCII",
        "seo_title": "Piano di Ristrutturazione Omologazione PRO Art. 64-bis CCII",
        "desc": "Lo strumento flessibile del CCII che permette di distribuire il valore in deroga all'ordine delle prelazioni (salvi i lavoratori) con l'approvazione unanime delle classi.",
        "keywords": ["piano ristrutturazione omologazione pro", "art 64 bis ccii", "deroga ordine prelazioni ccii"],
        "norme": ["Art. 64-bis CCII", "Art. 64-ter CCII", "Art. 64-quater CCII"],
        "scenario": "Un'impresa in crisi ha bisogno di distribuire il valore del risanamento in modo flessibile tra soci, fornitori strategici e banche derogando rigidamente alle cause di prelazione.",
        "rischio": "Nel PRO occorre l'approvazione di TUTTE le classi; se anche una sola classe vota contro, il PRO non puo' essere omologato (ma puo' convertirsi in concordato preventivo ex art. 64-quater).",
        "protocollo": [
            "Costruire classi omogenee di creditori negoziando preventivamente il consenso di ciascuna classe.",
            "Assicurare sempre il pagamento integrale entro 30 giorni dall'omologazione dei crediti dei lavoratori (art. 2751-bis n. 1 c.c.), unica deroga vietata.",
            "Conservare la gestione ordinaria e straordinaria dell'impresa sotto il controllo del commissario giudiziale (art. 64-bis co. 5).",
            "In caso di mancata unanimita' delle classi, attivare tempestivamente la conversione in concordato preventivo ex art. 64-quater CCII."
        ],
        "prove": ["Piano PRO e suddivisione in classi", "Attestazione di veridicita' e fattibilita' del professionista indipendente", "Dichiarazioni di voto delle classi", "Eventuale istanza di conversione in concordato preventivo"],
        "errori": ["Scegliere il PRO senza aver sondato prima la disponibilita' delle classi chiave", "Tardare a convertire in concordato preventivo quando una classe si oppone", "Non rispettare la tutela integrale dei crediti di lavoro"]
    },
    {
        "cod": "SOC-075", "slug": "ristrutturazione-trasversale-cross-class-cram-down-art-112",
        "cat": "concordato-accordi", "cat_lbl": "Concordato & Accordi", "pilastro": "concordato-preventivo-accordi-ristrutturazione",
        "titolo": "Ristrutturazione trasversale (cross-class cram-down) nel concordato in continuita' (art. 112 co. 2 CCII)",
        "seo_title": "Cross-Class Cram-Down Art. 112 co. 2 CCII: Omologa con Classi Dissenzienti",
        "desc": "Come ottenere l'omologazione del concordato preventivo in continuita' anche se una o piu' classi di creditori votano contro, rispettando le 4 condizioni dell'art. 112 co. 2 CCII.",
        "keywords": ["cross class cram down art 112 ccii", "ristrutturazione trasversale concordato", "omologa con classi dissenzienti"],
        "norme": ["Art. 112 co. 2 CCII", "Art. 84 co. 6 CCII", "D.Lgs. 136/2024"],
        "scenario": "Nel concordato preventivo in continuita', la maggioranza delle classi approva la proposta ma una classe (es. banche o fornitori) vota contro.",
        "rischio": "Se non vengono rispettate tutte e quattro le condizioni dell'art. 112 co. 2 (inclusa la regola della priorita' relativa e il voto di almeno una classe 'maltrattata' in the money), il Tribunale rigetta l'omologa.",
        "protocollo": [
            "Verificare il rispetto della priorita' assoluta sul valore di liquidazione e della priorita' relativa sul valore eccedente (surplus di continuita').",
            "Accertare che nessun creditore riceva piu' dell'importo del proprio credito.",
            "Verificare che la proposta sia approvata dalla maggioranza delle classi (almeno una di creditori privilegiati) oppure da almeno una classe 'in the money' parzialmente soddisfatta.",
            "Presentare istanza espressa di omologazione trasversale al Tribunale replicando alle opposizioni dei creditori dissenzienti (best interest test)."
        ],
        "prove": ["Esito dettagliato delle votazioni per singola classe", "Tabella di riparto valore di liquidazione vs surplus di continuita'", "Perizia sul valore di liquidazione e convenienza per i dissenzienti", "Istanza di ristrutturazione trasversale ex art. 112 co. 2 CCII"],
        "errori": ["Creare classi artificiose al solo scopo di fabbricare maggioranze (il Tribunale controlla la correttezza delle classi)", "Violare la regola della priorita' relativa trattando una classe dissenziente peggio di una di grado inferiore", "Dimenticare l'istanza espressa del debitore per il cross-class cram-down"]
    },
    {
        "cod": "SOC-076", "slug": "continuita-contratti-pubblici-appalti-concordato-art-95",
        "cat": "concordato-accordi", "cat_lbl": "Concordato & Accordi", "pilastro": "concordato-preventivo-accordi-ristrutturazione",
        "titolo": "Prosecuzione dei contratti pubblici e partecipazione a gare in concordato preventivo (art. 95 CCII)",
        "seo_title": "Contratti Pubblici e Appalti in Concordato Preventivo Art. 95 CCII",
        "desc": "Come mantenere in vita gli appalti pubblici in corso e partecipare a nuove gare durante il concordato preventivo in continuita' evitando la risoluzione automatica.",
        "keywords": ["contratti pubblici concordato art 95 ccii", "partecipazione gare appalto concordato", "continuita appalti pubblici crisi"],
        "norme": ["Art. 95 CCII", "D.Lgs. 36/2023", "Art. 186-bis L.F. (superato)"],
        "scenario": "Un'impresa edile o di servizi titolare di appalti con enti pubblici accede al concordato preventivo in continuita' e teme la risoluzione dei contratti o l'esclusione da nuove gare.",
        "rischio": "La perdita delle commesse pubbliche azzera i flussi su cui si regge il piano di continuita'.",
        "protocollo": [
            "Depositare l'attestazione del professionista indipendente di conformita' al piano e di ragionevole capacita' di adempimento del contratto pubblico (art. 95 co. 3 CCII).",
            "Per partecipare a nuove gare dopo il deposito della domanda (e prima dell'omologa), chiedere l'autorizzazione espressa al Tribunale sentito il commissario giudiziale.",
            "Valutare l'avvalimento di un altro operatore se richiesto dall'ANAC o dalla stazione appaltante nei casi previsti.",
            "Diffidare le stazioni appaltanti da eventuali risoluzioni automatiche vietate espressamente dall'art. 95 co. 1 CCII."
        ],
        "prove": ["Contratti di appalto pubblico in corso", "Relazione del professionista indipendente ex art. 95 co. 3 CCII", "Decreto autorizzativo del Tribunale per partecipazione a nuove gare", "Regolarita' contributiva post-deposito"],
        "errori": ["Partecipare a una nuova gara dopo la domanda di concordato senza preventiva autorizzazione del Tribunale", "Non produrre subito la relazione di capacita' di adempimento alla stazione appaltante", "Accettare clausole di risoluzione automatica per accesso al concordato (sono inefficaci per legge)"]
    },
    {
        "cod": "SOC-077", "slug": "finanziamenti-prededucibili-concordato-accordi-art-99-ccii",
        "cat": "concordato-accordi", "cat_lbl": "Concordato & Accordi", "pilastro": "concordato-preventivo-accordi-ristrutturazione",
        "titolo": "Finanziamenti prededucibili urgenti nel concordato preventivo e negli ARD (art. 99 CCII)",
        "seo_title": "Finanziamenti Prededucibili Art. 99 CCII: Concordato e ARD",
        "desc": "Come ottenere dal Tribunale l'autorizzazione a nuova finanza prededucibile (e mantenimento linee di credito) indispensabile per evitare un danno grave e irreparabile all'azienda.",
        "keywords": ["finanziamenti prededucibili art 99 ccii", "nuova finanza concordato preventivo", "autorizzazione tribunale finanziamento urgente"],
        "norme": ["Art. 99 CCII", "Art. 101 CCII", "Art. 102 CCII"],
        "scenario": "Subito dopo il deposito della domanda di concordato o ARD, l'impresa ha bisogno urgente di liquidita' ponte o del mantenimento di linee autoliquidanti per non fermare la produzione.",
        "rischio": "Senza il decreto autorizzativo del Tribunale ex art. 99 CCII, nessuna banca eroga finanza in procedura per timore di perdere la prededuzione.",
        "protocollo": [
            "Depositare ricorso motivato ex art. 99 CCII specificando l'oggetto, le condizioni economiche del finanziamento e le ragioni di urgenza (danno grave e irreparabile all'attivita').",
            "Allegare la relazione del professionista indipendente che attesta la funzionalita' alla migliore soddisfazione dei creditori (derogabile solo in casi di urgenza estrema).",
            "Se il finanziamento proviene dai soci, verificare la prededuzione nei limiti dell'80% (o 100% se diventano soci in esecuzione del piano) ex art. 102 CCII.",
            "Ottenere l'autorizzazione anche all'eventuale concessione di pegno o ipoteca a garanzia."
        ],
        "prove": ["Ricorso urgente ex art. 99 CCII e term sheet bancario", "Attestazione di funzionalita' del professionista indipendente", "Piano di cassa con evidenza del fabbisogno immediato", "Decreto autorizzativo del Tribunale"],
        "errori": ["Richiedere il finanziamento senza dimostrare che l'impresa non ha altre fonti di liquidita'", "Dimenticare il limite dell'80% per i finanziamenti dei soci ex art. 102 CCII", "Non sentire preventivamente il commissario giudiziale"]
    },
    {
        "cod": "SOC-078", "slug": "pagamento-fornitori-strategici-anteriori-concordato-art-100",
        "cat": "concordato-accordi", "cat_lbl": "Concordato & Accordi", "pilastro": "concordato-preventivo-accordi-ristrutturazione",
        "titolo": "Autorizzazione al pagamento di fornitori strategici anteriori nel concordato (art. 100 CCII)",
        "seo_title": "Pagamento Fornitori Strategici Art. 100 CCII in Concordato",
        "desc": "Come pagare fornitori essenziali o retribuzioni arretrate anteriori alla domanda di concordato in continuita' senza violare la par condicio creditorum.",
        "keywords": ["pagamento fornitori strategici art 100 ccii", "autorizzazione pagamento crediti anteriori", "concordato continuita fornitori essenziali"],
        "norme": ["Art. 100 CCII", "Art. 99 CCII"],
        "scenario": "Un fornitore monopolista o tecnologicamente infungibile rifiuta nuove consegne se non vengono pagate le fatture scadute prima del deposito del concordato.",
        "rischio": "Pagare un creditore anteriore senza autorizzazione del Tribunale comporta la revoca del concordato (art. 106 CCII) e rischi di bancarotta preferenziale.",
        "protocollo": [
            "Dimostrare che la prestazione del fornitore e' oggettivamente essenziale per la prosecuzione dell'attivita' e non sostituibile sul mercato in tempi utili.",
            "Acquisire l'attestazione del professionista indipendente che il pagamento e' funzionale ad assicurare la migliore soddisfazione dei creditori (non richiesta se si usa nuova finanza senza obbligo di restituzione o postergata).",
            "Depositare istanza di autorizzazione al Tribunale ex art. 100 CCII (utilizzabile anche per retribuzioni dei lavoratori addetti all'attivita').",
            "Eseguire il pagamento solo dopo il deposito del decreto autorizzativo."
        ],
        "prove": ["Istanza motivata ex art. 100 CCII", "Attestazione di essenzialita' e convenienza del professionista indipendente", "Documentazione dell'infungibilita' del fornitore", "Decreto autorizzativo del Tribunale"],
        "errori": ["Pagare il fornitore prima di ricevere l'autorizzazione scritta del giudice", "Qualificare come strategico un fornitore facilmente sostituibile", "Non verificare se il pagamento puo' essere coperto da finanza esterna apposita"]
    },
    {
        "cod": "SOC-079", "slug": "scioglimento-sospensione-contratti-pendenti-concordato-art-97",
        "cat": "concordato-accordi", "cat_lbl": "Concordato & Accordi", "pilastro": "concordato-preventivo-accordi-ristrutturazione",
        "titolo": "Scioglimento o sospensione dei contratti pendenti onerosi nel concordato (art. 97 CCII)",
        "seo_title": "Scioglimento Contratti Pendenti Art. 97 CCII in Concordato Preventivo",
        "desc": "Come liberare l'azienda da contratti di leasing, locazione o fornitura non coerenti col piano di concordato, liquidando al contraente solo un indennizzo chirografario.",
        "keywords": ["scioglimento contratti pendenti art 97 ccii", "sospensione contratti concordato", "indennizzo chirografario art 97"],
        "norme": ["Art. 97 CCII", "Art. 95 CCII"],
        "scenario": "L'azienda in concordato ha contratti di locazione di filiali in perdita, leasing sovradimensionati o forniture non piu' coerenti col piano di rilancio.",
        "rischio": "Lasciare attivi contratti in perdita genera crediti in prededuzione che assorbono la cassa del concordato.",
        "protocollo": [
            "Individuare i contratti ancora ineseguiti o non compiutamente eseguiti da entrambe le parti non coerenti con le previsioni del piano.",
            "Depositare istanza motivata di autorizzazione allo scioglimento o alla sospensione (fino a 30 giorni prorogabili una volta) ex art. 97 CCII, notificando alla controparte.",
            "Negoziare o far determinare l'indennizzo dovuto alla controparte, che viene soddisfatto come credito chirografario anteriore al concordato.",
            "Rispettare le esclusioni tassative (es. contratti di lavoro subordinato e preliminari di vendita abitazione principale trascritti)."
        ],
        "prove": ["Copia dei contratti pendenti e dimostrazione della loro non coerenza col piano", "Istanza ex art. 97 CCII notificata al contraente in bonis", "Calcolo dell'indennizzo chirografario da inserire nel piano", "Decreto autorizzativo del Tribunale"],
        "errori": ["Chiedere lo scioglimento di contratti gia' interamente eseguiti da una parte", "Omettere la notifica alla controparte (violazione del contraddittorio)", "Non appostare nel piano un fondo rischi per gli indennizzi chirografari"]
    },
    {
        "cod": "SOC-080", "slug": "proposte-offerte-concorrenti-concordato-artt-90-91",
        "cat": "concordato-accordi", "cat_lbl": "Concordato & Accordi", "pilastro": "concordato-preventivo-accordi-ristrutturazione",
        "titolo": "Difesa da proposte concorrenti e gestione delle offerte concorrenti (artt. 90-91 CCII)",
        "seo_title": "Proposte e Offerte Concorrenti Art. 90 e 91 CCII nel Concordato",
        "desc": "Come prevenire scalate ostili di creditori tramite proposte concorrenti (soglie 30%/20%) e come strutturare la gara sulle offerte concorrenti per l'acquisto dell'azienda.",
        "keywords": ["proposte concorrenti art 90 ccii", "offerte concorrenti art 91 ccii", "scalata ostile concordato preventivo"],
        "norme": ["Art. 90 CCII", "Art. 91 CCII"],
        "scenario": "Un creditore o un fondo (titolare di almeno il 10% dei crediti) minaccia di presentare una proposta concorrente per rilevare la societa', oppure un terzo fa un'offerta competitiva sull'azienda.",
        "rischio": "I soci originari possono perdere il controllo della societa' se la propria proposta non raggiunge le soglie protettive dell'art. 90 co. 5 CCII.",
        "protocollo": [
            "Verificare se la proposta del debitore assicura almeno il 30% ai chirografari (o il 20% se il debitore ha utilmente avviato la Composizione Negoziata), soglia che rende inammissibili le proposte concorrenti.",
            "In caso di offerte concorrenti ex art. 91 CCII, collaborare alla definizione di un bando di gara trasparente con cauzioni serie e rimborso spese all'offerente originario.",
            "Se si assiste un investitore interessato a rilevare un'azienda in concordato, strutturare la proposta o offerta concorrente nel termine di 30 giorni prima del voto.",
            "Monitorare la regolarita' del voto e l'esclusione del conflitto di interessi dei creditori proponenti."
        ],
        "prove": ["Attestazione del raggiungimento soglia 30% / 20% ex art. 90 co. 5", "Bando di gara e offerte cauzionate ex art. 91", "Relazione del commissario giudiziale comparativa", "Verbali di apertura buste e gara competitiva"],
        "errori": ["Sottovalutare il rischio di proposta concorrente quando si offre meno del 30% ai chirografari", "Omettere la Composizione Negoziata preventiva che abbassa la soglia protettiva al 20%", "Strutturare offerte chiuse non contendibili"]
    },
    {
        "cod": "SOC-081", "slug": "opposizione-omologazione-concordato-accordi-art-48",
        "cat": "concordato-accordi", "cat_lbl": "Concordato & Accordi", "pilastro": "concordato-preventivo-accordi-ristrutturazione",
        "titolo": "Opposizione all'omologazione del concordato preventivo o degli ARD (art. 48 CCII)",
        "seo_title": "Opposizione Omologazione Concordato e ARD Art. 48 CCII",
        "desc": "Come difendere l'omologazione del piano dalle opposizioni dei creditori dissenzienti o come proporre opposizione a tutela di un creditore leso.",
        "keywords": ["opposizione omologazione concordato art 48", "convenienza proposta concordato", "reclamo sentenza omologazione art 51"],
        "norme": ["Art. 48 CCII", "Art. 112 CCII", "Art. 51 CCII"],
        "scenario": "Un creditore dissenziente (o l'Agenzia delle Entrate) deposita memoria di opposizione almeno 10 giorni prima dell'udienza di omologazione contestando la fattibilita' o la convenienza del piano.",
        "rischio": "Il rigetto dell'omologazione puo' comportare la contestuale apertura della liquidazione giudiziale su istanza di un creditore o del PM.",
        "protocollo": [
            "Esaminare subito la legittimazione dell'opponente e i motivi dedotti (regolarita' procedura, fattibilita' del piano, difetto di convenienza rispetto alla liquidazione giudiziale).",
            "Replicare con memorie difensive e integrazioni dell'attestatore indipendente dimostrando il rispetto del best interest test.",
            "Verificare il parere motivato del commissario giudiziale depositato prima dell'udienza.",
            "In caso di sentenza sfavorevole, proporre reclamo in Corte d'Appello entro 30 giorni ex art. 51 CCII."
        ],
        "prove": ["Memoria di opposizione del creditore e data di deposito", "Parere motivato del commissario giudiziale ex art. 48", "Integrazione tecnica dell'attestatore e perizie di valore", "Sentenza di omologazione o rigetto"],
        "errori": ["Depositare l'opposizione oltre il termine di 10 giorni prima dell'udienza", "Non replicare puntualmente alle contestazioni numeriche sulla convenienza", "Dimenticare di chiedere la sospensione degli effetti in caso di reclamo"]
    },
    {
        "cod": "SOC-082", "slug": "risoluzione-annullamento-concordato-preventivo-art-119",
        "cat": "concordato-accordi", "cat_lbl": "Concordato & Accordi", "pilastro": "concordato-preventivo-accordi-ristrutturazione",
        "titolo": "Risoluzione per inadempimento e annullamento del concordato preventivo (artt. 119-120 CCII)",
        "seo_title": "Risoluzione e Annullamento Concordato Preventivo Art. 119 CCII",
        "desc": "Come difendere l'impresa da richieste di risoluzione del concordato omologato (eccezione di scarsa importanza, termine annuale) o come agire per conto del creditore insoddisfatto.",
        "keywords": ["risoluzione concordato preventivo art 119", "annullamento concordato art 120 ccii", "inadempimento scarsa importanza concordato"],
        "norme": ["Art. 119 CCII", "Art. 120 CCII", "Art. 1455 c.c."],
        "scenario": "Dopo l'omologazione, i realizzi o i flussi di continuita' subiscono ritardi e un creditore (o il commissario su istanza di un creditore) chiede la risoluzione del concordato.",
        "rischio": "La risoluzione fa cadere l'effetto esdebitatorio del concordato e apre la strada alla liquidazione giudiziale.",
        "protocollo": [
            "Verificare il rispetto del termine di decadenza di 1 anno dalla scadenza dell'ultimo adempimento previsto nel concordato (art. 119 co. 4 CCII).",
            "Dimostrare se l'inadempimento ha 'scarsa importanza' (art. 119 co. 3 CCII) rispetto all'economia complessiva del piano o se dipende da cause esterne sanabili.",
            "Proporre tempestivamente modifiche o apporti integrativi per evitare la declaratoria di risoluzione.",
            "Per i creditori: verificare se vi e' stata dolosa esagerazione del passivo o sottrazione dell'attivo ai fini dell'annullamento ex art. 120 CCII."
        ],
        "prove": ["Sentenza di omologazione e cronoprogramma dei pagamenti", "Rendiconti del liquidatore o relazioni semestrali sull'esecuzione", "Prove dei pagamenti gia' eseguiti e delle cause del ritardo", "Eventuali offerte integrative o nuova finanza"],
        "errori": ["Restare silenti di fronte ai primi ritardi esecutivi senza informare il commissario", "Dimenticare che il singolo creditore puo' chiedere la liquidazione giudiziale anche senza previa risoluzione del concordato (giurisprudenza a Sezioni Unite 4696/2022)", "Lasciar decorrere l'anno di decadenza da parte del creditore"]
    },
    {
        "cod": "SOC-083", "slug": "concordato-preventivo-gruppo-imprese-art-284-ccii",
        "cat": "concordato-accordi", "cat_lbl": "Concordato & Accordi", "pilastro": "concordato-preventivo-accordi-ristrutturazione",
        "titolo": "Concordato preventivo e accordi di ristrutturazione di gruppo (artt. 284-286 CCII)",
        "seo_title": "Concordato Preventivo di Gruppo Art. 284 CCII: Piano Unitario",
        "desc": "Come ristrutturare piu' societa' di un gruppo con un unico ricorso, piano unitario o collegato, trasferimenti infragruppo autorizzati e autonomia delle masse.",
        "keywords": ["concordato preventivo di gruppo art 284", "piano unitario gruppo ccii", "ristrutturazione gruppo societario"],
        "norme": ["Art. 284 CCII", "Art. 285 CCII", "Art. 286 CCII"],
        "scenario": "Un gruppo societario in crisi presenta un'unica domanda di concordato preventivo o di accordi di ristrutturazione per salvare il perimetro industriale sinergico.",
        "rischio": "La violazione del principio di separazione delle masse attive e passive o il pregiudizio ai creditori di una singola societa' porta al rigetto dell'omologazione.",
        "protocollo": [
            "Dimostrare analiticamente nell'attestazione le ragioni di maggiore convenienza della gestione unitaria di gruppo rispetto a piani autonomi separati.",
            "Rispettare rigorosamente l'autonomia delle masse attive e passive di ciascuna societa' (art. 284 co. 3 CCII).",
            "Eventuali trasferimenti di risorse infragruppo sono ammessi solo se attestati come necessari alla continuita' e coerenti con il miglior soddisfacimento dei creditori di tutte le imprese (art. 285).",
            "Gestire le votazioni separate per ciascuna impresa (con esclusione dal voto delle societa' del gruppo titolari di crediti infragruppo)."
        ],
        "prove": ["Domanda unitaria di gruppo e piano consolidato + piani singoli", "Attestazione indipendente di convenienza del piano di gruppo", "Prospetto masse separate e flussi infragruppo", "Elenco creditori esclusi dal voto per appartenenza al gruppo"],
        "errori": ["Fondere in un'unica massa i patrimoni delle societa' del gruppo", "Far votare le societa' del gruppo per alterare le maggioranze", "Non giustificare i vantaggi compensativi per la controllata che cede risorse"]
    },
    {
        "cod": "SOC-084", "slug": "classamento-creditori-concordato-preventivo-art-85",
        "cat": "concordato-accordi", "cat_lbl": "Concordato & Accordi", "pilastro": "concordato-preventivo-accordi-ristrutturazione",
        "titolo": "Formazione delle classi di creditori nel concordato preventivo (art. 85 CCII)",
        "seo_title": "Formazione Classi Creditori Concordato Art. 85 CCII",
        "desc": "Quando la suddivisione in classi e' obbligatoria (continuita', crediti fiscali/previdenziali non integrali, garanzie di terzi, PMI) e come evitare contestazioni del Tribunale.",
        "keywords": ["classi creditori concordato art 85", "classamento obbligatorio ccii", "creditori garantiti da terzi classe"],
        "norme": ["Art. 85 CCII", "Art. 84 CCII", "Art. 109 CCII"],
        "scenario": "Nella stesura della proposta di concordato preventivo occorre suddividere banche, Erario, fornitori, imprese minori e creditori muniti di garanzie di terzi in classi giuridicamente omogenee.",
        "rischio": "Un classamento scorretto o l'omissione di una classe obbligatoria (es. creditori con garanzia di terzi o imprese minori ex art. 85 co. 3) causa l'inammissibilita' della proposta.",
        "protocollo": [
            "Verificare tutti i casi di classamento obbligatorio dell'art. 85 co. 2 e 3 CCII (Erario/INPS falcidiati, creditori garantiti da terzi/MCC/fideiussori, fornitori PMI, creditori proponenti).",
            "Accorpare i creditori secondo criteri oggettivi di omogeneita' della posizione giuridica e degli interessi economici.",
            "Trattare correttamente i creditori muniti di garanzia pubblica MCC/SACE tenendo conto del privilegio di rivalsa dello Stato.",
            "Verificare il peso di voto di ciascuna classe in vista della maggioranza o del cross-class cram-down."
        ],
        "prove": ["Elenco analitico creditori con privilegi, garanzie di terzi e dimensione PMI", "Relazione sui criteri di omogeneita' delle classi", "Simulazione dei quorum di voto per classe", "Verifica del commissario giudiziale"],
        "errori": ["Inserire nella stessa classe banche garantite da MCC e fornitori chirografari puri", "Dimenticare la classe separata per le imprese minori nel concordato in continuita'", "Creare classi 'di comodo' prive di reale omogeneita'"]
    },
    {
        "cod": "SOC-085", "slug": "revoca-ammissione-concordato-atti-frode-art-106-ccii",
        "cat": "concordato-accordi", "cat_lbl": "Concordato & Accordi", "pilastro": "concordato-preventivo-accordi-ristrutturazione",
        "titolo": "Difesa contro la revoca del concordato per atti di frode scoperti dal commissario (art. 106 CCII)",
        "seo_title": "Revoca Concordato per Atti di Frode Art. 106 CCII: Difesa Impresa",
        "desc": "Come difendere la societa' nel procedimento ex art. 106 CCII quando il commissario segnala occultamenti di attivo, atti non autorizzati o difetto di fattibilita'.",
        "keywords": ["revoca concordato atti frode art 106", "segnalazione commissario giudiziale", "difesa procedimento art 106 ccii"],
        "norme": ["Art. 106 CCII", "Art. 47 CCII"],
        "scenario": "Il commissario giudiziale deposita una relazione ex art. 106 CCII segnalando presunti atti di frode anteriori non dichiarati nella proposta o pagamenti non autorizzati durante la procedura.",
        "rischio": "Revoca immediata dell'ammissione al concordato e contestuale dichiarazione di liquidazione giudiziale su istanza di creditori o PM, con riflessi penali.",
        "protocollo": [
            "Dimostrare che l'operazione contestata non aveva valenza decettiva ne' intento di ingannare i creditori sul consenso al voto.",
            "Verificare se il fatto era gia' desumibile dai bilanci o dalla documentazione depositata (piena disclosure esclude la frode).",
            "Integrare immediatamente la proposta e la relazione informativa prima del voto per garantire piena trasparenza ai creditori.",
            "Contestare l'eventuale erronea ricostruzione contabile del commissario con perizia di parte in udienza collegiale."
        ],
        "prove": ["Relazione ex art. 106 CCII del commissario giudiziale", "Documentazione gia' allegata alla domanda originaria (prova di disclosure)", "Perizia contabile di chiarimento sulle operazioni contestate", "Memoria difensiva e integrazione informativa ai creditori"],
        "errori": ["Omettere nella domanda di concordato operazioni pregresse delicate sperando che il commissario non le veda", "Compiere atti di straordinaria amministrazione senza autorizzazione del giudice delegato", "Non presidiare attivamente l'udienza ex art. 106"]
    },

    # ═══════════════════ 5. LIQUIDAZIONE GIUDIZIALE / FALLIMENTO (086-100) ═══════════════════
    {
        "cod": "SOC-086", "slug": "difesa-istanza-liquidazione-giudiziale-udienza-prefallimentare",
        "cat": "liquidazione-giudiziale", "cat_lbl": "Liquidazione Giudiziale", "pilastro": "liquidazione-giudiziale-fallimento-opposizioni",
        "titolo": "Difesa dell'impresa in udienza prefallimentare contro istanza di liquidazione giudiziale",
        "seo_title": "Difesa Istanza Liquidazione Giudiziale (Fallimento): Udienza Art. 41 CCII",
        "desc": "Come opporsi con successo al ricorso di un creditore per l'apertura della liquidazione giudiziale: contestazione credito, insolvenza, soglie impresa minore e desistenza.",
        "keywords": ["difesa istanza liquidazione giudiziale", "udienza prefallimentare art 41 ccii", "desistenza creditore fallimento"],
        "norme": ["Art. 40 CCII", "Art. 41 CCII", "Art. 49 CCII"],
        "scenario": "Un creditore notifica alla societa' il ricorso per l'apertura della liquidazione giudiziale e il decreto di convocazione davanti al Tribunale.",
        "rischio": "La mancata costituzione o una difesa generica porta quasi automaticamente alla sentenza di apertura della liquidazione giudiziale, con spossessamento immediato.",
        "protocollo": [
            "Costituirsi almeno 7 giorni prima dell'udienza (art. 41 co. 4 CCII) depositando i bilanci degli ultimi 3 esercizi e la situazione economico-patrimoniale aggiornata.",
            "Verificare tutte le difese preliminari: impresa minore sotto soglie (art. 2 CCII), debiti scaduti inferiori a 30.000 euro (art. 49 co. 5), contestazione seria del credito istante, assenza di insolvenza strutturale.",
            "Negoziare subito un accordo di saldo e stralcio o rientro con il creditore istante per ottenere il deposito dell'atto di desistenza prima della decisione.",
            "Se vi sono piu' creditori o insolvenza reale, valutare il deposito tempestivo di domanda di accesso a uno strumento di regolazione della crisi (art. 7 e 44 CCII)."
        ],
        "prove": ["Ricorso e decreto di convocazione con data notifica", "Bilanci degli ultimi tre esercizi e situazione aggiornata", "Prove di contestazione del credito (vizi, compensazione, prescrizione)", "Atto di desistenza del creditore o ricevuta di pagamento"],
        "errori": ["Non costituirsi in udienza pensando di risolvere parlando informalmente con il creditore", "Dimenticare di depositare i bilanci degli ultimi tre esercizi (l'onere della prova delle soglie grava sul debitore)", "Ottenere una desistenza verbale senza deposito formale telematico prima dell'udienza"]
    },
    {
        "cod": "SOC-087", "slug": "eccezione-impresa-minore-soglie-non-fallibilita-art-2-ccii",
        "cat": "liquidazione-giudiziale", "cat_lbl": "Liquidazione Giudiziale", "pilastro": "liquidazione-giudiziale-fallimento-opposizioni",
        "titolo": "Eccezione di impresa minore non fallibile: le tre soglie dimensionali dell'art. 2 CCII",
        "seo_title": "Soglie Non Fallibilita' Impresa Minore Art. 2 CCII: 300k, 200k, 500k",
        "desc": "Come provare rigorosamente il possesso congiunto dei tre requisiti dell'impresa minore (attivo <= 300.000, ricavi <= 200.000, debiti <= 500.000 euro) per far rigettare l'istanza.",
        "keywords": ["soglie impresa minore art 2 ccii", "non fallibilita 300000 200000 500000", "onere prova non fallibilita"],
        "norme": ["Art. 2 co. 1 lett. d CCII", "Art. 121 CCII"],
        "scenario": "Una piccola S.r.l. o ditta individuale riceve un'istanza di liquidazione giudiziale pur avendo dimensioni ridotte.",
        "rischio": "Se il debitore non fornisce la prova documentale rigorosa del mancato superamento di TUTTE e tre le soglie nei tre esercizi precedenti, il Tribunale dichiara la liquidazione giudiziale anche per aziende minuscole.",
        "protocollo": [
            "Verificare per ciascuno dei tre esercizi antecedenti (o dall'inizio attivita'): attivo patrimoniale <= 300.000 euro, ricavi lordi <= 200.000 euro, e al momento attuale debiti anche non scaduti <= 500.000 euro.",
            "Produrre i bilanci depositati (o, per ditte individuali/societa' di persone, dichiarazioni fiscali, IVA, registro beni ammortizzabili, situazione contabile asseverata).",
            "Attenzione: includere nel calcolo dei debiti anche quelli contestati o risultanti da estratto di ruolo AdER e INPS.",
            "Eccepire il difetto di presupposto soggettivo chiedendo il rigetto del ricorso con condanna alle spese."
        ],
        "prove": ["Bilanci depositati degli ultimi tre esercizi", "Dichiarazioni dei redditi, IVA e IRAP", "Estratto di ruolo AdER e visura debitoria INPS/INAIL aggiornata", "Relazione contabile di riscontro analitico delle tre soglie"],
        "errori": ["Superare anche una sola soglia in un solo anno (fa perdere la qualifica di impresa minore)", "Dimenticare di conteggiare i debiti fiscali o non ancora scaduti nella soglia dei 500.000 euro", "Produrre bilanci non approvati ne' supportati da scritture contabili"]
    },
    {
        "cod": "SOC-088", "slug": "soglia-30000-euro-debiti-scaduti-art-49-co-5-ccii",
        "cat": "liquidazione-giudiziale", "cat_lbl": "Liquidazione Giudiziale", "pilastro": "liquidazione-giudiziale-fallimento-opposizioni",
        "titolo": "Soglia dei 30.000 euro di debiti scaduti e non pagati (art. 49 co. 5 CCII)",
        "seo_title": "Soglia 30.000 Euro Liquidazione Giudiziale Art. 49 co. 5 CCII",
        "desc": "Come far rigettare l'istanza di liquidazione giudiziale dimostrando che l'ammontare complessivo dei debiti scaduti e non pagati risultanti dall'istruttoria e' inferiore a 30.000 euro.",
        "keywords": ["soglia 30000 euro liquidazione giudiziale", "art 49 comma 5 ccii", "debiti scaduti inferiori 30000"],
        "norme": ["Art. 49 co. 5 CCII"],
        "scenario": "Un creditore presenta istanza di liquidazione giudiziale per un credito di importo contenuto e dagli atti dell'istruttoria prefallimentare non emergono debiti scaduti superiori a 30.000 euro.",
        "rischio": "Senza verificare anche i debiti fiscali e previdenziali acquisiti d'ufficio dalla cancelleria (art. 42 CCII), si rischia di superare la soglia a propria insaputa.",
        "protocollo": [
            "Accedere subito al fascicolo telematico per verificare le informative d'ufficio acquisite dal Tribunale (AdE, AdER, INPS).",
            "Dimostrare l'avvenuta rateazione regolare o la sospensione/sgravio di eventuali cartelle per escluderle dai 'debiti scaduti e non pagati'.",
            "Ridurre l'esposizione scaduta sotto i 30.000 euro mediante pagamenti mirati o contestazioni fondate del credito istante.",
            "Chiedere il rigetto dell'istanza ai sensi dell'art. 49 co. 5 CCII."
        ],
        "prove": ["Informative ex art. 42 CCII acquisite nel fascicolo telematico", "Piani di rateazione AdER/INPS in regola con i pagamenti", "Quietanza di pagamento o prova di contestazione del credito", "Prospetto analitico dei debiti effettivamente scaduti"],
        "errori": ["Calcolare la soglia solo sul credito dell'istante ignorando INPS e AdER", "Avere rateazioni decadute che rendono l'intero debito immediatamente scaduto", "Non consultare il fascicolo telematico prima dell'udienza"]
    },
    {
        "cod": "SOC-089", "slug": "istanza-liquidazione-giudiziale-pubblico-ministero-art-38",
        "cat": "liquidazione-giudiziale", "cat_lbl": "Liquidazione Giudiziale", "pilastro": "liquidazione-giudiziale-fallimento-opposizioni",
        "titolo": "Difesa dall'istanza di liquidazione giudiziale proposta dal Pubblico Ministero (art. 38 CCII)",
        "seo_title": "Istanza Liquidazione Giudiziale del PM Art. 38 CCII: Difesa",
        "desc": "Come difendersi quando e' la Procura della Repubblica a chiedere la liquidazione giudiziale a seguito di segnalazione di un giudice civile, di un'indagine penale o della GdF.",
        "keywords": ["istanza liquidazione giudiziale pubblico ministero", "art 38 ccii pm", "difesa fallimento su richiesta pm"],
        "norme": ["Art. 38 CCII", "Art. 41 CCII", "Art. 2 co. 1 lett. d CCII"],
        "scenario": "Il Pubblico Ministero deposita ricorso per l'apertura della liquidazione giudiziale avendo avuto notizia dell'insolvenza da un procedimento penale, da una segnalazione di un giudice civile o da verifiche fiscali.",
        "rischio": "Con il PM istante non e' possibile negoziare una semplice 'desistenza' come con un creditore privato; inoltre la vicenda ha spesso paralleli profili penali.",
        "protocollo": [
            "Esaminare gli atti da cui il PM ha tratto la notizia dell'insolvenza (es. ingenti debiti erariali o pignoramenti negativi).",
            "Dimostrare la sussistenza delle soglie di impresa minore (art. 2 CCII) oppure l'insussistenza dello stato di insolvenza (es. rateazioni attive, cassa, affidamenti o beni capienti).",
            "Valutare l'accesso immediato a uno strumento di regolazione della crisi (concordato preventivo, ARD o Composizione Negoziata con misure protettive) che ha priorita' di trattazione (art. 7 CCII).",
            "Coordinare rigorosamente la difesa prefallimentare con la strategia difensiva penale."
        ],
        "prove": ["Ricorso del PM e allegati istruttori", "Bilanci ultimi tre esercizi e prova delle soglie o della solvibilita'", "Piani di rateazione fiscale/previdenziale approvati e in corso", "Eventuale istanza di accesso a strumento di regolazione della crisi"],
        "errori": ["Sottovalutare l'istanza del PM perche' nessun fornitore ha agito", "Rendere dichiarazioni imprudenti in udienza prefallimentare utilizzabili poi nel procedimento penale", "Non coordinare avvocato fallimentarista e penalista"]
    },
    {
        "cod": "SOC-090", "slug": "reclamo-corte-appello-sentenza-liquidazione-giudiziale-art-51",
        "cat": "liquidazione-giudiziale", "cat_lbl": "Liquidazione Giudiziale", "pilastro": "liquidazione-giudiziale-fallimento-opposizioni",
        "titolo": "Reclamo in Corte d'Appello contro la sentenza di liquidazione giudiziale entro 30 giorni (art. 51 CCII)",
        "seo_title": "Reclamo Sentenza Liquidazione Giudiziale Art. 51 CCII: 30 Giorni",
        "desc": "Come impugnare davanti alla Corte d'Appello la sentenza che apre la liquidazione giudiziale, chiedere la sospensione della liquidazione dell'attivo (art. 52) e ottenere la revoca.",
        "keywords": ["reclamo liquidazione giudiziale art 51", "impugnazione sentenza fallimento 30 giorni", "sospensione liquidazione attivo art 52"],
        "norme": ["Art. 51 CCII", "Art. 52 CCII", "Art. 53 CCII"],
        "scenario": "Il Tribunale ha pronunciato la sentenza di apertura della liquidazione giudiziale nonostante vizi di notifica, mancato superamento delle soglie di impresa minore o insussistenza dell'insolvenza.",
        "rischio": "Decorso il termine perentorio di 30 giorni dalla notificazione della sentenza (o iscrizione al Registro Imprese per gli altri interessati), la liquidazione diventa definitiva.",
        "protocollo": [
            "Calcolare rigorosamente il termine di 30 giorni dalla notifica al debitore e depositare ricorso in Corte d'Appello ex art. 51 CCII.",
            "Chiedere contestualmente la sospensione della liquidazione dell'attivo (o dell'esecuzione dei piani di riparto) per gravi e fondati motivi ex art. 52 CCII.",
            "Nel reclamo ex art. 51 (giudizio a cognizione piena con effetto devolutivo) produrre anche nuovi documenti decisivi (es. bilanci o quietanze) che provino la non fallibilita' o la solvibilita'.",
            "In caso di rigetto del reclamo, valutare le ulteriori tutele di legge e gli strumenti alternativi di ristrutturazione."
        ],
        "prove": ["Sentenza di apertura e relata/PEC di notifica", "Fascicolo del giudizio di primo grado e documenti integrativi decisivi", "Prova di eventuali vizi di notifica del ricorso introduttivo", "Istanza di sospensione ex art. 52 CCII"],
        "errori": ["Superare il termine perentorio di 30 giorni", "Omettere l'istanza di sospensione ex art. 52 consentendo al curatore di vendere subito i beni", "Notificare il reclamo solo al creditore dimenticando il curatore"]
    },
    {
        "cod": "SOC-091", "slug": "sospensione-liquidazione-attivo-pendente-reclamo-art-52",
        "cat": "liquidazione-giudiziale", "cat_lbl": "Liquidazione Giudiziale", "pilastro": "liquidazione-giudiziale-fallimento-opposizioni",
        "titolo": "Sospensione urgente della liquidazione dell'attivo durante il reclamo (art. 52 CCII)",
        "seo_title": "Sospensione Vendite Fallimentari in Reclamo Art. 52 CCII",
        "desc": "Come fermare in via d'urgenza aste, svendite di azienda o immobili disposte dal curatore mentre pende il reclamo in Corte d'Appello contro la liquidazione giudiziale.",
        "keywords": ["sospensione liquidazione attivo art 52", "fermare asta curatore pendente reclamo", "gravi e fondati motivi art 52 ccii"],
        "norme": ["Art. 52 CCII", "Art. 51 CCII"],
        "scenario": "Mentre la Corte d'Appello deve ancora decidere il reclamo contro la sentenza di liquidazione giudiziale, il curatore avvia la vendita dell'azienda, del magazzino o degli immobili.",
        "rischio": "Anche se la Corte d'Appello revocasse poi la liquidazione giudiziale, gli atti legalmente compiuti dagli organi della procedura restano salvi (art. 53 CCII), rendendo irreversibile la perdita dei beni.",
        "protocollo": [
            "Depositare istanza autonoma o contestuale al reclamo ex art. 52 CCII chiedendo la sospensione immediata (anche inaudita altera parte in caso di asta imminente).",
            "Dimostrare congiuntamente la fondatezza apparente del reclamo (fumus) e il danno grave e irreparabile derivante dalla dispersione dei beni aziendali.",
            "Offrire garanzie o impegni gestori a tutela della massa se richiesti dalla Corte d'Appello.",
            "Notificare subito il decreto di sospensione al curatore e al giudice delegato."
        ],
        "prove": ["Avvisi di vendita, bandi d'asta o programma di liquidazione del curatore", "Reclamo pendente ex art. 51 CCII con motivi solidi", "Stima del pregiudizio irreversibile sull'avviamento o sugli immobili", "Eventuali garanzie cauzionali"],
        "errori": ["Aspettare la data dell'udienza di merito del reclamo mentre il curatore vende l'azienda", "Non allegare la prova concreta dell'imminenza della liquidazione", "Non notificare immediatamente la sospensione al curatore"]
    },
    {
        "cod": "SOC-092", "slug": "domanda-insinuazione-stato-passivo-tempestiva-art-201",
        "cat": "liquidazione-giudiziale", "cat_lbl": "Liquidazione Giudiziale", "pilastro": "liquidazione-giudiziale-fallimento-opposizioni",
        "titolo": "Domanda di insinuazione allo stato passivo tempestiva (art. 201 CCII) per creditori e lavoratori",
        "seo_title": "Insinuazione Stato Passivo Art. 201 CCII: Termini, Data Certa e Privilegi",
        "desc": "Come presentare correttamente la domanda di ammissione al passivo entro 30 giorni prima dell'udienza, evitando esclusioni per difetto di data certa o errata indicazione del privilegio.",
        "keywords": ["insinuazione stato passivo art 201 ccii", "data certa fatture liquidazione giudiziale", "privilegio artigiano professionista lavoratore"],
        "norme": ["Art. 201 CCII", "Art. 2704 c.c.", "Art. 2751-bis c.c."],
        "scenario": "Un cliente o un datore di lavoro viene sottoposto a liquidazione giudiziale e il creditore (fornitore, professionista, banca, lavoratore) deve far accertare il proprio credito e il relativo privilegio.",
        "rischio": "Una domanda priva di data certa anteriore alla sentenza (art. 2704 c.c.) o che dimentica di indicare esattamente la norma del privilegio viene respinta o degradata a chirografo.",
        "protocollo": [
            "Trasmettere la domanda via PEC all'indirizzo della procedura almeno 30 giorni prima dell'udienza di verifica dello stato passivo.",
            "Allegare contratti, fatture elettroniche (con ricevuta SDI che fornisce data certa), DDT firmati, estratti autentici e prova dell'esecuzione della prestazione.",
            "Indicare con precisione il grado e la norma del privilegio richiesto (es. art. 2751-bis n. 1 lavoratori, n. 2 professionisti, n. 5 artigiani, ipoteca/pegno).",
            "Monitorare il progetto di stato passivo del curatore e depositare osservazioni scritte fino a 5 giorni prima dell'udienza (art. 203 CCII)."
        ],
        "prove": ["Fatture elettroniche XML con ricevuta SDI (data certa)", "Contratti, ordini, DDT, buste paga o parcelle e prova della consegna/prestazione", "Visura iscrizione albo artigiani o ordine professionale per privilegi", "PEC di trasmissione al curatore"],
        "errori": ["Inviare la sola fattura senza prova dell'effettiva consegna dei beni o svolgimento della prestazione", "Dimenticare di chiedere il privilegio (il giudice non lo riconosce d'ufficio)", "Inviare la domanda oltre il termine dei 30 giorni facendola scivolare tra le tardive"]
    },
    {
        "cod": "SOC-093", "slug": "domanda-tardiva-supertardiva-stato-passivo-art-208",
        "cat": "liquidazione-giudiziale", "cat_lbl": "Liquidazione Giudiziale", "pilastro": "liquidazione-giudiziale-fallimento-opposizioni",
        "titolo": "Domanda tardiva e supertardiva di ammissione allo stato passivo (art. 208 CCII)",
        "seo_title": "Insinuazione Tardiva e Supertardiva Art. 208 CCII: Termine 6 Mesi",
        "desc": "Come recuperare un credito dopo l'udienza di verifica: termine ridotto di 6 mesi nel CCII per le tardive e prova della causa non imputabile per le supertardive.",
        "keywords": ["domanda tardiva stato passivo 6 mesi", "supertardiva art 208 ccii", "causa non imputabile mancato avviso curatore"],
        "norme": ["Art. 208 CCII", "Art. 200 CCII"],
        "scenario": "Un creditore viene a conoscenza in ritardo della liquidazione giudiziale del proprio debitore (oppure non ha ricevuto l'avviso PEC del curatore) e deve insinuarsi tardivamente.",
        "rischio": "Nel Codice della Crisi il termine per le domande tardive e' stato dimezzato a 6 mesi (prorogabili a 12 in casi complessi) dal decreto di esecutivita' dello stato passivo: oltre tale limite serve provare la causa non imputabile.",
        "protocollo": [
            "Verificare subito la data di deposito del decreto di esecutivita' dello stato passivo per calcolare il termine semestrale dell'art. 208 co. 1 CCII.",
            "Se sono gia' decorsi i 6 mesi, agire entro 60 giorni dal momento in cui e' cessata la causa impeditiva dimostrando la non imputabilita' del ritardo (es. mancato invio dell'avviso ex art. 200 CCII da parte del curatore pur risultando il credito dalla contabilita').",
            "Trasmettere la domanda via PEC al curatore corredata di tutta la prova del credito e del privilegio.",
            "Tenere presente che i creditori tardivi concorrono solo sui riparti successivi, salvo crediti privilegiati o causa non imputabile."
        ],
        "prove": ["Data di esecutivita' dello stato passivo", "Prova del mancato ricevimento dell'avviso PEC ex art. 200 CCII", "Documentazione del credito con data certa", "Prova della tempestiva attivazione entro 60 giorni dalla scoperta"],
        "errori": ["Fare affidamento sul vecchio termine di 12 mesi della Legge Fallimentare (nel CCII e' 6 mesi)", "Attendere oltre 60 giorni dalla conoscenza effettiva della procedura per la supertardiva", "Non verificare se il credito era gia' presente nelle scritture del debitore"]
    },
    {
        "cod": "SOC-094", "slug": "opposizione-stato-passivo-esclusione-credito-art-206",
        "cat": "liquidazione-giudiziale", "cat_lbl": "Liquidazione Giudiziale", "pilastro": "liquidazione-giudiziale-fallimento-opposizioni",
        "titolo": "Opposizione allo stato passivo contro l'esclusione del credito o del privilegio (art. 206 CCII)",
        "seo_title": "Opposizione Stato Passivo Art. 206 CCII: Ricorso entro 30 Giorni",
        "desc": "Come impugnare davanti al Tribunale collegiale entro 30 giorni il decreto del giudice delegato che ha escluso il credito, negato il privilegio o ammesso con riserva.",
        "keywords": ["opposizione stato passivo art 206 ccii", "esclusione credito stato passivo 30 giorni", "ricorso opposizione stato passivo"],
        "norme": ["Art. 206 CCII", "Art. 207 CCII"],
        "scenario": "Il giudice delegato rigetta in tutto o in parte la domanda di ammissione al passivo (o degrada il credito da privilegiato a chirografario) accogliendo le eccezioni del curatore.",
        "rischio": "Decorso il termine perentorio di 30 giorni dalla comunicazione PEC del curatore, l'esclusione diventa definitiva e il creditore perde il diritto a partecipare ai riparti.",
        "protocollo": [
            "Controllare la data esatta della PEC di comunicazione dell'esito ex art. 205 CCII per rispettare il termine perentorio di 30 giorni.",
            "Depositare ricorso di opposizione allo stato passivo davanti al Tribunale collegiale ex art. 207 CCII (con assistenza obbligatoria di avvocato).",
            "Indicare a pena di decadenza nell'atto introduttivo tutti i mezzi di prova e i documenti nuovi o integrativi (l'opposizione non e' un appello chiuso ma consente nuove prove).",
            "Dimostrare la data certa, l'effettivita' della prestazione e la sussistenza dei requisiti del privilegio."
        ],
        "prove": ["Comunicazione PEC ex art. 205 CCII e copia del decreto di esecutivita' dello stato passivo", "Domanda originaria e documenti integrativi di data certa e adempimento", "Prove testimoniali o istanze di CTU contabile formulate a pena di decadenza nel ricorso", "Orientamenti di giurisprudenza di legittimita' sul privilegio contestato"],
        "errori": ["Superare il termine perentorio di 30 giorni", "Dimenticare di produrre i documenti o articolare i mezzi di prova direttamente nel ricorso ex art. 207 (decadenza)", "Riproporre semplicemente la domanda senza confutare la specifica motivazione del giudice delegato"]
    },
    {
        "cod": "SOC-095", "slug": "rivendica-restituzione-beni-terzi-leasing-liquidazione-giudiziale",
        "cat": "liquidazione-giudiziale", "cat_lbl": "Liquidazione Giudiziale", "pilastro": "liquidazione-giudiziale-fallimento-opposizioni",
        "titolo": "Domanda di rivendica e restituzione di beni di terzi (leasing, noleggio, deposito) art. 201 CCII",
        "seo_title": "Rivendica e Restituzione Beni in Liquidazione Giudiziale Art. 201 CCII",
        "desc": "Come recuperare macchinari, merci in conto vendita, automezzi in leasing o beni in deposito rinvenuti dal curatore presso la sede della societa' sottoposta a liquidazione giudiziale.",
        "keywords": ["rivendica restituzione beni liquidazione giudiziale", "beni in leasing fallimento", "riserva proprieta data certa"],
        "norme": ["Art. 201 CCII", "Art. 210 CCII", "Art. 1524 c.c."],
        "scenario": "All'apertura della liquidazione giudiziale, il curatore inventaria macchinari, merci o veicoli di proprieta' di terzi (locatori, societa' di leasing, fornitori con riserva di proprieta' o depositanti).",
        "rischio": "Senza una tempestiva domanda di rivendica con prova documentale di data certa anteriore, il curatore puo' vendere i beni all'asta a beneficio della massa.",
        "protocollo": [
            "Diffidare subito via PEC il curatore dal vendere i beni di proprieta' altrui allegando i titoli di proprieta' e i numeri di matricola/telaio.",
            "Presentare domanda formale di rivendica/restituzione ex art. 201 CCII entro 30 giorni prima dell'udienza di verifica (chiedendo la sospensione della liquidazione dei beni rivendicati ex art. 210 CCII).",
            "Dimostrare la proprieta' e l'affidamento al debitore con atti aventi data certa anteriore (contratti registrati, fatture SDI, DDT firmati, riserva di proprieta' ex art. 1524 c.c.).",
            "In caso di beni gia' alienati o non piu' reperibili, chiedere la controvalutazione in prededuzione o in chirografo secondo l'art. 210 CCII."
        ],
        "prove": ["Contratto di leasing, noleggio, comodato o vendita con patto di riservato dominio con data certa", "Fatture d'acquisto, certificati PRA, numeri di serie e matricole dei macchinari", "DDT di consegna presso la sede del debitore", "Istanza di sospensione della vendita ex art. 210 CCII"],
        "errori": ["Riprendersi fisicamente i beni dopo la sentenza senza autorizzazione del curatore (rischio penale)", "Non provare la data certa anteriore del patto di riservato dominio (art. 1524 c.c.)", "Inviare una semplice email informale invece della formale domanda ex art. 201 CCII"]
    },
    {
        "cod": "SOC-096", "slug": "difesa-azione-revocatoria-concorsuale-pagamenti-anomali-art-166",
        "cat": "liquidazione-giudiziale", "cat_lbl": "Liquidazione Giudiziale", "pilastro": "liquidazione-giudiziale-fallimento-opposizioni",
        "titolo": "Difesa da azione revocatoria concorsuale per atti e pagamenti anomali (art. 166 co. 1 CCII)",
        "seo_title": "Difesa Revocatoria Concorsuale Art. 166 co. 1 CCII: Atti Anomali",
        "desc": "Come difendere fornitori, banche e acquirenti dall'azione del curatore su vendite sproporzionate, pagamenti con mezzi anomali o garanzie costituite nell'anno anteriore.",
        "keywords": ["revocatoria concorsuale art 166 comma 1", "pagamenti mezzi anomali revocatoria", "inscientia decoctionis difesa"],
        "norme": ["Art. 166 co. 1 CCII", "Art. 170 CCII"],
        "scenario": "Il curatore cita un fornitore, un acquirente o una banca chiedendo la revoca di una vendita a prezzo ritenuto basso, di un pagamento tramite cessione di beni/crediti o di un'ipoteca giudiziale/volontaria.",
        "rischio": "Condanna alla restituzione integrale delle somme o dei beni alla procedura, con semplice ammissione al passivo chirografario ex art. 171 CCII.",
        "protocollo": [
            "Verificare subito i termini di decadenza e prescrizione dell'azione (3 anni dall'apertura della liquidazione giudiziale e comunque non oltre 5 anni dall'atto ex art. 170 CCII) e il periodo sospetto (1 anno o 6 mesi ante domanda di liquidazione).",
            "Dimostrare la congruita' del prezzo tramite perizia di stima (per escludere lo squilibrio oltre 1/4) o la normalita' commerciale del mezzo di pagamento.",
            "Provare la mancanza di conoscenza dello stato di insolvenza (inscientia decoctionis) mediante bilanci in utile, assenza di protesti, regolarita' dei rapporti e affidamenti bancari attivi all'epoca dell'atto.",
            "Valutare in subordine una transazione tombale con il curatore (previa autorizzazione del comitato creditori) per chiudere il rischio a saldo e stralcio."
        ],
        "prove": ["Perizia di valore di mercato del bene compravenduto all'epoca dell'atto", "Visure protesti/pregiudizievoli negative e bilanci pubblicati alla data del pagamento", "Contratti commerciali che giustificano le modalita' di pagamento o la contestualita' della garanzia", "Calcolo esatto del periodo sospetto e della decadenza ex art. 170 CCII"],
        "errori": ["Sottovalutare l'inversione dell'onere della prova nell'art. 166 co. 1 (qui e' il convenuto a dover provare la non conoscenza dell'insolvenza)", "Non verificare il termine di decadenza triennale dell'art. 170 CCII", "Dimenticare di verificare le esenzioni assolute dell'art. 166 co. 3 CCII"]
    },
    {
        "cod": "SOC-097", "slug": "difesa-revocatoria-pagamenti-scaduti-scientia-decoctionis-art-166-co-2",
        "cat": "liquidazione-giudiziale", "cat_lbl": "Liquidazione Giudiziale", "pilastro": "liquidazione-giudiziale-fallimento-opposizioni",
        "titolo": "Difesa da revocatoria di pagamenti di debiti scaduti: contestare la scientia decoctionis (art. 166 co. 2 CCII)",
        "seo_title": "Revocatoria Pagamenti Debiti Scaduti Art. 166 co. 2 CCII: Difesa",
        "desc": "Come difendere un fornitore o creditore citato dal curatore per pagamenti regolari ricevuti nei 6 mesi anteriori: onere della prova sul curatore e difetto di scientia decoctionis.",
        "keywords": ["revocatoria pagamenti debiti scaduti 6 mesi", "scientia decoctionis onere prova curatore", "art 166 comma 2 ccii"],
        "norme": ["Art. 166 co. 2 CCII", "Art. 166 co. 3 lett. a CCII"],
        "scenario": "Un fornitore riceve dal curatore la richiesta di restituire bonifici incassati nei 6 mesi precedenti la domanda di liquidazione giudiziale per fatture regolarmente scadute.",
        "rischio": "Dover restituire soldi gia' incassati per merci o servizi regolarmente forniti mesi prima.",
        "protocollo": [
            "Eccepire anzitutto l'esenzione assoluta dell'art. 166 co. 3 lett. a CCII (pagamenti nell'esercizio dell'attivita' d'impresa nei termini d'uso).",
            "Ricordare che nell'art. 166 co. 2 l'onere di provare la conoscenza effettiva (non mera conoscibilita') dello stato di insolvenza grava integralmente sul curatore.",
            "Smontare gli indici presuntivi allegati dal curatore (un semplice ritardo nei pagamenti o un piano di rientro non prova di per se' la conoscenza dell'insolvenza strutturale).",
            "Verificare l'esatta decorrenza a ritroso dei 6 mesi dalla data di deposito della domanda di liquidazione giudiziale (e non dalla sentenza)."
        ],
        "prove": ["Storico delle fatture e dei tempi medi di pagamento abituali tra le parti", "Estratti di visure e bilanci che non evidenziavano insolvenza conclamata", "Corrispondenza commerciale priva di ammissioni di decozione", "Data esatta dei bonifici rispetto al deposito della domanda di liquidazione"],
        "errori": ["Restituire spontaneamente le somme alla prima diffida del curatore senza verificare l'esenzione termini d'uso", "Non distinguere tra conoscenza effettiva dell'insolvenza e temporanea difficolta' di cassa", "Sbagliare il calcolo dei 6 mesi a ritroso"]
    },
    {
        "cod": "SOC-098", "slug": "esenzione-revocatoria-pagamenti-termini-uso-art-166-co-3",
        "cat": "liquidazione-giudiziale", "cat_lbl": "Liquidazione Giudiziale", "pilastro": "liquidazione-giudiziale-fallimento-opposizioni",
        "titolo": "Esenzione da revocatoria per pagamenti di beni e servizi nei termini d'uso (art. 166 co. 3 lett. a CCII)",
        "seo_title": "Esenzione Revocatoria Termini d'Uso Art. 166 co. 3 lett. a CCII",
        "desc": "Come blindare la difesa del fornitore dimostrando che i pagamenti sono avvenuti con le modalita' e le tempistiche abituali del rapporto commerciale.",
        "keywords": ["esenzione revocatoria termini d uso", "art 166 comma 3 lettera a ccii", "difesa fornitore revocatoria fallimentare"],
        "norme": ["Art. 166 co. 3 lett. a CCII"],
        "scenario": "Il curatore chiede la revoca dei pagamenti effettuati al fornitore negli ultimi 6 mesi, contestando che sono avvenuti con qualche settimana di ritardo rispetto alla scadenza in fattura.",
        "rischio": "Una lettura formalistica della scadenza in fattura porterebbe a revocare pagamenti perfettamente normali nella prassi tra le parti.",
        "protocollo": [
            "Ricostruire la prassi consolidata tra le parti negli anni precedenti: per la giurisprudenza di legittimita' i 'termini d'uso' si riferiscono alle modalita' e ai tempi abitualmente praticati in concreto tra quel fornitore e quel cliente.",
            "Dimostrare che anche negli esercizi in bonis le fatture venivano pagate con lo stesso mezzo (bonifico/RIBA) e con analoga tolleranza di giorni.",
            "Escludere ogni azione coattiva, decreto ingiuntivo o pressione anomala che interrompa la fisiologia dei pagamenti.",
            "Eccepire l'esenzione assoluta ex art. 166 co. 3 lett. a CCII come difesa tranchant."
        ],
        "prove": ["Partitario clienti-fornitori storico degli ultimi 2-3 anni", "Tabella comparativa dei giorni medi di incasso ante e intra periodo sospetto", "Fatture e contabili bancarie che confermano mezzi di pagamento ordinari", "Assenza di atti esecutivi o solleciti giudiziali"],
        "errori": ["Limitarsi a guardare la data di scadenza stampata sulla fattura senza produrre lo storico reale degli incassi", "Non provare la regolarita' delle modalita' di pagamento (es. bonifico vs assegni di terzi)", "Includere nella difesa pagamenti ottenuti tramite pignoramento (che non sono nei termini d'uso)"]
    },
    {
        "cod": "SOC-099", "slug": "difesa-revocatoria-rimesse-conto-corrente-bancario-art-166-co-3-b",
        "cat": "liquidazione-giudiziale", "cat_lbl": "Liquidazione Giudiziale", "pilastro": "liquidazione-giudiziale-fallimento-opposizioni",
        "titolo": "Revocatoria delle rimesse in conto corrente bancario e limite del rientro durevole (art. 166 co. 3 lett. b e 171 CCII)",
        "seo_title": "Revocatoria Rimesse Bancarie Art. 166 co. 3 lett. b e Art. 171 CCII",
        "desc": "Come difendersi (o calcolare esattamente l'importo) nelle revocatorie su conto corrente: requisito della riduzione durevole dell'esposizione e tetto massimo della differenza tra massimo scoperto e saldo finale.",
        "keywords": ["revocatoria rimesse bancarie art 166", "riduzione durevole esposizione bancaria", "art 171 comma 3 ccii massimo scoperto"],
        "norme": ["Art. 166 co. 3 lett. b CCII", "Art. 171 co. 3 CCII"],
        "scenario": "Il curatore agisce contro la banca (o verifica i conti) per revocare le rimesse affluite sul conto corrente affidato nei 6 mesi anteriori alla liquidazione giudiziale.",
        "rischio": "Conteggi errati che sommano tutte le rimesse in entrata senza verificare la durevolezza della riduzione e il tetto dell'art. 171 co. 3 generano richieste gonfiate.",
        "protocollo": [
            "Applicare la regola del saldo disponibile e verificare quali singole rimesse hanno ridotto in maniera effettivamente 'durevole' l'esposizione debitoria della societa' verso la banca.",
            "Applicare il limite quantitativo inderogabile dell'art. 171 co. 3 CCII: la banca non puo' essere condannata a restituire piu' della differenza tra l'ammontare massimo delle sue pretese nel periodo sospetto e l'ammontare residuo alla data di apertura della procedura (regola del massimo scoperto).",
            "Verificare il difetto di scientia decoctionis della banca nel periodo di riferimento.",
            "Affidare la ricostruzione matematica a un consulente tecnico bancario-contabile."
        ],
        "prove": ["Estratti conto integrali e scalari degli ultimi 12 mesi ante procedura", "Contratti di apertura di credito e fidi tempo per tempo vigenti", "Perizia econometrica sul saldo disponibile, durevolezza e differenza massimo scoperto", "Documentazione istruttoria fidi e Centrale Rischi"],
        "errori": ["Sommare meccanicamente tutti i bonifici in entrata senza verificare i successivi utilizzi del fido", "Dimenticare il tetto del massimo scoperto ex art. 171 co. 3 CCII", "Confondere saldo contabile, saldo per valuta e saldo disponibile"]
    },
    {
        "cod": "SOC-100", "slug": "azione-revocatoria-ordinaria-curatore-art-165-ccii-2901-cc",
        "cat": "liquidazione-giudiziale", "cat_lbl": "Liquidazione Giudiziale", "pilastro": "liquidazione-giudiziale-fallimento-opposizioni",
        "titolo": "Difesa dall'azione revocatoria ordinaria esercitata dal curatore (art. 165 CCII e art. 2901 c.c.)",
        "seo_title": "Revocatoria Ordinaria del Curatore Art. 165 CCII e Art. 2901 c.c.",
        "desc": "Come difendere vendite immobiliari, cessioni d'azienda, scissioni o atti dispositivi compiuti fino a 5 anni prima dalla revocatoria ordinaria del curatore.",
        "keywords": ["revocatoria ordinaria curatore art 165 ccii", "art 2901 cc fallimento 5 anni", "difesa acquirente immobile revocatoria"],
        "norme": ["Art. 165 CCII", "Art. 2901 c.c.", "Art. 2903 c.c."],
        "scenario": "Il curatore, non potendo usare la revocatoria concorsuale per superamento del periodo sospetto di 6/12 mesi, agisce in revocatoria ordinaria (fino a 5 anni indietro) su vendite di immobili, rami d'azienda o garanzie.",
        "rischio": "Dichiarazione di inefficacia dell'acquisto rispetto alla massa dei creditori con pignoramento e vendita forzata del bene acquistato dal terzo.",
        "protocollo": [
            "Verificare la prescrizione quinquennale dalla data dell'atto (o dalla trascrizione per gli immobili) ex art. 2903 c.c.",
            "Contestare l'eventus damni dimostrando che il prezzo incassato era congruo ed e' stato destinato a pagare debiti aziendali scaduti o a mantenere l'operativita' (nessun depauperamento della garanzia).",
            "Per gli atti a titolo oneroso, contestare la prova rigorosa della participatio fraudis del terzo acquirente (consapevolezza del pregiudizio ai creditori) e verificare la presenza di creditori anteriori effettivamente lesi.",
            "Invocare la protezione dei pagamenti di debiti scaduti (esenti da revocatoria ordinaria ex art. 2901 co. 3 c.c.)."
        ],
        "prove": ["Atto notarile di compravendita e data di trascrizione", "Perizia di congruita' del prezzo pagato e tracciabilita' integrale del pagamento", "Prove dell'utilizzo del corrispettivo per estinguere debiti aziendali o investimenti", "Assenza di rapporti di parentela o collusione tra venditore e acquirente"],
        "errori": ["Pensare che dopo 1 anno dall'atto si sia al sicuro da ogni revocatoria (l'ordinaria arriva a 5 anni)", "Pagare il prezzo con compensazioni opache o senza tracciabilita' bancaria", "Non eccepire l'art. 2901 co. 3 c.c. quando l'atto estingueva un debito scaduto"]
    }
]
