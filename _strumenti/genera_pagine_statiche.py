"""Genera pagine HTML statiche indicizzabili da Google per guide, casi risolti e percorsi
del sito (i dati della SPA sono in _strumenti/dati_spa). Uso: python genera_pagine_statiche.py <radice_sito>"""
import json, re, sys, html, unicodedata, datetime, ast
from pathlib import Path

R = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
D = Path(__file__).parent / "dati_spa"
SITE = "https://studiolegalefrancescoiaccarino.com"
OGGI = datetime.date.today().isoformat()
AREE = {"penale": "Diritto penale", "civile": "Diritto civile", "tributario": "Diritto tributario",
        "immigrazione": "Immigrazione e cittadinanza"}


def E(s):
    return html.escape(str(s or ""), quote=True)


def lista(v):
    if isinstance(v, list):
        return v
    try:
        x = ast.literal_eval(v)
        return x if isinstance(x, list) else [str(v)]
    except Exception:
        return [str(v)] if v else []


def slugify(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")[:70]


GTM = ("<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':new Date().getTime(),event:'gtm.js'});"
       "var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;"
       "j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);})"
       "(window,document,'script','dataLayer','GTM-N5PKHC93');</script>")

CSS = """body{margin:0;background:#06111F;color:#E8E4DA;font-family:'EB Garamond',Georgia,serif;font-size:1.12rem;line-height:1.7}
a{color:#C9A96E}header,footer{padding:1.1rem 6vw;border-bottom:1px solid rgba(201,169,110,.25)}
footer{border-top:1px solid rgba(201,169,110,.25);border-bottom:0;font-size:.95rem;color:#b9b3a6}
header a.logo{font-family:'Cormorant Garamond',serif;font-size:1.35rem;text-decoration:none;color:#E8E4DA}
nav a{margin-left:1.2rem;text-decoration:none;font-size:.98rem}
main{max-width:860px;margin:0 auto;padding:2.2rem 6vw 3rem}
h1,h2{font-family:'Cormorant Garamond',serif;font-weight:600;color:#F3EEE3}h1{font-size:2.3rem;line-height:1.2}
.bc{font-size:.85rem;color:#8d97a6}.bc a{color:#8d97a6}
.tag{display:inline-block;border:1px solid rgba(201,169,110,.5);color:#C9A96E;padding:.1rem .7rem;border-radius:20px;font-size:.85rem;margin:0 .4rem .3rem 0}
.box{background:#0B1D32;border:1px solid rgba(201,169,110,.25);border-radius:10px;padding:1.2rem 1.5rem;margin:1.6rem 0}
.cta{display:inline-block;background:#C9A96E;color:#06111F;padding:.7rem 1.4rem;border-radius:6px;text-decoration:none;font-weight:600;margin:.3rem .6rem .3rem 0}
ul.el li{margin:.35rem 0}"""

urls = []


def pagina(path, title, desc, corpo, briciole, schema):
    url = f"{SITE}/{path}"
    d = E(desc[:158])
    out = f"""<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="UTF-8">
{GTM}
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{E(title)}</title>
<meta name="description" content="{d}">
<meta name="robots" content="index, follow">
<link rel="canonical" href="{url.replace('/index.html', '/')}">
<meta property="og:type" content="article"><meta property="og:url" content="{url}">
<meta property="og:title" content="{E(title)}"><meta property="og:description" content="{d}"><meta property="og:locale" content="it_IT">
<meta property="og:image" content="{SITE}/assets/images/palazzo_barbaja_napoli.jpg">
<link rel="icon" type="image/png" sizes="48x48" href="/favicon-48.png"><link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600&family=EB+Garamond:ital@0;1&display=swap" rel="stylesheet">
<style>{CSS}</style>
<script type="application/ld+json">{json.dumps(schema, ensure_ascii=False)}</script>
</head>
<body>
<header><a class="logo" href="/">Studio Legale Avv. Francesco Iaccarino</a>
<nav><a href="/guide/">Guide</a><a href="/casi/">Casi risolti</a><a href="/percorsi/">Materie</a><a href="/prenota.html">Prenota</a></nav></header>
<main>
<div class="bc">{briciole}</div>
{corpo}
<div class="box"><strong>Serve assistenza su questo tema?</strong><br>Studio legale in Via Toledo 205, Napoli, operativo su tutto il territorio nazionale.<br>
<a class="cta" href="tel:+393335684659">Chiama 333 568 4659</a><a class="cta" href="https://wa.me/393335684659">WhatsApp</a><a class="cta" href="/prenota.html">Prenota una consulenza</a></div>
</main>
<footer>Studio Legale Avv. Francesco Iaccarino, Via Toledo 205, 80134 Napoli. Tel. 081 426459. <a href="/privacy.html">Privacy</a>. Le informazioni pubblicate hanno carattere generale e non sostituiscono un parere sul caso concreto; i casi sono descritti in forma anonima.</footer>
</body></html>
"""
    f = R / path
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_text(out, encoding="utf-8")
    urls.append(url.replace("/index.html", "/"))


def bc(*voci):
    pezzi = ['<a href="/">Home</a>'] + [f'<a href="{h}">{E(t)}</a>' if h else E(t) for t, h in voci]
    return " &rsaquo; ".join(pezzi)


ART = json.load(open(D / "blogArticles.json", encoding="utf-8"))
CASI = json.load(open(D / "casesArchive.json", encoding="utf-8"))
SUB = json.load(open(D / "subtopics.json", encoding="utf-8"))

# percorsi: se esiste gia' la vecchia pagina /<area>/<slug>.html si linka quella, non si duplica
perc_url = {}
for s in SUB:
    vecchia = R / s["area"] / f"{s['slug']}.html"
    perc_url[(s["area"], s["slug"])] = (f"/{s['area']}/{s['slug']}.html" if vecchia.exists()
                                        else f"/percorsi/{s['area']}/{s['slug']}.html")
casi_url = {c["id"]: f"/casi/{c['id'].lower()}-{slugify(c['title'])}.html" for c in CASI}
guide_url = {a["slug"]: f"/guide/{a['slug']}.html" for a in ART}
nome_sub = {(s["area"], s["slug"]): s["name"] for s in SUB}


def casi_correlati(area, sub, escl=None, n=6):
    l = [c for c in CASI if c["area"] == area and c.get("subtopic") == sub and c["id"] != escl]
    if len(l) < 3:
        l += [c for c in CASI if c["area"] == area and c not in l and c["id"] != escl][:n]
    return "".join(f'<li><a href="{casi_url[c["id"]]}">{E(c["title"])}</a> ({E(c["outcome"])})</li>' for c in l[:n])


def guide_correlate(area, sub, escl=None, n=6):
    l = [a for a in ART if a["area"] == area and a["subtopic"] == sub and a["slug"] != escl]
    if len(l) < 3:
        l += [a for a in ART if a["area"] == area and a not in l and a["slug"] != escl][:n]
    return "".join(f'<li><a href="{guide_url[a["slug"]]}">{E(a["title"])}</a></li>' for a in l[:n])


AUT = {"@type": "Person", "name": "Avv. Francesco Iaccarino"}

for a in ART:
    par = "".join(f"<p>{E(p)}</p>" for p in lista(a["paragraphs"]))
    chk = "".join(f"<li>{E(x)}</li>" for x in lista(a["checklist"]))
    pu = perc_url.get((a["area"], a["subtopic"]))
    corpo = (f"<p><span class='tag'>{E(AREE.get(a['area'], a['area']))}</span><span class='tag'>{E(a['subtopicName'])}</span>"
             f"<span class='tag'>{E(a['lawRef'])}</span></p>\n<h1>{E(a['title'])}</h1>"
             f"<p><em>{E(a['date'])}, lettura {E(a['readTime'])}</em></p>{par}\n"
             + (f"<h2>Cosa fare subito</h2><ul class='el'>{chk}</ul>\n" if chk else "")
             + (f"<p>Approfondimento della materia: <a href='{pu}'>{E(a['subtopicName'])}</a>.</p>\n" if pu else "")
             + f"<h2>Casi risolti dallo studio sul tema</h2><ul class='el'>{casi_correlati(a['area'], a['subtopic'])}</ul>\n"
             + f"<h2>Altre guide</h2><ul class='el'>{guide_correlate(a['area'], a['subtopic'], a['slug'])}</ul>")
    sch = {"@context": "https://schema.org", "@type": "Article", "headline": a["title"][:110],
           "description": a["excerpt"], "inLanguage": "it", "author": AUT,
           "publisher": {"@type": "LegalService", "name": "Studio Legale Avv. Francesco Iaccarino", "url": SITE}}
    pagina(guide_url[a["slug"]][1:], f"{a['title']} | Avv. Iaccarino Napoli", a["excerpt"], corpo,
           bc(("Guide", "/guide/"), (a["subtopicName"], None)), sch)

for c in CASI:
    att = "".join(f"<li>{E(x)}</li>" for x in lista(c.get("attivita")))
    sub = c.get("subtopic")
    pu = perc_url.get((c["area"], sub))
    corpo = (f"<p><span class='tag'>{E(AREE.get(c['area'], c['area']))}</span><span class='tag'>{E(c['court'])}</span>"
             f"<span class='tag'>Rif. {E(c['id'])}</span></p>\n<h1>{E(c['title'])}: {E(c['outcome'].lower())}</h1>\n"
             f"<h2>Il fatto</h2><p>{E(c['fatto'])}</p><h2>La strategia difensiva</h2><p>{E(c['strategia'])}</p>"
             f"<h2>La decisione</h2><p>{E(c['decisione'])}</p>\n"
             + (f"<h2>Attivit&agrave; svolte</h2><ul class='el'>{att}</ul>\n" if att else "")
             + (f"<p>Materia: <a href='{pu}'>{E(nome_sub.get((c['area'], sub), sub))}</a>.</p>\n" if pu else "")
             + f"<h2>Guide sul tema</h2><ul class='el'>{guide_correlate(c['area'], sub)}</ul>\n"
             + f"<h2>Altri casi simili</h2><ul class='el'>{casi_correlati(c['area'], sub, c['id'])}</ul>")
    desc = f"{c['title']} davanti al {c['court']}: {c['outcome']}. {c['fatto']}"
    sch = {"@context": "https://schema.org", "@type": "Article", "headline": f"{c['title']}: {c['outcome']}"[:110],
           "description": desc[:300], "inLanguage": "it", "author": AUT}
    pagina(casi_url[c["id"]][1:], f"{c['title']}, {c['outcome']} | Casi risolti Avv. Iaccarino", desc, corpo,
           bc(("Casi risolti", "/casi/"), (AREE.get(c["area"], c["area"]), f"/casi/{c['area']}.html")), sch)

for s in SUB:
    if not perc_url[(s["area"], s["slug"])].startswith("/percorsi/"):
        continue
    pil = "".join(f"<li>{E(x)}</li>" for x in lista(s.get("strategyPillars")))
    corpo = (f"<p><span class='tag'>{E(AREE.get(s['area'], s['area']))}</span><span class='tag'>{E(s['lawRef'])}</span></p>\n"
             f"<h1>{E(s['name'])}: avvocato a Napoli</h1><p>{E(s['summary'])}</p><p><em>{E(s.get('urgencyNote'))}</em></p>\n"
             + (f"<h2>Come imposta la difesa lo studio</h2><ul class='el'>{pil}</ul>\n" if pil else "")
             + f"<h2>Guide</h2><ul class='el'>{guide_correlate(s['area'], s['slug'])}</ul>"
             + f"<h2>Casi risolti</h2><ul class='el'>{casi_correlati(s['area'], s['slug'])}</ul>")
    sch = {"@context": "https://schema.org", "@type": "LegalService",
           "name": f"Studio Legale Avv. Francesco Iaccarino - {s['name']}", "url": SITE, "telephone": "+39081426459",
           "address": {"@type": "PostalAddress", "streetAddress": "Via Toledo 205", "addressLocality": "Napoli",
                       "postalCode": "80134", "addressCountry": "IT"}}
    pagina(perc_url[(s["area"], s["slug"])][1:], f"{s['name']} | Avvocato Napoli | Studio Iaccarino", s["summary"], corpo,
           bc(("Materie", "/percorsi/"), (s["name"], None)), sch)


def indice(path, titolo, desc, sezioni):
    corpo = f"<h1>{E(titolo)}</h1><p>{E(desc)}</p>" + "".join(
        f"<h2>{E(t)}</h2><ul class='el'>{v}</ul>" for t, v in sezioni if v)
    pagina(path, f"{titolo} | Studio Legale Iaccarino Napoli", desc, corpo, bc((titolo, None)),
           {"@context": "https://schema.org", "@type": "CollectionPage", "name": titolo})


indice("guide/index.html", "Guide legali",
       "Guide pratiche dello studio su diritto penale, civile, tributario e immigrazione.",
       [(AREE[k], "".join(f'<li><a href="{guide_url[a["slug"]]}">{E(a["title"])}</a></li>'
                          for a in ART if a["area"] == k)) for k in AREE])
for k in AREE:
    subs = list(dict.fromkeys(c.get("subtopic") for c in CASI if c["area"] == k))
    indice(f"casi/{k}.html", f"Casi risolti: {AREE[k].lower()}",
           f"Casi seguiti dallo studio in materia di {AREE[k].lower()}, descritti in forma anonima.",
           [(nome_sub.get((k, sub), sub or "Altri"),
             "".join(f'<li><a href="{casi_url[c["id"]]}">{E(c["title"])}</a> ({E(c["outcome"])})</li>'
                     for c in CASI if c["area"] == k and c.get("subtopic") == sub)) for sub in subs])
indice("casi/index.html", "Casi risolti", "Archivio dei casi seguiti dallo studio, in forma anonima.",
       [("Per materia", "".join(f'<li><a href="/casi/{k}.html">{E(AREE[k])}</a> '
                                f'({sum(1 for c in CASI if c["area"] == k)} casi)</li>' for k in AREE))])
indice("percorsi/index.html", "Materie trattate", "Le materie seguite dallo studio, con guide e casi risolti.",
       [(AREE[k], "".join(f'<li><a href="{perc_url[(s["area"], s["slug"])]}">{E(s["name"])}</a> ({E(s["lawRef"])})</li>'
                          for s in SUB if s["area"] == k)) for k in AREE])

sm = "".join(f"<url><loc>{u}</loc><lastmod>{OGGI}</lastmod></url>\n" for u in urls)
(R / "sitemap-guide-casi.xml").write_text(
    f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{sm}</urlset>\n',
    encoding="utf-8")
print(f"pagine {len(urls)}: guide {len(ART)}, casi {len(CASI)}, "
      f"percorsi nuovi {sum(1 for v in perc_url.values() if v.startswith('/percorsi/'))}")
