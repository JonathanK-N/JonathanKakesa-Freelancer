# 🚀 Démarrage Rapide - Jonathan Kakesa | Cognito Inc.

## Installation Express (5 minutes)

### 1. Prérequis
- Python 3.8+ installé
- Git installé

### 2. Installation
```bash
# Cloner le projet
git clone <repository-url>
cd JonathanKakesa-Freelancer

# Créer l'environnement virtuel
python -m venv venv

# Activer l'environnement (Windows)
venv\Scripts\activate

# Activer l'environnement (macOS/Linux)
source venv/bin/activate

# Installer les dépendances
pip install -r requirements.txt
```

### 3. Configuration
```bash
# Copier le fichier d'environnement
copy .env.example .env  # Windows
cp .env.example .env    # macOS/Linux

# Modifier .env avec vos paramètres (optionnel pour le test)
```

### 4. Lancement
```bash
# Démarrer l'application
python run.py
```

🎉 **L'application est maintenant accessible sur http://localhost:5000**

## 🔧 Interface d'Administration

Accédez à l'interface admin sur : http://localhost:5000/admin

Vous pouvez :
- Ajouter/modifier des projets
- Gérer les témoignages clients
- Consulter les messages de contact

## 📱 Pages Disponibles

- **Accueil** : http://localhost:5000/
- **À propos** : http://localhost:5000/about
- **Projets** : http://localhost:5000/projects
- **Services** : http://localhost:5000/services
- **Contact** : http://localhost:5000/contact

## 🐳 Démarrage avec Docker

```bash
# Construire et lancer avec Docker Compose
docker-compose up --build

# Ou avec Docker uniquement
docker build -t cognito-app .
docker run -p 5000:5000 cognito-app
```

## 🚀 Déploiement Rapide

### Render
1. Connectez votre repository GitHub à Render
2. Configurez les variables d'environnement
3. Déployez automatiquement

### Railway
```bash
npm install -g @railway/cli
railway login
railway init
railway up
```

### Vercel
```bash
npm install -g vercel
vercel
```

## 🎨 Personnalisation Rapide

### Modifier les informations personnelles
1. Éditez les templates dans `templates/`
2. Modifiez les données dans `app.py` (fonction `init_db`)

### Changer les couleurs
1. Modifiez les couleurs dans `templates/base.html` (section TailwindCSS config)
2. Personnalisez `static/css/custom.css`

### Ajouter des projets
1. Accédez à l'admin : http://localhost:5000/admin
2. Cliquez sur "Project" → "Create"
3. Remplissez les informations et sauvegardez

## 🆘 Dépannage

### Erreur de port déjà utilisé
```bash
# Changer le port dans run.py ou utiliser :
python run.py --port 8000
```

### Problème de base de données
```bash
# Supprimer la base et relancer
rm cognito.db
python run.py
```

### Erreur d'email
- Vérifiez la configuration SMTP dans `.env`
- Pour Gmail, utilisez un mot de passe d'application

## 📞 Support

- **Email** : jonathan@cognito-inc.com
- **Documentation complète** : Voir README.md
- **Issues** : Créez une issue sur GitHub

---

**Développé avec ❤️ par Jonathan Kakesa | Cognito Inc.**