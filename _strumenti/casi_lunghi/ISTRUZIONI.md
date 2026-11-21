# Allungamento dei casi risolti del sito (ordine dell'avvocato, 21.11.2026: "allungali, applica le norme e aggiungi contenuti per analogia")

Cartella: `D:\STUDIO LEGALE\MODELLI E FORMULARI\Nuovo sito internet\_SITO_GITHUB_PAGES\sito\_strumenti\casi_lunghi`

Ogni caso del sito oggi ha circa 90 parole (fatto, strategia, decisione). Quei tre testi RESTANO IDENTICI e la pagina li mostra già: tu NON li riscrivi e NON li ripeti. Scrivi le parti che si aggiungono sotto, così la pagina arriva a 800-1.100 parole e chi cerca su Google un problema simile trova il caso dello studio.

## Cosa ricevi
`_lotti/lotto_NN.json`: 14 casi (id, area, court, title, outcome, fatto, strategia, decisione, attivita, materia, sintesi_materia, norme_gia_lette_nelle_guide). Per ogni caso scrivi UN file `<id>.json` (es. `SLI-001.json`) in questa cartella.

## Schema (JSON UTF-8 valido)
{
 "id": "SLI-001",
 "seo_title": "max 60 caratteri, con la parola che la gente cerca (es. Truffa aggravata ente pubblico: assoluzione)",
 "description": "140-160 caratteri",
 "parole_chiave": ["4-6 ricerche reali in italiano"],
 "sezioni": [
   {"h2": "Le norme applicate al caso", "paragrafi": ["che cosa dice la norma, letta, con l'articolo"]},
   {"h2": "Perché la decisione è arrivata a questo esito", "paragrafi": ["come la norma ha operato SUI SOLI fatti scritti nel caso"]},
   {"h2": "Se ti trovi in una situazione simile", "paragrafi": ["per analogia: cosa vale in generale per chi ha lo stesso problema"], "elenco": ["voci facoltative: documenti, controlli"]},
   {"h2": "Termini e passi da non sbagliare", "paragrafi": ["..."]}
 ],
 "faq": [{"q": "domanda come la scrive la gente", "a": "40-80 parole"}],
 "norme_verificate": [{"norma": "art. 640 c.p.", "file": "percorso del file della Biblioteca"}],
 "parole": <numero di parole che hai scritto>
}
Titoli H2 liberi e adatti al caso (quelli sopra sono esempi): da 4 a 6 sezioni, da 3 a 5 FAQ, 700-1.000 parole scritte da te.

## Il limite più importante: MAI INVENTARE FATTI DEL CASO
- Del caso conosci solo ciò che c'è nel lotto. Non aggiungere date, importi, età, nazionalità, luoghi, numeri di persone, prove, testimoni, durata del processo, nomi di uffici diversi da `court`, dettagli che non sono scritti.
- Quando parli del caso: "nel caso", "in questa vicenda", riferendo solo i dati del lotto. Quando vai oltre, dillo: "in casi analoghi", "in generale", "chi si trova in una situazione simile".
- La sezione per analogia spiega cosa vale per situazioni dello stesso tipo, secondo la norma letta: cosa controllare, quali documenti raccogliere, quali errori evitare. Ogni vicenda va valutata sui suoi atti: dillo una volta, senza promettere esiti.
- Mai nomi, mai dettagli che rendano riconoscibile qualcuno.
- CONTROLLO A PROGRAMMA DELLE CIFRE: ogni importo in euro, percentuale o anno che scrivi deve comparire nei campi del caso (anche `outcome`) o nel file di una norma in `norme_verificate`; altrimenti il controllo dà ROSSO. Non dedurre "il risultato dimostra che..." se la regola generale non è scritta nella norma letta.

## Verità delle fonti (zero tolleranza)
- Ogni articolo, termine in giorni, soglia o importo che scrivi lo devi aver LETTO. Parti da `norme_gia_lette_nelle_guide` (file già nella Biblioteca: aprili e leggi l'articolo che usi). Se ti serve un'altra norma: grep in `D:\BIBLIOTECA GIURIDICA\<branca>\Norme\*.md`; se manca, `python -X utf8 D:/studio-iaccarino/centralino/chiama.py legal-it fetch_law_article "{\"act_type\":\"codice penale\",\"article\":\"640\"}"` (o decreto legislativo con date e act_number) e salva il testo in `.md` nella cartella Norme della branca. Se non riesci a leggerla, non scrivi numero né termine: descrivi in generale.
- VIETATO citare sentenze, "la Cassazione ha stabilito", "la giurisprudenza", "i giudici hanno", Sezioni Unite, Corte costituzionale, dottrina, statistiche, percentuali. VIETATO inventare procedure.
- Mai promesse ("vinciamo", "annulliamo sicuramente"), mai superlativi sullo studio.
- Mai trattini lunghi, mai caporali: solo virgolette rette. Niente markdown, asterischi, HTML.

## Niente copie
Casi della stessa materia nello stesso lotto: ognuno ha un taglio diverso, legato al suo fatto e al suo esito. Nessun paragrafo uguale o quasi uguale a un altro caso o alle guide (`..\guide_lunghe\*.json`): Google penalizza i duplicati. Se due casi sono simili, cambia l'angolo (prova, termini, rito, conseguenze, misure, documenti).

## Lo studio
Si nomina al massimo in una frase finale: Studio Legale Avv. Francesco Iaccarino, Napoli, Via Toledo 205. Niente contatti.

## Uscita
Scrivi i 14 file, poi lancia `python -X utf8 "D:/STUDIO LEGALE/MODELLI E FORMULARI/Nuovo sito internet/_SITO_GITHUB_PAGES/sito/_strumenti/controlla_casi_lunghi.py" --lotto NN` e correggi finché il tuo lotto ha zero rossi. Le correzioni (sed, script o Edit) le fai SOLO sui 14 file del tuo lotto, mai sugli altri SLI-*.json della cartella: ci lavorano altri redattori. Rispondi con UNA riga: lotto, casi scritti, parole medie, rossi, norme lette nuove.
