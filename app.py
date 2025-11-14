from flask import Flask, render_template, request, flash, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_mail import Mail, Message
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

try:
    import requests
    from requests.exceptions import RequestException
except ImportError:
    requests = None

    class RequestException(Exception):
        """Fallback exception when requests is absent."""
        pass

# Charger les variables d'environnement
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///cognito.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Configuration Mail
app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT', 587))
app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS', 'True').lower() == 'true'
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')

# Initialisation des extensions
db = SQLAlchemy(app)
mail = Mail(app)
admin = Admin(app, name='Cognito Admin', template_mode='bootstrap4')

GITHUB_USERNAME = "JonathanK-N"
GITHUB_CACHE_DURATION = timedelta(hours=3)
GITHUB_CACHE = {"profile": None, "repos": [], "timestamp": None}

GITHUB_FALLBACK_PROFILE = {
    "name": "Jonathan Kakesa",
    "login": GITHUB_USERNAME,
    "followers": 18,
    "public_repos": 49,
    "public_gists": 1,
    "html_url": f"https://github.com/{GITHUB_USERNAME}",
    "blog": "https://cognito-inc.ca/"
}

GITHUB_FALLBACK_REPOS = [
    {
        "name": "mechatronic-robot-arm-control",
        "description": "Système de contrôle pour bras robotique 6 DOF avec STM32, capteurs IoT et pipeline IA.",
        "html_url": "https://github.com/JonathanK-N/mechatronic-robot-arm-control",
        "language": "C++",
        "stargazers_count": 7,
        "pushed_at": "2024-09-28T00:00:00Z"
    },
    {
        "name": "Plateforme-Foi-et-Raison",
        "description": "Plateforme communautaire multimédia Foi & Raison avec Q&A et back-office complet.",
        "html_url": "https://github.com/JonathanK-N/Plateforme-Foi-et-Raison",
        "language": "HTML",
        "stargazers_count": 1,
        "pushed_at": "2024-07-10T00:00:00Z"
    },
    {
        "name": "Portfolio",
        "description": "Base de portfolio modulaire pour démontrer les expertises Cognito.",
        "html_url": "https://github.com/JonathanK-N/Portfolio",
        "language": "HTML",
        "stargazers_count": 1,
        "pushed_at": "2024-05-22T00:00:00Z"
    },
    {
        "name": "FaceBoom",
        "description": "Prototype d'automatisation Python pour tests de sécurité offensive.",
        "html_url": "https://github.com/JonathanK-N/FaceBoom",
        "language": "Python",
        "stargazers_count": 1,
        "pushed_at": "2023-11-01T00:00:00Z"
    }
]

PORTFOLIO_SITES = [
    {
        "name": "Cognito Inc. HQ",
        "url": "https://cognito-inc.ca/",
        "sector": "Corporate & Innovation Studio",
        "description": "Maison mère, hub de services et laboratoire produit pour la communauté Cognito.",
        "stack": ["Flask", "Next.js", "Tailwind", "AWS"],
        "status": "Live"
    },
    {
        "name": "ULC Digital Campus",
        "url": "https://ulc-cognito-web.com/",
        "sector": "Éducation | Loyola du Congo / ICAM",
        "description": "Portail campus + LMS avec admissions, IA pédagogique et outils de suivi.",
        "stack": ["Python", "PostgreSQL", "AI assistants"],
        "status": "Production"
    },
    {
        "name": "PrimaPhoto",
        "url": "https://primaphoto.ca/",
        "sector": "E-commerce & Créateurs",
        "description": "Boutique photo/vidéo avec configurateur, gestion d'ateliers et paiement intégré.",
        "stack": ["Next.js", "Shopify", "Serverless"],
        "status": "Live"
    },
    {
        "name": "Cognito Chatt",
        "url": "https://cognito-chatt.com/",
        "sector": "IA conversationnelle",
        "description": "Suite d'agents IA multilingues pour support client et automatisation commerciale.",
        "stack": ["Python", "LangChain", "Azure OpenAI"],
        "status": "Beta"
    },
    {
        "name": "Questions pour un Disciple",
        "url": "https://questions-pour-un-disciple.com/",
        "sector": "Médias & Communautés",
        "description": "Plateforme interactive de contenus religieux et d'émissions live.",
        "stack": ["Laravel", "Live streaming", "Redis"],
        "status": "Live"
    },
    {
        "name": "Lyft ICC",
        "url": "https://lyft-icc.com/",
        "sector": "Mobilité & Transport",
        "description": "Solution de dispatching et de suivi pour chauffeurs partenaires ICC.",
        "stack": ["Flutter", "Firebase", "Stripe"],
        "status": "Piloté"
    },
    {
        "name": "Green-Kin",
        "url": "https://green-kin.com/",
        "sector": "Impact & Climat",
        "description": "Plateforme de gestion d'énergies propres et suivi carbone pour Kinshasa.",
        "stack": ["Node.js", "IoT", "GIS"],
        "status": "Prototype"
    }
]

VENTURE_MILESTONES = [
    {
        "year": "2016",
        "title": "Création de Cognito Inc.",
        "details": "Studio d'innovation fondé entre Kinshasa et Montréal pour livrer des produits digitaux à haute valeur."
    },
    {
        "year": "2019",
        "title": "Primo-commerce & culture",
        "details": "Lancement de PrimaPhoto et premiers médias communautaires avec Questions pour un Disciple."
    },
    {
        "year": "2021",
        "title": "Éducation augmentée",
        "details": "Déploiement des plateformes ULC/ICAM avec un LMS propriétaire et assistants IA."
    },
    {
        "year": "2023",
        "title": "IA conversationnelle",
        "details": "Cognito Chatt voit le jour, industrialisant les agents personnalisés pour PME africaines."
    },
    {
        "year": "2024+",
        "title": "Impact & scaling",
        "details": "Programmes Green-Kin, Lyft ICC et industrialisation de la stack Cognito sur l'international."
    }
]

SPOTLIGHT_PROJECTS = [
    {
        "title": "Atlas Robotics Suite",
        "category": "Mécatronique & Robotique",
        "summary": "Contrôle d'un bras robotique 6 DOF avec vision embarquée, cinématique inverse et supervision cloud.",
        "image": "https://images.unsplash.com/photo-1581091012184-7c54c7d39cfa?auto=format&fit=crop&w=900&q=80",
        "tech": ["STM32", "ROS2", "TensorFlow Lite"],
        "case_url": "https://github.com/JonathanK-N/mechatronic-robot-arm-control",
        "github_url": "https://github.com/JonathanK-N/mechatronic-robot-arm-control"
    },
    {
        "title": "Cognito Neural Lab",
        "category": "IA Générative",
        "summary": "Construction de modèles maison pour copilotes sectoriels et agents conversationnels multilingues.",
        "image": "https://images.unsplash.com/photo-1503023345310-bd7c1de61c7d?auto=format&fit=crop&w=900&q=80",
        "tech": ["LangChain", "Azure OpenAI", "FastAPI"],
        "case_url": "https://cognito-chatt.com/",
        "github_url": "https://github.com/JonathanK-N/Plateforme-Foi-et-Raison"
    },
    {
        "title": "PrimaPhoto Experience",
        "category": "E-commerce créatif",
        "summary": "Plateforme immersive pour studios photo/vidéo avec configurateur, réservations et ateliers live.",
        "image": "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?auto=format&fit=crop&w=900&q=80",
        "tech": ["Next.js", "Shopify", "Serverless"],
        "case_url": "https://primaphoto.ca/",
        "github_url": "https://github.com/JonathanK-N/Portfolio"
    },
    {
        "title": "Green-Kin Energy Hub",
        "category": "Data & Climat",
        "summary": "Command center pour surveiller micro-grids, capteurs IoT et indicateurs ESG en temps réel.",
        "image": "https://images.unsplash.com/photo-1509391366360-2e959784a276?auto=format&fit=crop&w=900&q=80",
        "tech": ["Node.js", "IoT Core", "TimescaleDB"],
        "case_url": "https://green-kin.com/",
        "github_url": "https://github.com/JonathanK-N/JonathanK-N"
    }
]

PARTNER_NETWORK = [
    {"name": "Amazon Web Services", "tagline": "Build on AWS Activate", "url": "https://aws.amazon.com/", "segment": "Cloud"},
    {"name": "Microsoft Azure", "tagline": "Azure AI & App Services", "url": "https://azure.microsoft.com/", "segment": "Cloud"},
    {"name": "Railway", "tagline": "Infra serverless & previews", "url": "https://railway.app/", "segment": "DevOps"},
    {"name": "Polytechnique Montréal", "tagline": "Recherche & programmes d'innovation", "url": "https://www.polymtl.ca/", "segment": "Académique"},
    {"name": "Université Loyola du Congo - ICAM", "tagline": "Transformation numérique campus", "url": "https://ulc-cognito-web.com/", "segment": "Education"},
    {"name": "ICAM", "tagline": "Ingénierie & fabriques numériques", "url": "https://www.icam.fr/", "segment": "Education"},
    {"name": "Data-IT", "tagline": "Alliances data & cybersécurité", "url": "#", "segment": "Data"},
]

WORKFLOW_STEPS = [
    {"title": "Exploration", "description": "Interviews, audit et vision partagée avec les équipes dirigeantes."},
    {"title": "Design system", "description": "Branding, architecture produit, expériences UX/UI et prototypes."},
    {"title": "Build & IA", "description": "Développement full-stack, intégration IA et pipelines de déploiement."},
    {"title": "Scale", "description": "Formation, transfert, monitoring et growth loops industrialisés."}
]

# Modèles de base de données
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    github_url = db.Column(db.String(200), nullable=False)
    stack = db.Column(db.String(200), nullable=False)
    image_url = db.Column(db.String(200), default='default-project.jpg')
    detailed_description = db.Column(db.Text)
    demo_url = db.Column(db.String(200))
    features = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Testimonial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(100), nullable=False)
    company = db.Column(db.String(100))
    message = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, default=5)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Formulaire de contact
class ContactForm(FlaskForm):
    name = StringField('Nom', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Envoyer')

# Vues Admin
admin.add_view(ModelView(Project, db.session))
admin.add_view(ModelView(Testimonial, db.session))
admin.add_view(ModelView(Contact, db.session))

def fetch_github_assets(limit=4):
    """Récupère les stats GitHub avec mise en cache légère."""
    now = datetime.utcnow()
    if (
        GITHUB_CACHE["timestamp"]
        and now - GITHUB_CACHE["timestamp"] < GITHUB_CACHE_DURATION
        and GITHUB_CACHE["profile"]
    ):
        return GITHUB_CACHE["profile"], GITHUB_CACHE["repos"][:limit]

    profile = GITHUB_FALLBACK_PROFILE
    repos = GITHUB_FALLBACK_REPOS

    if requests:
        try:
            profile_resp = requests.get(
                f"https://api.github.com/users/{GITHUB_USERNAME}", timeout=5
            )
            if profile_resp.ok:
                data = profile_resp.json()
                profile = {
                    "name": data.get("name") or data.get("login"),
                    "login": data.get("login", GITHUB_USERNAME),
                    "followers": data.get("followers", 0),
                    "public_repos": data.get("public_repos", 0),
                    "public_gists": data.get("public_gists", 0),
                    "html_url": data.get("html_url"),
                    "blog": data.get("blog"),
                    "company": data.get("company"),
                    "bio": data.get("bio"),
                }
        except RequestException:
            pass

        try:
            repos_resp = requests.get(
                f"https://api.github.com/users/{GITHUB_USERNAME}/repos?per_page=100",
                timeout=5,
            )
            if repos_resp.ok:
                repo_data = repos_resp.json()
                repo_data = sorted(
                    repo_data,
                    key=lambda r: (
                        r.get("stargazers_count", 0),
                        r.get("forks_count", 0),
                        r.get("pushed_at") or r.get("updated_at") or "",
                    ),
                    reverse=True,
                )
                repos = [
                    {
                        "name": repo.get("name"),
                        "description": repo.get("description"),
                        "html_url": repo.get("html_url"),
                        "language": repo.get("language"),
                        "stargazers_count": repo.get("stargazers_count", 0),
                        "pushed_at": repo.get("pushed_at") or repo.get("updated_at"),
                    }
                    for repo in repo_data[: limit or 4]
                ]
        except RequestException:
            pass

    GITHUB_CACHE.update(
        {
            "profile": profile,
            "repos": repos,
            "timestamp": now,
        }
    )
    return profile, repos[:limit]

# Routes principales
@app.route('/')
def home():
    projects = Project.query.limit(3).all()
    testimonials = Testimonial.query.all()
    github_profile, github_repos = fetch_github_assets()
    return render_template(
        'home.html',
        projects=projects,
        testimonials=testimonials,
        github_profile=github_profile,
        github_repos=github_repos
    )

@app.route('/about')
def about():
    github_profile, github_repos = fetch_github_assets()
    return render_template('about.html', github_profile=github_profile, github_repos=github_repos)

@app.route('/projects')
def projects():
    all_projects = Project.query.all()
    github_profile, github_repos = fetch_github_assets(limit=6)
    return render_template(
        'projects.html',
        projects=all_projects,
        github_repos=github_repos,
        github_profile=github_profile
    )

@app.route('/project/<int:project_id>')
def project_detail(project_id):
    project = Project.query.get_or_404(project_id)
    return render_template('project_detail.html', project=project)

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/partners')
def partners():
    return render_template('partners.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        # Sauvegarder le message en base
        contact_msg = Contact(
            name=form.name.data,
            email=form.email.data,
            message=form.message.data
        )
        db.session.add(contact_msg)
        db.session.commit()
        
        # Envoyer l'email (optionnel)
        try:
            msg = Message(
                subject=f'Nouveau message de {form.name.data}',
                sender=app.config['MAIL_USERNAME'],
                recipients=[app.config['MAIL_USERNAME']],
                body=f"""
                Nom: {form.name.data}
                Email: {form.email.data}
                Message: {form.message.data}
                """
            )
            mail.send(msg)
        except:
            pass  # Continuer même si l'email échoue
        
        flash('Votre message a été envoyé avec succès!', 'success')
        return redirect(url_for('contact'))
    
    return render_template('contact.html', form=form)

@app.context_processor
def inject_globals():
    return {
        'current_year': datetime.now().year,
        'portfolio_sites': PORTFOLIO_SITES,
        'venture_milestones': VENTURE_MILESTONES,
        'spotlight_projects': SPOTLIGHT_PROJECTS,
        'partner_network': PARTNER_NETWORK,
        'workflow_steps': WORKFLOW_STEPS,
        'github_username': GITHUB_USERNAME
    }

# Initialisation de la base de données
def init_db():
    with app.app_context():
        # Supprimer et recréer toutes les tables
        db.drop_all()
        db.create_all()
        
        # Ajouter des données de démonstration
        sample_projects = [
                Project(
                    name="Plateforme LMS - Université Loyola du Congo/ICAM",
                    description="Système de gestion d'apprentissage complet avec IA pour l'enseignement supérieur",
                    github_url="https://github.com/cognito-inc/loyola-lms",
                    stack="Python, Flask, AI/ML, PostgreSQL, React",
                    image_url="https://via.placeholder.com/400x300/1A1A1A/00D4FF?text=LMS+Platform",
                    detailed_description="Plateforme d'éducation numérique conçue spécifiquement pour l'Université Loyola du Congo en partenariat avec l'ICAM. Cette solution intègre des fonctionnalités d'intelligence artificielle pour personnaliser l'apprentissage et améliorer l'engagement des étudiants.",
                    demo_url="https://loyola-lms.cognito-inc.com",
                    features="Gestion des cours et contenus, Suivi des progrès étudiants, IA pour recommandations personnalisées, Système d'évaluation automatisé, Interface multilingue, Tableau de bord analytique"
                ),
                Project(
                    name="CognitoAI Platform",
                    description="Plateforme d'intelligence artificielle pour l'automatisation des processus métier",
                    github_url="https://github.com/cognito-inc/cognitoai-platform",
                    stack="Python, Flask, TensorFlow, React",
                    image_url="https://via.placeholder.com/400x300/1A1A1A/00D4FF?text=AI+Platform",
                    detailed_description="Plateforme d'intelligence artificielle tout-en-un permettant aux entreprises d'automatiser leurs processus métier complexes grâce à des modèles d'IA pré-entrainés et personnalisables.",
                    demo_url="https://cognitoai.cognito-inc.com",
                    features="Modèles IA pré-entrainés, Interface drag-and-drop, API REST complète, Tableau de bord temps réel, Intégrations tierces, Système de monitoring"
                ),
                Project(
                    name="Smart Analytics Dashboard",
                    description="Tableau de bord analytique en temps réel pour startups",
                    github_url="https://github.com/cognito-inc/smart-analytics",
                    stack="Python, Django, Chart.js, PostgreSQL",
                    image_url="https://via.placeholder.com/400x300/1A1A1A/00D4FF?text=Analytics+Dashboard",
                    detailed_description="Solution d'analyse de données conçue pour les startups, offrant des insights actionables sur les performances business et les tendances du marché.",
                    demo_url="https://analytics.cognito-inc.com",
                    features="Visualisations interactives, Rapports automatisés, Alertes intelligentes, Intégration multi-sources, Export de données, Collaboration d'équipe"
                )
        ]
        
        sample_testimonials = [
                Testimonial(
                    client_name="Marie Dubois",
                    company="TechStart SAS",
                    message="Jonathan a transformé notre vision en une application exceptionnelle. Son expertise technique et sa créativité sont remarquables.",
                    rating=5
                ),
                Testimonial(
                    client_name="Pierre Martin",
                    company="InnovCorp",
                    message="Travail professionnel, délais respectés et résultats au-delà de nos attentes. Je recommande vivement!",
                    rating=5
            )
        ]
            
        for project in sample_projects:
            db.session.add(project)
        
        for testimonial in sample_testimonials:
            db.session.add(testimonial)
        
        db.session.commit()

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
