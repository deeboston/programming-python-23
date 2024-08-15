from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to the Flask World2!'

@app.route('/hello')
def hello():
    return 'Hello from the new route!'

@app.route('/html')
def html():
    return render_template('index.html')
