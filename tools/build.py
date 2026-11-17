#!/usr/bin/env python3
"""Génère les pages HTML statiques du site Energia Group.

Le site reste 100 % statique (aucun build côté hébergeur) : ce script sert
seulement à garder l'en-tête, le pied de page et les méta-données identiques
sur toutes les pages. Après avoir modifié un contenu ici :

    python3 tools/build.py

puis commitez les fichiers HTML générés.

Les chemins sont relatifs (../) pour que le site fonctionne aussi bien à la
racine d'un domaine que dans un sous-dossier (ex. GitHub Pages).
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# --------------------------------------------------------------------------
# Informations société (source : cahier des charges, section 5 « vérifiées »)
# --------------------------------------------------------------------------
SOCIETE = {
    "nom": "ENERGIA GROUP (SAS)",
    "siren": "909 268 286",
    "siret": "909 268 286 00020",
    "siege": "155 rue Anatole France, 92300 Levallois-Perret",
    "ape": "4322B — Installation d'équipements thermiques et de climatisation",
    "qualif": "RGE QualiPAC module chauffage et ECS — n° QPAC/69638",
    "assurances": "RC générale et décennale (ERGO Versicherung)",
}

ICON_BOLT = ('<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" '
             'stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
             '<path d="M13 2 3 14h7l-1 8 10-12h-7l1-8z"/></svg>')
CHEV = '<span aria-hidden="true">›</span>'

NAV = [
    ("Particuliers", "particuliers/", [
        ("Pompe à chaleur air/eau", "particuliers/pompe-a-chaleur-air-eau/"),
        ("Pompe à chaleur air/air", "particuliers/pompe-a-chaleur-air-air/"),
        ("Ballon thermodynamique", "particuliers/ballon-thermodynamique/"),
        ("Poêle à granulés, VMC, isolation", "particuliers/#autres-solutions"),
        ("Aides à la rénovation", "particuliers/aides-renovation/"),
    ]),
    ("Professionnels", "professionnels/", [
        ("Décret BACS", "professionnels/#decret-bacs"),
        ("Contrat de Performance Énergétique", "professionnels/#cpe"),
        ("Loi Climat et Résilience", "professionnels/#loi-climat"),
    ]),
    ("À propos", "a-propos/", None),
    ("SAV", "contact/#sav", None),
    ("Contact", "contact/", None),
]


def header(p, current):
    items = []
    for label, href, sub in NAV:
        cls = ' class="is-current"' if current and href.startswith(current) else ""
        if sub:
            subs = "".join(f'<a href="{p}{h}">{l}</a>' for l, h in sub)
            items.append(
                f'<div class="nav-item has-sub"><a href="{p}{href}"{cls}>{label}</a>'
                f'<div class="sub">{subs}</div></div>')
        else:
            items.append(f'<div class="nav-item"><a href="{p}{href}"{cls}>{label}</a></div>')
    return f"""
  <a class="skip" href="#main">Aller au contenu</a>
  <header class="site-header" id="header">
    <div class="container header-inner">
      <a href="{p}" class="logo" aria-label="Energia Group — Accueil">
        <span class="logo-mark">{ICON_BOLT}</span>
        <span class="logo-text">ENERGIA<strong>GROUP</strong></span>
      </a>
      <nav class="nav" id="nav" aria-label="Navigation principale">
        {''.join(items)}
        <div class="nav-ctas">
          <a href="{p}eligibilite/" class="btn btn-green btn-sm">Testez votre éligibilité</a>
          <a href="{p}professionnels/" class="btn btn-outline btn-sm">Espace Pro</a>
        </div>
      </nav>
      <button class="nav-toggle" id="navToggle" aria-label="Ouvrir le menu" aria-expanded="false" aria-controls="nav">
        <span></span><span></span><span></span>
      </button>
    </div>
  </header>"""


def footer(p):
    s = SOCIETE
    return f"""
  <section class="vigilance dark">
    <div class="container vigilance-inner">
      <div class="vigilance-icon" aria-hidden="true">!</div>
      <div>
        <h2 class="h4">Vigilance — démarchage abusif</h2>
        <p>Des appels ou messages frauduleux peuvent être passés en usurpant le nom d'Energia Group.
        Nos conseillers ne pratiquent pas de démarchage abusif. En cas de doute, ne communiquez aucune
        information personnelle et <a href="{p}contact/">contactez-nous directement</a>.</p>
      </div>
    </div>
  </section>
  <footer class="site-footer dark topo">
    <div class="container footer-inner">
      <div class="footer-brand">
        <a href="{p}" class="logo logo-light"><span class="logo-mark">{ICON_BOLT}</span>
          <span class="logo-text">ENERGIA<strong>GROUP</strong></span></a>
        <p>Installateur RGE QualiPAC de pompes à chaleur et de solutions de rénovation énergétique,
        pour les particuliers et les professionnels, partout en France.</p>
        <p class="small">Qualification {s['qualif']}</p>
        <div class="socials" data-socials></div>
      </div>
      <nav class="footer-col" aria-label="Particuliers">
        <h3 class="h5">Particuliers</h3>
        <a href="{p}particuliers/pompe-a-chaleur-air-eau/">Pompe à chaleur air/eau</a>
        <a href="{p}particuliers/pompe-a-chaleur-air-air/">Pompe à chaleur air/air</a>
        <a href="{p}particuliers/ballon-thermodynamique/">Ballon thermodynamique</a>
        <a href="{p}particuliers/aides-renovation/">Aides à la rénovation</a>
        <a href="{p}eligibilite/">Testez votre éligibilité</a>
      </nav>
      <nav class="footer-col" aria-label="Professionnels">
        <h3 class="h5">Professionnels</h3>
        <a href="{p}professionnels/#decret-bacs">Décret BACS</a>
        <a href="{p}professionnels/#cpe">Contrat de Performance Énergétique</a>
        <a href="{p}professionnels/#loi-climat">Loi Climat et Résilience</a>
      </nav>
      <nav class="footer-col" aria-label="Energia Group">
        <h3 class="h5">Energia Group</h3>
        <a href="{p}a-propos/">À propos</a>
        <a href="{p}contact/#sav">SAV</a>
        <a href="{p}contact/">Contact</a>
        <a href="{p}mentions-legales/">Mentions légales</a>
        <a href="{p}mentions-legales/#confidentialite">Politique de confidentialité</a>
      </nav>
    </div>
    <div class="container footer-bottom">
      <p>© <span data-year></span> {s['nom']} · SIREN {s['siren']}</p>
      <p>*Sous conditions d'éligibilité.</p>
    </div>
  </footer>
  <script src="{p}js/config.js"></script>
  <script src="{p}js/main.js"></script>"""


def page(path, title, description, body, current=None, depth=None):
    if depth is None:
        depth = path.count("/") + 1 if path else 0
    p = "../" * depth
    html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <meta name="theme-color" content="#1E2B2A">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:type" content="website">
  <link rel="icon" href="{p}img/favicon.svg" type="image/svg+xml">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@600;700;800&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{p}css/styles.css">
</head>
<body>
{header(p, current)}
  <main id="main">
{body.replace("{p}", p)}
  </main>
{footer(p)}
</body>
</html>
"""
    out = ROOT / path / "index.html" if path else ROOT / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    print("écrit", out.relative_to(ROOT))


# --------------------------------------------------------------------------
# Blocs réutilisables
# --------------------------------------------------------------------------
def page_hero(eyebrow, h1, lead, ctas=True):
    btns = (f"""<div class="hero-actions">
          <a href="{{p}}eligibilite/" class="btn btn-white">Testez votre éligibilité {CHEV}</a>
          <a href="{{p}}contact/" class="btn btn-outline-light">Être rappelé par un conseiller {CHEV}</a>
        </div>""" if ctas else "")
    return f"""    <section class="page-hero dark topo">
      <div class="container">
        <p class="eyebrow">{eyebrow}</p>
        <h1>{h1}</h1>
        <p class="lead">{lead}</p>
        {btns}
      </div>
    </section>"""


CTA_BAND = f"""    <section class="cta-band dark topo">
      <div class="container cta-band-inner">
        <div>
          <h2>Jusqu'à 90 % de votre projet financé par les aides de l'État*</h2>
          <p>Vérifiez en 2 minutes les aides auxquelles vous avez droit. Étude de votre dossier sous 48 h.</p>
        </div>
        <a href="{{p}}eligibilite/" class="btn btn-white btn-lg">Testez votre éligibilité {CHEV}</a>
      </div>
    </section>"""

STEPS = """    <section class="section dark topo">
      <div class="container">
        <div class="section-head">
          <p class="eyebrow">Votre parcours</p>
          <h2>Votre projet en 3 étapes</h2>
        </div>
        <ol class="steps">
          <li><span class="step-num">1</span><h3>Devis gratuit</h3>
            <p>Un conseiller détermine vos besoins et établit un devis sur mesure.</p></li>
          <li><span class="step-num">2</span><h3>Accompagnement</h3>
            <p>Nous obtenons vos aides de l'État et les déduisons du devis final.</p></li>
          <li><span class="step-num">3</span><h3>Installation</h3>
            <p>Nos équipes RGE installent votre matériel selon les chartes de qualité en vigueur.</p></li>
        </ol>
      </div>
    </section>"""

BRANDS = ["Daikin", "Mitsubishi Electric", "Atlantic", "Panasonic", "De Dietrich"]


def faq(items):
    return "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in items)


# --------------------------------------------------------------------------
# Pages
# --------------------------------------------------------------------------
def build_home():
    brands = "".join(f"<li>{b}</li>" for b in BRANDS)
    body = f"""    <section class="hero dark topo">
      <div class="container hero-inner">
        <div class="hero-content">
          <p class="eyebrow">ENERGIA GROUP</p>
          <h1>Vous avez le projet d'installer une pompe à chaleur&nbsp;?</h1>
          <p class="hero-sub">Jusqu'à <strong>90 % financé</strong> par les aides de l'État*</p>
          <p class="lead">Spécialiste de la rénovation énergétique, nous accompagnons particuliers et
          professionnels de l'audit jusqu'à l'obtention de vos aides.</p>
          <p class="lead muted-light">Expert en travaux de rénovation énergétique, nous mettons en œuvre les
          solutions les plus performantes — pompe à chaleur, ballon thermodynamique, isolation — et gérons
          votre projet de bout en bout&nbsp;: du financement à la récupération de vos aides.</p>
          <div class="hero-actions">
            <a href="{{p}}eligibilite/" class="btn btn-white btn-lg">Testez votre éligibilité {CHEV}</a>
            <a href="{{p}}professionnels/" class="btn btn-outline-light btn-lg">Vous êtes un professionnel&nbsp;? {CHEV}</a>
          </div>
          <p class="fineprint">*Sous conditions d'éligibilité.</p>
        </div>
        <aside class="hero-card" aria-label="Test d'éligibilité rapide">
          <p class="hero-card-title">Votre éligibilité en 2 minutes</p>
          <form class="quick-elig" action="{{p}}eligibilite/" method="get">
            <label for="qe-chauffage">Votre chauffage actuel</label>
            <select id="qe-chauffage" name="chauffage">
              <option value="fioul">Chaudière fioul</option>
              <option value="gaz">Chaudière gaz</option>
              <option value="electrique">Radiateurs électriques</option>
              <option value="bois">Bois / charbon</option>
              <option value="autre">Autre</option>
            </select>
            <label for="qe-cp">Code postal du logement</label>
            <input id="qe-cp" name="cp" inputmode="numeric" pattern="[0-9]{{5}}" maxlength="5" placeholder="Ex. 92300">
            <button class="btn btn-green btn-block" type="submit">Continuer {CHEV}</button>
          </form>
          <ul class="hero-card-points">
            <li>Gratuit et sans engagement</li>
            <li>Réponse sous 48 h</li>
            <li>Aides déduites du devis</li>
          </ul>
        </aside>
      </div>
    </section>

    <section class="keyfigures green">
      <div class="container keyfigures-grid">
        <div><strong>Des centaines</strong><span>d'installations réalisées</span></div>
        <div><strong>Jusqu'à 90 %</strong><span>financé par les aides de l'État*</span></div>
        <div><strong>48 h</strong><span>pour l'étude de votre dossier</span></div>
        <div><strong>France entière</strong><span>intervention sur tout le territoire</span></div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="section-head">
          <p class="eyebrow">Choisissez votre profil</p>
          <h2>Un accompagnement adapté à votre profil</h2>
        </div>
        <div class="profiles">
          <a class="profile-card profile-b2c" href="{{p}}particuliers/">
            <span class="tag">Particuliers</span>
            <h3>Vous êtes un particulier</h3>
            <p>Remplacez votre ancien système de chauffage, réduisez vos factures et bénéficiez des aides de l'État.</p>
            <span class="link">Découvrir nos solutions {CHEV}</span>
          </a>
          <a class="profile-card profile-b2b" href="{{p}}professionnels/">
            <span class="tag">Professionnels</span>
            <h3>Vous êtes un professionnel</h3>
            <p>Mise en conformité réglementaire et performance énergétique de vos bâtiments&nbsp;: Décret BACS, CPE, Loi Climat et Résilience.</p>
            <span class="link">Accéder à l'espace pro {CHEV}</span>
          </a>
        </div>
      </div>
    </section>

    <section class="section section-alt">
      <div class="container split">
        <div>
          <p class="eyebrow">Notre approche</p>
          <h2>Energia Group vous accompagne vers un logement plus performant</h2>
          <p class="lead-dark">Nous remplaçons votre ancienne chaudière par un système de chauffage performant,
          pour des économies pouvant atteindre <strong>3&nbsp;000&nbsp;€/an</strong>*.</p>
        </div>
        <ul class="guarantees">
          <li><span class="g-icon" aria-hidden="true">48h</span><div><h3>Audit de votre dossier en 48 h</h3><p>Un conseiller étudie votre projet et vos aides rapidement.</p></div></li>
          <li><span class="g-icon" aria-hidden="true">RGE</span><div><h3>Entreprise qualifiée RGE QualiPAC</h3><p>Qualification n° QPAC/69638, condition d'accès aux aides de l'État.</p></div></li>
          <li><span class="g-icon" aria-hidden="true">€</span><div><h3>Aides déduites directement de votre devis</h3><p>Vous ne réglez que le reste à charge.</p></div></li>
        </ul>
      </div>
    </section>

{STEPS}

    <section class="section">
      <div class="container">
        <div class="section-head">
          <p class="eyebrow">Nos solutions</p>
          <h2>Des équipements performants pour votre logement</h2>
        </div>
        <div class="products">
          <a class="product" href="{{p}}particuliers/pompe-a-chaleur-air-eau/">
            <span class="product-tag">Le plus demandé</span>
            <h3>Pompe à chaleur air/eau</h3>
            <p>Remplace votre chaudière fioul ou gaz. Chauffage par radiateurs ou plancher chauffant, et eau chaude sanitaire.</p>
            <span class="link">En savoir plus {CHEV}</span></a>
          <a class="product" href="{{p}}particuliers/pompe-a-chaleur-air-air/">
            <h3>Pompe à chaleur air/air</h3>
            <p>Chauffage et climatisation réversible pour un confort toute l'année.</p>
            <span class="link">En savoir plus {CHEV}</span></a>
          <a class="product" href="{{p}}particuliers/ballon-thermodynamique/">
            <h3>Ballon thermodynamique</h3>
            <p>Produisez votre eau chaude en consommant jusqu'à trois fois moins d'électricité qu'un cumulus classique.</p>
            <span class="link">En savoir plus {CHEV}</span></a>
          <a class="product" href="{{p}}particuliers/#autres-solutions">
            <h3>Poêle à granulés, VMC, isolation</h3>
            <p>Complétez votre rénovation pour réduire encore vos besoins de chauffage.</p>
            <span class="link">En savoir plus {CHEV}</span></a>
        </div>
      </div>
    </section>

    <section class="section dark coverage">
      <div class="container split">
        <div>
          <p class="eyebrow">Couverture</p>
          <h2>Nous intervenons partout en France</h2>
          <p>Où que vous soyez, nos équipes qualifiées RGE réalisent votre installation et assurent le suivi
          de votre équipement. Laissez-nous votre code postal&nbsp;: un conseiller vous confirme la prise en
          charge de votre secteur.</p>
          <a href="{{p}}eligibilite/" class="btn btn-white">Vérifier mon secteur {CHEV}</a>
        </div>
        <ul class="coverage-points">
          <li><strong>France métropolitaine</strong><span>Intervention sur tout le territoire</span></li>
          <li><strong>Équipes RGE</strong><span>Installation selon les chartes de qualité en vigueur</span></li>
          <li><strong>Suivi</strong><span>Mise en service, entretien et SAV</span></li>
        </ul>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="section-head">
          <p class="eyebrow">Certifications &amp; partenaires</p>
          <h2>Nos certifications, votre garantie</h2>
          <p class="section-sub">Energia Group est titulaire de la qualification RGE QualiPAC module chauffage et ECS,
          qui atteste de notre expertise sur l'installation de pompes à chaleur aérothermiques et géothermiques
          ainsi que de chauffe-eau thermodynamiques. Cette qualification conditionne l'accès aux aides de l'État
          (MaPrimeRénov', CEE, TVA réduite).</p>
        </div>
        <div class="cert-box">
          <div class="cert-badge"><strong>RGE</strong><span>QualiPAC</span></div>
          <p>Qualification QualiPAC n° <strong>QPAC/69638</strong> — vérifiable sur
          <a href="https://www.qualit-enr.org/annuaire/" target="_blank" rel="noopener">qualit-enr.org</a>, rubrique Annuaire.
          Entreprise couverte par une assurance RC générale et décennale.</p>
        </div>
        <p class="brands-title">Nos partenaires fabricants</p>
        <ul class="brands">{brands}</ul>
      </div>
    </section>

    <section class="section dark topo">
      <div class="container">
        <div class="section-head">
          <p class="eyebrow">Confiance</p>
          <h2>Pourquoi nous faire confiance</h2>
        </div>
        <div class="trust">
          <div><strong>Des centaines</strong><span>d'installations réalisées</span></div>
          <div><strong>RGE QualiPAC</strong><span>qualification n° QPAC/69638</span></div>
          <div><strong>Garantie décennale</strong><span>RC générale et décennale</span></div>
          <div><strong>France entière</strong><span>intervention sur tout le territoire</span></div>
        </div>
      </div>
    </section>

    <section class="section section-alt" id="financement">
      <div class="container split">
        <div>
          <p class="eyebrow">Financement &amp; aides</p>
          <h2>Jusqu'à 90 % de votre projet financé par les aides de l'État*</h2>
          <p>Grâce à notre qualification RGE QualiPAC, vous accédez à l'ensemble des dispositifs&nbsp;:
          MaPrimeRénov', Certificats d'Économies d'Énergie (CEE) et TVA réduite. Nous montons votre dossier
          et déduisons directement les aides de votre devis — vous ne réglez que le reste à charge.</p>
          <a href="{{p}}particuliers/aides-renovation/" class="link">Tout savoir sur les aides {CHEV}</a>
          <p class="fineprint dark-text">*Sous conditions d'éligibilité.</p>
        </div>
        <div class="form-card">
          <h3>Être rappelé par un conseiller</h3>
          <form class="lead-form" data-lead-form data-source="Accueil — rappel" novalidate>
            <label>Nom et prénom<input name="nom" autocomplete="name" required></label>
            <label>Téléphone<input name="telephone" type="tel" autocomplete="tel" required></label>
            <label>Code postal<input name="code_postal" inputmode="numeric" maxlength="5" required></label>
            <label>Votre projet
              <select name="projet">
                <option>Pompe à chaleur air/eau</option><option>Pompe à chaleur air/air</option>
                <option>Ballon thermodynamique</option><option>Autre / je ne sais pas</option>
              </select></label>
            <label class="consent"><input type="checkbox" name="consentement" required>
              J'accepte d'être recontacté par Energia Group au sujet de ma demande.
              <a href="{{p}}mentions-legales/#confidentialite">En savoir plus</a></label>
            <button class="btn btn-green btn-block" type="submit">Testez votre éligibilité en 2 minutes {CHEV}</button>
            <p class="form-status" role="status" aria-live="polite"></p>
          </form>
        </div>
      </div>
    </section>"""
    page("", "Pompe à chaleur jusqu'à 90 % financée* | Energia Group — installateur RGE QualiPAC",
         "Energia Group, installateur RGE QualiPAC : pompe à chaleur air/eau, air/air et ballon thermodynamique. "
         "Aides de l'État déduites du devis, étude sous 48 h, France entière.", body, depth=0)


def build_particuliers():
    body = f"""{page_hero("Particuliers", "Rénovez votre chauffage, réduisez vos factures",
        "Pompe à chaleur, eau chaude, isolation : nous choisissons avec vous la solution adaptée à votre logement et nous occupons de vos aides de l'État.")}
    <section class="section">
      <div class="container">
        <div class="section-head"><p class="eyebrow">Nos solutions</p><h2>Quelle solution pour votre logement&nbsp;?</h2></div>
        <div class="products">
          <a class="product" href="{{p}}particuliers/pompe-a-chaleur-air-eau/"><span class="product-tag">Le plus demandé</span>
            <h3>Pompe à chaleur air/eau</h3><p>Idéale pour remplacer une chaudière fioul ou gaz : elle alimente vos radiateurs ou votre plancher chauffant et peut produire votre eau chaude.</p><span class="link">En savoir plus {CHEV}</span></a>
          <a class="product" href="{{p}}particuliers/pompe-a-chaleur-air-air/">
            <h3>Pompe à chaleur air/air</h3><p>Chauffe en hiver, rafraîchit en été. Une solution simple pour les logements chauffés à l'électricité.</p><span class="link">En savoir plus {CHEV}</span></a>
          <a class="product" href="{{p}}particuliers/ballon-thermodynamique/">
            <h3>Ballon thermodynamique</h3><p>Remplace votre cumulus électrique et divise votre consommation pour l'eau chaude.</p><span class="link">En savoir plus {CHEV}</span></a>
        </div>
      </div>
    </section>
    <section class="section section-alt" id="autres-solutions">
      <div class="container">
        <div class="section-head"><p class="eyebrow">Compléter votre rénovation</p><h2>Poêle à granulés, VMC, isolation</h2></div>
        <div class="grid-3">
          <article class="card"><h3>Poêle à granulés</h3><p>Un chauffage d'appoint ou principal au bois, économique et pilotable.</p></article>
          <article class="card"><h3>VMC</h3><p>Une ventilation adaptée assainit l'air et préserve l'efficacité de votre chauffage.</p></article>
          <article class="card"><h3>Isolation</h3><p>Moins de pertes de chaleur, c'est une pompe à chaleur mieux dimensionnée et des factures plus basses.</p></article>
        </div>
        <p class="center"><a href="{{p}}eligibilite/" class="btn btn-green">Étudier mon projet {CHEV}</a></p>
      </div>
    </section>
{STEPS}
{CTA_BAND}"""
    page("particuliers", "Solutions de rénovation énergétique pour particuliers | Energia Group",
         "Pompe à chaleur air/eau et air/air, ballon thermodynamique, isolation : Energia Group, installateur RGE, gère votre projet et vos aides.",
         body, current="particuliers/")


def build_pac_air_eau():
    body = f"""{page_hero("Particuliers · Pompe à chaleur air/eau",
        "Pompe à chaleur air/eau : remplacez votre chaudière",
        "Jusqu'à 90 % financé par les aides de l'État*. Energia Group, installateur RGE QualiPAC, s'occupe de tout : étude, aides, installation et mise en service.")}
    <section class="section">
      <div class="container split">
        <div>
          <p class="eyebrow">Comment ça marche</p>
          <h2>La chaleur de l'air extérieur pour chauffer votre maison</h2>
          <p>La pompe à chaleur air/eau capte les calories présentes dans l'air extérieur, même par temps froid,
          et les transfère à l'eau de votre circuit de chauffage. Elle se raccorde à vos <strong>radiateurs à eau</strong>
          ou à votre <strong>plancher chauffant</strong> existants, et peut aussi produire votre <strong>eau chaude sanitaire</strong>.</p>
          <p>Pour 1 kWh d'électricité consommé, elle restitue en moyenne 3 à 4 kWh de chaleur&nbsp;: c'est ce qui en fait
          l'une des solutions les plus économiques pour remplacer une chaudière fioul, gaz ou un ancien système électrique.</p>
        </div>
        <ul class="checklist">
          <li>Jusqu'à 3&nbsp;000&nbsp;€ d'économies par an*</li>
          <li>Compatible avec vos radiateurs ou votre plancher chauffant</li>
          <li>Chauffage et eau chaude avec un seul équipement</li>
          <li>Éligible à MaPrimeRénov', aux CEE et à la TVA réduite*</li>
          <li>Matériel de grandes marques : Daikin, Mitsubishi Electric, Atlantic, Panasonic, De Dietrich</li>
        </ul>
      </div>
    </section>
    <section class="section section-alt">
      <div class="container">
        <div class="section-head"><p class="eyebrow">Pour qui&nbsp;?</p><h2>La pompe à chaleur air/eau est faite pour vous si…</h2></div>
        <div class="grid-3">
          <article class="card"><h3>Vous vous chauffez au fioul ou au gaz</h3><p>Le remplacement d'une chaudière fossile est le cas le mieux soutenu par les aides de l'État.</p></article>
          <article class="card"><h3>Vous avez un circuit de chauffage à eau</h3><p>Radiateurs ou plancher chauffant : la PAC se raccorde à votre installation existante.</p></article>
          <article class="card"><h3>Vous êtes propriétaire d'une maison</h3><p>Résidence principale ou logement mis en location : nous vérifions votre éligibilité aux aides.</p></article>
        </div>
      </div>
    </section>
{STEPS}
    <section class="section">
      <div class="container narrow">
        <div class="section-head"><p class="eyebrow">Questions fréquentes</p><h2>Pompe à chaleur air/eau : vos questions</h2></div>
        <div class="faq">{faq([
            ("Quelles aides pour une pompe à chaleur air/eau ?", "Selon vos revenus et votre logement : MaPrimeRénov', la prime CEE (Certificats d'Économies d'Énergie) et la TVA à taux réduit. Grâce à notre qualification RGE QualiPAC, nous montons le dossier et déduisons les aides directement de votre devis."),
            ("Faut-il changer mes radiateurs ?", "Dans la plupart des cas, non. Nous vérifions lors de l'étude que vos émetteurs sont compatibles et dimensionnons la pompe à chaleur en conséquence."),
            ("Combien de temps dure l'installation ?", "La pose est généralement réalisée en 1 à 2 jours, mise en service comprise. Nous vous accompagnons ensuite pour l'entretien."),
            ("Une pompe à chaleur fonctionne-t-elle quand il fait très froid ?", "Oui. Les modèles actuels continuent de produire de la chaleur à des températures extérieures négatives ; le dimensionnement réalisé lors de l'étude tient compte du climat de votre région."),
        ])}</div>
      </div>
    </section>
{CTA_BAND}"""
    page("particuliers/pompe-a-chaleur-air-eau",
         "Pompe à chaleur air/eau — jusqu'à 90 % financée* | Energia Group RGE QualiPAC",
         "Remplacez votre chaudière fioul ou gaz par une pompe à chaleur air/eau. Installateur RGE QualiPAC, aides déduites du devis, étude sous 48 h.",
         body, current="particuliers/")


def build_pac_air_air():
    body = f"""{page_hero("Particuliers · Pompe à chaleur air/air",
        "Pompe à chaleur air/air : chauffage et climatisation",
        "Une solution réversible pour chauffer votre logement en hiver et le rafraîchir en été, installée par des techniciens qualifiés.")}
    <section class="section">
      <div class="container split">
        <div>
          <p class="eyebrow">Comment ça marche</p>
          <h2>Un confort toute l'année</h2>
          <p>La pompe à chaleur air/air capte les calories de l'air extérieur et les diffuse dans votre logement
          par des unités intérieures (splits muraux, consoles ou gainable). En été, le cycle s'inverse pour
          rafraîchir vos pièces.</p>
          <p>C'est une alternative efficace aux radiateurs électriques, pour les maisons comme pour les appartements.</p>
        </div>
        <ul class="checklist">
          <li>Chauffage en hiver, climatisation en été</li>
          <li>Jusqu'à 3 fois moins d'électricité consommée que des radiateurs électriques</li>
          <li>Pilotage pièce par pièce</li>
          <li>Prime CEE possible sous conditions*</li>
        </ul>
      </div>
    </section>
    <section class="section section-alt">
      <div class="container narrow">
        <div class="notice"><strong>Bon à savoir&nbsp;:</strong> la pompe à chaleur air/air n'est pas éligible à MaPrimeRénov'.
        Si vous vous chauffez au fioul ou au gaz avec des radiateurs à eau, la <a href="{{p}}particuliers/pompe-a-chaleur-air-eau/">pompe à chaleur air/eau</a>
        est généralement plus adaptée et mieux financée. Nous vous conseillons la bonne solution lors de l'étude gratuite.</div>
      </div>
    </section>
{STEPS}
{CTA_BAND}"""
    page("particuliers/pompe-a-chaleur-air-air",
         "Pompe à chaleur air/air réversible | Energia Group",
         "Pompe à chaleur air/air : chauffage et climatisation réversible installés par Energia Group. Étude gratuite sous 48 h.",
         body, current="particuliers/")


def build_ballon():
    body = f"""{page_hero("Particuliers · Ballon thermodynamique",
        "Ballon thermodynamique : votre eau chaude moins chère",
        "Remplacez votre cumulus électrique par un chauffe-eau thermodynamique et réduisez fortement la consommation liée à votre eau chaude.")}
    <section class="section">
      <div class="container split">
        <div>
          <p class="eyebrow">Comment ça marche</p>
          <h2>Une petite pompe à chaleur dédiée à l'eau chaude</h2>
          <p>Le ballon thermodynamique utilise une pompe à chaleur intégrée pour chauffer l'eau du ballon à partir
          des calories de l'air. Il consomme jusqu'à trois fois moins d'électricité qu'un chauffe-eau électrique classique.</p>
        </div>
        <ul class="checklist">
          <li>Installation rapide, en remplacement de votre cumulus</li>
          <li>Jusqu'à 70 % d'économies sur la production d'eau chaude</li>
          <li>Éligible à MaPrimeRénov' et aux CEE sous conditions*</li>
          <li>Installé par une entreprise RGE QualiPAC (module ECS)</li>
        </ul>
      </div>
    </section>
{STEPS}
{CTA_BAND}"""
    page("particuliers/ballon-thermodynamique",
         "Ballon thermodynamique — aides de l'État* | Energia Group",
         "Chauffe-eau thermodynamique installé par Energia Group, RGE QualiPAC module ECS. Aides déduites du devis.",
         body, current="particuliers/")


def build_aides():
    body = f"""{page_hero("Particuliers · Aides à la rénovation",
        "Jusqu'à 90 % de votre projet financé par les aides de l'État*",
        "Nous montons votre dossier et déduisons les aides directement de votre devis : vous ne réglez que le reste à charge.")}
    <section class="section">
      <div class="container">
        <div class="section-head"><p class="eyebrow">Les dispositifs</p><h2>Les aides auxquelles vous pouvez prétendre</h2>
        <p class="section-sub">Les montants dépendent de vos revenus, de votre logement et des travaux réalisés. Ils évoluent régulièrement :
        nous vérifions votre situation au moment de l'étude.</p></div>
        <div class="grid-3">
          <article class="card"><h3>MaPrimeRénov'</h3><p>Aide de l'État pour les propriétaires, calculée selon les revenus du foyer et le type de travaux (pompe à chaleur air/eau, ballon thermodynamique…).</p></article>
          <article class="card"><h3>Prime CEE</h3><p>Les Certificats d'Économies d'Énergie, financés par les fournisseurs d'énergie, notamment pour le remplacement d'une chaudière fossile.</p></article>
          <article class="card"><h3>TVA à taux réduit</h3><p>Une TVA réduite s'applique sur les travaux de rénovation énergétique éligibles réalisés par une entreprise RGE.</p></article>
        </div>
      </div>
    </section>
    <section class="section section-alt">
      <div class="container split">
        <div>
          <p class="eyebrow">Pourquoi passer par nous</p>
          <h2>La qualification RGE, condition d'accès aux aides</h2>
          <p>Seuls les travaux réalisés par une entreprise qualifiée RGE ouvrent droit à MaPrimeRénov', aux CEE et à la
          TVA réduite. Energia Group est qualifiée <strong>RGE QualiPAC</strong> (n° QPAC/69638), vérifiable sur
          <a href="https://www.qualit-enr.org/annuaire/" target="_blank" rel="noopener">qualit-enr.org</a>.</p>
        </div>
        <ul class="checklist">
          <li>Vérification de votre éligibilité</li>
          <li>Montage complet du dossier</li>
          <li>Aides déduites directement du devis</li>
          <li>Vous ne réglez que le reste à charge</li>
        </ul>
      </div>
    </section>
{CTA_BAND}"""
    page("particuliers/aides-renovation",
         "Aides rénovation énergétique : MaPrimeRénov', CEE, TVA réduite | Energia Group",
         "MaPrimeRénov', prime CEE, TVA réduite : Energia Group, entreprise RGE QualiPAC, monte votre dossier et déduit les aides du devis.",
         body, current="particuliers/")


def build_eligibilite():
    body = """    <section class="page-hero dark topo compact">
      <div class="container">
        <p class="eyebrow">Test d'éligibilité</p>
        <h1>Testez votre éligibilité en 2 minutes</h1>
        <p class="lead">Gratuit et sans engagement. Un conseiller étudie votre dossier sous 48 h.</p>
      </div>
    </section>
    <section class="section">
      <div class="container narrow">
        <form class="wizard" id="wizard" data-lead-form data-source="Test d'éligibilité" novalidate>
          <div class="wizard-progress" aria-hidden="true"><span id="wizardBar"></span></div>
          <p class="wizard-count" id="wizardCount"></p>

          <fieldset class="wstep" data-step>
            <legend>Quel est votre projet&nbsp;?</legend>
            <div class="choices">
              <label><input type="radio" name="projet" value="Pompe à chaleur air/eau" required><span>Pompe à chaleur air/eau</span></label>
              <label><input type="radio" name="projet" value="Pompe à chaleur air/air"><span>Pompe à chaleur air/air</span></label>
              <label><input type="radio" name="projet" value="Ballon thermodynamique"><span>Ballon thermodynamique</span></label>
              <label><input type="radio" name="projet" value="Je ne sais pas"><span>Je ne sais pas, conseillez-moi</span></label>
            </div>
          </fieldset>

          <fieldset class="wstep" data-step>
            <legend>Comment chauffez-vous votre logement aujourd'hui&nbsp;?</legend>
            <div class="choices">
              <label><input type="radio" name="chauffage" value="fioul" required><span>Chaudière fioul</span></label>
              <label><input type="radio" name="chauffage" value="gaz"><span>Chaudière gaz</span></label>
              <label><input type="radio" name="chauffage" value="electrique"><span>Radiateurs électriques</span></label>
              <label><input type="radio" name="chauffage" value="bois"><span>Bois / charbon</span></label>
              <label><input type="radio" name="chauffage" value="autre"><span>Autre</span></label>
            </div>
          </fieldset>

          <fieldset class="wstep" data-step>
            <legend>Votre logement</legend>
            <div class="choices two">
              <label><input type="radio" name="logement" value="Maison" required><span>Maison</span></label>
              <label><input type="radio" name="logement" value="Appartement"><span>Appartement</span></label>
            </div>
            <div class="choices two">
              <label><input type="radio" name="statut" value="Propriétaire occupant" required><span>Propriétaire occupant</span></label>
              <label><input type="radio" name="statut" value="Propriétaire bailleur"><span>Propriétaire bailleur</span></label>
              <label><input type="radio" name="statut" value="Locataire"><span>Locataire</span></label>
            </div>
            <div class="choices two">
              <label><input type="radio" name="anciennete" value="Plus de 15 ans" required><span>Construit il y a plus de 15 ans</span></label>
              <label><input type="radio" name="anciennete" value="Entre 2 et 15 ans"><span>Entre 2 et 15 ans</span></label>
              <label><input type="radio" name="anciennete" value="Moins de 2 ans"><span>Moins de 2 ans</span></label>
            </div>
          </fieldset>

          <fieldset class="wstep" data-step>
            <legend>Votre foyer</legend>
            <p class="hint">Ces informations servent uniquement à estimer le niveau de vos aides.</p>
            <label class="field">Code postal du logement<input name="code_postal" inputmode="numeric" pattern="[0-9]{5}" maxlength="5" required></label>
            <label class="field">Nombre de personnes dans le foyer
              <select name="personnes" required><option value="">Choisir</option><option>1</option><option>2</option><option>3</option><option>4</option><option>5</option><option>6 ou plus</option></select></label>
            <label class="field">Revenu fiscal de référence du foyer
              <select name="revenus" required><option value="">Choisir</option>
                <option>Moins de 25 000 €</option><option>De 25 000 à 35 000 €</option><option>De 35 000 à 50 000 €</option>
                <option>De 50 000 à 75 000 €</option><option>Plus de 75 000 €</option><option>Je ne sais pas</option></select></label>
          </fieldset>

          <fieldset class="wstep" data-step>
            <legend>Vos coordonnées</legend>
            <label class="field">Nom et prénom<input name="nom" autocomplete="name" required></label>
            <label class="field">Téléphone<input name="telephone" type="tel" autocomplete="tel" required></label>
            <label class="field">Email<input name="email" type="email" autocomplete="email" required></label>
            <label class="consent"><input type="checkbox" name="consentement" required>
              J'accepte d'être recontacté par Energia Group au sujet de ma demande. Mes données ne sont ni cédées ni revendues.
              <a href="{p}mentions-legales/#confidentialite">En savoir plus</a></label>
          </fieldset>

          <div class="wstep wdone" data-done hidden>
            <h2>Merci, votre demande est bien enregistrée&nbsp;!</h2>
            <p>Un conseiller Energia Group étudie votre dossier et vous rappelle sous 48 h pour vous présenter les aides auxquelles vous avez droit.</p>
            <p class="small">Rappel : nos conseillers ne pratiquent pas de démarchage abusif.</p>
          </div>

          <div class="wizard-nav">
            <button type="button" class="btn btn-outline" id="wPrev">Retour</button>
            <button type="button" class="btn btn-green" id="wNext">Continuer ›</button>
            <button type="submit" class="btn btn-green" id="wSubmit">Recevoir mon étude gratuite ›</button>
          </div>
          <p class="form-status" role="status" aria-live="polite"></p>
        </form>
      </div>
    </section>"""
    page("eligibilite", "Testez votre éligibilité aux aides pompe à chaleur | Energia Group",
         "Test gratuit en 2 minutes : vérifiez votre éligibilité aux aides de l'État pour votre pompe à chaleur. Réponse sous 48 h.",
         body)


def build_pro():
    body = f"""{page_hero("Espace Pro", "Performance énergétique et conformité de vos bâtiments",
        "Tertiaire, collectif, industriel : nous accompagnons les professionnels dans leurs obligations réglementaires et la réduction de leurs consommations.", ctas=False)}
    <section class="section">
      <div class="container">
        <div class="grid-3">
          <article class="card" id="decret-bacs"><h3>Décret BACS</h3><p>Mise en place de systèmes d'automatisation et de contrôle des bâtiments tertiaires (GTB) pour piloter chauffage et climatisation.</p></article>
          <article class="card" id="cpe"><h3>Contrat de Performance Énergétique</h3><p>Un engagement sur des économies d'énergie mesurables, avec un plan de travaux et un suivi des performances.</p></article>
          <article class="card" id="loi-climat"><h3>Loi Climat et Résilience</h3><p>Anticipez les obligations de rénovation et améliorez la performance de votre patrimoine immobilier.</p></article>
        </div>
      </div>
    </section>
    <section class="section section-alt">
      <div class="container split">
        <div><p class="eyebrow">Contact professionnels</p><h2>Parlons de votre bâtiment</h2>
        <p>Décrivez-nous votre site et vos enjeux : un interlocuteur dédié revient vers vous rapidement.</p></div>
        <div class="form-card">
          <form class="lead-form" data-lead-form data-source="Espace Pro" novalidate>
            <label>Société<input name="societe" autocomplete="organization" required></label>
            <label>Nom et prénom<input name="nom" autocomplete="name" required></label>
            <label>Téléphone<input name="telephone" type="tel" autocomplete="tel" required></label>
            <label>Email<input name="email" type="email" autocomplete="email" required></label>
            <label>Votre besoin<textarea name="message" rows="4"></textarea></label>
            <label class="consent"><input type="checkbox" name="consentement" required>
              J'accepte d'être recontacté par Energia Group au sujet de ma demande.</label>
            <button class="btn btn-green btn-block" type="submit">Envoyer {CHEV}</button>
            <p class="form-status" role="status" aria-live="polite"></p>
          </form>
        </div>
      </div>
    </section>"""
    page("professionnels", "Espace Pro — Décret BACS, CPE, Loi Climat et Résilience | Energia Group",
         "Energia Group accompagne les professionnels : Décret BACS, Contrat de Performance Énergétique, Loi Climat et Résilience.",
         body, current="professionnels/")


def build_apropos():
    s = SOCIETE
    rows = "".join(f"<tr><th>{k}</th><td>{v}</td></tr>" for k, v in [
        ("Dénomination", s["nom"]), ("SIREN", s["siren"]), ("SIRET (établissement)", s["siret"]),
        ("Siège", s["siege"]), ("Activité (APE)", s["ape"]), ("Qualification", s["qualif"]),
        ("Assurances", s["assurances"])])
    body = f"""{page_hero("Qui sommes-nous", "Energia Group, votre partenaire en rénovation énergétique",
        "Installateur spécialisé en pompes à chaleur, chauffage et solutions d'efficacité énergétique, au service des particuliers et des professionnels.", ctas=False)}
    <section class="section">
      <div class="container split">
        <div>
          <p class="eyebrow">Notre métier</p>
          <h2>De l'étude à la maintenance</h2>
          <p>Energia Group est une société spécialisée dans l'étude, la vente, l'installation et la maintenance de systèmes
          de chauffage et de climatisation performants&nbsp;: pompes à chaleur, ventilation, traitement d'air et d'eau,
          plomberie et isolation. Nous intervenons aussi bien sur des installations individuelles que collectives,
          tertiaires et industrielles.</p>
          <p>Notre mission&nbsp;: rendre la rénovation énergétique simple et accessible, en accompagnant chaque client de
          l'audit de son projet jusqu'à l'obtention de ses aides de l'État.</p>
        </div>
        <ul class="guarantees">
          <li><span class="g-icon" aria-hidden="true">1</span><div><h3>Accompagnement complet</h3><p>Du diagnostic à la mise en service.</p></div></li>
          <li><span class="g-icon" aria-hidden="true">RGE</span><div><h3>Artisans qualifiés RGE QualiPAC</h3><p>Gage de qualité et condition d'accès aux aides.</p></div></li>
          <li><span class="g-icon" aria-hidden="true">€</span><div><h3>Transparence</h3><p>Aides déduites directement de votre devis.</p></div></li>
        </ul>
      </div>
    </section>
    <section class="section section-alt">
      <div class="container narrow">
        <h2>Informations légales</h2>
        <table class="legal">{rows}</table>
      </div>
    </section>
{CTA_BAND}"""
    page("a-propos", "À propos — Energia Group, installateur RGE QualiPAC",
         "Energia Group : étude, installation et maintenance de pompes à chaleur et solutions de rénovation énergétique. RGE QualiPAC n° QPAC/69638.",
         body, current="a-propos/")


def build_contact():
    body = f"""{page_hero("Contact", "Contactez Energia Group",
        "Une question, un projet, un besoin de SAV ? Laissez-nous vos coordonnées, nous vous recontactons rapidement.", ctas=False)}
    <section class="section">
      <div class="container split">
        <div>
          <h2>Nos coordonnées</h2>
          <ul class="contact-list">
            <li><strong>Téléphone</strong><span data-contact="phone">—</span></li>
            <li><strong>Email</strong><span data-contact="email">—</span></li>
            <li><strong>Siège</strong><span>{SOCIETE['siege']}</span></li>
          </ul>
          <div class="sav" id="sav">
            <h2>Service après-vente</h2>
            <p>Vous êtes client et rencontrez un problème avec votre installation&nbsp;? Sélectionnez «&nbsp;SAV&nbsp;» dans le
            formulaire en précisant votre adresse et la nature de la panne&nbsp;: notre équipe technique revient vers vous.</p>
          </div>
        </div>
        <div class="form-card">
          <form class="lead-form" data-lead-form data-source="Contact" novalidate>
            <label>Objet
              <select name="objet"><option>Nouveau projet</option><option>SAV</option><option>Professionnel</option><option>Autre</option></select></label>
            <label>Nom et prénom<input name="nom" autocomplete="name" required></label>
            <label>Téléphone<input name="telephone" type="tel" autocomplete="tel" required></label>
            <label>Email<input name="email" type="email" autocomplete="email"></label>
            <label>Code postal<input name="code_postal" inputmode="numeric" maxlength="5"></label>
            <label>Message<textarea name="message" rows="4"></textarea></label>
            <label class="consent"><input type="checkbox" name="consentement" required>
              J'accepte d'être recontacté par Energia Group au sujet de ma demande.
              <a href="{{p}}mentions-legales/#confidentialite">En savoir plus</a></label>
            <button class="btn btn-green btn-block" type="submit">Envoyer {CHEV}</button>
            <p class="form-status" role="status" aria-live="polite"></p>
          </form>
        </div>
      </div>
    </section>"""
    page("contact", "Contact et SAV | Energia Group",
         "Contactez Energia Group pour un projet de pompe à chaleur, une demande professionnelle ou le SAV.",
         body, current="contact/")


def build_legal():
    s = SOCIETE
    body = f"""{page_hero("Informations légales", "Mentions légales &amp; confidentialité", "", ctas=False)}
    <section class="section">
      <div class="container narrow prose">
        <h2>Éditeur du site</h2>
        <p>{s['nom']}<br>Siège social : {s['siege']}<br>SIREN : {s['siren']} — SIRET : {s['siret']}<br>
        Activité : {s['ape']}<br>Qualification : {s['qualif']}<br>Assurances : {s['assurances']}</p>
        <p>Directeur de la publication : <span class="todo">[à compléter]</span><br>
        Contact : <span data-contact="email">—</span></p>
        <h2>Hébergement</h2>
        <p><span class="todo">[à compléter selon l'hébergeur retenu]</span></p>
        <h2 id="confidentialite">Politique de confidentialité</h2>
        <p>Les informations recueillies via les formulaires du site (nom, coordonnées, caractéristiques du logement et du
        foyer) sont utilisées par Energia Group uniquement pour étudier votre demande, vérifier votre éligibilité aux aides
        et vous recontacter. Elles ne sont ni cédées ni revendues à des tiers.</p>
        <p>Elles sont conservées pendant la durée nécessaire au traitement de votre demande et, au plus, 3 ans après le
        dernier contact. Conformément au RGPD, vous disposez d'un droit d'accès, de rectification, d'effacement et
        d'opposition, que vous pouvez exercer en nous écrivant à l'adresse ci-dessus. Vous pouvez également introduire
        une réclamation auprès de la CNIL.</p>
        <p>Vous pouvez vous inscrire gratuitement sur la liste d'opposition au démarchage téléphonique Bloctel.</p>
        <h2>Aides de l'État</h2>
        <p>*Les montants et taux de financement mentionnés sur ce site (« jusqu'à 90 % ») sont donnés sous conditions
        d'éligibilité (ressources du foyer, logement, travaux) et selon la réglementation en vigueur.</p>
      </div>
    </section>"""
    page("mentions-legales", "Mentions légales et confidentialité | Energia Group",
         "Mentions légales et politique de confidentialité du site Energia Group.", body)


if __name__ == "__main__":
    build_home()
    build_particuliers()
    build_pac_air_eau()
    build_pac_air_air()
    build_ballon()
    build_aides()
    build_eligibilite()
    build_pro()
    build_apropos()
    build_contact()
    build_legal()
