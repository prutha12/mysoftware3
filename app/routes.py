from flask import Flask
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'usename': 'prutha'}
    title = {'my web app page'}
    return render_template('index.html',title=title,user=user)
