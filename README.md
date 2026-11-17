# Energia Group — Site internet

Site vitrine d'**Energia Group** (SAS, SIREN 909 268 286), installateur RGE QualiPAC
de pompes à chaleur. Contenu et charte : *Energia Group Cahier des charges.docx*.

Priorité actuelle : le parcours **Particuliers (B2C) pompe à chaleur**, avec le
test d'éligibilité en 5 étapes qui génère les demandes de rappel.

## Pages

| URL | Contenu |
| --- | --- |
| `/` | Accueil (12 sections du cahier des charges) |
| `/particuliers/` | Solutions particuliers (+ poêle, VMC, isolation) |
| `/particuliers/pompe-a-chaleur-air-eau/` | PAC air/eau |
| `/particuliers/pompe-a-chaleur-air-air/` | PAC air/air |
| `/particuliers/ballon-thermodynamique/` | Ballon thermodynamique |
| `/particuliers/aides-renovation/` | MaPrimeRénov', CEE, TVA réduite |
| `/eligibilite/` | Test d'éligibilité (formulaire en étapes) |
| `/professionnels/` | Espace Pro : Décret BACS, CPE, Loi Climat |
| `/a-propos/`, `/contact/` (+ SAV), `/mentions-legales/` | |

## Avant la mise en ligne — `js/config.js`

- `formEndpoint` : adresse qui reçoit les demandes (POST JSON), par ex. un
  formulaire Formspree. **Sans elle ni `email`, les formulaires affichent une
  erreur et aucune demande n'est reçue.**
- `email`, `phone` : coordonnées affichées (page Contact, mentions légales).
- `socials` : liens réseaux sociaux du pied de page.

À compléter aussi : directeur de la publication et hébergeur dans
`/mentions-legales/` (marqués `[à compléter]`), photos de chantiers et logos
fabricants (cahier des charges, section 7).

## Modifier le site

Le site est 100 % statique (HTML/CSS/JS, sans dépendance). L'en-tête, le pied de
page et les textes sont dans `tools/build.py` :

```bash
python3 tools/build.py          # régénère les pages HTML
python3 -m http.server 8000     # aperçu sur http://localhost:8000
```

Commitez ensuite les fichiers HTML générés. Les chemins sont relatifs : le site
fonctionne à la racine d'un domaine comme dans un sous-dossier (GitHub Pages).
