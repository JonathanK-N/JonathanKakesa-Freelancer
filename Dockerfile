# Dockerfile pour l'application Jonathan Kakesa | Cognito Inc.

# Utiliser Python 3.11 comme image de base
FROM python:3.11-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de dépendances
COPY requirements.txt .

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code de l'application
COPY . .

# Créer un utilisateur non-root pour la sécurité
RUN useradd --create-home --shell /bin/bash app && chown -R app:app /app
USER app

# Exposer le port 5000
EXPOSE 5000

# Variables d'environnement
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# Commande de démarrage
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]