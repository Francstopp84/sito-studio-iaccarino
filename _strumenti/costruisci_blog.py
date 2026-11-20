"""Costruisce il blog dentro il sito (sostituisce la funzione Netlify blog.js).
Uso: python costruisci_blog.py <cartella_repo_blog> <cartella_sito>"""
import json, os, shutil, sys, html

def esc(x):
    return html.escape("" if x is None else str(x), quote=True).replace("&#x27;", "'")

repo, sito = sys.argv[1], sys.argv[2]
lista = json.load(open(os.path.join(repo, "articles.json"), encoding="utf-8"))
blog = os.path.join(sito, "blog"); os.makedirs(blog, exist_ok=True)

# indice
tpl = open(os.path.join(repo, "indice_template.html"), encoding="utf-8").read()
cards = "\n\n".join(
    f'''<a href="/blog/{esc(a['slug'])}.html" class="article-card">
    <div class="article-meta">
      <span class="article-area">{esc(a.get('area'))}</span>
      <span class="article-date">{esc(a.get('data_it'))}</span>
    </div>
    <h2>{esc(a.get('titolo'))}</h2>
    <p>{esc(a.get('descrizione'))}</p>
    <span class="article-cta">Leggi l&#8217;articolo &rarr;</span>
  </a>''' for a in lista)
open(os.path.join(blog, "index.html"), "w", encoding="utf-8", newline="").write(tpl.replace("<!--ARTICOLI-->", cards))

# articoli dal repo (i file statici gia' nel sito hanno la precedenza, come su Netlify)
statici = set(json.load(open(os.path.join(sito, "_strumenti", "blog_statici.json"), encoding="utf-8")))
fatti = 0
for f in os.listdir(os.path.join(repo, "posts")):
    if not f.endswith(".html") or f in statici:
        continue
    t = open(os.path.join(repo, "posts", f), encoding="utf-8").read()
    me = f[:-5]
    altri = [a for a in lista if a["slug"] != me][:4]
    if altri and "</article>" in t and "leggi-anche" not in t:
        li = "".join(f'<li><a href="/blog/{esc(a["slug"])}.html">{esc(a["titolo"])}</a></li>' for a in altri)
        t = t.replace("</article>", f'<aside class="leggi-anche" style="margin:2.5rem 0 1rem;padding:1.2rem 1.5rem;border:1px solid #B8965A;border-radius:8px"><h2 style="font-size:1.3rem;margin:0 0 .6rem">Leggi anche</h2><ul style="margin:0;padding-left:1.2rem;line-height:1.9">{li}</ul><p style="margin:.8rem 0 0"><a href="/blog/">Tutte le guide legali &rarr;</a></p></aside></article>', 1)
    open(os.path.join(blog, f), "w", encoding="utf-8", newline="").write(t); fatti += 1

# immagini
img_src = os.path.join(repo, "img"); img_dst = os.path.join(sito, "img", "blog")
os.makedirs(img_dst, exist_ok=True)
for f in os.listdir(img_src):
    shutil.copy2(os.path.join(img_src, f), os.path.join(img_dst, f))

# sitemap degli articoli non statici
urls = "\n".join(
    f"  <url>\n    <loc>https://studiolegalefrancescoiaccarino.com/blog/{a['slug']}.html</loc>\n    <lastmod>{a.get('data_iso') or ''}</lastmod>\n  </url>"
    for a in lista if not a.get("statico"))
open(os.path.join(sito, "sitemap-blog-extra.xml"), "w", encoding="utf-8", newline="").write(
    f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}\n</urlset>')
print(f"blog: indice {len(lista)} articoli, {fatti} pagine dal repo, {len(os.listdir(img_src))} immagini")
