from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'usename': 'prutha'}
    posts = [
    {
             'author' :{'usename':'prutha'},
             'body' :'hellw'
    },
    {
             'author' :{'usename':'kalan'},
             'body' :'hiiii'
    }
    ]
   
    return render_template('index.html',title='my web pg',user=user,posts=posts)
