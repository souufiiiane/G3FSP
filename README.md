# G3FSP — Site web

Site statique (HTML/CSS/JS, sans bundler) pour **G3FSP — Fondations Spéciales &
Géotechnique**, Casablanca.

---

## Architecture retenue

| | |
|---|---|
| **Accueil** | Expérience *scroll-driven* : canvas image par image piloté au scroll (192 frames extraites de `drilling_rig_G3FSP.mp4`), Lenis + GSAP ScrollTrigger. Thème sombre. |
| **Pages intérieures** | Thème clair éditorial, sans scroll-jacking. Lecture longue, conforme à la charte. |

### Modèle d'animation repris de la V2

La V2 avait une animation plus réussie ; son modèle a été repris intégralement,
avec l'identité et le SEO de la V3 par-dessus.

| Point | V2 | V3 (première version) | V3 (actuelle) |
|---|---|---|---|
| Apparition de la machine | dès le 1ᵉʳ pixel | après ~1,5 écran (hero épinglé + `clip-path`) | **dès le 1ᵉʳ pixel** |
| Chargement | non bloquant, dessin au fil de l'eau | loader plein écran bloquant | **non bloquant** |
| Liaison frames | `document.documentElement` | `#scroll-container` (démarrait trop tard) | **`document.documentElement`** |
| Mise en page | canvas 2/3 droite + texte à gauche | canvas plein cadre, texte en marges | **canvas 2/3 droite** |
| Lisibilité du texte | dégradé sombre gauche→droite | `text-shadow` | **dégradé sombre** |
| Révélations | CSS + IntersectionObserver | timelines GSAP en `scrub` | **CSS + IntersectionObserver** |
| Épinglage du hero | aucun | `pin: true` | **aucun** |

Les deux causes du défaut « la machine n'apparaît qu'après plusieurs scrolls » :
le hero était épinglé sur 100 vh **et** le canvas était masqué par un
`clip-path: circle(0%)` tant que le hero n'avait pas fini de défiler. Les deux
sont supprimés.

### Pourquoi pas une seule page ?

La stratégie SEO définie dans `G3FSP_Phase1_SEO_Architecture.md` repose sur des
pages piliers de 1500–2500 mots, des pages locales par ville et un blog
technique. Chacune a besoin de son propre `<title>`, `<h1>`, `meta description`
et `canonical` — impossible sur une page unique.

L'accueil combine donc les deux : l'expérience scroll **et** une zone statique
en dessous (`.static-region`) qui porte le contenu référencé. Les sections
animées sont du vrai HTML crawlable, mais le référencement ne repose pas sur
elles (GSAP les met à `opacity: 0`).

---

## Structure

```
website/
├── index.html              ← accueil, écrit à la main
├── 404.html
├── build.py                ← générateur des pages intérieures
├── content.py              ← contenu rédactionnel (source de vérité)
├── common.py               ← constantes + schémas JSON-LD
├── css/
│   ├── brand.css           ← design system (couleurs, typo, header, footer)
│   ├── home.css            ← accueil scroll-driven uniquement
│   └── page.css            ← pages intérieures
├── js/
│   ├── site.js             ← menu mobile, reveals, compteurs (toutes pages)
│   └── home.js             ← Lenis + GSAP + rendu canvas (accueil)
├── frames/                 ← 192 × WebP 1280px (8,6 Mo)
├── icons/apple-touch-icon.png
├── favicon.svg
├── robots.txt
├── sitemap.xml
├── services/{,micropieux,tirants-ancrage,beton-projete}/
├── realisations/{,mosquee-tinmel}/
├── zones-intervention/{,casablanca,rabat,tanger,marrakech,agadir}/
├── a-propos/
├── contact/
└── mentions-legales/
```

---

## Développement

Le site doit être servi en HTTP (les frames ne se chargent pas en `file://`) :

```bash
cd website
python -m http.server 8000
# http://localhost:8000
```

### Modifier le contenu des pages intérieures

Éditer **`content.py`**, puis régénérer :

```bash
python build.py
```

Les fichiers `*/index.html` sont **générés** — toute modification directe sera
écrasée. L'accueil `index.html` est écrit à la main et n'est jamais touché par
le script.

### Régénérer les frames depuis la vidéo

```bash
ffmpeg -i drilling_rig_G3FSP.mp4 \
  -vf "delogo=x=1785:y=995:w=120:h=66,fps=24,scale=1280:-1" \
  -c:v libwebp -quality 58 -compression_level 6 \
  frames/frame_%04d.webp
```

Le filtre `delogo` supprime le filigrane « Veo » présent en bas à droite de la
vidéo source. Si le nombre de frames change, mettre à jour `FRAME_COUNT` dans
`js/home.js`.

---

## Réglages de l'accueil (`js/home.js`)

| Constante | Valeur | Effet |
|---|---|---|
| `FRAME_COUNT` | 192 | Doit correspondre au nombre de fichiers dans `frames/` |
| `FRAME_SPEED` | *calculé* | Recalculé à chaque `refresh` pour que la séquence s'achève pile à l'entrée de la zone statique, quel que soit le breakpoint |
| `IMAGE_SCALE` | 1.0 | Cover strict. **Ne pas descendre sous 1.0** : des bandes noires apparaîtraient en haut/bas, visibles sur les frames de fin (bas rocheux) |
| `HERO_FADE_PX` | 900 | Distance sur laquelle le hero s'efface en parallaxe |

Les sections se positionnent via `data-enter` / `data-leave`, exprimés en
**pourcentage du conteneur de scroll** — elles suivent donc automatiquement les
hauteurs définies par breakpoint dans `css/home.css` (`#scroll-container` :
620vh desktop / 480vh tablette / 430vh mobile). `data-animation` choisit le type
d'entrée (`fade-up`, `slide-left`, `slide-right`, `scale-up`, `clip-reveal`).

### Lisibilité du texte

**Desktop** — le texte occupe le tiers gauche, la machine les deux tiers droits.
La séparation repose sur `#dark-overlay`, un dégradé horizontal qui assombrit la
gauche et laisse la droite transparente. *Si la largeur de `.hero-inner` ou de
`.section-inner` est augmentée, les points d'arrêt du dégradé doivent l'être
aussi*, sinon le texte déborde sur la zone claire.

**Mobile (< 1024px)** — le canvas passe en pleine largeur : le texte se
superpose donc à la machine. Deux règles :

1. **Aucun bloc opaque derrière le texte.** La charte d'animation l'interdit
   explicitement (« no glassmorphism cards, no visible containers »), et un
   rectangle sombre masque l'animation — c'était le défaut d'une version
   précédente.
2. Le contraste est assuré par `.scroll-section::before`, un **halo elliptique
   sans bord** : opaque à ~90 % derrière le texte, totalement transparent aux
   extrémités. La machine reste visible tout autour. Le halo apparaît en fondu
   avec le texte (`.is-visible`), jamais avant.

Le voile global `#dark-overlay` est volontairement **léger** sur mobile
(0,34 au centre) : il ne pose qu'une base de contraste, le halo fait le reste.
Des `text-shadow` servent de filet de sécurité si le halo passe sur une zone
claire de l'image.

> En cas de retouche : ne jamais remonter l'opacité du voile global pour
> corriger un problème de lisibilité local — élargir le halo à la place.

---

## À faire avant mise en ligne

1. **Activer FormSubmit** — le formulaire poste vers
   `https://formsubmit.co/soufiane.nidlahadj@g3fsp.ma`. Au **premier envoi**,
   FormSubmit envoie un e-mail de confirmation à cette adresse : il faut cliquer
   sur le lien d'activation, sinon rien n'arrive.
2. **Images Open Graph** — créer `/og/*.jpg` (1200×630) ; les balises y font
   déjà référence.
3. **Mentions légales** — compléter forme juridique, RC, IF, ICE, adresse
   postale, directeur de publication, hébergeur.
4. **Logo vectoriel** — le logo utilisé (`img/logo-mark.webp`, repris de la V2)
   est un PNG détouré rasterisé. Un SVG serait préférable pour la netteté.
5. **Photos de chantier** — seules deux photos réelles existent (Tinmel, Nador).
   Les pages services et villes gagneraient à en recevoir. La charte demande
   contraste élevé, légère désaturation, le vert G3 Volt comme seule couleur vive.
6. **Google Search Console + Google My Business** — soumettre `sitemap.xml`,
   créer la fiche GMB décrite dans le document SEO.
7. **Vérifier les données chantier** — voir ci-dessous.

### ⚠ Écarts entre les deux documents sources

| Chantier | Plaquette (tableau détaillé) | Brochure trifold | Retenu sur le site |
|---|---|---|---|
| Tinmel | Ø 100 mm · 12,00 m · **93** | **90** tirants · Ø **150** mm | Données du tableau détaillé |
| Californie | Ø 800 : 4 + 32 + 1 = **37** pieux | **50** pieux Ø 800 | Diamètres/profondeurs uniquement, sans total |

Le tableau détaillé (diamètre / profondeur / quantité) a été retenu comme
référence. **À confirmer avant mise en ligne.**

---

## Contenu à produire (phase 2)

Le document SEO prévoit un blog technique `/ressources/` — non créé ici, car il
suppose la rédaction d'articles de 1000–1800 mots. Sujets prioritaires
identifiés :

- Qu'est-ce qu'un micropieu ? Types I à IV expliqués
- Sols argileux de Casablanca : nos recommandations
- Séisme et fondations : que dit la norme RPS 2011 ?
- Béton projeté voie sèche vs voie humide
- Restauration de la Mosquée de Tinmel : notre intervention

---

## Conformité à la charte

- Vert **G3 Volt `#6DD400`** présent partout, jamais dilué
- **Blanc Chantier `#F5F4F0`** en fond principal des pages intérieures
- Thème sombre réservé aux heros et sections d'impact
- **Barlow Condensed** (titres) + **IBM Plex Sans** (corps)
- *The Bedrock Line* (trait 3px), trame technique 5 %, numéros `00X /`
- Ton de voix : direct, technique mais accessible, sobre, sans superlatif
