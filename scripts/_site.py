"""Shared head/header/footer extraction + page shell, used by every static
page generator in this repo (build_pages.py, build_blog.py). Centralized so a
second generator script can't drift into its own copy of page_shell() the way
build_pages.py's PAGE_STYLE once duplicated CSS already present in index.html's
own <head> — see git history for that bug."""
import html
import json
import os
import re

SITE_URL = "https://davidhuangxie.com"

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX = os.path.join(ROOT, "index.html")

with open(INDEX, encoding="utf-8") as f:
    SRC = f.read()


def _extract(start_marker, end_marker, label):
    try:
        start = SRC.index(start_marker)
    except ValueError:
        raise SystemExit(
            f"index.html structure changed: could not find the start marker for {label} "
            f"({start_marker!r}). Update the marker in scripts/_site.py to match."
        )
    try:
        end = SRC.index(end_marker, start) + len(end_marker)
    except ValueError:
        raise SystemExit(
            f"index.html structure changed: could not find the end marker for {label} "
            f"({end_marker!r}) after its start. Update the marker in scripts/_site.py to match."
        )
    return SRC[start:end]


HEAD = _extract("<head>", "</head>", "HEAD")
# Starts at the language-switcher div (not <header id="brx-header"> itself) so
# the switcher and the two skip-links right before the header aren't dropped
# from every generated page.
HEADER = _extract('<div id="dhx-lang-switcher"', "</header>", "HEADER")
FOOTER = _extract('<footer id="brx-footer">', "</footer>", "FOOTER")

FOOTER_SIMPLE = re.sub(r'<p id="brxe-dsiurf".*?</p>', "", FOOTER, count=1, flags=re.S)

NAV_EXTRA = (
    '<a class="brxe-text-link label text-blue underline" href="/proyectos/">Más_Proyectos</a>'
    '<a class="brxe-text-link label text-blue underline" href="/estudios/">Estudios</a>'
    '<a class="brxe-text-link label text-blue underline" href="/experiencia/">Experiencia</a>'
    '<a class="brxe-text-link label text-blue underline" href="/blog/">Blog</a>'
)


def abs_url(path):
    """Canonical, og:url and sitemap <loc> must be absolute: relative values are
    invalid in Open Graph and in the sitemap protocol, and Google drops them."""
    if path.startswith("http"):
        return path
    return SITE_URL + (path if path.startswith("/") else "/" + path)


def _localize_json_ld(head, page_url, title):
    """index.html's JSON-LD describes the homepage. Copied verbatim into every
    generated page it would claim each one *is* the homepage, so rewrite the
    WebPage node (and the reference to it) to point at this page instead."""
    m = re.search(r'(<script type="application/ld\+json"[^>]*>)(.*?)(</script>)', head, re.S)
    if not m:
        return head
    try:
        data = json.loads(m.group(2))
    except ValueError:
        return head
    for node in data.get("@graph", []):
        if node.get("@type") == "WebPage":
            node["@id"] = page_url + "#webpage"
            node["url"] = page_url
            node["name"] = title
        if isinstance(node.get("mainEntityOfPage"), dict):
            node["mainEntityOfPage"]["@id"] = page_url + "#webpage"
    return head[:m.start(2)] + json.dumps(data, ensure_ascii=False) + head[m.end(2):]


def build_head(title, description, path):
    """title/description are plain text (escaped here) — never pass pre-built HTML."""
    title = html.escape(title)
    description = html.escape(description)
    h = HEAD
    h = re.sub(r"<title>.*?</title>", f"<title>{title}</title>", h, count=1, flags=re.S)
    h = re.sub(
        r'<meta name="description" content=".*?">',
        f'<meta name="description" content="{description}">',
        h, count=1,
    )
    page_url = abs_url(path)
    h = re.sub(r'<link rel="canonical" href=".*?">', f'<link rel="canonical" href="{page_url}">', h, count=1)
    h = re.sub(r'<meta property="og:title" content=".*?">', f'<meta property="og:title" content="{title}">', h, count=1)
    h = re.sub(
        r'<meta property="og:description" content=".*?">',
        f'<meta property="og:description" content="{description}">',
        h, count=1,
    )
    h = re.sub(r'<meta name="twitter:title" content=".*?">', f'<meta name="twitter:title" content="{title}">', h, count=1)
    h = re.sub(
        r'<meta name="twitter:description" content=".*?">',
        f'<meta name="twitter:description" content="{description}">',
        h, count=1,
    )
    # Both og:url tags in index.html (Rank Math's + the hand-added one) get
    # corrected. Matched by regex rather than by the literal content="/" string:
    # index.html's own og:url is absolute now, so a literal match would silently
    # leave every generated page pointing at the homepage.
    h = re.sub(r'<meta property="og:url" content="[^"]*">',
               f'<meta property="og:url" content="{page_url}">', h)
    h = _localize_json_ld(h, page_url, title)
    return h


# The homepage's own section anchors. On a generated page these must become
# "/#..." so they navigate home first; the skip-links (#brx-content,
# #brx-footer) exist on every page and are deliberately left alone.
HOME_ANCHORS = ("sobre-mi", "servicios", "proyectos", "stack", "contacto")


def build_header(prefix, active):
    h = HEADER
    # cross-page anchors need "/#..." instead of "#..." so smooth-scroll JS (which
    # only targets same-page "#" links) doesn't try to intercept them
    if prefix:
        h = re.sub(r'href="#(' + "|".join(HOME_ANCHORS) + r')"', r'href="/#\1"', h)
    # index.html's header already carries the extra nav links (added directly);
    # only inject them here if they're missing, so re-running this script stays idempotent
    if "Más_Proyectos" in h:
        return h
    h = h.replace(
        '<a id="brxe-hvforz" class="brxe-text-link label text-blue underline" href="%sproyectos" data-brx-anchor="true">Proyectos_Reales</a>'
        % ("/#" if prefix else "#"),
        '<a id="brxe-hvforz" class="brxe-text-link label text-blue underline" href="%sproyectos" data-brx-anchor="true">Proyectos_Reales</a>%s'
        % ("/#" if prefix else "#", NAV_EXTRA),
    )
    return h


def page_shell(title, description, path, active, main_html, extra_style="", extra_head=""):
    head = build_head(title, description, path)
    if extra_style:
        head = head.replace("</head>", f"<style>{extra_style}</style>\n</head>")
    if extra_head:
        head = head.replace("</head>", f"{extra_head}\n</head>")
    header = build_header("/", active)
    return f"""<!DOCTYPE html>
<html lang="es-ES" prefix="og: https://ogp.me/ns#">
{head}
<body class="page-template-default page wp-theme-bricks brx-body">
{header}
<main id="brx-content">
{main_html}
</main>
{FOOTER_SIMPLE}
<script id="bricksforge-gsap-js" src="/assets/vendor/gsap.min.js"></script>
<script id="bricksforge-scrolltrigger-js" src="/assets/vendor/scroll-trigger.min.js"></script>
<script id="bricksforge-splittext-js" src="/assets/vendor/split-text.min.js"></script>
<script id="dhx-animations-js" src="/assets/js/animations.js"></script>
</body></html>"""
