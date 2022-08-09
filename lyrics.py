from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
@app.route('/lyrics')
def index():
    return render_template('index.html')

@app.route('/add')
def add_lyrics():
    return render_template('add.html')