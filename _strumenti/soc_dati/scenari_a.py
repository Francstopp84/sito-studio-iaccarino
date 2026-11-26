# -*- coding: utf-8 -*-
"""Scenari operativi e protocolli di difesa SOC-001 -> SOC-050 (Governance & Soci 20, Modello 231 25, Crisi 5)."""

SCENARI_A = [
    # ═══════════════════ 1. GOVERNANCE & SOCI (001-020) ═══════════════════
    {
        "cod": "SOC-001", "slug": "stallo-assembleare-soci-50-50-deadlock-srl",
        "cat": "governance-soci", "cat_lbl": "Governance & Soci", "pilastro": "diritto-societario-governance-srl-spa",
        "titolo": "Stallo assembleare tra due soci al 50% (deadlock): come sbloccare la S.r.l.",
        "seo_title": "Stallo Assembleare Soci 50 e 50 S.r.l.: Soluzioni e Scioglimento",
        "desc": "Protocollo operativo in caso di paralisi decisionale tra soci paritetici: revoca amministratore, clausole anti-deadlock, mediazione, art. 2484 c.c. e liquidazione giudiziale del liquidatore.",
        "keywords": ["stallo assembleare 50 50", "deadlock srl", "impossibilita funzionamento assemblea art 2484"],
        "norme": ["Art. 2484 co. 1 n. 3 c.c.", "Art. 2487 c.c.", "Art. 2476 c.c."],
        "scenario": "Due soci titolari ciascuno del 50% di una S.r.l. non riescono piu' ad approvare il bilancio ne' a nominare o sostituire l'organo amministrativo, bloccando l'operativita' aziendale.",
        "rischio": "La paralisi prolungata distrugge il valore dell'avviamento, espone a sanzioni per mancato deposito bilanci e conduce allo scioglimento della societa' per impossibilita' di funzionamento dell'assemblea (art. 2484 n. 3 c.c.).",
        "protocollo": [
            "Verificare nello statuto e nei patti parasociali la presenza di clausole anti-stallo (russian roulette, texas shoot-out, opzione put/call).",
            "Formalizzare la convocazione dell'assemblea su punti decisivi (bilancio, rinnovo cariche) per documentare oggettivamente il blocco reiterato.",
            "Attivare una trattativa strutturata di separazione (acquisto quota o scissione asimmetrica) supportata da perizia indipendente.",
            "In caso di persistente ostruzionismo, chiedere al Tribunale l'accertamento della causa di scioglimento e la nomina di un liquidatore giudiziale ex art. 2487 c.c."
        ],
        "prove": ["Verbali di assemblee andate deserte o concluse senza maggioranza", "Statuto e patti parasociali vigenti", "Bilanci e situazione finanziaria aggiornata", "Corrispondenza PEC di convocazione e proposte transattive"],
        "errori": ["Lasciare che un socio gestisca la societa' di fatto senza approvazione dei conti", "Aprire una societa' concorrente stornando clienti prima della definizione della lite", "Ritardare l'intervento finche' la banca revoca i fidi per mancato deposito del bilancio"]
    },
    {
        "cod": "SOC-002", "slug": "impugnazione-delibera-approvazione-bilancio-falso-irregolare",
        "cat": "governance-soci", "cat_lbl": "Governance & Soci", "pilastro": "contenzioso-soci-patti-parasociali-recesso",
        "titolo": "Impugnazione della delibera di approvazione del bilancio non veritiero o irregolare",
        "seo_title": "Impugnazione Bilancio S.r.l. e S.p.A.: Nullita' e Termini",
        "desc": "Come impugnare davanti al Tribunale delle Imprese un bilancio privo di chiarezza, verita' e correttezza: art. 2423 c.c., limite dell'art. 2434-bis c.c. e interesse ad agire.",
        "keywords": ["impugnazione bilancio srl", "bilancio falso nullita delibera", "art 2434 bis codice civile"],
        "norme": ["Art. 2423 c.c.", "Art. 2379 c.c.", "Art. 2434-bis c.c."],
        "scenario": "Un socio di minoranza riscontra poste gonfiate, crediti inesigibili non svalutati, ricavi omessi o mancata chiarezza nella nota integrativa del bilancio approvato dalla maggioranza.",
        "rischio": "La delibera di approvazione del bilancio non puo' piu' essere impugnata dopo che e' avvenuta l'approvazione del bilancio dell'esercizio successivo (art. 2434-bis c.c.).",
        "protocollo": [
            "Esercitare subito il diritto di ispezione ex art. 2476 co. 2 c.c. (nella S.r.l.) per acquisire mastrini, fatture e documentazione di supporto alle poste dubbie.",
            "Far redigere una perizia contabile di parte che dimostri violazioni concrete e rilevanti dei principi di chiarezza, verita' e correttezza (art. 2423 c.c.).",
            "Notificare atto di citazione dinanzi al Tribunale delle Imprese prima dell'approvazione del bilancio dell'esercizio successivo.",
            "Valutare in parallelo la denuncia ex art. 2409 c.c. o la tutela penale per false comunicazioni sociali (art. 2621 c.c.) nei casi di frode grave."
        ],
        "prove": ["Fascicolo integrale di bilancio (SP, CE, nota integrativa, relazione gestione)", "Verbale assembleare di approvazione con voto contrario o astensione", "Mastrini contabili e perizia tecnica di parte", "Eventuali rilievi del collegio sindacale o del revisore"],
        "errori": ["Aspettare l'approvazione del bilancio dell'anno successivo perdendo la legittimazione", "Contestare errori contabili marginali privi di interesse concreto ad agire", "Non verificare la clausola compromissoria arbitrale eventualmente presente in statuto"]
    },
    {
        "cod": "SOC-003", "slug": "impugnazione-delibera-assembleare-annullabile-90-giorni",
        "cat": "governance-soci", "cat_lbl": "Governance & Soci", "pilastro": "contenzioso-soci-patti-parasociali-recesso",
        "titolo": "Impugnazione di delibera assembleare annullabile e sospensione cautelare entro 90 giorni",
        "seo_title": "Impugnazione Delibera Assembleare 90 Giorni e Sospensione",
        "desc": "Come impugnare delibere viziate per conflitto di interessi, abuso di maggioranza o vizi di convocazione davanti al Tribunale delle Imprese entro il termine perentorio di 90 giorni.",
        "keywords": ["impugnazione delibera assembleare 90 giorni", "art 2479 ter cc", "sospensione cautelare delibera"],
        "norme": ["Art. 2377 c.c.", "Art. 2378 c.c.", "Art. 2479-ter c.c."],
        "scenario": "L'assemblea adotta a maggioranza una delibera lesiva (es. compensi sproporzionati, trasferimento sede o operazione in conflitto di interessi) senza rispettare la legge o lo statuto.",
        "rischio": "Decorso il termine perentorio di 90 giorni dalla trascrizione nel libro delle decisioni dei soci (o dall'iscrizione nel Registro delle Imprese), la delibera annullabile diventa definitiva.",
        "protocollo": [
            "Accertare la data esatta della delibera e della trascrizione/iscrizione per calcolare il termine di 90 giorni.",
            "Verificare se lo statuto prevede una clausola arbitrale societaria o la competenza del Tribunale delle Imprese.",
            "Notificare citazione di impugnazione accompagnata da ricorso cautelare ex art. 2378 co. 3 c.c. per sospendere subito gli effetti della delibera.",
            "Dimostrare il pregiudizio grave e irreparabile comparato rispetto all'interesse della societa' alla pronta esecuzione."
        ],
        "prove": ["Avviso di convocazione e prova della data di ricezione", "Verbale integrale dell'assemblea e deleghe di voto", "Visura camerale e copia libro decisioni dei soci", "Documentazione del conflitto di interessi o abuso della maggioranza"],
        "errori": ["Votare a favore in assemblea perdendo la legittimazione a impugnare", "Proporre l'istanza di sospensione cautelare prima di aver notificato la causa di merito", "Confondere la data dell'assemblea con la data di trascrizione o iscrizione"]
    },
    {
        "cod": "SOC-004", "slug": "delibera-assembleare-nulla-mancata-convocazione-oggetto-illecito",
        "cat": "governance-soci", "cat_lbl": "Governance & Soci", "pilastro": "contenzioso-soci-patti-parasociali-recesso",
        "titolo": "Delibera assembleare nulla per mancata convocazione, mancanza di verbale o oggetto illecito",
        "seo_title": "Delibera Assembleare Nulla: Mancata Convocazione e Termine 3 Anni",
        "desc": "Quando una delibera societaria e' nulla ex artt. 2379 e 2479-ter c.c., chi puo' impugnarla entro 3 anni e quali vizi sono rilevabili senza limiti di tempo.",
        "keywords": ["delibera assembleare nulla", "mancata convocazione assemblea srl", "art 2379 codice civile"],
        "norme": ["Art. 2379 c.c.", "Art. 2379-bis c.c.", "Art. 2479-ter co. 3 c.c."],
        "scenario": "Un socio scopre che l'assemblea ha deliberato operazioni straordinarie o modifiche statutarie senza averlo mai convocato o con un oggetto contrario a norme imperative.",
        "rischio": "La delibera produce comunque effetti verso i terzi in buona fede se non viene tempestivamente sospesa e dichiarata nulla entro il termine di 3 anni.",
        "protocollo": [
            "Verificare se vi e' stata assoluta mancanza di informazione (nullita' 3 anni) oppure mera irregolarita' della convocazione (annullabilita' 90 giorni).",
            "Controllare che non ricorra la sanatoria dell'art. 2379-bis c.c. (dichiarazione di assenso allo svolgimento dell'assemblea).",
            "Agire davanti al Tribunale delle Imprese chiedendo l'accertamento della nullita' e la sospensione cautelare.",
            "Richiedere la cancellazione dell'iscrizione della delibera nulla dal Registro delle Imprese."
        ],
        "prove": ["PEC o raccomandate omesse e registro protocollo", "Verbale depositato presso il Registro delle Imprese", "Statuto sociale con le modalita' obbligatorie di convocazione", "Atti esecutivi eventualmente posti in essere sulla base della delibera"],
        "errori": ["Dare assenso scritto o partecipare senza opporsi alla trattazione sanando il vizio", "Lasciar trascorrere il triennio dalla trascrizione", "Non agire in via cautelare mentre vengono ceduti beni sociali"]
    },
    {
        "cod": "SOC-005", "slug": "diritto-controllo-accesso-atti-socio-srl-art-2476",
        "cat": "governance-soci", "cat_lbl": "Governance & Soci", "pilastro": "contenzioso-soci-patti-parasociali-recesso",
        "titolo": "Diritto di controllo e accesso integrale ai documenti del socio di S.r.l. (art. 2476 co. 2 c.c.)",
        "seo_title": "Diritto di Accesso Atti Socio S.r.l. Art. 2476 c.c. e Ricorso 700",
        "desc": "Come ottenere fatture, estratti conto bancari, contratti e libri sociali quando l'amministratore nega l'accesso al socio non amministratore di S.r.l.",
        "keywords": ["accesso atti socio srl art 2476", "ricorso 700 esibizione documenti sociali", "controllo socio non amministratore"],
        "norme": ["Art. 2476 co. 2 c.c.", "Art. 700 c.p.c.", "Art. 2625 c.c."],
        "scenario": "L'amministratore di una S.r.l. rifiuta o dilaziona la consegna di estratti conto, contratti, fatture e mastrini richiesti dal socio non amministratore.",
        "rischio": "Senza accesso rapido ai documenti, il socio non puo' accertare eventuali distrazioni, conflitti di interesse o la reale situazione patrimoniale prima che il patrimonio venga svuotato.",
        "protocollo": [
            "Inviare diffida formale via PEC indicando puntualmente i documenti richiesti, il professionista di fiducia incaricato e una data per l'accesso in sede.",
            "Escludere ogni pretesto di riservatezza opponibile salvo casi eccezionali di socio in diretta concorrenza sleale (gestibili con oscuramento selettivo).",
            "In caso di rifiuto o silenzio, depositare ricorso d'urgenza ex art. 700 c.p.c. davanti al Tribunale delle Imprese con richiesta di astreinte (penale giornaliera art. 614-bis c.p.c.).",
            "Valutare la segnalazione per impedito controllo (art. 2625 c.c.) e la revoca dell'amministratore."
        ],
        "prove": ["Visura camerale attestante la qualifica di socio non amministratore", "PEC di richiesta accesso atti e risposte dilatorie o negative", "Lettera di incarico al commercialista o avvocato di fiducia", "Eventuali indizi di gestione opaca o irregolare"],
        "errori": ["Presentarsi in sede senza preavviso scritto ne' tracciamento PEC", "Usare i documenti acquisiti per fare concorrenza sleale alla societa'", "Accontentarsi del solo bilancio sintetico rinunciando a estratti conto e fatture"]
    },
    {
        "cod": "SOC-006", "slug": "revoca-cautelare-amministratore-srl-gravi-irregolarita",
        "cat": "governance-soci", "cat_lbl": "Governance & Soci", "pilastro": "contenzioso-soci-patti-parasociali-recesso",
        "titolo": "Revoca cautelare giudiziale dell'amministratore di S.r.l. per gravi irregolarita'",
        "seo_title": "Revoca Cautelare Amministratore S.r.l. Art. 2476 co. 3 c.c.",
        "desc": "Come ottenere in via d'urgenza dal Tribunale delle Imprese la revoca dell'amministratore che distrae fondi, viola gli obblighi contabili o agisce in conflitto di interessi.",
        "keywords": ["revoca cautelare amministratore srl", "art 2476 comma 3 codice civile", "gravi irregolarita amministratore"],
        "norme": ["Art. 2476 co. 3 c.c.", "Art. 669-bis ss. c.p.c.", "Art. 2409 c.c."],
        "scenario": "Un socio di S.r.l. accerta che l'amministratore sta distraendo liquidita', omettendo il pagamento di imposte o compiendo atti in conflitto di interessi a danno della societa'.",
        "rischio": "Attendere i tempi di una causa ordinaria consentirebbe all'amministratore infedele di completare lo svuotamento del patrimonio aziendale.",
        "protocollo": [
            "Raccogliere prove documentali certe delle gravi irregolarita' gestionali (estratti conto, contratti anomali, mancata tenuta contabilita', omesso versamento tributi).",
            "Proporre ricorso cautelare ante causam (o in corso di causa) ex art. 2476 co. 3 c.c. davanti al Tribunale delle Imprese chiedendo la revoca immediata.",
            "Valutare il cumulo con la richiesta di sequestro conservativo sui beni personali dell'amministratore per garantire il risarcimento.",
            "Coordinare l'azione con la convocazione assembleare per la nomina del nuovo organo amministrativo o con il procedimento ex art. 2409 c.c."
        ],
        "prove": ["Documentazione bancaria e contabile delle operazioni irregolari", "Esito dell'ispezione ex art. 2476 co. 2 c.c.", "Verbali assembleari e statuto", "Perizia tecnica di quantificazione del danno attuale o imminente"],
        "errori": ["Fondare il ricorso cautelare su mere divergenze imprenditoriali anziche' su gravi irregolarita' provate", "Dimenticare di instaurare il giudizio di merito se richiesto dal regime cautelare", "Non prevedere subito come sostituire l'amministratore revocato"]
    },
    {
        "cod": "SOC-007", "slug": "denuncia-tribunale-gravi-irregolarita-art-2409-cc",
        "cat": "governance-soci", "cat_lbl": "Governance & Soci", "pilastro": "contenzioso-soci-patti-parasociali-recesso",
        "titolo": "Denuncia al Tribunale per gravi irregolarita' gestionali (art. 2409 c.c.) e ispezione",
        "seo_title": "Denuncia Tribunale Gravi Irregolarita' Art. 2409 c.c. | S.r.l. e S.p.A.",
        "desc": "Procedura ex art. 2409 c.c. applicabile sia a S.p.A. sia a S.r.l.: quorum del 10%, ispezione giudiziale, revoca organi e nomina di amministratore giudiziario.",
        "keywords": ["denuncia tribunale art 2409 cc", "amministratore giudiziario srl", "ispezione giudiziale societa"],
        "norme": ["Art. 2409 c.c.", "Art. 2477 co. 6 c.c.", "Art. 2086 co. 2 c.c."],
        "scenario": "Soci che rappresentano almeno il 10% del capitale (o l'organo di controllo) hanno fondato sospetto di gravi irregolarita' gestionali potenzialmente dannose per la societa' o le controllate.",
        "rischio": "La prosecuzione della gestione irregolare, inclusa la totale mancanza di adeguati assetti ex art. 2086 c.c., puo' trascinare la societa' in insolvenza irreversibile.",
        "protocollo": [
            "Verificare il raggiungimento della soglia di legittimazione (10% del capitale in S.r.l. e S.p.A. chiuse; 5% in S.p.A. aperte; oppure iniziativa del collegio sindacale).",
            "Depositare ricorso di volontaria giurisdizione ex art. 2409 c.c. davanti al Tribunale delle Imprese dettagliando le violazioni e il danno potenziale.",
            "Chiedere l'ordine di ispezione giudiziale dell'amministrazione e, nei casi piu' gravi, la revoca di amministratori e sindaci con nomina di un amministratore giudiziario.",
            "Monitorare l'eventuale sostituzione spontanea degli organi sociali con soggetti di adeguata professionalita' per sospendere la procedura."
        ],
        "prove": ["Visura camerale attestante la quota >= 10%", "Bilanci, atti gestori irregolari, omessi versamenti o assenza di adeguati assetti", "Segnalazioni dell'organo di controllo o del revisore", "Diffide rimaste senza esito"],
        "errori": ["Denunciare fatti ormai esauriti che non producono piu' danno attuale alla societa'", "Usare l'art. 2409 c.c. per risolvere liti meramente personali tra soci", "Non considerare le spese dell'ispezione poste a carico dei ricorrenti in caso di infondatezza"]
    },
    {
        "cod": "SOC-008", "slug": "recesso-socio-srl-spa-valutazione-liquidazione-quota",
        "cat": "governance-soci", "cat_lbl": "Governance & Soci", "pilastro": "contenzioso-soci-patti-parasociali-recesso",
        "titolo": "Recesso del socio di S.r.l. o S.p.A. e contestazione della liquidazione della quota",
        "seo_title": "Recesso Socio S.r.l. e Valutazione Quota Art. 2473 c.c.",
        "desc": "Quando spetta il diritto di recesso legale o statutario, termini di comunicazione, determinazione del valore di mercato della quota e nomina di esperto del Tribunale.",
        "keywords": ["recesso socio srl art 2473", "valutazione quota recesso valore mercato", "liquidazione quota socio receduto"],
        "norme": ["Art. 2473 c.c.", "Art. 2437 c.c.", "Art. 2437-ter c.c."],
        "scenario": "Un socio dissenziente rispetto a una modifica rilevante dell'oggetto sociale, fusione, trasferimento sede all'estero o societa' a tempo indeterminato intende recedere e ottenere il giusto valore della quota.",
        "rischio": "La maggioranza tenta spesso di liquidare la quota al mero patrimonio netto contabile, azzerando avviamento e plusvalenze reali.",
        "protocollo": [
            "Verificare la causa legittimante di recesso (legale o statutaria) e il termine perentorio per l'invio della dichiarazione (15 giorni dall'iscrizione o 30 giorni dalla conoscenza del fatto).",
            "Inviare la dichiarazione di recesso via PEC/raccomandata con formale richiesta di liquidazione a valore di mercato (art. 2473 co. 3 c.c.).",
            "In caso di disaccordo sulla stima degli amministratori, chiedere al Tribunale la nomina di un esperto indipendente ex art. 1349 c.c.",
            "Monitorare il termine di 180 giorni per il pagamento della quota e agire in via monitoria/esecutiva se la societa' non liquida."
        ],
        "prove": ["Statuto vigente e visura camerale", "Delibera legittimante il recesso e prova del dissenso/assenza", "PEC di esercizio del recesso nei termini", "Perizia di valutazione d'azienda inclusiva di avviamento e immobili a valore corrente"],
        "errori": ["Inviare il recesso fuori termine decadendo dal diritto", "Accettare la valutazione contabile senza contestarla formalmente", "Non verificare se la societa' ha revocato la delibera entro 90 giorni rendendo inefficace il recesso"]
    },
    {
        "cod": "SOC-009", "slug": "esclusione-socio-srl-giusta-causa-opposizione",
        "cat": "governance-soci", "cat_lbl": "Governance & Soci", "pilastro": "contenzioso-soci-patti-parasociali-recesso",
        "titolo": "Esclusione del socio di S.r.l. per giusta causa statutaria e difesa contro esclusione abusiva",
        "seo_title": "Esclusione Socio S.r.l. Art. 2473-bis c.c.: Difesa e Opposizione",
        "desc": "Presupposti di legittimita' dell'esclusione del socio nella S.r.l. (art. 2473-bis c.c.), divieto di clausole generiche, opposizione cautelare e diritto alla liquidazione della quota.",
        "keywords": ["esclusione socio srl art 2473 bis", "opposizione esclusione socio", "giusta causa esclusione srl"],
        "norme": ["Art. 2473-bis c.c.", "Art. 2473 c.c.", "Art. 2287 c.c."],
        "scenario": "La maggioranza delibera l'esclusione di un socio contestando inadempimenti o concorrenza, oppure la societa' deve estromettere un socio gravemente inadempiente.",
        "rischio": "Una clausola statutaria generica di esclusione e' nulla; d'altro canto, il socio escluso rischia di perdere subito i diritti amministrativi se non ottiene la sospensione cautelare.",
        "protocollo": [
            "Verificare nello statuto se la specifica ipotesi di giusta causa e' tipizzata in modo determinato ex art. 2473-bis c.c.",
            "Controllare il rispetto rigoroso della procedura di contestazione, convocazione e motivazione della delibera.",
            "Se si difende il socio escluso, proporre opposizione/impugnazione con istanza cautelare di sospensione davanti al Tribunale delle Imprese.",
            "In ogni caso verificare la corretta liquidazione della quota a valore di mercato (escluso il rimborso mediante riduzione del capitale sociale)."
        ],
        "prove": ["Statuto sociale con clausola di esclusione", "Delibera di esclusione e lettera di comunicazione", "Prove documentali a confutazione o conferma dell'inadempimento contestato", "Situazione patrimoniale per eventuale liquidazione"],
        "errori": ["Deliberare l'esclusione senza una specifica clausola statutaria preventiva", "Pretendere di azzerare il valore della quota del socio escluso come sanzione", "Non rispettare il termine breve di opposizione"]
    },
    {
        "cod": "SOC-010", "slug": "violazione-patti-parasociali-sindacato-voto-blocco",
        "cat": "governance-soci", "cat_lbl": "Governance & Soci", "pilastro": "diritto-societario-governance-srl-spa",
        "titolo": "Violazione dei patti parasociali (sindacato di voto, blocco e governance): tutele e penali",
        "seo_title": "Violazione Patti Parasociali: Risarcimento, Penali e Art. 2341-bis",
        "desc": "Come tutelarsi quando un socio viola il patto parasociale su voto, nomina amministratori o trasferimento quote: efficacia obbligatoria, penali e risoluzione.",
        "keywords": ["violazione patti parasociali", "sindacato di voto art 2341 bis", "clausola penale patto parasociale"],
        "norme": ["Art. 2341-bis c.c.", "Art. 2341-ter c.c.", "Art. 1382 c.c."],
        "scenario": "Un socio vota in assemblea in modo difforme dal sindacato di voto oppure cede la partecipazione violando un patto di blocco o di co-vendita.",
        "rischio": "Poiche' i patti parasociali hanno efficacia meramente obbligatoria tra i firmatari, la delibera votata in violazione del patto resta generalmente valida verso la societa', rendendo cruciali penali e risarcimento.",
        "protocollo": [
            "Verificare la durata e la validita' del patto (limite quinquennale ex art. 2341-bis c.c. per le S.p.A. o diritto di recesso con preavviso di 180 giorni se a tempo indeterminato).",
            "Contestare immediatamente via PEC l'inadempimento azionando eventuali clausole penali o opzioni call punitive previste nel patto.",
            "Quantificare il danno risarcibile subito dagli altri paciscenti e valutare l'azione giudiziale o arbitrale.",
            "Valutare il trasferimento delle clausole chiave (prelazione, gradimento, quorum) direttamente nello statuto per ottenere efficacia reale."
        ],
        "prove": ["Testo integrale del patto parasociale sottoscritto", "Verbale assembleare o atto notarile di cessione quote in violazione", "Diffide PEC e documentazione del danno economico", "Statuto sociale"],
        "errori": ["Impugnare la delibera sociale pensando che il patto parasociale abbia efficacia reale come lo statuto", "Sottoscrivere patti parasociali privi di clausola penale o meccanismi di esecuzione", "Ignorare il limite massimo di durata quinquennale"]
    },
    {
        "cod": "SOC-011", "slug": "aumento-capitale-sociale-diluitivo-abuso-maggioranza",
        "cat": "governance-soci", "cat_lbl": "Governance & Soci", "pilastro": "contenzioso-soci-patti-parasociali-recesso",
        "titolo": "Aumento di capitale sociale diluitivo e abuso di maggioranza ai danni del socio di minoranza",
        "seo_title": "Aumento Capitale Diluitivo e Abuso di Maggioranza | Difesa Socio",
        "desc": "Come difendersi da un aumento di capitale deliberato al solo scopo di annacquare la quota del socio di minoranza: impugnazione per abuso di potere e diritto di opzione.",
        "keywords": ["aumento capitale diluitivo abuso maggioranza", "annacquamento quota socio minoranza", "diritto opzione sottoscrizione"],
        "norme": ["Art. 2481-bis c.c.", "Art. 2441 c.c.", "Art. 1375 c.c."],
        "scenario": "La maggioranza delibera un aumento di capitale ingiustificato, senza reale fabbisogno finanziario e con esclusione del sovrapprezzo o termini stretti, per diluire il socio di minoranza privo di liquidita'.",
        "rischio": "La quota del socio di minoranza viene ridotta a percentuali irrisorie, facendogli perdere poteri di controllo (es. soglia 10% art. 2409 c.c.) e quota parte del valore reale dell'azienda.",
        "protocollo": [
            "Analizzare i bilanci e la cassa per verificare se la societa' avesse reale bisogno di nuovi capitali o se l'operazione e' puramente pretestuosa.",
            "Controllare la congruita' del prezzo di emissione rispetto al valore economico reale della societa' (assenza di sovrapprezzo) e il rispetto del diritto di opzione.",
            "Impugnare la delibera entro 90 giorni per abuso di maggioranza (violazione di buona fede ex art. 1375 c.c.) chiedendo la sospensione cautelare.",
            "Valutare in alternativa l'esercizio del recesso ex art. 2481-bis c.c. quando l'aumento e' offerto a terzi."
        ],
        "prove": ["Verbale di assemblea straordinaria di aumento capitale", "Situazione patrimoniale e liquidita' aziendale pre-aumento", "Perizia di valutazione del valore reale delle quote vs valore nominale", "Corrispondenza tra soci che rivela l'intento espulsivo"],
        "errori": ["Lasciare decorrere i 90 giorni senza impugnare ne' sospendere la delibera", "Non contestare la mancanza di sovrapprezzo in presenza di ingenti riserve o avviamento", "Sottoscrivere senza riserve se si intende contestare l'abuso"]
    },
    {
        "cod": "SOC-012", "slug": "mancata-distribuzione-utili-abuso-maggioranza-srl",
        "cat": "governance-soci", "cat_lbl": "Governance & Soci", "pilastro": "contenzioso-soci-patti-parasociali-recesso",
        "titolo": "Mancata distribuzione sistematica degli utili per estromettere il socio di minoranza",
        "seo_title": "Mancata Distribuzione Utili S.r.l.: Quando e' Abuso di Maggioranza",
        "desc": "Quando il sistematico accantonamento a riserva degli utili mentre la maggioranza incassa alti compensi integra abuso di maggioranza impugnabile davanti al Tribunale delle Imprese.",
        "keywords": ["mancata distribuzione utili srl", "abuso maggioranza accantonamento riserve", "diritto agli utili socio minoranza"],
        "norme": ["Art. 2433 c.c.", "Art. 2478-bis c.c.", "Art. 1375 c.c."],
        "scenario": "Per molti esercizi consecutivi la societa' produce utili cospicui che la maggioranza accantona sistematicamente a riserva senza piani di investimento, mentre i soci di maggioranza prelevano ingenti compensi come amministratori.",
        "rischio": "Il socio di minoranza viene 'affamato' (freeze-out) e costretto a vendere la propria quota sottocosto.",
        "protocollo": [
            "Ricostruire la serie storica di bilanci, riserve accumulate, liquidita' in cassa e compensi percepiti dagli amministratori soci di maggioranza.",
            "Verbalizzare in assemblea domande puntuali sull'effettiva destinazione delle riserve e votare contro l'accantonamento immotivato.",
            "Impugnare la delibera di destinazione dell'utile entro 90 giorni per eccesso di potere e abuso della regola di maggioranza.",
            "Utilizzare l'impugnazione e l'accesso agli atti ex art. 2476 c.c. come leva per ottenere la distribuzione o una way-out equa."
        ],
        "prove": ["Bilanci degli ultimi 3-5 esercizi con andamento utili e riserve", "Delibere di attribuzione compensi agli amministratori", "Verbali assembleari con richieste di spiegazione rimaste inevase", "Estratti conto e inesistenza di piani di investimento reali"],
        "errori": ["Pensare che il socio di S.r.l. abbia un diritto automatico al dividendo ogni anno (occorre provare l'abuso sistematico)", "Non far verbalizzare il proprio dissenso motivato in assemblea", "Trascurare il parallelo profilo dei compensi sproporzionati agli amministratori"]
    },
    {
        "cod": "SOC-013", "slug": "compensi-sproporzionati-amministratori-conflitto-interessi",
        "cat": "governance-soci", "cat_lbl": "Governance & Soci", "pilastro": "responsabilita-amministratori-sindaci-azioni",
        "titolo": "Compensi sproporzionati agli amministratori e voto in conflitto di interessi",
        "seo_title": "Compensi Sproporzionati Amministratori: Impugnazione e Responsabilita'",
        "desc": "Come contestare delibere con cui il socio-amministratore di maggioranza si attribuisce compensi esorbitanti svuotando la societa': art. 2373, art. 2479-ter e danno sociale.",
        "keywords": ["compensi sproporzionati amministratore", "voto conflitto interessi compenso", "impugnazione delibera compenso amministratore"],
        "norme": ["Art. 2373 c.c.", "Art. 2389 c.c.", "Art. 2479-ter co. 2 c.c."],
        "scenario": "Il socio di maggioranza, anche amministratore unico, delibera con il proprio voto determinante compensi o TFM del tutto sproporzionati rispetto al fatturato, agli utili e alla dimensione aziendale.",
        "rischio": "La cassa aziendale viene prosciugata a beneficio esclusivo dell'amministratore, azzerando utili, patrimonio e garanzie per soci e creditori (con rischi persino penali in caso di crisi).",
        "protocollo": [
            "Confrontare il compenso deliberato con i margini operativi, l'EBITDA, i parametri di mercato e gli esercizi precedenti.",
            "Impugnare la delibera entro 90 giorni per conflitto di interessi del socio-amministratore (voto determinante e danno potenziale alla societa').",
            "Agire per la restituzione delle somme indebitamente percepite e per il risarcimento del danno ex art. 2476 c.c.",
            "Verificare anche la deducibilita' fiscale contestabile dall'Agenzia delle Entrate per antieconomicita'."
        ],
        "prove": ["Delibera assembleare di determinazione compenso e TFM", "Bilanci e conto economico comparativo", "Bonifici effettuati all'amministratore senza delibera o oltre il deliberato", "Perizia di mercato sui compensi manageriali di settore"],
        "errori": ["Pagarsi compensi da amministratore senza una preventiva delibera assembleare (sono nulli e ripetibili)", "Sottovalutare il rischio di contestazione di distrazione in caso di successiva crisi", "Non impugnare tempestivamente la delibera viziata"]
    },
    {
        "cod": "SOC-014", "slug": "conflitto-interessi-amministratore-contratti-parti-correlate",
        "cat": "governance-soci", "cat_lbl": "Governance & Soci", "pilastro": "diritto-societario-governance-srl-spa",
        "titolo": "Contratti conclusi dall'amministratore in conflitto di interessi (art. 2475-ter e 2391 c.c.)",
        "seo_title": "Conflitto di Interessi Amministratore: Annullamento Contratto Art. 2475-ter",
        "desc": "Come annullare contratti stipulati dall'amministratore con societa' a lui riconducibili o parti correlate a condizioni svantaggiose per l'azienda.",
        "keywords": ["conflitto interessi amministratore art 2475 ter", "annullamento contratto amministratore", "art 2391 codice civile"],
        "norme": ["Art. 2475-ter c.c.", "Art. 2391 c.c.", "Art. 2634 c.c."],
        "scenario": "L'amministratore stipula contratti di affitto, consulenza o vendita di beni aziendali a prezzi fuori mercato con una societa' intestata a familiari o a se' stesso.",
        "rischio": "Trasferimento occulto di risorse aziendali verso terzi e grave danno al patrimonio sociale, fino a integrare il reato di infedelta' patrimoniale (art. 2634 c.c.).",
        "protocollo": [
            "Ricostruire i legami societari e familiari della controparte contrattuale tramite visure storiche e titolarita' effettiva.",
            "Dimostrare la conoscibilita' del conflitto da parte del terzo contraente e il danno subito dalla societa'.",
            "Agire per l'annullamento del contratto ex art. 2475-ter c.c. (entro 5 anni) e per la revoca e il risarcimento contro l'amministratore.",
            "Nei casi di danno intenzionale per ingiusto profitto, valutare la querela per infedelta' patrimoniale ex art. 2634 c.c."
        ],
        "prove": ["Contratto contestato e visura della societa' controparte", "Perizia di stima del valore di mercato della prestazione", "Verbali di CdA privi della necessaria informativa sul conflitto", "Pagamenti eseguiti a favore della parte correlata"],
        "errori": ["Non verificare la prova della conoscibilita' del conflitto da parte del terzo", "Confondere la legittimazione della societa' con quella del singolo socio", "Attendere oltre il termine di prescrizione quinquennale"]
    },
    {
        "cod": "SOC-015", "slug": "violazione-clausola-prelazione-statutaria-cessione-quote",
        "cat": "governance-soci", "cat_lbl": "Governance & Soci", "pilastro": "contenzioso-soci-patti-parasociali-recesso",
        "titolo": "Cessione di quote in violazione della clausola di prelazione statutaria: inefficacia e tutele",
        "seo_title": "Violazione Prelazione Societaria Cessione Quote: Rimedi Legali",
        "desc": "Cosa succede se un socio vende la propria quota a un estraneo senza rispettare il diritto di prelazione previsto nello statuto della S.r.l. o S.p.A.",
        "keywords": ["violazione clausola prelazione quote srl", "cessione quote senza prelazione inefficace", "denuntiatio prelazione societaria"],
        "norme": ["Art. 2469 c.c.", "Art. 2355-bis c.c.", "Art. 1372 c.c."],
        "scenario": "Un socio trasferisce le proprie quote a un terzo estraneo (o a un concorrente) omettendo la preventiva offerta in prelazione (denuntiatio) agli altri soci o indicando un prezzo fittizio.",
        "rischio": "Ingresso indesiderato di terzi nella compagine sociale con alterazione degli equilibri di controllo.",
        "protocollo": [
            "Esaminare esattamente il testo della clausola di prelazione nello statuto (prelazione propria, impropria, termini e modalita' di denuntiatio).",
            "Diffidare immediatamente l'organo amministrativo dal riconoscere la legittimazione al voto dell'acquirente per inefficacia del trasferimento verso la societa'.",
            "Agire davanti al Tribunale delle Imprese per accertare l'inefficacia della cessione nei confronti della societa' e ottenere il risarcimento del danno (oltre all'eventuale riscatto se previsto).",
            "Impugnare eventuali delibere assunte con il voto determinante dell'acquirente non legittimato."
        ],
        "prove": ["Statuto sociale vigente al momento della cessione", "Atto notarile di trasferimento quote iscritto al Registro Imprese", "Assenza di denuntiatio o prova della simulazione del prezzo", "Diffide inviate agli amministratori e al socio cedente"],
        "errori": ["Confondere la prelazione statutaria (efficacia reale verso la societa') con quella solo parasociale (efficacia obbligatoria)", "Non contestare subito la legittimazione al voto del nuovo acquirente", "Omettere di verificare se la cessione e' avvenuta tramite conferimento o fusione elusiva"]
    },
    {
        "cod": "SOC-016", "slug": "clausole-drag-along-tag-along-cessione-partecipazioni",
        "cat": "governance-soci", "cat_lbl": "Governance & Soci", "pilastro": "diritto-societario-governance-srl-spa",
        "titolo": "Clausole drag-along (trascinamento) e tag-along (co-vendita): validita' e contenzioso",
        "seo_title": "Clausole Drag-Along e Tag-Along in Statuto e Patti: Difesa Soci",
        "desc": "Condizioni di validita' delle clausole di trascinamento e co-vendita, tutela del prezzo minimo (fair value ex art. 2437-ter c.c.) e difesa del socio trascinato.",
        "keywords": ["clausola drag along validita", "tag along co vendita quote", "valore equo trascinamento socio"],
        "norme": ["Art. 2437-ter c.c.", "Art. 2473 c.c.", "Art. 1322 c.c."],
        "scenario": "Il socio di maggioranza attiva una clausola drag-along per obbligare la minoranza a vendere l'intera societa' a un terzo, oppure vende senza rispettare il diritto di tag-along della minoranza.",
        "rischio": "Una clausola drag-along che non garantisce al socio trascinato almeno il valore di liquidazione ex lege (criteri del recesso) rischia di essere dichiarata nulla o inefficace.",
        "protocollo": [
            "Verificare se la clausola drag-along rispetta la soglia minima inderogabile di valorizzazione equa (criteri art. 2437-ter / 2473 c.c.).",
            "Controllare che l'offerta del terzo sia genuina, vincolante e a parita' di condizioni per tutti i soci (assenza di side-letter occulte a favore della maggioranza).",
            "In caso di violazione del tag-along, agire per inefficacia/risarcimento e bloccare il closing con provvedimento d'urgenza se necessario.",
            "In sede di redazione statutaria, blindare le clausole con meccanismi di perizia indipendente e mandato irrevocabile."
        ],
        "prove": ["Statuto o patto parasociale contenente la clausola", "Offerta vincolante del terzo acquirente e condizioni economiche", "Perizia di stima del valore di mercato della partecipazione", "Comunicazioni formali di attivazione del trascinamento o co-vendita"],
        "errori": ["Inserire clausole drag-along prive di floor valutativo", "Introdurre il drag-along a maggioranza in statuto senza il consenso unanime dei soci", "Accettare prezzi penalizzanti senza verificare accordi collaterali con l'acquirente"]
    },
    {
        "cod": "SOC-017", "slug": "perdita-capitale-sociale-art-2482-ter-2484-cc",
        "cat": "governance-soci", "cat_lbl": "Governance & Soci", "pilastro": "diritto-societario-governance-srl-spa",
        "titolo": "Perdita del capitale sociale oltre un terzo o sotto il minimo legale (artt. 2482-bis e 2482-ter c.c.)",
        "seo_title": "Perdita Capitale Sociale S.r.l. Art. 2482-ter: Obblighi Amministratori",
        "desc": "Cosa devono fare subito gli amministratori quando le perdite erodono il capitale sotto il minimo legale: convocazione senza indugio, ricapitalizzazione, trasformazione o scioglimento.",
        "keywords": ["perdita capitale sociale art 2482 ter", "ricapitalizzazione o liquidazione srl", "gestione conservativa art 2486"],
        "norme": ["Art. 2482-bis c.c.", "Art. 2482-ter c.c.", "Art. 2484 co. 1 n. 4 c.c.", "Art. 2486 c.c."],
        "scenario": "Dalla situazione infrannuale o dal bilancio emerge che le perdite hanno ridotto il capitale sociale al di sotto del minimo legale (o azzerato il patrimonio netto).",
        "rischio": "Continuare l'attivita' ordinaria con nuove operazioni speculative dopo la perdita del capitale espone gli amministratori a responsabilita' personale integrale ex art. 2486 c.c.",
        "protocollo": [
            "Convocare 'senza indugio' l'assemblea straordinaria allegando una relazione aggiornata sulla situazione patrimoniale e le osservazioni dell'organo di controllo.",
            "Sottoporre ai soci le alternative di legge: ripianamento perdite e ricapitalizzazione, trasformazione della societa' oppure messa in liquidazione.",
            "Valutare se ricorrono i presupposti per accedere alla Composizione Negoziata (art. 20 CCII) o a uno strumento concorsuale che sospende la causa di scioglimento.",
            "Fino alla delibera, limitare rigorosamente la gestione ai soli atti conservativi dell'integrita' e del valore del patrimonio (art. 2486 c.c.)."
        ],
        "prove": ["Situazione patrimoniale infrannuale aggiornata e relazione degli amministratori", "Avviso di convocazione tempestiva dell'assemblea", "Verbale assembleare notarile di ricapitalizzazione o liquidazione", "Eventuale istanza di accesso a strumento CCII con sospensione ex art. 20/89 CCII"],
        "errori": ["Nascondere le perdite rinviando l'approvazione del bilancio", "Proseguire nuovi investimenti o contrarre debiti non conservativi a capitale azzerato", "Omettere l'iscrizione della causa di scioglimento nel Registro delle Imprese"]
    },
    {
        "cod": "SOC-018", "slug": "omesso-adeguamento-assetti-organizzativi-art-2086-cc",
        "cat": "governance-soci", "cat_lbl": "Governance & Soci", "pilastro": "diritto-societario-governance-srl-spa",
        "titolo": "Mancanza di adeguati assetti organizzativi, amministrativi e contabili (art. 2086 c.c. e art. 3 CCII)",
        "seo_title": "Adeguati Assetti Organizzativi Art. 2086 c.c. e Art. 3 CCII: Obblighi",
        "desc": "Come adeguare la S.r.l. o S.p.A. agli obblighi dell'art. 2086 co. 2 c.c. e dell'art. 3 CCII per evitare denunce ex art. 2409 c.c. e azioni di responsabilita' degli amministratori.",
        "keywords": ["adeguati assetti organizzativi art 2086", "art 3 codice crisi impresa", "assetti amministrativi contabili srl"],
        "norme": ["Art. 2086 co. 2 c.c.", "Art. 3 CCII", "Art. 2475 c.c.", "Art. 2409 c.c."],
        "scenario": "Una societa' opera senza organigramma, senza budget di tesoreria a 12 mesi, senza controllo mensile degli scostamenti ne' monitoraggio degli indici di allerta (DSCR, debiti scaduti INPS/AdE).",
        "rischio": "La giurisprudenza dei Tribunali delle Imprese qualifica l'assenza di adeguati assetti come grave irregolarita' gestionale sanzionabile ex art. 2409 c.c. anche prima dell'insolvenza.",
        "protocollo": [
            "Redigere organigramma, funzionigramma e sistema di deleghe formalizzato con delibera del CdA o determina dell'amministratore unico.",
            "Implementare un controllo di gestione periodico con budget di cassa forward-looking a 6-12 mesi e monitoraggio soglie art. 3 co. 4 CCII.",
            "Formalizzare flussi informativi trimestrali tra amministratori, direzione finanziaria e organo di controllo/revisore.",
            "Documentare nei verbali di CdA le verifiche periodiche di adeguatezza degli assetti e le azioni correttive tempestive."
        ],
        "prove": ["Delibera CdA di approvazione assetti e organigramma", "Report trimestrali di tesoreria e DSCR", "Monitoraggio scadenze tributarie, previdenziali e bancarie", "Verbali di scambio informativo con collegio sindacale o revisore"],
        "errori": ["Considerare gli adeguati assetti un obbligo solo per grandi S.p.A. (vale per tutte le societa')", "Comprare un manuale standard senza mai produrre report di cassa reali", "Ignorare le segnalazioni scritte del collegio sindacale o del revisore"]
    },
    {
        "cod": "SOC-019", "slug": "mancata-convocazione-assemblea-soci-ostruzionismo",
        "cat": "governance-soci", "cat_lbl": "Governance & Soci", "pilastro": "contenzioso-soci-patti-parasociali-recesso",
        "titolo": "Ostruzionismo dell'amministratore che rifiuta di convocare l'assemblea richiesta dai soci",
        "seo_title": "Mancata Convocazione Assemblea Soci: Potere Sostitutivo e Tribunale",
        "desc": "Cosa fare se l'amministratore ignora la richiesta di convocazione dell'assemblea: potere diretto del socio titolare di un terzo nella S.r.l. (art. 2479 c.c.) e decreto del Tribunale.",
        "keywords": ["mancata convocazione assemblea soci", "convocazione assemblea su richiesta soci", "art 2367 e 2479 codice civile"],
        "norme": ["Art. 2367 c.c.", "Art. 2479 co. 1 c.c.", "Art. 2631 c.c."],
        "scenario": "I soci chiedono la convocazione dell'assemblea per revocare l'amministratore o discutere la gestione, ma l'amministratore rimane inerte o rinvia all'infinito.",
        "rischio": "La gestione resta bloccata nelle mani di un amministratore sfiduciato che puo' compiere atti pregiudizievoli prima della sostituzione.",
        "protocollo": [
            "Inviare richiesta formale di convocazione via PEC con ordine del giorno preciso e termine breve.",
            "Nella S.r.l., se i soci richiedenti rappresentano almeno 1/3 del capitale, valutare la convocazione diretta in caso di inerzia (orientamento consolidato su art. 2479 c.c.) o il ricorso al Tribunale.",
            "Nella S.p.A. (quorum 10%), ricorrere al Presidente del Tribunale ex art. 2367 co. 2 c.c. per la convocazione d'ufficio con decreto e designazione del presidente.",
            "Contestare l'illecito amministrativo di omessa convocazione (art. 2631 c.c.) e agire per la revoca."
        ],
        "prove": ["PEC di richiesta convocazione con ordine del giorno", "Visura attestante la quota di capitale dei richiedenti", "Statuto con disciplina di convocazione", "Prova dell'inerzia o del rifiuto dell'organo amministrativo"],
        "errori": ["Indicare un ordine del giorno generico o su materie riservate esclusivamente agli amministratori", "Convocare senza rispettare i termini di preavviso statutari rendendo la delibera impugnabile", "Non coinvolgere il collegio sindacale ove presente (che ha potere sostitutivo ex art. 2406 c.c.)"]
    },
    {
        "cod": "SOC-020", "slug": "nomina-organo-controllo-revisore-srl-soglie-art-2477",
        "cat": "governance-soci", "cat_lbl": "Governance & Soci", "pilastro": "diritto-societario-governance-srl-spa",
        "titolo": "Obbligo di nomina dell'organo di controllo o revisore nella S.r.l. (soglie art. 2477 c.c.)",
        "seo_title": "Obbligo Revisore o Sindaco S.r.l. Art. 2477 c.c.: Soglie e Rischi",
        "desc": "Quando scatta l'obbligo di nominare il sindaco unico o il revisore legale nella S.r.l. (4 milioni attivo/ricavi, 20 dipendenti), rischi di nomina d'ufficio del Tribunale e sanzioni.",
        "keywords": ["obbligo revisore srl art 2477", "soglie nomina organo controllo srl", "nomina d ufficio revisore tribunale"],
        "norme": ["Art. 2477 c.c.", "Art. 2631 c.c.", "D.Lgs. 39/2010"],
        "scenario": "Una S.r.l. supera per due esercizi consecutivi almeno uno dei limiti dell'art. 2477 c.c. (totale attivo 4 milioni, ricavi 4 milioni o media 20 dipendenti) ma l'assemblea non nomina il revisore o sindaco.",
        "rischio": "Segnalazione del Conservatore del Registro delle Imprese al Tribunale, nomina giudiziale d'ufficio con costi imposti, irregolarita' delle delibere di bilancio e responsabilita' degli amministratori.",
        "protocollo": [
            "Verificare sugli ultimi due bilanci approvati il superamento delle soglie dimensionali o dell'obbligo di bilancio consolidato/controllo di societa' soggetta a revisione.",
            "Valutare la scelta strategica tra sindaco unico (anche con revisione legale) e revisore legale esterno.",
            "Convocare l'assemblea entro 30 giorni dall'approvazione del bilancio che certifica il superamento delle soglie.",
            "Aggiornare lo statuto se necessario e definire il perimetro di vigilanza sugli adeguati assetti ex art. 2086 c.c."
        ],
        "prove": ["Bilanci degli ultimi due esercizi con attivo, ricavi e media dipendenti", "Statuto sociale vigente", "Delibera assembleare di nomina e accettazione dell'incarico", "Comunicazione del Registro delle Imprese se gia' pervenuta"],
        "errori": ["Attendere la segnalazione del Registro delle Imprese al Tribunale", "Nominare un soggetto privo di requisiti di indipendenza o iscrizione al registro revisori", "Sottovalutare che il sindaco unico ha anche doveri di segnalazione della crisi ex art. 25-octies CCII"]
    },

    # ═══════════════════ 2. MODELLO 231 & ENTI (021-045) ═══════════════════
    {
        "cod": "SOC-021", "slug": "sequestro-preventivo-conti-azienda-art-53-dlgs-231",
        "cat": "modello-231", "cat_lbl": "Modello 231 & Enti", "pilastro": "sequestri-231-misure-interdittive-confisca",
        "titolo": "Sequestro preventivo sui conti correnti della societa' ex art. 53 D.Lgs. 231/2001",
        "seo_title": "Sequestro Preventivo 231 Conti Aziendali: Riesame in 10 Giorni",
        "desc": "Difesa penale d'urgenza contro il blocco dei conti bancari e dei beni aziendali finalizzato alla confisca del profitto (artt. 19 e 53 D.Lgs. 231/2001).",
        "keywords": ["sequestro preventivo 231 conti azienda", "art 53 dlgs 231 2001", "riesame sequestro profitto ente"],
        "norme": ["Art. 53 D.Lgs. 231/2001", "Art. 19 D.Lgs. 231/2001", "Art. 324 c.p.p."],
        "scenario": "La Guardia di Finanza esegue un decreto di sequestro preventivo per milioni di euro sui conti correnti operativi della societa' nell'ambito di un'indagine 231, paralizzando stipendi e fornitori.",
        "rischio": "Crisi immediata di liquidita', revoca degli affidamenti bancari e insolvenza di un'azienda sana se il sequestro non viene revocato o ridimensionato.",
        "protocollo": [
            "Nominare subito un difensore dell'ente distinto da quello dell'amministratore indagato (art. 39 D.Lgs. 231/2001) per evitare inammissibilita' del ricorso.",
            "Depositare istanza di Riesame entro 10 giorni contestando fumus commissi delicti, interesse/vantaggio dell'ente e quantificazione del profitto sequestrabile.",
            "Produrre perizia contabile di parte per scomputare i costi leciti sostenuti e contestare eventuali duplicazioni di sequestro tra persona fisica ed ente.",
            "Chiedere in subordine la sostituzione del sequestro con garanzie o lo sblocco parziale per il pagamento di stipendi e imposte correnti."
        ],
        "prove": ["Decreto di sequestro preventivo del GIP e verbali di esecuzione", "Delibera societaria di nomina procuratore speciale non indagato", "Perizia contabile sul profitto netto reale vs fatturato lordo", "Elenco scadenze stipendi, fornitori e impegni bancari"],
        "errori": ["Far firmare la nomina del difensore dell'ente dall'amministratore indagato (causa di inammissibilita' del Riesame)", "Far scadere il termine perentorio di 10 giorni", "Non contestare il calcolo lordo del profitto del reato"]
    },
    {
        "cod": "SOC-022", "slug": "misura-cautelare-interdittiva-231-art-45-difesa",
        "cat": "modello-231", "cat_lbl": "Modello 231 & Enti", "pilastro": "sequestri-231-misure-interdittive-confisca",
        "titolo": "Difesa urgente contro misure cautelari interdittive 231 (art. 45 D.Lgs. 231/2001)",
        "seo_title": "Misura Cautelare Interdittiva 231 Art. 45: Udienza e Sospensione",
        "desc": "Come difendere la societa' nell'udienza camerale ex art. 47 D.Lgs. 231/2001 contro la richiesta del PM di interdizione dall'attivita' o divieto di contrattare con la PA.",
        "keywords": ["misura cautelare interdittiva 231", "art 45 dlgs 231 2001", "sospensione misura interdittiva art 49"],
        "norme": ["Art. 45 D.Lgs. 231/2001", "Art. 47 D.Lgs. 231/2001", "Art. 49 D.Lgs. 231/2001"],
        "scenario": "Il Pubblico Ministero chiede al GIP l'applicazione di una misura cautelare interdittiva (sospensione licenze, divieto appalti PA o interdizione dall'attivita') e il giudice fissa l'udienza camerale.",
        "rischio": "L'applicazione della misura interdittiva puo' bloccare immediatamente l'operativita' dell'azienda, far decadere commesse pubbliche e causare licenziamenti.",
        "protocollo": [
            "Costituirsi formalmente per l'ente tramite rappresentante non in conflitto (art. 39) ed estrarre subito copia integrale degli atti depositati dal PM.",
            "Contestare in udienza camerale i gravi indizi di responsabilita' dell'ente e il pericolo concreto e attuale di reiterazione di illeciti della stessa indole.",
            "Presentare istanza di sospensione ex art. 49 D.Lgs. 231/2001 con piano immediato di adozione/revisione del Modello 231, estromissione dei soggetti coinvolti e risarcimento.",
            "In caso di ordinanza sfavorevole, proporre appello cautelare entro 10 giorni (art. 52) o chiedere la nomina di commissario giudiziale ex art. 15."
        ],
        "prove": ["Richiesta del PM e avviso di fissazione udienza art. 47", "Modello 231 aggiornato e delibera di estromissione degli indagati dalla gestione", "Documentazione sui livelli occupazionali e sulle commesse in corso", "Offerta di cauzione o piano di riparazione ex art. 17"],
        "errori": ["Presentarsi all'udienza camerale senza aver gia' avviato un concreto piano di riorganizzazione e discontinuità", "Lasciare l'amministratore indagato al comando durante l'udienza cautelare", "Non richiedere la sospensione ex art. 49 come paracadute processuale"]
    },
    {
        "cod": "SOC-023", "slug": "divieto-contrattare-pubblica-amministrazione-231-appalti",
        "cat": "modello-231", "cat_lbl": "Modello 231 & Enti", "pilastro": "sequestri-231-misure-interdittive-confisca",
        "titolo": "Divieto di contrattare con la Pubblica Amministrazione (art. 9 D.Lgs. 231/2001) e appalti",
        "seo_title": "Divieto di Contrattare con la PA 231 e Salvataggio Appalti Pubblici",
        "desc": "Come tutelare un'impresa che opera in appalti pubblici dal divieto di contrattare con la PA (art. 9 co. 2 lett. c D.Lgs. 231/2001) e dalle esclusioni del Codice Appalti.",
        "keywords": ["divieto contrattare pubblica amministrazione 231", "esclusione appalti pubblici 231", "self cleaning appalti 231"],
        "norme": ["Art. 9 co. 2 lett. c D.Lgs. 231/2001", "Art. 17 D.Lgs. 231/2001", "Art. 96 D.Lgs. 36/2023"],
        "scenario": "Un'impresa affidataria di lavori o servizi pubblici subisce la contestazione di un illecito 231 con rischio di divieto di contrattare con la PA ed esclusione dalle gare per grave illecito professionale.",
        "rischio": "Perdita delle commesse in corso, escussione delle cauzioni definitive, segnalazione ANAC ed esclusione pluriennale dalle gare pubbliche.",
        "protocollo": [
            "Attivare in parallelo la difesa penale 231 (riparazione ex art. 17 e 49) e il percorso di self-cleaning amministrativo ex art. 96 D.Lgs. 36/2023.",
            "Documentare la dissociazione effettiva dalle persone fisiche indagate, il risarcimento integrale e l'adozione di un MOG 231 specifico sui rischi appalti.",
            "Chiedere in sede penale la limitazione della misura ai soli rami d'azienda coinvolti o la sostituzione con commissario giudiziale (art. 15).",
            "Gestire in modo trasparente le dichiarazioni alle stazioni appaltanti per evitare contestazioni di falso dichiarativo."
        ],
        "prove": ["Contratti di appalto in essere e bandi in corso", "Delibere di revoca deleghe e ristrutturazione governance (self-cleaning)", "Modello 231 con protocolli gare e subappalti + verbali OdV", "Quietanza di risarcimento o accantonamento vincolato"],
        "errori": ["Omettere di dichiarare un procedimento rilevante alla stazione appaltante", "Limitarsi a un modello 231 generico privo di presidi sugli appalti", "Non coordinare l'avvocato penalista 231 con il difensore amministrativista"]
    },
    {
        "cod": "SOC-024", "slug": "nomina-commissario-giudiziale-231-art-15-continuita",
        "cat": "modello-231", "cat_lbl": "Modello 231 & Enti", "pilastro": "sequestri-231-misure-interdittive-confisca",
        "titolo": "Nomina del Commissario Giudiziale ex art. 15 D.Lgs. 231/2001 per evitare la chiusura",
        "seo_title": "Commissario Giudiziale 231 Art. 15: Continuita' Aziendale e Occupazione",
        "desc": "Quando chiedere al giudice la prosecuzione dell'attivita' tramite commissario giudiziale invece dell'interdizione: servizi essenziali e tutela dei livelli occupazionali.",
        "keywords": ["commissario giudiziale art 15 dlgs 231", "prosecuzione attivita ente 231", "tutela occupazione misura interdittiva"],
        "norme": ["Art. 15 D.Lgs. 231/2001", "Art. 45 co. 3 D.Lgs. 231/2001", "Art. 79 D.Lgs. 231/2001"],
        "scenario": "A fronte del rischio concreto di una sanzione o misura cautelare interdittiva che fermerebbe l'impresa, occorre preservare la continuita' produttiva e i posti di lavoro.",
        "rischio": "La chiusura temporanea o la sospensione delle autorizzazioni determinerebbe la perdita definitiva dei clienti e il licenziamento collettivo dei dipendenti.",
        "protocollo": [
            "Documentare in modo rigoroso che l'ente svolge un servizio pubblico/di pubblica necessita' oppure che l'interruzione provoca rilevanti ripercussioni sull'occupazione nel territorio.",
            "Chiedere in via subordinata al giudice l'applicazione del commissario giudiziale (art. 15 e art. 45 co. 3) per la durata della misura.",
            "Definire con precisione i poteri del commissario per consentire l'adozione del Modello 231 e il rientro in bonis dell'impresa.",
            "Calcolare l'impatto della confisca del profitto derivante dalla prosecuzione dell'attivita' (art. 15 co. 4)."
        ],
        "prove": ["Libro unico del lavoro (LUL) e numero dipendenti diretti e dell'indotto", "Contratti di servizio pubblico, sanita', logistica o forniture essenziali", "Relazione economico-sociale sull'impatto territoriale della chiusura", "Piano di adeguamento organizzativo 231"],
        "errori": ["Invocare genericamente la perdita di posti di lavoro senza dati numerici e territoriali provati", "Dimenticare che il profitto prodotto durante il commissariamento e' soggetto a confisca", "Non utilizzare il periodo di commissariamento per sanare i deficit organizzativi"]
    },
    {
        "cod": "SOC-025", "slug": "condotte-riparatorie-art-17-dlgs-231-evitare-interdizione",
        "cat": "modello-231", "cat_lbl": "Modello 231 & Enti", "pilastro": "modello-231-responsabilita-enti-odv",
        "titolo": "Condotte riparatorie ex art. 17 D.Lgs. 231/2001 prima del dibattimento per escludere l'interdizione",
        "seo_title": "Condotte Riparatorie Art. 17 D.Lgs. 231/2001: Come Evitare Interdizioni",
        "desc": "Le tre condizioni cumulative dell'art. 17 D.Lgs. 231/2001 (risarcimento, adozione Modello 231 idoneo, messa a disposizione del profitto) per evitare sanzioni interdittive.",
        "keywords": ["art 17 dlgs 231 condotte riparatorie", "evitare sanzioni interdittive 231", "riduzione sanzione pecuniaria art 12"],
        "norme": ["Art. 17 D.Lgs. 231/2001", "Art. 12 D.Lgs. 231/2001", "Art. 65 D.Lgs. 231/2001"],
        "scenario": "La societa' e' stata rinviata a giudizio per un illecito 231 che prevede gravi sanzioni interdittive e vuole disinnescare la paralisi aziendale prima dell'apertura del dibattimento.",
        "rischio": "Superata la dichiarazione di apertura del dibattimento di primo grado senza aver completato le condotte riparatorie (o chiesto la sospensione ex art. 65), l'esenzione dall'interdizione sfuma.",
        "protocollo": [
            "Risarcire integralmente il danno ed eliminare le conseguenze dannose o pericolose del reato (o adoperarsi efficacemente in tal senso).",
            "Eliminare le carenze organizzative mediante l'adozione e l'effettiva attuazione di un Modello 231 idoneo a prevenire reati della stessa specie, con OdV operativo.",
            "Mettere a disposizione il profitto conseguito ai fini della confisca.",
            "Se i tempi prima dell'udienza sono stretti, chiedere al giudice la sospensione del processo ex art. 65 D.Lgs. 231/2001 per completare gli adempimenti."
        ],
        "prove": ["Quietanze di risarcimento o atti di transazione con le parti lese", "Modello 231 adottato dal CdA, verbali di attuazione e audit OdV", "Documentazione del versamento o messa a disposizione del profitto", "Istanza motivata di sospensione ex art. 65 D.Lgs. 231/2001"],
        "errori": ["Presentare un modello 231 solo formale senza prova della sua effettiva attuazione", "Arrivare all'apertura del dibattimento senza aver avviato il risarcimento", "Trascurare il beneficio concorrente della riduzione fino alla meta' della sanzione pecuniaria (art. 12)"]
    },
    {
        "cod": "SOC-026", "slug": "conflitto-interessi-nomina-difensore-ente-art-39-dlgs-231",
        "cat": "modello-231", "cat_lbl": "Modello 231 & Enti", "pilastro": "modello-231-responsabilita-enti-odv",
        "titolo": "Incompatibilita' del legale rappresentante indagato a nominare il difensore dell'ente (art. 39 D.Lgs. 231/2001)",
        "seo_title": "Art. 39 D.Lgs. 231/2001: Nomina Difensore Ente senza Conflitto",
        "desc": "Come costituire validamente la societa' nel processo penale 231 quando l'amministratore e' indagato per il reato presupposto, evitando l'inammissibilita' di riesami e impugnazioni.",
        "keywords": ["art 39 dlgs 231 nomina difensore", "incompatibilita rappresentante legale 231", "procuratore speciale ad litem 231"],
        "norme": ["Art. 39 D.Lgs. 231/2001", "Art. 40 D.Lgs. 231/2001", "giurisprudenza a Sezioni Unite 33041/2015"],
        "scenario": "L'amministratore unico o il presidente del CdA e' indagato per il reato presupposto e nomina di propria iniziativa il difensore della societa' per impugnare un sequestro 231.",
        "rischio": "Secondo le Sezioni Unite (sent. Gabrielloni n. 33041/2015), la nomina effettuata dal rappresentante legale indagato e' inammissibile per conflitto di interessi assoluto, facendo dichiarare inammissibili tutti gli atti difensivi dell'ente.",
        "protocollo": [
            "Verificare immediatamente se il legale rappresentante risulti iscritto nel registro degli indagati per il reato presupposto.",
            "Far deliberare dall'assemblea o dal CdA (con astensione dell'indagato) la nomina di un procuratore speciale ad processum estraneo ai fatti, oppure sostituire il legale rappresentante.",
            "Far sottoscrivere al procuratore speciale non indagato la nomina del difensore di fiducia dell'ente e la dichiarazione di costituzione ex art. 39.",
            "Mantenere distinte le linee difensive tra persona fisica ed ente."
        ],
        "prove": ["Verbale assembleare o di CdA di nomina del procuratore speciale ad processum", "Procura speciale notarile o autenticata priva di conflitto", "Atto di costituzione dell'ente ex art. 39 D.Lgs. 231/2001", "Visura camerale aggiornata"],
        "errori": ["Far nominare il difensore della societa' dall'amministratore indagato (errore fatale)", "Nominare un avvocato unico per amministratore indagato ed ente quando le difese divergono", "Costituirsi tardivamente dopo la scadenza dei termini cautelari"]
    },
    {
        "cod": "SOC-027", "slug": "infortunio-lavoro-omicidio-lesioni-colpose-art-25-septies-231",
        "cat": "modello-231", "cat_lbl": "Modello 231 & Enti", "pilastro": "modello-231-responsabilita-enti-odv",
        "titolo": "Infortunio grave o mortale sul lavoro e responsabilita' dell'ente (art. 25-septies D.Lgs. 231/2001)",
        "seo_title": "Infortunio sul Lavoro e Responsabilita' 231 Art. 25-septies",
        "desc": "Difesa dell'azienda per omicidio colposo o lesioni gravi con violazione norme sicurezza (D.Lgs. 81/2008): criterio di interesse/vantaggio nei reati colposi, art. 30 T.U. sicurezza e deleghe.",
        "keywords": ["art 25 septies dlgs 231 infortunio lavoro", "interesse vantaggio reati colposi 231", "art 30 dlgs 81 2008 modello 231"],
        "norme": ["Art. 25-septies D.Lgs. 231/2001", "Art. 30 D.Lgs. 81/2008", "Artt. 589-590 c.p."],
        "scenario": "A seguito di un infortunio grave o mortale in stabilimento o cantiere, la Procura contesta il reato colposo al datore di lavoro e l'illecito 231 alla societa' ipotizzando un risparmio di spesa o di tempi.",
        "rischio": "Sanzioni pecuniarie fino a 1.000 quote, misure interdittive fino a 1 anno e blocco dei cantieri.",
        "protocollo": [
            "Dimostrare attraverso documenti contabili e di sicurezza l'assenza di qualsiasi sistematico risparmio di spesa o accelerazione dei ritmi produttivi (interesse/vantaggio dell'ente).",
            "Produrre il Modello 231 conforme all'art. 30 D.Lgs. 81/2008, le certificazioni ISO 45001, il DVR aggiornato, i verbali formazione e i controlli del preposto.",
            "Verificare la validita' delle deleghe di funzione sicurezza ex art. 16 D.Lgs. 81/2008 e la vigilanza dell'OdV.",
            "Valutare il risarcimento integrale tramite assicurazione RCT/RCO e gli adempimenti riparatori ex art. 17."
        ],
        "prove": ["DVR, DUVRI, POS/PSC e registro manutenzioni macchinari", "Certificazione ISO 45001 e Modello 231 conforme all'art. 30 T.U.", "Attestati formazione, consegna DPI e sanzioni disciplinari applicate ai lavoratori", "Fatture di investimento in sicurezza che smentiscono il risparmio di spesa"],
        "errori": ["Non avere un Modello 231 integrato con i requisiti specifici dell'art. 30 D.Lgs. 81/2008", "Trascurare il ruolo dell'OdV sui flussi infortuni e quasi-infortuni (near miss)", "Confondere la colpa del singolo lavoratore con la tenuta complessiva del sistema di sicurezza"]
    },
    {
        "cod": "SOC-028", "slug": "reati-tributari-fatture-false-231-art-25-quinquiesdecies",
        "cat": "modello-231", "cat_lbl": "Modello 231 & Enti", "pilastro": "modello-231-responsabilita-enti-odv",
        "titolo": "Reati tributari e fatture false nel Modello 231 (art. 25-quinquiesdecies D.Lgs. 231/2001)",
        "seo_title": "Reati Tributari 231 Art. 25-quinquiesdecies e Fatture False",
        "desc": "Difesa dell'ente per dichiarazione fraudolenta (artt. 2-3 D.Lgs. 74/2000), emissione fatture false (art. 8), occultamento scritture (art. 10) e frodi IVA transfrontaliere.",
        "keywords": ["reati tributari 231 art 25 quinquiesdecies", "fatture false responsabilita ente", "modello 231 tax control framework"],
        "norme": ["Art. 25-quinquiesdecies D.Lgs. 231/2001", "D.Lgs. 74/2000", "Art. 19 D.Lgs. 231/2001"],
        "scenario": "Dopo una verifica della Guardia di Finanza su fatture per operazioni inesistenti o indebite compensazioni, la Procura iscrive anche la societa' ai sensi dell'art. 25-quinquiesdecies D.Lgs. 231/2001.",
        "rischio": "Sequestro preventivo sui conti sociali per il risparmio d'imposta, sanzioni fino a 500 quote e divieto di contrattare con la PA.",
        "protocollo": [
            "Coordinare strettamente la difesa penale 231 con il contenzioso tributario per contestare l'inesistenza delle operazioni o l'entita' dell'imposta evasa.",
            "Verificare i presidi del Modello 231 sul ciclo passivo (qualificazione fornitori, verifica effettivita' prestazione, segregazione autorizzazioni e pagamenti).",
            "Valutare l'estinzione del debito tributario (anche rateale) per ridurre l'area sequestrabile e integrare le condotte riparatorie.",
            "Contestare eventuali duplicazioni di sequestro tra il profitto dell'ente e quello delle persone fisiche."
        ],
        "prove": ["PVC della Guardia di Finanza e avvisi di accertamento", "Documentazione dell'effettivita' delle prestazioni (DDT, SAL, email, foto, contratti)", "Procedure di qualificazione fornitori e controllo fatture nel MOG 231", "Quietanza di pagamento o rateizzazione con l'Agenzia delle Entrate"],
        "errori": ["Non aggiornare il Modello 231 ai reati tributari introdotti dal 2019-2020", "Pagare fornitori non qualificati senza tracciatura della prestazione effettiva", "Gestire separatamente e in contraddizione il processo tributario e quello penale 231"]
    },
    {
        "cod": "SOC-029", "slug": "corruzione-appalti-rapporti-pa-artt-24-25-dlgs-231",
        "cat": "modello-231", "cat_lbl": "Modello 231 & Enti", "pilastro": "modello-231-responsabilita-enti-odv",
        "titolo": "Corruzione, concussione e reati contro la PA nel D.Lgs. 231/2001 (artt. 24 e 25)",
        "seo_title": "Corruzione e Reati contro la PA D.Lgs. 231/2001: Difesa Ente",
        "desc": "Difesa dell'ente per corruzione, induzione indebita, traffico di influenze e turbata liberta' degli incanti: elusione fraudolenta del MOG, sanzioni interdittive lunghe e compliance ISO 37001.",
        "keywords": ["corruzione 231 art 25", "reati contro pa dlgs 231", "elusione fraudolenta modello 231"],
        "norme": ["Art. 24 D.Lgs. 231/2001", "Art. 25 D.Lgs. 231/2001", "Artt. 318-322-bis c.p."],
        "scenario": "Un dirigente o commerciale e' indagato per accordi corruttivi o utilita' promesse a un pubblico ufficiale per aggiudicarsi una gara o ottenere un'autorizzazione amministrativa.",
        "rischio": "Sanzioni interdittive particolarmente severe (da 4 a 7 anni se il reato e' commesso da apicale, riducibili con la collaborazione post factum ex art. 25 co. 5-bis).",
        "protocollo": [
            "Verificare se l'autore ha agito eludendo fraudolentemente i protocolli 231 (es. fondi extracontabili, consulenze fittizie, aggiramento della doppia firma).",
            "Attivare un'indagine interna difensiva per isolare la condotta e dimostrare la non riferibilita' a una politica aziendale.",
            "Valutare la collaborazione qualificata ex art. 25 co. 5-bis D.Lgs. 231/2001 per abbattere drasticamente la durata delle sanzioni interdittive.",
            "Rafforzare i protocolli anti-corruzione (gestione consulenti, agenti, omaggi, sponsorizzazioni, gare) anche secondo lo standard ISO 37001."
        ],
        "prove": ["Modello 231 Parte Speciale PA e procedure gare/consulenze", "Verbali OdV e tracciatura delle autorizzazioni di spesa", "Documentazione di elusione fraudolenta da parte del singolo soggetto", "Delibere di rimozione dell'indagato e misure riparatorie"],
        "errori": ["Autorizzare consulenze e provvigioni a intermediari senza verifica dell'attivita' reale", "Mantenere l'indagato in ruolo operativo durante le indagini", "Ignorare la riduzione premiale dell'art. 25 co. 5-bis D.Lgs. 231/2001"]
    },
    {
        "cod": "SOC-030", "slug": "truffa-fondi-pnrr-finanziamenti-pubblici-art-24-231",
        "cat": "modello-231", "cat_lbl": "Modello 231 & Enti", "pilastro": "modello-231-responsabilita-enti-odv",
        "titolo": "Truffa aggravata su fondi PNRR, contributi pubblici e crediti d'imposta (art. 24 D.Lgs. 231/2001)",
        "seo_title": "Truffa Fondi PNRR e Finanziamenti Pubblici: Difesa 231 Art. 24",
        "desc": "Difesa della societa' contro contestazioni di indebita percezione di erogazioni pubbliche (art. 316-ter c.p.), malversazione (art. 316-bis) e truffa aggravata (art. 640-bis c.p.) anche davanti a EPPO.",
        "keywords": ["truffa fondi pnrr 231", "indebita percezione erogazioni pubbliche art 24", "procura europea eppo 231"],
        "norme": ["Art. 24 D.Lgs. 231/2001", "Artt. 316-bis, 316-ter, 640-bis c.p.", "Reg. UE 2017/1939 (EPPO)"],
        "scenario": "La Guardia di Finanza o la Procura Europea (EPPO) contesta irregolarita' nella rendicontazione di contributi PNRR, bandi regionali, crediti R&S o finanziamenti garantiti MCC.",
        "rischio": "Sequestro integrale del contributo erogato, esclusione da futuri finanziamenti pubblici e revoca delle agevolazioni gia' concesse.",
        "protocollo": [
            "Verificare la distinzione tecnica tra mero inadempimento amministrativo (che comporta solo revoca del contributo) e artificio/raggiro penalmente rilevante.",
            "Ricostruire la documentazione tecnica di spesa, SAL, perizie asseverate e destinazione effettiva dei fondi al progetto finanziato.",
            "Difendersi contro sequestri sproporzionati distinguendo la quota di spese regolari da quelle contestate.",
            "Implementare nel Modello 231 un protocollo dedicato alla gestione e rendicontazione di bandi e fondi pubblici."
        ],
        "prove": ["Bando, domanda di ammissione e decreto di concessione del contributo", "Fatture quietanzate, bonifici dedicati, perizie tecniche e SAL", "Corrispondenza con l'ente erogatore o Invitalia/Simest/Regione", "Protocolli 231 su finanza agevolata"],
        "errori": ["Utilizzare i fondi vincolati per coprire liquidita' corrente estranea al progetto", "Affidarsi a consulenti esterni senza verificare la veridicita' delle dichiarazioni sottoscritte dal legale rappresentante", "Non distinguere la competenza della Procura Europea (EPPO) per fondi UE"]
    },
    {
        "cod": "SOC-031", "slug": "reati-ambientali-gestione-rifiuti-art-25-undecies-231",
        "cat": "modello-231", "cat_lbl": "Modello 231 & Enti", "pilastro": "modello-231-responsabilita-enti-odv",
        "titolo": "Reati ambientali, smaltimento rifiuti e inquinamento (art. 25-undecies D.Lgs. 231/2001)",
        "seo_title": "Reati Ambientali e Rifiuti 231 Art. 25-undecies: Difesa Imprese",
        "desc": "Tutela penale e 231 per imprese industriali e logistiche: gestione illecita rifiuti, scarichi, emissioni, traffico organizzato (art. 452-quaterdecies c.p.) e deleghe ambientali.",
        "keywords": ["reati ambientali 231 art 25 undecies", "gestione rifiuti responsabilita ente", "delega ambientale modello 231"],
        "norme": ["Art. 25-undecies D.Lgs. 231/2001", "D.Lgs. 152/2006 (TUA)", "Artt. 452-bis ss. c.p."],
        "scenario": "Un controllo ARPA o NOE contesta irregolarita' su codici CER, formulari FIR, depositi temporanei di rifiuti o superamento limiti di scarico/emissione.",
        "rischio": "Sequestro dell'impianto o dell'area aziendale, sanzioni pecuniarie e interdittive 231, oltre a obblighi onerosi di bonifica.",
        "protocollo": [
            "Verificare subito le autorizzazioni (AIA, AUA), i registri carico/scarico, i FIR e la regolare iscrizione all'Albo Gestori Ambientali dei trasportatori/smaltitori.",
            "Attivare, ove applicabile per le contravvenzioni ambientali, la procedura estintiva delle prescrizioni ARPA (art. 318-bis ss. D.Lgs. 152/2006).",
            "Dimostrare l'esistenza di una delega ambientale valida e di un Modello 231 integrato con sistema di gestione ISO 14001.",
            "Chiedere il dissequestro dell'impianto con facolta' d'uso per eseguire la messa in sicurezza."
        ],
        "prove": ["AIA/AUA, registri rifiuti, formulari FIR e analisi chimiche di classificazione", "Contratti e visure Albo Gestori dei fornitori di smaltimento", "Certificazione ISO 14001, delega ambientale e audit OdV", "Verbali ARPA e prescrizioni ottemperate"],
        "errori": ["Affidare rifiuti a trasportatori privi di autorizzazione per quel codice CER", "Superare i limiti temporali o volumetrici del deposito temporaneo", "Non prevedere audit a sorpresa dell'OdV sulle aree di stoccaggio"]
    },
    {
        "cod": "SOC-032", "slug": "reati-informatici-cybercrime-231-art-24-bis-legge-90-2024",
        "cat": "modello-231", "cat_lbl": "Modello 231 & Enti", "pilastro": "modello-231-responsabilita-enti-odv",
        "titolo": "Reati informatici e cybersicurezza nel Modello 231 (art. 24-bis aggiornato dalla L. 90/2024)",
        "seo_title": "Reati Informatici 231 Art. 24-bis e Legge 90/2024: Adeguamento MOG",
        "desc": "Aggiornamento obbligatorio del Modello 231 dopo la Legge 90/2024: inclusione dell'estorsione informatica (art. 629 co. 3 c.p.), accesso abusivo e coordinamento con NIS2 e GDPR.",
        "keywords": ["art 24 bis dlgs 231 legge 90 2024", "reati informatici modello 231", "adeguamento mog 231 cybersicurezza"],
        "norme": ["Art. 24-bis D.Lgs. 231/2001", "L. 90/2024", "D.Lgs. 138/2024 (NIS2)"],
        "scenario": "Un dipendente o collaboratore accede abusivamente a sistemi di concorrenti, altera dati o utilizza software illeciti nell'interesse dell'azienda, oppure il MOG 231 non e' aggiornato alla L. 90/2024.",
        "rischio": "Sanzioni pecuniarie aggravate dalla L. 90/2024, interdizioni informatiche e contestazione di inadeguatezza del modello organizzativo.",
        "protocollo": [
            "Aggiornare la Parte Speciale Reati Informatici del Modello 231 includendo la nuova estorsione informatica e i presidi della L. 90/2024.",
            "Integrare i protocolli 231 con le policy GDPR, NIS2 (D.Lgs. 138/2024), gestione credenziali, log degli amministratori di sistema e licenze software.",
            "Prevedere flussi informativi diretti tra CISO/IT, DPO e Organismo di Vigilanza in caso di incidenti di sicurezza.",
            "In caso di contestazione, dimostrare l'elusione delle policy IT e dei blocchi tecnici aziendali."
        ],
        "prove": ["Modello 231 aggiornato post L. 90/2024", "Policy IT aziendale, registro amministratori di sistema e log di accesso", "Licenze software regolari e contratti fornitori IT", "Verbali di coordinamento tra DPO, IT e OdV"],
        "errori": ["Mantenere un Modello 231 fermo a prima del 2024", "Non monitorare l'uso di account condivisi o software pirata", "Tenere separati a compartimenti stagni GDPR, NIS2 e Modello 231"]
    },
    {
        "cod": "SOC-033", "slug": "riciclaggio-autoriciclaggio-art-25-octies-dlgs-231",
        "cat": "modello-231", "cat_lbl": "Modello 231 & Enti", "pilastro": "modello-231-responsabilita-enti-odv",
        "titolo": "Riciclaggio, autoriciclaggio e impiego di denaro illecito (art. 25-octies D.Lgs. 231/2001)",
        "seo_title": "Autoriciclaggio e Riciclaggio 231 Art. 25-octies: Difesa Imprese",
        "desc": "Come prevenire e difendere la societa' da contestazioni di autoriciclaggio (art. 648-ter.1 c.p.) derivanti dal reimpiego di risparmi fiscali o proventi illeciti nei flussi aziendali.",
        "keywords": ["autoriciclaggio 231 art 25 octies", "riciclaggio responsabilita ente", "reimpiego proventi illeciti societa"],
        "norme": ["Art. 25-octies D.Lgs. 231/2001", "Artt. 648-bis, 648-ter, 648-ter.1 c.p.", "D.Lgs. 231/2007"],
        "scenario": "A seguito di un reato presupposto (anche tributario o societario), la Procura contesta all'ente l'autoriciclaggio per aver reimpiegato le somme in attivita' economiche o trasferimenti infragruppo.",
        "rischio": "Pene e sanzioni 231 elevatissime, sequestro del valore equivalente dei capitali movimentati e segnalazioni UIF con chiusura dei rapporti bancari.",
        "protocollo": [
            "Verificare se la condotta contestata integra un reale ostacolo concreto all'identificazione della provenienza delittuosa (requisito essenziale dell'art. 648-ter.1 c.p.) o un mero utilizzo trasparente non punibile.",
            "Implementare presidi rigorosi di tracciabilita' dei flussi finanziari, divieto di contante oltre soglia, verifica KYC su controparti estere e controllo delle operazioni infragruppo.",
            "Contestare il cumulo illegittimo di sequestri tra reato presupposto e autoriciclaggio.",
            "Affiancare una perizia bancaria-contabile per dimostrare la tracciabilita' integrale dei bonifici."
        ],
        "prove": ["Estratti conto e documentazione giustificativa dei bonifici e trasferimenti", "Procedure 231 di tesoreria, KYC fornitori/clienti e operazioni infragruppo", "Perizia sui flussi finanziari che esclude l'intento dissimulatorio", "Reportistica antiriciclaggio ove applicabile"],
        "errori": ["Effettuare giri di denaro opachi tramite societa' estere o conti personali", "Non documentare la causa economica reale dei finanziamenti infragruppo", "Trascurare il rischio di autoriciclaggio derivante da reati tributari"]
    },
    {
        "cod": "SOC-034", "slug": "reati-societari-falso-bilancio-art-25-ter-dlgs-231",
        "cat": "modello-231", "cat_lbl": "Modello 231 & Enti", "pilastro": "modello-231-responsabilita-enti-odv",
        "titolo": "Reati societari e false comunicazioni sociali nel D.Lgs. 231/2001 (art. 25-ter)",
        "seo_title": "Reati Societari 231 Art. 25-ter: Falso in Bilancio e Corruzione Privati",
        "desc": "Responsabilita' dell'ente per false comunicazioni sociali (artt. 2621-2622 c.c.), operazioni sul capitale e corruzione tra privati (art. 2635 c.c.): difese e protocolli contabili.",
        "keywords": ["reati societari 231 art 25 ter", "falso in bilancio responsabilita ente", "corruzione tra privati 231"],
        "norme": ["Art. 25-ter D.Lgs. 231/2001", "Artt. 2621-2622 c.c.", "Art. 2635 c.c."],
        "scenario": "Viene contestata alla societa' l'alterazione del bilancio per ottenere affidamenti bancari o la corresponsione di utilita' a dirigenti di clienti privati per ottenere forniture.",
        "rischio": "Sanzioni pecuniarie raddoppiate dalla normativa, danno reputazionale con le banche e revoca delle linee di credito.",
        "protocollo": [
            "Verificare il requisito dell'interesse dell'ente: molti reati societari danneggiano la societa' stessa e non possono fondare la responsabilita' 231.",
            "Dimostrare la conformita' delle valutazioni di bilancio ai principi contabili OIC/IAS tramite consulenza tecnica.",
            "Verificare la presenza di protocolli 231 sulla chiusura del bilancio, rapporti con revisori, omaggi commerciali e selezione fornitori privati.",
            "In tema di corruzione tra privati, controllare la procedibilita' e l'effettiva violazione di obblighi d'ufficio."
        ],
        "prove": ["Bilanci, carte di lavoro della chiusura contabile e relazioni del revisore", "Modello 231 Parte Speciale Reati Societari e procedure commerciali", "Perizia contabile sui criteri di valutazione adottati", "Contratti commerciali a condizioni di mercato"],
        "errori": ["Pensare che la corruzione tra privati non rilevi ai fini 231", "Lasciare la redazione del bilancio senza tracciatura dei passaggi tra amministrazione e direzione", "Non verificare se il reato societario ha recato danno anziche' vantaggio all'ente"]
    },
    {
        "cod": "SOC-035", "slug": "caporalato-sfruttamento-lavoro-appalti-art-25-quinquies-231",
        "cat": "modello-231", "cat_lbl": "Modello 231 & Enti", "pilastro": "modello-231-responsabilita-enti-odv",
        "titolo": "Caporalato, sfruttamento del lavoro e filiera subappalti (art. 25-quinquies D.Lgs. 231/2001)",
        "seo_title": "Caporalato e Appalti 231 Art. 25-quinquies: Amministrazione Giudiziaria",
        "desc": "Difesa delle aziende committenti contro contestazioni ex art. 603-bis c.p., illecito 231 e misure di prevenzione dell'amministrazione giudiziaria ex art. 34 Codice Antimafia.",
        "keywords": ["caporalato 231 art 25 quinquies", "amministrazione giudiziaria art 34 appalti", "sfruttamento lavoro subappalto"],
        "norme": ["Art. 25-quinquies D.Lgs. 231/2001", "Art. 603-bis c.p.", "Art. 34 D.Lgs. 159/2011"],
        "scenario": "Un'impresa committente (moda, logistica, edilizia, agricoltura) viene coinvolta in un'indagine su cooperative o subappaltatori che sfruttano manodopera, rischiando il procedimento 231 o l'amministrazione giudiziaria.",
        "rischio": "Commissariamento dell'impresa ex art. 34 Codice Antimafia, sequestri, danno reputazionale gravissimo e perdita di grandi clienti.",
        "protocollo": [
            "Audit immediato di tutta la catena di appalti e subappalti: DURC, DURF, congruità dei prezzi orari rispetto ai CCNL, divieto di subappalto non autorizzato.",
            "Dimostrare che la committente ha pagato corrispettivi congrui e ha svolto verifiche documentali e ispettive reali sui fornitori.",
            "Risolvere immediatamente i contratti con i fornitori irregolari e integrare il Modello 231 con protocolli rigorosi di qualificazione e audit di filiera.",
            "In caso di misura di prevenzione ex art. 34, attivare subito il piano di bonifica organizzativa per ottenere la revoca anticipata."
        ],
        "prove": ["Contratti di appalto con clausole etiche e divieto di subappalto occulto", "DURC, prospetti paghe, verifiche ispettive in sito e tariffe congrue ai CCNL", "Modello 231 aggiornato con protocollo filiera fornitori", "Atti di risoluzione contrattuale verso fornitori inadempienti"],
        "errori": ["Scegliere fornitori con tariffe orarie palesemente sottocosto rispetto ai CCNL", "Accontentarsi del solo DURC formale senza controlli sostanziali in cantiere/magazzino", "Ignorare segnalazioni whistleblowing su irregolarita' della filiera"]
    },
    {
        "cod": "SOC-036", "slug": "contraffazione-marchi-diritto-autore-art-25-bis-novies-231",
        "cat": "modello-231", "cat_lbl": "Modello 231 & Enti", "pilastro": "modello-231-responsabilita-enti-odv",
        "titolo": "Contraffazione marchi, brevetti e violazione diritto d'autore (artt. 25-bis e 25-novies D.Lgs. 231/2001)",
        "seo_title": "Contraffazione Marchi e Diritto Autore 231: Difesa Aziende",
        "desc": "Difesa dell'ente per commercio di prodotti con segni falsi, violazione brevetti, frode in commercio e uso aziendale di software senza licenza.",
        "keywords": ["contraffazione marchi 231", "frode in commercio art 25 bis 1", "software senza licenza art 25 novies"],
        "norme": ["Art. 25-bis D.Lgs. 231/2001", "Art. 25-bis.1 D.Lgs. 231/2001", "Art. 25-novies D.Lgs. 231/2001"],
        "scenario": "Un sequestro doganale o un'ispezione contesta la commercializzazione di prodotti con marchi contraffatti, origine 'Made in Italy' ingannevole o l'uso di software aziendali privi di licenza.",
        "rischio": "Sequestro della merce o dei server, sanzioni pecuniarie e interdittive 231, oltre a risarcimenti civili davanti al Tribunale delle Imprese.",
        "protocollo": [
            "Verificare le ricerche di anteriorita' marchi/brevetti, le dichiarazioni doganali di origine e le garanzie contrattuali rilasciate dai fornitori.",
            "Dimostrare la buona fede e l'assenza di colpa organizzativa tramite procedure di verifica IP e gestione licenze software (SAM).",
            "Regolarizzare immediatamente eventuali licenze scoperte o ritirare lotti contestati a fini riparatori.",
            "Coordinare la difesa penale 231 con l'eventuale causa civile di proprieta' industriale."
        ],
        "prove": ["Certificati di registrazione marchi/brevetti e pareri IP", "Contratti di fornitura con garanzie di originalita' e tracciabilita' doganale", "Inventario licenze software aziendali e fatture di acquisto", "Procedure 231 su proprieta' intellettuale e IT"],
        "errori": ["Importare merci senza verificare la catena di autorizzazione del titolare del marchio", "Apporre 'Made in Italy' senza rispettare le regole doganali di trasformazione sostanziale", "Tollerare l'installazione di software non licenziati sui PC aziendali"]
    },
    {
        "cod": "SOC-037", "slug": "modello-231-cartapesta-inidoneo-come-renderlo-esimente",
        "cat": "modello-231", "cat_lbl": "Modello 231 & Enti", "pilastro": "modello-231-responsabilita-enti-odv",
        "titolo": "Modello 231 'di cartapesta': perche' i giudici lo bocciano e come renderlo davvero esimente",
        "seo_title": "Modello 231 Inidoneo (di Cartapesta): Come Renderlo Esimente",
        "desc": "Come trasformare un Modello 231 generico e copiato in un sistema di prevenzione idoneo a superare il vaglio del giudice penale ex artt. 6 e 7 D.Lgs. 231/2001.",
        "keywords": ["modello 231 di cartapesta", "giudizio idoneita modello 231", "colpa di organizzazione art 6"],
        "norme": ["Art. 6 D.Lgs. 231/2001", "Art. 7 D.Lgs. 231/2001"],
        "scenario": "Un'azienda dispone di un Modello 231 scaricato o redatto anni prima senza reale mappatura dei processi, senza formazione documentata e senza verbali dell'OdV.",
        "rischio": "In caso di processo, il giudice dichiara il modello inidoneo per 'colpa di organizzazione' e condanna la societa' nonostante la spesa gia' sostenuta.",
        "protocollo": [
            "Eseguire un gap analysis reale intervistando i responsabili di funzione e mappando i processi aziendali effettivi.",
            "Eliminare protocolli astratti e introdurre controlli concreti: segregazione di funzioni, tracciabilita' delle decisioni, limiti di firma e verifiche a campione.",
            "Attivare un calendario reale di formazione certificata del personale e un sistema disciplinare effettivamente applicato.",
            "Garantire budget autonomo e verifiche periodiche documentate dell'Organismo di Vigilanza."
        ],
        "prove": ["Documento di risk assessment su misura firmato dai responsabili d'area", "Protocolli operativi integrati con le procedure reali aziendali", "Registri formazione firmata e test di verifica", "Verbali di audit e ispezioni a sorpresa dell'OdV"],
        "errori": ["Copiare il modello di un'altra azienda con riferimenti a uffici inesistenti", "Adottare il modello e dimenticarlo in un cassetto senza aggiornarlo alle nuove leggi", "Non dotare l'OdV di poteri di spesa e accesso autonomi"]
    },
    {
        "cod": "SOC-038", "slug": "organismo-vigilanza-odv-autonomia-flussi-responsabilita",
        "cat": "modello-231", "cat_lbl": "Modello 231 & Enti", "pilastro": "modello-231-responsabilita-enti-odv",
        "titolo": "Organismo di Vigilanza (OdV) inerte o privo di autonomia: rischi per l'ente e per i membri",
        "seo_title": "Organismo di Vigilanza OdV 231: Autonomia, Flussi e Rischi",
        "desc": "Requisiti di autonomia, indipendenza e continuita' d'azione dell'OdV ex art. 6 co. 1 lett. b D.Lgs. 231/2001, incompatibilita' dei componenti e gestione dei flussi informativi.",
        "keywords": ["organismo di vigilanza odv autonomia", "incompatibilita membri odv", "omessa vigilanza odv 231"],
        "norme": ["Art. 6 co. 1 lett. b D.Lgs. 231/2001", "Art. 6 co. 4-bis D.Lgs. 231/2001"],
        "scenario": "L'OdV e' composto da soggetti dipendenti o consulenti operativi in conflitto di interessi, oppure non si riunisce mai ne' riceve flussi informativi dalle aree a rischio.",
        "rischio": "La carenza di vigilanza autonoma fa cadere l'intera esimente del Modello 231 (art. 6 co. 1 lett. d) e puo' esporre i componenti dell'OdV a responsabilita' civile verso la societa'.",
        "protocollo": [
            "Verificare i requisiti di indipendenza e onorabilita' di tutti i componenti (preferendo un OdV esterno o misto con presidente esterno indipendente).",
            "Assegnare un budget annuo autonomo spendibile senza preventiva autorizzazione dell'amministratore.",
            "Istituire flussi informativi obbligatori periodici e ad evento (infortuni, verifiche GdF/ARPA, segnalazioni, contenziosi) verso la casella riservata dell'OdV.",
            "Verbalizzare ogni riunione, audit a campione e relazione semestrale al CdA e al Collegio Sindacale."
        ],
        "prove": ["Delibera CdA di nomina OdV e assegnazione budget autonomo", "Regolamento interno OdV e piano annuale delle verifiche", "Archivio verbali di riunione, audit e flussi informativi ricevuti", "Relazioni periodiche trasmesse al CdA"],
        "errori": ["Nominare nell'OdV l'amministratore delegato o il direttore operativo che dovrebbe essere controllato", "Lasciare l'OdV senza budget ne' flussi informativi", "Redigere verbali fotocopia privi di verifiche reali"]
    },
    {
        "cod": "SOC-039", "slug": "whistleblowing-dlgs-24-2023-modello-231-sanzioni-anac",
        "cat": "modello-231", "cat_lbl": "Modello 231 & Enti", "pilastro": "modello-231-responsabilita-enti-odv",
        "titolo": "Whistleblowing aziendale (D.Lgs. 24/2023), integrazione Modello 231 e sanzioni ANAC",
        "seo_title": "Whistleblowing D.Lgs. 24/2023 e Modello 231: Obblighi e Sanzioni ANAC",
        "desc": "Adeguamento del canale interno di segnalazione crittografato, gestione segnalazioni entro 7 giorni e 3 mesi, tutela del segnalante e difesa da sanzioni ANAC fino a 50.000 euro.",
        "keywords": ["whistleblowing dlgs 24 2023 modello 231", "sanzioni anac whistleblowing", "canale segnalazione interno 231"],
        "norme": ["D.Lgs. 24/2023", "Art. 6 co. 2-bis D.Lgs. 231/2001", "Art. 21 D.Lgs. 24/2023"],
        "scenario": "Un'impresa con Modello 231 (o >= 50 dipendenti) non ha attivato un canale whistleblowing conforme al D.Lgs. 24/2023, oppure riceve una segnalazione interna e rischia errori procedurali o ritorsioni.",
        "rischio": "Sanzioni amministrative ANAC da 10.000 a 50.000 euro, nullita' di eventuali provvedimenti ritorsivi contro il segnalante e inidoneita' del Modello 231.",
        "protocollo": [
            "Attivare una piattaforma whistleblowing crittografata (mai semplice email in chiaro) con nomina formale del gestore autonomo (spesso l'OdV o comitato dedicato).",
            "Rispettare rigorosamente le scadenze di legge: avviso di ricevimento entro 7 giorni e riscontro al segnalante entro 3 mesi.",
            "Eseguire la DPIA privacy sul canale whistleblowing e informare i lavoratori e le rappresentanze sindacali.",
            "In caso di segnalazione fondata, avviare istruttoria riservata proteggendo l'identita' del segnalante e impedendo qualsiasi misura ritorsiva."
        ],
        "prove": ["Procedura whistleblowing integrata nel MOG 231 e atto di nomina gestore", "DPIA GDPR e informative rese ai dipendenti", "Registro crittografato delle segnalazioni e dei riscontri 7gg/3mesi", "Verbali di consultazione sindacale"],
        "errori": ["Usare una casella email aziendale ordinaria accessibile agli amministratori IT", "Rivelare l'identita' del segnalante senza consenso espresso", "Licenziare o demansionare il segnalante esponendosi a nullita' ritorsiva e sanzione ANAC"]
    },
    {
        "cod": "SOC-040", "slug": "responsabilita-231-gruppi-societari-holding-controllate",
        "cat": "modello-231", "cat_lbl": "Modello 231 & Enti", "pilastro": "modello-231-responsabilita-enti-odv",
        "titolo": "Responsabilita' 231 nei gruppi societari: quando risponde la holding capogruppo",
        "seo_title": "Responsabilita' 231 nei Gruppi di Imprese e Holding Capogruppo",
        "desc": "Limiti alla risalita della responsabilita' 231 dalla controllata alla holding: interesse di gruppo, concorso dell'apicale della capogruppo e coordinamento tra Modelli 231 e OdV.",
        "keywords": ["responsabilita 231 gruppi societari", "holding capogruppo dlgs 231", "interesse di gruppo 231"],
        "norme": ["Artt. 5-7 D.Lgs. 231/2001", "Art. 2497 c.c."],
        "scenario": "Un reato presupposto commesso in una societa' controllata viene contestato anche alla holding capogruppo ipotizzando un interesse o vantaggio economico di gruppo.",
        "rischio": "Estensione di sequestri e misure interdittive all'intera capogruppo con blocco dei finanziamenti consolidati.",
        "protocollo": [
            "Contestare ogni estensione automatica: per coinvolgere la holding serve la prova rigorosa che un soggetto della capogruppo abbia concorso nel reato e che la holding abbia tratto un interesse/vantaggio concreto e specifico.",
            "Dotare ciascuna societa' del gruppo di un proprio Modello 231 autonomo (mai un solo modello generico di gruppo) e di un proprio OdV.",
            "Disciplinare in modo trasparente i contratti di servizi infragruppo (service agreements) e il cash pooling con corrispettivi a valore di mercato.",
            "Prevedere scambi informativi tra gli OdV delle controllate e l'OdV della capogruppo nel rispetto dell'autonomia di ciascun ente."
        ],
        "prove": ["Modelli 231 autonomi di holding e controllate", "Contratti infragruppo con prezzi di mercato e rendicontazioni reali", "Delibere autonome dei CdA delle controllate", "Verbali di coordinamento tra gli OdV di gruppo"],
        "errori": ["Adottare un unico Modello 231 di gruppo identico per tutte le controllate", "Esercitare ingerenza di fatto della holding nella gestione quotidiana della controllata senza deleghe", "Sottoscrivere service infragruppo generici privi di prestazioni documentate"]
    },
    {
        "cod": "SOC-041", "slug": "societa-estera-operante-italia-responsabilita-231",
        "cat": "modello-231", "cat_lbl": "Modello 231 & Enti", "pilastro": "modello-231-responsabilita-enti-odv",
        "titolo": "Societa' estera operante in Italia e applicazione del D.Lgs. 231/2001",
        "seo_title": "Societa' Estera in Italia e D.Lgs. 231/2001: Giurisdizione e MOG",
        "desc": "Quando una societa' con sede all'estero risponde davanti al giudice penale italiano ai sensi del D.Lgs. 231/2001 e come adeguare i compliance program esteri (FCPA/UKBA) allo standard italiano.",
        "keywords": ["societa estera dlgs 231", "giurisdizione italiana 231 enti esteri", "compliance program estero modello 231"],
        "norme": ["Art. 4 D.Lgs. 231/2001", "Art. 6 c.p.", "D.Lgs. 231/2001"],
        "scenario": "Una multinazionale o societa' estera con branch o attivita' in Italia subisce un'indagine penale italiana per reati commessi sul territorio nazionale, pur disponendo di un compliance program straniero.",
        "rischio": "La giurisprudenza italiana afferma la giurisdizione 231 anche sugli enti aventi sede all'estero per reati commessi in Italia e non ritiene automaticamente sufficiente un compliance program straniero privo di OdV.",
        "protocollo": [
            "Eseguire un bridge-assessment tra il compliance program di casa madre (es. FCPA, UK Bribery Act, Sapin II) e i requisiti specifici del D.Lgs. 231/2001.",
            "Integrare i protocolli locali con il catalogo dei reati presupposto italiani (sicurezza lavoro, fisco, ambiente, PA) e nominare un OdV locale.",
            "In caso di indagine, verificare i profili di giurisdizione ex art. 6 c.p. e art. 4 D.Lgs. 231/2001.",
            "Predisporre la traduzione certificata e la dimostrazione di effettivita' dei controlli del gruppo."
        ],
        "prove": ["Addendum italiano 231 al compliance program di casa madre", "Nomina e verbali dell'OdV locale", "Documentazione sui contratti e sull'operativita' in Italia", "Atti di indagine e verifica locus commissi delicti"],
        "errori": ["Pensare che la sede legale all'estero escluda l'applicazione del D.Lgs. 231/2001", "Depositare in Tribunale un codice etico in inglese privo di mappatura dei rischi italiani e senza OdV", "Trascurare le norme italiane su sicurezza lavoro e appalti"]
    },
    {
        "cod": "SOC-042", "slug": "adozione-tardiva-modello-231-post-factum-benefici",
        "cat": "modello-231", "cat_lbl": "Modello 231 & Enti", "pilastro": "modello-231-responsabilita-enti-odv",
        "titolo": "Adozione del Modello 231 dopo l'avvio delle indagini (post factum): benefici concreti",
        "seo_title": "Modello 231 Post Factum Dopo Indagini: Riduzione Sanzioni e Art. 17",
        "desc": "Perche' conviene adottare subito un Modello 231 serio anche dopo la notifica di un avviso di garanzia: riduzione sanzione pecuniaria (art. 12), stop interdizioni (art. 17) e sospensione cautelare (art. 49).",
        "keywords": ["adozione modello 231 post factum", "modello 231 dopo indagini", "riduzione sanzioni art 12 dlgs 231"],
        "norme": ["Art. 12 co. 2 lett. b D.Lgs. 231/2001", "Art. 17 D.Lgs. 231/2001", "Art. 49 D.Lgs. 231/2001"],
        "scenario": "Un'impresa sprovvista di Modello 231 riceve la notizia di un'indagine penale per un reato presupposto e teme che ormai sia troppo tardi per correre ai ripari.",
        "rischio": "Restare inerti espone l'ente alla piena misura delle sanzioni pecuniarie e all'applicazione di misure interdittive definitive.",
        "protocollo": [
            "Avviare immediatamente la rimozione delle criticita' organizzative che hanno reso possibile il reato contestato (discontinuita' gestoria e procedurale).",
            "Adottare e attuare realmente un Modello 231 tarato sul reato oggetto di indagine con nomina di un OdV indipendente e audit immediati.",
            "Depositare il modello e i verbali di attuazione prima dell'apertura del dibattimento per ottenere la riduzione della sanzione pecuniaria (art. 12 co. 2).",
            "Cumulare l'adozione con risarcimento e messa a disposizione del profitto per escludere le interdizioni (art. 17)."
        ],
        "prove": ["Delibera CdA di adozione del Modello 231 post factum", "Relazione sulle specifiche modifiche organizzative introdotte rispetto al fatto contestato", "Primi verbali di verifica dell'OdV che attestano l'effettiva attuazione", "Atti riparatori e risarcitori"],
        "errori": ["Rinunciare a dotarsi del Modello 231 ritenendo che serva solo prima del reato", "Presentare al giudice un modello non calibrato sulla specifica falla emersa nelle indagini", "Attendere il dibattimento perdendo le finestre premiali"]
    },
    {
        "cod": "SOC-043", "slug": "patteggiamento-ente-art-63-dlgs-231-valutazione",
        "cat": "modello-231", "cat_lbl": "Modello 231 & Enti", "pilastro": "modello-231-responsabilita-enti-odv",
        "titolo": "Patteggiamento dell'ente (art. 63 D.Lgs. 231/2001): quando conviene e riflessi sugli appalti",
        "seo_title": "Patteggiamento Ente Art. 63 D.Lgs. 231/2001: Strategia e Appalti",
        "desc": "Presupposti e convenienza del patteggiamento della societa' ex art. 63 D.Lgs. 231/2001: riduzione fino a un terzo, esclusione sanzioni interdittive e impatto sul casellario 231.",
        "keywords": ["patteggiamento ente art 63 dlgs 231", "casellario sanzioni amministrative 231", "riduzione pena patteggiamento 231"],
        "norme": ["Art. 63 D.Lgs. 231/2001", "Art. 444 c.p.p.", "Art. 17 D.Lgs. 231/2001"],
        "scenario": "A fronte di un quadro probatorio solido, la societa' deve decidere se affrontare il dibattimento o negoziare un patteggiamento ex art. 63 D.Lgs. 231/2001 con il Pubblico Ministero.",
        "rischio": "Un patteggiamento mal negoziato puo' lasciare in piedi una confisca sproporzionata o produrre effetti negativi sulla reputazione e sulle gare pubbliche.",
        "protocollo": [
            "Completare prima le condotte riparatorie (artt. 12 e 17) per abbattere la sanzione pecuniaria ed escludere le sanzioni interdittive.",
            "Negoziare con la Procura una pena pecuniaria ridotta fino a un terzo, escludendo le interdizioni e circoscrivendo la confisca.",
            "Valutare preventivamente l'impatto dell'iscrizione nell'Anagrafe delle sanzioni amministrative dipendenti da reato rispetto a gare PA, banche e rating.",
            "Verificare se la persona fisica sceglie una strada diversa (le sorti processuali di ente e persona fisica possono divergere)."
        ],
        "prove": ["Fascicolo integrale delle indagini e valutazione del rischio dibattimentale", "Documentazione degli adempimenti ex artt. 12 e 17", "Prospetto dei rapporti con banche e stazioni appaltanti", "Bozza di accordo ex art. 63 D.Lgs. 231/2001"],
        "errori": ["Patteggiare prima di aver neutralizzato le sanzioni interdittive con l'art. 17", "Non verificare l'impatto del patteggiamento sui bandi di gara pubblici", "Dimenticare che il patteggiamento e' ammesso anche quando il reato presupposto e' punito con sola pena pecuniaria per l'ente"]
    },
    {
        "cod": "SOC-044", "slug": "confisca-profitto-equivalente-art-19-dlgs-231",
        "cat": "modello-231", "cat_lbl": "Modello 231 & Enti", "pilastro": "sequestri-231-misure-interdittive-confisca",
        "titolo": "Confisca diretta e per equivalente del profitto del reato ex art. 19 D.Lgs. 231/2001",
        "seo_title": "Confisca Profitto 231 Art. 19: Calcolo Netto, Costi e Difesa",
        "desc": "Come contestare la quantificazione del profitto confiscabile nel processo 231: distinzione tra profitto lordo e netto, utilita' conseguite dal danneggiato e divieto di duplicazione.",
        "keywords": ["confisca profitto 231 art 19", "calcolo profitto netto 231", "confisca per equivalente societa"],
        "norme": ["Art. 19 D.Lgs. 231/2001", "Art. 53 D.Lgs. 231/2001", "giurisprudenza a Sezioni Unite 26654/2008"],
        "scenario": "La Procura chiede la confisca (e prima il sequestro) dell'intero corrispettivo incassato dalla societa' su un contratto o appalto, senza detrarre i costi effettivi sostenuti per la prestazione lecita.",
        "rischio": "Una confisca calcolata sul fatturato lordo anziche' sul profitto netto reale puo' distruggere il patrimonio netto e portare la societa' al fallimento.",
        "protocollo": [
            "Richiamare i principi delle Sezioni Unite sul 'reato in contratto': quando la prestazione e' stata effettivamente eseguita a beneficio del committente, va detratta l'utilita' conseguita dalla controparte.",
            "Affidare a un consulente tecnico contabile la scomposizione analitica tra ricavi, costi diretti leciti e margine netto reale.",
            "Eccepire il divieto di confisca sulla parte di profitto gia' restituita al danneggiato o gia' versata all'Erario.",
            "Contestare il cumulo solidaristico che ecceda complessivamente l'ammontare unitario del profitto tra persona fisica ed ente."
        ],
        "prove": ["Contratti, SAL, certificati di regolare esecuzione e collaudi", "Contabilita' analitica di commessa con fatture costi materiali e manodopera", "Perizia contabile di parte sul profitto netto", "Quietanza di restituzioni o versamenti fiscali"],
        "errori": ["Accettare passivamente la coincidenza tra fatturato e profitto confiscabile", "Non documentare l'utilita' effettivamente ricevuta dalla controparte contrattuale", "Omettere di verificare se parte del profitto e' gia' stata sequestrata alla persona fisica"]
    },
    {
        "cod": "SOC-045", "slug": "verifica-231-catena-appalti-subappalti-fornitori",
        "cat": "modello-231", "cat_lbl": "Modello 231 & Enti", "pilastro": "modello-231-responsabilita-enti-odv",
        "titolo": "Clausole 231 e audit nella catena di appalti, subappalti e fornitori strategici",
        "seo_title": "Clausole 231 nei Contratti con Fornitori e Subappaltatori",
        "desc": "Come proteggere l'impresa dai reati commessi da fornitori, agenti e subappaltatori: clausole risolutive espresse 231, audit preventivi e qualificazione dell'albo fornitori.",
        "keywords": ["clausole 231 contratti fornitori", "audit fornitori modello 231", "responsabilita 231 subappaltatori"],
        "norme": ["Art. 5 D.Lgs. 231/2001", "Art. 6 D.Lgs. 231/2001", "Art. 1456 c.c."],
        "scenario": "Un fornitore, agente commerciale o subappaltatore commette un illecito (sicurezza, ambiente, corruzione, lavoro irregolare) nell'esecuzione di servizi per la societa' committente.",
        "rischio": "Coinvolgimento dell'impresa committente per concorso nel reato o per difetto di vigilanza e selezione della filiera.",
        "protocollo": [
            "Inserire in tutti i contratti B2B clausole 231 vincolanti con presa visione del Codice Etico, obbligo di rispetto delle norme e clausola risolutiva espressa ex art. 1456 c.c.",
            "Istituire una procedura di qualificazione preventiva dei fornitori (visure, antimafia, DURC, autorizzazioni ambientali, assenza precedenti).",
            "Prevedere il diritto contrattuale di audit e ispezione a campione presso i subappaltatori critici.",
            "Documentare la pronta attivazione dei rimedi contrattuali in caso di violazione."
        ],
        "prove": ["Contratti di fornitura/appalto con clausola risolutiva 231", "Schede di qualificazione albo fornitori e controlli periodici", "Report di audit di filiera e segnalazioni all'OdV", "Lettere di diffida o risoluzione contrattuale"],
        "errori": ["Inserire clausole 231 standard senza mai fare verifiche sostanziali sui fornitori ad alto rischio", "Consentire subappalti non autorizzati", "Pagare provvigioni anomale ad agenti privi di struttura operativa"]
    },

    # ═══════════════════ 3. CRISI & COMPOSIZIONE NEGOZIATA (046-050) ═══════════════════
    {
        "cod": "SOC-046", "slug": "accesso-composizione-negoziata-crisi-art-12-ccii",
        "cat": "crisi-composizione", "cat_lbl": "Crisi & Composizione", "pilastro": "crisi-impresa-composizione-negoziata-ccii",
        "titolo": "Accesso alla Composizione Negoziata della Crisi (artt. 12-17 CCII): requisiti e piattaforma",
        "seo_title": "Composizione Negoziata della Crisi Art. 12 CCII: Come Accedere",
        "desc": "Quando e come presentare istanza di Composizione Negoziata sulla piattaforma camerale, nomina dell'Esperto indipendente, test pratico e gestione riservata della crisi.",
        "keywords": ["composizione negoziata crisi art 12 ccii", "piattaforma composizione negoziata", "nomina esperto indipendente crisi"],
        "norme": ["Art. 12 CCII", "Art. 17 CCII", "D.Lgs. 136/2024"],
        "scenario": "Un'impresa in squilibrio patrimoniale o economico-finanziario (anche gia' insolvente ma risanabile) vuole negoziare con banche, Fisco e fornitori senza aprire una procedura concorsuale invasiva.",
        "rischio": "Attendere troppo trasforma una crisi reversibile in insolvenza conclamata, bruciando la possibilita' di salvare l'azienda.",
        "protocollo": [
            "Eseguire subito il test pratico di risanabilita' e predisporre il piano finanziario a 6 mesi e il progetto di piano di risanamento.",
            "Raccogliere tutti i certificati di legge (debiti tributari AdE/AdER, contributivi INPS/INAIL, Centrale Rischi Banca d'Italia) e depositare l'istanza sulla piattaforma telematica CCIAA.",
            "Valutare la contestuale richiesta di misure protettive del patrimonio (art. 18 CCII) e sospensione degli obblighi sul capitale (art. 20 CCII).",
            "Avviare le trattative guidate dall'Esperto indipendente con un dossier credibile e trasparente."
        ],
        "prove": ["Bilanci ultimi tre esercizi e situazione contabile aggiornata", "Progetto di piano di risanamento e piano finanziario a 6 mesi", "Certificati unici debiti fiscali/contributivi e Centrale Rischi", "Elenco creditori con ammontare e cause di prelazione"],
        "errori": ["Depositare l'istanza senza un progetto di piano realistico causando l'archiviazione immediata dell'Esperto", "Omettere debiti rilevanti nell'elenco creditori", "Dimenticare di coordinare la richiesta di misure protettive fin dal primo giorno"]
    },
    {
        "cod": "SOC-047", "slug": "misure-protettive-patrimonio-art-18-ccii-blocco-pignoramenti",
        "cat": "crisi-composizione", "cat_lbl": "Crisi & Composizione", "pilastro": "crisi-impresa-composizione-negoziata-ccii",
        "titolo": "Misure protettive del patrimonio ex art. 18 CCII: blocco pignoramenti e istanze di fallimento",
        "seo_title": "Misure Protettive Art. 18 CCII: Blocco Pignoramenti e Fallimento",
        "desc": "Come ottenere lo scudo automatico contro azioni esecutive, cautelari, ipoteche giudiziali e sentenze di liquidazione giudiziale durante la Composizione Negoziata.",
        "keywords": ["misure protettive art 18 ccii", "blocco pignoramenti composizione negoziata", "stop liquidazione giudiziale"],
        "norme": ["Art. 18 CCII", "Art. 19 CCII", "D.Lgs. 136/2024"],
        "scenario": "Fornitori, banche o AdER hanno notificato precetti, pignoramenti presso terzi sui conti correnti o un'istanza di liquidazione giudiziale che rischiano di bloccare l'azienda.",
        "rischio": "Il pignoramento dei conti operativi paralizza pagamenti, stipendi e forniture, rendendo impossibile qualsiasi risanamento.",
        "protocollo": [
            "Chiedere le misure protettive erga omnes o selettive contestualmente all'istanza di Composizione Negoziata (con effetto immediato dalla pubblicazione nel Registro delle Imprese).",
            "Depositare il giorno stesso (o entro il giorno successivo) il ricorso al Tribunale per la conferma delle misure ex art. 19 CCII.",
            "Notificare subito l'avvenuta pubblicazione ai creditori procedenti e ai giudici dell'esecuzione per fermare pignoramenti e aste.",
            "Ricordare che i diritti di credito dei lavoratori sono sempre esclusi dalle misure protettive (art. 18 co. 3 CCII)."
        ],
        "prove": ["Ricevuta di pubblicazione dell'istanza nel Registro delle Imprese", "Ricorso di conferma ex art. 19 CCII depositato in Tribunale", "Parere favorevole dell'Esperto sulla funzionalita' delle misure al risanamento", "Atti di pignoramento o istanze pendenti da sospendere"],
        "errori": ["Depositare il ricorso di conferma in Tribunale oltre il giorno successivo perdendo l'efficacia delle misure", "Non notificare la protezione ai creditori che stanno eseguendo pignoramenti", "Chiedere misure protettive senza un piano reale (il Tribunale le revoca)"]
    },
    {
        "cod": "SOC-048", "slug": "udienza-conferma-misure-protettive-art-19-ccii-tribunale",
        "cat": "crisi-composizione", "cat_lbl": "Crisi & Composizione", "pilastro": "crisi-impresa-composizione-negoziata-ccii",
        "titolo": "Udienza di conferma delle misure protettive e cautelari davanti al Tribunale (art. 19 CCII)",
        "seo_title": "Conferma Misure Protettive Art. 19 CCII: Udienza in Tribunale",
        "desc": "Come preparare l'udienza in Tribunale per ottenere la conferma (da 30 a 120 giorni, prorogabili fino a 240) delle misure protettive e cautelari contro le opposizioni dei creditori.",
        "keywords": ["conferma misure protettive art 19 ccii", "udienza tribunale misure protettive", "durata misure protettive 120 giorni"],
        "norme": ["Art. 19 CCII", "Art. 18 CCII", "Art. 669-terdecies c.p.c."],
        "scenario": "Il Tribunale fissa l'udienza entro 10 giorni dal ricorso ex art. 19 CCII e alcuni creditori (banche o fornitori) si costituiscono chiedendo la revoca delle misure protettive.",
        "rischio": "La mancata conferma espone immediatamente l'impresa all'aggressione dei creditori e alla dichiarazione di liquidazione giudiziale.",
        "protocollo": [
            "Allegare al ricorso tutti i documenti obbligatori dell'art. 19 co. 2 CCII (bilanci, situazione aggiornata, elenco creditori, piano finanziario a 6 mesi, dichiarazione dell'Esperto).",
            "Dimostrare in udienza la ragionevole perseguibilita' del risanamento e la proporzionalita' del sacrificio imposto ai creditori.",
            "Chiedere anche misure cautelari atipiche se necessarie (es. inibitoria escussione garanzie o mantenimento contratti essenziali).",
            "In caso di rigetto parziale o totale, valutare il reclamo al collegio ex art. 669-terdecies c.p.c."
        ],
        "prove": ["Fascicolo completo ex art. 19 co. 2 CCII", "Parere scritto dell'Esperto sulla concretezza delle trattative", "Piano industriale e di cassa verificabile", "Prove dell'avvenuta notifica del decreto di fissazione udienza ai creditori"],
        "errori": ["Omettere anche uno solo dei documenti tassativi richiesti dall'art. 19 co. 2 CCII", "Presentarsi in udienza senza il parere positivo dell'Esperto", "Non notificare correttamente il ricorso e il decreto ai creditori indicati dal giudice"]
    },
    {
        "cod": "SOC-049", "slug": "segnalazione-allerta-agenzia-entrate-inps-ader-art-25-novies",
        "cat": "crisi-composizione", "cat_lbl": "Crisi & Composizione", "pilastro": "crisi-impresa-composizione-negoziata-ccii",
        "titolo": "Segnalazione di allerta di Agenzia delle Entrate, INPS, INAIL o AdER (art. 25-novies CCII)",
        "seo_title": "Segnalazione Allerta Art. 25-novies CCII: INPS, AdE e AdER",
        "desc": "Cosa fare quando arriva la PEC di segnalazione dei creditori pubblici qualificati per debiti IVA, contributi INPS o cartelle scadute: rischi per gli amministratori e rimedi.",
        "keywords": ["segnalazione allerta art 25 novies ccii", "pec agenzia entrate inps crisi impresa", "soglie creditori pubblici qualificati"],
        "norme": ["Art. 25-novies CCII", "Art. 25-octies CCII", "Art. 2086 c.c."],
        "scenario": "L'imprenditore e l'organo di controllo ricevono via PEC una segnalazione formale da INPS, INAIL, Agenzia delle Entrate o AdER per superamento delle soglie di debito scaduto dell'art. 25-novies CCII.",
        "rischio": "Ignorare la segnalazione aggrava pesantemente la posizione degli amministratori in caso di futura azione di responsabilita' o bancarotta semplice per aggravamento del dissesto.",
        "protocollo": [
            "Verificare immediatamente l'esattezza contabile degli importi segnalati (eventuali pagamenti, compensazioni, sgravi o rateazioni gia' in corso).",
            "Convocare senza indugio il CdA e l'organo di controllo per verbalizzare la presa d'atto e l'analisi della sostenibilita' del debito.",
            "Se lo squilibrio e' temporaneo, regolarizzare tramite rateazione/ravvedimento; se strutturale, attivare subito la Composizione Negoziata o uno strumento CCII.",
            "Rispondere formalmente all'organo di controllo documentando le iniziative adottate."
        ],
        "prove": ["PEC di segnalazione ex art. 25-novies CCII", "Estratti di ruolo AdER, cassetto fiscale e previdenziale aggiornati", "Verbale del CdA con analisi di cassa e piano di rientro", "Eventuale istanza di rateazione o accesso a Composizione Negoziata"],
        "errori": ["Cestinare o ignorare la PEC pensando sia un semplice avviso bonario", "Non informare il collegio sindacale o il revisore", "Proseguire nell'accumulo di debiti IVA e ritenute senza un piano di riequilibrio"]
    },
    {
        "cod": "SOC-050", "slug": "revoca-affidamenti-bancari-composizione-negoziata-art-16-ccii",
        "cat": "crisi-composizione", "cat_lbl": "Crisi & Composizione", "pilastro": "crisi-impresa-composizione-negoziata-ccii",
        "titolo": "Divieto di revoca automatica dei fidi bancari in Composizione Negoziata (art. 16 co. 5 CCII)",
        "seo_title": "Revoca Fidi Bancari in Composizione Negoziata: Tutela Art. 16 CCII",
        "desc": "Come difendere l'impresa se la banca sospende o revoca gli affidamenti per il solo fatto dell'accesso alla Composizione Negoziata: dovere di buona fede e riattivazione cautelare.",
        "keywords": ["revoca fidi composizione negoziata", "art 16 comma 5 ccii banche", "sospensione linee credito crisi impresa"],
        "norme": ["Art. 16 co. 5 CCII", "Art. 18 co. 5 CCII", "D.Lgs. 136/2024"],
        "scenario": "Appena viene pubblicata l'istanza di Composizione Negoziata, una banca congela le linee di anticipo fatture o revoca gli affidamenti bancari senza una valida giustificazione prudenziale.",
        "rischio": "Il blocco improvviso del circolante bancario soffoca la liquidita' aziendale e fa saltare le trattative con tutti gli altri creditori.",
        "protocollo": [
            "Diffidare formalmente la banca richiamando l'art. 16 co. 5 CCII (come rafforzato dal Correttivo-ter D.Lgs. 136/2024): la notizia dell'accesso alla Composizione Negoziata non costituisce di per se' causa di sospensione o revoca degli affidamenti.",
            "Chiedere all'istituto di motivare analiticamente l'eventuale sospensione in base a effettive regole di vigilanza prudenziale e coinvolgere subito l'Esperto.",
            "In caso di revoca illegittima o pretestuosa, chiedere al Tribunale una misura cautelare di riattivazione delle linee di credito ex art. 19 CCII.",
            "Negoziare con il ceto bancario un accordo di standstill e mantenimento linee autoliquidanti."
        ],
        "prove": ["Comunicazione bancaria di sospensione o revoca fidi", "Contratti di apertura di credito e andamento regolare dei pagamenti ante-istanza", "Piano finanziario a 6 mesi e parere dell'Esperto", "Diffida PEC ex art. 16 co. 5 CCII"],
        "errori": ["Subire passivamente il congelamento dei castelletti senza contestarlo per iscritto", "Non coinvolgere l'Esperto nella comunicazione verso gli uffici crediti della banca", "Trascurare il raccordo tra le norme prudenziali bancarie e la richiesta cautelare in Tribunale"]
    }
]
