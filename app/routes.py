from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'usename': 'prutha'}
   
    return render_template('index.html',title='my web pg',user=user)
