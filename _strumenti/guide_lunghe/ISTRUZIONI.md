# Riscrittura lunga delle guide del sito (ordine dell'avvocato, 20.11.2026)

Scopo: le guide del sito oggi sono di circa 140 parole, tutte uguali. Vanno riscritte come guide vere, lunghe e utili, così chi cerca su Google ("arrestato cosa fare", "cartella esattoriale prescritta", "permesso di soggiorno rifiutato", "avvocato Napoli ...") trova le pagine dello studio.

## Cosa ricevi
Un file `_lotti/lotto_NN.json` con le guide (slug, titolo attuale, materia, lawRef, excerpt, checklist, sintesi della materia). Per ogni guida scrivi UN file `guide_lunghe/<slug>.json`.

## Schema del file (JSON UTF-8, valido)
{
 "slug": "<identico a quello del lotto>",
 "title": "titolo H1, chiaro, max 75 caratteri, con la parola che la gente cerca",
 "seo_title": "max 60 caratteri",
 "description": "meta description 140-160 caratteri",
 "parole_chiave": ["5-8 ricerche reali in italiano"],
 "intro": ["1-2 paragrafi che rispondono subito alla domanda"],
 "sezioni": [{"h2": "...", "paragrafi": ["..."], "elenco": ["voci facoltative"]}],
 "faq": [{"q": "domanda come la scrive la gente", "a": "risposta 40-90 parole"}],
 "norme_verificate": [{"norma": "art. 186 D.Lgs. 285/1992", "file": "percorso del file della Biblioteca dove l'hai letta"}],
 "parole": <numero totale di parole del testo>
}

## Misura e struttura
- Tra 1.100 e 1.600 parole per guida (intro + sezioni + faq). Da 5 a 8 sezioni H2, da 5 a 7 FAQ.
- Sezioni tipo: che cosa dice la legge, cosa succede in pratica (passi e tempi), termini da non perdere, errori più frequenti, documenti da portare all'avvocato, come lavora lo studio. Adattale al tema, senza schemi ripetuti.
- Guide della stessa materia: ciascuna ha un taglio diverso, secondo il suo titolo. Mai paragrafi copiati da una guida all'altra (Google penalizza i contenuti duplicati).
- Prosa chiara per un cittadino non giurista, frasi complete, tono professionale e umano. Testo semplice: niente markdown, niente asterischi, niente HTML.

## Verità delle fonti (zero tolleranza)
- Ogni articolo di legge, termine (giorni), soglia o importo che scrivi lo devi aver LETTO nella Biblioteca: `D:\BIBLIOTECA GIURIDICA\<branca>\Norme\*.md` (grep sul numero dell'articolo, poi leggi il testo). Mettilo in `norme_verificate` con il file.
- Se la norma non c'è nella Biblioteca: `python -X utf8 D:/studio-iaccarino/centralino/chiama.py legal-it fetch_law_article "{\"act_type\":\"decreto legislativo\",\"article\":\"N\",\"date\":\"AAAA\",\"act_number\":\"NNN\"}"` e salva il testo nella cartella Norme della branca giusta, in un file `.md`. Se non riesci a leggerla, non scrivi il numero dell'articolo né il termine: descrivi in generale.
- VIETATO citare sentenze (numeri, date, "la Cassazione ha stabilito che..."), dottrina, statistiche o percentuali. VIETATO inventare procedure: se non sei sicuro di un passo, non lo scrivi.
- Mai promettere risultati ("vinciamo", "annulliamo sicuramente"), mai superlativi sullo studio ("il migliore", "il più esperto"): regole deontologiche forensi.
- Mai nomi di clienti, mai casi reali con dettagli identificabili.
- Mai trattini lunghi (– —), mai caporali (« »): solo virgolette rette e trattino semplice.

## Lo studio (si nomina in UNA sola sezione finale, breve, non in ogni paragrafo)
Studio Legale Avv. Francesco Iaccarino, Napoli, Palazzo Barbaja, Via Toledo 205. Opera a Napoli e in tutta Italia. Contatti li aggiunge la pagina, non scriverli.

## Uscita
Scrivi i file JSON, poi controlla con `python -X utf8 -c "import json,glob;[json.load(open(f,encoding='utf8')) for f in glob.glob('<cartella>/*.json')]"` che siano validi. Rispondi con UNA riga: lotto, guide scritte, parole medie, norme lette.
