#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
G3FSP — Constantes et générateurs de données structurées.
Importé à la fois par build.py (gabarits) et content.py (contenu).
"""

SITE = "https://www.g3fsp.com"

TEL_RAW = "+212661455673"
TEL_FMT = "+212 661 455 673"
MAIL = "soufiane.nidlahadj@g3fsp.ma"
WA = "https://wa.me/212661455673"


def breadcrumb_schema(crumbs):
    """crumbs = [(label, href|None), ...]"""
    elements = []
    for pos, (label, href) in enumerate(crumbs, start=1):
        item = {"@type": "ListItem", "position": pos, "name": label}
        if href:
            item["item"] = SITE + href
        elements.append(item)
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": elements,
    }


def service_schema(name, description):
    return {
        "@context": "https://schema.org",
        "@type": "Service",
        "name": name,
        "provider": {
            "@type": "LocalBusiness",
            "name": "G3FSP",
            "telephone": TEL_RAW,
            "url": SITE,
        },
        "areaServed": "MA",
        "description": description,
    }


def faq_schema(pairs):
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": a},
            }
            for q, a in pairs
        ],
    }


def faq_block(pairs, num, heading):
    """Rend la FAQ visible sur la page.

    Google exige que le contenu déclaré en FAQPage soit visible par
    l'utilisateur : ce bloc et le schéma sont générés depuis la même source.
    """
    items = "\n".join(
        """      <div class="faq-item" data-reveal>
        <h3>%s</h3>
        <p>%s</p>
      </div>""" % (q, a)
        for q, a in pairs
    )
    return """
<section class="band band--pale">
  <div class="wrap wrap--narrow">
    <div class="section-head" data-reveal>
      <span class="sec-num">%s /</span>
      <h2>%s</h2>
    </div>
    <div class="faq">
%s
    </div>
  </div>
</section>
""" % (num, heading, items)
