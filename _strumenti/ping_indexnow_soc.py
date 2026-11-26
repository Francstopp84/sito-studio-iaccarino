# -*- coding: utf-8 -*-
"""Invia ping IndexNow per tutte le 200 URL della 6a area Societario/231/CCII + home."""
import json
import sys
import urllib.request
from pathlib import Path

ROOT = Path(r"D:\STUDIO LEGALE\MODELLI E FORMULARI\Nuovo sito internet\_SITO_GITHUB_PAGES\sito")
BASE_URL = "https://studiolegalefrancescoiaccarino.com"
HOST = "studiolegalefrancescoiaccarino.com"

sys.path.insert(0, str(ROOT / "_strumenti"))
from soc_dati.pilastri import PILASTRI, LINGUE_ESTERE
from soc_dati.scenari_a import SCENARI_A
from soc_dati.scenari_b import SCENARI_B
from soc_dati.scenari_c import SCENARI_C
from soc_dati.guide_soc import GUIDE_SOC

SCENARI = SCENARI_A + SCENARI_B + SCENARI_C

KEY_FILE = ROOT / "24f4bc2b1b81fcbddb240c707060128f.txt"
KEY = KEY_FILE.read_text(encoding="utf-8").strip()

urls = [
    f"{BASE_URL}/",
    f"{BASE_URL}/societario.html",
    f"{BASE_URL}/societario/scenari/index.html",
    f"{BASE_URL}/societario/guide/index.html",
]
urls += [f"{BASE_URL}/societario/{p['slug']}.html" for p in PILASTRI]
urls += [f"{BASE_URL}/societario/scenari/{s['slug']}.html" for s in SCENARI]
urls += [f"{BASE_URL}/societario/guide/{g['slug']}.html" for g in GUIDE_SOC]
urls += [f"{BASE_URL}/{code}/societario.html" for code in LINGUE_ESTERE]

seen = set()
url_list = []
for u in urls:
    if u not in seen:
        seen.add(u)
        url_list.append(u)

payload = {
    "host": HOST,
    "key": KEY,
    "keyLocation": f"{BASE_URL}/{KEY}.txt",
    "urlList": url_list,
}

req = urllib.request.Request(
    "https://api.indexnow.org/indexnow",
    data=json.dumps(payload).encode("utf-8"),
    headers={"Content-Type": "application/json; charset=utf-8"},
    method="POST",
)

try:
    with urllib.request.urlopen(req, timeout=30) as resp:
        status = resp.status
        body = resp.read().decode("utf-8", errors="ignore")
        print(f"INDEXNOW_STATUS={status} | URL_INVIATE={len(url_list)} | KEY={KEY}")
        if body:
            print("BODY:", body[:300])
except Exception as e:
    print(f"INDEXNOW_ERRORE={e}")
    sys.exit(1)
