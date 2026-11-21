"""Controllo a programma dei casi lunghi. Uso: python -X utf8 controlla_casi_lunghi.py [--lotto NN]
Scrive casi_lunghi/_CONTROLLO.md (o _CONTROLLO_lotto_NN.md) e stampa una riga."""
import json, re, glob, os, sys, collections
from pathlib import Path

R = Path(__file__).parent
D = R / "casi_lunghi"
CASI = {c["id"]: c for c in json.load(open(R / "dati_spa" / "casesArchive.json", encoding="utf-8"))}
lotto = None
if "--lotto" in sys.argv:
    NL = sys.argv[sys.argv.index("--lotto") + 1].zfill(2)
    lotto = {c["id"] for c in json.load(open(D / "_lotti" / f"lotto_{NL}.json", encoding="utf-8"))}
SENT = re.compile(r"\bCass\.|Cassazione[^.\n]{0,30}\b(ha|hanno) (stabilito|affermato|chiarito|ritenuto)|\b(sentenza|ordinanza) n\.|Sez\.\s*U|\bn\.\s*\d{3,6}\s*/\s*(19|20)\d\d|Corte cost|Sezioni Unite|giurisprudenz|i giudici hanno|dottrina", re.I)
PROM = re.compile(r"\b(il migliore|i migliori|garantiamo|garantisce|vinciamo|sicuramente|certamente vinc|esito garantito)", re.I)


NORME_TXT = {}


def norm_txt(fp):
    if fp not in NORME_TXT:
        try: NORME_TXT[fp] = re.sub(r"[.\s]", "", open(fp, encoding="utf-8", errors="ignore").read())
        except Exception: NORME_TXT[fp] = ""
    return NORME_TXT[fp]


CIFRA = re.compile(r"(?:€\s*([\d.,]+\d))|(?:\b(\d[\d.,]*\d|\d)\s*(?:euro|%|per cento))|\b((?:19|20)\d\d)\b", re.I)


def cifre_inventate(g, caso):
    base = re.sub(r"[.\s]", "", " ".join(str(v) for v in caso.values()))
    norme = "".join(norm_txt(nv.get("file", "")) for nv in g.get("norme_verificate", []))
    t = " \n ".join(testi_di(g) + [g.get("seo_title", ""), g.get("description", "")])
    out = []
    for m in CIFRA.finditer(t):
        num = re.sub(r"[.\s]", "", next(x for x in m.groups() if x))
        if num in base or num in norme: continue
        out.append(f"cifra non presente nel caso ne' nelle norme: '{t[max(0,m.start()-40):m.end()+20]}'")
    return out


def testi_di(g):
    t = list(g.get("intro", []))
    for s in g.get("sezioni", []):
        t += [s.get("h2", "")] + s.get("paragrafi", []) + s.get("elenco", [])
    for q in g.get("faq", []):
        t += [q.get("q", ""), q.get("a", "")]
    return t


par_visti = collections.defaultdict(list)
for f in glob.glob(str(R / "guide_lunghe" / "*.json")):
    try:
        for p in testi_di(json.load(open(f, encoding="utf-8"))):
            if len(p) > 120: par_visti[p.strip()].append("guida:" + Path(f).stem)
    except Exception:
        pass
righe, rossi, tot, fatti = [], 0, [], 0
files = sorted(glob.glob(str(D / "SLI-*.json")))
for f in files:
    cid = Path(f).stem
    g = None
    try:
        g = json.load(open(f, encoding="utf-8"))
    except Exception as e:
        if lotto is None or cid in lotto:
            righe.append(f"ROSSO {cid}: JSON non valido ({e})"); rossi += 1
        continue
    testi = testi_di(g)
    for p in testi:
        if len(p) > 120: par_visti[p.strip()].append(cid)
    if lotto is not None and cid not in lotto:
        continue
    fatti += 1
    err = []
    if cid not in CASI: err.append("id non presente nel sito")
    if g.get("id") != cid: err.append("id interno diverso dal nome del file")
    t = "\n".join(testi + [g.get("seo_title", ""), g.get("description", "")])
    n = len("\n".join(testi).split()); tot.append(n)
    if n < 650: err.append(f"corto ({n} parole)")
    if len(g.get("seo_title", "")) > 65: err.append("seo_title oltre 60")
    if re.search("[–—]", t): err.append("trattino lungo")
    if re.search("[«»]", t): err.append("caporali")
    if re.search(r"\*\*|^#|<[a-z]", t, re.M): err.append("markdown o html")
    for m in SENT.finditer(t):
        err.append(f"sentenza o fonte vietata: '{t[max(0,m.start()-50):m.end()+50]}'")
    for m in PROM.finditer(t):
        err.append(f"promessa: '{t[max(0,m.start()-40):m.end()+40]}'")
    if not g.get("norme_verificate"): err.append("nessuna norma verificata")
    for nv in g.get("norme_verificate", []):
        fp = nv.get("file", "")
        if not fp or not os.path.exists(fp): err.append(f"norma senza file: {nv.get('norma')} -> {fp}")
    if cid in CASI: err += cifre_inventate(g, CASI[cid])
    if len(g.get("faq", [])) < 3: err.append("FAQ meno di 3")
    if len(g.get("sezioni", [])) < 4: err.append("sezioni meno di 4")
    if err:
        rossi += 1; righe.append(f"ROSSO {cid}: " + "; ".join(err))
dup = [(p, s) for p, s in par_visti.items() if len(set(s)) > 1 and (lotto is None or set(s) & lotto)]
for p, s in dup:
    righe.append(f"DUPLICATO in {sorted(set(s))}: {p[:90]}...")
attesi = lotto if lotto is not None else set(CASI)
mancanti = sorted(attesi - {Path(f).stem for f in files})
out = (f"# Controllo casi lunghi{' lotto ' + NL if lotto else ''}\n\nCasi: {fatti} su {len(attesi)}; parole medie {sum(tot)//max(1,len(tot))}; "
       f"rossi {rossi}; paragrafi duplicati {len(dup)}\n\nMancanti: {', '.join(mancanti) or 'nessuno'}\n\n" + "\n".join(righe) + "\n")
nome = f"_CONTROLLO_lotto_{NL}.md" if lotto else "_CONTROLLO.md"
open(D / nome, "w", encoding="utf-8").write(out)
print(f"casi {fatti}/{len(attesi)}, parole medie {sum(tot)//max(1,len(tot))}, rossi {rossi}, duplicati {len(dup)}, mancanti {len(mancanti)} (dettaglio in casi_lunghi/{nome})")
