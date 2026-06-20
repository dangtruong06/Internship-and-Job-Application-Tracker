from flask import Flask, render_template
from models import db, User, Job
from forms import Register
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

# DB SETUP
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
db.init_app(app)

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

@app.route('/')
def home():
    return 'HELLO WORLD'

if __name__ == '__main__':
    app.run(port=5000, debug=True)

