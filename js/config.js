/* ============================================================
   Energia Group — Configuration du site (à remplir avant mise en ligne)
   ============================================================ */
window.ENERGIA_CONFIG = {
  // Coordonnées affichées sur le site (page Contact, mentions légales).
  phone: '',            // ex. '01 23 45 67 89'
  email: '',            // ex. 'contact@energia-group.fr'

  // Réception des demandes (test d'éligibilité, rappel, contact, SAV).
  // Adresse d'un service de formulaires qui accepte un POST JSON et renvoie
  // une réponse 2xx (ex. Formspree : 'https://formspree.io/f/xxxxxxx').
  // Tant qu'elle est vide, le site ouvre la messagerie du visiteur avec la
  // demande pré-remplie à destination de `email` ci-dessus.
  formEndpoint: '',

  // Réseaux sociaux (laisser vide pour masquer).
  socials: {
    facebook: '',
    instagram: '',
    linkedin: ''
  }
};
