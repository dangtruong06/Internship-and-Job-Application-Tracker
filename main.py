from flask import Flask, render_template
from models import db, User, Job
from forms import Register, Login
from dotenv import load_dotenv
from flask_login import LoginManager, login_user, logout_user, current_user
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

        return 'Success'
    
    return 'Register Page'

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = Login()
    if form.validate_on_submit():
        user = db.session.execute(db.select(User).where(User.email == form.email.data)).scalar()

        if not user:
            print('User does not exist')
        elif not user.check_password(form.password.data):
            print('Incorrect password')
        else:
            login_user(user)
            return 'Log in successful'
    
    return 'Log in page'

@app.route('/')
def home():
    return 'HELLO WORLD'

if __name__ == '__main__':
    app.run(port=5000, debug=True)

