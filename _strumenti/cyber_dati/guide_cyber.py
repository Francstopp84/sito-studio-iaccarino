# -*- coding: utf-8 -*-
"""18 Guide Operative e Checklist Forensi di Cybersicurezza e Protezione Dati (GUI-01 -> GUI-18)."""

GUIDE_CYBER = [
    {
        "cod": "GUI-01",
        "slug": "guida-notifica-data-breach-garante-privacy-72-ore",
        "pilastro": "data-breach-garante-privacy",
        "titolo": "Guida completa alla notifica di data breach al Garante Privacy entro 72 ore",
        "seo_title": "Guida Notifica Data Breach Garante Privacy 72 Ore | Checklist GDPR",
        "desc": "Guida operativa passo passo all'art. 33 e 34 GDPR: calcolo delle 72 ore, valutazione del rischio, compilazione portale Garante, notifica in fasi e registro interno.",
        "norme": ["Art. 33 GDPR", "Art. 34 GDPR", "Art. 83 par. 4 GDPR", "Linee guida EDPB 9/2022"],
        "intro": "Quando si verifica una violazione di sicurezza che comporta distruzione, perdita, modifica o divulgazione non autorizzata di dati personali, il titolare del trattamento deve attivare una procedura rigorosa nelle prime 72 ore dalla scoperta. Questa guida illustra i passaggi giuridici e operativi per evitare sanzioni e contestazioni.",
        "sezioni": [
            ("1. Quando decorre realmente il termine delle 72 ore", "Il termine decorre dal momento in cui il titolare acquisisce un ragionevole grado di certezza che si e' verificato un incidente di sicurezza riguardante dati personali. Una breve indagine preliminare tecnica e' ammessa, ma non puo' diventare un pretesto per ritardare la notifica oltre il ragionevole."),
            ("2. Valutazione del rischio e soglia di obbligatorieta'", "La notifica al Garante e' obbligatoria salvo che sia improbabile che la violazione presenti un rischio per i diritti e le liberta' delle persone fisiche. Se invece il rischio e' elevato (es. dati sanitari, bancari, credenziali, furto d'identita'), scatta anche l'obbligo di comunicazione diretta agli interessati ex art. 34 GDPR."),
            ("3. Notifica per fasi e registro interno dei data breach", "Se entro 72 ore l'analisi forense non e' conclusa, l'art. 33 par. 4 GDPR consente la notifica in fasi (prima notifica provvisoria seguita da integrazioni). Anche quando si decide di non notificare per rischio improbabile, la motivazione tecnica e giuridica va sempre annotata nel registro interno ex art. 33 par. 5 GDPR.")
        ],
        "checklist": [
            "Isolare i sistemi colpiti senza cancellare i log e fissare data e ora esatte della scoperta.",
            "Censire categorie di interessati, volume approssimativo dei record e tipologie di dati coinvolti.",
            "Verificare se i dati erano cifrati con chiavi non compromesse (esenzione art. 34 par. 3 lett. a).",
            "Inviare la notifica telematica sul portale del Garante Privacy tramite SPID/CIE o tramite delega al legale/DPO.",
            "Aggiornare il registro interno delle violazioni e documentare le misure correttive adottate."
        ],
        "faqs": [
            ("Posso integrare la notifica al Garante dopo le 72 ore?", "Si', l'art. 33 par. 4 GDPR prevede espressamente la possibilita' di fornire le informazioni in fasi successive senza ulteriore ingiustificato ritardo."),
            ("Se la violazione riguarda solo 5 clienti devo notificare?", "Non conta solo il numero ma la gravita' del rischio: anche pochi interessati con dati sanitari o finanziari esposti possono rendere obbligatoria la notifica.")
        ]
    },
    {
        "cod": "GUI-02",
        "slug": "guida-notifica-incidente-acn-csirt-24-ore-nis2",
        "pilastro": "direttiva-nis2-acn-legge-90-2024",
        "titolo": "Guida alla pre-notifica di incidente significativo ad ACN / CSIRT in 24 ore (NIS2)",
        "seo_title": "Guida Notifica ACN CSIRT 24 Ore NIS2 | D.Lgs. 138/2024",
        "desc": "Procedura completa per le notifiche obbligatorie NIS2: pre-notifica entro 24 ore, notifica formale entro 72 ore, relazione finale entro un mese e coordinamento col Garante.",
        "norme": ["Art. 25 D.Lgs. 138/2024", "Art. 1 L. 90/2024", "Determinazioni ACN NIS2"],
        "intro": "Il D.Lgs. 138/2024 di recepimento della Direttiva NIS2 impone ai soggetti essenziali e importanti un calendario di notifica estremamente serrato verso il CSIRT Italia presso l'ACN in caso di incidente significativo.",
        "sezioni": [
            ("1. La finestra critica delle 24 ore (Pre-notifica)", "Entro 24 ore dalla conoscenza di un incidente significativo, il Punto di Contatto NIS2 deve inviare una pre-notifica al CSIRT Italia indicando se si sospetta un atto illecito o malevolo e se l'incidente puo' avere impatto transfrontaliero."),
            ("2. La notifica di incidente entro 72 ore e la relazione finale", "Entro 72 ore va trasmessa una notifica completa con valutazione iniziale di gravita', impatto e indicatori di compromissione (IoC). Entro un mese segue la relazione finale con analisi della causa radice e misure di mitigazione."),
            ("3. Coordinamento tra ACN, Garante Privacy e Polizia Postale", "Un singolo ransomware puo' attivare contemporaneamente l'obbligo NIS2 (24h ACN), l'obbligo GDPR (72h Garante) e la denuncia penale. Le ricostruzioni devono essere perfettamente coerenti tra loro.")
        ],
        "checklist": [
            "Verificare la qualifica aziendale (soggetto essenziale, importante o fornitore PA ex L. 90/2024).",
            "Attivare il Punto di Contatto registrato sulla piattaforma ACN.",
            "Inviare la pre-notifica CSIRT entro 24 ore dalla scoperta dell'incidente significativo.",
            "Raccogliere gli indicatori di compromissione (IoC) per la notifica completa delle 72 ore.",
            "Allineare il testo della notifica ACN con l'eventuale notifica al Garante Privacy."
        ],
        "faqs": [
            ("Cosa si intende per incidente significativo NIS2?", "Un incidente che causa o puo' causare una grave perturbazione operativa dei servizi o perdite finanziarie rilevanti per il soggetto, oppure danni materiali o immateriali considerevoli a terzi."),
            ("La notifica al CSIRT sostituisce quella al Garante Privacy?", "No, sono due obblighi distinti con autorita', termini e presupposti differenti.")
        ]
    },
    {
        "cod": "GUI-03",
        "slug": "guida-querela-polizia-postale-reati-informatici",
        "pilastro": "reati-informatici-difesa-penale",
        "titolo": "Guida pratica alla querela alla Polizia Postale per reati informatici e truffe online",
        "seo_title": "Come Fare Querela alla Polizia Postale: Guida e Documenti",
        "desc": "Come redigere una querela efficace per reati informatici, phishing, ransomware o diffamazione online: termini di 3 mesi, allegati tecnici e richieste di sequestro.",
        "norme": ["Art. 124 c.p.", "Art. 336 c.p.p.", "Art. 615-ter e 640-ter c.p.", "L. 90/2024"],
        "intro": "Una denuncia generica o priva di allegati tecnici porta quasi sempre all'archiviazione contro ignoti. Redigere una querela informatica strutturata con prove digitali integre consente invece alla Procura e alla Polizia Postale di attivare subito rogatorie, sequestri e acquisizione di log.",
        "sezioni": [
            ("1. Termine perentorio di 3 mesi e procedibilita'", "Molti reati informatici e la diffamazione aggravata sono procedibili a querela della persona offesa entro 3 mesi dalla notizia del fatto. Altre fattispecie aggravate (es. estorsione informatica art. 629 co. 3 c.p.) sono procedibili d'ufficio."),
            ("2. Struttura tecnica degli allegati indispensabili", "La querela deve contenere la cronologia esatta (con fuso orario), gli URL completi, gli header delle email (.eml), gli IBAN o indirizzi wallet beneficiari e l'acquisizione forense certificata."),
            ("3. Istanze operative alla Procura della Repubblica", "Nell'atto di querela e' opportuno sollecitare subito i provvedimenti urgenti: sequestro preventivo di conti o criptovalute, acquisizione dei tabulati IP prima della scadenza di conservazione e conservazione dei log presso provider esteri.")
        ],
        "checklist": [
            "Verificare il termine di 3 mesi dalla scoperta dell'illecito.",
            "Raccogliere file originali (.eml, log, TXID, contabili bancarie) senza alterarne i metadati.",
            "Indicare chiaramente la volonta' punitiva e la riserva di costituzione di parte civile.",
            "Allegare richiesta motivata di sequestro d'urgenza se vi sono somme o beni ancora tracciabili.",
            "Depositare l'atto tramite difensore presso la Procura competente o la Polizia Postale."
        ],
        "faqs": [
            ("Basta la segnalazione online sul portale della Polizia Postale?", "La segnalazione web e' utile per l'allerta immediata ma non sostituisce la formale querela sottoscritta e depositata ai fini processuali."),
            ("Se l'autore e' all'estero conviene comunque sporgere querela?", "Si', sia per attivare i canali di cooperazione giudiziaria e il blocco su exchange/banche, sia perche' la querela e' presupposto necessario per rimborsi bancari e polizze assicurative.")
        ]
    },
    {
        "cod": "GUI-04",
        "slug": "guida-conservazione-prove-digitali-hash-forense",
        "pilastro": "ex-dipendenti-sottrazione-dati-segreti-aziendali",
        "titolo": "Guida alla preservazione delle prove digitali, copia forense e hash SHA-256",
        "seo_title": "Conservazione Prove Digitali e Hash Forense: Guida Legale",
        "desc": "Come raccogliere e conservare email, chat, pagine web, log e dispositivi per renderli inattaccabili in giudizio civile e penale secondo gli standard forensi ISO 27037.",
        "norme": ["Art. 2712 c.c.", "Art. 254-bis c.p.p.", "L. 48/2008", "Standard ISO/IEC 27037"],
        "intro": "Nel processo moderno le prove digitali decidono l'esito della causa, ma sono estremamente fragili: un semplice riavvio, una stampa parziale o una copia manuale possono comprometterne l'utilizzabilita'.",
        "sezioni": [
            ("1. Cos'e' la catena di custodia digitale", "La catena di custodia documenta chi ha acquisito il dato, quando, con quali strumenti e con quale impronta crittografica (hash SHA-256), garantendo che il file prodotto in giudizio e' identico bit per bit all'originale."),
            ("2. Acquisizione di contenuti web, social e chat", "Per pagine web, recensioni false o post social non bastano screenshot ritagliati: occorre un'acquisizione certificata di sessione con marca temporale qualificata e pacchetto forense."),
            ("3. Conservazione di PC, server e smartphone", "In caso di intrusione, ransomware o infedelta' di un dipendente, il dispositivo non va utilizzato ne' formattato: si esegue una copia bit-stream tramite write-blocker hardware.")
        ],
        "checklist": [
            "Non spegnere o riavviare macchine compromesse senza indicazione del tecnico forense (per non perdere la RAM).",
            "Salvare sempre i file originali (.eml, .p7m, video, audio) evitando conversioni che cancellano i metadati.",
            "Calcolare l'hash SHA-256 e apporre marca temporale qualificata.",
            "Documentare ogni passaggio in un verbale di acquisizione.",
            "Conservare almeno due copie integre in luogo sicuro fino alla definizione del giudizio."
        ],
        "faqs": [
            ("Uno screenshot di WhatsApp ha valore legale?", "Può avere valore indiziario ex art. 2712 c.c., ma se la controparte lo disconosce motivatamente occorre disporre del dispositivo originale o di una copia forense certificata."),
            ("Quanto costa una copia forense certificata?", "Dipende dal tipo di acquisizione (una singola pagina web certificata richiede poche ore, mentre l'imaging completo di server aziendali richiede un intervento dedicato).")
        ]
    },
    {
        "cod": "GUI-05",
        "slug": "guida-rimborso-phishing-bancario-reclamo-abf",
        "pilastro": "truffe-online-phishing-sim-swap-banche",
        "titolo": "Guida al rimborso per phishing, smishing e frodi bancarie davanti all'ABF",
        "seo_title": "Guida Rimborso Phishing Bancario e Ricorso ABF | D.Lgs. 11/2010",
        "desc": "Come ottenere dalla banca il rimborso delle somme sottratte con phishing o SMS spoofing: onere della prova PSD2, reclamo PEC, ricorso ABF e azione giudiziaria.",
        "norme": ["Art. 10 D.Lgs. 11/2010", "Art. 12 D.Lgs. 11/2010", "Disposizioni Banca d'Italia su ABF"],
        "intro": "Le banche respingono spesso automaticamente i reclami dei clienti truffati invocando la presunta colpa grave. La legge (D.Lgs. 11/2010) pone tuttavia un onere probatorio severissimo a carico dell'intermediario.",
        "sezioni": [
            ("1. L'onere della prova a carico della banca", "Ai sensi dell'art. 10 D.Lgs. 11/2010, spetta alla banca provare che l'operazione e' stata autenticata con autenticazione forte (SCA), correttamente registrata e contabilizzata e non ha subito malfunzionamenti. Inoltre la banca deve provare il dolo o la colpa grave del cliente."),
            ("2. Reclamo preventivo PEC e termine di risposta", "Prima di ricorrere all'ABF e' obbligatorio inviare un reclamo formale alla banca, che ha 15 giorni lavorativi (per i servizi di pagamento) per rispondere motivatamente."),
            ("3. Ricorso all'Arbitro Bancario Finanziario o al Tribunale", "Se la banca nega il rimborso o non risponde, si deposita il ricorso all'ABF (costo vivo 20 euro, decisione rapida su base documentale) oppure, per importi elevati o casi che richiedono istruttoria tecnica, si agisce in Tribunale.")
        ],
        "checklist": [
            "Bloccare subito carte e credenziali e sporgere denuncia querela dettagliata.",
            "Conservare SMS spoofing, email phishing, registro chiamate ed estratti conto.",
            "Inviare reclamo PEC chiedendo il rimborso integrale e la produzione dei log SCA completi.",
            "Attendere i 15 giorni lavorativi di risposta della banca.",
            "Depositare il ricorso ABF o avviare l'azione giudiziaria con assistenza legale tecnica."
        ],
        "faqs": [
            ("Se ho inserito i codici su un sito identico a quello della banca perdo sempre il rimborso?", "No: la giurisprudenza ABF e di merito valuta la sofisticazione dell'inganno (es. SMS spoofing nello stesso thread della banca, caller ID spoofing) e la diligenza dei sistemi antifrode dell'istituto."),
            ("Quanto tempo serve per una decisione ABF?", "In media alcuni mesi dal deposito, con procedura interamente telematica e senza necessita' di udienze fisiche.")
        ]
    },
    {
        "cod": "GUI-06",
        "slug": "guida-rimozione-contenuti-google-meta-tiktok-dsa",
        "pilastro": "reputazione-online-deepfake-revenge-porn",
        "titolo": "Guida alla rimozione urgente di contenuti diffamatori su Google, Meta e TikTok (DSA)",
        "seo_title": "Rimozione Contenuti Online su Google, Meta e TikTok | Guida DSA",
        "desc": "Come usare il Digital Services Act (Reg. UE 2022/2065), le segnalazioni legali qualificate e il ricorso ex art. 700 c.p.c. per rimuovere post, video e recensioni illecite.",
        "norme": ["Art. 16 Reg. UE 2022/2065 (DSA)", "Art. 17 GDPR", "Art. 700 c.p.c."],
        "intro": "Il Digital Services Act ha rafforzato gli obblighi delle grandi piattaforme online nella gestione delle segnalazioni di contenuti illegali. Una richiesta redatta in modo tecnicamente preciso aumenta drasticamente i tassi di rimozione rapida.",
        "sezioni": [
            ("1. Meccanismo di segnalazione qualificata ex art. 16 DSA", "Le piattaforme devono offrire canali accessibili e decidere in modo tempestivo e motivato sulle segnalazioni che indicano URL esatti, norme violate e ragioni dell'illiceita'."),
            ("2. Deindicizzazione sui motori di ricerca", "Quando il sito sorgente e' ospitato all'estero o non collabora, la deindicizzazione su Google e Bing abbatte la visibilita' del contenuto lesivo sulle ricerche per nome e cognome."),
            ("3. Ricorso cautelare d'urgenza ex art. 700 c.p.c.", "Se la piattaforma rigetta la richiesta nonostante la palese illiceita', l'ordine del giudice civile impone la rimozione immediata con penalita' giornaliere di mora.")
        ],
        "checklist": [
            "Cristallizzare tutti gli URL e i contenuti con acquisizione forense prima della segnalazione.",
            "Individuare il profilo giuridico preciso (diffamazione, violazione privacy, marchio, impersonation).",
            "Inviare la notice-and-action formale tramite i canali legali della piattaforma.",
            "Tracciare numeri di ticket e risposte ricevute per l'eventuale reclamo al Garante o al giudice.",
            "Valutare in parallelo la querela penale entro 3 mesi contro l'autore."
        ],
        "faqs": [
            ("Quanto tempo impiega Google a valutare una richiesta di deindicizzazione?", "Generalmente da pochi giorni a qualche settimana, a seconda della complessita' del bilanciamento tra privacy e interesse pubblico."),
            ("Posso chiedere la rimozione senza conoscere il nome reale dell'autore del profilo falso?", "Si', la richiesta alla piattaforma e la deindicizzazione possono essere avviate subito, mentre l'identificazione avviene tramite la Procura.")
        ]
    },
    {
        "cod": "GUI-07",
        "slug": "guida-adeguamento-direttiva-nis2-pmi-italiane",
        "pilastro": "direttiva-nis2-acn-legge-90-2024",
        "titolo": "Guida all'adeguamento NIS2 per PMI e medie imprese italiane (D.Lgs. 138/2024)",
        "seo_title": "Adeguamento NIS2 Aziende Italiane: Guida D.Lgs. 138/2024",
        "desc": "Roadmap legale e organizzativa per l'adeguamento NIS2: verifica perimetro, registrazione ACN, responsabilita' CdA, misure di sicurezza e contratti fornitori.",
        "norme": ["D.Lgs. 138/2024", "Art. 23, 24, 25 e 38 D.Lgs. 138/2024"],
        "intro": "La Direttiva NIS2, recepita in Italia con il D.Lgs. 138/2024, trasforma la cybersicurezza da tema puramente informatico a obbligo di governance societaria direttamente in capo agli amministratori.",
        "sezioni": [
            ("1. Verifica del perimetro e registrazione ACN", "Occorre verificare se l'impresa opera nei settori degli Allegati I o II e supera le soglie dimensionali di media impresa (tenendo conto anche di controllate e collegate), procedendo alla registrazione e all'aggiornamento annuale su ACN."),
            ("2. Responsabilita' degli organi di amministrazione", "L'art. 23 D.Lgs. 138/2024 impone al CdA di approvare le modalita' di attuazione delle misure di gestione del rischio, sovrintendere alla loro applicazione e seguire una formazione periodica specifica."),
            ("3. Sicurezza della catena di fornitura (Supply Chain)", "Le aziende NIS2 devono estendere i requisiti di cybersicurezza ai propri fornitori ICT tramite clausole contrattuali dedicate, audit e obblighi di notifica rapida degli incidenti.")
        ],
        "checklist": [
            "Verificare formalmente l'assoggettamento al D.Lgs. 138/2024 e conservare il parere di scoping.",
            "Completare la registrazione e la nomina del Punto di Contatto sulla piattaforma ACN.",
            "Far approvare dal CdA il piano di adeguamento e il budget cybersicurezza.",
            "Implementare le misure di base ACN (MFA, backup offline, gestione vulnerabilita', continuita' operativa).",
            "Aggiornare i contratti con i fornitori IT inserendo clausole di notifica incidente entro 12-24 ore."
        ],
        "faqs": [
            ("Anche una piccola impresa puo' essere coinvolta dalla NIS2?", "Si', sia in casi eccezionali di criticita' settoriale, sia indirettamente come fornitore della catena di approvvigionamento di grandi clienti soggetti a NIS2."),
            ("A quanto ammontano le sanzioni NIS2?", "Fino a 10 milioni di euro o al 2% del fatturato mondiale annuo per i soggetti essenziali, e fino a 7 milioni o all'1,4% per i soggetti importanti.")
        ]
    },
    {
        "cod": "GUI-08",
        "slug": "guida-modello-231-cybersicurezza-art-24-bis",
        "pilastro": "modello-231-reati-informatici",
        "titolo": "Guida al Modello 231 e ai reati informatici (art. 24-bis dopo la L. 90/2024)",
        "seo_title": "Modello 231 e Reati Informatici Art. 24-bis | Guida Legge 90/2024",
        "desc": "Come integrare la cybersicurezza nel Modello Organizzativo 231 dopo la Legge 90/2024: reati presupposto, protocolli IT, flussi OdV ed esimente per la societa'.",
        "norme": ["Art. 24-bis D.Lgs. 231/2001", "L. 90/2024", "Art. 6 e 7 D.Lgs. 231/2001"],
        "intro": "La Legge 90/2024 ha ampliato e aggravato le sanzioni a carico degli enti per i delitti informatici, includendo l'estorsione informatica e aumentando le quote pecuniarie e interdittive.",
        "sezioni": [
            ("1. I reati informatici presupposto dell'art. 24-bis", "Rientrano nel catalogo l'accesso abusivo a sistemi informatici, l'intercettazione illecita, il danneggiamento di dati e sistemi, le falsita' in documenti informatici e le nuove fattispecie introdotte dalla L. 90/2024."),
            ("2. Protocolli concreti per l'efficacia esimente", "Un Modello 231 efficace deve prevedere segregazione dei ruoli amministrativi, gestione rigorosa di credenziali e licenze software, controllo sugli accessi a portali PA e procedure di incident response."),
            ("3. Flussi informativi verso l'Organismo di Vigilanza", "Ogni anomalia di sicurezza, data breach o contestazione su accessi abusivi deve generare un flusso informativo documentato verso l'OdV.")
        ],
        "checklist": [
            "Aggiornare la mappatura dei rischi 231 alle novita' della Legge 90/2024.",
            "Verificare la coerenza tra Parte Speciale 231, policy GDPR e misure NIS2.",
            "Definire procedure scritte per gestione password, profili privilegiati e disattivazione ex dipendenti.",
            "Attivare flussi periodici e ad evento verso l'Organismo di Vigilanza.",
            "Documentare la formazione annuale del personale sui rischi penali informatici."
        ],
        "faqs": [
            ("L'adozione del Modello 231 e' obbligatoria per legge?", "No, ma e' l'unico strumento che consente alla societa' di evitare pesanti sanzioni pecuniarie e interdittive in caso di reato commesso da dipendenti o dirigenti."),
            ("La certificazione ISO 27001 sostituisce il Modello 231?", "No, costituisce una solida base tecnica ma va integrata con i protocolli giuridici, il sistema disciplinare e la vigilanza dell'OdV.")
        ]
    },
    {
        "cod": "GUI-09",
        "slug": "guida-dpo-registro-trattamenti-art-30-gdpr",
        "pilastro": "compliance-gdpr-dpo-privacy",
        "titolo": "Guida al DPO e al Registro dei trattamenti (art. 30 e 37 GDPR) per imprese e studi",
        "seo_title": "Guida DPO e Registro Trattamenti Art. 30 GDPR per Aziende",
        "desc": "Quando il DPO e' obbligatorio, come compilare un Registro dei trattamenti a prova di ispezione GdF/Garante e come evitare errori formali sanzionabili.",
        "norme": ["Art. 30 GDPR", "Artt. 37-39 GDPR", "Linee guida WP243 sul DPO"],
        "intro": "Il Registro delle attivita' di trattamento e' il primo documento richiesto dal Garante Privacy o dalla Guardia di Finanza durante un'ispezione. Accanto ad esso, la corretta valutazione sulla nomina del DPO evita sanzioni immediate.",
        "sezioni": [
            ("1. Chi deve tenere il Registro dei trattamenti", "Sebbene l'art. 30 par. 5 preveda un'esenzione per le imprese sotto i 250 dipendenti, tale esenzione cade se il trattamento non e' occasionale o riguarda dati particolari/giudiziari: nella pratica quasi tutte le aziende e gli studi professionali devono tenerlo aggiornato."),
            ("2. Quando il DPO e' obbligatorio e requisiti di indipendenza", "Il DPO e' obbligatorio per enti pubblici e per soggetti privati che effettuano monitoraggio regolare e sistematico su larga scala o trattano su larga scala dati sanitari o giudiziari. Deve operare senza conflitti di interesse."),
            ("3. Aggiornamento continuo e accountability", "Il Registro non e' un documento statico: va aggiornato ogni volta che si introduce un nuovo software, un CRM, una telecamera o uno strumento di AI.")
        ],
        "checklist": [
            "Mappare tutti i processi aziendali (HR, clienti, fornitori, marketing, videosorveglianza, IT).",
            "Indicare per ogni trattamento base giuridica, tempi di conservazione e misure di sicurezza.",
            "Verificare se sussiste l'obbligo di nomina del DPO e comunicare i dati sul portale del Garante.",
            "Assicurare che il DPO non ricopra ruoli decisionali in conflitto (es. CEO o responsabile IT interno).",
            "Programmare un riesame annuale documentato del Registro."
        ],
        "faqs": [
            ("Il responsabile IT interno puo' fare il DPO?", "Di regola no, perche' il Garante ha piu' volte sanzionato il conflitto di interessi di chi determina le modalita' tecniche dei trattamenti e dovrebbe poi controllarle."),
            ("Quanto costa un DPO esterno?", "Varia in base alla complessita' dell'azienda, ma il DPO esterno garantisce indipendenza e copertura specialistica continua.")
        ]
    },
    {
        "cod": "GUI-10",
        "slug": "guida-dpia-valutazione-impatto-art-35-gdpr",
        "pilastro": "compliance-gdpr-dpo-privacy",
        "titolo": "Guida alla DPIA (Valutazione d'Impatto Privacy ex art. 35 GDPR)",
        "seo_title": "Guida DPIA Art. 35 GDPR: Quando e' Obbligatoria e Come Farla",
        "desc": "Quando occorre redigere la DPIA prima di avviare un nuovo software, un sistema di AI, la videosorveglianza o il monitoraggio dipendenti, con checklist operativa.",
        "norme": ["Art. 35 GDPR", "Art. 36 GDPR", "Provvedimento Garante elenco trattamenti DPIA"],
        "intro": "La Valutazione d'Impatto sulla Protezione dei Dati (DPIA) e' obbligatoria prima di iniziare qualsiasi trattamento che presenti un rischio elevato per i diritti e le liberta' delle persone fisiche.",
        "sezioni": [
            ("1. Casi in cui la DPIA e' sempre obbligatoria", "Trattamenti su larga scala di dati sanitari o biometrici, profilazione con effetti significativi, sistemi di geolocalizzazione o controllo lavoratori, piattaforme whistleblowing e nuovi progetti basati su AI."),
            ("2. Contenuto minimo legale della DPIA", "Descrizione sistematica dei flussi di dati, valutazione di necessita' e proporzionalita', analisi dettagliata dei rischi per gli interessati e misure tecniche/organizzative per ridurli."),
            ("3. Consultazione del DPO e riesame periodico", "Il parere del DPO va acquisito e documentato; se il rischio residuo resta elevato occorre consultare preventivamente il Garante ex art. 36 GDPR.")
        ],
        "checklist": [
            "Eseguire uno screening DPIA prima del lancio di ogni nuovo progetto digitale o AI.",
            "Coinvolgere congiuntamente legale privacy, IT, DPO e responsabile di business.",
            "Valutare rischi di accesso abusivo, perdita dati e decisioni automatizzate discriminatorie.",
            "Documentare le contromisure adottate (cifratura, minimizzazione, pseudonimizzazione).",
            "Archiviare la DPIA firmata e riesaminarla in caso di modifiche sostanziali."
        ],
        "faqs": [
            ("Posso fare la DPIA dopo aver gia' attivato il software?", "No, la legge richiede che la DPIA sia preventiva; se manca, va redatta con la massima urgenza in sede di sanatoria."),
            ("La DPIA va inviata al Garante?", "Solo se il rischio residuo rimane elevato nonostante le misure di mitigazione; altrimenti va conservata in azienda per eventuali ispezioni.")
        ]
    },
    {
        "cod": "GUI-11",
        "slug": "guida-contratti-dpa-fornitori-art-28-gdpr",
        "pilastro": "compliance-gdpr-dpo-privacy",
        "titolo": "Guida ai contratti DPA e alla nomina dei Responsabili del Trattamento (art. 28 GDPR)",
        "seo_title": "Guida DPA Art. 28 GDPR: Nomina Fornitori IT, Cloud e Consulenti",
        "desc": "Come regolare giuridicamente i rapporti con software house, cloud provider, agenzie marketing e consulenti del lavoro per proteggere l'azienda da responsabilita' solidale.",
        "norme": ["Art. 28 GDPR", "Art. 29 GDPR", "Art. 82 GDPR"],
        "intro": "Ogni fornitore esterno che tratta dati personali per conto dell'azienda (gestionale, cloud, paghe, marketing, assistenza IT) deve essere vincolato da un contratto conforme all'art. 28 GDPR (DPA).",
        "sezioni": [
            ("1. Clausole essenziali di un DPA blindato", "Oggetto e durata, istruzioni documentate, obbligo di riservatezza, misure tecniche art. 32, disciplina dei sub-responsabili, assistenza nei data breach entro termini certi (es. 24 ore) e restituzione/cancellazione dati a fine contratto."),
            ("2. Clausole di manleva e riparto di responsabilita'", "Nei contratti SaaS standard i fornitori limitano spesso la propria responsabilita' a poche mensilita': una negoziazione mirata protegge il titolare in caso di data breach imputabile al provider."),
            ("3. Controllo dei sub-responsabili", "Il titolare deve conoscere e autorizzare i sub-fornitori usati dal provider, verificando eventuali trasferimenti di dati fuori dallo Spazio Economico Europeo.")
        ],
        "checklist": [
            "Censire tutti i fornitori esterni che accedono a dati aziendali o clienti.",
            "Stipulare un DPA art. 28 GDPR prima di concedere credenziali o flussi di dati.",
            "Inserire l'obbligo del fornitore di segnalare incidenti entro 24 ore dalla scoperta.",
            "Verificare l'elenco aggiornato dei sub-responsabili e la sede dei server.",
            "Prevedere la cancellazione certificata dei dati alla cessazione del contratto."
        ],
        "faqs": [
            ("Il commercialista o il consulente del lavoro va nominato ex art. 28?", "Il consulente del lavoro che elabora le buste paga per conto dell'azienda opera di regola come Responsabile ex art. 28; per alcuni incarichi autonomi il professionista puo' operare come Titolare autonomo."),
            ("Cosa rischio se manca il DPA con un fornitore IT?", "Sanzione autonoma del Garante per violazione dell'art. 28 GDPR e forte indebolimento della rivalsa in caso di violazione dati.")
        ]
    },
    {
        "cod": "GUI-12",
        "slug": "guida-ai-act-aziende-italiane-regolamento-2024-1689",
        "pilastro": "contratti-it-cloud-saas-ai-act",
        "titolo": "Guida pratica all'AI Act (Reg. UE 2024/1689) per imprese e professionisti italiani",
        "seo_title": "Guida AI Act per Aziende Italiane | Reg. UE 2024/1689",
        "desc": "Cosa cambia con l'AI Act europeo e la normativa italiana: sistemi vietati, AI ad alto rischio, obbligo di alfabetizzazione AI (art. 4), trasparenza e governance.",
        "norme": ["Reg. UE 2024/1689 (AI Act)", "Art. 4 AI Act (AI Literacy)", "Art. 5 AI Act (Pratiche vietate)", "GDPR"],
        "intro": "L'AI Act introduce un quadro normativo basato sul rischio che riguarda non solo gli sviluppatori di intelligenza artificiale, ma anche tutte le imprese che utilizzano sistemi AI (deployer) in ambito HR, credito, marketing e customer care.",
        "sezioni": [
            ("1. Pratiche AI vietate e obbligo di alfabetizzazione (Art. 4 e 5)", "Sono vietati sistemi di social scoring, manipolazione subliminale e riconoscimento emozioni sul luogo di lavoro. E' gia' vigente l'obbligo per le aziende di assicurare un livello adeguato di alfabetizzazione AI del personale."),
            ("2. Sistemi AI ad alto rischio (HR, selezione, credito)", "Chi usa l'AI per filtrare curriculum, valutare dipendenti o concedere credito deve rispettare obblighi rigorosi di supervisione umana, informativa ai lavoratori/clienti, conservazione log e valutazione d'impatto."),
            ("3. Obblighi di trasparenza e contenuti sintetici", "Chatbot, sistemi di interazione automatica e contenuti audio/video generati o manipolati (deepfake) richiedono una chiara informativa agli utenti.")
        ],
        "checklist": [
            "Creare l'inventario di tutti gli strumenti AI usati in azienda (anche integrati nei software).",
            "Verificare l'assenza di pratiche vietate ex art. 5 AI Act (es. monitoraggio emotivo dipendenti).",
            "Adottare una Policy AI interna e svolgere la formazione obbligatoria di AI literacy.",
            "Aggiornare informative privacy e DPIA per i processi che integrano l'intelligenza artificiale.",
            "Controllare i contratti con i fornitori AI su proprieta' intellettuale e non utilizzo dei dati per training."
        ],
        "faqs": [
            ("L'AI Act si applica anche se usiamo solo ChatGPT o Copilot in ufficio?", "Si', in qualita' di deployer l'azienda e' comunque tenuta agli obblighi di alfabetizzazione AI, trasparenza, protezione dati GDPR e tutela dei segreti aziendali."),
            ("Quali sono le sanzioni massime dell'AI Act?", "Fino a 35 milioni di euro o al 7% del fatturato mondiale annuo per l'uso di sistemi AI vietati.")
        ]
    },
    {
        "cod": "GUI-13",
        "slug": "guida-videosorveglianza-lavoro-art-4-statuto-lavoratori",
        "pilastro": "compliance-gdpr-dpo-privacy",
        "titolo": "Guida alla videosorveglianza aziendale a norma (art. 4 Statuto Lavoratori e GDPR)",
        "seo_title": "Videosorveglianza Aziendale a Norma: Guida Art. 4 e ITL",
        "desc": "Come installare telecamere in negozi, uffici e stabilimenti evitando sanzioni penali e privacy: istanza ITL, accordo sindacale, cartelli e tempi di conservazione.",
        "norme": ["Art. 4 L. 300/1970", "Art. 13 GDPR", "Linee guida EDPB 3/2019"],
        "intro": "L'installazione di impianti di videosorveglianza in presenza di lavoratori dipendenti richiede il rispetto cumulativo delle regole giuslavoristiche e della disciplina GDPR.",
        "sezioni": [
            ("1. Accordo sindacale o autorizzazione ITL prima dell'installazione", "Le telecamere possono essere installate solo per esigenze organizzative, produttive, sicurezza del lavoro o tutela del patrimonio, previo accordo con RSA/RSU o autorizzazione dell'Ispettorato Territoriale del Lavoro."),
            ("2. Cartellonistica, informativa e tempi di conservazione", "Occorre esporre cartelli ben visibili prima del raggio d'azione, rendere disponibile l'informativa estesa e limitare la conservazione delle immagini a 24-48 ore (salvo motivate esigenze di sicurezza)."),
            ("3. Accesso alle immagini e fornitori esterni", "L'accesso ai filmati deve essere protetto da credenziali personali, tracciato e affidato a soggetti autorizzati per iscritto, con DPA art. 28 verso l'istituto di vigilanza.")
        ],
        "checklist": [
            "Non installare ne' attivare telecamere prima di aver ottenuto accordo sindacale o autorizzazione ITL.",
            "Predisporre planimetria tecnica con coni di ripresa che evitino aree di riposo o spogliatoi.",
            "Affiggere cartelli aggiornati con indicazione del titolare e delle finalita'.",
            "Configurare la sovrascrittura automatica entro 24-48 ore.",
            "Consegnare informativa ai lavoratori sulle modalita' d'uso e sui controlli."
        ],
        "faqs": [
            ("Se tutti i dipendenti firmano una liberatoria posso installare le telecamere?", "No: la Corte di Cassazione ha ribadito che il consenso dei singoli dipendenti non sostituisce mai l'accordo sindacale o l'autorizzazione ITL."),
            ("Posso guardare le telecamere dallo smartphone da remoto?", "Solo se espressamente previsto nell'autorizzazione ITL/accordo e con rigide limitazioni contro il controllo continuo a distanza dei lavoratori.")
        ]
    },
    {
        "cod": "GUI-14",
        "slug": "guida-ransomware-prime-72-ore-piano-crisi-legale",
        "pilastro": "ransomware-estorsione-informatica",
        "titolo": "Guida Ransomware: il piano legale delle prime 72 ore per imprenditori e CdA",
        "seo_title": "Piano Legale Ransomware 72 Ore per Aziende | Guida Operativa",
        "desc": "Cosa fare ora per ora dopo un attacco ransomware con cifratura dei server ed esfiltrazione dati: isolamento, riscatto, ACN, Garante Privacy, polizza cyber e denuncia.",
        "norme": ["Art. 629 comma 3 c.p. (L. 90/2024)", "Art. 33 GDPR", "Art. 25 D.Lgs. 138/2024"],
        "intro": "Un attacco ransomware colpisce contemporaneamente l'operativita' aziendale, la riservatezza dei dati e la responsabilita' degli amministratori. Le decisioni prese nelle prime ore determinano l'esito legale dell'intera crisi.",
        "sezioni": [
            ("1. Gestione della prima ora e perimetro forense", "Disconnettere i sistemi infetti dalla rete senza spegnerli bruscamente, attivare il team forense e il legale cyber sotto segreto professionale (legal privilege) e verificare l'integrita' dei backup offline."),
            ("2. Il nodo del riscatto e della doppia estorsione", "I gruppi ransomware esfiltrano i dati prima di cifrarli minacciandone la pubblicazione. Pagare il riscatto non garantisce la distruzione dei file e comporta gravi rischi legali (inclusi profili sanzionatori internazionali e antiriciclaggio)."),
            ("3. Gestione coordinata di ACN, Garante, assicurazione e clienti", "Attivare la polizza cyber entro le prime ore, rispettare le finestre di 24h (ACN se NIS2) e 72h (Garante Privacy) e preparare comunicazioni verificate per clienti, banche e dipendenti.")
        ],
        "checklist": [
            "Isolare la rete e congelare le prove forensi senza formattare le macchine.",
            "Attivare subito legale cyber, team IT di incident response e assicurazione cyber.",
            "Verificare se vi e' stata esfiltrazione di dati personali (doppia estorsione).",
            "Rispettare i termini di 24h (ACN) e 72h (Garante Privacy) con testi coerenti.",
            "Depositare denuncia querela per estorsione informatica ex art. 629 comma 3 c.p."
        ],
        "faqs": [
            ("Se ripristino tutto dai backup devo comunque notificare al Garante?", "Dipende: se i criminali hanno solo cifrato ma anche copiato dati personali all'esterno, oppure se la perdita di disponibilita' ha creato rischi seri, la notifica resta obbligatoria."),
            ("Conviene negoziare con gli hacker?", "Mai in autonomia: ogni contatto espone a rischi giuridici e tattici e va gestito solo nell'ambito di una strategia forense e legale rigorosa.")
        ]
    },
    {
        "cod": "GUI-15",
        "slug": "guida-polizza-cyber-clausole-critiche-aziende",
        "pilastro": "ransomware-estorsione-informatica",
        "titolo": "Guida alle polizze cyber per aziende: clausole di esclusione e gestione del sinistro",
        "seo_title": "Polizza Cyber Aziendale: Clausole Critiche e Gestione Sinistri",
        "desc": "Come leggere una polizza cyber prima della firma e come evitare il rifiuto dell'indennizzo dopo un incidente: questionario IT, social engineering, sub-limiti e tempi di denuncia.",
        "norme": ["Artt. 1892-1893 c.c.", "Art. 1913 c.c.", "Art. 1341 e 1370 c.c."],
        "intro": "Molte imprese sottoscrivono polizze cyber senza verificare la corrispondenza tra il questionario assuntivo e la propria reale infrastruttura IT, scoprendo esclusioni decisive solo dopo l'attacco.",
        "sezioni": [
            ("1. Il rischio del questionario pre-contrattuale", "Dichiarare la presenza di MFA universale o backup immutabili quando non sono realmente attivi su tutti i sistemi puo' consentire alla compagnia di eccepire l'annullamento o la riduzione dell'indennizzo ex artt. 1892-1893 c.c."),
            ("2. Estensioni spesso escluse o sub-limitate", "Le frodi BEC (falso bonifico / social engineering), le sanzioni amministrative GDPR, i danni reputazionali e i guasti di fornitori cloud sono frequentemente oggetto di esclusioni o massimali ridotti."),
            ("3. Obblighi immediati in caso di sinistro", "Le polizze impongono spesso la denuncia entro 24-72 ore e il ricorso a fornitori forensi convenzionati: violare tali procedure puo' pregiudicare il rimborso.")
        ],
        "checklist": [
            "Verificare con il reparto IT ogni singola risposta data nel questionario assuntivo.",
            "Controllare la copertura specifica per social engineering, BEC e fermo attivita'.",
            "Annotare il numero di emergenza sinistri cyber nel piano di crisi aziendale.",
            "Chiedere conferma scritta alla compagnia prima di sostenere spese forensi rilevanti.",
            "Documentare analiticamente tutti i costi di ripristino e il mancato fatturato."
        ],
        "faqs": [
            ("La polizza cyber copre le sanzioni del Garante Privacy?", "In Italia le sanzioni amministrative sono di regola non assicurabili per legge, ma la polizza puo' coprire spese legali di difesa, perizie forensi, gestione crisi e risarcimenti civili verso terzi."),
            ("Posso contestare il rifiuto dell'assicurazione?", "Si', esaminando l'effettiva incidenza della presunta inesattezza e l'eventuale vessatorieta' o ambiguita' delle clausole di esclusione.")
        ]
    },
    {
        "cod": "GUI-16",
        "slug": "guida-diritto-all-oblio-deindicizzazione-google",
        "pilastro": "reputazione-online-deepfake-revenge-porn",
        "titolo": "Guida al diritto all'oblio e alla deindicizzazione su Google (art. 17 GDPR e art. 64-ter)",
        "seo_title": "Guida Diritto all'Oblio e Deindicizzazione Google | Art. 17 GDPR",
        "desc": "Quando si ha diritto a far sparire vecchie notizie da Google: riforma Cartabia (art. 64-ter disp. att. c.p.p.), bilanciamento cronaca/privacy, reclamo al Garante e ricorso.",
        "norme": ["Art. 17 GDPR", "Art. 64-ter disp. att. c.p.p.", "Linee guida EDPB 5/2019"],
        "intro": "Il diritto all'oblio tutela la persona contro la permanenza indefinita sui motori di ricerca di notizie superate, non piu' di interesse pubblico o smentite da un'assoluzione o archiviazione.",
        "sezioni": [
            ("1. La corsia preferenziale dell'art. 64-ter disp. att. c.p.p.", "Introdotto dalla Riforma Cartabia, consente all'imputato assolto o all'indagato archiviato di ottenere l'attestazione giudiziale per la preclusione all'indicizzazione o la deindicizzazione dai motori di ricerca."),
            ("2. Criteri di bilanciamento per altre notizie risalenti", "Anche fuori dai casi di assoluzione, si valuta il tempo trascorso, il ruolo non pubblico della persona, l'esito della vicenda e il pregiudizio sproporzionato alla vita professionale o privata."),
            ("3. Tutela contro il rifiuto del motore di ricerca o dell'editore", "In caso di rigetto da parte di Google o della testata, si puo' proporre reclamo formale al Garante Privacy o ricorso diretto al Tribunale.")
        ],
        "checklist": [
            "Raccogliere tutti gli URL esatti e le chiavi di ricerca che fanno emergere la notizia.",
            "Acquisire copia conforme di sentenze di assoluzione, decreti di archiviazione o riabilitazioni.",
            "Valutare l'istanza ex art. 64-ter disp. att. c.p.p. presso il giudice competente.",
            "Presentare richiesta motivata di deindicizzazione a Google/Bing e di aggiornamento/anonimizzazione agli editori.",
            "In caso di diniego, agire avanti al Garante Privacy o al Tribunale."
        ],
        "faqs": [
            ("La deindicizzazione cancella l'articolo dal sito del giornale?", "No, impedisce che l'articolo appaia cercando il tuo nome su Google; per intervenire direttamente sull'articolo occorre rivolgersi anche all'editore."),
            ("Quanto tempo deve passare per chiedere il diritto all'oblio?", "Non esiste un numero fisso di anni valido per tutti: in caso di assoluzione o archiviazione si puo' agire subito; per altri fatti conta la perdita di interesse pubblico attuale.")
        ]
    },
    {
        "cod": "GUI-17",
        "slug": "guida-sequestro-dispositivi-informatici-difesa-penale",
        "pilastro": "ex-dipendenti-sottrazione-dati-segreti-aziendali",
        "titolo": "Guida alla difesa contro il sequestro probatorio di smartphone, PC e server",
        "seo_title": "Sequestro Smartphone e PC nel Processo Penale: Guida alla Difesa",
        "desc": "Diritti dell'indagato e del terzo durante perquisizioni informatiche e sequestri di cellulari o server: proporzionalita', riesame 10 giorni, CTP e dissequestro.",
        "norme": ["Artt. 247, 254, 254-bis e 324 c.p.p.", "Art. 360 c.p.p."],
        "intro": "Smartphone e computer contengono oggi l'intera sfera personale, familiare e lavorativa di una persona. La giurisprudenza della Cassazione impone limiti severi contro i sequestri esplorativi o indiscriminati.",
        "sezioni": [
            ("1. Il principio di proporzionalita' nel sequestro informatico", "Il decreto di sequestro deve spiegare perche' e' necessario acquisire l'intero dispositivo, quale sia il nesso pertinenziale con il reato e quali criteri selettivi (parole chiave, arco temporale) guideranno l'estrazione."),
            ("2. Impugnazione entro 10 giorni al Tribunale del Riesame", "Contro il sequestro probatorio privo di adeguata motivazione o sproporzionato si propone richiesta di riesame entro 10 giorni dall'esecuzione."),
            ("3. Ruolo del Consulente Tecnico di Parte (CTP)", "La nomina immediata di un informatico forense consente di controllare l'integrita' della copia bit-stream e di opporsi all'acquisizione di chat o file estranei all'indagine.")
        ],
        "checklist": [
            "Richiedere copia del decreto del PM e verificare attentamente il verbale di sequestro e i sigilli.",
            "Contattare immediatamente il difensore per rispettare il termine perentorio di 10 giorni per il riesame.",
            "Chiedere la restituzione tempestiva dell'originale previa estrazione della sola copia pertinente.",
            "Nominare un CTP informatico in caso di avviso di accertamento tecnico ex art. 360 c.p.p.",
            "Documentare l'eventuale blocco di attivita' aziendale o professionale per accelerare il dissequestro."
        ],
        "faqs": [
            ("Sono obbligato a fornire il PIN o la password del mio cellulare durante la perquisizione?", "L'indagato ha diritto al silenzio e non e' obbligato a collaborare contro se' stesso; la scelta va sempre valutata con il difensore in base al caso concreto."),
            ("Quanto tempo possono tenere sequestrato il mio telefono?", "Solo per il tempo strettamente necessario a estrarre la copia forense dei dati pertinenti, dopodiche' va chiesta la restituzione.")
        ]
    },
    {
        "cod": "GUI-18",
        "slug": "guida-compliance-ecommerce-cookie-marketing-gdpr",
        "pilastro": "compliance-gdpr-dpo-privacy",
        "titolo": "Guida alla compliance privacy, cookie e marketing per siti web ed e-commerce",
        "seo_title": "Compliance GDPR E-commerce, Cookie e Marketing | Guida Legale",
        "desc": "Checklist legale completa per mettere a norma un e-commerce italiano: privacy policy, cookie banner conforme al Garante, checkbox marketing, pixel pubblicitari e DPA.",
        "norme": ["Artt. 6, 7, 13 GDPR", "Art. 122 e 130 D.Lgs. 196/2003", "Linee guida Cookie Garante"],
        "intro": "Un e-commerce raccoglie quotidianamente dati anagrafici, indirizzi, cronologia acquisti e tracciamenti comportamentali. Errori nel cookie banner o nelle caselle di consenso espongono a segnalazioni e sanzioni evitabili.",
        "sezioni": [
            ("1. Cookie banner e blocco preventivo degli script", "Nessun cookie di profilazione o pixel pubblicitario (Meta, Google Ads, TikTok) puo' attivarsi prima del consenso esplicito. Il banner deve consentire il rifiuto con la stessa facilita' dell'accettazione."),
            ("2. Checkbox separate per marketing, profilazione e cessione dati", "Le caselle di consenso nei form di checkout o registrazione non possono mai essere pre-spuntate e devono distinguere finalita' di marketing diretto, profilazione e comunicazione a terzi."),
            ("3. Soft spam e gestione delle revoche", "L'invio di offerte su prodotti analoghi a chi ha gia' acquistato (soft spam ex art. 130 co. 4 Codice Privacy) richiede informativa chiara e possibilita' immediata di disiscrizione a ogni email.")
        ],
        "checklist": [
            "Verificare tecnicamente il blocco preventivo di cookie e pixel prima del consenso.",
            "Eliminare checkbox pre-spuntate e separare consenso marketing da termini di vendita.",
            "Conservare i log di consenso CMP e form per dimostrare la prova del consenso.",
            "Stipulare DPA art. 28 con piattaforma e-commerce, hosting, email marketing e agenzie ads.",
            "Aggiornare Privacy Policy e Cookie Policy con dati reali e tempi di conservazione certi."
        ],
        "faqs": [
            ("Posso usare una privacy policy generica copiata da un altro sito?", "No: le informative generiche o incoerenti con i software realmente usati dal sito sono tra le prime violazioni contestate dal Garante."),
            ("Il soft spam vale anche per chi si e' solo registrato senza comprare?", "No, l'art. 130 comma 4 Codice Privacy richiede un precedente acquisto effettivo e riguarda solo prodotti o servizi analoghi.")
        ]
    },
]
