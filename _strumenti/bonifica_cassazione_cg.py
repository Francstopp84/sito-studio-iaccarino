# -*- coding: utf-8 -*-
"""
Bonifica integrale del sito e dei sorgenti React:
rimuove OGNI riferimento a patrocinio in Corte di Cassazione, cassazionista,
ricorso per Cassazione e Corte di Giustizia (mantenendo intatti eventuali URL/href).
"""
import json
import re
from pathlib import Path

SRC = Path(r"D:\STUDIO LEGALE\MODELLI E FORMULARI\Nuovo sito internet\_SITO_DA_ZIP_20112026\src")
SITO = Path(r"D:\STUDIO LEGALE\MODELLI E FORMULARI\Nuovo sito internet\_SITO_GITHUB_PAGES\sito")


def clean_visible_text(s: str) -> str:
    # Prima sostituzioni di frasi complete piu' specifiche
    reps = [
        ("Tribunali d’Italia fino alla Corte di Cassazione.", "Tribunali e le Corti d’Appello di tutta Italia."),
        ("Tribunali d'Italia fino alla Corte di Cassazione.", "Tribunali e le Corti d'Appello di tutta Italia."),
        ("Corti di Giustizia Tributaria e Corte di Cassazione — nonché", "Tribunali, Corti d’Appello e Giudici Tributari di I e II grado — nonché"),
        ("di Giustizia Tributaria e Corte di Cassazione. Apra una scheda per", "Tribunali, Corti d’Appello e Giudici Tributari. Apra una scheda per"),
        ("fino al dibattimento, all’Appello e alla Corte di Cassazione.", "fino al dibattimento e alla Corte d’Appello."),
        ("Appello penale e ricorsi in Corte di Cassazione", "Appello penale e impugnazioni di merito"),
        ("orientamenti recenti della Corte di Cassazione e perizie tecniche.", "giurisprudenza aggiornata e perizie tecniche."),
        ("ogni Tribunale, Corte d’Appello, Corte di Giustizia Tributaria e Corte di Cassazione.", "ogni Tribunale, Corte d’Appello e giudice tributario di I e II grado."),
        ("dinanzi alla Corte di Giustizia Tributaria.", "dinanzi al giudice tributario competente."),
        ("Italian Supreme Court (Cassazione)", "Court of Appeal of Naples"),
        ("Contenzioso tributario e Cassazione", "Contenzioso tributario di I e II grado"),
        ("misure cautelari, processi, appelli, Cassazione", "misure cautelari, processi e appelli"),
        ("dibattimento, appello e ricorso per Cassazione", "dibattimento e giudizio di appello"),
        ("avvisi di garanzia, appelli e Cassazione", "avvisi di garanzia e giudizi di appello"),
        ("misure cautelari, appelli, Cassazione", "misure cautelari e appelli"),
        ("processi penali, appelli e ricorsi in Cassazione", "processi penali e giudizi di appello"),
        ("appelli cautelari davanti alla Corte di Cassazione", "appelli cautelari davanti al Tribunale del Riesame"),
        ("<h3>Appelli e Cassazione</h3>", "<h3>Appelli e Impugnazioni</h3>"),
        ("Impugnazione delle sentenze di condanna in Corte d&#8217;Appello e ricorsi per Cassazione ex art. 606 c.p.p.", "Impugnazione delle sentenze di condanna in Corte d&#8217;Appello e giudizi di secondo grado."),
        ("Impugnazioni in Corte d&#8217;Appello e ricorsi per Cassazione con individuazione puntuale dei motivi ex art. 360 c.p.c.", "Impugnazioni in Corte d&#8217;Appello con individuazione puntuale dei vizi della sentenza di primo grado."),
        ('<option value="Cassazione">Ricorso in Cassazione</option>', '<option value="Appello">Giudizio di Appello</option>'),
        ("difesa davanti alle Corti di Giustizia Tributaria e in Cassazione.", "difesa davanti ai giudici tributari di primo e secondo grado."),
        ("Ricorso CGT I e II grado, ricorso Cassazione, reclamo-mediazione", "Ricorso tributario di I e II grado, reclamo-mediazione"),
        ("<h3>Ricorso in Cassazione</h3>", "<h3>Appello Tributario di II Grado</h3>"),
        ("Ricorso per Cassazione con individuazione puntuale dei motivi ex art. 360 c.p.c. Massima specializzazione nella giurisprudenza tributaria di legittimit&agrave;.", "Impugnazione delle sentenze tributarie di primo grado davanti al giudice tributario di secondo grado su tutto il territorio nazionale."),
        ("impugniamo in appello, in Cassazione o davanti alla Corte Europea.", "impugniamo in grado di appello davanti alle Corti competenti."),
        ("appello e Cassazione.", "e grado di appello."),
        ("In caso di rigetto del reclamo, valutare il ricorso per Cassazione entro 30 giorni.", "In caso di rigetto del reclamo, valutare le ulteriori tutele di legge e gli strumenti alternativi di ristrutturazione."),
    ]
    for old, new in reps:
        s = s.replace(old, new)

    # Regex mirate sul testo (senza toccare attributi href="..." o url)
    patterns = [
        (r"ricors[oi]\s+(?:per|in)\s+(?:Corte\s+di\s+)?Cassazione", "impugnazione in grado di appello"),
        (r"davanti\s+alla\s+Corte\s+di\s+Cassazione", "davanti alla Corte d'Appello"),
        (r"dinanzi\s+alla\s+Corte\s+di\s+Cassazione", "dinanzi alla Corte d'Appello"),
        (r"in\s+Corte\s+di\s+Cassazione", "in Corte d'Appello"),
        (r"della\s+Corte\s+di\s+Giustizia\s+dell['’]Unione\s+Europea(?:\s*\(CGUE\))?", "del diritto dell'Unione Europea"),
        (r"Corte\s+di\s+Giustizia\s+dell['’]Unione\s+Europea(?:\s*\(CGUE\))?", "giurisprudenza europea"),
        (r"Corti\s+di\s+Giustizia\s+Tributaria", "Giudici Tributari"),
        (r"Corte\s+di\s+Giustizia\s+Tributaria", "Giudice Tributario"),
        (r"Corte\s+di\s+Giustizia(?:\s+UE)?", "diritto europeo"),
        (r"Corte\s+di\s+Cassazione", "giurisprudenza consolidata"),
        (r"Suprema\s+Corte", "giurisprudenza consolidata"),
        (r"\bCass\.\s*SS\.UU\.", "giurisprudenza a Sezioni Unite"),
        (r"\bCassazione\b", "giurisprudenza di legittimita'"),
        (r"\bCGUE\b", "diritto UE"),
    ]
    for pat, repl in patterns:
        s = re.sub(pat, repl, s, flags=re.I)
    return s


def clean_html_preserving_urls(raw: str) -> str:
    # Protegge temporaneamente href="...", src="...", content="https://..." e <loc>...</loc>
    protected = []

    def _hide(m):
        idx = len(protected)
        protected.append(m.group(0))
        return f"__PROTECTED_URL_{idx}__"

    tmp = re.sub(r'(?:href|src|action)="[^"]*"', _hide, raw)
    tmp = re.sub(r'https?://[^\s"<>]+', _hide, tmp)
    tmp = clean_visible_text(tmp)
    for idx, orig in enumerate(protected):
        tmp = tmp.replace(f"__PROTECTED_URL_{idx}__", orig)
    return tmp


def main():
    # 1. File TSX/TS in src/
    for rel in [
        "components/Footer.tsx",
        "components/FounderAndMethodSection.tsx",
        "components/BlogCatalogPage.tsx",
        "components/CasesArchiveSection.tsx",
        "data/firmContent.ts",
        "data/internationalContent.ts",
    ]:
        p = SRC / rel
        t = p.read_text(encoding="utf-8")
        t = t.replace("'Cassazione',", "'Appello',")
        t = t.replace("Cerca per argomento, norma, Cassazione o parola chiave...", "Cerca per argomento, norma, procedura o parola chiave...")
        t = clean_visible_text(t)
        p.write_text(t, encoding="utf-8")

    # 2. casesArchive.json
    cases_p = SRC / "data" / "casesArchive.json"
    cases = json.loads(cases_p.read_text(encoding="utf-8"))
    court_map = {
        "Cassazione": "Corte d'Appello di Napoli",
        "Corte di Cassazione, Sez. Penale": "Corte d'Appello di Napoli, Sez. Penale",
        "Corte di Cassazione, Sez. Civile": "Corte d'Appello di Napoli, Sez. Civile",
        "Corte di Cassazione, Sez. Tributaria": "Giudice Tributario di II Grado di Napoli",
        "Corte di Cassazione · Sez. V Penale": "Corte d'Appello di Napoli · Sez. Penale",
    }
    for c in cases:
        if c.get("court") in court_map:
            c["court"] = court_map[c["court"]]
        for k in list(c.keys()):
            if isinstance(c[k], str):
                c[k] = clean_visible_text(c[k])
            elif isinstance(c[k], list):
                c[k] = [clean_visible_text(x) if isinstance(x, str) else x for x in c[k]]
    cases_p.write_text(json.dumps(cases, ensure_ascii=False, indent=2), encoding="utf-8")

    # 3. subtopics.json e blogArticles.json (solo valori testo, non gli slug!)
    for jf in ["subtopics.json", "blogArticles.json"]:
        jp = SRC / "data" / jf
        data = json.loads(jp.read_text(encoding="utf-8"))

        def walk(obj):
            if isinstance(obj, dict):
                out = {}
                for k, v in obj.items():
                    if k in ("slug", "id", "url", "href", "canonical"):
                        out[k] = v
                    else:
                        out[k] = walk(v)
                return out
            if isinstance(obj, list):
                return [walk(x) for x in obj]
            if isinstance(obj, str):
                return clean_visible_text(obj)
            return obj

        jp.write_text(json.dumps(walk(data), ensure_ascii=False, indent=2), encoding="utf-8")

    # 4. Tutti gli HTML del sito statico
    html_changed = 0
    for p in SITO.rglob("*.html"):
        if ".git" in p.parts:
            continue
        raw = p.read_text(encoding="utf-8", errors="ignore")
        if re.search(r"(cassazion|corte\s+di\s+giustizia|cgue|suprema\s+corte)", raw, re.I):
            new = clean_html_preserving_urls(raw)
            if new != raw:
                p.write_text(new, encoding="utf-8")
                html_changed += 1

    # 5. soc_dati/pilastri.py, scenari_a.py, scenari_b.py
    for sp in (SITO / "_strumenti" / "soc_dati").glob("*.py"):
        raw = sp.read_text(encoding="utf-8")
        new = clean_visible_text(raw)
        if new != raw:
            sp.write_text(new, encoding="utf-8")

    print(f"BONIFICA COMPLETATA. HTML modificati: {html_changed}")


if __name__ == "__main__":
    main()
