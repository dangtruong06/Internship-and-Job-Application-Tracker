from flask import Flask, render_template
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

@app.route('/')
def home():
    return 'HELLO WORLD'

if __name__ == '__main__':
    app.run(port=5000)

