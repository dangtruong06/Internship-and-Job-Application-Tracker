from flask import Flask, render_template, redirect, url_for, flash, request
from models import db, User, Job
from forms import Register, Login, AddJob
from dotenv import load_dotenv
from flask_login import LoginManager, login_user, logout_user, current_user, login_required
from collections import Counter
import os

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

# DB SETUP
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
db.init_app(app)

# LOG IN MANAGER
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User,int(user_id))

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = Register()

    if form.validate_on_submit():
        new_user = User(name=form.name.data,
                        email=form.email.data)
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()

        login_user(new_user)

        return redirect(url_for('dashboard'))
    
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = Login()
    if form.validate_on_submit():
        user = db.session.execute(db.select(User).where(User.email == form.email.data)).scalar()

        if not user:
            flash('User does not exist', 'danger')
        elif not user.check_password(form.password.data):
            flash('Incorrect password', 'danger')
        else:
            login_user(user)
            return redirect(url_for('dashboard'))
    
    return render_template('login.html', form=form)

@app.route('/')
def home():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    return render_template('index.html')

# Dashboard displays jobs of current logged in user
@app.route('/dashboard')
@login_required
def dashboard():
    jobs = db.session.execute(db.select(Job
                            ).where(Job.user_id == current_user.id
                            )).scalars().all()
    
    counts = Counter(job.status for job in jobs)
    
    status_counts = {
        'total':len(jobs),
        'applied':counts['Applied'],
        'interview':counts['Interview'],
        'rejected':counts['Rejected'],
        'screen':counts['Screen']
    }

    return render_template('dashboard.html', jobs=jobs, status_counts=status_counts)

@app.route('/add-job', methods=['POST', 'GET'])
@login_required
def add():
    form = AddJob()

    if form.validate_on_submit():
        new_job = Job(company=form.company.data,
                      role=form.role.data,
                      status=form.status.data,
                      url=form.url.data,
                      notes=form.notes.data,
                      applied_on=form.date.data,
                      user_id=current_user.id)
        
        db.session.add(new_job)
        db.session.commit()
        return redirect(url_for('dashboard'))
    
    return render_template('add.html', form=form)

@app.route('/delete-job/<int:job_id>', methods=['POST'])
@login_required
def delete_job(job_id):
    job = db.get_or_404(Job, job_id)
    db.session.delete(job)
    db.session.commit()
    return redirect(url_for('dashboard'))


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(port=5000, debug=True)

