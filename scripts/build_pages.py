#!/usr/bin/env python3
"""Generates /proyectos/, /estudios/ and /experiencia/ static pages
from index.html's head/header/footer, reusing the site's design system.
Shared extraction/shell logic lives in _site.py."""
import html
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _site import ARROW_ICON, ROOT, page_shell  # noqa: E402

PAGE_STYLESHEET = '<link rel="stylesheet" href="/assets/css/pages.css">'

os.makedirs(os.path.join(ROOT, "proyectos"), exist_ok=True)
os.makedirs(os.path.join(ROOT, "estudios"), exist_ok=True)
os.makedirs(os.path.join(ROOT, "experiencia"), exist_ok=True)

DATA = os.path.join(ROOT, "assets", "data")


def load_json(name):
    path = os.path.join(DATA, name)
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def require(entry, field, index, source):
    if field not in entry:
        raise SystemExit(f"{source} entrada {index} sin campo obligatorio {field!r}: {entry}")
    return entry[field]


def esc(value):
    return html.escape(str(value)) if value is not None else ""


# ---------------------------------------------------------------- PROYECTOS
projects = load_json("projects.json")
case_studies = load_json("case-studies.json")


def visit_link(url, text="Visita la web"):
    # Los enlaces externos abren pestaña nueva; los internos (/blog/) no.
    external = url.startswith("http")
    target = ' target="_blank" rel="noopener noreferrer"' if external else ""
    return (f'<a class="brxe-text-link label text-blue underline" href="{esc(url)}"{target}>'
            f'<span class="icon">{ARROW_ICON}</span><span class="text">{esc(text)}</span></a>')


def stack_html(items):
    return "".join(f'<p class="brxe-text-basic badge-infraestructure">{esc(s)}</p>' for s in items)


def project_card(i, p):
    img = require(p, "img", i, "projects.json")
    alt = require(p, "alt", i, "projects.json")
    name = require(p, "name", i, "projects.json")
    mini_description = require(p, "miniDescription", i, "projects.json")
    if p.get("link"):
        link_html = visit_link(p["link"])
    else:
        link_html = '<p class="brxe-text-basic label" style="color:var(--color-text-muted)">Proyecto interno / sin enlace público</p>'
    return f"""<div class="brxe-block terminal grow-hover project-card">
<div class="project-card-image background-glow"><img src="/assets/projects/{esc(img)}" alt="{esc(alt)}" loading="lazy"></div>
<div class="project-card-body">
<h3 class="brxe-heading">{esc(name)}</h3>
<div class="project-card-stack">{stack_html(p.get("stack", []))}</div>
<p class="brxe-text-basic">{esc(mini_description)}</p>
{link_html}
</div>
</div>"""


def case_list(title, items, extra_class=""):
    if not items:
        return ""
    lis = "".join(f"<li>{esc(x)}</li>" for x in items)
    return (f'<div class="case-card-block"><p class="brxe-text-basic label text-blue">{esc(title)}</p>'
            f'<ul class="case-list{extra_class}">{lis}</ul></div>')


def case_card(i, c):
    name = require(c, "name", i, "case-studies.json")
    context = require(c, "context", i, "case-studies.json")
    reto = require(c, "reto", i, "case-studies.json")
    hice = require(c, "hice", i, "case-studies.json")
    status = f'<p class="brxe-text-basic badge-primary">{esc(c["status"])}</p>' if c.get("status") else ""
    link_html = visit_link(c["link"], c.get("linkText", "Visita la web")) if c.get("link") else ""
    return f"""<article class="brxe-block terminal case-card">
<div class="case-card-head"><p class="brxe-text-basic label">{esc(context)}</p>{status}</div>
<h3 class="brxe-heading text-white">{esc(name)}</h3>
<p class="brxe-text-basic">{esc(reto)}</p>
<div class="case-card-cols">
{case_list("Qué hice", hice)}
{case_list("Resultado", c.get("resultado", []), " case-result")}
</div>
<div class="project-card-stack">{stack_html(c.get("stack", []))}</div>
{link_html}
</article>"""


def section_title(label, title):
    return (f'<div class="proyectos-section-title"><p class="brxe-text-basic label text-blue">{esc(label)}</p>'
            f'<h2 class="brxe-heading text-white">{esc(title)}</h2></div>')


client_cards = [project_card(i, p) for i, p in enumerate(projects) if not p.get("practica")]
practice_cards = [project_card(i, p) for i, p in enumerate(projects) if p.get("practica")]
case_cards = [case_card(i, c) for i, c in enumerate(case_studies)]

proyectos_main = f"""<section class="brxe-section section"><div class="brxe-container" style="flex-direction:column">
<div class="page-hero">
<p class="brxe-text-basic label text-blue">// ALL_DEPLOYMENTS</p>
<h1 class="brxe-heading text-white">Proyectos</h1>
<p class="brxe-text-basic">Primero, tres casos contados de principio a fin: qué problema había, qué hice y qué resultado dio. Después, las webs que he hecho para clientes y, al final, las prácticas con las que aprendí.</p>
<a class="brxe-button btn-secondary grow-hover bricks-button back-link" href="/">&larr; Volver al inicio</a>
</div>
{section_title("// CASE_STUDIES", "Casos de estudio")}
<div class="casos-grid">
{''.join(case_cards)}
</div>
{section_title("// CLIENT_DEPLOYMENTS", "Webs para clientes")}
<div class="proyectos-grid">
{''.join(client_cards)}
</div>
{section_title("// TRAINING", "Prácticas de formación")}
<div class="proyectos-grid">
{''.join(practice_cards)}
</div>
</div></section>"""

with open(os.path.join(ROOT, "proyectos", "index.html"), "w", encoding="utf-8") as f:
    f.write(page_shell(
        "Proyectos | David Huang Xie — Desarrollador Web Full-Stack",
        "Casos de estudio y webs reales: automatización con n8n e IA, infraestructura propia y webs WordPress y WooCommerce para negocios: qué hice y qué resultado dio.",
        "/proyectos/", "proyectos", proyectos_main, extra_head=PAGE_STYLESHEET,
    ))

# ----------------------------------------------------------------- ESTUDIOS
studies = load_json("studies.json")

study_cards = []
for i, s in enumerate(studies):
    degree = require(s, "degree", i, "studies.json")
    institution = require(s, "institution", i, "studies.json")
    img = require(s, "img", i, "studies.json")
    description = require(s, "description", i, "studies.json")

    desc = "".join(f'<p class="brxe-text-basic">{esc(d)}</p>' for d in description)
    study_cards.append(f"""<div class="brxe-block terminal grow-hover study-card">
<div class="study-card-image background-glow"><img src="/assets/{esc(img)}" alt="{esc(degree)}" loading="lazy"></div>
<div class="study-card-body">
<div class="study-card-header">
<h2 class="brxe-heading">{esc(degree)}</h2>
<p class="brxe-text-basic badge-primary">{esc(s.get('time', ''))}</p>
</div>
<p class="brxe-text-basic label text-blue">{esc(institution)}</p>
<div class="study-card-desc">{desc}</div>
</div>
</div>""")

estudios_main = f"""<section class="brxe-section section"><div class="brxe-container" style="flex-direction:column">
<div class="page-hero">
<p class="brxe-text-basic label text-blue">// ACADEMIC_LOG</p>
<h1 class="brxe-heading text-white">Estudios</h1>
<p class="brxe-text-basic">Mi trayectoria académica: estudios universitarios, un Erasmus+ en Portugal y los cursos y bootcamps que he realizado a lo largo de mi carrera para especializarme en desarrollo web.</p>
<a class="brxe-button btn-secondary grow-hover bricks-button back-link" href="/">&larr; Volver al inicio</a>
</div>
<div class="estudios-list">
{''.join(study_cards)}
</div>
</div></section>"""

with open(os.path.join(ROOT, "estudios", "index.html"), "w", encoding="utf-8") as f:
    f.write(page_shell(
        "Estudios | David Huang Xie — Desarrollador Web Full-Stack",
        "Trayectoria académica de David Huang Xie: Bootcamp de Desarrollo Web Full-Stack, Diseño UX, Marketing e Investigación de Mercados y Erasmus+ en Portugal.",
        "/estudios/", "estudios", estudios_main, extra_head=PAGE_STYLESHEET,
    ))

# -------------------------------------------------------------- EXPERIENCIA
workplace = load_json("workplace.json")

verko = {
    "position": "Desarrollador WordPress",
    "company": "Grupo Verko",
    "time": "Septiembre 2026 - Actualidad",
    "img": "experiencia/Verko.webp",
    "miniDescription": (
        "Agencia de marketing en la que trabajo actualmente. Desarrollo los sitios web de los clientes de la "
        "agencia con WordPress y Bricks Builder, dentro de un equipo con procesos y estándares ya establecidos, "
        "y participo en el desarrollo de plugins propios a medida."
    ),
    "funciones": [
        "Desarrollo y maquetación web con WordPress y Bricks Builder",
        "Desarrollo de plugins a medida",
        "SEO técnico on-page y Core Web Vitals",
    ],
    "link": "https://grupoverko.com/",
}

angulotres = {
    "position": "Diseñador y Desarrollador Web",
    "company": "Ángulo Tres",
    "time": "Enero 2026 - Agosto 2026",
    "img": "experiencia/AnguloTres.webp",
    "miniDescription": (
        "Único perfil técnico de la agencia. Mi puesto de contrato era Diseñador Web, pero en la práctica cubrí "
        "todo el ciclo de vida de los proyectos digitales: diseño, desarrollo con WordPress y Bricks Builder, "
        "automatización de procesos internos y de clientes con n8n y agentes de IA, SEO técnico e infraestructura "
        "on-premise, que monté y mantuve yo. Por confidencialidad con los clientes de la agencia no puedo enlazar "
        "los proyectos concretos en los que trabajé."
    ),
    "funciones": [
        "Desarrollo y maquetación web con WordPress y Bricks Builder",
        "Automatización de procesos con n8n, agentes de IA y MCP",
        "SEO técnico on-page y off-page, Core Web Vitals",
        "Infraestructura on-premise: Docker, servidores locales, LLMs locales",
    ],
    "link": None,
}

jobs = [verko, angulotres] + workplace

job_cards = []
for i, j in enumerate(jobs):
    position = require(j, "position", i, "workplace.json (o entrada fija)")
    company = require(j, "company", i, "workplace.json (o entrada fija)")
    mini_description = require(j, "miniDescription", i, "workplace.json (o entrada fija)")

    funciones = "".join(f'<p class="brxe-text-basic badge-infraestructure">{esc(fn)}</p>' for fn in j.get("funciones", []))
    if j.get("img"):
        img_html = f'<div class="job-card-image"><img src="/assets/{esc(j["img"])}" alt="{esc(company)}" loading="lazy"></div>'
    else:
        img_html = '<div class="job-card-image placeholder"><p class="brxe-text-basic label" style="text-align:center">Trabajo actual<br>bajo NDA</p></div>'
    if j.get("link"):
        link_html = (f'<a class="brxe-text-link label text-blue underline" href="{esc(j["link"])}" target="_blank" '
                     f'rel="noopener noreferrer"><span class="icon">{ARROW_ICON}</span>'
                     f'<span class="text">Visita la web</span></a>')
    else:
        link_html = ""
    time_html = f'<p class="brxe-text-basic badge-primary">{esc(j["time"])}</p>' if j.get("time") else ""
    job_cards.append(f"""<div class="brxe-block terminal grow-hover job-card">
{img_html}
<div class="job-card-body">
<div class="job-card-header">
<h2 class="brxe-heading">{esc(position)}</h2>
{time_html}
</div>
<p class="brxe-text-basic label text-blue">{esc(company)}</p>
<p class="brxe-text-basic">{esc(mini_description)}</p>
<div class="job-card-funciones">{funciones}</div>
{link_html}
</div>
</div>""")

experiencia_main = f"""<section class="brxe-section section"><div class="brxe-container" style="flex-direction:column">
<div class="page-hero">
<p class="brxe-text-basic label text-blue">// WORK_LOG</p>
<h1 class="brxe-heading text-white">Experiencia</h1>
<p class="brxe-text-basic">Mi trayectoria profesional, desde mis prácticas universitarias hasta mi puesto actual en Verko. Desarrollo web con WordPress, automatización con n8n e IA, SEO técnico e infraestructura.</p>
<a class="brxe-button btn-secondary grow-hover bricks-button back-link" href="/">&larr; Volver al inicio</a>
</div>
<div class="experiencia-list">
{''.join(job_cards)}
</div>
</div></section>"""

with open(os.path.join(ROOT, "experiencia", "index.html"), "w", encoding="utf-8") as f:
    f.write(page_shell(
        "Experiencia | David Huang Xie — Desarrollador Web Full-Stack",
        "Trayectoria profesional de David Huang Xie: Verko, Ángulo Tres, Almoraima Soluciones y La Buhardilla del Marketing. Desarrollo web, automatización con IA y SEO técnico.",
        "/experiencia/", "experiencia", experiencia_main, extra_head=PAGE_STYLESHEET,
    ))

print("Built /proyectos/, /estudios/, /experiencia/")
