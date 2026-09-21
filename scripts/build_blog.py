#!/usr/bin/env python3
"""Generates /blog/ (post list) and /blog/<slug>/ (each post) from Markdown
files in content/blog/, and keeps page-sitemap.xml in sync. Shares head/
header/footer logic with build_pages.py via _site.py."""
import html
import json
import math
import os
import re
import sys
from datetime import date

import markdown
from markdown.extensions.toc import slugify_unicode

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _site import ARROW_ICON, ROOT, page_shell  # noqa: E402

CONTENT_DIR = os.path.join(ROOT, "content", "blog")
BLOG_DIR = os.path.join(ROOT, "blog")
SITEMAP_PATH = os.path.join(ROOT, "page-sitemap.xml")
# Índices que apuntan a page-sitemap.xml (robots.txt anuncia sitemap_index.xml;
# sitemap.xml es la ruta que prueban los rastreadores por defecto).
SITEMAP_INDEX_PATHS = [os.path.join(ROOT, name) for name in ("sitemap_index.xml", "sitemap.xml")]
# og:image/twitter:image need an absolute URL to resolve for external crawlers
# (Facebook/LinkedIn/Twitter preview bots), unlike canonical links elsewhere
# in this site which stay relative.
from _site import SITE_URL as BASE_URL  # una sola definición del dominio

PAGE_STYLESHEET = '<link rel="stylesheet" href="/assets/css/blog.css">'
# Solo en las páginas de post: marca en el índice la sección que se está leyendo.
POST_SCRIPT = '<script src="/assets/js/blog-toc.js" defer></script>'


def parse_post(path):
    with open(path, encoding="utf-8") as f:
        raw = f.read()

    m = re.match(r"^---\n(.*?)\n---\n(.*)$", raw, flags=re.S)
    if not m:
        raise SystemExit(f"{path}: falta el frontmatter delimitado por '---' al principio del archivo.")
    frontmatter_raw, body_raw = m.groups()

    frontmatter = {}
    for line in frontmatter_raw.splitlines():
        if not line.strip():
            continue
        if ":" not in line:
            raise SystemExit(f"{path}: línea de frontmatter inválida (falta ':'): {line!r}")
        key, _, value = line.partition(":")
        frontmatter[key.strip()] = value.strip()

    for required in ("title", "description", "date"):
        if required not in frontmatter:
            raise SystemExit(f"{path}: falta el campo obligatorio {required!r} en el frontmatter.")

    try:
        post_date = date.fromisoformat(frontmatter["date"])
    except ValueError:
        raise SystemExit(f"{path}: 'date' debe tener formato AAAA-MM-DD, no {frontmatter['date']!r}.")

    updated = None
    if "updated" in frontmatter:
        try:
            updated = date.fromisoformat(frontmatter["updated"])
        except ValueError:
            raise SystemExit(f"{path}: 'updated' debe tener formato AAAA-MM-DD, no {frontmatter['updated']!r}.")
        if updated < post_date:
            raise SystemExit(f"{path}: 'updated' ({updated}) no puede ser anterior a 'date' ({post_date}).")

    if ("image" in frontmatter) != ("image_alt" in frontmatter):
        raise SystemExit(f"{path}: 'image' e 'image_alt' deben ir juntos (falta uno de los dos).")

    slug = os.path.splitext(os.path.basename(path))[0]
    # "toc" da un id a cada encabezado (para el índice del sidebar) y devuelve la lista de secciones.
    md = markdown.Markdown(
        extensions=["fenced_code", "tables", "toc"],
        extension_configs={"toc": {"slugify": slugify_unicode, "toc_depth": "2-3"}},
    )
    body_html = md.convert(body_raw.strip())
    sections = [(t["id"], t["name"]) for t in md.toc_tokens if t["level"] == 2]

    return {
        "slug": slug,
        "title": frontmatter["title"],
        "description": frontmatter["description"],
        "date": post_date,
        # Fecha de la última revisión de contenido; si no hay, cuenta la de publicación.
        "updated": updated or post_date,
        "body_html": body_html,
        "sections": sections,
        "words": len(body_raw.split()),
        "image": frontmatter.get("image"),
        "image_alt": frontmatter.get("image_alt"),
    }


def post_dates(post):
    published = post["date"].strftime("%d/%m/%Y")
    if post["updated"] == post["date"]:
        return published
    return f"{published} · Actualizado {post['updated'].strftime('%d/%m/%Y')}"


def image_meta_tags(post):
    if not post["image"]:
        return ""
    url = f"{BASE_URL}{post['image']}"
    return (
        f'<meta property="og:image" content="{html.escape(url)}">'
        f'<meta name="twitter:image" content="{html.escape(url)}">'
    )


def json_ld_article(post):
    data = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": post["title"],
        "description": post["description"],
        "datePublished": post["date"].isoformat(),
        "dateModified": post["updated"].isoformat(),
        "author": {"@type": "Person", "name": "David Huang Xie"},
    }
    if post["image"]:
        data["image"] = f"{BASE_URL}{post['image']}"
    # json.dumps is HTML-safe enough for a script tag here (no user input, no "</script" risk
    # from our own frontmatter), but escape defensively anyway since titles are free text.
    return f'<script type="application/ld+json">{json.dumps(data, ensure_ascii=False)}</script>'


def reading_time(post):
    return f"{max(1, math.ceil(post['words'] / 200))} min de lectura"


def toc_list(post):
    # Los nombres que devuelve "toc" ya vienen escapados.
    items = "".join(f'<li><a href="#{sid}">{name}</a></li>' for sid, name in post["sections"])
    return f"<ol>{items}</ol>"


def _text(fragment):
    return html.unescape(re.sub(r"<[^>]+>", "", fragment)).strip()


FAQ_H2 = re.compile(r'<h2 id="([^"]*)">Preguntas frecuentes</h2>')


def split_faq(body_html):
    """Saca la sección "Preguntas frecuentes" del cuerpo y la convierte en un bloque
    propio con cada pregunta desplegable. Devuelve (html, [(pregunta, respuesta)])."""
    m = FAQ_H2.search(body_html)
    if not m:
        return body_html, []
    end = body_html.find("<h2", m.end())
    end = len(body_html) if end == -1 else end
    chunk = body_html[m.end():end]
    parts = re.split(r"(?=<h3)", chunk)
    intro, items, faq = parts[0], [], []
    for part in parts[1:]:
        q = re.match(r'<h3 id="([^"]*)">(.*?)</h3>(.*)', part, flags=re.S)
        if not q:
            intro += part
            continue
        qid, question, answer = q.groups()
        items.append(
            f'<details class="blog-faq-item"><summary><h3 id="{qid}">{question}</h3></summary>'
            f'<div class="blog-faq-answer">{answer.strip()}</div></details>'
        )
        faq.append((_text(question), _text(answer)))
    if not items:
        return body_html, []
    section = (
        f'<section class="blog-faq" aria-labelledby="{m.group(1)}">'
        f'<p class="blog-faq-label">// FAQ</p><h2 id="{m.group(1)}">Preguntas frecuentes</h2>{intro.strip()}'
        f'<div class="blog-faq-list">{"".join(items)}</div></section>'
    )
    return body_html[:m.start()] + section + body_html[end:], faq


def wrap_cta(body_html):
    """El cierre de cada post (### ¿…? + [Contáctame](/#contacto)) pasa a ser una caja con botón."""
    m = re.search(r'<h3 id="[^"]*">¿[^<]*</h3>(?:(?!<h[23]).)*?<a href="/#contacto">[^<]*</a>(?:(?!<h[23]).)*$',
                  body_html, flags=re.S)
    if not m:
        return body_html
    cta = m.group(0).replace('<a href="/#contacto">',
                             '<a class="brxe-button btn-primary bricks-button grow-hover" href="/#contacto">')
    return body_html[:m.start()] + f'<div class="blog-cta">{cta}</div>' + body_html[m.end():]


def related_posts(post, posts):
    """Primero los posts que el artículo enlaza; después, los más recientes."""
    by_slug = {p["slug"]: p for p in posts}
    linked = re.findall(r'href="/blog/([a-z0-9-]+)/"', post["body_html"])
    order = [s for s in dict.fromkeys(linked) if s in by_slug and s != post["slug"]]
    order += [p["slug"] for p in posts if p["slug"] != post["slug"] and p["slug"] not in order]
    return [by_slug[s] for s in order[:3]]


def json_ld_faq(faq):
    if not faq:
        return ""
    data = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq
        ],
    }
    return f'<script type="application/ld+json">{json.dumps(data, ensure_ascii=False)}</script>'


def update_sitemap(posts):
    if not os.path.exists(SITEMAP_PATH):
        return
    with open(SITEMAP_PATH, encoding="utf-8") as f:
        sitemap = f.read()

    # Remove any previously-generated /blog/ entries so re-running this script
    # doesn't accumulate duplicates as posts are added, renamed or removed.
    sitemap = re.sub(r"\t<url>\n\t\t<loc>" + re.escape(BASE_URL) + r"/blog/[^<]*</loc>\n\t\t<lastmod>[^<]*</lastmod>\n\t</url>\n", "", sitemap)

    # El listado cambia cuando se publica o se actualiza cualquier post.
    last_change = max((post["updated"] for post in posts), default=None)
    entries = [f"\t<url>\n\t\t<loc>{BASE_URL}/blog/</loc>\n\t\t<lastmod>{last_change.isoformat()}T00:00:00+00:00</lastmod>\n\t</url>\n"] if posts else []
    for post in posts:
        entries.append(
            f"\t<url>\n\t\t<loc>{BASE_URL}/blog/{post['slug']}/</loc>\n\t\t<lastmod>{post['updated'].isoformat()}T00:00:00+00:00</lastmod>\n\t</url>\n"
        )

    sitemap = sitemap.replace("</urlset>", "".join(entries) + "</urlset>")
    # Google rechaza el sitemap entero si una sola <loc> o <image:loc> es relativa
    # (pasó con las imágenes heredadas del export de Rank Math).
    relative = [u for u in re.findall(r"<(?:image:)?loc>([^<]*)</", sitemap) if not u.startswith(BASE_URL + "/")]
    if relative:
        raise SystemExit(f"{SITEMAP_PATH}: URLs no absolutas en el sitemap: {relative}")
    with open(SITEMAP_PATH, "w", encoding="utf-8") as f:
        f.write(sitemap)
    update_sitemap_indexes(sitemap)


def update_sitemap_indexes(sitemap):
    """El <lastmod> del índice es la señal de que page-sitemap.xml ha cambiado:
    sin esto se quedaba con la fecha del export de Rank Math (2026-07-08)."""
    last_change = max(re.findall(r"<lastmod>([^<]*)</lastmod>", sitemap), key=lambda v: v[:10])
    for path in SITEMAP_INDEX_PATHS:
        if not os.path.exists(path):
            continue
        with open(path, encoding="utf-8") as f:
            index = f.read()
        entry = re.escape(f"<loc>{BASE_URL}/page-sitemap.xml</loc>")
        index, n = re.subn(r"(" + entry + r"\s*<lastmod>)[^<]*(</lastmod>)", r"\g<1>" + last_change + r"\g<2>", index)
        if n != 1:
            raise SystemExit(f"{path}: no encuentro la entrada de page-sitemap.xml con su <lastmod>.")
        with open(path, "w", encoding="utf-8") as f:
            f.write(index)


def main():
    if not os.path.isdir(CONTENT_DIR):
        print("content/blog/ no existe todavía — nada que generar.")
        return

    paths = [os.path.join(CONTENT_DIR, name) for name in sorted(os.listdir(CONTENT_DIR)) if name.endswith(".md")]
    posts = sorted((parse_post(p) for p in paths), key=lambda post: post["date"], reverse=True)

    os.makedirs(BLOG_DIR, exist_ok=True)

    list_items = []
    for post in posts:
        thumb_html = (
            f'<img src="{post["image"]}" alt="{html.escape(post["image_alt"])}" loading="lazy">'
            if post["image"] else ""
        )
        list_items.append(f"""<div class="brxe-block terminal grow-hover blog-list-item">
{thumb_html}
<p class="blog-date">{post['date'].strftime('%d/%m/%Y')}</p>
<h2 class="brxe-heading"><a class="brxe-text-link" href="/blog/{post['slug']}/">{html.escape(post['title'])}</a></h2>
<p class="brxe-text-basic">{html.escape(post['description'])}</p>
<a class="brxe-text-link label text-blue underline" href="/blog/{post['slug']}/"><span class="icon">{ARROW_ICON}</span><span class="text">Leer más</span></a>
</div>""")

    blog_main = f"""<section class="brxe-section section"><div class="brxe-container" style="flex-direction:column">
<div class="page-hero">
<p class="brxe-text-basic label text-blue">// WRITE_LOG</p>
<h1 class="brxe-heading text-white">Blog</h1>
<p class="brxe-text-basic">Notas sobre desarrollo web, WordPress, automatización y los proyectos en los que trabajo.</p>
<a class="brxe-button btn-secondary grow-hover bricks-button back-link" href="/">&larr; Volver al inicio</a>
</div>
<div class="blog-list">
{''.join(list_items) if list_items else '<p class="brxe-text-basic">Todavía no hay artículos publicados.</p>'}
</div>
</div></section>"""

    with open(os.path.join(BLOG_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(page_shell(
            "Blog | David Huang Xie — Desarrollador Web Full-Stack",
            "Notas sobre desarrollo web, WordPress, Bricks Builder, automatización con IA y los proyectos en los que trabajo.",
            "/blog/", "blog", blog_main, extra_head=PAGE_STYLESHEET,
        ))

    for post in posts:
        post_dir = os.path.join(BLOG_DIR, post["slug"])
        os.makedirs(post_dir, exist_ok=True)

        hero_html = (
            f'<img src="{post["image"]}" alt="{html.escape(post["image_alt"])}" loading="lazy">'
            if post["image"] else ""
        )
        body_html, faq = split_faq(post["body_html"])
        body_html = wrap_cta(body_html)
        toc = toc_list(post)
        related = "".join(
            f"""<a class="blog-related-item grow-hover" href="/blog/{r['slug']}/">
<span class="blog-date">{r['date'].strftime('%d/%m/%Y')}</span>
<span class="blog-related-title">{html.escape(r['title'])}</span>
</a>""" for r in related_posts(post, posts)
        )
        post_main = f"""<section class="brxe-section section"><div class="brxe-container" style="flex-direction:column">
<div class="blog-post">
<a class="brxe-button btn-secondary grow-hover bricks-button back-link" href="/blog/">&larr; Volver al blog</a>
<header class="blog-post-header">
{hero_html}
<p class="blog-date">{post_dates(post)} · {reading_time(post)}</p>
<h1 class="brxe-heading text-white">{html.escape(post['title'])}</h1>
<p class="blog-post-lead">{html.escape(post['description'])}</p>
</header>
<div class="blog-post-layout">
<article class="blog-post-card">
<div class="blog-post-bar"><div class="mac-controls"><span></span></div><span class="blog-post-file">~/blog/{post['slug']}.md</span></div>
<details class="blog-toc-mobile"><summary>Índice del artículo</summary><nav aria-label="Índice del artículo">{toc}</nav></details>
<div class="blog-post-body">
{body_html}
</div>
</article>
<aside class="blog-post-aside">
<nav class="blog-toc" aria-label="Índice del artículo">
<p class="blog-toc-label">// ÍNDICE</p>
{toc}
</nav>
</aside>
</div>
<section class="blog-related" aria-labelledby="sigue-leyendo">
<h2 id="sigue-leyendo" class="blog-related-heading">Sigue leyendo</h2>
<div class="blog-related-list">
{related}
</div>
</section>
</div>
</div></section>"""

        with open(os.path.join(post_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(page_shell(
                f"{post['title']} | Blog de David Huang Xie",
                post["description"],
                f"/blog/{post['slug']}/", "blog", post_main,
                extra_head=PAGE_STYLESHEET + POST_SCRIPT + json_ld_article(post) + json_ld_faq(faq) + image_meta_tags(post),
            ))

    update_sitemap(posts)
    print(f"Built /blog/ with {len(posts)} post(s), updated page-sitemap.xml")


if __name__ == "__main__":
    main()
