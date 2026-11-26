# -*- coding: utf-8 -*-
"""
Generatore completo della 6a area strutturale del sito Studio Legale Avv. Francesco Iaccarino:
DIRITTO SOCIETARIO, MODELLO 231 E CRISI D'IMPRESA / FALLIMENTARE (200 URL ESATTE):
- 1 Hub principale IT: societario.html
- 12 Pagine Pilastro: societario/<slug>.html
- 1 Indice Scenari + 150 Scenari Operativi: societario/scenari/index.html e societario/scenari/<slug>.html
- 1 Indice Guide + 26 Guide Operative: societario/guide/index.html e societario/guide/<slug>.html
- 9 Hub Lingue Estere: en/, es/, pt/, ru/, ar/, zh/, hi/, bn/, si/ -> societario.html
- Aggiornamento menu/footer di index.html, penale.html, civile.html, tributario.html, immigrazione.html, cybersicurezza.html
- Aggiornamento sitemap.xml, sitemap-guide-casi.xml, sitemap-lingue.xml
- Validazione automatica finale (200 URL esatte, 0 errori, 0 link rotti, 0 JSON-LD invalidi, 0 duplicati, 0 caporali, 0 Cassazione/Corte di Giustizia).
"""
import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(r"D:\STUDIO LEGALE\MODELLI E FORMULARI\Nuovo sito internet\_SITO_GITHUB_PAGES\sito")
BASE_URL = "https://studiolegalefrancescoiaccarino.com"
OG_IMG = f"{BASE_URL}/img/og-societario.jpg"
TODAY = "2026-11-26"

sys.path.insert(0, str(ROOT / "_strumenti"))
from soc_dati.pilastri import PILASTRI, COMPASS_DATA, CATEGORIE_SCENARI, LINGUE_ESTERE
from soc_dati.scenari_a import SCENARI_A
from soc_dati.scenari_b import SCENARI_B
from soc_dati.scenari_c import SCENARI_C
from soc_dati.guide_soc import GUIDE_SOC

SCENARI = SCENARI_A + SCENARI_B + SCENARI_C
PILASTRI_BY_SLUG = {p["slug"]: p for p in PILASTRI}

ALL_LANGS = [
    ("it", "it", "Italiano", "/societario.html"),
    ("en", "en", "English", "/en/societario.html"),
    ("es", "es", "Español", "/es/societario.html"),
    ("pt", "pt", "Português", "/pt/societario.html"),
    ("ru", "ru", "Русский", "/ru/societario.html"),
    ("ar", "ar", "العربية", "/ar/societario.html"),
    ("zh", "zh-Hans", "中文", "/zh/societario.html"),
    ("hi", "hi", "हिन्दी", "/hi/societario.html"),
    ("bn", "bn", "বাংলা", "/bn/societario.html"),
    ("si", "si", "සිංහල", "/si/societario.html"),
]

GTM_HEAD = """<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-N5PKHC93');</script>
<!-- End Google Tag Manager -->"""

GTM_BODY = """<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-N5PKHC93" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->"""

WA_FLOAT = """<style>
#wa-float{position:fixed;left:22px;top:50%;transform:translateY(-50%);z-index:10000;
  display:flex;align-items:center;gap:.6rem;background:#25D366;color:#fff;text-decoration:none;
  padding:.82rem 1.25rem .82rem 1rem;border-radius:50px;
  font-family:'Cormorant Garamond',Georgia,serif;font-size:1rem;font-weight:700;
  box-shadow:0 6px 26px rgba(37,211,102,.48),0 2px 10px rgba(0,0,0,.3);transition:transform .25s ease;}
#wa-float:hover{background:#1da851;color:#fff;transform:translateY(-50%) scale(1.04);}
#wa-float svg{width:28px;height:28px;flex:0 0 28px;display:block;}
@media (max-width:900px){#wa-float{left:14px;top:auto;bottom:18px;transform:none;padding:.8rem;gap:0;}#wa-float .wa-txt{display:none;}}
</style>
<a id="wa-float" href="https://wa.me/393335684659?text=CONSULENZA%20SOCIETARIO%20231%20CRISI%3A%20richiedo%20assistenza%20legale%20urgente." target="_blank" rel="noopener noreferrer" aria-label="Scrivi allo Studio su WhatsApp">
  <svg viewBox="0 0 32 32" fill="currentColor" aria-hidden="true"><path d="M16.02 3.2c-7.06 0-12.8 5.74-12.8 12.8 0 2.26.59 4.47 1.72 6.42L3.2 28.8l6.55-1.71a12.74 12.74 0 0 0 6.27 1.6h.01c7.05 0 12.79-5.74 12.79-12.8 0-3.42-1.33-6.63-3.75-9.05a12.7 12.7 0 0 0-9.05-3.64zm0 23.34h-.01c-1.98 0-3.93-.53-5.63-1.54l-.4-.24-4.18 1.1 1.11-4.08-.26-.42a10.6 10.6 0 0 1-1.63-5.66c0-5.87 4.78-10.64 10.65-10.64 2.84 0 5.51 1.11 7.52 3.12a10.57 10.57 0 0 1 3.11 7.53c0 5.87-4.77 10.64-10.64 10.64zm5.84-7.97c-.32-.16-1.89-.93-2.18-1.04-.29-.11-.5-.16-.71.16-.21.32-.82 1.04-1.01 1.25-.18.21-.37.24-.69.08-.32-.16-1.35-.5-2.57-1.59-.95-.85-1.59-1.89-1.78-2.21-.18-.32-.02-.5.14-.66.14-.14.32-.37.48-.56.16-.19.21-.32.32-.53.11-.21.05-.4-.03-.56-.08-.16-.71-1.72-.98-2.35-.26-.62-.52-.54-.71-.55l-.61-.01c-.21 0-.56.08-.85.4-.29.32-1.11 1.09-1.11 2.65 0 1.56 1.14 3.07 1.3 3.28.16.21 2.25 3.43 5.45 4.81.76.33 1.35.52 1.82.67.76.24 1.46.21 2.01.13.61-.09 1.89-.77 2.16-1.52.27-.75.27-1.38.19-1.52-.08-.13-.29-.21-.61-.37z"/></svg>
  <span class="wa-txt">Desk Societario WhatsApp</span>
</a>"""


def esc(s: str) -> str:
    return html.escape(str(s), quote=True)


def hreflang_block() -> str:
    lines = [f'<link rel="alternate" hreflang="x-default" href="{BASE_URL}/societario.html">']
    for _, hreflang, _, path in ALL_LANGS:
        lines.append(f'<link rel="alternate" hreflang="{hreflang}" href="{BASE_URL}{path}">')
    return "\n".join(lines)


def lang_switcher(current_label: str) -> str:
    links = "".join(
        f'<a href="{path}" hreflang="{hl}" lang="{hl}" translate="no">{name}</a>'
        for _, hl, name, path in ALL_LANGS
    )
    return (
        f'<details class="lang-switch lang-fissa" translate="no">'
        f'<summary aria-label="Lingua / Language">'
        f'<svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3 3 15 0 18M12 3c-3 3-3 15 0 18"/></svg>'
        f'<span>{esc(current_label)}</span></summary><div class="lang-menu">{links}</div></details>'
    )


def nav_it(active: str = "soc") -> str:
    return f"""<nav class="cy-nav" role="navigation" aria-label="Menu principale">
  <div class="cy-nav-inner">
    <a href="/" class="cy-logo">Studio Legale Iaccarino <span class="cy-logo-badge">Societario &amp; 231</span></a>
    <div class="cy-nav-links">
      <a href="/">Home</a>
      <a href="/penale.html">Penale</a>
      <a href="/civile.html">Civile</a>
      <a href="/tributario.html">Tributario</a>
      <a href="/immigrazione.html">Immigrazione</a>
      <a href="/cybersicurezza.html">Cybersicurezza</a>
      <a href="/societario.html" class="{'active' if active=='soc' else ''}">Societario &amp; 231</a>
      <a href="/societario/scenari/index.html" class="{'active' if active=='scenari' else ''}">150 Protocolli</a>
      <a href="/societario/guide/index.html" class="{'active' if active=='guide' else ''}">26 Guide</a>
      <a href="/consulenza.html?area=societario" class="cy-nav-cta">Richiedi Consulenza</a>
    </div>
  </div>
</nav>"""


def alert_bar_it() -> str:
    return """<div class="cy-alert-bar" role="region" aria-label="Pronto intervento societario, 231 e crisi">
  <div class="cy-alert-inner">
    <div class="cy-alert-left">
      <span class="cy-pulse-dot" aria-hidden="true"></span>
      <span class="cy-alert-tag">Desk Imprese, 231 &amp; Crisi</span>
      <span>Sequestro 231 (10gg), istanza di liquidazione giudiziale, pignoramenti o lite tra soci? Intervento immediato in tutta Italia.</span>
    </div>
    <div class="cy-alert-actions">
      <a href="tel:+393335684659" class="cy-btn-urgent">Chiama +39 333 568 4659</a>
      <a href="/consulenza.html?area=societario&amp;urgenza=si" class="cy-btn-urgent">Attiva Difesa Impresa</a>
    </div>
  </div>
</div>"""


def footer_it() -> str:
    return """<footer class="cy-footer">
  <div class="cy-footer-inner">
    <div>
      <strong>Studio Legale Avv. Francesco Iaccarino</strong> | Palazzo Barbaja, Via Toledo 205, 80132 Napoli | Tel. +39 081 426459 | Urgenze +39 333 568 4659 | Assistenza in tutta Italia e da remoto.
    </div>
    <div class="cy-footer-links">
      <a href="/">Home</a>
      <a href="/penale.html">Penale</a>
      <a href="/civile.html">Civile</a>
      <a href="/tributario.html">Tributario</a>
      <a href="/immigrazione.html">Immigrazione</a>
      <a href="/cybersicurezza.html">Cybersicurezza</a>
      <a href="/societario.html">Societario &amp; 231</a>
      <a href="/societario/scenari/index.html">150 Protocolli Impresa</a>
      <a href="/societario/guide/index.html">26 Guide Operative</a>
      <a href="/casi-risolti.html">Casi Reali</a>
      <a href="/privacy.html">Privacy Policy</a>
    </div>
  </div>
</footer>"""


def head_common(title: str, desc: str, canonical: str, ld_blocks: list, lang: str = "it", locale: str = "it_IT", include_hreflang: bool = False) -> str:
    ld_html = "\n".join(
        f'<script type="application/ld+json">\n{json.dumps(b, ensure_ascii=False, indent=2)}\n</script>'
        for b in ld_blocks
    )
    hl = hreflang_block() if include_hreflang else ""
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
{GTM_HEAD}
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta name="robots" content="index, follow">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:url" content="{canonical}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:image" content="{OG_IMG}">
<meta property="og:locale" content="{locale}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/png" sizes="48x48" href="/favicon-48.png">
<link rel="icon" type="image/png" sizes="192x192" href="/logo-192.png">
<link rel="shortcut icon" href="/favicon.ico">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;500;600&family=Cormorant+Garamond:wght@500;600;700&family=JetBrains+Mono:wght@400;500;600&family=Manrope:wght@400;500;600;700&display=swap" rel="stylesheet">
{hl}
<link rel="stylesheet" href="/css/lingue.css">
<link rel="stylesheet" href="/css/cyber-wow.css?v=2">
{ld_html}
</head>"""


def build_hub_it():
    canonical = f"{BASE_URL}/societario.html"
    faqs_hub = [
        ("Quando conviene adottare il Modello 231 (D.Lgs. 231/2001)?", "Prima che accada un reato presupposto (sicurezza lavoro, fisco, ambiente, PA, cyber), ma anche dopo l'avvio delle indagini (post factum ex artt. 12 e 17 D.Lgs. 231/2001) per evitare misure interdittive e dimezzare le sanzioni pecuniarie."),
        ("Come funziona la Composizione Negoziata della Crisi nel CCII?", "Permette all'impresa in difficolta' di negoziare con banche, Agenzia delle Entrate, INPS e fornitori con l'ausilio di un Esperto indipendente, conservando la gestione aziendale e bloccando pignoramenti e istanze di liquidazione giudiziale tramite le misure protettive ex art. 18 CCII."),
        ("Quali sono le soglie di non fallibilita' dell'impresa minore (art. 2 CCII)?", "L'impresa non e' soggetta a liquidazione giudiziale se dimostra il possesso congiunto nei tre esercizi antecedenti di: attivo patrimoniale annuo <= 300.000 euro, ricavi annui <= 200.000 euro e debiti anche non scaduti <= 500.000 euro."),
        ("Cosa cambia per i sindaci con la riforma dell'art. 2407 c.c. (Legge 35/2025)?", "Salvo il caso di dolo, la L. 14 marzo 2025, n. 35 limita la responsabilita' risarcitoria dei sindaci a multipli del compenso annuo (15x fino a 10.000 euro, 12x tra 10.000 e 50.000 euro, 10x oltre 50.000 euro) e fissa una prescrizione certa di 5 anni dal deposito della relazione ex art. 2429 c.c."),
        ("Come posso liberarmi da una fideiussione omnibus firmata per la mia societa'?", "Verificando se il contratto riproduce le clausole 2, 6 e 8 dello schema ABI censurato da Banca d'Italia (nullita' parziale) e se la banca e' decaduta ex art. 1957 c.c. per non aver agito giudizialmente entro 6 mesi dalla scadenza."),
        ("Lo Studio assiste aziende e amministratori in tutta Italia?", "Si'. La sede e' a Napoli in Palazzo Barbaja, Via Toledo 205, e il Dipartimento Societario, 231 e Crisi d'Impresa opera presso tutti i Tribunali delle Imprese, le Sezioni Fallimentari e le Corti d'Appello d'Italia, anche in videochiamata.")
    ]
    ld_blocks = [
        {
            "@context": "https://schema.org",
            "@type": "LegalService",
            "name": "Studio Legale Avv. Francesco Iaccarino - Diritto Societario, Modello 231 e Crisi d'Impresa",
            "url": canonical,
            "image": OG_IMG,
            "description": "Assistenza legale in diritto societario, governance, M&A, Modello 231 (D.Lgs. 231/2001), Codice della Crisi (CCII e D.Lgs. 136/2024), concordato preventivo, liquidazione giudiziale e bancarotta.",
            "telephone": "+393335684659",
            "email": "studiolegalefrancescoiaccarino@outlook.com",
            "address": {
                "@type": "PostalAddress",
                "streetAddress": "Via Toledo 205",
                "addressLocality": "Napoli",
                "postalCode": "80132",
                "addressRegion": "Campania",
                "addressCountry": "IT"
            },
            "areaServed": {"@type": "Country", "name": "Italy"},
            "priceRange": "EUR 200"
        },
        {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{BASE_URL}/"},
                {"@type": "ListItem", "position": 2, "name": "Diritto Societario, 231 e Crisi d'Impresa", "item": canonical}
            ]
        },
        {
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": [
                {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
                for q, a in faqs_hub
            ]
        }
    ]

    pillars_html = []
    for p in PILASTRI:
        tags = "".join(f'<span class="cy-tag">{esc(n)}</span>' for n in p["norme"])
        pillars_html.append(f"""<a href="/societario/{p['slug']}.html" class="cy-pillar-card">
  <span class="cy-pillar-num">{p['num']}</span>
  <div class="cy-pillar-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">{p['icona']}</svg></div>
  <div>
    <h3>{esc(p['titolo'])}</h3>
    <p>{esc(p['sintesi'])}</p>
    <div class="cy-pillar-tags">{tags}</div>
    <span class="cy-link-more">Apri la guida e il protocollo &rarr;</span>
  </div>
</a>""")

    filter_pills = "".join(
        f'<button type="button" class="cy-filter-pill {"active" if k=="tutti" else ""}" data-cat="{k}">{esc(lbl)}</button>'
        for k, lbl in CATEGORIE_SCENARI
    )

    scenario_cards = []
    for s in SCENARI:
        search_blob = " ".join([s["cod"], s["titolo"], s["desc"], s["cat_lbl"], " ".join(s["keywords"]), " ".join(s["norme"])])
        scenario_cards.append(f"""<a href="/societario/scenari/{s['slug']}.html" class="cy-scenario-card" data-cat="{s['cat']}" data-search="{esc(search_blob)}">
  <div>
    <div class="cy-sc-top"><span class="cy-sc-code">{s['cod']}</span><span class="cy-sc-cat">{esc(s['cat_lbl'])}</span></div>
    <h3>{esc(s['titolo'])}</h3>
    <p>{esc(s['desc'])}</p>
  </div>
  <div class="cy-sc-foot"><span>{esc(s['norme'][0])}</span><span>Apri protocollo &rarr;</span></div>
</a>""")

    faq_html = "".join(
        f'<details class="cy-faq-item"><summary>{esc(q)}</summary><p>{esc(a)}</p></details>'
        for q, a in faqs_hub
    )

    compass_tabs = []
    compass_panels = []
    for i, (k, v) in enumerate(COMPASS_DATA.items()):
        act = "active" if i == 0 else ""
        compass_tabs.append(f'<button type="button" class="cy-compass-tab {act}" data-target="{k}">{esc(v["titolo"])}</button>')
        steps = "".join(f"<li>{esc(x)}</li>" for x in v["passi"])
        compass_panels.append(f"""<div class="cy-compass-panel {act}" id="panel-{k}">
  <div class="cy-compass-urg">{esc(v['urgenza'])}</div>
  <ol class="cy-compass-list">{steps}</ol>
  <a href="{v['link']}" class="cy-btn-primary">Apri la pagina di approfondimento &rarr;</a>
</div>""")

    body = f"""<body class="cyber-page">
<div class="cy-progress" aria-hidden="true"></div>
{lang_switcher("Italiano")}
{GTM_BODY}
{nav_it("soc")}
{alert_bar_it()}

<header class="cy-hero">
  <div class="cy-container">
    <nav class="cy-breadcrumb" aria-label="Percorso">
      <a href="/">Home</a> <span>/</span> <span>Diritto Societario, Modello 231 e Crisi d'Impresa</span>
    </nav>
    <div class="cy-hero-grid">
      <div>
        <span class="cy-eyebrow">CORPORATE LAW, D.LGS. 231/2001 &amp; CODICE DELLA CRISI (CCII)</span>
        <h1>Avvocato <em>Societario</em>, Modello 231 e Fallimentare in Italia</h1>
        <p class="cy-hero-lead">Difesa strategica per societa', amministratori, sindaci e soci: governance e adeguati assetti (art. 2086 c.c.), Modelli Organizzativi 231 e difesa da sequestri/interdizioni, Composizione Negoziata e misure protettive (CCII e Correttivo-ter D.Lgs. 136/2024), concordato preventivo, transazione fiscale, liquidazione giudiziale, bancarotta e M&amp;A.</p>
        <div class="cy-cta-row">
          <a href="/consulenza.html?area=societario" class="cy-btn-primary">Richiedi Consulenza Impresa</a>
          <a href="#bussola-crisi" class="cy-btn-cyber">Bussola Urgenze Societarie &darr;</a>
        </div>
        <div class="cy-hero-stats">
          <div class="cy-stat"><strong>12</strong><span>Pilastri Societario, 231 &amp; CCII</span></div>
          <div class="cy-stat"><strong>150</strong><span>Protocolli Operativi di Difesa</span></div>
          <div class="cy-stat"><strong>26</strong><span>Guide &amp; Checklist Forensi</span></div>
          <div class="cy-stat"><strong>10</strong><span>Lingue Desk Internazionale</span></div>
        </div>
      </div>
      <div class="cy-hero-visual">
        <img src="/assets/sculptures/societario.png" alt="Scultura architettonica Diritto Societario, 231 e Crisi d'Impresa Palazzo Barbaja" class="cy-hero-sculpture" loading="eager">
      </div>
    </div>
  </div>
</header>

<section class="cy-section" id="bussola-crisi">
  <div class="cy-container">
    <span class="cy-eyebrow">ORIENTAMENTO IMMEDIATO</span>
    <h2 class="cy-sec-title">Bussola Urgenze Societarie, 231 e Crisi d'Impresa</h2>
    <p class="cy-sec-sub">Seleziona la situazione che stai affrontando adesso per vedere subito le prime quattro mosse legali essenziali.</p>
    <div class="cy-compass-box">
      <div class="cy-compass-tabs">{''.join(compass_tabs)}</div>
      <div class="cy-compass-body">{''.join(compass_panels)}</div>
    </div>
  </div>
</section>

<section class="cy-section" id="pilastri">
  <div class="cy-container">
    <span class="cy-eyebrow">12 AREE SPECIALISTICHE</span>
    <h2 class="cy-sec-title">I 12 Pilastri del Dipartimento Societario, 231 e Fallimentare</h2>
    <p class="cy-sec-sub">Copertura completa dalla vita ordinaria della societa' fino alla difesa penale d'impresa, alle misure cautelari 231 e alla ristrutturazione della crisi.</p>
    <div class="cy-pillars-grid">{''.join(pillars_html)}</div>
  </div>
</section>

<section class="cy-section" id="scenari">
  <div class="cy-container">
    <span class="cy-eyebrow">ARCHIVIO OPERATIVO · 150 PROTOCOLLI</span>
    <h2 class="cy-sec-title">Cerca tra i 150 Protocolli Societari, 231 e Fallimentari</h2>
    <p class="cy-sec-sub">Filtra per materia o digita una parola chiave (es. bancarotta, 231, concordato, 2407, fideiussione, revocatoria, recesso, pignoramento).</p>
    <div class="cy-search-bar">
      <input type="search" id="cy-search-input" class="cy-search-input" placeholder="Cerca protocollo per parola chiave, articolo o problema (es. 231, concordato, bancarotta, 2476, ABI)..." aria-label="Cerca tra i 150 protocolli societari">
      <span id="cy-count" class="cy-count-badge">150 / 150 protocolli</span>
    </div>
    <div class="cy-filter-pills">{filter_pills}</div>
    <div class="cy-scenarios-grid" id="cy-scenarios-grid">{''.join(scenario_cards)}</div>
    <div style="text-align:center;margin-top:2rem;">
      <a href="/societario/guide/index.html" class="cy-btn-primary">Esplora tutte le 26 Guide Operative &rarr;</a>
    </div>
  </div>
</section>

<section class="cy-section" id="faq">
  <div class="cy-container">
    <span class="cy-eyebrow">DOMANDE FREQUENTI</span>
    <h2 class="cy-sec-title">Risposte Rapide su Diritto Societario, 231 e Crisi d'Impresa</h2>
    <div class="cy-faq-list">{faq_html}</div>
  </div>
</section>

{footer_it()}
{WA_FLOAT}
<script src="/js/cyber-wow.js?v=1" defer></script>
</body>
</html>"""
    (ROOT / "societario.html").write_text(
        head_common(
            "Avvocato Diritto Societario, Modello 231 e Fallimentare | Studio Iaccarino",
            "Assistenza legale per imprese, amministratori e soci in tutta Italia: diritto societario, Modello 231 (D.Lgs. 231/2001), Codice della Crisi (CCII), concordato, liquidazione giudiziale e bancarotta.",
            canonical, ld_blocks, include_hreflang=True
        ) + "\n" + body,
        encoding="utf-8"
    )


def build_pilastri():
    out_dir = ROOT / "societario"
    out_dir.mkdir(parents=True, exist_ok=True)
    for p in PILASTRI:
        canonical = f"{BASE_URL}/societario/{p['slug']}.html"
        rel_scenari = [s for s in SCENARI if s["pilastro"] == p["slug"]]
        rel_guide = [g for g in GUIDE_SOC if g["pilastro"] == p["slug"]]

        ld_blocks = [
            {
                "@context": "https://schema.org",
                "@type": "LegalService",
                "name": p["titolo"],
                "url": canonical,
                "description": p["description"],
                "telephone": "+393335684659",
                "areaServed": {"@type": "Country", "name": "Italy"}
            },
            {
                "@context": "https://schema.org",
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{BASE_URL}/"},
                    {"@type": "ListItem", "position": 2, "name": "Societario, 231 & Crisi", "item": f"{BASE_URL}/societario.html"},
                    {"@type": "ListItem", "position": 3, "name": p["titolo"], "item": canonical}
                ]
            },
            {
                "@context": "https://schema.org",
                "@type": "FAQPage",
                "mainEntity": [
                    {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
                    for q, a in p["faq"]
                ]
            }
        ]

        intro_html = "".join(f"<p>{esc(par)}</p>" for par in p["intro"])
        azioni_html = "".join(f"<li>{esc(x)}</li>" for x in p["azioni"])
        prove_html = "".join(f"<li>{esc(x)}</li>" for x in p["prove"])
        tags_html = "".join(f'<span class="cy-tag">{esc(n)}</span>' for n in p["norme"])
        faq_html = "".join(f'<details class="cy-faq-item"><summary>{esc(q)}</summary><p>{esc(a)}</p></details>' for q, a in p["faq"])
        sc_cards = "".join(
            f'<a href="/societario/scenari/{s["slug"]}.html" class="cy-scenario-card"><div><div class="cy-sc-top"><span class="cy-sc-code">{s["cod"]}</span><span class="cy-sc-cat">{esc(s["cat_lbl"])}</span></div><h3>{esc(s["titolo"])}</h3><p>{esc(s["desc"])}</p></div><div class="cy-sc-foot"><span>{esc(s["norme"][0])}</span><span>Apri protocollo &rarr;</span></div></a>'
            for s in rel_scenari
        )
        g_links = "".join(
            f'<li><a href="/societario/guide/{g["slug"]}.html">{esc(g["titolo"])}</a></li>'
            for g in rel_guide
        )
        altri_pilastri = "".join(
            f'<li><a href="/societario/{ap["slug"]}.html">{ap["num"]} · {esc(ap["titolo"])}</a></li>'
            for ap in PILASTRI if ap["slug"] != p["slug"]
        )

        body = f"""<body class="cyber-page">
<div class="cy-progress" aria-hidden="true"></div>
{GTM_BODY}
{nav_it("soc")}
{alert_bar_it()}
<header class="cy-hero" style="padding:3.8rem 1.5rem 2.8rem;">
  <div class="cy-container">
    <nav class="cy-breadcrumb" aria-label="Percorso">
      <a href="/">Home</a> <span>/</span> <a href="/societario.html">Societario &amp; 231</a> <span>/</span> <span>{esc(p['titolo'])}</span>
    </nav>
    <span class="cy-eyebrow">PILASTRO {p['num']} · {esc(p['urgenza'])}</span>
    <h1>{esc(p['h1'])}</h1>
    <p class="cy-hero-lead">{esc(p['description'])}</p>
    <div class="cy-pillar-tags" style="margin-top:1.2rem;">{tags_html}</div>
  </div>
</header>
<main class="cy-section">
  <div class="cy-container cy-article-layout">
    <article class="cy-article-body">
      <div class="cy-card-block">
        <h2>Inquadramento Giuridico e Strategia Difensiva</h2>
        {intro_html}
      </div>
      <div class="cy-card-block">
        <h2>Azioni Operative dello Studio</h2>
        <ol class="cy-step-list">{azioni_html}</ol>
      </div>
      <div class="cy-card-block">
        <h2>Documenti e Prove Chiave da Raccogliere Subito</h2>
        <ul class="cy-check-list">{prove_html}</ul>
      </div>
      <div class="cy-card-block">
        <h2>Domande Frequenti</h2>
        <div class="cy-faq-list">{faq_html}</div>
      </div>
      {f'<div class="cy-card-block"><h2>Protocolli Operativi Collegati ({len(rel_scenari)})</h2><div class="cy-scenarios-grid">{sc_cards}</div></div>' if rel_scenari else ''}
    </article>
    <aside class="cy-sidebar-box">
      <div class="cy-side-card">
        <h3>Serve assistenza su questo tema?</h3>
        <p>Valutazione riservata in studio a Napoli (Via Toledo 205) o in videochiamata in tutta Italia.</p>
        <a href="/consulenza.html?area=societario" class="cy-btn-primary" style="width:100%;justify-content:center;margin-bottom:.65rem;">Richiedi Consulenza</a>
        <a href="tel:+393335684659" class="cy-btn-cyber" style="width:100%;justify-content:center;">Chiama +39 333 568 4659</a>
      </div>
      {f'<div class="cy-side-card"><h3>Guide Operative Collegate</h3><ul style="padding-left:1.1rem;margin:0;font-size:.86rem;line-height:1.7;">{g_links}</ul></div>' if g_links else ''}
      <div class="cy-side-card">
        <h3>Tutti i 12 Pilastri</h3>
        <ul style="padding-left:1.1rem;margin:0;font-size:.84rem;line-height:1.68;">{altri_pilastri}</ul>
      </div>
    </aside>
  </div>
</main>
{footer_it()}
{WA_FLOAT}
<script src="/js/cyber-wow.js?v=1" defer></script>
</body>
</html>"""
        (out_dir / f"{p['slug']}.html").write_text(
            head_common(p["seo_title"], p["description"], canonical, ld_blocks) + "\n" + body,
            encoding="utf-8"
        )


def build_scenari():
    out_dir = ROOT / "societario" / "scenari"
    out_dir.mkdir(parents=True, exist_ok=True)
    for idx, s in enumerate(SCENARI):
        canonical = f"{BASE_URL}/societario/scenari/{s['slug']}.html"
        pil = PILASTRI_BY_SLUG[s["pilastro"]]
        prev_s = SCENARI[idx - 1] if idx > 0 else None
        next_s = SCENARI[idx + 1] if idx < len(SCENARI) - 1 else None
        prev_link = f'<a href="/societario/scenari/{prev_s["slug"]}.html" class="cy-btn-cyber">&larr; {prev_s["cod"]}</a>' if prev_s else "<span></span>"
        next_link = f'<a href="/societario/scenari/{next_s["slug"]}.html" class="cy-btn-cyber">{next_s["cod"]} &rarr;</a>' if next_s else "<span></span>"
        correlati = [x for x in SCENARI if x["cat"] == s["cat"] and x["slug"] != s["slug"]][:6]
        corr_html = "".join(
            f'<li><a href="/societario/scenari/{x["slug"]}.html">{x["cod"]} · {esc(x["titolo"])}</a></li>'
            for x in correlati
        )
        ld_blocks = [
            {
                "@context": "https://schema.org",
                "@type": "Article",
                "headline": s["titolo"],
                "description": s["desc"],
                "author": {"@type": "Person", "name": "Avv. Francesco Iaccarino"},
                "publisher": {"@type": "Organization", "name": "Studio Legale Avv. Francesco Iaccarino"},
                "datePublished": TODAY,
                "dateModified": TODAY,
                "mainEntityOfPage": canonical
            },
            {
                "@context": "https://schema.org",
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{BASE_URL}/"},
                    {"@type": "ListItem", "position": 2, "name": "Societario & 231", "item": f"{BASE_URL}/societario.html"},
                    {"@type": "ListItem", "position": 3, "name": "150 Protocolli", "item": f"{BASE_URL}/societario/scenari/index.html"},
                    {"@type": "ListItem", "position": 4, "name": s["cod"], "item": canonical}
                ]
            }
        ]
        norme_tags = "".join(f'<span class="cy-tag">{esc(n)}</span>' for n in s["norme"])
        prot_li = "".join(f"<li>{esc(x)}</li>" for x in s["protocollo"])
        prove_li = "".join(f"<li>{esc(x)}</li>" for x in s["prove"])
        err_li = "".join(f"<li>{esc(x)}</li>" for x in s["errori"])

        body = f"""<body class="cyber-page">
<div class="cy-progress" aria-hidden="true"></div>
{GTM_BODY}
{nav_it("scenari")}
{alert_bar_it()}
<header class="cy-hero" style="padding:3.6rem 1.5rem 2.5rem;">
  <div class="cy-container">
    <nav class="cy-breadcrumb" aria-label="Percorso">
      <a href="/">Home</a> <span>/</span> <a href="/societario.html">Societario &amp; 231</a> <span>/</span> <a href="/societario/scenari/index.html">150 Protocolli</a> <span>/</span> <span>{s['cod']}</span>
    </nav>
    <span class="cy-eyebrow">{s['cod']} · {esc(s['cat_lbl'])}</span>
    <h1>{esc(s['titolo'])}</h1>
    <p class="cy-hero-lead">{esc(s['desc'])}</p>
    <div class="cy-pillar-tags" style="margin-top:1.1rem;">{norme_tags}</div>
  </div>
</header>
<main class="cy-section">
  <div class="cy-container cy-article-layout">
    <article class="cy-article-body">
      <div class="cy-card-block">
        <h2>Scenario Operativo Tipo</h2>
        <p>{esc(s['scenario'])}</p>
        <h3>Rischio Legale e Patrimoniale</h3>
        <p>{esc(s['rischio'])}</p>
      </div>
      <div class="cy-card-block">
        <h2>Protocollo di Difesa in 4 Passi</h2>
        <ol class="cy-step-list">{prot_li}</ol>
      </div>
      <div class="cy-card-block">
        <h2>Prove e Documenti Decisivi</h2>
        <ul class="cy-check-list">{prove_li}</ul>
      </div>
      <div class="cy-card-block">
        <h2>Errori da Evitare</h2>
        <ul class="cy-warn-list">{err_li}</ul>
      </div>
      <div style="display:flex;justify-content:space-between;align-items:center;gap:1rem;flex-wrap:wrap;margin-top:2rem;">
        {prev_link}
        <a href="/societario/{pil['slug']}.html" class="cy-btn-primary">Torna al Pilastro {pil['num']}</a>
        {next_link}
      </div>
    </article>
    <aside class="cy-sidebar-box">
      <div class="cy-side-card">
        <h3>Stai vivendo questo scenario?</h3>
        <p>Ogni vicenda societaria, 231 o di crisi va valutata sui documenti reali prima che scadano i termini.</p>
        <a href="/consulenza.html?area=societario" class="cy-btn-primary" style="width:100%;justify-content:center;margin-bottom:.65rem;">Richiedi Consulenza</a>
        <a href="tel:+393335684659" class="cy-btn-cyber" style="width:100%;justify-content:center;">Chiama +39 333 568 4659</a>
      </div>
      <div class="cy-side-card">
        <h3>Protocolli Correlati</h3>
        <ul style="padding-left:1.1rem;margin:0;font-size:.85rem;line-height:1.68;">{corr_html}</ul>
      </div>
    </aside>
  </div>
</main>
{footer_it()}
{WA_FLOAT}
<script src="/js/cyber-wow.js?v=1" defer></script>
</body>
</html>"""
        (out_dir / f"{s['slug']}.html").write_text(
            head_common(f"{s['seo_title']} | Studio Iaccarino", s["desc"], canonical, ld_blocks) + "\n" + body,
            encoding="utf-8"
        )

    # Indice 150 scenari
    idx_canonical = f"{BASE_URL}/societario/scenari/index.html"
    filter_pills = "".join(
        f'<button type="button" class="cy-filter-pill {"active" if k=="tutti" else ""}" data-cat="{k}">{esc(lbl)}</button>'
        for k, lbl in CATEGORIE_SCENARI
    )
    cards = "".join(
        f'<a href="/societario/scenari/{s["slug"]}.html" class="cy-scenario-card" data-cat="{s["cat"]}" data-search="{esc(" ".join([s["cod"], s["titolo"], s["desc"], s["cat_lbl"], " ".join(s["keywords"]), " ".join(s["norme"])]))}"><div><div class="cy-sc-top"><span class="cy-sc-code">{s["cod"]}</span><span class="cy-sc-cat">{esc(s["cat_lbl"])}</span></div><h3>{esc(s["titolo"])}</h3><p>{esc(s["desc"])}</p></div><div class="cy-sc-foot"><span>{esc(s["norme"][0])}</span><span>Apri protocollo &rarr;</span></div></a>'
        for s in SCENARI
    )
    idx_ld = [
        {
            "@context": "https://schema.org",
            "@type": "ItemList",
            "name": "150 Protocolli Operativi di Diritto Societario, Modello 231 e Crisi d'Impresa",
            "numberOfItems": len(SCENARI),
            "itemListElement": [
                {"@type": "ListItem", "position": i + 1, "name": s["titolo"], "url": f"{BASE_URL}/societario/scenari/{s['slug']}.html"}
                for i, s in enumerate(SCENARI)
            ]
        }
    ]
    idx_body = f"""<body class="cyber-page">
<div class="cy-progress" aria-hidden="true"></div>
{GTM_BODY}
{nav_it("scenari")}
{alert_bar_it()}
<header class="cy-hero" style="padding:3.8rem 1.5rem 2.8rem;">
  <div class="cy-container">
    <nav class="cy-breadcrumb" aria-label="Percorso">
      <a href="/">Home</a> <span>/</span> <a href="/societario.html">Societario &amp; 231</a> <span>/</span> <span>150 Protocolli Operativi</span>
    </nav>
    <span class="cy-eyebrow">ARCHIVIO COMPLETO · 150 SCENARI</span>
    <h1>150 Protocolli di Difesa <em>Societaria</em>, 231 e Fallimentare</h1>
    <p class="cy-hero-lead">Cerca per parola chiave, articolo di legge o materia tra tutti i 150 scenari operativi su governance, liti tra soci, D.Lgs. 231/2001, Composizione Negoziata, concordato, liquidazione giudiziale, bancarotta, M&amp;A e fideiussioni.</p>
  </div>
</header>
<main class="cy-section">
  <div class="cy-container">
    <div class="cy-search-bar">
      <input type="search" id="cy-search-input" class="cy-search-input" placeholder="Cerca tra i 150 protocolli (es. 231, bancarotta, 2407, concordato, ABI, 2476)..." aria-label="Cerca tra i 150 protocolli">
      <span id="cy-count" class="cy-count-badge">150 / 150 protocolli</span>
    </div>
    <div class="cy-filter-pills">{filter_pills}</div>
    <div class="cy-scenarios-grid" id="cy-scenarios-grid">{cards}</div>
  </div>
</main>
{footer_it()}
{WA_FLOAT}
<script src="/js/cyber-wow.js?v=1" defer></script>
</body>
</html>"""
    (out_dir / "index.html").write_text(
        head_common("150 Protocolli Diritto Societario, Modello 231 e Fallimentare | Studio Iaccarino",
                    "Indice completo dei 150 protocolli legali operativi su governance S.r.l./S.p.A., D.Lgs. 231/2001, Composizione Negoziata CCII, concordato, liquidazione giudiziale, bancarotta e M&A.",
                    idx_canonical, idx_ld) + "\n" + idx_body,
        encoding="utf-8"
    )


def build_guide():
    out_dir = ROOT / "societario" / "guide"
    out_dir.mkdir(parents=True, exist_ok=True)
    for idx, g in enumerate(GUIDE_SOC):
        canonical = f"{BASE_URL}/societario/guide/{g['slug']}.html"
        prev_g = GUIDE_SOC[idx - 1] if idx > 0 else None
        next_g = GUIDE_SOC[idx + 1] if idx < len(GUIDE_SOC) - 1 else None
        prev_link = f'<a href="/societario/guide/{prev_g["slug"]}.html" class="cy-btn-cyber">&larr; {prev_g["cod"]}</a>' if prev_g else "<span></span>"
        next_link = f'<a href="/societario/guide/{next_g["slug"]}.html" class="cy-btn-cyber">{next_g["cod"]} &rarr;</a>' if next_g else "<span></span>"
        altre_guide = "".join(
            f'<li><a href="/societario/guide/{ag["slug"]}.html">{ag["cod"]} · {esc(ag["titolo"])}</a></li>'
            for ag in GUIDE_SOC if ag["slug"] != g["slug"]
        )
        ld_blocks = [
            {
                "@context": "https://schema.org",
                "@type": "Article",
                "headline": g["titolo"],
                "description": g["desc"],
                "author": {"@type": "Person", "name": "Avv. Francesco Iaccarino"},
                "datePublished": TODAY,
                "dateModified": TODAY,
                "mainEntityOfPage": canonical
            },
            {
                "@context": "https://schema.org",
                "@type": "FAQPage",
                "mainEntity": [
                    {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
                    for q, a in g["faqs"]
                ]
            }
        ]
        norme_tags = "".join(f'<span class="cy-tag">{esc(n)}</span>' for n in g["norme"])
        sez_html = "".join(f'<div class="cy-card-block"><h2>{esc(t)}</h2><p>{esc(c)}</p></div>' for t, c in g["sezioni"])
        chk_html = "".join(f"<li>{esc(x)}</li>" for x in g["checklist"])
        faq_html = "".join(f'<details class="cy-faq-item"><summary>{esc(q)}</summary><p>{esc(a)}</p></details>' for q, a in g["faqs"])

        body = f"""<body class="cyber-page">
<div class="cy-progress" aria-hidden="true"></div>
{GTM_BODY}
{nav_it("guide")}
{alert_bar_it()}
<header class="cy-hero" style="padding:3.6rem 1.5rem 2.5rem;">
  <div class="cy-container">
    <nav class="cy-breadcrumb" aria-label="Percorso">
      <a href="/">Home</a> <span>/</span> <a href="/societario.html">Societario &amp; 231</a> <span>/</span> <a href="/societario/guide/index.html">26 Guide</a> <span>/</span> <span>{g['cod']}</span>
    </nav>
    <span class="cy-eyebrow">{g['cod']} · GUIDA OPERATIVA</span>
    <h1>{esc(g['titolo'])}</h1>
    <p class="cy-hero-lead">{esc(g['intro'])}</p>
    <div class="cy-pillar-tags" style="margin-top:1.1rem;">{norme_tags}</div>
  </div>
</header>
<main class="cy-section">
  <div class="cy-container cy-article-layout">
    <article class="cy-article-body">
      {sez_html}
      <div class="cy-card-block">
        <h2>Checklist Operativa</h2>
        <ul class="cy-check-list">{chk_html}</ul>
      </div>
      <div class="cy-card-block">
        <h2>Domande Frequenti</h2>
        <div class="cy-faq-list">{faq_html}</div>
      </div>
      <div style="display:flex;justify-content:space-between;align-items:center;gap:1rem;flex-wrap:wrap;margin-top:2rem;">
        {prev_link}
        <a href="/societario/guide/index.html" class="cy-btn-primary">Tutte le 26 Guide Operative</a>
        {next_link}
      </div>
    </article>
    <aside class="cy-sidebar-box">
      <div class="cy-side-card">
        <h3>Assistenza su questa procedura?</h3>
        <p>Consulenza riservata a Napoli o da remoto in tutta Italia per gestire subito adempimenti, difese o urgenze societarie.</p>
        <a href="/consulenza.html?area=societario" class="cy-btn-primary" style="width:100%;justify-content:center;margin-bottom:.65rem;">Richiedi Consulenza</a>
        <a href="tel:+393335684659" class="cy-btn-cyber" style="width:100%;justify-content:center;">Chiama +39 333 568 4659</a>
      </div>
      <div class="cy-side-card">
        <h3>Altre Guide Societario &amp; 231</h3>
        <ul style="padding-left:1.1rem;margin:0;font-size:.84rem;line-height:1.68;">{altre_guide}</ul>
      </div>
    </aside>
  </div>
</main>
{footer_it()}
{WA_FLOAT}
<script src="/js/cyber-wow.js?v=1" defer></script>
</body>
</html>"""
        (out_dir / f"{g['slug']}.html").write_text(
            head_common(f"{g['seo_title']} | Studio Iaccarino", g["desc"], canonical, ld_blocks) + "\n" + body,
            encoding="utf-8"
        )

    idx_canonical = f"{BASE_URL}/societario/guide/index.html"
    cards = "".join(
        f'<a href="/societario/guide/{g["slug"]}.html" class="cy-scenario-card"><div><div class="cy-sc-top"><span class="cy-sc-code">{g["cod"]}</span><span class="cy-sc-cat">Guida Operativa</span></div><h3>{esc(g["titolo"])}</h3><p>{esc(g["desc"])}</p></div><div class="cy-sc-foot"><span>{esc(g["norme"][0])}</span><span>Leggi guida &rarr;</span></div></a>'
        for g in GUIDE_SOC
    )
    idx_ld = [
        {
            "@context": "https://schema.org",
            "@type": "ItemList",
            "name": "26 Guide Operative di Diritto Societario, Modello 231 e Crisi d'Impresa",
            "numberOfItems": len(GUIDE_SOC),
            "itemListElement": [
                {"@type": "ListItem", "position": i + 1, "name": g["titolo"], "url": f"{BASE_URL}/societario/guide/{g['slug']}.html"}
                for i, g in enumerate(GUIDE_SOC)
            ]
        }
    ]
    idx_body = f"""<body class="cyber-page">
<div class="cy-progress" aria-hidden="true"></div>
{GTM_BODY}
{nav_it("guide")}
{alert_bar_it()}
<header class="cy-hero" style="padding:3.8rem 1.5rem 2.8rem;">
  <div class="cy-container">
    <nav class="cy-breadcrumb" aria-label="Percorso">
      <a href="/">Home</a> <span>/</span> <a href="/societario.html">Societario &amp; 231</a> <span>/</span> <span>26 Guide Operative</span>
    </nav>
    <span class="cy-eyebrow">MANUALISTICA OPERATIVA · CHECKLIST LEGALI</span>
    <h1>26 Guide Operative di <em>Societario</em>, 231 e Crisi d'Impresa</h1>
    <p class="cy-hero-lead">Procedure passo passo, scadenze di legge e checklist forensi su adeguati assetti, Modello 231, OdV, whistleblowing, Composizione Negoziata, concordato, transazione fiscale, liquidazione giudiziale, bancarotta, riforma sindaci L. 35/2025 e fideiussioni.</p>
  </div>
</header>
<main class="cy-section">
  <div class="cy-container">
    <div class="cy-scenarios-grid">{cards}</div>
  </div>
</main>
{footer_it()}
{WA_FLOAT}
<script src="/js/cyber-wow.js?v=1" defer></script>
</body>
</html>"""
    (out_dir / "index.html").write_text(
        head_common("26 Guide Operative Societario, Modello 231 e Crisi d'Impresa | Studio Iaccarino",
                    "Guide pratiche e checklist legali su adeguati assetti art. 2086, Modello 231, OdV, Composizione Negoziata CCII, concordato, liquidazione giudiziale, bancarotta e M&A.",
                    idx_canonical, idx_ld) + "\n" + idx_body,
        encoding="utf-8"
    )


def build_multilingua():
    for code, data in LINGUE_ESTERE.items():
        lang_dir = ROOT / code
        lang_dir.mkdir(parents=True, exist_ok=True)
        canonical = f"{BASE_URL}/{code}/societario.html"
        ld_blocks = [
            {
                "@context": "https://schema.org",
                "@type": "LegalService",
                "name": f"Studio Legale Avv. Francesco Iaccarino - {data['nav_soc']}",
                "url": canonical,
                "description": data["desc"],
                "telephone": "+393335684659",
                "areaServed": {"@type": "Country", "name": "Italy"}
            }
        ]
        cards = []
        for idx, (num, pt, pd) in enumerate(data["pillars"]):
            slug = PILASTRI[idx]["slug"]
            cards.append(f"""<a href="/societario/{slug}.html" class="cy-pillar-card">
  <span class="cy-pillar-num">{num}</span>
  <div class="cy-pillar-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">{PILASTRI[idx]['icona']}</svg></div>
  <div>
    <h3>{esc(pt)}</h3>
    <p>{esc(pd)}</p>
    <span class="cy-link-more">&rarr;</span>
  </div>
</a>""")
        dir_attr = f' dir="{data["dir"]}"' if data["dir"] == "rtl" else ""
        head = head_common(data["title"], data["desc"], canonical, ld_blocks, lang=data["locale"], locale=data["locale"], include_hreflang=True)
        head = head.replace(f'<html lang="{data["locale"]}">', f'<html lang="{data["locale"]}"{dir_attr}>')

        body = f"""<body class="cyber-page">
<div class="cy-progress" aria-hidden="true"></div>
{lang_switcher(data['name'])}
{GTM_BODY}
<nav class="cy-nav" role="navigation">
  <div class="cy-nav-inner">
    <a href="/{code}/" class="cy-logo">Studio Legale Iaccarino <span class="cy-logo-badge">Corporate &amp; 231</span></a>
    <div class="cy-nav-links">
      <a href="/{code}/">{esc(data['nav_home'])}</a>
      <a href="/{code}/penale.html">{esc(data['nav_penale'])}</a>
      <a href="/{code}/civile.html">{esc(data['nav_civile'])}</a>
      <a href="/{code}/tributario.html">{esc(data['nav_trib'])}</a>
      <a href="/{code}/immigrazione.html">{esc(data['nav_imm'])}</a>
      <a href="/{code}/cybersicurezza.html">{esc(data['nav_cyber'])}</a>
      <a href="/{code}/societario.html" class="active">{esc(data['nav_soc'])}</a>
      <a href="/consulenza.html?area=societario" class="cy-nav-cta">{esc(data['nav_cta'])}</a>
    </div>
  </div>
</nav>
<div class="cy-alert-bar">
  <div class="cy-alert-inner">
    <div class="cy-alert-left">
      <span class="cy-pulse-dot" aria-hidden="true"></span>
      <span class="cy-alert-tag">{esc(data['alert_tag'])}</span>
      <span>{esc(data['alert_text'])}</span>
    </div>
    <div class="cy-alert-actions">
      <a href="https://wa.me/393335684659?text=CORPORATE%20231%20ITALY" target="_blank" rel="noopener noreferrer" class="cy-btn-urgent">{esc(data['cta_urgent'])}</a>
    </div>
  </div>
</div>
<header class="cy-hero">
  <div class="cy-container">
    <span class="cy-eyebrow">{esc(data['eyebrow'])}</span>
    <h1>{data['h1']}</h1>
    <p class="cy-hero-lead">{esc(data['lead'])}</p>
    <div class="cy-cta-row">
      <a href="/consulenza.html?area=societario" class="cy-btn-primary">{esc(data['cta_book'])}</a>
      <a href="/societario.html" class="cy-btn-cyber">{esc(data['cta_it'])}</a>
    </div>
  </div>
</header>
<main class="cy-section">
  <div class="cy-container">
    <h2 class="cy-sec-title">{esc(data['pillars_title'])}</h2>
    <p class="cy-sec-sub">{esc(data['pillars_sub'])}</p>
    <div class="cy-pillars-grid">{''.join(cards)}</div>
  </div>
</main>
{footer_it()}
{WA_FLOAT}
<script src="/js/cyber-wow.js?v=1" defer></script>
</body>
</html>"""
        (lang_dir / "societario.html").write_text(head + "\n" + body, encoding="utf-8")


def integrate_existing_pages():
    # 1. Aggiorna index.html (JSON-LD + nav + sezione aree)
    idx_path = ROOT / "index.html"
    txt = idx_path.read_text(encoding="utf-8")
    if "societario.html" not in txt:
        txt = txt.replace(
            '"knowsAbout": ["Diritto Penale","Diritto Civile","Diritto del Lavoro","Diritto Tributario","Diritto dell\'Immigrazione","Cybersicurezza","Protezione Dati GDPR","Direttiva NIS2","Reati Informatici"]',
            '"knowsAbout": ["Diritto Penale","Diritto Civile","Diritto del Lavoro","Diritto Tributario","Diritto dell\'Immigrazione","Cybersicurezza","Protezione Dati GDPR","Direttiva NIS2","Reati Informatici","Diritto Societario","Modello 231","Crisi d\'Impresa CCII","Diritto Fallimentare"]'
        )
        txt = txt.replace(
            '{ "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Cybersicurezza, GDPR, NIS2 e Reati Informatici", "url": "https://studiolegalefrancescoiaccarino.com/cybersicurezza.html" } }',
            '{ "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Cybersicurezza, GDPR, NIS2 e Reati Informatici", "url": "https://studiolegalefrancescoiaccarino.com/cybersicurezza.html" } },\n          { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Diritto Societario, Modello 231 e Crisi d\'Impresa", "url": "https://studiolegalefrancescoiaccarino.com/societario.html" } }'
        )
        txt = txt.replace(
            '"name": ["Diritto Penale", "Diritto Civile", "Diritto Tributario", "Immigrazione", "Cybersicurezza", "Guide Legali", "Prenota Consulenza", "Richiedi Consulenza"]',
            '"name": ["Diritto Penale", "Diritto Civile", "Diritto Tributario", "Immigrazione", "Cybersicurezza", "Societario e 231", "Guide Legali", "Prenota Consulenza", "Richiedi Consulenza"]'
        )
        txt = txt.replace(
            '"https://studiolegalefrancescoiaccarino.com/cybersicurezza.html",',
            '"https://studiolegalefrancescoiaccarino.com/cybersicurezza.html",\n        "https://studiolegalefrancescoiaccarino.com/societario.html",'
        )
        txt = txt.replace(
            '<a href="/cybersicurezza.html">Cybersicurezza e Protezione Dati</a>',
            '<a href="/cybersicurezza.html">Cybersicurezza e Protezione Dati</a>\n          <a href="/societario.html">Diritto Societario, 231 e Fallimentare</a>'
        )
        txt = txt.replace(
            '<a href="/cybersicurezza.html">Approfondisci Cybersicurezza</a>.</p>',
            '<a href="/cybersicurezza.html">Approfondisci Cybersicurezza</a>.</p>\n          <p><strong>Diritto Societario, Modello 231 e Crisi d\'Impresa:</strong> governance S.r.l. e S.p.A., adeguati assetti (art. 2086 c.c.), Modelli Organizzativi 231 e difesa da sequestri e misure interdittive, Composizione Negoziata (CCII e D.Lgs. 136/2024), concordato preventivo, transazione fiscale, liquidazione giudiziale, bancarotta, M&amp;A e fideiussioni, con 150 protocolli operativi e 26 guide. <a href="/societario.html">Approfondisci Societario e 231</a>.</p>'
        )
        idx_path.write_text(txt, encoding="utf-8")

    # 2. Aggiorna nav e footer delle pagine di area principali (IT)
    for area_file in ["penale.html", "civile.html", "tributario.html", "immigrazione.html", "cybersicurezza.html"]:
        p = ROOT / area_file
        if not p.exists():
            continue
        t = p.read_text(encoding="utf-8")
        if "societario.html" not in t:
            t = t.replace(
                '<a href="cybersicurezza.html" class="nav-back">Cybersicurezza</a>',
                '<a href="cybersicurezza.html" class="nav-back">Cybersicurezza</a>\n      <a href="societario.html" class="nav-back">Societario &amp; 231</a>'
            )
            t = t.replace(
                '<a href="cybersicurezza.html">Cybersicurezza</a>',
                '<a href="cybersicurezza.html">Cybersicurezza</a>\n    <a href="societario.html">Societario &amp; 231</a>'
            )
            t = t.replace(
                '<a href="/cybersicurezza.html" class="active">Cybersicurezza</a>',
                '<a href="/cybersicurezza.html" class="active">Cybersicurezza</a>\n      <a href="/societario.html">Societario &amp; 231</a>'
            )
            p.write_text(t, encoding="utf-8")

    # 3. Aggiorna sitemap.xml (hub + 12 pilastri + indice scenari + indice guide)
    sm_path = ROOT / "sitemap.xml"
    sm = sm_path.read_text(encoding="utf-8")
    new_urls = [
        (f"{BASE_URL}/societario.html", "weekly", "0.95"),
        (f"{BASE_URL}/societario/scenari/index.html", "weekly", "0.90"),
        (f"{BASE_URL}/societario/guide/index.html", "weekly", "0.90"),
    ] + [(f"{BASE_URL}/societario/{p['slug']}.html", "weekly", "0.85") for p in PILASTRI]
    entries = []
    for u, freq, prio in new_urls:
        if u not in sm:
            entries.append(f"  <url>\n    <loc>{u}</loc>\n    <lastmod>{TODAY}</lastmod>\n    <changefreq>{freq}</changefreq>\n    <priority>{prio}</priority>\n  </url>")
    if entries:
        sm = sm.replace("</urlset>", "\n".join(entries) + "\n</urlset>")
        sm_path.write_text(sm, encoding="utf-8")

    # 4. Aggiorna sitemap-guide-casi.xml con tutti i 150 scenari e le 26 guide
    sm2_path = ROOT / "sitemap-guide-casi.xml"
    if sm2_path.exists():
        sm2 = sm2_path.read_text(encoding="utf-8")
        sc_entries = []
        for s in SCENARI:
            u = f"{BASE_URL}/societario/scenari/{s['slug']}.html"
            if u not in sm2:
                sc_entries.append(f"  <url>\n    <loc>{u}</loc>\n    <lastmod>{TODAY}</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>0.80</priority>\n  </url>")
        for g in GUIDE_SOC:
            u = f"{BASE_URL}/societario/guide/{g['slug']}.html"
            if u not in sm2:
                sc_entries.append(f"  <url>\n    <loc>{u}</loc>\n    <lastmod>{TODAY}</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>0.82</priority>\n  </url>")
        if sc_entries:
            sm2 = sm2.replace("</urlset>", "\n".join(sc_entries) + "\n</urlset>")
            sm2_path.write_text(sm2, encoding="utf-8")

    # 5. Aggiorna sitemap-lingue.xml con le 9 lingue estere
    sm3_path = ROOT / "sitemap-lingue.xml"
    if sm3_path.exists():
        sm3 = sm3_path.read_text(encoding="utf-8")
        lg_entries = []
        for code in LINGUE_ESTERE:
            u = f"{BASE_URL}/{code}/societario.html"
            if u not in sm3:
                lg_entries.append(f"  <url>\n    <loc>{u}</loc>\n    <lastmod>{TODAY}</lastmod>\n    <changefreq>weekly</changefreq>\n    <priority>0.85</priority>\n  </url>")
        if lg_entries:
            sm3 = sm3.replace("</urlset>", "\n".join(lg_entries) + "\n</urlset>")
            sm3_path.write_text(sm3, encoding="utf-8")


def validate_all():
    errors = []
    assert len(PILASTRI) == 12, f"Pilastri={len(PILASTRI)}"
    assert len(SCENARI) == 150, f"Scenari={len(SCENARI)}"
    assert len(GUIDE_SOC) == 26, f"Guide={len(GUIDE_SOC)}"
    assert len(LINGUE_ESTERE) == 9, f"Lingue={len(LINGUE_ESTERE)}"

    if len(set(s["slug"] for s in SCENARI)) != 150:
        errors.append("Slug duplicati nei 150 scenari!")
    if len(set(s["titolo"] for s in SCENARI)) != 150:
        errors.append("Titoli duplicati nei 150 scenari!")
    if len(set(g["slug"] for g in GUIDE_SOC)) != 26:
        errors.append("Slug duplicati nelle 26 guide!")

    files_to_check = [
        ROOT / "societario.html",
        ROOT / "societario" / "scenari" / "index.html",
        ROOT / "societario" / "guide" / "index.html",
    ] + [ROOT / "societario" / f"{p['slug']}.html" for p in PILASTRI] \
      + [ROOT / "societario" / "scenari" / f"{s['slug']}.html" for s in SCENARI] \
      + [ROOT / "societario" / "guide" / f"{g['slug']}.html" for g in GUIDE_SOC] \
      + [ROOT / code / "societario.html" for code in LINGUE_ESTERE]

    assert len(files_to_check) == 200, f"Attese 200 URL esatte, trovate {len(files_to_check)}"

    for f in files_to_check:
        if not f.exists():
            errors.append(f"File mancante: {f}")
            continue
        raw = f.read_text(encoding="utf-8")
        for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', raw, re.S):
            try:
                json.loads(m.group(1))
            except Exception as ex:
                errors.append(f"JSON-LD non valido in {f.name}: {ex}")
        for href in re.findall(r'href="(/societario[^"#?]*)"', raw):
            target = ROOT / href.lstrip("/")
            if not target.exists():
                errors.append(f"Link interno rotto in {f.name}: {href}")
        if "«" in raw or "»" in raw:
            errors.append(f"Caporali trovati in {f.name}")
        if re.search(r"(cassazion|corte\s+di\s+giustizia)", raw, re.I):
            errors.append(f"Cassazione o Corte di Giustizia trovata in {f.name}")

    print(f"FILE SOCIETARIO GENERATI E VERIFICATI: {len(files_to_check)}")
    print(f"PILASTRI: {len(PILASTRI)} | SCENARI: {len(SCENARI)} | GUIDE: {len(GUIDE_SOC)} | LINGUE ESTERE: {len(LINGUE_ESTERE)}")
    if errors:
        print("ERRORI RILEVATI:")
        for e in errors[:20]:
            print(" -", e)
        sys.exit(1)
    else:
        print("VALIDAZIONE OK: 200/200 URL, 0 ERRORI, 0 LINK ROTTI, 0 JSON-LD INVALIDI, 0 DUPLICATI, 0 CASSAZIONE/CG.")


if __name__ == "__main__":
    build_hub_it()
    build_pilastri()
    build_scenari()
    build_guide()
    build_multilingua()
    integrate_existing_pages()
    validate_all()
