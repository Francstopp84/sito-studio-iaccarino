"""Controllo a programma delle guide lunghe. Uso: python -X utf8 controlla_guide_lunghe.py
Scrive guide_lunghe/_CONTROLLO.md e stampa una riga."""
import json, re, glob, os, collections
from pathlib import Path

D = Path(__file__).parent / "guide_lunghe"
ART = {a["slug"] for a in json.load(open(Path(__file__).parent / "dati_spa" / "blogArticles.json", encoding="utf-8"))}
righe, rossi, tot, par_visti = [], 0, [], collections.defaultdict(list)
SENT = re.compile(r"\bCass\.|Cassazione[^.\n]{0,30}\b(ha|hanno) (stabilito|affermato|chiarito|ritenuto)|\b(sentenza|ordinanza) n\.|Sez\.\s*U|\bn\.\s*\d{3,6}\s*/\s*(19|20)\d\d|Corte cost|Sezioni Unite|la giurisprudenza|i giudici hanno", re.I)
for f in sorted(glob.glob(str(D / "*.json"))):
    slug = Path(f).stem
    err = []
    try:
        g = json.load(open(f, encoding="utf-8"))
    except Exception as e:
        righe.append(f"ROSSO {slug}: JSON non valido ({e})"); rossi += 1; continue
    if slug not in ART: err.append("slug non presente nel sito")
    testi = list(g.get("intro", []))
    for s in g.get("sezioni", []):
        testi += [s.get("h2", "")] + s.get("paragrafi", []) + s.get("elenco", [])
    for q in g.get("faq", []):
        testi += [q.get("q", ""), q.get("a", "")]
    testi += [g.get("title", ""), g.get("description", "")]
    t = "\n".join(testi)
    n = len(t.split()); tot.append(n)
    if n < 1000: err.append(f"corta ({n} parole)")
    if re.search("[–—]", t): err.append("trattino lungo")
    if re.search("[«»]", t): err.append("caporali")
    if re.search(r"\*\*|^#|<[a-z]", t, re.M): err.append("markdown o html")
    for m in SENT.finditer(t):
        err.append(f"sentenza citata: '{t[max(0,m.start()-60):m.end()+60]}'")
    if re.search(r"\b(il migliore|i migliori|garantiamo|vinciamo|sicuramente annull)", t, re.I): err.append("promessa o superlativo")
    for nv in g.get("norme_verificate", []):
        fp = nv.get("file", "")
        if not fp or not os.path.exists(fp): err.append(f"norma senza file: {nv.get('norma')} -> {fp}")
    if len(g.get("faq", [])) < 4: err.append("FAQ meno di 4")
    if len(g.get("sezioni", [])) < 4: err.append("sezioni meno di 4")
    for p in testi:
        if len(p) > 120: par_visti[p.strip()].append(slug)
    if err:
        rossi += 1; righe.append(f"ROSSO {slug}: " + "; ".join(err))
dup = [(p, s) for p, s in par_visti.items() if len(set(s)) > 1]
for p, s in dup:
    righe.append(f"DUPLICATO in {sorted(set(s))}: {p[:90]}...")
mancanti = sorted(ART - {Path(f).stem for f in glob.glob(str(D / '*.json'))})
out = (f"# Controllo guide lunghe\n\nGuide: {len(tot)} su {len(ART)}; parole medie {sum(tot)//max(1,len(tot))}; "
       f"rosse {rossi}; paragrafi duplicati {len(dup)}\n\nMancanti: {', '.join(mancanti) or 'nessuna'}\n\n" + "\n".join(righe) + "\n")
open(D / "_CONTROLLO.md", "w", encoding="utf-8").write(out)
print(f"guide {len(tot)}/{len(ART)}, parole medie {sum(tot)//max(1,len(tot))}, rosse {rossi}, duplicati {len(dup)}, mancanti {len(mancanti)}")
