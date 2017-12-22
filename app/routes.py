from flask import render_template,flash,redirect
from app import app
from app.forms import LoginForm

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login request for user{}, remember_me={}',format( form.username.data, form.remember_me.data))
    return redirect('/index')
 return render_template('login.html',title='Sign In',form=form)

@app.route('/')
@app.route('/index')
def index():
    user = {'usename': 'prutha'}
    posts = [
    {
             'author' :{'usename':'prutha'},
             'body' :'hello'
    },
    {
             'author' :{'usename':'kalan'},
             'body' :'hiiii'
    }
    ]
   
    return render_template('index.html',title='my web pg',user=user,posts=posts)
