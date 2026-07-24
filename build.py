#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
G3FSP — Générateur des pages intérieures.

Produit du HTML statique pur (aucune dépendance à l'exécution).
Relancer après modification du contenu :  python build.py
L'accueil (index.html) est écrit à la main et n'est pas touché par ce script.
"""

import os
import json

from common import SITE, TEL_RAW, TEL_FMT, MAIL, WA

ROOT = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------------------
# Fragments partagés
# ---------------------------------------------------------------------------

HEADER = """<header class="site-header">
  <div class="site-header__inner">
    <a class="logo" href="/" aria-label="G3FSP — Accueil">
      <img src="/img/logo-mark.webp" alt="G3FSP" width="440" height="352" class="logo__img">
    </a>
    <nav class="site-nav" aria-label="Navigation principale">
      <ul>
        <li><a href="/services/"{cur_services}>Services</a></li>
        <li><a href="/realisations/"{cur_real}>Réalisations</a></li>
        <li><a href="/zones-intervention/"{cur_zones}>Zones</a></li>
        <li><a href="/a-propos/"{cur_apropos}>À propos</a></li>
        <li><a href="/contact/"{cur_contact}>Contact</a></li>
      </ul>
    </nav>
    <div class="header-actions">
      <a class="header-tel" href="tel:TELRAW">TELFMT</a>
      <a class="btn btn--primary" href="/contact/">Devis gratuit</a>
      <button class="burger" type="button" aria-expanded="false"
              aria-controls="mobile-menu" aria-label="Ouvrir le menu">
        <span></span><span></span><span></span>
      </button>
    </div>
  </div>
</header>

<div class="mobile-menu" id="mobile-menu" data-open="false">
  <a href="/services/">Services</a>
  <a href="/realisations/">Réalisations</a>
  <a href="/zones-intervention/">Zones d'intervention</a>
  <a href="/a-propos/">À propos</a>
  <a href="/contact/">Contact</a>
  <a class="btn btn--primary" href="/contact/">Demander un devis</a>
</div>
""".replace("TELRAW", TEL_RAW).replace("TELFMT", TEL_FMT.replace(" ", "&nbsp;"))

CTA_BAND = """
<section class="cta-band trame">
  <div class="wrap">
    <div data-reveal>
      <span class="sec-num">{num} /</span>
      <h2>{title}</h2>
      <p>{text}</p>
      <div class="cta-band__actions">
        <a class="btn btn--primary" href="/contact/">
          Demander un devis gratuit <span class="btn__arrow" aria-hidden="true">&rarr;</span>
        </a>
        <a class="btn btn--ghost-invert" href="tel:TELRAW">TELFMT</a>
      </div>
    </div>
  </div>
</section>
""".replace("TELRAW", TEL_RAW).replace("TELFMT", TEL_FMT)

FOOTER = """
<footer class="site-footer">
  <div class="footer-grid">
    <div class="footer-col">
      <a class="logo" href="/" aria-label="G3FSP — Accueil">
        <img src="/img/logo-mark.webp" alt="G3FSP" width="440" height="352"
             class="logo__img logo__img--footer">
      </a>
      <p class="footer-brandline">Construire sur du solide</p>
      <p>Fondations spéciales &amp; géotechnique.<br>Casablanca, Maroc.</p>
    </div>
    <div class="footer-col">
      <h3>Services</h3>
      <ul>
        <li><a href="/services/micropieux/">Pieux &amp; Micropieux</a></li>
        <li><a href="/services/tirants-ancrage/">Tirants d'ancrage</a></li>
        <li><a href="/services/tirants-ancrage/">Clouage</a></li>
        <li><a href="/services/beton-projete/">Béton projeté</a></li>
      </ul>
    </div>
    <div class="footer-col">
      <h3>Zones</h3>
      <ul>
        <li><a href="/zones-intervention/casablanca/">Casablanca</a></li>
        <li><a href="/zones-intervention/rabat/">Rabat</a></li>
        <li><a href="/zones-intervention/tanger/">Tanger</a></li>
        <li><a href="/zones-intervention/marrakech/">Marrakech</a></li>
        <li><a href="/zones-intervention/agadir/">Agadir</a></li>
      </ul>
    </div>
    <div class="footer-col">
      <h3>Contact</h3>
      <ul>
        <li><a href="tel:TELRAW">TELFMT</a></li>
        <li><a href="mailto:MAIL">MAIL</a></li>
        <li><a href="WA" target="_blank" rel="noopener">WhatsApp</a></li>
        <li>Lun–Ven · 8h–18h</li>
      </ul>
    </div>
  </div>
  <div class="footer-bottom">
    <span class="footer-services-line">
      Pieux · Micropieux · Tirants d'ancrage · Clouage · Béton projeté
    </span>
    <span>© <span data-year>2026</span> G3FSP — Fondations Spéciales &amp; Géotechnique ·
      <a href="/mentions-legales/">Mentions légales</a></span>
  </div>
</footer>

<a class="wa-float" href="WA" target="_blank" rel="noopener"
   aria-label="Nous écrire sur WhatsApp">
  <svg width="26" height="26" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
    <path d="M17.47 14.38c-.3-.15-1.75-.86-2.02-.96-.27-.1-.47-.15-.67.15-.2.3-.77.96-.94 1.16-.17.2-.35.22-.64.07-.3-.15-1.25-.46-2.38-1.47-.88-.78-1.47-1.75-1.64-2.05-.17-.3-.02-.46.13-.6.13-.14.3-.35.45-.52.15-.17.2-.3.3-.5.1-.2.05-.37-.02-.52-.08-.15-.67-1.6-.92-2.2-.24-.58-.49-.5-.67-.5h-.57c-.2 0-.52.07-.79.37-.27.3-1.04 1.01-1.04 2.47s1.06 2.86 1.21 3.06c.15.2 2.1 3.2 5.08 4.49.71.3 1.26.49 1.69.63.71.22 1.36.19 1.87.12.57-.09 1.75-.72 2-1.41.25-.69.25-1.28.17-1.41-.07-.13-.27-.2-.57-.35zM12.05 21.5h-.01a9.4 9.4 0 0 1-4.79-1.31l-.35-.2-3.56.93.95-3.47-.22-.36a9.38 9.38 0 0 1-1.44-5.01c0-5.18 4.22-9.4 9.42-9.4a9.35 9.35 0 0 1 6.65 2.76 9.32 9.32 0 0 1 2.76 6.65c0 5.18-4.22 9.41-9.41 9.41zM20.52 3.49A11.78 11.78 0 0 0 12.05 0C5.5 0 .18 5.32.17 11.86c0 2.09.55 4.13 1.59 5.93L.07 24l6.35-1.66a11.87 11.87 0 0 0 5.67 1.44h.01c6.54 0 11.87-5.32 11.87-11.86 0-3.17-1.23-6.15-3.47-8.39z"/>
  </svg>
</a>
""".replace("TELRAW", TEL_RAW).replace("TELFMT", TEL_FMT).replace("MAIL", MAIL).replace("WA", WA)

TEMPLATE = """<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{site}{path}">

<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{site}/og/{og}.jpg">
<meta property="og:url" content="{site}{path}">
<meta property="og:locale" content="fr_MA">
<meta property="og:site_name" content="G3FSP — Fondations Spéciales Maroc">

<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{site}/og/{og}.jpg">

<meta name="geo.region" content="MA">
<meta name="geo.placename" content="{placename}">
<meta name="geo.position" content="{geopos}">
<meta name="ICBM" content="{icbm}">
<meta name="theme-color" content="#1A1A1A">

<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/icons/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="/icons/apple-touch-icon.png">

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:ital,wght@0,600;0,700;1,600&family=IBM+Plex+Sans:wght@400;500;600&display=swap" rel="stylesheet">

<link rel="stylesheet" href="/css/brand.css">
<link rel="stylesheet" href="/css/page.css">
{schema}
</head>

<body class="page">
<a class="skip-link" href="#contenu">Aller au contenu principal</a>

{header}

<main id="contenu">

<section class="page-hero trame">
  <div class="wrap">
    {breadcrumb}
    <span class="eyebrow">{eyebrow}</span>
    <h1>{h1}</h1>
    <p class="page-hero__lead">{lead}</p>
    <div class="page-hero__actions">
      <a class="btn btn--primary" href="/contact/">
        {cta_label} <span class="btn__arrow" aria-hidden="true">&rarr;</span>
      </a>
      <a class="btn btn--ghost-invert" href="tel:{tel_raw}">{tel_fmt}</a>
    </div>
  </div>
</section>

{body}

{cta}
</main>

{footer}

<script src="/js/site.js"></script>
</body>
</html>
"""


def breadcrumb_html(crumbs):
    """crumbs = [(label, href|None), ...] — le dernier élément est la page courante."""
    items = []
    for label, href in crumbs:
        if href:
            items.append('<li><a href="%s">%s</a></li>' % (href, label))
        else:
            items.append('<li><span aria-current="page">%s</span></li>' % label)
    return ('<nav class="breadcrumb" aria-label="Fil d\'Ariane">\n'
            '      <ol>%s</ol>\n    </nav>' % "".join(items))


def render(page):
    nav_keys = {"cur_services": "", "cur_real": "", "cur_zones": "",
                "cur_apropos": "", "cur_contact": ""}
    if page.get("nav"):
        nav_keys[page["nav"]] = ' aria-current="page"'

    schemas = page.get("schema", [])
    schema_html = "\n".join(
        '<script type="application/ld+json">\n%s\n</script>'
        % json.dumps(s, ensure_ascii=False, indent=2) for s in schemas
    )

    cta = page.get("cta_band")
    cta_html = CTA_BAND.format(**cta) if cta else ""

    html = TEMPLATE.format(
        title=page["title"],
        desc=page["desc"],
        robots=page.get("robots", "index, follow"),
        site=SITE,
        path=page["path"],
        og=page.get("og", "accueil"),
        placename=page.get("placename", "Casablanca"),
        geopos=page.get("geopos", "33.5731;-7.5898"),
        icbm=page.get("icbm", "33.5731, -7.5898"),
        schema=schema_html,
        header=HEADER.format(**nav_keys),
        breadcrumb=breadcrumb_html(page["crumbs"]),
        eyebrow=page["eyebrow"],
        h1=page["h1"],
        lead=page["lead"],
        cta_label=page.get("cta_label", "Demander un devis gratuit"),
        tel_raw=TEL_RAW,
        tel_fmt=TEL_FMT,
        body=page["body"],
        cta=cta_html,
        footer=FOOTER,
    )

    out_dir = os.path.join(ROOT, page["path"].strip("/").replace("/", os.sep))
    if page["path"] == "/404.html":
        out_path = os.path.join(ROOT, "404.html")
    else:
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "index.html")

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    return out_path


# ---------------------------------------------------------------------------
# Contenu des pages
# ---------------------------------------------------------------------------

from content import PAGES  # noqa: E402

if __name__ == "__main__":
    written = [render(p) for p in PAGES]
    print("%d pages générées :" % len(written))
    for w in written:
        print("  " + os.path.relpath(w, ROOT))
