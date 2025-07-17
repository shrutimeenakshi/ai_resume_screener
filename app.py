from flask import Flask, render_template, request, redirect, session, url_for, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from utils.resume_parser import extract_text_from_pdf, extract_name_and_email
from utils.matcher import match_resume_with_jd
from seed_job_roles import seed_roles

UPLOAD_FOLDER = 'resumes'

app = Flask(__name__)
app.secret_key = 'shrut_secret_key_2025'
app.config['SESSION_TYPE'] = 'filesystem'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db', 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'admin123'

class ResumeEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    job_role = db.Column(db.String(100))
    skills = db.Column(db.Text)
    experience_years = db.Column(db.Integer)
    match_score = db.Column(db.Float)
    resume_text = db.Column(db.Text)
    filename = db.Column(db.String(100))
    matched_skills = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

class JobRole(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    role_key = db.Column(db.String(50), unique=True, nullable=False)
    role_name = db.Column(db.String(100), nullable=False)
    job_description = db.Column(db.Text, nullable=False)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_resume():
    jd_text = request.form['job_desc']
    resume_files = request.files.getlist('resume')

    all_results = []

    for resume_file in resume_files:
        if resume_file and resume_file.filename.endswith('.pdf'):
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], resume_file.filename)
            resume_file.save(filepath)

            resume_text = extract_text_from_pdf(filepath)
            name, email = extract_name_and_email(resume_text)
            score, matched_skills = match_resume_with_jd(resume_text, jd_text)

            entry = ResumeEntry(
                filename=resume_file.filename,
                match_score=score,
                matched_skills=", ".join(matched_skills),
                resume_text=resume_text,
                name=name,
                email=email
            )
            db.session.add(entry)
            db.session.commit()

            all_results.append({
                'id': entry.id,
                'filename': resume_file.filename,
                'score': score,
                'skills': matched_skills,
                'name': name,
                'email': email
            })

    return render_template('result.html', results=all_results)

@app.route('/admin', methods=['GET'])
def admin_dashboard():
    if not session.get('admin_logged_in'):
        return redirect(url_for('login'))

    min_exp = request.args.get('min_exp', type=int)
    skill_filter = request.args.get('skills', '')

    entries = ResumeEntry.query.order_by(ResumeEntry.match_score.desc()).all()
    filtered_entries = []

    for entry in entries:
        match = True

        if min_exp is not None and entry.experience_years is not None:
            if entry.experience_years < min_exp:
                match = False

        if skill_filter:
            required_skills = [s.strip().lower() for s in skill_filter.split(',')]
            if entry.skills:
                if not all(skill in entry.skills.lower() for skill in required_skills):
                    match = False
            else:
                match = False

        if match:
            filtered_entries.append(entry)

    return render_template('admin.html', entries=filtered_entries)

@app.route('/download/<filename>')
def download_resume(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        uname = request.form['username']
        pwd = request.form['password']
        if uname == ADMIN_USERNAME and pwd == ADMIN_PASSWORD:
            session['admin_logged_in'] = True
            return redirect(url_for('admin_dashboard'))
        else:
            error = "Invalid credentials. Try again."
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('admin_logged_in', None)
    return redirect('/')

@app.route('/send_to_ta', methods=['POST'])
def send_to_ta():
    selected_ids = request.form.getlist('selected_ids')
    if selected_ids:
        selected_profiles = ResumeEntry.query.filter(ResumeEntry.id.in_(selected_ids)).all()
        return render_template('ta_confirmation.html', profiles=selected_profiles)
    return redirect('/admin')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        if not JobRole.query.first():
            seed_roles()
    app.run(debug=True)