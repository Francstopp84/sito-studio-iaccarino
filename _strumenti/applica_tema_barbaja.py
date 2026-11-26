# -*- coding: utf-8 -*-
"""
Applica il tema Palazzo Barbaja (Nero Ossidiana #060709 + Oro Champagne #C9B080)
a TUTTE le pagine storiche del sito lasciando intatti al 100% tutti i testi.
"""
from pathlib import Path

SITO = Path(r"D:\STUDIO LEGALE\MODELLI E FORMULARI\Nuovo sito internet\_SITO_GITHUB_PAGES\sito")
LINK_TAG = '<link rel="stylesheet" href="/css/palazzo-barbaja-dark.css?v=1">'


def main():
    updated = 0
    for p in SITO.rglob("*.html"):
        if ".git" in p.parts:
            continue
        rel = p.relative_to(SITO).as_posix()
        # Escludi index.html React e le pagine nuove che usano gia' cyber-wow.css?v=2
        if rel == "index.html":
            continue
        if rel.startswith("cybersicurezza") or rel.startswith("societario"):
            continue
        if rel.endswith("/cybersicurezza.html") or rel.endswith("/societario.html"):
            continue

        raw = p.read_text(encoding="utf-8", errors="ignore")
        if "palazzo-barbaja-dark.css" in raw:
            continue
        if "</head>" in raw:
            new = raw.replace("</head>", f"{LINK_TAG}\n</head>", 1)
            p.write_text(new, encoding="utf-8")
            updated += 1
    print(f"TEMA PALAZZO BARBAJA APPLICATO A {updated} PAGINE STORICHE.")


if __name__ == "__main__":
    main()
