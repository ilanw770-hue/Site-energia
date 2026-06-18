# Energia Group — Site internet

Site vitrine moderne et responsive pour **Energia Group**, entreprise spécialisée
dans les solutions d'énergie renouvelable (solaire, éolien, stockage, efficacité
énergétique).

## ⚡ Aperçu

Site statique en HTML / CSS / JavaScript (sans dépendance ni build), prêt à être
déployé sur n'importe quel hébergement statique (GitHub Pages, Netlify, Vercel,
serveur Apache/Nginx…).

## 📁 Structure

```
.
├── index.html        # Page principale (toutes les sections)
├── css/
│   └── styles.css    # Styles, design system et responsive
├── js/
│   └── main.js       # Menu mobile, animations, compteurs, formulaire
└── README.md
```

## 🧩 Sections

- **Hero** — accroche et appels à l'action
- **Services** — 6 expertises (solaire, éolien, stockage, efficacité, audit, maintenance)
- **À propos** — présentation de l'entreprise
- **Réalisations** — chiffres clés animés
- **Méthode** — déroulé du projet en 4 étapes
- **Témoignages** — avis clients
- **Contact** — coordonnées et formulaire avec validation

## 🚀 Lancer en local

Aucune installation requise. Ouvrez `index.html` dans un navigateur, ou servez
le dossier :

```bash
python3 -m http.server 8000
# puis ouvrez http://localhost:8000
```

## 🔧 Personnalisation

- **Couleurs & design** : variables CSS dans `:root` (fichier `css/styles.css`).
- **Contenu** : éditez directement `index.html`.
- **Formulaire** : l'envoi est simulé dans `js/main.js`. Connectez-le à un
  service d'emailing (Formspree, EmailJS, backend…) pour la mise en production.

## ✅ Caractéristiques

- 100 % responsive (mobile, tablette, desktop)
- Accessible (HTML sémantique, ARIA, navigation clavier)
- Respecte `prefers-reduced-motion`
- Léger et rapide, sans framework
