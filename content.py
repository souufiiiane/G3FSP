#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
G3FSP — Contenu rédactionnel des pages intérieures.

Toutes les données techniques et chiffrées proviennent des documents
sources G3FSP (plaquette commerciale + brochure trifold).
"""

from common import (breadcrumb_schema, service_schema, faq_schema, faq_block,
                    TEL_RAW, TEL_FMT, MAIL, WA)

# ===========================================================================
# FAQ — source unique pour le schéma FAQPage ET le bloc visible.
# Google exige que le contenu déclaré en FAQPage soit visible sur la page.
# ===========================================================================

FAQ_MICRO = [
    ("Qu'est-ce qu'un micropieu ?",
     "Un micropieu est un élément de fondation profonde de petit diamètre "
     "(100 à 300 mm), foré puis injecté au coulis de ciment. Il transfère les "
     "charges de l'ouvrage vers des couches de sol résistantes, même en terrain "
     "difficile ou en espace exigu."),
    ("Quelle est la différence entre un pieu et un micropieu ?",
     "Le pieu foré est de grand diamètre (jusqu'à 1200 mm chez G3FSP) et reprend "
     "des charges très importantes pour les ouvrages d'art et les bâtiments de "
     "grande hauteur. Le micropieu, de 100 à 300 mm, s'emploie lorsque l'accès "
     "est contraint, sur ouvrage existant, ou en sol hétérogène."),
    ("Peut-on réaliser des micropieux sous un bâtiment existant ?",
     "Oui. C'est l'un des principaux usages du micropieu : la reprise en "
     "sous-œuvre. Le faible encombrement des machines d'ancrage permet de "
     "travailler en sous-sol ou à l'intérieur d'un bâtiment occupé, avec des "
     "hauteurs libres réduites."),
    ("Quelle profondeur peut atteindre un micropieu ?",
     "La profondeur dépend de la stratigraphie et de la position de l'horizon "
     "porteur, pas d'une limite technique fixe. Sur nos chantiers récents, nous "
     "avons exécuté des éléments de 5 à plus de 20 mètres. C'est l'étude "
     "géotechnique qui fixe la profondeur d'ancrage nécessaire."),
    ("Combien de temps prend un chantier de micropieux ?",
     "La cadence dépend du nombre d'éléments, du diamètre, de la nature du "
     "terrain et de l'accessibilité du site. Un chantier de quelques dizaines "
     "d'unités se traite généralement en quelques semaines. Nous remettons un "
     "planning d'exécution détaillé avec notre proposition."),
]

FAQ_TIRANTS = [
    ("Quelle est la différence entre un tirant actif et un tirant passif ?",
     "Un tirant actif est mis en tension après scellement : il exerce "
     "immédiatement un effort sur le terrain et limite les déformations avant "
     "qu'elles n'apparaissent. Un tirant passif n'est pas précontraint : il ne "
     "travaille que lorsque le terrain se déplace et vient le solliciter."),
    ("Qu'est-ce qu'une berlinoise tirantée ?",
     "C'est une paroi de soutènement composée de profilés verticaux et de "
     "blindage, reprise par des lits de tirants d'ancrage. Elle permet de "
     "réaliser des fouilles profondes en site urbain contraint sans étaiement "
     "encombrant en fond de fouille."),
    ("Quelles normes s'appliquent aux tirants d'ancrage ?",
     "L'exécution des tirants d'ancrage relève de la norme EN 1537. Le "
     "dimensionnement des éléments en béton armé associés se réfère aux règles "
     "BAEL, et les vérifications sismiques au règlement marocain RPS 2011."),
    ("Un tirant d'ancrage est-il définitif ou provisoire ?",
     "Les deux existent. Un tirant provisoire assure la stabilité pendant la "
     "durée des travaux et n'est plus sollicité ensuite. Un tirant permanent "
     "reste en service pendant toute la vie de l'ouvrage et exige une protection "
     "anticorrosion renforcée. Le choix relève du marché et de la note de calcul."),
    ("Comment vérifie-t-on qu'un tirant tient sa charge ?",
     "Par des essais de réception réalisés au vérin avant mise en service. On "
     "applique une charge d'épreuve supérieure à la charge de service et l'on "
     "mesure le déplacement de la tête. Chaque tirant fait par ailleurs l'objet "
     "d'une fiche d'exécution consignant longueurs, volumes et pressions."),
    ("Quelle différence entre clouage et tirant d'ancrage ?",
     "Le clouage met en œuvre des inclusions passives rapprochées qui renforcent "
     "un massif de sol dans son ensemble, généralement avec un parement en béton "
     "projeté. Le tirant d'ancrage est un élément unitaire, souvent précontraint, "
     "qui reprend un effort concentré vers une couche résistante éloignée."),
]

FAQ_BETON = [
    ("Quelle est la différence entre la voie sèche et la voie humide ?",
     "En voie sèche, le mélange sec est transporté par air comprimé et l'eau est "
     "ajoutée à la lance au moment de la projection. En voie humide, le béton est "
     "déjà malaxé avec son eau et pompé jusqu'à la lance. La voie sèche offre plus "
     "de souplesse pour les petits volumes et les arrêts fréquents ; la voie humide "
     "donne de meilleurs rendements et moins de poussière."),
    ("Le béton projeté nécessite-t-il un coffrage ?",
     "Non. C'est son principal avantage : il permet de bétonner des surfaces "
     "verticales, inclinées ou en voûte sans coffrage traditionnel, ce qui réduit "
     "les délais et permet d'épouser des géométries irrégulières."),
    ("Qu'est-ce que le rebond, et comment le limiter ?",
     "Le rebond est la fraction du matériau qui ne adhère pas à la surface et "
     "retombe au sol. Il dépend de la distance et de l'angle de projection, de la "
     "granulométrie et du dosage en eau. Une lance tenue perpendiculairement à la "
     "paroi, à bonne distance, réduit sensiblement les pertes."),
    ("Le béton projeté peut-il être armé ?",
     "Oui. Il est couramment mis en œuvre sur treillis soudé, ou formulé avec des "
     "fibres métalliques ou synthétiques incorporées au mélange. Le choix dépend "
     "de la géométrie de la surface et des sollicitations prévues."),
    ("Dans quel délai le béton projeté est-il résistant ?",
     "C'est l'un de ses intérêts : la montée en résistance est rapide, ce qui "
     "permet une mise en sécurité quasi immédiate d'une paroi fraîchement "
     "excavée. Des adjuvants accélérateurs peuvent renforcer cet effet lorsque "
     "la cadence du chantier l'exige."),
]

# ===========================================================================
# Blocs réutilisables
# ===========================================================================

EQUIPEMENTS_BAND = """
<section class="band band--dark trame">
  <div class="wrap">
    <div class="section-head" data-reveal>
      <span class="sec-num">%s /</span>
      <h2>Notre parc <span class="accent">matériel</span></h2>
      <p>Des équipements de pointe pour garantir performance et précision sur
         tous nos chantiers de fondations spéciales.</p>
    </div>
    <div class="grid grid--3">
      <div class="card" data-reveal>
        <div class="card__num">01</div>
        <h3>Machines de forage</h3>
        <p>Machine de forage de diamètre jusqu'à <strong>1200 mm</strong> pour les
           travaux majeurs : pieux de grand diamètre, ouvrages d'art et
           infrastructures lourdes.</p>
      </div>
      <div class="card" data-reveal>
        <div class="card__num">02</div>
        <h3>Machines d'ancrage</h3>
        <p>Machine d'ancrage <strong>petit diamètre</strong> adaptée aux espaces
           contraints : sous-sols, intérieurs de bâtiments existants, accès
           difficiles.</p>
      </div>
      <div class="card" data-reveal>
        <div class="card__num">03</div>
        <h3>Injection &amp; bétonnage</h3>
        <p>Équipements performants dédiés aux opérations d'<strong>injection</strong>
           et de <strong>bétonnage</strong>, ainsi que compresseurs haute pression
           pour la projection de béton.</p>
      </div>
    </div>
  </div>
</section>
"""

AUTRES_SERVICES = """
<section class="band band--pale">
  <div class="wrap">
    <div class="section-head" data-reveal>
      <span class="sec-num">%s /</span>
      <h2>Nos autres <span class="accent">solutions</span></h2>
    </div>
    <div class="grid grid--2">
      %s
    </div>
  </div>
</section>
"""

CARD_MICRO = """<a class="card" href="/services/micropieux/" data-reveal>
        <h3>Pieux &amp; Micropieux</h3>
        <p>Fondations profondes pour transférer les charges vers les couches
           résistantes : pieux forés de grand diamètre et micropieux injectés
           de 100 à 300 mm.</p>
        <span class="card__link">Découvrir <span aria-hidden="true">&rarr;</span></span>
      </a>"""

CARD_TIRANTS = """<a class="card" href="/services/tirants-ancrage/" data-reveal>
        <h3>Tirants d'ancrage &amp; Clouage</h3>
        <p>Reprise d'efforts de traction pour le soutènement de parois, la
           stabilisation de talus et les berlinoises tirantées.</p>
        <span class="card__link">Découvrir <span aria-hidden="true">&rarr;</span></span>
      </a>"""

CARD_BETON = """<a class="card" href="/services/beton-projete/" data-reveal>
        <h3>Béton projeté</h3>
        <p>Projection pneumatique pour le confortement de parois, les tunnels,
           les bassins et la réparation structurale d'ouvrages en béton.</p>
        <span class="card__link">Découvrir <span aria-hidden="true">&rarr;</span></span>
      </a>"""

ZONES_BAND = """
<section class="band band--dark trame">
  <div class="wrap">
    <div class="section-head" data-reveal>
      <span class="sec-num">%s /</span>
      <h2>Où nous <span class="accent">intervenons</span></h2>
      <p>Basés à Casablanca, nos équipes et nos équipements se déplacent sur
         l'ensemble du territoire marocain.</p>
    </div>
    <ul class="city-list" data-reveal>
      <li><a href="/zones-intervention/casablanca/"><span class="idx">01</span> Casablanca</a></li>
      <li><a href="/zones-intervention/rabat/"><span class="idx">02</span> Rabat</a></li>
      <li><a href="/zones-intervention/tanger/"><span class="idx">03</span> Tanger</a></li>
      <li><a href="/zones-intervention/marrakech/"><span class="idx">04</span> Marrakech</a></li>
      <li><a href="/zones-intervention/agadir/"><span class="idx">05</span> Agadir</a></li>
      <li><a href="/zones-intervention/"><span class="idx">06</span> Nador</a></li>
    </ul>
  </div>
</section>
"""

# ===========================================================================
# PAGES
# ===========================================================================

PAGES = []

# ---------------------------------------------------------------------------
# /services/
# ---------------------------------------------------------------------------

PAGES.append({
    "path": "/services/",
    "nav": "cur_services",
    "og": "services",
    "title": "Nos Services — Fondations Spéciales &amp; Géotechnique | G3FSP",
    "desc": "Pieux forés, micropieux, tirants d'ancrage, clouage et béton projeté. "
            "G3FSP exécute vos travaux de fondations spéciales partout au Maroc.",
    "eyebrow": "Expertise &amp; Solutions",
    "h1": "Nos services de <span class=\"accent\">fondations spéciales</span>",
    "lead": "Une gamme complète de techniques d'exécution pour les fondations "
            "profondes, le soutènement et le confortement d'ouvrages — mises en "
            "œuvre par nos équipes sur l'ensemble du territoire marocain.",
    "cta_label": "Étudier votre projet",
    "crumbs": [("Accueil", "/"), ("Services", None)],
    "schema": [breadcrumb_schema([("Accueil", "/"), ("Services", "/services/")])],
    "cta_band": {
        "num": "006",
        "title": "Un terrain, une <span class=\"accent\">solution</span>",
        "text": "Décrivez-nous votre ouvrage, vos contraintes de sol et vos délais. "
                "Nos ingénieurs reviennent vers vous avec une proposition technique "
                "et un chiffrage sous 48 heures.",
    },
    "body": """
<section class="band">
  <div class="wrap">
    <div class="prose" data-reveal>
      <p>
        <strong>G3FSP</strong> est une entreprise de <strong>travaux</strong> de
        fondations spéciales. Nous n'intervenons pas seulement en étude : nous
        exécutons sur le terrain, en coordination avec le bureau d'études
        géotechnique et la maîtrise d'œuvre, les ouvrages qui ancrent votre
        projet dans le sol.
      </p>
      <p>
        Nos cinq spécialités couvrent l'ensemble du cycle : reprendre une charge
        en profondeur, retenir un terrain qui pousse, ou conforter une paroi
        existante. Chaque technique répond à une contrainte de sol précise —
        et c'est le sol qui décide.
      </p>
    </div>
  </div>
</section>

<section class="band band--pale">
  <div class="wrap">
    <div class="section-head" data-reveal>
      <span class="sec-num">002 /</span>
      <h2>Cinq <span class="accent">spécialités</span></h2>
    </div>
    <div class="grid grid--3">
      <a class="card" href="/services/micropieux/" data-reveal>
        <div class="card__num">01</div>
        <h3>Pieux forés</h3>
        <p>Pieux de grand diamètre pour ouvrages d'art, ponts, bâtiments de
           grande hauteur et infrastructures lourdes. Réalisés par forage
           mécanique — tarière continue ou tubage — ils offrent une capacité
           portante maximale.</p>
        <span class="card__link">En savoir plus <span aria-hidden="true">&rarr;</span></span>
      </a>
      <a class="card" href="/services/micropieux/" data-reveal>
        <div class="card__num">02</div>
        <h3>Micropieux</h3>
        <p>Fondation profonde de petit diamètre (100 à 300 mm), forée et injectée
           au coulis de ciment. Transfère les charges vers les couches résistantes
           même en terrain difficile ou en espace exigu.</p>
        <span class="card__link">En savoir plus <span aria-hidden="true">&rarr;</span></span>
      </a>
      <a class="card" href="/services/tirants-ancrage/" data-reveal>
        <div class="card__num">03</div>
        <h3>Tirants d'ancrage</h3>
        <p>Transmission d'efforts de traction importants vers une couche
           résistante. Actifs ou passifs, ils servent au soutènement de parois
           et à la stabilisation de talus.</p>
        <span class="card__link">En savoir plus <span aria-hidden="true">&rarr;</span></span>
      </a>
      <a class="card" href="/services/tirants-ancrage/" data-reveal>
        <div class="card__num">04</div>
        <h3>Clouage</h3>
        <p>Clouage de sol et parois clouées pour sécuriser fouilles, talus et
           terrains en zones contraintes. Souvent associé au béton projeté pour
           former un parement continu.</p>
        <span class="card__link">En savoir plus <span aria-hidden="true">&rarr;</span></span>
      </a>
      <a class="card" href="/services/beton-projete/" data-reveal>
        <div class="card__num">05</div>
        <h3>Béton projeté</h3>
        <p>Projection pneumatique à haute vitesse permettant de bétonner des
           surfaces verticales, inclinées ou en voûte sans coffrage
           traditionnel.</p>
        <span class="card__link">En savoir plus <span aria-hidden="true">&rarr;</span></span>
      </a>
      <a class="card" href="/contact/" data-reveal>
        <div class="card__num">06</div>
        <h3>Étude sur mesure</h3>
        <p>Un terrain particulier, une contrainte d'accès, un ouvrage existant à
           renforcer ? Nos ingénieurs étudient votre cas et vous chiffrent
           l'intervention sous 48 heures.</p>
        <span class="card__link">Nous contacter <span aria-hidden="true">&rarr;</span></span>
      </a>
    </div>
  </div>
</section>

<section class="band">
  <div class="wrap">
    <div class="section-head" data-reveal>
      <span class="sec-num">003 /</span>
      <h2>Domaines d'<span class="accent">application</span></h2>
      <p>Nos techniques s'adressent à quatre grandes familles d'ouvrages.</p>
    </div>
    <div class="grid grid--4">
      <div class="card" data-reveal>
        <h3>Bâtiments</h3>
        <p>Résidentiel &amp; tertiaire — fondations profondes de immeubles,
           tours et ensembles collectifs.</p>
      </div>
      <div class="card" data-reveal>
        <h3>Ouvrages existants</h3>
        <p>Renforcement &amp; réhabilitation — reprise en sous-œuvre,
           confortement de structures dégradées.</p>
      </div>
      <div class="card" data-reveal>
        <h3>Talus &amp; terrains</h3>
        <p>Zones contraintes &amp; difficiles — stabilisation de pentes,
           soutènement de fouilles profondes.</p>
      </div>
      <div class="card" data-reveal>
        <h3>Industriel &amp; urbain</h3>
        <p>Grands projets &amp; infrastructures — ouvrages d'art, tunnels,
           équipements sportifs.</p>
      </div>
    </div>
  </div>
</section>
""" + (EQUIPEMENTS_BAND % "004") + (ZONES_BAND % "005"),
})

# ---------------------------------------------------------------------------
# /services/micropieux/
# ---------------------------------------------------------------------------

PAGES.append({
    "path": "/services/micropieux/",
    "nav": "cur_services",
    "og": "micropieux",
    "title": "Micropieux au Maroc — Fondations Profondes | G3FSP",
    "desc": "G3FSP réalise des micropieux (type I à IV) adaptés à tous types de sols "
            "marocains : transfert de charges, reprise en sous-œuvre, zones "
            "difficiles d'accès.",
    "eyebrow": "002 / Pieux &amp; Micropieux",
    "h1": "Micropieux &amp; pieux : <span class=\"accent\">fondations profondes</span> au Maroc",
    "lead": "Transférer les charges d'un ouvrage vers les couches de sol résistantes, "
            "même en terrain difficile ou en espace exigu. C'est le cœur du métier "
            "de G3FSP.",
    "cta_label": "Étudier votre projet avec nos ingénieurs",
    "crumbs": [("Accueil", "/"), ("Services", "/services/"), ("Micropieux", None)],
    "schema": [
        breadcrumb_schema([("Accueil", "/"), ("Services", "/services/"),
                           ("Micropieux", "/services/micropieux/")]),
        service_schema("Micropieux au Maroc",
                       "Réalisation de micropieux de type I à IV pour fondations "
                       "profondes au Maroc."),
        faq_schema(FAQ_MICRO),
    ],
    "cta_band": {
        "num": "008",
        "title": "Étudier votre projet de <span class=\"accent\">fondations</span>",
        "text": "Transmettez-nous votre rapport géotechnique et les descentes de "
                "charges : nos ingénieurs vous proposent une méthode d'exécution "
                "et un chiffrage sous 48 heures.",
    },
    "body": """
<section class="band">
  <div class="wrap">
    <div class="prose" data-reveal>
      <h2>Qu'est-ce qu'un micropieu ?</h2>
      <p>
        Le <strong>micropieu</strong> est un élément de fondation profonde de petit
        diamètre — généralement <strong>100 à 300 mm</strong> — foré puis injecté au
        coulis de ciment. Il transfère les charges de l'ouvrage vers des couches de
        sol résistantes situées en profondeur, même lorsque le terrain de surface
        est médiocre, hétérogène, ou lorsque l'espace de travail est exigu.
      </p>
      <p>
        Son intérêt tient à trois propriétés : un <strong>encombrement réduit</strong>
        qui permet d'intervenir là où une foreuse classique ne passe pas ; une
        <strong>faible vibration</strong> à la mise en œuvre, essentielle à proximité
        de structures existantes ; et une <strong>adaptabilité</strong> à presque
        tous les types de sols grâce aux techniques d'injection.
      </p>

      <h2>Pieux forés de grand diamètre</h2>
      <p>
        Lorsque les charges à reprendre sont considérables, le
        <strong>pieu foré de grand diamètre</strong> reste la solution de référence.
        Idéal pour les <strong>ouvrages d'art</strong>, les <strong>ponts</strong>,
        les <strong>bâtiments de grande hauteur</strong> et les infrastructures
        lourdes, il est réalisé par forage mécanique — tarière continue ou tubage
        selon la tenue du terrain — et offre une capacité portante maximale ainsi
        qu'une reprise de charge exceptionnelle.
      </p>
      <p>
        Notre parc comprend une machine de forage permettant d'atteindre des
        diamètres jusqu'à <strong>1200 mm</strong>. Sur nos chantiers récents à
        Tanger, nous avons exécuté des pieux Ø 800 mm à des profondeurs comprises
        entre 5,70 m et 20,50 m.
      </p>

      <div class="callout">
        <p class="callout__title">Pieu ou micropieu ?</p>
        <p>
          Le choix ne se fait jamais dans l'absolu. Il dépend de la descente de
          charges, de la stratigraphie révélée par l'étude géotechnique, de
          l'accessibilité du site et de la proximité d'avoisinants sensibles.
          Nous étudions les deux hypothèses avec votre bureau d'études.
        </p>
      </div>
    </div>
  </div>
</section>

<section class="band band--pale">
  <div class="wrap">
    <div class="section-head" data-reveal>
      <span class="sec-num">003 /</span>
      <h2>Les 4 types de <span class="accent">micropieux</span></h2>
      <p>
        La classification française (DTU 13.2 / NF P 94-262) distingue quatre types
        de micropieux selon leur mode de scellement et d'injection.
      </p>
    </div>

    <div class="grid grid--4">
      <div class="card" data-reveal>
        <div class="card__num">I</div>
        <h3>Foré simple</h3>
        <p>Sans tubage, injection globale. Scellement du coulis par gravité.
           Réservé aux <strong>sols cohérents stables</strong>, qui tiennent
           naturellement à la paroi du forage.</p>
      </div>
      <div class="card" data-reveal>
        <div class="card__num">II</div>
        <h3>Foré tubé</h3>
        <p>Tubage provisoire, injection globale. Le tube soutient le forage
           pendant l'exécution puis est retiré. Convient à
           <strong>tous types de sols</strong>.</p>
      </div>
      <div class="card" data-reveal>
        <div class="card__num">III</div>
        <h3>IGU — injection globale unitaire</h3>
        <p>Armature équipée d'un tube à manchettes. Injection sous
           <strong>haute pression en une seule passe</strong> sur toute la
           longueur de scellement. Portance nettement supérieure.</p>
      </div>
      <div class="card" data-reveal>
        <div class="card__num">IV</div>
        <h3>IRS — injection répétitive sélective</h3>
        <p>Tube à manchettes également, mais l'injection est
           <strong>répétée et sélective</strong>, passe par passe. Permet de
           traiter précisément les horizons les plus porteurs.</p>
      </div>
    </div>

    <div class="callout" data-reveal style="margin-top:2.5rem;max-width:68ch">
      <p>
        Sur nos chantiers, les <strong>types I et II</strong> couvrent la majorité
        des besoins courants. Les types III et IV sont mobilisés lorsque la
        portance visée l'exige ou lorsque le terrain nécessite un traitement
        d'injection maîtrisé horizon par horizon.
      </p>
    </div>
  </div>
</section>

<section class="band">
  <div class="wrap">
    <div class="section-head" data-reveal>
      <span class="sec-num">004 /</span>
      <h2>Dans quels cas utilise-t-on un <span class="accent">micropieu</span> ?</h2>
    </div>
    <div class="grid grid--2">
      <div class="card" data-reveal>
        <h3>Reprise en sous-œuvre</h3>
        <p>
          Renforcer les fondations d'un bâtiment existant qui tasse, ou reprendre
          les charges avant un surélèvement ou un creusement de sous-sol.
          L'encombrement réduit des machines d'ancrage permet de travailler à
          l'intérieur, en site occupé, avec des hauteurs libres limitées.
        </p>
      </div>
      <div class="card" data-reveal>
        <h3>Zone sismique</h3>
        <p>
          Le Maroc est soumis au règlement parasismique <strong>RPS 2011</strong>.
          Dans les zones d'aléa élevé, les micropieux permettent d'assurer
          l'ancrage de l'ouvrage dans un horizon stable et de reprendre les
          efforts horizontaux induits par un séisme.
        </p>
      </div>
      <div class="card" data-reveal>
        <h3>Sol hétérogène</h3>
        <p>
          Remblais anciens, poches de sol compressible, substratum irrégulier :
          lorsque la portance varie fortement d'un point à l'autre de l'emprise,
          le micropieu va chercher individuellement la couche résistante.
        </p>
      </div>
      <div class="card" data-reveal>
        <h3>Réhabilitation</h3>
        <p>
          Ouvrages patrimoniaux, structures dégradées, bâtiments à conserver :
          la faible vibration de la mise en œuvre protège les maçonneries
          fragiles. C'est la technique que nous avons employée à la
          <a href="/realisations/mosquee-tinmel/">Mosquée de Tinmel</a>.
        </p>
      </div>
    </div>
  </div>
</section>

<section class="band band--dark trame">
  <div class="wrap">
    <div class="section-head" data-reveal>
      <span class="sec-num">005 /</span>
      <h2>Notre processus d'<span class="accent">exécution</span></h2>
      <p>Cinq étapes, du dossier technique à la réception des travaux.</p>
    </div>
    <div class="prose" style="max-width:72ch;color:var(--gris-clair)" data-reveal>
      <ol>
        <li>
          <strong style="color:var(--blanc-chantier)">Analyse du dossier géotechnique.</strong>
          Lecture du rapport de sol, des descentes de charges et des contraintes
          d'accès. Choix du type de micropieu et de la méthode de forage.
        </li>
        <li>
          <strong style="color:var(--blanc-chantier)">Implantation et installation.</strong>
          Piquetage topographique, amenée du matériel, mise en place des
          protections et des accès. Vérification des réseaux enterrés.
        </li>
        <li>
          <strong style="color:var(--blanc-chantier)">Forage.</strong>
          Réalisation du forage au diamètre et à la profondeur prescrits, avec
          ou sans tubage selon la tenue du terrain. Relevé des paramètres de
          forage.
        </li>
        <li>
          <strong style="color:var(--blanc-chantier)">Armature et injection.</strong>
          Mise en place de l'armature, puis injection du coulis de ciment selon
          le type retenu (gravitaire, IGU ou IRS). Contrôle des volumes et des
          pressions.
        </li>
        <li>
          <strong style="color:var(--blanc-chantier)">Recépage et contrôle.</strong>
          Recépage en tête, essais de contrôle si prescrits, et remise du
          dossier d'exécution avec les fiches de forage.
        </li>
      </ol>
    </div>
  </div>
</section>

<section class="band">
  <div class="wrap">
    <div class="section-head" data-reveal>
      <span class="sec-num">006 /</span>
      <h2>Micropieux et types de sols <span class="accent">marocains</span></h2>
    </div>
    <div class="prose" data-reveal>
      <p>
        La géologie du Royaume est loin d'être uniforme, et c'est précisément ce
        qui rend l'expérience terrain déterminante. Nous intervenons
        principalement sur trois familles de contextes :
      </p>
      <ul>
        <li>
          <strong>Sols argileux</strong> — fréquents dans la région de Casablanca
          et sur les plaines côtières. Sensibles aux variations de teneur en eau,
          ils imposent d'aller chercher un horizon porteur plus profond plutôt que
          de fonder superficiellement.
        </li>
        <li>
          <strong>Calcaires et substratums rocheux</strong> — bonne portance mais
          irrégularité du toit rocheux et risque de karst. Le micropieu s'ancre
          individuellement, ce qui absorbe la variabilité du niveau d'assise.
        </li>
        <li>
          <strong>Terrains difficiles et hétérogènes</strong> — remblais, éboulis,
          marnes altérées, versants instables. C'est le domaine où le choix du type
          de micropieu et de la méthode d'injection fait toute la différence.
        </li>
      </ul>
      <p class="pull-quote">
        « Chaque fondation est invisible. Notre travail, lui, dure des générations. »
      </p>
      <p>
        Consultez nos pages dédiées aux
        <a href="/zones-intervention/casablanca/">fondations spéciales à Casablanca</a>,
        <a href="/zones-intervention/tanger/">à Tanger</a> ou
        <a href="/zones-intervention/marrakech/">à Marrakech</a> pour les
        spécificités géotechniques locales.
      </p>
    </div>
  </div>
</section>

<section class="band band--pale">
  <div class="wrap">
    <div class="section-head" data-reveal>
      <span class="sec-num">007 /</span>
      <h2>Nos réalisations en <span class="accent">micropieux</span></h2>
    </div>
    <div class="grid grid--3">
      <div class="card" data-reveal>
        <h3>Stade Boukhalef</h3>
        <p><strong>Tanger</strong> — Complexe sportif.<br>
           155 micropieux Ø 300 mm (5,20 m) et 20 pieux Ø 800 mm (14,00 m).</p>
      </div>
      <div class="card" data-reveal>
        <h3>Californie</h3>
        <p><strong>Tanger</strong> — Fondations profondes.<br>
           Pieux Ø 800 mm, profondeurs de 7,60 m à 20,50 m.</p>
      </div>
      <div class="card" data-reveal>
        <h3>El Balia</h3>
        <p><strong>Tanger</strong> — Fondations de bâtiment.<br>
           Pieux Ø 800 mm, profondeurs de 5,70 m à 12,00 m.</p>
      </div>
    </div>
    <p style="margin-top:2.5rem" data-reveal>
      <a class="btn btn--ghost" href="/realisations/">
        Toutes nos réalisations <span class="btn__arrow" aria-hidden="true">&rarr;</span>
      </a>
    </p>
  </div>
</section>

<section class="band">
  <div class="wrap">
    <div class="section-head" data-reveal>
      <span class="sec-num">007b /</span>
      <h2>Contrôle et <span class="accent">qualité d'exécution</span></h2>
    </div>
    <div class="prose" data-reveal>
      <p>
        Un micropieu est un ouvrage que personne ne reverra jamais. Une fois le
        recépage effectué et la dalle coulée, il n'existe plus que sous forme de
        documents. C'est pourquoi la <strong>traçabilité de l'exécution</strong>
        n'est pas un supplément administratif : c'est la seule preuve durable de
        ce qui a été réalisé.
      </p>

      <h3>La fiche de forage</h3>
      <p>
        Chaque élément fait l'objet d'une fiche consignant sa position, sa
        profondeur réelle, le diamètre exécuté, la nature des terrains traversés,
        le volume de coulis injecté et les pressions relevées. L'écart entre le
        volume théorique et le volume réellement injecté est un indicateur
        précieux : il signale les cavités, les terrains fracturés ou les zones de
        forte perméabilité rencontrées en cours de forage.
      </p>

      <h3>Les essais de contrôle</h3>
      <p>
        Lorsque le marché les prescrit, des <strong>essais de chargement
        statique</strong> permettent de vérifier expérimentalement la portance
        d'un élément témoin. Des méthodes de contrôle non destructif — essais
        d'impédance, contrôle par transparence sonique — peuvent également être
        mises en œuvre pour vérifier la continuité et l'intégrité du fût.
      </p>

      <h3>Le dossier d'exécution</h3>
      <p>
        À la réception, nous remettons un dossier réunissant le plan
        d'implantation avec les positions réellement exécutées, l'ensemble des
        fiches de forage, les bons de livraison du ciment, les résultats d'essais
        et les éventuelles fiches de non-conformité avec leur traitement. Ce
        dossier accompagne l'ouvrage tout au long de sa vie.
      </p>

      <div class="callout">
        <p class="callout__title">Notre rôle dans la chaîne</p>
        <p>
          G3FSP est une entreprise de <strong>travaux</strong>. Le
          dimensionnement relève du bureau d'études géotechnique et du bureau
          d'études structure ; nous intervenons sur la
          <strong>méthode d'exécution</strong>, la mise en œuvre et le contrôle
          de ce qui est réalisé. Cette répartition claire des responsabilités
          protège tout le monde — à commencer par le maître d'ouvrage.
        </p>
      </div>
    </div>
  </div>
</section>
""" + faq_block(FAQ_MICRO, "007c", "Questions <span class=\"accent\">fréquentes</span>")
   + (AUTRES_SERVICES % ("008b", CARD_TIRANTS + "\n      " + CARD_BETON)),
})

# ---------------------------------------------------------------------------
# /services/tirants-ancrage/
# ---------------------------------------------------------------------------

PAGES.append({
    "path": "/services/tirants-ancrage/",
    "nav": "cur_services",
    "og": "tirants-ancrage",
    "title": "Tirants d'Ancrage &amp; Clouage au Maroc | G3FSP",
    "desc": "Conception et installation de tirants d'ancrage actifs et passifs pour "
            "soutènement de parois, stabilisation de talus et reprise en sous-œuvre. "
            "Experts géotechniques au Maroc.",
    "eyebrow": "003 / Tirants d'ancrage &amp; Clouage",
    "h1": "Tirants d'ancrage &amp; <span class=\"accent\">clouage de sol</span> au Maroc",
    "lead": "Les tirants transmettent des efforts de traction importants vers une "
            "couche résistante. Actifs ou passifs, ils servent au soutènement de "
            "parois et à la stabilisation de talus.",
    "cta_label": "Demander une étude technique",
    "crumbs": [("Accueil", "/"), ("Services", "/services/"), ("Tirants d'ancrage", None)],
    "schema": [
        breadcrumb_schema([("Accueil", "/"), ("Services", "/services/"),
                           ("Tirants d'ancrage", "/services/tirants-ancrage/")]),
        service_schema("Tirants d'ancrage et clouage au Maroc",
                       "Installation de tirants d'ancrage actifs et passifs, clouage "
                       "de sol et berlinoises tirantées au Maroc."),
        faq_schema(FAQ_TIRANTS),
    ],
    "cta_band": {
        "num": "007",
        "title": "Sécuriser votre <span class=\"accent\">soutènement</span>",
        "text": "Fouille profonde, talus instable, paroi à reprendre : transmettez-nous "
                "votre note géotechnique. Nous vous proposons une solution d'ancrage "
                "chiffrée sous 48 heures.",
    },
    "body": """
<section class="band">
  <div class="wrap">
    <div class="prose" data-reveal>
      <h2>Tirant actif ou tirant passif ?</h2>
      <p>
        Un <strong>tirant d'ancrage</strong> est un élément linéaire scellé dans une
        couche de sol résistante, destiné à reprendre des efforts de
        <strong>traction</strong>. Toute la question est de savoir s'il doit
        travailler immédiatement ou seulement en cas de mouvement.
      </p>

      <h3>Le tirant actif (précontraint)</h3>
      <p>
        Après scellement, le tirant est <strong>mis en tension</strong> au vérin.
        Il exerce dès lors une force sur la structure de soutènement et
        <strong>limite les déformations avant qu'elles n'apparaissent</strong>.
        C'est la solution retenue lorsque les déplacements admissibles sont
        faibles — fouille en site urbain dense, proximité immédiate d'un bâtiment
        existant, ouvrage sensible.
      </p>

      <h3>Le tirant passif (clou)</h3>
      <p>
        Il n'est pas précontraint. Il ne se met à travailler que
        <strong>lorsque le terrain se déplace</strong> et vient le solliciter.
        Plus simple et plus économique, il convient à la stabilisation de talus
        et aux parois clouées, où de petits déplacements sont tolérables. C'est
        le principe du <strong>clouage</strong>.
      </p>

      <div class="callout">
        <p class="callout__title">Le clouage en pratique</p>
        <p>
          Le clouage consiste à renforcer un massif de sol par des inclusions
          passives rapprochées, généralement associées à un parement en
          <a href="/services/beton-projete/">béton projeté</a>. La paroi clouée
          se construit de haut en bas, par passes successives : on excave, on
          cloue, on projette, puis on descend d'un niveau.
        </p>
      </div>
    </div>
  </div>
</section>

<section class="band band--pale">
  <div class="wrap">
    <div class="section-head" data-reveal>
      <span class="sec-num">003 /</span>
      <h2>Applications : soutènement, <span class="accent">stabilisation de talus</span></h2>
    </div>
    <div class="grid grid--3">
      <div class="card" data-reveal>
        <div class="card__num">01</div>
        <h3>Soutènement</h3>
        <p>
          Maintien des parois d'une fouille profonde en site contraint. Les
          tirants reprennent la poussée des terres et permettent de dégager
          l'emprise du chantier — pas d'étaiement encombrant en fond de fouille.
        </p>
      </div>
      <div class="card" data-reveal>
        <div class="card__num">02</div>
        <h3>Stabilisation de talus</h3>
        <p>
          Renforcement de pentes naturelles ou de déblais instables. Les tirants
          traversent la surface de rupture potentielle et l'ancrent dans le
          massif stable en arrière.
        </p>
      </div>
      <div class="card" data-reveal>
        <div class="card__num">03</div>
        <h3>Berlinoise tirantée</h3>
        <p>
          Profilés verticaux, blindage entre profilés et lits de tirants
          d'ancrage. Solution de référence pour les fouilles urbaines profondes
          où l'emprise disponible est réduite.
        </p>
      </div>
    </div>

    <div class="prose" style="margin-top:3rem" data-reveal>
      <p>
        Les tirants trouvent également leur place en
        <strong>reprise en sous-œuvre</strong>, en complément des
        <a href="/services/micropieux/">micropieux</a>, lorsqu'il faut à la fois
        reprendre une charge verticale et retenir un terrain.
      </p>
    </div>
  </div>
</section>

<section class="band">
  <div class="wrap">
    <div class="section-head" data-reveal>
      <span class="sec-num">004 /</span>
      <h2>Normes <span class="accent">appliquées</span></h2>
    </div>
    <div class="prose" data-reveal>
      <p>
        L'ancrage est un ouvrage dont la ruine est brutale. Le respect du
        référentiel normatif n'est donc pas une formalité administrative :
        c'est la condition de la sécurité du chantier et de la pérennité de
        l'ouvrage.
      </p>
      <div class="table-wrap">
        <table class="tech">
          <caption>Référentiel appliqué sur nos chantiers d'ancrage</caption>
          <thead>
            <tr><th>Référence</th><th>Objet</th></tr>
          </thead>
          <tbody>
            <tr>
              <td>EN 1537</td>
              <td>Exécution des travaux géotechniques spéciaux — tirants d'ancrage.
                  Conception, matériaux, mise en œuvre, essais de réception.</td>
            </tr>
            <tr>
              <td>BAEL</td>
              <td>Dimensionnement des éléments en béton armé associés :
                  longrines, têtes d'ancrage, plaques de répartition.</td>
            </tr>
            <tr>
              <td>RPS 2011</td>
              <td>Règlement de construction parasismique marocain — vérification
                  du comportement de l'ouvrage sous sollicitation sismique.</td>
            </tr>
          </tbody>
        </table>
      </div>
      <p>
        Chaque tirant fait l'objet d'une <strong>fiche d'exécution</strong>
        (profondeur, longueur libre et longueur de scellement, volume de coulis,
        pression d'injection). Les <strong>essais de réception</strong> prescrits
        au marché sont réalisés avant mise en service.
      </p>
    </div>
  </div>
</section>
""" + (EQUIPEMENTS_BAND % "005") + """
<section class="band band--pale">
  <div class="wrap">
    <div class="section-head" data-reveal>
      <span class="sec-num">006 /</span>
      <h2>Projets <span class="accent">réalisés</span></h2>
    </div>
    <div class="grid grid--2">
      <a class="card" href="/realisations/mosquee-tinmel/" data-reveal>
        <h3>Mosquée de Tinmel</h3>
        <p>
          <strong>Haut Atlas</strong> — Restauration après le séisme d'Al Haouz
          de 2023. Tirants d'ancrage Ø 100 mm sur 12,00 m de profondeur,
          93 unités. Un chantier patrimonial en zone de montagne.
        </p>
        <span class="card__link">Lire l'étude de cas <span aria-hidden="true">&rarr;</span></span>
      </a>
      <a class="card" href="/realisations/" data-reveal>
        <h3>Autres chantiers</h3>
        <p>
          Retrouvez l'ensemble de nos réalisations en fondations spéciales à
          Tanger, Marrakech et sur le reste du territoire, avec le détail
          technique de chaque intervention.
        </p>
        <span class="card__link">Voir les réalisations <span aria-hidden="true">&rarr;</span></span>
      </a>
    </div>
  </div>
</section>

<section class="band">
  <div class="wrap">
    <div class="section-head" data-reveal>
      <span class="sec-num">006b /</span>
      <h2>Anatomie d'un <span class="accent">tirant d'ancrage</span></h2>
    </div>
    <div class="prose" data-reveal>
      <p>
        Un tirant se décompose en trois parties, et c'est cette géométrie qui
        conditionne tout son fonctionnement.
      </p>
      <ul>
        <li>
          <strong>La tête d'ancrage</strong> — située côté ouvrage, elle
          transmet l'effort à la structure de soutènement via une plaque de
          répartition. C'est aussi par elle que s'effectuent la mise en tension
          et les essais de réception.
        </li>
        <li>
          <strong>La longueur libre</strong> — la partie de l'armature qui n'est
          pas solidaire du terrain. Elle doit traverser intégralement la zone de
          sol susceptible de glisser, faute de quoi le tirant s'ancrerait dans le
          massif qu'il est censé retenir. C'est l'erreur de conception classique.
        </li>
        <li>
          <strong>La longueur de scellement</strong> — la partie injectée au
          coulis, solidaire du terrain résistant. C'est elle qui reprend
          effectivement l'effort, par frottement entre le coulis et le sol.
        </li>
      </ul>

      <h3>Protection contre la corrosion</h3>
      <p>
        Un tirant permanent travaille en traction pendant des décennies, souvent
        dans un environnement humide et parfois agressif. La
        <strong>protection anticorrosion</strong> — gaine, graisse, double
        protection selon la classe retenue — n'est donc pas un détail
        d'exécution : c'est ce qui détermine la durée de vie réelle de l'ouvrage.
        La norme EN 1537 définit les exigences applicables selon que le tirant
        est provisoire ou permanent.
      </p>
    </div>
  </div>
</section>

<section class="band band--dark trame">
  <div class="wrap">
    <div class="section-head" data-reveal>
      <span class="sec-num">006c /</span>
      <h2>Notre processus d'<span class="accent">exécution</span></h2>
      <p>Du forage à la réception, six étapes contrôlées.</p>
    </div>
    <div class="prose" style="max-width:72ch;color:var(--gris-clair)" data-reveal>
      <ol>
        <li>
          <strong style="color:var(--blanc-chantier)">Forage.</strong>
          Réalisation du forage à l'inclinaison et à la longueur prescrites.
          L'inclinaison est un paramètre sensible : quelques degrés d'écart
          déplacent significativement la zone de scellement.
        </li>
        <li>
          <strong style="color:var(--blanc-chantier)">Mise en place de l'armature.</strong>
          Descente du tirant équipé de ses dispositifs de protection et de ses
          centreurs, qui garantissent un enrobage régulier du coulis.
        </li>
        <li>
          <strong style="color:var(--blanc-chantier)">Injection de scellement.</strong>
          Injection du coulis de ciment sur la longueur de scellement, avec
          relevé des volumes et des pressions.
        </li>
        <li>
          <strong style="color:var(--blanc-chantier)">Durcissement.</strong>
          Respect du délai de prise avant toute sollicitation. Cette attente
          n'est pas compressible, quelle que soit la pression du planning.
        </li>
        <li>
          <strong style="color:var(--blanc-chantier)">Mise en tension.</strong>
          Pour les tirants actifs, mise en tension au vérin à la charge prescrite
          et blocage de la tête.
        </li>
        <li>
          <strong style="color:var(--blanc-chantier)">Essai de réception.</strong>
          Application d'une charge d'épreuve supérieure à la charge de service et
          mesure du déplacement de la tête, conformément à l'EN 1537.
        </li>
      </ol>
    </div>
  </div>
</section>

<section class="band">
  <div class="wrap">
    <div class="section-head" data-reveal>
      <span class="sec-num">006e /</span>
      <h2>Quand le tirant n'est <span class="accent">pas</span> la solution</h2>
    </div>
    <div class="prose" data-reveal>
      <p>
        Une entreprise de travaux a rarement intérêt à expliquer les limites de
        sa propre technique. Nous le faisons quand même, parce qu'un ancrage posé
        dans un contexte inadapté coûte plus cher qu'il ne résout.
      </p>
      <ul>
        <li>
          <strong>Emprise foncière insuffisante.</strong> Un tirant s'ancre en
          arrière de la paroi, souvent sous une parcelle voisine ou sous le
          domaine public. Sans autorisation de tréfonds, la solution est
          juridiquement impraticable, quelle qu'en soit la pertinence technique.
        </li>
        <li>
          <strong>Terrain sans horizon d'ancrage.</strong> Si aucune couche
          résistante n'est atteignable à une longueur raisonnable, le scellement
          ne mobilisera pas l'effort attendu. Une paroi autostable ou butonnée
          sera plus adaptée.
        </li>
        <li>
          <strong>Réseaux enterrés denses.</strong> En centre urbain, la présence
          de canalisations, câbles ou ouvrages souterrains peut interdire le
          forage incliné sur les zones concernées.
        </li>
      </ul>
      <p>
        Dans ces cas, nous le disons dès l'étude de la demande, et nous orientons
        vers la technique appropriée — y compris lorsqu'elle ne relève pas de
        notre périmètre. C'est le sens de notre engagement d'intégrité.
      </p>
    </div>
  </div>
</section>
""" + faq_block(FAQ_TIRANTS, "006d", "Questions <span class=\"accent\">fréquentes</span>")
   + (AUTRES_SERVICES % ("007b", CARD_MICRO + "\n      " + CARD_BETON)),
})

# ---------------------------------------------------------------------------
# /services/beton-projete/
# ---------------------------------------------------------------------------

PAGES.append({
    "path": "/services/beton-projete/",
    "nav": "cur_services",
    "og": "beton-projete",
    "title": "Béton Projeté au Maroc — Voie Sèche &amp; Humide | G3FSP",
    "desc": "G3FSP projette du béton par voie sèche ou humide pour le confortement de "
            "parois, tunnels et la réparation d'ouvrages au Maroc. Résistance rapide, "
            "mise en œuvre optimisée.",
    "eyebrow": "004 / Béton projeté",
    "h1": "Béton projeté : <span class=\"accent\">revêtement</span> &amp; confortement",
    "lead": "Projection pneumatique à haute vitesse : bétonner des surfaces "
            "verticales, inclinées ou en voûte sans recours à un coffrage "
            "traditionnel.",
    "cta_label": "Demander un devis",
    "crumbs": [("Accueil", "/"), ("Services", "/services/"), ("Béton projeté", None)],
    "schema": [
        breadcrumb_schema([("Accueil", "/"), ("Services", "/services/"),
                           ("Béton projeté", "/services/beton-projete/")]),
        service_schema("Béton projeté au Maroc",
                       "Mise en œuvre de béton projeté par voie sèche ou voie humide "
                       "pour confortement de parois, tunnels et réparation "
                       "structurale au Maroc."),
        faq_schema(FAQ_BETON),
    ],
    "cta_band": {
        "num": "006",
        "title": "Conforter sans <span class=\"accent\">coffrage</span>",
        "text": "Paroi à conforter, galerie à revêtir, ouvrage en béton à réparer : "
                "décrivez-nous la géométrie et les contraintes d'accès, nous vous "
                "chiffrons l'intervention sous 48 heures.",
    },
    "body": """
<section class="band">
  <div class="wrap">
    <div class="prose" data-reveal>
      <h2>Le principe</h2>
      <p>
        Le <strong>béton projeté</strong> est mis en œuvre par
        <strong>projection pneumatique à haute vitesse</strong> contre la surface
        à traiter. La vitesse d'impact assure à la fois la mise en place et le
        compactage du matériau, sans vibration ni coffrage.
      </p>
      <p>
        Il permet de bétonner des surfaces <strong>verticales, inclinées ou en
        voûte</strong> sans recours à un coffrage traditionnel. Il garantit une
        <strong>flexibilité d'exécution maximale</strong> et une
        <strong>mise en sécurité rapide</strong> des chantiers — deux qualités
        décisives lorsqu'une paroi vient d'être excavée et doit être stabilisée
        sans délai.
      </p>

      <h2>Voie sèche ou voie humide ?</h2>
      <p>
        Deux procédés coexistent, et le choix relève autant de la géométrie du
        chantier que du volume à mettre en œuvre.
      </p>
      <div class="table-wrap">
        <table class="tech">
          <caption>Comparaison des deux procédés</caption>
          <thead>
            <tr><th>Critère</th><th>Voie sèche</th><th>Voie humide</th></tr>
          </thead>
          <tbody>
            <tr>
              <td>Principe</td>
              <td>Mélange sec transporté par air comprimé, eau ajoutée à la lance</td>
              <td>Béton déjà malaxé avec son eau, pompé jusqu'à la lance</td>
            </tr>
            <tr>
              <td>Rendement</td>
              <td>Modéré</td>
              <td>Élevé — adapté aux gros volumes</td>
            </tr>
            <tr>
              <td>Souplesse</td>
              <td>Excellente : arrêts et reprises fréquents sans contrainte</td>
              <td>Moindre : le circuit doit rester en mouvement</td>
            </tr>
            <tr>
              <td>Poussière &amp; pertes</td>
              <td>Plus importantes</td>
              <td>Réduites</td>
            </tr>
            <tr>
              <td>Usage type</td>
              <td>Réparations ponctuelles, petits volumes, accès difficiles</td>
              <td>Tunnels, grandes parois, chantiers à cadence soutenue</td>
            </tr>
          </tbody>
        </table>
      </div>
      <p>
        Nous mettons en œuvre les <strong>deux procédés</strong> et retenons celui
        qui convient au chantier, en fonction du volume, de la cadence attendue,
        de l'accessibilité et des contraintes d'environnement.
      </p>
    </div>
  </div>
</section>

<section class="band band--dark trame">
  <div class="wrap">
    <div class="section-head" data-reveal>
      <span class="sec-num">003 /</span>
      <h2>Domaines d'application <span class="accent">principaux</span></h2>
    </div>
    <div class="grid grid--3">
      <div class="card" data-reveal>
        <div class="card__num">01</div>
        <h3>Soutènement &amp; confortement</h3>
        <p>
          Parois clouées, talus, blindages de fouilles et galeries. Le béton
          projeté forme le parement continu qui solidarise les têtes de
          <a href="/services/tirants-ancrage/">clous</a> et protège le terrain
          de l'érosion.
        </p>
      </div>
      <div class="card" data-reveal>
        <div class="card__num">02</div>
        <h3>Génie civil &amp; infrastructures</h3>
        <p>
          Tunnels, ouvrages d'art et bassins. Le procédé épouse les géométries
          courbes et irrégulières que le coffrage traditionnel traite mal, et
          permet une mise en sécurité immédiate après excavation.
        </p>
      </div>
      <div class="card" data-reveal>
        <div class="card__num">03</div>
        <h3>Réparation structurale</h3>
        <p>
          Renforcement et réhabilitation d'ouvrages en béton dégradés. Après
          purge des zones altérées et traitement des armatures, le béton projeté
          reconstitue la section et l'enrobage.
        </p>
      </div>
    </div>
  </div>
</section>

<section class="band">
  <div class="wrap">
    <div class="section-head" data-reveal>
      <span class="sec-num">004 /</span>
      <h2>Avantages du <span class="accent">béton projeté</span></h2>
    </div>
    <div class="prose" data-reveal>
      <ul>
        <li>
          <strong>Aucun coffrage</strong> — suppression du poste coffrage, donc
          des délais et des coûts associés, et liberté totale de géométrie.
        </li>
        <li>
          <strong>Mise en sécurité rapide</strong> — une paroi fraîchement
          excavée peut être revêtue dans la foulée, avant toute dégradation.
        </li>
        <li>
          <strong>Adaptabilité aux surfaces irrégulières</strong> — voûtes,
          parements rocheux, géométries complexes.
        </li>
        <li>
          <strong>Accessibilité</strong> — la lance atteint des zones où un
          coffrage serait impossible à mettre en place.
        </li>
        <li>
          <strong>Compacité</strong> — la vitesse d'impact assure le compactage
          du matériau sans vibration mécanique.
        </li>
      </ul>
    </div>
  </div>
</section>

<section class="band band--pale">
  <div class="wrap">
    <div class="section-head" data-reveal>
      <span class="sec-num">005 /</span>
      <h2>Nos <span class="accent">chantiers</span></h2>
    </div>
    <div class="prose" data-reveal>
      <p>
        Le béton projeté intervient rarement seul : il complète le plus souvent
        une opération de <a href="/services/tirants-ancrage/">clouage</a> ou de
        soutènement. Nos équipes disposent des
        <strong>compresseurs haute pression</strong> et des équipements de
        projection nécessaires pour intervenir sur l'ensemble du territoire.
      </p>
      <p>
        <a class="btn btn--ghost" href="/realisations/">
          Voir nos réalisations <span class="btn__arrow" aria-hidden="true">&rarr;</span>
        </a>
      </p>
    </div>
  </div>
</section>

<section class="band">
  <div class="wrap">
    <div class="section-head" data-reveal>
      <span class="sec-num">005c /</span>
      <h2>Composition et <span class="accent">formulation</span></h2>
    </div>
    <div class="prose" data-reveal>
      <p>
        Un béton projeté n'est pas un béton ordinaire passé dans une lance. Sa
        formulation répond à une contrainte propre au procédé : le matériau doit
        <strong>adhérer immédiatement</strong> à une paroi verticale ou en voûte,
        et y rester malgré son propre poids, avant même d'avoir commencé à faire
        prise.
      </p>

      <h3>Granulométrie</h3>
      <p>
        Le diamètre maximal des granulats est volontairement limité. Des éléments
        trop gros augmentent le <strong>rebond</strong> — la fraction de matériau
        qui ne colle pas et retombe au sol — et accélèrent l'usure des conduites.
        Une courbe granulométrique continue, riche en éléments fins, favorise la
        cohésion du matériau projeté.
      </p>

      <h3>Adjuvants</h3>
      <p>
        Les <strong>accélérateurs de prise</strong> permettent une montée en
        résistance rapide, indispensable lorsqu'une paroi fraîchement excavée
        doit être sécurisée sans délai. En voie humide, des
        <strong>plastifiants</strong> maintiennent la pompabilité du mélange sans
        excès d'eau, qui dégraderait la résistance finale.
      </p>

      <h3>Renforcement</h3>
      <p>
        Deux approches coexistent. Le <strong>treillis soudé</strong> fixé contre
        la paroi avant projection reste la solution classique, mais il crée des
        zones d'ombre derrière les fils où le béton peut mal s'enrober. Les
        <strong>fibres</strong> — métalliques ou synthétiques — incorporées
        directement au mélange suppriment ce risque et simplifient la mise en
        œuvre, au prix d'une formulation plus délicate.
      </p>
    </div>
  </div>
</section>

<section class="band band--dark trame">
  <div class="wrap">
    <div class="section-head" data-reveal>
      <span class="sec-num">005d /</span>
      <h2>Mise en œuvre <span class="accent">étape par étape</span></h2>
    </div>
    <div class="prose" style="max-width:72ch;color:var(--gris-clair)" data-reveal>
      <ol>
        <li>
          <strong style="color:var(--blanc-chantier)">Préparation du support.</strong>
          Purge des matériaux instables, nettoyage de la surface, traitement des
          venues d'eau. Une paroi souillée ou ruisselante compromet l'adhérence,
          quelle que soit la qualité du béton.
        </li>
        <li>
          <strong style="color:var(--blanc-chantier)">Repères d'épaisseur.</strong>
          Mise en place de témoins permettant au porte-lance de contrôler
          visuellement l'épaisseur atteinte — un point difficile à apprécier
          autrement en cours de projection.
        </li>
        <li>
          <strong style="color:var(--blanc-chantier)">Armature éventuelle.</strong>
          Fixation du treillis soudé si la solution fibres n'a pas été retenue.
        </li>
        <li>
          <strong style="color:var(--blanc-chantier)">Projection.</strong>
          Lance tenue perpendiculairement à la paroi, à distance constante, par
          passes successives. La régularité du geste conditionne directement la
          compacité et le taux de rebond.
        </li>
        <li>
          <strong style="color:var(--blanc-chantier)">Finition et cure.</strong>
          Réglage de surface si le parement est destiné à rester apparent, puis
          protection contre la dessiccation pendant la prise.
        </li>
      </ol>
    </div>
  </div>
</section>

<section class="band">
  <div class="wrap">
    <div class="section-head" data-reveal>
      <span class="sec-num">005e /</span>
      <h2>Contrôle <span class="accent">qualité</span></h2>
    </div>
    <div class="prose" data-reveal>
      <p>
        Le béton projeté est un matériau dont la qualité dépend fortement de
        l'exécution : le même mélange, projeté correctement ou non, ne donne pas
        le même ouvrage. Le contrôle porte donc autant sur le
        <strong>geste</strong> que sur le matériau.
      </p>
      <ul>
        <li>
          <strong>Épaisseur</strong> — vérifiée par les témoins mis en place
          avant projection, et par sondages ponctuels après durcissement.
        </li>
        <li>
          <strong>Résistance</strong> — mesurée sur des caisses témoins projetées
          dans les mêmes conditions que l'ouvrage, puis carottées. Prélever
          directement dans la structure reste possible lorsque le marché
          l'impose.
        </li>
        <li>
          <strong>Adhérence au support</strong> — contrôlée par essais
          d'arrachement, particulièrement en réparation structurale où toute la
          performance repose sur la liaison avec le béton existant.
        </li>
        <li>
          <strong>Qualification du porte-lance</strong> — l'opérateur est un
          facteur de qualité à part entière. Son expérience se lit directement
          dans le taux de rebond et la régularité du parement.
        </li>
      </ul>
    </div>
  </div>
</section>

<section class="band band--pale">
  <div class="wrap">
    <div class="section-head" data-reveal>
      <span class="sec-num">005g /</span>
      <h2>Béton projeté &amp; <span class="accent">paroi clouée</span></h2>
      <p>La combinaison la plus fréquente sur nos chantiers.</p>
    </div>
    <div class="prose" data-reveal>
      <p>
        Le béton projeté intervient rarement seul. Dans la majorité des cas, il
        forme le <strong>parement d'une paroi clouée</strong> — une technique de
        soutènement qui associe des inclusions passives et un revêtement continu.
      </p>

      <h3>Un principe descendant</h3>
      <p>
        Contrairement à un mur de soutènement classique, qui se construit de bas
        en haut, la paroi clouée se réalise <strong>de haut en bas</strong>, par
        passes successives. On excave sur une hauteur limitée — typiquement un à
        deux mètres — puis on met en place les
        <a href="/services/tirants-ancrage/">clous</a>, on projette le béton, et
        seulement ensuite on descend d'un niveau.
      </p>
      <p>
        Cette séquence n'est pas une commodité d'organisation : elle est
        <strong>imposée par la stabilité</strong>. Excaver trop haut avant de
        clouer et de projeter expose la paroi à une rupture locale. La hauteur de
        passe est donc un paramètre de sécurité, pas un levier de productivité.
      </p>

      <h3>Le rôle exact du béton projeté</h3>
      <p>
        Il remplit trois fonctions simultanées. Il
        <strong>solidarise les têtes de clous</strong> en répartissant les efforts
        entre elles. Il <strong>protège le terrain de l'érosion</strong> et des
        venues d'eau, qui déstabiliseraient progressivement la face excavée. Et
        il <strong>reprend les poussées locales</strong> du sol entre les
        inclusions, là où le terrain n'est pas directement retenu.
      </p>

      <div class="callout">
        <p class="callout__title">Une seule entreprise, trois métiers</p>
        <p>
          Clouage, projection et — le cas échéant —
          <a href="/services/micropieux/">reprise en fondation</a> relèvent chez
          nous des mêmes équipes. C'est un avantage concret sur ce type
          d'ouvrage : pas d'interface entre lots, pas d'attente entre
          intervenants, et une responsabilité unique sur le résultat.
        </p>
      </div>
    </div>
  </div>
</section>
""" + faq_block(FAQ_BETON, "005f", "Questions <span class=\"accent\">fréquentes</span>")
   + (AUTRES_SERVICES % ("005b", CARD_MICRO + "\n      " + CARD_TIRANTS)),
})

# ---------------------------------------------------------------------------
# /realisations/
# ---------------------------------------------------------------------------

PAGES.append({
    "path": "/realisations/",
    "nav": "cur_real",
    "og": "realisations",
    "title": "Nos Réalisations — Chantiers de Fondations Spéciales | G3FSP",
    "desc": "Mosquée de Tinmel, Stade Boukhalef à Tanger, Californie, El Balia : "
            "découvrez les chantiers de fondations spéciales réalisés par G3FSP "
            "au Maroc, avec leur détail technique.",
    "eyebrow": "005 / Références &amp; expérience",
    "h1": "Nos projets <span class=\"accent\">réalisés</span>",
    "lead": "Sélection de chantiers récents démontrant notre expertise technique "
            "en pieux, micropieux et tirants d'ancrage.",
    "cta_label": "Parler de votre projet",
    "crumbs": [("Accueil", "/"), ("Réalisations", None)],
    "schema": [breadcrumb_schema([("Accueil", "/"), ("Réalisations", "/realisations/")])],
    "cta_band": {
        "num": "004",
        "title": "Votre ouvrage, <span class=\"accent\">notre prochain chantier</span>",
        "text": "Nous intervenons en sous-traitance de fondations spéciales pour les "
                "entreprises générales, les promoteurs et les maîtres d'ouvrage publics.",
    },
    "body": """
<section class="band">
  <div class="wrap">
    <div class="prose" data-reveal>
      <p>
        Les tableaux ci-dessous reprennent le <strong>détail d'exécution</strong>
        de nos chantiers : diamètre, profondeur et quantité par type d'élément.
        C'est l'information que cherchent les ingénieurs et les bureaux d'études —
        nous préférons la publier plutôt que de nous en tenir aux généralités.
      </p>
    </div>
  </div>
</section>

<section class="band band--pale">
  <div class="wrap">
    <div class="section-head" data-reveal>
      <span class="sec-num">002 /</span>
      <h2>Chantiers <span class="accent">en images</span></h2>
    </div>

    <div class="grid grid--2">
      <a class="project-card" href="/realisations/mosquee-tinmel/" data-reveal>
        <img src="/img/projets/mosquee-tinmel.webp"
             alt="Restauration de la Mosquée de Tinmel — tirants d'ancrage"
             loading="lazy" width="1200" height="675">
        <div class="project-card__body">
          <span class="project-card__place">Haut Atlas — Marrakech</span>
          <h3>Restauration de la Mosquée de Tinmel</h3>
          <p>
            Restauration après le séisme d'Al Haouz de 2023. Un chantier
            patrimonial en zone de montagne, où la faible vibration de la mise
            en œuvre était une contrainte absolue.
          </p>
          <div class="table-wrap" style="margin-bottom:0">
            <table class="tech">
              <caption>Tirants d'ancrage — détail d'exécution</caption>
              <thead>
                <tr><th>Ø (mm)</th><th>Prof. (m)</th><th>Qté</th></tr>
              </thead>
              <tbody>
                <tr><td>100</td><td>12,00</td><td>93</td></tr>
              </tbody>
            </table>
          </div>
          <span class="card__link">Lire l'étude de cas <span aria-hidden="true">&rarr;</span></span>
        </div>
      </a>

      <div class="project-card" data-reveal>
        <img src="/img/projets/talus-nador.webp"
             alt="Stabilisation de talus à Nador — forage et mise en place d'armatures"
             loading="lazy" width="1200" height="675">
        <div class="project-card__body">
          <span class="project-card__place">Nador — Oriental</span>
          <h3>Stabilisation de talus</h3>
          <p>
            Confortement d'un talus en zone de relief : forage, mise en place
            des armatures et scellement. Un contexte où la stabilité du terrain
            conditionne la sécurité de tout l'ouvrage en amont.
          </p>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="band">
  <div class="wrap">
    <div class="section-head" data-reveal>
      <span class="sec-num">003 /</span>
      <h2>Autres <span class="accent">chantiers</span></h2>
    </div>

    <div class="grid grid--3">
      <div class="card" data-reveal>
        <h3>Stade Boukhalef</h3>
        <p><strong>Tanger</strong> — Complexe sportif.<br>Micropieux &amp; pieux forés.</p>
        <div class="table-wrap" style="margin-bottom:0">
          <table class="tech">
            <thead>
              <tr><th>Ø (mm)</th><th>Prof. (m)</th><th>Qté</th></tr>
            </thead>
            <tbody>
              <tr><td>800</td><td>14,00</td><td>20</td></tr>
              <tr><td>300</td><td>5,20</td><td>155</td></tr>
            </tbody>
          </table>
        </div>
      </div>

      <div class="card" data-reveal>
        <h3>Californie</h3>
        <p><strong>Tanger</strong> — Fondations profondes.<br>Pieux forés de grand diamètre.</p>
        <div class="table-wrap" style="margin-bottom:0">
          <table class="tech">
            <thead>
              <tr><th>Ø (mm)</th><th>Prof. (m)</th><th>Qté</th></tr>
            </thead>
            <tbody>
              <tr><td>800</td><td>20,50</td><td>4</td></tr>
              <tr><td>800</td><td>11,60</td><td>32</td></tr>
              <tr><td>800</td><td>7,60</td><td>1</td></tr>
            </tbody>
          </table>
        </div>
      </div>

      <div class="card" data-reveal>
        <h3>El Balia</h3>
        <p><strong>Tanger</strong> — Fondations de bâtiment.<br>Pieux forés.</p>
        <div class="table-wrap" style="margin-bottom:0">
          <table class="tech">
            <thead>
              <tr><th>Ø (mm)</th><th>Prof. (m)</th><th>Qté</th></tr>
            </thead>
            <tbody>
              <tr><td>800</td><td>12,00</td><td>9</td></tr>
              <tr><td>800</td><td>7,00</td><td>1</td></tr>
              <tr><td>800</td><td>5,70</td><td>2</td></tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</section>
""" + (ZONES_BAND % "003b"),
})

# ---------------------------------------------------------------------------
# /realisations/mosquee-tinmel/
# ---------------------------------------------------------------------------

PAGES.append({
    "path": "/realisations/mosquee-tinmel/",
    "nav": "cur_real",
    "og": "mosquee-tinmel",
    "placename": "Tinmel",
    "geopos": "31.1442;-8.3364",
    "icbm": "31.1442, -8.3364",
    "title": "Mosquée de Tinmel — Tirants d'Ancrage Post-Séisme | G3FSP",
    "desc": "Étude de cas : restauration de la Mosquée de Tinmel (Haut Atlas) après le "
            "séisme d'Al Haouz 2023. 93 tirants d'ancrage Ø 100 mm sur 12 m par G3FSP.",
    "eyebrow": "Étude de cas",
    "h1": "Mosquée de <span class=\"accent\">Tinmel</span>",
    "lead": "Haut Atlas — Restauration après le séisme d'Al Haouz de 2023. "
            "Tirants d'ancrage sur un monument du XIIᵉ siècle.",
    "cta_label": "Discuter d'un projet patrimonial",
    "crumbs": [("Accueil", "/"), ("Réalisations", "/realisations/"),
               ("Mosquée de Tinmel", None)],
    "schema": [
        breadcrumb_schema([("Accueil", "/"), ("Réalisations", "/realisations/"),
                           ("Mosquée de Tinmel", "/realisations/mosquee-tinmel/")]),
        {
            "@context": "https://schema.org",
            "@type": "Project",
            "name": "Restauration de la Mosquée de Tinmel — tirants d'ancrage",
            "description": "Mise en œuvre de 93 tirants d'ancrage Ø 100 mm sur 12 m de "
                           "profondeur dans le cadre de la restauration de la Mosquée "
                           "de Tinmel après le séisme d'Al Haouz de 2023.",
            "location": {"@type": "Place", "name": "Tinmel, Haut Atlas, Maroc"},
            "participant": {"@type": "Organization", "name": "G3FSP"},
        },
    ],
    "cta_band": {
        "num": "005",
        "title": "Un ouvrage <span class=\"accent\">sensible</span> à reprendre ?",
        "text": "Monument historique, bâtiment occupé, structure fragilisée : nous "
                "adaptons la méthode d'exécution à la contrainte, pas l'inverse.",
    },
    "body": """
<section class="band">
  <div class="wrap wrap--narrow">
    <figure data-reveal style="margin:0 0 clamp(2rem,4vw,3rem)">
      <img src="/img/projets/mosquee-tinmel.webp"
           alt="Chantier de restauration de la Mosquée de Tinmel — mise en œuvre des tirants d'ancrage"
           width="1200" height="675"
           style="width:100%;aspect-ratio:16/9;object-fit:cover;border-left:var(--bedrock) solid var(--volt)">
      <figcaption style="margin-top:.7rem;font-size:.82rem;color:var(--gris-technique)">
        Mosquée de Tinmel — intervention G3FSP sur tirants d'ancrage.
      </figcaption>
    </figure>
    <div class="prose" data-reveal>
      <h2>Le contexte</h2>
      <p>
        Le <strong>séisme d'Al Haouz</strong> de septembre 2023 a durement frappé
        le Haut Atlas. Parmi les édifices touchés figure la
        <strong>Mosquée de Tinmel</strong>, monument majeur de l'architecture
        almohade, situé en zone de montagne à environ 100 km au sud de Marrakech.
      </p>
      <p>
        L'intervention sur un ouvrage de cette nature impose des contraintes
        qu'un chantier courant ne connaît pas : <strong>accès difficile</strong>
        en terrain montagneux, <strong>maçonneries anciennes fragilisées</strong>
        qui ne tolèrent aucune vibration significative, et exigence de
        réversibilité propre aux interventions patrimoniales.
      </p>

      <h2>Notre intervention</h2>
      <p>
        G3FSP a réalisé la mise en œuvre des <strong>tirants d'ancrage</strong>
        destinés à reprendre les efforts et à ancrer la structure dans un horizon
        stable.
      </p>

      <div class="table-wrap">
        <table class="tech">
          <caption>Tirants d'ancrage — détail d'exécution</caption>
          <thead>
            <tr><th>Type d'élément</th><th>Ø (mm)</th><th>Profondeur (m)</th><th>Quantité</th></tr>
          </thead>
          <tbody>
            <tr><td>Tirant d'ancrage</td><td>100</td><td>12,00</td><td>93</td></tr>
          </tbody>
        </table>
      </div>

      <h2>Pourquoi cette technique</h2>
      <p>
        Le choix du <strong>tirant d'ancrage de petit diamètre</strong> répondait
        directement aux trois contraintes du site :
      </p>
      <ul>
        <li>
          <strong>Faible vibration</strong> — la mise en œuvre par forage de petit
          diamètre n'induit pas les vibrations d'un battage, ce qui protège les
          maçonneries anciennes déjà sollicitées par le séisme.
        </li>
        <li>
          <strong>Encombrement réduit</strong> — nos machines d'ancrage petit
          diamètre sont conçues pour les espaces contraints, condition nécessaire
          pour intervenir sur un site patrimonial en montagne.
        </li>
        <li>
          <strong>Ancrage profond</strong> — 12 mètres de profondeur permettent
          d'atteindre un horizon résistant sous les niveaux superficiels
          remaniés.
        </li>
      </ul>

      <p class="pull-quote">
        « Chaque fondation est invisible. Notre travail, lui, dure des générations. »
      </p>

      <h2>Ce que ce chantier dit de nous</h2>
      <p>
        Tinmel n'est pas notre plus gros chantier en volume — 93 tirants, c'est
        modeste comparé aux 155 micropieux du
        <a href="/realisations/">Stade Boukhalef</a>. Mais c'est celui qui
        illustre le mieux notre positionnement : intervenir là où la contrainte
        technique prime sur la quantité, avec une
        <a href="/services/tirants-ancrage/">méthode d'ancrage</a> choisie pour
        le site plutôt que pour la facilité d'exécution.
      </p>
      <div class="callout">
        <p class="callout__title">Vous portez un projet comparable ?</p>
        <p>
          Renforcement de structure existante, ouvrage patrimonial, bâtiment
          fragilisé en zone sismique : parlez-en à nos ingénieurs. Voir aussi nos
          <a href="/services/micropieux/">solutions de reprise en sous-œuvre</a>
          et notre page
          <a href="/zones-intervention/marrakech/">fondations spéciales à Marrakech</a>.
        </p>
      </div>
    </div>
  </div>
</section>
""",
})

# ---------------------------------------------------------------------------
# /zones-intervention/
# ---------------------------------------------------------------------------

PAGES.append({
    "path": "/zones-intervention/",
    "nav": "cur_zones",
    "og": "zones",
    "title": "Zones d'Intervention — Fondations Spéciales au Maroc | G3FSP",
    "desc": "G3FSP intervient à Casablanca, Rabat, Tanger, Marrakech, Agadir et Nador "
            "pour tous vos travaux de micropieux, tirants d'ancrage et béton projeté.",
    "eyebrow": "Couverture nationale",
    "h1": "Nous intervenons dans <span class=\"accent\">tout le Royaume</span>",
    "lead": "Basés à Casablanca, nos équipes et nos équipements se déplacent sur "
            "l'ensemble du territoire marocain.",
    "cta_label": "Vérifier notre disponibilité",
    "crumbs": [("Accueil", "/"), ("Zones d'intervention", None)],
    "schema": [breadcrumb_schema([("Accueil", "/"),
                                  ("Zones d'intervention", "/zones-intervention/")])],
    "cta_band": {
        "num": "003",
        "title": "Un chantier <span class=\"accent\">hors de ces villes</span> ?",
        "text": "Notre couverture ne s'arrête pas à cette liste. Décrivez-nous la "
                "localisation et la nature des travaux : nous vous dirons rapidement "
                "si nous pouvons mobiliser.",
    },
    "body": """
<section class="band">
  <div class="wrap">
    <div class="prose" data-reveal>
      <p>
        Les fondations spéciales sont un métier de <strong>mobilité</strong> :
        le matériel se déplace, les équipes suivent. Depuis notre base de
        Casablanca, nous intervenons sur les grands pôles économiques du Royaume
        comme en zone de montagne — la
        <a href="/realisations/mosquee-tinmel/">Mosquée de Tinmel</a>, dans le
        Haut Atlas, en est l'illustration.
      </p>
      <p>
        Chaque région pose ses propres questions géotechniques. Les pages
        ci-dessous détaillent les spécificités de sol que nous rencontrons
        localement et les techniques que nous y déployons le plus souvent.
      </p>
    </div>
  </div>
</section>

<section class="band band--pale">
  <div class="wrap">
    <div class="section-head" data-reveal>
      <span class="sec-num">002 /</span>
      <h2>Nos <span class="accent">implantations</span></h2>
    </div>

    <div class="grid grid--3">
      <a class="card" href="/zones-intervention/casablanca/" data-reveal>
        <div class="card__num">01</div>
        <h3>Casablanca</h3>
        <p>Siège de l'entreprise. Sols argileux, tissu urbain dense, reprises en
           sous-œuvre en site occupé.</p>
        <span class="card__link">En savoir plus <span aria-hidden="true">&rarr;</span></span>
      </a>
      <a class="card" href="/zones-intervention/rabat/" data-reveal>
        <div class="card__num">02</div>
        <h3>Rabat</h3>
        <p>Capitale administrative. Grands équipements publics, vallée du
           Bouregreg, terrains côtiers.</p>
        <span class="card__link">En savoir plus <span aria-hidden="true">&rarr;</span></span>
      </a>
      <a class="card" href="/zones-intervention/tanger/" data-reveal>
        <div class="card__num">03</div>
        <h3>Tanger</h3>
        <p>Notre terrain d'expérience le plus dense : Stade Boukhalef,
           Californie, El Balia. Marnes et versants instables.</p>
        <span class="card__link">En savoir plus <span aria-hidden="true">&rarr;</span></span>
      </a>
      <a class="card" href="/zones-intervention/marrakech/" data-reveal>
        <div class="card__num">04</div>
        <h3>Marrakech</h3>
        <p>Plaine du Haouz et Haut Atlas. Zone sismique — restauration
           post-séisme de la Mosquée de Tinmel.</p>
        <span class="card__link">En savoir plus <span aria-hidden="true">&rarr;</span></span>
      </a>
      <a class="card" href="/zones-intervention/agadir/" data-reveal>
        <div class="card__num">05</div>
        <h3>Agadir</h3>
        <p>Zone de forte sismicité, sols sableux littoraux et alluvions de la
           vallée du Souss.</p>
        <span class="card__link">En savoir plus <span aria-hidden="true">&rarr;</span></span>
      </a>
      <div class="card" data-reveal>
        <div class="card__num">06</div>
        <h3>Nador &amp; Oriental</h3>
        <p>Interventions en stabilisation de talus et fondations profondes sur
           la façade méditerranéenne orientale.</p>
      </div>
    </div>
  </div>
</section>
""",
})

# ---------------------------------------------------------------------------
# Pages villes
# ---------------------------------------------------------------------------

VILLES = [
    {
        "slug": "casablanca",
        "nom": "Casablanca",
        "geopos": "33.5731;-7.5898",
        "kw": "Micropieux &amp; Fondations Spéciales à Casablanca",
        "desc": "G3FSP intervient à Casablanca pour tous vos projets de fondations "
                "spéciales : micropieux, tirants d'ancrage, béton projeté. Sols "
                "argileux et zones urbaines denses maîtrisés.",
        "lead": "Siège de l'entreprise. Nos équipes et nos équipements sont basés "
                "à Casablanca et mobilisables sur toute la région du Grand Casablanca.",
        "geologie": """
      <p>
        Casablanca et sa région présentent une configuration que nous connaissons
        bien, pour y être installés : des <strong>formations superficielles
        argileuses et limoneuses</strong> d'épaisseur variable reposant sur un
        substratum plus ancien. Cette couverture argileuse est
        <strong>sensible aux variations de teneur en eau</strong> — elle gonfle et
        se rétracte au rythme des saisons, ce qui la rend peu fiable comme niveau
        d'assise pour un ouvrage lourd.
      </p>
      <p>
        La conséquence pratique est simple : sur beaucoup de projets casablancais,
        fonder superficiellement expose à des tassements différentiels. Il faut
        <strong>aller chercher l'horizon porteur en profondeur</strong>, ce qui
        est exactement la fonction du pieu et du micropieu.
      </p>
      <p>
        S'ajoute la contrainte urbaine. Le tissu dense du centre et des quartiers
        d'affaires impose de travailler <strong>en mitoyenneté</strong>, avec des
        emprises de chantier réduites, des accès contraints et des avoisinants
        sensibles aux vibrations. C'est le terrain d'élection du micropieu et de
        la <strong>berlinoise tirantée</strong>.
      </p>
""",
        "interventions": [
            ("Reprise en sous-œuvre",
             "Renforcement de fondations de bâtiments existants, création de "
             "sous-sols sous immeuble occupé, reprise avant surélévation. Nos "
             "machines d'ancrage petit diamètre travaillent en hauteur libre "
             "réduite."),
            ("Fondations profondes",
             "Pieux forés jusqu'à Ø 1200 mm et micropieux de 100 à 300 mm pour "
             "immeubles résidentiels et tertiaires, sur les horizons porteurs "
             "situés sous la couverture argileuse."),
            ("Soutènement de fouilles",
             "Tirants d'ancrage et berlinoises tirantées pour les fouilles "
             "profondes en site urbain contraint, sans étaiement encombrant en "
             "fond de fouille."),
        ],
    },
    {
        "slug": "rabat",
        "nom": "Rabat",
        "geopos": "34.0209;-6.8416",
        "kw": "Micropieux &amp; Fondations Spéciales à Rabat",
        "desc": "Travaux de fondations spéciales à Rabat et Salé : micropieux, pieux "
                "forés, tirants d'ancrage et béton projeté. G3FSP intervient sur la "
                "région de Rabat-Salé-Kénitra.",
        "lead": "Capitale administrative et pôle de grands équipements publics, "
                "Rabat concentre des projets où l'exigence de qualité d'exécution "
                "est élevée.",
        "geologie": """
      <p>
        La région de Rabat-Salé associe plusieurs contextes géotechniques
        distincts. Sur les plateaux, on rencontre des
        <strong>formations gréseuses et calcaires</strong> offrant de bonnes
        caractéristiques mécaniques, mais dont le toit peut être irrégulier —
        ce qui complique le choix d'un niveau d'assise homogène.
      </p>
      <p>
        La <strong>vallée du Bouregreg</strong> présente une configuration
        radicalement différente : des <strong>alluvions récentes</strong>,
        potentiellement compressibles et saturées, sur des épaisseurs qui peuvent
        être importantes. Les grands projets d'aménagement de la vallée y ont
        largement recours aux fondations profondes.
      </p>
      <p>
        Enfin, la frange littorale comporte des <strong>sables dunaires</strong>
        peu cohérents, où la tenue des parois de forage impose généralement un
        <strong>tubage provisoire</strong> — micropieu de type II plutôt que
        type I.
      </p>
""",
        "interventions": [
            ("Fondations profondes",
             "Pieux forés et micropieux pour équipements publics, programmes "
             "tertiaires et résidentiels, avec ancrage dans le substratum gréseux "
             "ou calcaire."),
            ("Traversée d'alluvions",
             "Micropieux de type II avec tubage provisoire pour traverser les "
             "niveaux alluvionnaires de la vallée du Bouregreg et atteindre "
             "l'horizon résistant."),
            ("Soutènement &amp; ancrage",
             "Tirants d'ancrage actifs pour fouilles profondes et parois de "
             "soutènement, conformément à la norme EN 1537."),
        ],
    },
    {
        "slug": "tanger",
        "nom": "Tanger",
        "geopos": "35.7595;-5.8340",
        "kw": "Fondations Spéciales &amp; Micropieux à Tanger",
        "desc": "G3FSP a réalisé le Stade Boukhalef, Californie et El Balia à Tanger. "
                "Micropieux, pieux forés Ø 800 mm et tirants d'ancrage sur terrains "
                "marno-argileux.",
        "lead": "Notre terrain d'expérience le plus dense : trois chantiers majeurs "
                "livrés — Stade Boukhalef, Californie et El Balia.",
        "geologie": """
      <p>
        Tanger est, du point de vue géotechnique, l'une des villes les plus
        exigeantes du Royaume. Le contexte du <strong>Rif</strong> y impose des
        <strong>formations marno-argileuses</strong> et des matériaux de type
        flysch, souvent altérés en surface et de caractéristiques mécaniques
        médiocres.
      </p>
      <p>
        Deux conséquences directes pour le constructeur. D'abord, la
        <strong>portance superficielle est faible</strong> : les ouvrages un peu
        lourds appellent presque systématiquement une fondation profonde. Ensuite,
        le relief accidenté combiné à la nature argileuse du terrain crée un
        <strong>risque d'instabilité de versant</strong> bien identifié dans la
        région — glissements, reptations, désordres sur talus de déblai.
      </p>
      <p>
        C'est ce contexte qui explique le profil de nos chantiers tangérois :
        des <strong>pieux Ø 800 mm descendus jusqu'à 20,50 m</strong> à
        Californie, et un mixte micropieux/pieux au Stade Boukhalef. On ne fonde
        pas superficiellement à Tanger sans de très bonnes raisons.
      </p>
""",
        "interventions": [
            ("Pieux forés de grand diamètre",
             "Ø 800 mm jusqu'à 20,50 m de profondeur, comme réalisé sur le chantier "
             "Californie. Ancrage sous les niveaux marneux altérés."),
            ("Micropieux",
             "155 micropieux Ø 300 mm exécutés au Stade Boukhalef, en complément de "
             "20 pieux Ø 800 mm — la combinaison type sur terrain hétérogène."),
            ("Stabilisation de talus",
             "Tirants d'ancrage, clouage et béton projeté pour sécuriser les talus "
             "de déblai et les versants instables, fréquents sur le relief tangérois."),
        ],
    },
    {
        "slug": "marrakech",
        "nom": "Marrakech",
        "geopos": "31.6295;-7.9811",
        "kw": "Micropieux &amp; Fondations Spéciales à Marrakech",
        "desc": "Fondations spéciales à Marrakech et dans le Haut Atlas : micropieux, "
                "tirants d'ancrage, renforcement post-sismique. G3FSP a restauré la "
                "Mosquée de Tinmel.",
        "lead": "Plaine du Haouz et Haut Atlas. C'est ici que nous avons réalisé la "
                "restauration de la Mosquée de Tinmel après le séisme de 2023.",
        "geologie": """
      <p>
        Marrakech s'étend sur la <strong>plaine du Haouz</strong>, constituée de
        formations alluviales issues du démantèlement du Haut Atlas : alternances
        de <strong>graviers, galets, sables et niveaux argileux</strong>. La
        portance y est globalement correcte, mais l'<strong>hétérogénéité
        latérale</strong> est la règle plutôt que l'exception — un sondage ne
        décrit pas fidèlement le point situé vingt mètres plus loin.
      </p>
      <p>
        Le second paramètre est la <strong>sismicité</strong>. Le séisme d'Al
        Haouz de septembre 2023 l'a rappelé de la manière la plus dure. Le
        <strong>règlement parasismique RPS 2011</strong> impose des vérifications
        spécifiques, et les fondations profondes jouent un rôle central : elles
        ancrent l'ouvrage dans un horizon stable et reprennent les efforts
        horizontaux.
      </p>
      <p>
        Enfin, la région concentre un <strong>patrimoine bâti ancien</strong>
        considérable. Intervenir sur ces structures exige des techniques à faible
        vibration — c'est précisément la logique qui a présidé au choix des
        tirants d'ancrage de petit diamètre à
        <a href="/realisations/mosquee-tinmel/">Tinmel</a>.
      </p>
""",
        "interventions": [
            ("Renforcement post-sismique",
             "Reprise en sous-œuvre et ancrage de structures fragilisées, à faible "
             "vibration. 93 tirants Ø 100 mm sur 12 m réalisés à la Mosquée de "
             "Tinmel."),
            ("Fondations en sol hétérogène",
             "Micropieux allant chercher individuellement la couche résistante, "
             "adaptés à la variabilité latérale des alluvions du Haouz."),
            ("Interventions en montagne",
             "Machines d'ancrage petit diamètre mobilisables sur des sites d'accès "
             "difficile dans le Haut Atlas."),
        ],
    },
    {
        "slug": "agadir",
        "nom": "Agadir",
        "geopos": "30.4278;-9.5981",
        "kw": "Fondations Spéciales &amp; Micropieux à Agadir",
        "desc": "G3FSP réalise vos fondations spéciales à Agadir et dans la vallée du "
                "Souss : micropieux, pieux forés et tirants d'ancrage en zone de forte "
                "sismicité.",
        "lead": "Zone de forte sismicité et sols littoraux. Agadir impose une "
                "attention particulière au comportement dynamique des fondations.",
        "geologie": """
      <p>
        Agadir occupe une place à part dans l'histoire de la construction
        marocaine : le <strong>séisme de 1960</strong> est à l'origine directe de
        la réglementation parasismique nationale. La ville se situe dans une
        <strong>zone d'aléa sismique élevé</strong>, et le
        <strong>RPS 2011</strong> y impose les vérifications les plus strictes.
      </p>
      <p>
        Sur le plan des terrains, la région combine des <strong>sols sableux
        littoraux</strong> peu cohérents et les <strong>alluvions de la vallée du
        Souss</strong>. Ces formations posent deux questions au concepteur : la
        portance, et surtout le comportement sous sollicitation cyclique — les
        sables lâches et saturés sont susceptibles de perdre leur résistance lors
        d'une secousse.
      </p>
      <p>
        Dans ce contexte, la fondation profonde n'est pas seulement une réponse à
        un problème de portance : c'est un <strong>choix de comportement
        sismique</strong>. Ancrer l'ouvrage sous les niveaux susceptibles de se
        déstructurer relève de la sécurité, pas du confort.
      </p>
""",
        "interventions": [
            ("Fondations en zone sismique",
             "Pieux et micropieux ancrés sous les horizons superficiels, "
             "dimensionnés en cohérence avec les prescriptions du RPS 2011 et la "
             "note de calcul du bureau d'études."),
            ("Traversée de sols sableux",
             "Micropieux de type II à tubage provisoire, nécessaires pour tenir "
             "la paroi de forage dans les sables littoraux peu cohérents."),
            ("Ouvrages touristiques &amp; tertiaires",
             "Fondations profondes pour hôtels, résidences et équipements sur le "
             "littoral d'Agadir et la vallée du Souss."),
        ],
    },
]

# Question spécifique à chaque ville (la plus recherchée localement)
FAQ_VILLES = {
    "casablanca": (
        "Pourquoi les sols argileux de Casablanca posent-ils problème ?",
        "Les argiles sont sensibles aux variations de teneur en eau : elles "
        "gonflent en saison humide et se rétractent en saison sèche. Un ouvrage "
        "fondé superficiellement sur ces formations subit des mouvements "
        "différentiels qui se traduisent par des fissures. La fondation profonde "
        "reporte la charge sous cette couche active."),
    "rabat": (
        "Faut-il des fondations profondes dans la vallée du Bouregreg ?",
        "Très souvent, oui. Les alluvions récentes de la vallée peuvent être "
        "compressibles et saturées sur des épaisseurs importantes. Les pieux et "
        "micropieux traversent ces niveaux pour reporter la charge sur le "
        "substratum gréseux ou calcaire sous-jacent. Seule l'étude géotechnique "
        "du site permet de trancher."),
    "tanger": (
        "Pourquoi les chantiers tangérois nécessitent-ils souvent des pieux profonds ?",
        "Le contexte rifain impose des formations marno-argileuses souvent "
        "altérées en surface, de faible portance. Pour atteindre un horizon "
        "résistant, il faut descendre : sur notre chantier Californie, certains "
        "pieux Ø 800 mm ont été exécutés jusqu'à 20,50 m de profondeur."),
    "marrakech": (
        "Le règlement parasismique RPS 2011 change-t-il la conception des fondations ?",
        "Oui. En zone d'aléa sismique, les fondations doivent reprendre des "
        "efforts horizontaux en plus des charges verticales, et être ancrées dans "
        "un horizon stable. Le séisme d'Al Haouz de 2023 a rappelé l'importance "
        "de ces vérifications sur l'ensemble de la région du Haouz."),
    "agadir": (
        "Que faut-il surveiller dans les sols sableux d'Agadir ?",
        "Deux points : la tenue de la paroi de forage, qui impose généralement un "
        "tubage provisoire, et le comportement du sol sous sollicitation "
        "sismique. Les sables lâches et saturés peuvent perdre une part de leur "
        "résistance lors d'une secousse, ce qui plaide pour un ancrage sous ces "
        "niveaux."),
}


for i, v in enumerate(VILLES):
    cards = "\n      ".join(
        """<div class="card" data-reveal>
        <div class="card__num">%02d</div>
        <h3>%s</h3>
        <p>%s</p>
      </div>""" % (n + 1, titre, texte)
        for n, (titre, texte) in enumerate(v["interventions"])
    )

    faq_ville = [
        FAQ_VILLES[v["slug"]],
        ("Intervenez-vous à %s pour des chantiers de petite taille ?" % v["nom"],
         "Oui. Nous traitons aussi bien les opérations de quelques dizaines "
         "d'éléments que les chantiers de plusieurs centaines. Nos machines "
         "d'ancrage petit diamètre sont précisément conçues pour les interventions "
         "ponctuelles en espace contraint, notamment en reprise en sous-œuvre."),
        ("Sous quel délai obtient-on un devis pour un projet à %s ?" % v["nom"],
         "Nos ingénieurs répondent sous 48 heures. Pour un chiffrage précis dès le "
         "premier échange, transmettez-nous le rapport géotechnique, les descentes "
         "de charges et un plan de masse. À défaut, nous pouvons fournir un ordre "
         "de grandeur puis affiner."),
        ("Êtes-vous basés à %s ?" % v["nom"],
         "G3FSP est basée à Casablanca. Nos équipes et nos équipements se "
         "déplacent sur l'ensemble du territoire marocain, y compris en zone de "
         "montagne — la restauration de la Mosquée de Tinmel, dans le Haut Atlas, "
         "en est l'illustration."),
    ]

    PAGES.append({
        "path": "/zones-intervention/%s/" % v["slug"],
        "nav": "cur_zones",
        "og": "zone-%s" % v["slug"],
        "placename": v["nom"],
        "geopos": v["geopos"],
        "icbm": v["geopos"].replace(";", ", "),
        "title": "%s | G3FSP" % v["kw"],
        "desc": v["desc"],
        "eyebrow": "Zone d'intervention",
        "h1": "Fondations spéciales à <span class=\"accent\">%s</span>" % v["nom"],
        "lead": v["lead"],
        "cta_label": "Nous contacter pour un projet à %s" % v["nom"],
        "crumbs": [("Accueil", "/"), ("Zones d'intervention", "/zones-intervention/"),
                   (v["nom"], None)],
        "schema": [
            breadcrumb_schema([("Accueil", "/"),
                               ("Zones d'intervention", "/zones-intervention/"),
                               (v["nom"], "/zones-intervention/%s/" % v["slug"])]),
            {
                "@context": "https://schema.org",
                "@type": "LocalBusiness",
                "name": "G3FSP — Fondations spéciales %s" % v["nom"],
                "description": "Travaux de fondations spéciales à %s : micropieux, "
                               "pieux forés, tirants d'ancrage et béton projeté."
                               % v["nom"],
                "url": "https://www.g3fsp.com/zones-intervention/%s/" % v["slug"],
                "telephone": TEL_RAW,
                "email": MAIL,
                "address": {"@type": "PostalAddress", "addressLocality": "Casablanca",
                            "addressCountry": "MA"},
                "areaServed": {"@type": "City", "name": v["nom"]},
            },
            faq_schema(faq_ville),
        ],
        "cta_band": {
            "num": "004",
            "title": "Un projet à <span class=\"accent\">%s</span> ?" % v["nom"],
            "text": "Transmettez-nous votre rapport géotechnique et vos descentes de "
                    "charges. Nos ingénieurs vous répondent sous 48 heures avec une "
                    "méthode d'exécution et un chiffrage.",
        },
        "body": """
<section class="band">
  <div class="wrap">
    <div class="section-head" data-reveal>
      <span class="sec-num">002 /</span>
      <h2>Spécificités géotechniques de <span class="accent">%s</span></h2>
    </div>
    <div class="prose" data-reveal>
%s
    </div>
  </div>
</section>

<section class="band band--pale">
  <div class="wrap">
    <div class="section-head" data-reveal>
      <span class="sec-num">003 /</span>
      <h2>Nos interventions dans la <span class="accent">région</span></h2>
    </div>
    <div class="grid grid--3">
      %s
    </div>

    <div class="prose" style="margin-top:3rem" data-reveal>
      <p>
        Découvrez le détail de nos techniques :
        <a href="/services/micropieux/">pieux et micropieux</a>,
        <a href="/services/tirants-ancrage/">tirants d'ancrage et clouage</a>,
        <a href="/services/beton-projete/">béton projeté</a>.
      </p>
    </div>
  </div>
</section>

<section class="band">
  <div class="wrap">
    <div class="section-head" data-reveal>
      <span class="sec-num">003c /</span>
      <h2>Comment se déroule une intervention à <span class="accent">%s</span></h2>
    </div>
    <div class="prose" data-reveal>
      <p>
        Notre méthode ne change pas d'une ville à l'autre — ce sont les
        contraintes de terrain qui changent. Le déroulement type est le suivant :
      </p>
      <ol>
        <li>
          <strong>Analyse du dossier.</strong> Lecture du rapport géotechnique,
          des descentes de charges et des contraintes d'accès du site.
        </li>
        <li>
          <strong>Proposition technique et chiffrage.</strong> Sous 48 heures :
          méthode d'exécution retenue, quantités, planning prévisionnel.
        </li>
        <li>
          <strong>Mobilisation.</strong> Amenée du matériel adapté depuis
          Casablanca, installation de chantier et implantation topographique.
        </li>
        <li>
          <strong>Exécution et suivi.</strong> Réalisation des travaux avec
          relevé systématique des paramètres, en coordination avec la maîtrise
          d'œuvre.
        </li>
        <li>
          <strong>Réception.</strong> Essais de contrôle prescrits au marché et
          remise du dossier d'exécution complet.
        </li>
      </ol>
    </div>
  </div>
</section>
""" % (v["nom"], v["geologie"], cards, v["nom"])
        + faq_block(faq_ville, "003d",
                    "Questions fréquentes — <span class=\"accent\">%s</span>" % v["nom"])
        + (ZONES_BAND % "003e"),
    })

# ---------------------------------------------------------------------------
# /a-propos/
# ---------------------------------------------------------------------------

PAGES.append({
    "path": "/a-propos/",
    "nav": "cur_apropos",
    "og": "a-propos",
    "title": "À Propos — Qui Sommes-Nous | G3FSP",
    "desc": "G3FSP est une entreprise marocaine spécialisée dans les fondations "
            "spéciales et la géotechnique. Basée à Casablanca. Expertise, intégrité, "
            "innovation.",
    "eyebrow": "001 / Qui sommes-nous",
    "h1": "Une entreprise marocaine de <span class=\"accent\">fondations spéciales</span>",
    "lead": "Basée à Casablanca, G3FSP accompagne ingénieurs et maîtres d'ouvrage "
            "dans leurs ouvrages les plus exigeants.",
    "cta_label": "Travailler avec nous",
    "crumbs": [("Accueil", "/"), ("À propos", None)],
    "schema": [
        breadcrumb_schema([("Accueil", "/"), ("À propos", "/a-propos/")]),
        {
            "@context": "https://schema.org",
            "@type": "Organization",
            "name": "G3FSP",
            "alternateName": "Géotechnique 3 Fondations Spéciales & Parois",
            "url": "https://www.g3fsp.com",
            "email": MAIL,
            "telephone": TEL_RAW,
            "slogan": "Construire sur du solide",
            "address": {"@type": "PostalAddress", "addressLocality": "Casablanca",
                        "addressCountry": "MA"},
        },
    ],
    "cta_band": {
        "num": "005",
        "title": "Construire sur du <span class=\"accent\">solide</span>",
        "text": "Que vous soyez bureau d'études, entreprise générale ou maître "
                "d'ouvrage, nos ingénieurs sont disponibles pour étudier votre "
                "projet.",
    },
    "body": """
<section class="band">
  <div class="wrap">
    <div class="prose" data-reveal>
      <p>
        <strong>G3FSP</strong> — <em>Géotechnique 3 Fondations Spéciales &amp;
        Parois</em> — est une entreprise marocaine spécialisée dans les
        <strong>fondations spéciales</strong> et la <strong>géotechnique</strong>.
        Basée à Casablanca, nous accompagnons ingénieurs et maîtres d'ouvrage dans
        leurs ouvrages les plus exigeants.
      </p>
      <p>
        Notre expertise couvre les <strong>pieux</strong> pour le transfert de
        charges en profondeur, les <strong>tirants d'ancrage</strong> pour le
        soutènement, et le <strong>béton projeté</strong> pour le confortement des
        parois.
      </p>
      <p>
        Forts d'une expérience terrain sur des projets emblématiques — dont la
        restauration de la <a href="/realisations/mosquee-tinmel/">Mosquée de
        Tinmel</a> après le séisme d'Al Haouz — nous apportons rigueur technique
        et réactivité.
      </p>
      <p class="pull-quote">
        « Chaque fondation est invisible. Notre travail, lui, dure des générations. »
      </p>
    </div>
  </div>
</section>

<section class="band band--dark trame">
  <div class="wrap">
    <div class="section-head" data-reveal>
      <span class="sec-num">002 /</span>
      <h2>G3FSP en <span class="accent">chiffres</span></h2>
    </div>
    <div class="stat-row" data-reveal>
      <div class="stat-item">
        <span class="n"><span data-count="2" data-suffix="">0</span>+</span>
        <span class="l">Ans d'existence</span>
      </div>
      <div class="stat-item">
        <span class="n"><span data-count="10" data-suffix="">0</span>+</span>
        <span class="l">Projets livrés</span>
      </div>
      <div class="stat-item">
        <span class="n"><span data-count="6" data-suffix="">0</span></span>
        <span class="l">Villes couvertes</span>
      </div>
      <div class="stat-item">
        <span class="n"><span data-count="5" data-suffix="">0</span></span>
        <span class="l">Spécialités</span>
      </div>
    </div>
  </div>
</section>

<section class="band">
  <div class="wrap">
    <div class="section-head" data-reveal>
      <span class="sec-num">003 /</span>
      <h2>Nos <span class="accent">valeurs</span></h2>
    </div>
    <div class="grid grid--3">
      <div class="card" data-reveal>
        <div class="card__num">01</div>
        <h3>Expertise</h3>
        <p>
          Savoir-faire sur projets complexes à travers le Maroc. Une équipe jeune
          et qualifiée, formée aux techniques d'exécution des fondations
          spéciales.
        </p>
      </div>
      <div class="card" data-reveal>
        <div class="card__num">02</div>
        <h3>Intégrité</h3>
        <p>
          Transparence sur les méthodes et les engagements contractuels. Nous
          disons ce que nous faisons, nous documentons ce que nous exécutons.
        </p>
      </div>
      <div class="card" data-reveal>
        <div class="card__num">03</div>
        <h3>Innovation</h3>
        <p>
          Techniques avancées en injection, forage et monitoring. Des équipements
          de pointe au service de la précision d'exécution.
        </p>
      </div>
    </div>
  </div>
</section>

<section class="band band--pale">
  <div class="wrap">
    <div class="section-head" data-reveal>
      <span class="sec-num">004 /</span>
      <h2>Ce qui nous <span class="accent">distingue</span></h2>
    </div>
    <div class="grid grid--3">
      <div class="card" data-reveal>
        <h3>Expertise terrain</h3>
        <p>Géologie marocaine maîtrisée — argiles, calcaires, terrains difficiles.</p>
      </div>
      <div class="card" data-reveal>
        <h3>Réactivité</h3>
        <p>Réponse technique sur tout le territoire, sous 48 heures.</p>
      </div>
      <div class="card" data-reveal>
        <h3>Culture sécurité &amp; qualité</h3>
        <p>Approche à la fois technique et économique de chaque chantier.</p>
      </div>
    </div>
  </div>
</section>
""" + (EQUIPEMENTS_BAND % "004b"),
})

# ---------------------------------------------------------------------------
# /contact/
# ---------------------------------------------------------------------------

PAGES.append({
    "path": "/contact/",
    "nav": "cur_contact",
    "og": "contact",
    "title": "Contact — Demandez votre Devis Gratuit | G3FSP",
    "desc": "Contactez G3FSP pour vos travaux de fondations spéciales au Maroc. "
            "Téléphone +212 661 455 673, WhatsApp, e-mail. Réponse technique "
            "sous 48 heures.",
    "eyebrow": "Parlons de votre projet",
    "h1": "Demandez votre <span class=\"accent\">devis gratuit</span>",
    "lead": "Décrivez-nous votre ouvrage, vos contraintes de sol et vos délais. "
            "Nos ingénieurs reviennent vers vous sous 48 heures.",
    "cta_label": "Appeler maintenant",
    "crumbs": [("Accueil", "/"), ("Contact", None)],
    "schema": [
        breadcrumb_schema([("Accueil", "/"), ("Contact", "/contact/")]),
        {
            "@context": "https://schema.org",
            "@type": "ContactPage",
            "name": "Contact G3FSP",
            "url": "https://www.g3fsp.com/contact/",
            "mainEntity": {
                "@type": "LocalBusiness",
                "name": "G3FSP",
                "telephone": TEL_RAW,
                "email": MAIL,
                "address": {"@type": "PostalAddress", "addressLocality": "Casablanca",
                            "addressCountry": "MA"},
                "openingHoursSpecification": [{
                    "@type": "OpeningHoursSpecification",
                    "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
                    "opens": "08:00", "closes": "18:00",
                }],
            },
        },
    ],
    "body": ("""
<section class="band">
  <div class="wrap">
    <div class="grid grid--2" style="gap:clamp(2rem,5vw,4rem);align-items:start">

      <div data-reveal>
        <div class="section-head">
          <span class="sec-num">002 /</span>
          <h2>Nous <span class="accent">joindre</span></h2>
        </div>
        <ul class="contact-info-list">
          <li>
            <span class="k">Téléphone</span>
            <span class="v"><a href="tel:TELRAW">TELFMT</a></span>
          </li>
          <li>
            <span class="k">WhatsApp</span>
            <span class="v"><a href="WA" target="_blank" rel="noopener">TELFMT</a></span>
          </li>
          <li>
            <span class="k">E-mail</span>
            <span class="v"><a href="mailto:MAIL">MAIL</a></span>
          </li>
          <li>
            <span class="k">Adresse</span>
            <span class="v">Casablanca, Maroc</span>
          </li>
          <li>
            <span class="k">Horaires</span>
            <span class="v">Lundi – Vendredi<br>8h – 18h</span>
          </li>
        </ul>

        <div class="callout" style="margin-top:2rem">
          <p class="callout__title">Pour un chiffrage rapide</p>
          <p>
            Joignez si possible votre <strong>rapport géotechnique</strong>, les
            <strong>descentes de charges</strong> et un <strong>plan de
            masse</strong>. Avec ces trois éléments, nous pouvons répondre
            précisément dès le premier échange.
          </p>
        </div>
      </div>

      <div data-reveal>
        <div class="section-head">
          <span class="sec-num">003 /</span>
          <h2>Votre <span class="accent">demande</span></h2>
        </div>

        <form class="form-grid" action="https://formsubmit.co/MAIL" method="POST">
          <!-- Configuration FormSubmit (champs masqués) -->
          <input type="hidden" name="_subject" value="Nouvelle demande depuis g3fsp.com">
          <input type="hidden" name="_template" value="table">
          <input type="hidden" name="_captcha" value="false">
          <input type="hidden" name="_next" value="https://www.g3fsp.com/contact/merci/">
          <input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off">

          <div class="field">
            <label for="nom">Nom &amp; prénom <span class="req">*</span></label>
            <input type="text" id="nom" name="nom" required autocomplete="name">
          </div>
          <div class="field">
            <label for="societe">Société</label>
            <input type="text" id="societe" name="societe" autocomplete="organization">
          </div>
          <div class="field">
            <label for="email">E-mail <span class="req">*</span></label>
            <input type="email" id="email" name="email" required autocomplete="email">
          </div>
          <div class="field">
            <label for="tel">Téléphone</label>
            <input type="tel" id="tel" name="telephone" autocomplete="tel">
          </div>
          <div class="field">
            <label for="ville">Ville du projet</label>
            <select id="ville" name="ville">
              <option value="">— Sélectionner —</option>
              <option>Casablanca</option>
              <option>Rabat</option>
              <option>Tanger</option>
              <option>Marrakech</option>
              <option>Agadir</option>
              <option>Nador</option>
              <option>Autre</option>
            </select>
          </div>
          <div class="field">
            <label for="service">Prestation souhaitée</label>
            <select id="service" name="service">
              <option value="">— Sélectionner —</option>
              <option>Pieux forés</option>
              <option>Micropieux</option>
              <option>Tirants d'ancrage</option>
              <option>Clouage</option>
              <option>Béton projeté</option>
              <option>Je ne sais pas encore</option>
            </select>
          </div>
          <div class="field field--full">
            <label for="message">Votre projet <span class="req">*</span></label>
            <textarea id="message" name="message" required
              placeholder="Nature de l'ouvrage, contraintes de sol connues, délais souhaités…"></textarea>
          </div>
          <div class="field field--full">
            <button class="btn btn--primary" type="submit">
              Envoyer ma demande <span class="btn__arrow" aria-hidden="true">&rarr;</span>
            </button>
            <p class="form-note">
              Envoi via FormSubmit — <strong>l'adresse MAIL doit être activée une
              première fois</strong> : au premier envoi, un e-mail de confirmation
              est reçu, il suffit de cliquer sur le lien d'activation.
              Vous pouvez aussi nous écrire directement à
              <a href="mailto:MAIL">MAIL</a> ou via
              <a href="WA" target="_blank" rel="noopener">WhatsApp</a>.
            </p>
          </div>
        </form>
      </div>

    </div>
  </div>
</section>

<section class="band band--dark trame">
  <div class="wrap">
    <div class="section-head" data-reveal>
      <span class="sec-num">004 /</span>
      <h2>Nous intervenons dans <span class="accent">tout le Royaume</span></h2>
    </div>
    <ul class="city-list" data-reveal>
      <li><a href="/zones-intervention/casablanca/"><span class="idx">01</span> Casablanca</a></li>
      <li><a href="/zones-intervention/rabat/"><span class="idx">02</span> Rabat</a></li>
      <li><a href="/zones-intervention/tanger/"><span class="idx">03</span> Tanger</a></li>
      <li><a href="/zones-intervention/marrakech/"><span class="idx">04</span> Marrakech</a></li>
      <li><a href="/zones-intervention/agadir/"><span class="idx">05</span> Agadir</a></li>
      <li><a href="/zones-intervention/"><span class="idx">06</span> Nador</a></li>
    </ul>
  </div>
</section>
""".replace("TELRAW", TEL_RAW).replace("TELFMT", TEL_FMT)
     .replace("MAIL", MAIL).replace("WA", WA)),
})

# ---------------------------------------------------------------------------
# /contact/merci/  — page de confirmation après envoi du formulaire
# ---------------------------------------------------------------------------

PAGES.append({
    "path": "/contact/merci/",
    "nav": "cur_contact",
    "og": "contact",
    "robots": "noindex, follow",
    "title": "Demande envoyée — Merci | G3FSP",
    "desc": "Votre demande a bien été transmise aux équipes G3FSP. "
            "Nous revenons vers vous sous 48 heures.",
    "eyebrow": "Demande transmise",
    "h1": "Merci, c'est <span class=\"accent\">bien reçu</span>",
    "lead": "Votre demande a été transmise à nos ingénieurs. Nous revenons vers "
            "vous sous 48 heures ouvrées.",
    "cta_label": "Retour à l'accueil",
    "crumbs": [("Accueil", "/"), ("Contact", "/contact/"), ("Merci", None)],
    "schema": [],
    "body": ("""
<section class="band">
  <div class="wrap wrap--narrow">
    <div class="prose" data-reveal>
      <p>
        En attendant notre retour, vous pouvez nous joindre directement :
      </p>
      <ul>
        <li>Par téléphone au <a href="tel:TELRAW">TELFMT</a> (lun–ven, 8h–18h)</li>
        <li>Sur <a href="WA" target="_blank" rel="noopener">WhatsApp</a></li>
        <li>Par e-mail à <a href="mailto:MAIL">MAIL</a></li>
      </ul>
      <div class="callout">
        <p class="callout__title">Pour accélérer le chiffrage</p>
        <p>
          Si vous ne l'avez pas encore fait, envoyez-nous votre
          <strong>rapport géotechnique</strong>, vos
          <strong>descentes de charges</strong> et un <strong>plan de masse</strong>
          par e-mail. Avec ces trois éléments, notre réponse sera précise dès le
          premier échange.
        </p>
      </div>
    </div>

    <div class="grid grid--3" style="margin-top:clamp(2rem,4vw,3rem)">
      <a class="card" href="/services/" data-reveal>
        <h3>Nos services</h3>
        <p>Pieux, micropieux, tirants d'ancrage, clouage et béton projeté.</p>
        <span class="card__link">Voir <span aria-hidden="true">&rarr;</span></span>
      </a>
      <a class="card" href="/realisations/" data-reveal>
        <h3>Nos réalisations</h3>
        <p>Le détail technique de nos chantiers au Maroc.</p>
        <span class="card__link">Voir <span aria-hidden="true">&rarr;</span></span>
      </a>
      <a class="card" href="/a-propos/" data-reveal>
        <h3>Qui sommes-nous</h3>
        <p>Une entreprise marocaine de fondations spéciales, basée à Casablanca.</p>
        <span class="card__link">Voir <span aria-hidden="true">&rarr;</span></span>
      </a>
    </div>
  </div>
</section>
""".replace("TELRAW", TEL_RAW).replace("TELFMT", TEL_FMT)
     .replace("MAIL", MAIL).replace("WA", WA)),
})

# ---------------------------------------------------------------------------
# /mentions-legales/
# ---------------------------------------------------------------------------

PAGES.append({
    "path": "/mentions-legales/",
    "og": "accueil",
    "robots": "noindex, follow",
    "title": "Mentions Légales | G3FSP",
    "desc": "Mentions légales du site g3fsp.com — G3FSP, fondations spéciales et "
            "géotechnique, Casablanca, Maroc.",
    "eyebrow": "Informations légales",
    "h1": "Mentions <span class=\"accent\">légales</span>",
    "lead": "Informations relatives à l'éditeur et à l'hébergement du site g3fsp.com.",
    "cta_label": "Nous contacter",
    "crumbs": [("Accueil", "/"), ("Mentions légales", None)],
    "schema": [],
    "body": ("""
<section class="band">
  <div class="wrap wrap--narrow">
    <div class="prose" data-reveal>
      <h2>Éditeur du site</h2>
      <p>
        <strong>G3FSP</strong> — Géotechnique 3 Fondations Spéciales &amp; Parois<br>
        Casablanca, Maroc<br>
        Téléphone : <a href="tel:TELRAW">TELFMT</a><br>
        E-mail : <a href="mailto:MAIL">MAIL</a>
      </p>
      <div class="callout">
        <p class="callout__title">À compléter avant mise en ligne</p>
        <p>
          Forme juridique, capital social, numéro de registre de commerce (RC),
          identifiant fiscal (IF), ICE, adresse postale complète et nom du
          directeur de la publication doivent être renseignés ici.
        </p>
      </div>

      <h2>Hébergement</h2>
      <p>
        Les coordonnées de l'hébergeur du site sont à renseigner ici une fois
        l'hébergement souscrit.
      </p>

      <h2>Propriété intellectuelle</h2>
      <p>
        L'ensemble des contenus présents sur ce site — textes, images, données
        techniques, identité visuelle et éléments graphiques — est la propriété
        de G3FSP, sauf mention contraire. Toute reproduction ou représentation,
        totale ou partielle, sans autorisation écrite préalable est interdite.
      </p>

      <h2>Données personnelles</h2>
      <p>
        Les informations transmises via le formulaire de contact sont utilisées
        uniquement pour répondre à votre demande et ne font l'objet d'aucune
        cession à des tiers. Conformément à la loi 09-08 relative à la protection
        des personnes physiques à l'égard du traitement des données à caractère
        personnel, vous disposez d'un droit d'accès, de rectification et
        d'opposition sur les données vous concernant. Pour l'exercer, écrivez à
        <a href="mailto:MAIL">MAIL</a>.
      </p>

      <h2>Cookies</h2>
      <p>
        Ce site n'utilise pas de cookie de suivi publicitaire. Si des outils de
        mesure d'audience (Google Analytics, Search Console) sont mis en place,
        cette section devra être complétée en conséquence.
      </p>
    </div>
  </div>
</section>
""".replace("TELRAW", TEL_RAW).replace("TELFMT", TEL_FMT).replace("MAIL", MAIL)),
})

# ---------------------------------------------------------------------------
# 404
# ---------------------------------------------------------------------------

PAGES.append({
    "path": "/404.html",
    "og": "accueil",
    "robots": "noindex, follow",
    "title": "Page introuvable | G3FSP",
    "desc": "La page demandée n'existe pas ou a été déplacée.",
    "eyebrow": "Erreur 404",
    "h1": "Terrain <span class=\"accent\">non reconnu</span>",
    "lead": "La page que vous cherchez n'existe pas, ou a été déplacée. "
            "Revenons sur du solide.",
    "cta_label": "Nous contacter",
    "crumbs": [("Accueil", "/"), ("Page introuvable", None)],
    "schema": [],
    "body": """
<section class="band">
  <div class="wrap">
    <div class="section-head" data-reveal>
      <h2>Où souhaitez-vous <span class="accent">aller</span> ?</h2>
    </div>
    <div class="grid grid--3">
      <a class="card" href="/services/" data-reveal>
        <h3>Nos services</h3>
        <p>Pieux, micropieux, tirants d'ancrage, clouage et béton projeté.</p>
        <span class="card__link">Voir <span aria-hidden="true">&rarr;</span></span>
      </a>
      <a class="card" href="/realisations/" data-reveal>
        <h3>Nos réalisations</h3>
        <p>Le détail technique de nos chantiers au Maroc.</p>
        <span class="card__link">Voir <span aria-hidden="true">&rarr;</span></span>
      </a>
      <a class="card" href="/contact/" data-reveal>
        <h3>Contact</h3>
        <p>Un devis gratuit, une réponse technique sous 48 heures.</p>
        <span class="card__link">Voir <span aria-hidden="true">&rarr;</span></span>
      </a>
    </div>
  </div>
</section>
""",
})
