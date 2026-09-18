"""Shared head/header/footer extraction + page shell, used by every static
page generator in this repo (build_pages.py, build_blog.py). Centralized so a
second generator script can't drift into its own copy of page_shell() the way
build_pages.py's PAGE_STYLE once duplicated CSS already present in index.html's
own <head> — see git history for that bug."""
import html
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
# Starts at the first skip-link (not <header id="brx-header"> itself) so the two
# skip-links right before the header aren't dropped from every generated page.
HEADER = _extract('<a class="skip-link" href="#brx-content">', "</header>", "HEADER")
FOOTER = _extract('<footer id="brx-footer">', "</footer>", "FOOTER")

FOOTER_SIMPLE = re.sub(r'<p id="brxe-dsiurf".*?</p>', "", FOOTER, count=1, flags=re.S)

# Flecha de los enlaces "Visita la web" / "Leer más". Era un glifo de Ionicons,
# cuya fuente se perdió al retirar wp-content: un SVG inline no depende de nada.
ARROW_ICON = (
    '<svg width="1em" height="1em" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
    'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">'
    '<path d="M5 12h14M13 6l6 6-6 6"/></svg>'
)


def abs_url(path):
    """Canonical, og:url and sitemap <loc> must be absolute: relative values are
    invalid in Open Graph and in the sitemap protocol, and Google drops them."""
    if path.startswith("http"):
        return path
    return SITE_URL + (path if path.startswith("/") else "/" + path)


def _strip_home_only_metadata(head):
    """index.html's Rank Math JSON-LD and og:updated_time describe the homepage:
    its dates, and a Person as the page's main entity. Rewriting the @id per page
    (as this once did) still left every post with the homepage's dateModified next
    to its own Article JSON-LD, so generated pages drop both instead. Posts get
    their dates from build_blog.py's Article JSON-LD."""
    head, n = re.subn(r'<script type="application/ld\+json" class="rank-math-schema">.*?</script>\n?',
                      "", head, count=1, flags=re.S)
    if not n:
        raise SystemExit(
            "index.html structure changed: could not find its rank-math-schema JSON-LD. "
            "Update _strip_home_only_metadata() in scripts/_site.py to match."
        )
    return re.sub(r'<meta property="og:updated_time" content="[^"]*">\n?', "", head, count=1)


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
    h = _strip_home_only_metadata(h)
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
<script src="/assets/js/i18n.js"></script>
<script src="/assets/js/analytics.js"></script>
<script src="/firma.js"></script>
</body></html>"""
