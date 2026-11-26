# -*- coding: utf-8 -*-
"""
Generatore completo della 5a area strutturale del sito Studio Legale Avv. Francesco Iaccarino:
- Hub principale: cybersicurezza.html
- 10 pagine pilastro: cybersicurezza/<slug>.html
- Indice + 70 pagine scenari operativi: cybersicurezza/scenari/index.html e cybersicurezza/scenari/<slug>.html
- 9 pagine hub in tutte le lingue estere del sito: en/, es/, pt/, ru/, ar/, zh/, hi/, bn/, si/
- Aggiornamento menu/footer di index.html, penale.html, civile.html, tributario.html, immigrazione.html
- Aggiornamento sitemap.xml, sitemap-guide-casi.xml, sitemap-lingue.xml
- Validazione automatica finale (link, lunghezza, unicita', zero trattini lunghi, zero caporali).
"""
import html
import json
import os
import re
import sys
from pathlib import Path

ROOT = Path(r"D:\STUDIO LEGALE\MODELLI E FORMULARI\Nuovo sito internet\_SITO_GITHUB_PAGES\sito")
BASE_URL = "https://studiolegalefrancescoiaccarino.com"
OG_IMG = f"{BASE_URL}/img/og-cybersicurezza.jpg"
TODAY = "2026-11-26"

sys.path.insert(0, str(ROOT / "_strumenti"))
from cyber_dati.pilastri import PILASTRI, COMPASS_DATA, CATEGORIE_SCENARI, LINGUE_ESTERE
from cyber_dati.scenari_a import SCENARI_A
from cyber_dati.scenari_b import SCENARI_B
from cyber_dati.scenari_c import SCENARI_C
from cyber_dati.guide_cyber import GUIDE_CYBER

SCENARI = SCENARI_A + SCENARI_B + SCENARI_C
PILASTRI_BY_SLUG = {p["slug"]: p for p in PILASTRI}

ALL_LANGS = [
    ("it", "it", "Italiano", "/cybersicurezza.html"),
    ("en", "en", "English", "/en/cybersicurezza.html"),
    ("es", "es", "Español", "/es/cybersicurezza.html"),
    ("pt", "pt", "Português", "/pt/cybersicurezza.html"),
    ("ru", "ru", "Русский", "/ru/cybersicurezza.html"),
    ("ar", "ar", "العربية", "/ar/cybersicurezza.html"),
    ("zh", "zh-Hans", "中文", "/zh/cybersicurezza.html"),
    ("hi", "hi", "हिन्दी", "/hi/cybersicurezza.html"),
    ("bn", "bn", "বাংলা", "/bn/cybersicurezza.html"),
    ("si", "si", "සිංහල", "/si/cybersicurezza.html"),
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
<a id="wa-float" href="https://wa.me/393335684659?text=EMERGENZA%20CYBER%3A%20richiedo%20assistenza%20legale%20urgente%20per%20cybersicurezza%20o%20data%20breach." target="_blank" rel="noopener noreferrer" aria-label="Scrivi allo Studio su WhatsApp">
  <svg viewBox="0 0 32 32" fill="currentColor" aria-hidden="true"><path d="M16.02 3.2c-7.06 0-12.8 5.74-12.8 12.8 0 2.26.59 4.47 1.72 6.42L3.2 28.8l6.55-1.71a12.74 12.74 0 0 0 6.27 1.6h.01c7.05 0 12.79-5.74 12.79-12.8 0-3.42-1.33-6.63-3.75-9.05a12.7 12.7 0 0 0-9.05-3.64zm0 23.34h-.01c-1.98 0-3.93-.53-5.63-1.54l-.4-.24-4.18 1.1 1.11-4.08-.26-.42a10.6 10.6 0 0 1-1.63-5.66c0-5.87 4.78-10.64 10.65-10.64 2.84 0 5.51 1.11 7.52 3.12a10.57 10.57 0 0 1 3.11 7.53c0 5.87-4.77 10.64-10.64 10.64zm5.84-7.97c-.32-.16-1.89-.93-2.18-1.04-.29-.11-.5-.16-.71.16-.21.32-.82 1.04-1.01 1.25-.18.21-.37.24-.69.08-.32-.16-1.35-.5-2.57-1.59-.95-.85-1.59-1.89-1.78-2.21-.18-.32-.02-.5.14-.66.14-.14.32-.37.48-.56.16-.19.21-.32.32-.53.11-.21.05-.4-.03-.56-.08-.16-.71-1.72-.98-2.35-.26-.62-.52-.54-.71-.55l-.61-.01c-.21 0-.56.08-.85.4-.29.32-1.11 1.09-1.11 2.65 0 1.56 1.14 3.07 1.3 3.28.16.21 2.25 3.43 5.45 4.81.76.33 1.35.52 1.82.67.76.24 1.46.21 2.01.13.61-.09 1.89-.77 2.16-1.52.27-.75.27-1.38.19-1.52-.08-.13-.29-.21-.61-.37z"/></svg>
  <span class="wa-txt">Urgenze Cyber WhatsApp</span>
</a>"""


def esc(s: str) -> str:
    return html.escape(str(s), quote=True)


def hreflang_block() -> str:
    lines = [
        f'<link rel="alternate" hreflang="x-default" href="{BASE_URL}/cybersicurezza.html">'
    ]
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


def nav_it(active: str = "cyber") -> str:
    return f"""<nav class="cy-nav" role="navigation" aria-label="Menu principale">
  <div class="cy-nav-inner">
    <a href="/" class="cy-logo">Studio Legale Iaccarino <span class="cy-logo-badge">Cyber Law</span></a>
    <div class="cy-nav-links">
      <a href="/">Home</a>
      <a href="/penale.html">Penale</a>
      <a href="/civile.html">Civile</a>
      <a href="/tributario.html">Tributario</a>
      <a href="/immigrazione.html">Immigrazione</a>
      <a href="/cybersicurezza.html" class="{'active' if active=='cyber' else ''}">Cybersicurezza</a>
      <a href="/cybersicurezza/scenari/index.html" class="{'active' if active=='scenari' else ''}">110 Protocolli</a>
      <a href="/cybersicurezza/guide/index.html" class="{'active' if active=='guide' else ''}">Guide Cyber</a>
      <a href="/consulenza.html?area=cybersicurezza" class="cy-nav-cta">Richiedi Consulenza</a>
    </div>
  </div>
</nav>"""


def alert_bar_it() -> str:
    return """<div class="cy-alert-bar" role="region" aria-label="Pronto intervento emergenza cyber">
  <div class="cy-alert-inner">
    <div class="cy-alert-left">
      <span class="cy-pulse-dot" aria-hidden="true"></span>
      <span class="cy-alert-tag">Desk Emergenze 24h / 72h</span>
      <span>Attacco ransomware, data breach o conto svuotato in corso? Le scadenze ACN (24h) e Garante GDPR (72h) decorrono subito.</span>
    </div>
    <div class="cy-alert-actions">
      <a href="tel:+393335684659" class="cy-btn-urgent">Chiama +39 333 568 4659</a>
      <a href="/consulenza.html?area=cybersicurezza&amp;urgenza=si" class="cy-btn-urgent">Attiva Protocollo Urgenza</a>
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
      <a href="/cybersicurezza/scenari/index.html">110 Protocolli Cyber</a>
      <a href="/cybersicurezza/guide/index.html">18 Guide Operative</a>
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
    canonical = f"{BASE_URL}/cybersicurezza.html"
    faqs_hub = [
        ("Quando scatta l'obbligo di notifica di un data breach al Garante Privacy?", "Ai sensi dell'articolo 33 del Regolamento (UE) 2016/679 (GDPR), il titolare del trattamento deve notificare la violazione dei dati personali al Garante senza ingiustificato ritardo e, ove possibile, entro 72 ore dal momento in cui ne viene a conoscenza, salvo che sia improbabile che l'evento presenti un rischio per i diritti e le liberta' delle persone fisiche."),
        ("Quali aziende rientrano nella Direttiva NIS2 (D.Lgs. 138/2024) in Italia?", "Il D.Lgs. 138/2024 distingue soggetti essenziali e soggetti importanti in base ai settori degli Allegati I e II (energia, trasporti, sanita', digitale, manifattura critica, logistica, alimentare, PA e filiera ICT) e alle soglie dimensionali di medie e grandi imprese, con obbligo di registrazione sul portale ACN e notifica incidenti in 24 e 72 ore."),
        ("Cosa prevede la Legge 90/2024 sull'estorsione informatica e sui reati cyber?", "La Legge 28 giugno 2024, n. 90 ha introdotto il nuovo reato di estorsione informatica all'art. 629 comma 3 c.p. (mirato anche agli attacchi ransomware), ha aumentato fino a 10-12 anni le pene per l'accesso abusivo aggravato (art. 615-ter c.p.) e ha aggiornato l'art. 24-bis del D.Lgs. 231/2001 sulla responsabilita' delle societa'."),
        ("Se subisco phishing, SMS spoofing o SIM swap posso ottenere il rimborso dalla banca?", "Si': gli articoli 10 e 12 del D.Lgs. 11/2010 (recepimento PSD2) pongono sulla banca l'onere rigoroso di provare l'autenticazione forte (SCA) e il dolo o la colpa grave del cliente. In assenza di tale prova tecnica si agisce tramite reclamo, Arbitro Bancario Finanziario (ABF) o Tribunale."),
        ("Come vengono gestiti i 70 protocolli operativi pubblicati in questa sezione?", "I 70 protocolli sono scenari operativi tipo elaborati sulle norme italiane ed europee vigenti per orientare subito imprese e privati sulle prime mosse, sulle prove da preservare e sugli errori da evitare. Sono distinti dall'archivio dei casi reali seguiti dallo Studio (consultabile nella pagina Casi Risolti) e ogni vicenda concreta richiede una valutazione dedicata sui propri documenti."),
        ("Lo Studio assiste aziende e privati in cybersicurezza in tutta Italia?", "Si'. La sede e' a Napoli in Palazzo Barbaja, Via Toledo 205, ma il desk legale di Cybersicurezza e Protezione Dati opera da remoto e presso tutti i Tribunali, le Procure, il Garante Privacy, l'ACN e l'ABF sull'intero territorio nazionale.")
    ]
    ld_blocks = [
        {
            "@context": "https://schema.org",
            "@type": "LegalService",
            "name": "Studio Legale Avv. Francesco Iaccarino - Cybersicurezza e Protezione Dati",
            "url": canonical,
            "image": OG_IMG,
            "description": "Assistenza legale in cybersicurezza, data breach 72 ore GDPR, ransomware, Direttiva NIS2 (D.Lgs. 138/2024), Legge 90/2024, reati informatici, phishing bancario, Modello 231 e AI Act in tutta Italia.",
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
                {"@type": "ListItem", "position": 2, "name": "Cybersicurezza e Protezione Dati", "item": canonical}
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
        pillars_html.append(f"""<a href="/cybersicurezza/{p['slug']}.html" class="cy-pillar-card">
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
        scenario_cards.append(f"""<a href="/cybersicurezza/scenari/{s['slug']}.html" class="cy-scenario-card" data-cat="{s['cat']}" data-search="{esc(search_blob)}">
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

    body = f"""<body class="cyber-page">
<div class="cy-progress" aria-hidden="true"></div>
{lang_switcher("Italiano")}
{GTM_BODY}
{nav_it("cyber")}
{alert_bar_it()}

<header class="cy-hero">
  <div class="cy-container">
    <nav class="cy-breadcrumb" aria-label="Percorso">
      <a href="/">Home</a> <span>/</span> <span>Cybersicurezza e Protezione Dati</span>
    </nav>
    <div class="cy-hero-grid">
      <div>
        <span class="cy-eyebrow">CYBER LAW, DATA PROTECTION &amp; INCIDENT RESPONSE</span>
        <h1>Avvocato <em>Cybersicurezza</em> e Protezione Dati in Italia</h1>
        <p class="cy-hero-lead">Difesa legale immediata per imprese, consigli di amministrazione, professionisti e privati: gestione crisi data breach (72 ore GDPR), ransomware ed estorsione informatica (L. 90/2024), adeguamento Direttiva NIS2 e ACN (D.Lgs. 138/2024), reati informatici, rimborso frodi bancarie, Modello 231 e AI Act.</p>
        <div class="cy-cta-row">
          <a href="/consulenza.html?area=cybersicurezza" class="cy-btn-primary">Richiedi Consulenza Legale</a>
          <a href="#bussola-crisi" class="cy-btn-cyber">Bussola Emergenza 30 Minuti &darr;</a>
        </div>
      </div>
      <aside aria-label="Scultura e scadenze legali di emergenza cyber">
        <div class="cy-sculpture-stage">
          <img src="/assets/sculptures/cybersicurezza.png" alt="Cybersicurezza e Protezione Dati - Monolite crittografico in marmo Nero Marquina e ottone satinato" loading="eager">
          <div class="cy-sculpture-caption">
            <span>05 · CYBERSICUREZZA</span>
            <span>PALAZZO BARBAJA · NAPOLI</span>
          </div>
        </div>
        <div class="cy-radar-card">
        <div class="cy-radar-head">
          <span class="cy-radar-title">Scadenze Critiche di Legge</span>
          <span class="cy-radar-status">DESK ATTIVO</span>
        </div>
        <div class="cy-clock-grid">
          <div class="cy-clock-box urgent">
            <div class="cy-clock-num">24 ORE</div>
            <div class="cy-clock-lbl">Preallarme ACN / CSIRT Italia (art. 25 D.Lgs. 138/2024 NIS2 e PA L. 90/2024)</div>
          </div>
          <div class="cy-clock-box cyan">
            <div class="cy-clock-num">72 ORE</div>
            <div class="cy-clock-lbl">Notifica Data Breach al Garante Privacy (art. 33 Reg. UE 2016/679 GDPR)</div>
          </div>
        </div>
        <ul class="cy-radar-list">
          <li><strong>Breach Coaching legale-tecnico</strong> in coordinamento con forensi IT e DPO</li>
          <li><strong>Difesa penale e parte civile</strong> post Legge 90/2024 (pene fino a 10-12 anni)</li>
          <li><strong>Recupero somme da phishing, SIM swap e frode BEC</strong> (D.Lgs. 11/2010 e ABF)</li>
          <li><strong>Governance imprese:</strong> NIS2, Modello 231 art. 24-bis, Cloud/SaaS e AI Act</li>
        </ul>
        <a href="https://wa.me/393335684659?text=EMERGENZA%20CYBER%3A%20richiedo%20assistenza%20legale%20urgente." target="_blank" rel="noopener noreferrer" class="cy-btn-primary" style="width:100%;justify-content:center;">Attiva Desk Urgenze su WhatsApp</a>
        </div>
      </aside>
    </div>
    <div class="cy-kpi-strip">
      <div class="cy-kpi"><strong>10 Aree Pilastro</strong><span>Copertura completa: imprese, PA, penale, banche, lavoro e IA</span></div>
      <div class="cy-kpi"><strong>110 Protocolli</strong><span>Scenari operativi verificati su norme vigenti italiane ed europee</span></div>
      <div class="cy-kpi"><strong>18 Guide Legali</strong><span>Checklist operative per Garante 72h, ACN 24h, ABF, 231 e AI Act</span></div>
      <div class="cy-kpi"><strong>Tutta Italia</strong><span>Sede a Napoli (Via Toledo 205) e operativita' nazionale e internazionale</span></div>
    </div>
  </div>
</header>

<section class="cy-section cy-section-alt" id="bussola-crisi">
  <div class="cy-container">
    <span class="cy-sec-label">Strumento Operativo Immediato</span>
    <h2 class="cy-sec-title">Bussola di Emergenza: che cosa ti e' successo?</h2>
    <p class="cy-sec-sub">Seleziona lo scenario piu' vicino al tuo problema per vedere subito le 3 mosse legali e tecniche da compiere nei primi 30 minuti, le scadenze di legge e le autorita' competenti.</p>
    <div class="cy-compass">
      <div class="cy-compass-tabs" role="tablist" aria-label="Scenari di emergenza cyber">
        <button type="button" class="cy-compass-btn active" data-key="ransomware">Attacco Ransomware</button>
        <button type="button" class="cy-compass-btn" data-key="databreach">Data Breach / Furto Dati</button>
        <button type="button" class="cy-compass-btn" data-key="phishing">Phishing / Conto Svuotato</button>
        <button type="button" class="cy-compass-btn" data-key="dipendente">Ex Dipendente Ruba Dati</button>
        <button type="button" class="cy-compass-btn" data-key="nis2">Adeguamento NIS2 / ACN</button>
        <button type="button" class="cy-compass-btn" data-key="penale">Avviso di Garanzia / Sequestro</button>
        <button type="button" class="cy-compass-btn" data-key="reputazione">Deepfake / Revenge Porn</button>
        <button type="button" class="cy-compass-btn" data-key="ai231">Contratti IT / AI Act / 231</button>
      </div>
      <div class="cy-compass-panel">
        <div>
          <h3 id="cy-c-title">Attacco Ransomware o Blocco Sistemi in Corso</h3>
          <p id="cy-c-desc" style="color:var(--cy-soft);margin:0;">Ogni minuto conta per preservare le prove digitali e rispettare le scadenze di legge.</p>
          <ul class="cy-compass-steps" id="cy-c-steps"></ul>
        </div>
        <div class="cy-compass-meta">
          <div class="cy-meta-row"><span class="cy-meta-k">Scadenza critica</span><span class="cy-meta-v" id="cy-c-deadline"></span></div>
          <div class="cy-meta-row"><span class="cy-meta-k">Norme chiave vigenti</span><span class="cy-meta-v" id="cy-c-norm"></span></div>
          <div class="cy-meta-row"><span class="cy-meta-k">Autorita' coinvolte</span><span class="cy-meta-v" id="cy-c-auth"></span></div>
          <div style="margin-top:1.2rem;display:grid;gap:.65rem;">
            <a id="cy-c-link" href="/cybersicurezza/ransomware-estorsione-informatica.html" class="cy-btn-cyber" style="justify-content:center;">Apri protocollo completo</a>
            <a href="/consulenza.html?area=cybersicurezza" class="cy-btn-primary" style="justify-content:center;">Parla con l'Avvocato</a>
          </div>
        </div>
      </div>
    </div>
    <script id="cy-compass-data" type="application/json">{json.dumps(COMPASS_DATA, ensure_ascii=False)}</script>
  </div>
</section>

<section class="cy-section" id="pilastri">
  <div class="cy-container">
    <span class="cy-sec-label">Architettura delle Competenze</span>
    <h2 class="cy-sec-title">10 Aree Pilastro di Cybersicurezza e Diritto Digitale</h2>
    <p class="cy-sec-sub">Dall'emergenza data breach e ransomware alla difesa penale informatica, dal recupero somme bancarie alla compliance NIS2, GDPR, Modello 231 e Regolamento Europeo AI Act.</p>
    <div class="cy-pillars-grid">
      {''.join(pillars_html)}
    </div>
  </div>
</section>

<section class="cy-section cy-section-alt" id="timeline-72h">
  <div class="cy-container">
    <span class="cy-sec-label">Metodo Incident Response</span>
    <h2 class="cy-sec-title">La Cronologia Legale delle Prime 72 Ore</h2>
    <p class="cy-sec-sub">Nelle crisi informatiche gli errori commessi nella prima giornata costano piu' dell'attacco stesso. Ecco la sequenza strutturata con cui coordiniamo difesa legale, tecnici IT e autorita'.</p>
    <div class="cy-timeline">
      <div class="cy-step-card">
        <span class="cy-step-time">ORE 00 - 02</span>
        <h3>Contenimento e Prove Forensi</h3>
        <p>Isolamento controllato dei sistemi, revoca credenziali, attivazione del privilegio legale e preservazione certificata dei log e degli indicatori di compromissione senza formattare.</p>
      </div>
      <div class="cy-step-card s2">
        <span class="cy-step-time">ORE 02 - 24</span>
        <h3>Preallarme ACN e Denuncia</h3>
        <p>Valutazione perimetro NIS2/PA e invio del preallarme al CSIRT Italia entro 24 ore (art. 25 D.Lgs. 138/2024), denuncia alla Polizia Postale (art. 629 co. 3 o 615-ter c.p.) e avviso polizza cyber.</p>
      </div>
      <div class="cy-step-card s3">
        <span class="cy-step-time">ORE 24 - 72</span>
        <h3>Notifica Garante Privacy</h3>
        <p>Analisi giuridica del rischio sui dati personali, invio della notifica al Garante entro 72 ore (art. 33 GDPR, anche per fasi) e preparazione dell'eventuale comunicazione agli interessati (art. 34).</p>
      </div>
      <div class="cy-step-card s4">
        <span class="cy-step-time">GIORNI 04 - 30</span>
        <h3>Relazione Finale e Tutele</h3>
        <p>Deposito relazione finale ACN entro 1 mese, chiusura registro interno violazioni, difesa in eventuali ispezioni, gestione contratti clienti/fornitori e azioni risarcitorie o di rivalsa.</p>
      </div>
    </div>
  </div>
</section>

<section class="cy-section" id="scenari-operativi">
  <div class="cy-container">
    <span class="cy-sec-label">Casistica Operativa e Protocolli di Difesa</span>
    <h2 class="cy-sec-title">110 Scenari Operativi e Protocolli Pratici</h2>
    <p class="cy-sec-sub">Cerca il problema esatto che stai affrontando: ogni scheda analizza un caso-tipo frequente su norme italiane ed europee vigenti, con mosse immediate, prove digitali da conservare, errori da evitare e FAQ. Per i casi reali gia' definiti dallo Studio consulta invece la pagina <a href="/casi-risolti.html">Casi Risolti</a>.</p>
    <div class="cy-explorer-controls">
      <div class="cy-search-wrap">
        <svg class="cy-search-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
        <input type="search" id="cy-scenario-search" class="cy-search-input" placeholder="Cerca: es. ransomware, 72 ore, phishing, SIM swap, crypto, SPID, NIS2, 615-ter, deepfake..." aria-label="Cerca tra i 110 scenari operativi">
      </div>
      <div class="cy-filter-pills" role="group" aria-label="Filtra per categoria">{filter_pills}</div>
    </div>
    <div class="cy-count-line" id="cy-scenario-count">Archivio completo: 110 protocolli operativi verificati</div>
    <div class="cy-scenarios-grid">
      {''.join(scenario_cards)}
    </div>
    <div style="text-align:center;margin-top:2rem;display:flex;justify-content:center;gap:1rem;flex-wrap:wrap;">
      <button type="button" id="cy-show-all" class="cy-btn-cyber" style="cursor:pointer;">Mostra tutti i 110 protocolli in questa pagina</button>
      <a href="/cybersicurezza/scenari/index.html" class="cy-btn-primary">Apri l'Indice Completo dei 110 Protocolli</a>
      <a href="/cybersicurezza/guide/index.html" class="cy-btn-cyber">Apri le 18 Guide Legali Operative</a>
    </div>
  </div>
</section>

<section class="cy-section cy-section-alt">
  <div class="cy-container">
    <span class="cy-sec-label">Standard Internazionale, Diritto Italiano</span>
    <h2 class="cy-sec-title">Perche' un approccio integrato supera i modelli standard</h2>
    <p class="cy-sec-sub">Abbiamo studiato le metodologie dei principali dipartimenti statunitensi di Incident Response e Data Privacy e le abbiamo potenziate per la realta' processuale e normativa italiana ed europea.</p>
    <div class="cy-bench-grid">
      <div class="cy-bench-card">
        <h3>Breach Coaching + Difesa Penale Vera</h3>
        <p>Molti consulenti privacy si fermano ai moduli cartacei. Noi uniamo compliance GDPR/NIS2 alla difesa penale sul campo davanti a Procura, Polizia Postale e Tribunale del Riesame.</p>
      </div>
      <div class="cy-bench-card">
        <h3>Imprese, CdA ma anche Privati</h3>
        <p>Oltre alla governance per aziende, DPO e consigli di amministrazione, tuteliamo concretamente privati e professionisti contro phishing, SIM swap, deepfake, revenge porn e furti d'identita'.</p>
      </div>
      <div class="cy-bench-card">
        <h3>Solo Norme Vigenti Verificate</h3>
        <p>Ogni protocollo integra le riforme recenti: Direttiva NIS2 (D.Lgs. 138/2024), Legge Cybersicurezza 90/2024 (estorsione informatica e art. 24-bis 231), PSD2 e Regolamento Europeo AI Act.</p>
      </div>
    </div>
  </div>
</section>

<section class="cy-section" id="faq">
  <div class="cy-container-narrow">
    <span class="cy-sec-label">Domande Frequenti</span>
    <h2 class="cy-sec-title">Risposte rapide su Cybersicurezza e Dati</h2>
    <div class="cy-faq-list">{faq_html}</div>
  </div>
</section>

<section class="cy-section">
  <div class="cy-container">
    <div class="cy-cta-banner">
      <span class="cy-sec-label">Consulenza Riservata in Studio o da Remoto</span>
      <h2>Hai un'emergenza informatica o devi adeguare la tua azienda?</h2>
      <p>Prima consulenza legale dedicata (in studio a Napoli, Via Toledo 205, oppure in videochiamata in tutta Italia) con analisi immediata del rischio, delle scadenze e della strategia difensiva.</p>
      <div class="cy-cta-row" style="justify-content:center;margin-bottom:0;">
        <a href="/consulenza.html?area=cybersicurezza" class="cy-btn-primary">Richiedi Consulenza Adesso</a>
        <a href="/prenota.html" class="cy-btn-cyber">Prenota Appuntamento</a>
      </div>
    </div>
  </div>
</section>

{footer_it()}
{WA_FLOAT}
<script src="/js/cyber-wow.js?v=1" defer></script>
</body>
</html>"""

    out = ROOT / "cybersicurezza.html"
    out.write_text(head_common(
        "Avvocato Cybersicurezza, GDPR, NIS2 e Reati Informatici | Studio Iaccarino",
        "Studio Legale specializzato in cybersicurezza e protezione dati in tutta Italia: data breach 72 ore GDPR, ransomware (L. 90/2024), NIS2 e ACN (D.Lgs. 138/2024), phishing bancario ABF, Modello 231 e AI Act. 110 protocolli operativi e 18 guide legali.",
        canonical, ld_blocks, lang="it", locale="it_IT", include_hreflang=True
    ) + "\n" + body, encoding="utf-8")


def build_pilastri():
    out_dir = ROOT / "cybersicurezza"
    out_dir.mkdir(parents=True, exist_ok=True)
    for p in PILASTRI:
        canonical = f"{BASE_URL}/cybersicurezza/{p['slug']}.html"
        correlati = [s for s in SCENARI if s["pilastro"] == p["slug"]]
        if len(correlati) < 6:
            extra = [s for s in SCENARI if s["cat"] == p["cat_scenari"] and s not in correlati]
            correlati.extend(extra[:6 - len(correlati)])
        ld_blocks = [
            {
                "@context": "https://schema.org",
                "@type": "LegalService",
                "name": f"Studio Legale Iaccarino - {p['titolo']}",
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
                    {"@type": "ListItem", "position": 2, "name": "Cybersicurezza", "item": f"{BASE_URL}/cybersicurezza.html"},
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
        norme_tags = "".join(f'<span class="cy-tag">{esc(n)}</span>' for n in p["norme"])
        faq_html = "".join(f'<details class="cy-faq-item"><summary>{esc(q)}</summary><p>{esc(a)}</p></details>' for q, a in p["faq"])
        corr_html = "".join(
            f'<a href="/cybersicurezza/scenari/{s["slug"]}.html" class="cy-scenario-card"><div><div class="cy-sc-top"><span class="cy-sc-code">{s["cod"]}</span><span class="cy-sc-cat">{esc(s["cat_lbl"])}</span></div><h3>{esc(s["titolo"])}</h3><p>{esc(s["desc"])}</p></div><div class="cy-sc-foot"><span>{esc(s["norme"][0])}</span><span>Apri protocollo &rarr;</span></div></a>'
            for s in correlati[:9]
        )
        altri_pilastri = "".join(
            f'<li><a href="/cybersicurezza/{x["slug"]}.html">{esc(x["titolo"])}</a></li>'
            for x in PILASTRI if x["slug"] != p["slug"]
        )

        body = f"""<body class="cyber-page">
<div class="cy-progress" aria-hidden="true"></div>
{GTM_BODY}
{nav_it("cyber")}
{alert_bar_it()}

<header class="cy-hero" style="padding:4rem 1.5rem 3.2rem;">
  <div class="cy-container">
    <nav class="cy-breadcrumb" aria-label="Percorso">
      <a href="/">Home</a> <span>/</span> <a href="/cybersicurezza.html">Cybersicurezza</a> <span>/</span> <span>{esc(p['titolo'])}</span>
    </nav>
    <span class="cy-eyebrow">AREA PILASTRO {p['num']} | {esc(p['urgenza'])}</span>
    <h1 style="max-width:960px;">{esc(p['h1'])}</h1>
    <p class="cy-hero-lead" style="max-width:820px;">{esc(p['description'])}</p>
    <div class="cy-pillar-tags" style="margin-bottom:1.6rem;">{norme_tags}</div>
    <div class="cy-cta-row" style="margin-bottom:0;">
      <a href="/consulenza.html?area=cybersicurezza" class="cy-btn-primary">Richiedi Valutazione Legale</a>
      <a href="/cybersicurezza.html#scenari-operativi" class="cy-btn-cyber">Esplora i 110 Protocolli</a>
    </div>
  </div>
</header>

<main class="cy-section">
  <div class="cy-container cy-article-layout">
    <article class="cy-article-body">
      <h2>Quadro Giuridico e Strategia di Intervento</h2>
      {intro_html}
      <div class="cy-norma-box">
        <h3>Norme Vigenti di Riferimento</h3>
        <p style="margin:0;">{esc(', '.join(p['norme']))}. Ogni intervento dello Studio viene calibrato sul testo vigente delle norme italiane ed europee e sugli atti concreti della pratica.</p>
      </div>
      <h2>Come Interviene lo Studio: Fasi Operative</h2>
      <ul>{azioni_html}</ul>
      <h2>Prove Digitali e Documenti da Preparare Subito</h2>
      <ul>{prove_html}</ul>
      <h2>Domande Frequenti</h2>
      <div class="cy-faq-list">{faq_html}</div>
      <div class="cy-disclaimer">
        Nota informativa: i contenuti di questa pagina hanno finalita' informativa generale sulle norme vigenti e sui protocolli operativi dello Studio Legale Avv. Francesco Iaccarino (Napoli, Via Toledo 205). Ogni vicenda concreta va esaminata sui propri atti e documenti specifici senza garanzie automatiche di esito.
      </div>
    </article>
    <aside class="cy-sidebar-box">
      <div class="cy-side-card">
        <h3>Urgenza su questo tema?</h3>
        <p>Parla direttamente con lo Studio Legale per bloccare i rischi immediati, rispettare i termini di legge e proteggere le prove digitali.</p>
        <a href="/consulenza.html?area=cybersicurezza" class="cy-btn-primary" style="width:100%;justify-content:center;margin-bottom:.65rem;">Richiedi Consulenza</a>
        <a href="tel:+393335684659" class="cy-btn-cyber" style="width:100%;justify-content:center;">Chiama +39 333 568 4659</a>
      </div>
      <div class="cy-side-card">
        <h3>Altre Aree Cybersicurezza</h3>
        <ul style="padding-left:1.1rem;margin:0;font-size:.9rem;line-height:1.75;">{altri_pilastri}</ul>
      </div>
    </aside>
  </div>
</main>

<section class="cy-section cy-section-alt">
  <div class="cy-container">
    <span class="cy-sec-label">Protocolli Correlati</span>
    <h2 class="cy-sec-title">Scenari Operativi Collegati a Questa Area</h2>
    <div class="cy-scenarios-grid">{corr_html}</div>
  </div>
</section>

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
    out_dir = ROOT / "cybersicurezza" / "scenari"
    out_dir.mkdir(parents=True, exist_ok=True)

    # 1. Pagina singola per ciascuno dei 70 scenari operativi
    for idx, s in enumerate(SCENARI):
        canonical = f"{BASE_URL}/cybersicurezza/scenari/{s['slug']}.html"
        pil = PILASTRI_BY_SLUG[s["pilastro"]]
        same_cat = [x for x in SCENARI if x["cat"] == s["cat"] and x["slug"] != s["slug"]][:6]

        faqs = [
            (f"Quali norme si applicano allo scenario: {s['titolo']}?", f"Il quadro normativo di riferimento comprende {', '.join(s['norme'])}. L'applicazione concreta dipende dalla ricostruzione tecnica dell'incidente, dalla qualifica dei soggetti coinvolti e dalla documentazione disponibile."),
            ("Quali sono le prime mosse da compiere appena emerge il problema?", f"{s['protocollo'][0]} Subito dopo occorre procedere con l'analisi legale mirata: {s['protocollo'][1]}"),
            ("Quali prove digitali e documenti conviene conservare subito?", f"E' essenziale preservare integralmente senza alterazioni: {', '.join(s['prove'])}. Una conservazione corretta fin dalle prime ore e' decisiva in sede amministrativa, civile o penale."),
            ("Qual e' l'errore piu' grave da evitare in questa situazione?", f"Tra gli errori piu' frequenti che compromettono la difesa rientrano: {s['errori'][0]}; inoltre va evitato di {s['errori'][1][0].lower() + s['errori'][1][1:]}.")
        ]

        ld_blocks = [
            {
                "@context": "https://schema.org",
                "@type": "Article",
                "headline": s["titolo"],
                "description": s["desc"],
                "author": {"@type": "Person", "name": "Avv. Francesco Iaccarino"},
                "publisher": {"@type": "Organization", "name": "Studio Legale Avv. Francesco Iaccarino", "url": BASE_URL},
                "datePublished": TODAY,
                "dateModified": TODAY,
                "mainEntityOfPage": canonical,
                "keywords": ", ".join(s["keywords"])
            },
            {
                "@context": "https://schema.org",
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{BASE_URL}/"},
                    {"@type": "ListItem", "position": 2, "name": "Cybersicurezza", "item": f"{BASE_URL}/cybersicurezza.html"},
                    {"@type": "ListItem", "position": 3, "name": "110 Protocolli Operativi", "item": f"{BASE_URL}/cybersicurezza/scenari/index.html"},
                    {"@type": "ListItem", "position": 4, "name": s["cod"], "item": canonical}
                ]
            },
            {
                "@context": "https://schema.org",
                "@type": "FAQPage",
                "mainEntity": [
                    {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
                    for q, a in faqs
                ]
            }
        ]

        norme_tags = "".join(f'<span class="cy-tag">{esc(n)}</span>' for n in s["norme"])
        kw_tags = "".join(f'<span class="cy-tag">{esc(k)}</span>' for k in s["keywords"])
        proto_li = "".join(f"<li><strong>Fase {i+1}:</strong> {esc(step)}</li>" for i, step in enumerate(s["protocollo"]))
        prove_li = "".join(f"<li>{esc(pr)}</li>" for pr in s["prove"])
        err_li = "".join(f"<li>{esc(er)}</li>" for er in s["errori"])
        faq_html = "".join(f'<details class="cy-faq-item"><summary>{esc(q)}</summary><p>{esc(a)}</p></details>' for q, a in faqs)
        corr_html = "".join(
            f'<a href="/cybersicurezza/scenari/{c["slug"]}.html" class="cy-scenario-card"><div><div class="cy-sc-top"><span class="cy-sc-code">{c["cod"]}</span><span class="cy-sc-cat">{esc(c["cat_lbl"])}</span></div><h3>{esc(c["titolo"])}</h3><p>{esc(c["desc"])}</p></div><div class="cy-sc-foot"><span>{esc(c["norme"][0])}</span><span>Apri &rarr;</span></div></a>'
            for c in same_cat
        )

        prev_link = f'<a href="/cybersicurezza/scenari/{SCENARI[idx-1]["slug"]}.html" class="cy-btn-cyber">&larr; {SCENARI[idx-1]["cod"]}</a>' if idx > 0 else ""
        next_link = f'<a href="/cybersicurezza/scenari/{SCENARI[idx+1]["slug"]}.html" class="cy-btn-cyber">{SCENARI[idx+1]["cod"]} &rarr;</a>' if idx < len(SCENARI) - 1 else ""

        body = f"""<body class="cyber-page">
<div class="cy-progress" aria-hidden="true"></div>
{GTM_BODY}
{nav_it("scenari")}
{alert_bar_it()}

<header class="cy-hero" style="padding:3.8rem 1.5rem 3rem;">
  <div class="cy-container">
    <nav class="cy-breadcrumb" aria-label="Percorso">
      <a href="/">Home</a> <span>/</span> <a href="/cybersicurezza.html">Cybersicurezza</a> <span>/</span> <a href="/cybersicurezza/scenari/index.html">110 Protocolli</a> <span>/</span> <span>{s['cod']}</span>
    </nav>
    <span class="cy-eyebrow">PROTOCOLLO OPERATIVO {s['cod']} | {esc(s['cat_lbl'])}</span>
    <h1 style="max-width:960px;font-size:clamp(2rem,4.4vw,3.35rem);">{esc(s['titolo'])}</h1>
    <p class="cy-hero-lead" style="max-width:820px;">{esc(s['desc'])}</p>
    <div class="cy-pillar-tags">{norme_tags}</div>
  </div>
</header>

<main class="cy-section">
  <div class="cy-container cy-article-layout">
    <article class="cy-article-body">
      <h2>1. Lo scenario operativo ricorrente</h2>
      <p>{esc(s['scenario'])}</p>
      <p><strong>Esposizione giuridica e rischi concreti:</strong> {esc(s['rischio'])} In contesti digitali ad alta velocita' la differenza tra un danno contenuto e una responsabilita' grave si gioca sulla qualita' delle decisioni prese nelle prime ore e sulla tenuta probatoria delle verifiche tecniche.</p>

      <div class="cy-norma-box">
        <h3>2. Quadro normativo vigente applicabile</h3>
        <p style="margin:0;">Norme di riferimento: <strong>{esc(', '.join(s['norme']))}</strong>. Questa scheda rientra nell'area specialistica <a href="/cybersicurezza/{pil['slug']}.html">{esc(pil['titolo'])}</a>, dove sono illustrati in modo sistematico i presidi legali, le autorita' competenti e le strategie difensive dello Studio.</p>
      </div>

      <h2>3. Protocollo di intervento passo dopo passo</h2>
      <p>Quando si verifica una vicenda riconducibile a questo scenario, il metodo di lavoro dello Studio Legale Avv. Francesco Iaccarino segue una sequenza ordinata per mettere in sicurezza sia il profilo tecnico sia quello processuale e regolatorio:</p>
      <ul>{proto_li}</ul>

      <h2>4. Prove digitali e documenti da preservare subito</h2>
      <p>Nel contenzioso informatico, davanti al Garante Privacy, ad ACN, all'ABF o all'Autorita' Giudiziaria, le affermazioni generiche non bastano. Prima di modificare configurazioni o inviare comunicazioni informali occorre raccogliere e mettere al sicuro i seguenti elementi:</p>
      <ul>{prove_li}</ul>

      <h2>5. Errori critici da evitare</h2>
      <p>Nella prassi forense gran parte delle sanzioni o delle sconfitte nasce da reazioni affrettate nelle prime ore dopo la scoperta dell'evento. In particolare occorre evitare:</p>
      <ul>{err_li}</ul>

      <h2>6. Domande frequenti su questo scenario</h2>
      <div class="cy-faq-list">{faq_html}</div>

      <div style="margin-top:1.8rem;">
        <span class="cy-sec-label" style="margin-bottom:.5rem;">Ricerche correlate coperte da questo protocollo</span>
        <div class="cy-pillar-tags">{kw_tags}</div>
      </div>

      <div class="cy-disclaimer">
        Trasparenza deontologica: questa scheda descrive uno scenario operativo tipo e un protocollo di difesa basato sulle norme vigenti italiane ed europee; non rappresenta la cronaca di un singolo processo reale ne' una promessa di risultato. I casi reali definiti dallo Studio sono raccolti separatamente nella pagina <a href="/casi-risolti.html">Casi Risolti</a>. Ogni situazione concreta va esaminata sui propri atti e documenti presso lo Studio Legale Avv. Francesco Iaccarino, Napoli, Via Toledo 205.
      </div>

      <div style="display:flex;justify-content:space-between;align-items:center;gap:1rem;flex-wrap:wrap;margin-top:2rem;">
        {prev_link}
        <a href="/cybersicurezza/scenari/index.html" class="cy-btn-primary">Tutti i 110 Protocolli</a>
        {next_link}
      </div>
    </article>

    <aside class="cy-sidebar-box">
      <div class="cy-side-card">
        <h3>Ti trovi in questa situazione?</h3>
        <p>Richiedi subito una valutazione legale riservata sui tuoi atti, log o comunicazioni. Assistenza a Napoli e da remoto in tutta Italia.</p>
        <a href="/consulenza.html?area=cybersicurezza" class="cy-btn-primary" style="width:100%;justify-content:center;margin-bottom:.65rem;">Richiedi Consulenza</a>
        <a href="https://wa.me/393335684659?text=Richiedo%20assistenza%20su%20protocollo%20{s['cod']}" target="_blank" rel="noopener noreferrer" class="cy-btn-cyber" style="width:100%;justify-content:center;">WhatsApp Urgenze</a>
      </div>
      <div class="cy-side-card">
        <h3>Area Pilastro di Riferimento</h3>
        <p>{esc(pil['sintesi'])}</p>
        <a href="/cybersicurezza/{pil['slug']}.html" class="cy-link-more">Vai a {esc(pil['titolo'])} &rarr;</a>
      </div>
    </aside>
  </div>
</main>

<section class="cy-section cy-section-alt">
  <div class="cy-container">
    <span class="cy-sec-label">Approfondisci la stessa area</span>
    <h2 class="cy-sec-title">Altri Protocolli in {esc(s['cat_lbl'])}</h2>
    <div class="cy-scenarios-grid">{corr_html}</div>
  </div>
</section>

{footer_it()}
{WA_FLOAT}
<script src="/js/cyber-wow.js?v=1" defer></script>
</body>
</html>"""

        (out_dir / f"{s['slug']}.html").write_text(
            head_common(f"{s['seo_title']} | Studio Iaccarino", s["desc"], canonical, ld_blocks) + "\n" + body,
            encoding="utf-8"
        )

    # 2. Pagina indice completa cybersicurezza/scenari/index.html
    idx_canonical = f"{BASE_URL}/cybersicurezza/scenari/index.html"
    filter_pills = "".join(
        f'<button type="button" class="cy-filter-pill {"active" if k=="tutti" else ""}" data-cat="{k}">{esc(lbl)}</button>'
        for k, lbl in CATEGORIE_SCENARI
    )
    all_cards = []
    for s in SCENARI:
        blob = " ".join([s["cod"], s["titolo"], s["desc"], s["cat_lbl"], " ".join(s["keywords"]), " ".join(s["norme"])])
        all_cards.append(f"""<a href="/cybersicurezza/scenari/{s['slug']}.html" class="cy-scenario-card" data-cat="{s['cat']}" data-search="{esc(blob)}">
  <div>
    <div class="cy-sc-top"><span class="cy-sc-code">{s['cod']}</span><span class="cy-sc-cat">{esc(s['cat_lbl'])}</span></div>
    <h3>{esc(s['titolo'])}</h3>
    <p>{esc(s['desc'])}</p>
  </div>
  <div class="cy-sc-foot"><span>{esc(s['norme'][0])}</span><span>Apri protocollo &rarr;</span></div>
</a>""")

    idx_ld = [
        {
            "@context": "https://schema.org",
            "@type": "ItemList",
            "name": "110 Protocolli Operativi di Cybersicurezza e Protezione Dati",
            "numberOfItems": len(SCENARI),
            "itemListElement": [
                {"@type": "ListItem", "position": i + 1, "name": s["titolo"], "url": f"{BASE_URL}/cybersicurezza/scenari/{s['slug']}.html"}
                for i, s in enumerate(SCENARI)
            ]
        },
        {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{BASE_URL}/"},
                {"@type": "ListItem", "position": 2, "name": "Cybersicurezza", "item": f"{BASE_URL}/cybersicurezza.html"},
                {"@type": "ListItem", "position": 3, "name": "110 Protocolli Operativi", "item": idx_canonical}
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
      <a href="/">Home</a> <span>/</span> <a href="/cybersicurezza.html">Cybersicurezza</a> <span>/</span> <span>110 Protocolli Operativi</span>
    </nav>
    <span class="cy-eyebrow">ARCHIVIO COMPLETO | 7 CATEGORIE | 110 SCHEDE</span>
    <h1>110 Scenari Operativi e Protocolli di <em>Difesa Cyber</em></h1>
    <p class="cy-hero-lead">Indice integrale delle 110 casistiche operative in materia di data breach, GDPR, ransomware, Direttiva NIS2, phishing e banche, crypto, SPID, penale informatico, ex dipendenti, deepfake, reputazione online, contratti IT, AI Act e Modello 231.</p>
  </div>
</header>
<main class="cy-section">
  <div class="cy-container">
    <div class="cy-explorer-controls">
      <div class="cy-search-wrap">
        <svg class="cy-search-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
        <input type="search" id="cy-scenario-search" class="cy-search-input" placeholder="Filtra per parola chiave, reato, articolo o problema..." aria-label="Cerca tra i 110 protocolli">
      </div>
      <div class="cy-filter-pills">{filter_pills}</div>
    </div>
    <div class="cy-count-line" id="cy-scenario-count">Archivio completo: 110 protocolli operativi</div>
    <div class="cy-scenarios-grid">{''.join(all_cards)}</div>
  </div>
</main>
{footer_it()}
{WA_FLOAT}
<script src="/js/cyber-wow.js?v=1" defer></script>
</body>
</html>"""
    (out_dir / "index.html").write_text(
        head_common("110 Protocolli Operativi Cybersicurezza, GDPR e NIS2 | Studio Iaccarino",
                    "Archivio completo di 110 scenari operativi e protocolli di difesa legale su data breach, ransomware, NIS2, phishing bancario, crypto, SPID, reati informatici, deepfake, lavoro, cloud e AI Act.",
                    idx_canonical, idx_ld) + "\n" + idx_body,
        encoding="utf-8"
    )


def build_guide():
    out_dir = ROOT / "cybersicurezza" / "guide"
    out_dir.mkdir(parents=True, exist_ok=True)

    for idx, g in enumerate(GUIDE_CYBER):
        canonical = f"{BASE_URL}/cybersicurezza/guide/{g['slug']}.html"
        pil = PILASTRI_BY_SLUG[g["pilastro"]]
        ld_blocks = [
            {
                "@context": "https://schema.org",
                "@type": "Article",
                "headline": g["titolo"],
                "description": g["desc"],
                "author": {"@type": "Person", "name": "Avv. Francesco Iaccarino"},
                "publisher": {"@type": "Organization", "name": "Studio Legale Avv. Francesco Iaccarino", "url": BASE_URL},
                "datePublished": TODAY,
                "dateModified": TODAY,
                "mainEntityOfPage": canonical
            },
            {
                "@context": "https://schema.org",
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{BASE_URL}/"},
                    {"@type": "ListItem", "position": 2, "name": "Cybersicurezza", "item": f"{BASE_URL}/cybersicurezza.html"},
                    {"@type": "ListItem", "position": 3, "name": "Guide Operative", "item": f"{BASE_URL}/cybersicurezza/guide/index.html"},
                    {"@type": "ListItem", "position": 4, "name": g["cod"], "item": canonical}
                ]
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
        sez_html = "".join(f"<h2>{esc(st)}</h2><p>{esc(sp)}</p>" for st, sp in g["sezioni"])
        chk_html = "".join(f"<li>{esc(c)}</li>" for c in g["checklist"])
        faq_html = "".join(f'<details class="cy-faq-item"><summary>{esc(q)}</summary><p>{esc(a)}</p></details>' for q, a in g["faqs"])
        altre_guide = "".join(
            f'<li><a href="/cybersicurezza/guide/{x["slug"]}.html">{esc(x["titolo"])}</a></li>'
            for x in GUIDE_CYBER if x["slug"] != g["slug"]
        )
        prev_link = f'<a href="/cybersicurezza/guide/{GUIDE_CYBER[idx-1]["slug"]}.html" class="cy-btn-cyber">&larr; {GUIDE_CYBER[idx-1]["cod"]}</a>' if idx > 0 else ""
        next_link = f'<a href="/cybersicurezza/guide/{GUIDE_CYBER[idx+1]["slug"]}.html" class="cy-btn-cyber">{GUIDE_CYBER[idx+1]["cod"]} &rarr;</a>' if idx < len(GUIDE_CYBER) - 1 else ""

        body = f"""<body class="cyber-page">
<div class="cy-progress" aria-hidden="true"></div>
{GTM_BODY}
{nav_it("guide")}
{alert_bar_it()}
<header class="cy-hero" style="padding:3.8rem 1.5rem 3rem;">
  <div class="cy-container">
    <nav class="cy-breadcrumb" aria-label="Percorso">
      <a href="/">Home</a> <span>/</span> <a href="/cybersicurezza.html">Cybersicurezza</a> <span>/</span> <a href="/cybersicurezza/guide/index.html">Guide Operative</a> <span>/</span> <span>{g['cod']}</span>
    </nav>
    <span class="cy-eyebrow">GUIDA LEGALE OPERATIVA {g['cod']} | STUDIO LEGALE IACCARINO</span>
    <h1 style="max-width:960px;font-size:clamp(1.9rem,4vw,3.15rem);">{esc(g['titolo'])}</h1>
    <p class="cy-hero-lead" style="max-width:820px;">{esc(g['desc'])}</p>
    <div class="cy-pillar-tags">{norme_tags}</div>
  </div>
</header>
<main class="cy-section">
  <div class="cy-container cy-article-layout">
    <article class="cy-article-body">
      <p>{esc(g['intro'])}</p>
      <div class="cy-norma-box">
        <h3>Norme Vigenti di Riferimento</h3>
        <p style="margin:0;"><strong>{esc(', '.join(g['norme']))}</strong>. Area specialistica collegata: <a href="/cybersicurezza/{pil['slug']}.html">{esc(pil['titolo'])}</a>.</p>
      </div>
      {sez_html}
      <h2>Checklist Operativa Immediata</h2>
      <ul>{chk_html}</ul>
      <h2>Domande Frequenti</h2>
      <div class="cy-faq-list">{faq_html}</div>
      <div class="cy-disclaimer">
        Nota informativa: guida operativa redatta sulle norme vigenti dallo Studio Legale Avv. Francesco Iaccarino (Palazzo Barbaja, Via Toledo 205, Napoli). Ogni caso concreto va esaminato sui propri atti e documenti specifici.
      </div>
      <div style="display:flex;justify-content:space-between;align-items:center;gap:1rem;flex-wrap:wrap;margin-top:2rem;">
        {prev_link}
        <a href="/cybersicurezza/guide/index.html" class="cy-btn-primary">Tutte le 18 Guide Operative</a>
        {next_link}
      </div>
    </article>
    <aside class="cy-sidebar-box">
      <div class="cy-side-card">
        <h3>Assistenza su questa procedura?</h3>
        <p>Richiedi una consulenza riservata in studio a Napoli o da remoto in tutta Italia per gestire subito adempimenti, difese o urgenze.</p>
        <a href="/consulenza.html?area=cybersicurezza" class="cy-btn-primary" style="width:100%;justify-content:center;margin-bottom:.65rem;">Richiedi Consulenza</a>
        <a href="tel:+393335684659" class="cy-btn-cyber" style="width:100%;justify-content:center;">Chiama +39 333 568 4659</a>
      </div>
      <div class="cy-side-card">
        <h3>Altre Guide Cyber</h3>
        <ul style="padding-left:1.1rem;margin:0;font-size:.86rem;line-height:1.7;">{altre_guide}</ul>
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
            head_common(g["seo_title"], g["desc"], canonical, ld_blocks) + "\n" + body,
            encoding="utf-8"
        )

    idx_canonical = f"{BASE_URL}/cybersicurezza/guide/index.html"
    cards = "".join(
        f'<a href="/cybersicurezza/guide/{g["slug"]}.html" class="cy-scenario-card"><div><div class="cy-sc-top"><span class="cy-sc-code">{g["cod"]}</span><span class="cy-sc-cat">Guida Operativa</span></div><h3>{esc(g["titolo"])}</h3><p>{esc(g["desc"])}</p></div><div class="cy-sc-foot"><span>{esc(g["norme"][0])}</span><span>Leggi guida &rarr;</span></div></a>'
        for g in GUIDE_CYBER
    )
    idx_ld = [
        {
            "@context": "https://schema.org",
            "@type": "ItemList",
            "name": "18 Guide Operative di Cybersicurezza, GDPR, NIS2 e AI Act",
            "numberOfItems": len(GUIDE_CYBER),
            "itemListElement": [
                {"@type": "ListItem", "position": i + 1, "name": g["titolo"], "url": f"{BASE_URL}/cybersicurezza/guide/{g['slug']}.html"}
                for i, g in enumerate(GUIDE_CYBER)
            ]
        },
        {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{BASE_URL}/"},
                {"@type": "ListItem", "position": 2, "name": "Cybersicurezza", "item": f"{BASE_URL}/cybersicurezza.html"},
                {"@type": "ListItem", "position": 3, "name": "18 Guide Operative", "item": idx_canonical}
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
      <a href="/">Home</a> <span>/</span> <a href="/cybersicurezza.html">Cybersicurezza</a> <span>/</span> <span>18 Guide Operative</span>
    </nav>
    <span class="cy-eyebrow">MANUALISTICA OPERATIVA | CHECKLIST LEGALI</span>
    <h1>18 Guide Operative di <em>Cybersicurezza</em> e Protezione Dati</h1>
    <p class="cy-hero-lead">Procedure passo passo, scadenze di legge e checklist forensi per imprese, DPO, amministratori e privati su Garante Privacy 72h, ACN 24h NIS2, Polizia Postale, ABF, Modello 231, AI Act, videosorveglianza ed e-commerce.</p>
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
        head_common("18 Guide Operative Cybersicurezza, GDPR, NIS2 e AI Act | Studio Iaccarino",
                    "Guide pratiche e checklist legali su data breach 72 ore, pre-notifica ACN 24 ore NIS2, querela Polizia Postale, prove digitali, ABF phishing, Modello 231 e AI Act.",
                    idx_canonical, idx_ld) + "\n" + idx_body,
        encoding="utf-8"
    )


def build_multilingua():
    for code, data in LINGUE_ESTERE.items():
        lang_dir = ROOT / code
        lang_dir.mkdir(parents=True, exist_ok=True)
        canonical = f"{BASE_URL}/{code}/cybersicurezza.html"
        ld_blocks = [
            {
                "@context": "https://schema.org",
                "@type": "LegalService",
                "name": f"Studio Legale Avv. Francesco Iaccarino - {data['nav_cyber']}",
                "url": canonical,
                "description": data["desc"],
                "telephone": "+393335684659",
                "areaServed": {"@type": "Country", "name": "Italy"}
            }
        ]
        cards = []
        for idx, (num, pt, pd) in enumerate(data["pillars"]):
            slug = PILASTRI[idx]["slug"]
            cards.append(f"""<a href="/cybersicurezza/{slug}.html" class="cy-pillar-card">
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
    <a href="/{code}/" class="cy-logo">Studio Legale Iaccarino <span class="cy-logo-badge">Cyber Law</span></a>
    <div class="cy-nav-links">
      <a href="/{code}/">{esc(data['nav_home'])}</a>
      <a href="/{code}/penale.html">{esc(data['nav_penale'])}</a>
      <a href="/{code}/civile.html">{esc(data['nav_civile'])}</a>
      <a href="/{code}/tributario.html">{esc(data['nav_trib'])}</a>
      <a href="/{code}/immigrazione.html">{esc(data['nav_imm'])}</a>
      <a href="/{code}/cybersicurezza.html" class="active">{esc(data['nav_cyber'])}</a>
      <a href="/consulenza.html?area=cybersicurezza" class="cy-nav-cta">{esc(data['nav_cta'])}</a>
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
      <a href="https://wa.me/393335684659?text=CYBER%20URGENT" target="_blank" rel="noopener noreferrer" class="cy-btn-urgent">{esc(data['cta_urgent'])}</a>
    </div>
  </div>
</div>
<header class="cy-hero">
  <div class="cy-container">
    <span class="cy-eyebrow">{esc(data['eyebrow'])}</span>
    <h1>{data['h1']}</h1>
    <p class="cy-hero-lead">{esc(data['lead'])}</p>
    <div class="cy-cta-row">
      <a href="/consulenza.html?area=cybersicurezza" class="cy-btn-primary">{esc(data['cta_book'])}</a>
      <a href="/cybersicurezza.html" class="cy-btn-cyber">{esc(data['cta_it'])}</a>
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
        (lang_dir / "cybersicurezza.html").write_text(head + "\n" + body, encoding="utf-8")


def integrate_existing_pages():
    # 1. Aggiorna index.html (JSON-LD + nav + sezione aree)
    idx_path = ROOT / "index.html"
    txt = idx_path.read_text(encoding="utf-8")
    if "cybersicurezza.html" not in txt:
        txt = txt.replace(
            '"knowsAbout": ["Diritto Penale","Diritto Civile","Diritto del Lavoro","Diritto Tributario","Diritto dell\'Immigrazione"]',
            '"knowsAbout": ["Diritto Penale","Diritto Civile","Diritto del Lavoro","Diritto Tributario","Diritto dell\'Immigrazione","Cybersicurezza","Protezione Dati GDPR","Direttiva NIS2","Reati Informatici"]'
        )
        txt = txt.replace(
            '{ "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Diritto dell\'Immigrazione e Cittadinanza", "url": "https://studiolegalefrancescoiaccarino.com/immigrazione.html" } }',
            '{ "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Diritto dell\'Immigrazione e Cittadinanza", "url": "https://studiolegalefrancescoiaccarino.com/immigrazione.html" } },\n          { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Cybersicurezza, GDPR, NIS2 e Reati Informatici", "url": "https://studiolegalefrancescoiaccarino.com/cybersicurezza.html" } }'
        )
        txt = txt.replace(
            '"name": ["Diritto Penale", "Diritto Civile", "Diritto Tributario", "Immigrazione", "Guide Legali", "Prenota Consulenza", "Richiedi Consulenza"]',
            '"name": ["Diritto Penale", "Diritto Civile", "Diritto Tributario", "Immigrazione", "Cybersicurezza", "Guide Legali", "Prenota Consulenza", "Richiedi Consulenza"]'
        )
        txt = txt.replace(
            '"https://studiolegalefrancescoiaccarino.com/immigrazione.html",',
            '"https://studiolegalefrancescoiaccarino.com/immigrazione.html",\n        "https://studiolegalefrancescoiaccarino.com/cybersicurezza.html",'
        )
        txt = txt.replace(
            '<a href="/immigrazione.html">Diritto dell\'Immigrazione</a>',
            '<a href="/immigrazione.html">Diritto dell\'Immigrazione</a>\n          <a href="/cybersicurezza.html">Cybersicurezza e Protezione Dati</a>'
        )
        txt = txt.replace(
            '<p><strong>Diritto dell\'Immigrazione:</strong> permessi di soggiorno, cittadinanza italiana, ricongiungimento familiare e ricorsi contro dinieghi ed espulsioni. <a href="/immigrazione.html">Approfondisci Immigrazione</a>.</p>',
            '<p><strong>Diritto dell\'Immigrazione:</strong> permessi di soggiorno, cittadinanza italiana, ricongiungimento familiare e ricorsi contro dinieghi ed espulsioni. <a href="/immigrazione.html">Approfondisci Immigrazione</a>.</p>\n          <p><strong>Cybersicurezza e Protezione Dati:</strong> data breach 72 ore GDPR, ransomware ed estorsione informatica (L. 90/2024), adeguamento Direttiva NIS2 e ACN (D.Lgs. 138/2024), phishing bancario ABF, reati informatici, Modello 231 e AI Act, con 70 protocolli operativi. <a href="/cybersicurezza.html">Approfondisci Cybersicurezza</a>.</p>'
        )
        idx_path.write_text(txt, encoding="utf-8")

    # 2. Aggiorna nav e footer delle 4 pagine di area principali (IT)
    for area_file in ["penale.html", "civile.html", "tributario.html", "immigrazione.html"]:
        p = ROOT / area_file
        if not p.exists():
            continue
        t = p.read_text(encoding="utf-8")
        if "cybersicurezza.html" not in t:
            t = t.replace(
                '<a href="immigrazione.html" class="nav-back">Immigrazione</a>',
                '<a href="immigrazione.html" class="nav-back">Immigrazione</a>\n      <a href="cybersicurezza.html" class="nav-back">Cybersicurezza</a>'
            )
            t = t.replace(
                '<a href="immigrazione.html">Immigrazione</a>',
                '<a href="immigrazione.html">Immigrazione</a>\n    <a href="cybersicurezza.html">Cybersicurezza</a>'
            )
            p.write_text(t, encoding="utf-8")

    # 3. Aggiorna sitemap.xml (hub + 10 pilastri + indice scenari + indice guide)
    sm_path = ROOT / "sitemap.xml"
    sm = sm_path.read_text(encoding="utf-8")
    new_urls = [
        (f"{BASE_URL}/cybersicurezza.html", "weekly", "0.95"),
        (f"{BASE_URL}/cybersicurezza/scenari/index.html", "weekly", "0.90"),
        (f"{BASE_URL}/cybersicurezza/guide/index.html", "weekly", "0.90"),
    ] + [(f"{BASE_URL}/cybersicurezza/{p['slug']}.html", "weekly", "0.85") for p in PILASTRI]
    entries = []
    for u, freq, prio in new_urls:
        if u not in sm:
            entries.append(f"  <url>\n    <loc>{u}</loc>\n    <lastmod>{TODAY}</lastmod>\n    <changefreq>{freq}</changefreq>\n    <priority>{prio}</priority>\n  </url>")
    if entries:
        sm = sm.replace("</urlset>", "\n".join(entries) + "\n</urlset>")
        sm_path.write_text(sm, encoding="utf-8")

    # 4. Aggiorna sitemap-guide-casi.xml con tutti i 110 scenari operativi e le 18 guide
    sm2_path = ROOT / "sitemap-guide-casi.xml"
    if sm2_path.exists():
        sm2 = sm2_path.read_text(encoding="utf-8")
        sc_entries = []
        for s in SCENARI:
            u = f"{BASE_URL}/cybersicurezza/scenari/{s['slug']}.html"
            if u not in sm2:
                sc_entries.append(f"  <url>\n    <loc>{u}</loc>\n    <lastmod>{TODAY}</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>0.80</priority>\n  </url>")
        for g in GUIDE_CYBER:
            u = f"{BASE_URL}/cybersicurezza/guide/{g['slug']}.html"
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
            u = f"{BASE_URL}/{code}/cybersicurezza.html"
            if u not in sm3:
                lg_entries.append(f"  <url>\n    <loc>{u}</loc>\n    <lastmod>{TODAY}</lastmod>\n    <changefreq>weekly</changefreq>\n    <priority>0.85</priority>\n  </url>")
        if lg_entries:
            sm3 = sm3.replace("</urlset>", "\n".join(lg_entries) + "\n</urlset>")
            sm3_path.write_text(sm3, encoding="utf-8")


def validate_all():
    errors = []
    # 1. Controlla conteggio esatto
    assert len(PILASTRI) == 10, f"Pilastri={len(PILASTRI)}"
    assert len(SCENARI) == 110, f"Scenari={len(SCENARI)}"
    assert len(GUIDE_CYBER) == 18, f"Guide={len(GUIDE_CYBER)}"
    slugs = [s["slug"] for s in SCENARI]
    if len(set(slugs)) != 110:
        errors.append("Slug duplicati nei 110 scenari!")
    titles = [s["titolo"] for s in SCENARI]
    if len(set(titles)) != 110:
        errors.append("Titoli duplicati nei 110 scenari!")
    g_slugs = [g["slug"] for g in GUIDE_CYBER]
    if len(set(g_slugs)) != 18:
        errors.append("Slug duplicati nelle 18 guide!")

    # 2. Controlla che tutti i file esistano e non contengano link rotti o JSON-LD invalidi
    files_to_check = [
        ROOT / "cybersicurezza.html",
        ROOT / "cybersicurezza" / "scenari" / "index.html",
        ROOT / "cybersicurezza" / "guide" / "index.html",
    ] + [ROOT / "cybersicurezza" / f"{p['slug']}.html" for p in PILASTRI] \
      + [ROOT / "cybersicurezza" / "scenari" / f"{s['slug']}.html" for s in SCENARI] \
      + [ROOT / "cybersicurezza" / "guide" / f"{g['slug']}.html" for g in GUIDE_CYBER] \
      + [ROOT / code / "cybersicurezza.html" for code in LINGUE_ESTERE]

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
        for href in re.findall(r'href="(/cybersicurezza[^"#?]*)"', raw):
            target = ROOT / href.lstrip("/")
            if not target.exists():
                errors.append(f"Link interno rotto in {f.name}: {href}")
        if "«" in raw or "»" in raw:
            errors.append(f"Caporali trovati in {f.name}")

    print(f"FILE GENERATI E VERIFICATI: {len(files_to_check)}")
    print(f"PILASTRI: {len(PILASTRI)} | SCENARI: {len(SCENARI)} | GUIDE: {len(GUIDE_CYBER)} | LINGUE ESTERE: {len(LINGUE_ESTERE)}")
    if errors:
        print("ERRORI RILEVATI:")
        for e in errors[:20]:
            print(" -", e)
        sys.exit(1)
    else:
        print("VALIDAZIONE OK: 0 ERRORI, 0 LINK ROTTI, 0 JSON-LD INVALIDI, 0 DUPLICATI.")


if __name__ == "__main__":
    build_hub_it()
    build_pilastri()
    build_scenari()
    build_guide()
    build_multilingua()
    integrate_existing_pages()
    validate_all()
