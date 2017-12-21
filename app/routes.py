from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'usename': 'prutha'}
    ttitle = {'my web app page'}
    return render_template('index.html',title=ttitle,user=user)
