#!/usr/bin/env python3
"""
Script de démarrage pour l'application Jonathan Kakesa | Cognito Inc.
"""

from app import app, init_db

if __name__ == '__main__':
    # Initialiser la base de données
    print("🚀 Initialisation de la base de données...")
    init_db()
    print("✅ Base de données initialisée avec succès!")
    
    print("🌟 Démarrage de l'application Jonathan Kakesa | Cognito Inc.")
    print("📱 Application accessible sur : http://localhost:5000")
    print("🔧 Interface admin accessible sur : http://localhost:5000/admin")
    print("💡 Appuyez sur Ctrl+C pour arrêter l'application")
    
    # Lancer l'application
    app.run(debug=True, host='0.0.0.0', port=5000)