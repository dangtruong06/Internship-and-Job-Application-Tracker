from flask import Flask, render_template
from models import db, User, Job
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

# DB SETUP
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
db.init_app(app)

@app.route('/')
def home():
    return 'HELLO WORLD'

if __name__ == '__main__':
    app.run(port=5000, debug=True)

