# Jonathan Kakesa | Cognito Inc. - Portfolio Website

Une application web moderne et professionnelle présentant Jonathan Kakesa, CEO et fondateur de Cognito Inc., en tant que freelance, entrepreneur et créateur de projets technologiques innovants.

## 🚀 Fonctionnalités

### Pages principales
- **Accueil** : Hero section avec présentation, projets phares et témoignages
- **À propos** : Biographie détaillée, compétences et liens vers Cognito Inc.
- **Projets** : Grille animée des réalisations avec liens GitHub
- **Services** : Détail des prestations freelance et packages startup
- **Contact** : Formulaire de contact avec informations et FAQ

### Fonctionnalités techniques
- ✨ Design moderne avec thème sombre et accents bleus électriques
- 🎨 Animations fluides avec GSAP (ScrollTrigger, fade-in, parallax)
- 📱 Responsive design (mobile, tablette, desktop)
- 🔧 Interface d'administration Flask-Admin
- 📧 Système de contact avec Flask-Mail
- 🗄️ Base de données SQLite avec modèles pour projets et témoignages
- 🔒 Formulaires sécurisés avec Flask-WTF
- ⚡ Optimisations SEO et meta tags
- 🎯 Google Analytics ready

## 🛠️ Technologies utilisées

### Backend
- **Flask** - Framework web Python
- **SQLAlchemy** - ORM pour la base de données
- **Flask-Admin** - Interface d'administration
- **Flask-Mail** - Envoi d'emails
- **Flask-WTF** - Gestion des formulaires

### Frontend
- **TailwindCSS** - Framework CSS utilitaire
- **GSAP** - Animations JavaScript avancées
- **HTML5** - Structure sémantique
- **JavaScript ES6+** - Interactions dynamiques

### Base de données
- **SQLite** - Base de données légère (développement)
- **PostgreSQL** - Recommandé pour la production

## 📦 Installation

### Prérequis
- Python 3.8+
- pip (gestionnaire de packages Python)

### Étapes d'installation

1. **Cloner le projet**
```bash
git clone <repository-url>
cd JonathanKakesa-Freelancer
```

2. **Créer un environnement virtuel**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

3. **Installer les dépendances**
```bash
pip install -r requirements.txt
```

4. **Configuration de l'environnement**
```bash
# Copier le fichier .env et modifier les valeurs
cp .env.example .env
```

Modifier le fichier `.env` avec vos propres valeurs :
```env
SECRET_KEY=votre-clé-secrète-très-sécurisée
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=votre-email@gmail.com
MAIL_PASSWORD=votre-mot-de-passe-app
DATABASE_URL=sqlite:///cognito.db
```

5. **Initialiser la base de données**
```bash
python app.py
```

6. **Lancer l'application**
```bash
python app.py
```

L'application sera accessible sur `http://localhost:5000`

## 🔧 Configuration

### Configuration email
Pour activer l'envoi d'emails via le formulaire de contact :

1. **Gmail** : Activez l'authentification à 2 facteurs et générez un mot de passe d'application
2. **Autres fournisseurs** : Modifiez les paramètres SMTP dans `.env`

### Configuration base de données
Pour utiliser PostgreSQL en production :

```env
DATABASE_URL=postgresql://username:password@localhost/cognito_db
```

### Google Analytics
Remplacez `GA_MEASUREMENT_ID` dans `templates/base.html` par votre ID de suivi.

## 🚀 Déploiement

### Render (Recommandé)

1. **Créer un compte sur Render.com**
2. **Connecter votre repository GitHub**
3. **Configurer le service web** :
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
   - Environment: Python 3

4. **Variables d'environnement** :
   Ajouter toutes les variables du fichier `.env`

### Railway

1. **Installer Railway CLI**
```bash
npm install -g @railway/cli
```

2. **Déployer**
```bash
railway login
railway init
railway up
```

### Vercel

1. **Installer Vercel CLI**
```bash
npm install -g vercel
```

2. **Créer vercel.json**
```json
{
  "builds": [
    {
      "src": "app.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "app.py"
    }
  ]
}
```

3. **Déployer**
```bash
vercel
```

## 📁 Structure du projet

```
JonathanKakesa-Freelancer/
├── app.py                 # Application Flask principale
├── requirements.txt       # Dépendances Python
├── .env                  # Variables d'environnement
├── README.md             # Documentation
├── templates/            # Templates HTML
│   ├── base.html         # Template de base
│   ├── home.html         # Page d'accueil
│   ├── about.html        # Page à propos
│   ├── projects.html     # Page projets
│   ├── services.html     # Page services
│   └── contact.html      # Page contact
├── static/               # Fichiers statiques
│   ├── css/             # Styles CSS personnalisés
│   ├── js/              # Scripts JavaScript
│   │   └── main.js      # Script principal avec animations
│   └── images/          # Images et assets
└── cognito.db           # Base de données SQLite (générée)
```

## 🎨 Personnalisation

### Couleurs et thème
Les couleurs principales sont définies dans `templates/base.html` :
```javascript
colors: {
    'electric-blue': '#00D4FF',
    'dark-bg': '#0A0A0A',
    'dark-card': '#1A1A1A',
    'dark-border': '#2A2A2A'
}
```

### Contenu
1. **Projets** : Ajoutez vos projets via l'interface admin `/admin`
2. **Témoignages** : Gérez les avis clients dans l'admin
3. **Informations personnelles** : Modifiez les templates HTML

### Animations
Les animations GSAP sont configurées dans `static/js/main.js`. Vous pouvez :
- Modifier les durées et effets
- Ajouter de nouvelles animations
- Personnaliser les triggers de scroll

## 🔐 Administration

Accédez à l'interface d'administration sur `/admin` pour :
- Gérer les projets
- Modérer les témoignages
- Consulter les messages de contact

## 📧 Support et Contact

- **Email** : jonathan@cognito-inc.com
- **GitHub** : [Cognito Inc.](https://github.com/cognito-inc)
- **Website** : [Cognito Inc.](https://cognito-inc.com)

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :
1. Fork le projet
2. Créer une branche pour votre fonctionnalité
3. Commiter vos changements
4. Pousser vers la branche
5. Ouvrir une Pull Request

## 🎯 Roadmap

- [ ] Mode sombre/clair basculable
- [ ] Section partenaires/collaborations
- [ ] Intégration chatbot IA
- [ ] Blog/actualités
- [ ] Multilingue (FR/EN)
- [ ] PWA (Progressive Web App)

---

**Développé avec ❤️ par Jonathan Kakesa | Cognito Inc.**