from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
@app.route('/lyrics')
def index():
    return render_template('index.html')

@app.route('/add')
def add_lyrics():
    return render_template('add.html')