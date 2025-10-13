from flask import Flask, render_template, request, flash, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_mail import Mail, Message
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email
from datetime import datetime
import os
from dotenv import load_dotenv

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

# Routes principales
@app.route('/')
def home():
    projects = Project.query.limit(3).all()
    testimonials = Testimonial.query.all()
    return render_template('home.html', projects=projects, testimonials=testimonials)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    all_projects = Project.query.all()
    return render_template('projects.html', projects=all_projects)

@app.route('/project/<int:project_id>')
def project_detail(project_id):
    project = Project.query.get_or_404(project_id)
    return render_template('project_detail.html', project=project)

@app.route('/services')
def services():
    return render_template('services.html')

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
def inject_year():
    return {'current_year': datetime.now().year}

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
                    image_url="https://images.unsplash.com/photo-1522202176988-66273c2fd55f?w=400&h=300&fit=crop&crop=center",
                    detailed_description="Plateforme d'éducation numérique conçue spécifiquement pour l'Université Loyola du Congo en partenariat avec l'ICAM. Cette solution intègre des fonctionnalités d'intelligence artificielle pour personnaliser l'apprentissage et améliorer l'engagement des étudiants.",
                    demo_url="https://loyola-lms.cognito-inc.com",
                    features="Gestion des cours et contenus, Suivi des progrès étudiants, IA pour recommandations personnalisées, Système d'évaluation automatisé, Interface multilingue, Tableau de bord analytique"
                ),
                Project(
                    name="CognitoAI Platform",
                    description="Plateforme d'intelligence artificielle pour l'automatisation des processus métier",
                    github_url="https://github.com/cognito-inc/cognitoai-platform",
                    stack="Python, Flask, TensorFlow, React",
                    image_url="https://images.unsplash.com/photo-1677442136019-21780ecad995?w=400&h=300&fit=crop&crop=center",
                    detailed_description="Plateforme d'intelligence artificielle tout-en-un permettant aux entreprises d'automatiser leurs processus métier complexes grâce à des modèles d'IA pré-entrainés et personnalisables.",
                    demo_url="https://cognitoai.cognito-inc.com",
                    features="Modèles IA pré-entrainés, Interface drag-and-drop, API REST complète, Tableau de bord temps réel, Intégrations tierces, Système de monitoring"
                ),
                Project(
                    name="Smart Analytics Dashboard",
                    description="Tableau de bord analytique en temps réel pour startups",
                    github_url="https://github.com/cognito-inc/smart-analytics",
                    stack="Python, Django, Chart.js, PostgreSQL",
                    image_url="https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=400&h=300&fit=crop&crop=center",
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