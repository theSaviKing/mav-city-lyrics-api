from app import app

@app.route('/')
@app.route('/index')
@app.route('/lyrics')
def index():
    return "Hello, World!"