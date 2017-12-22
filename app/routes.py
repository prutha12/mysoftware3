from flask import render_template,flash,redirect,url_for
from app import app
from app.forms import LoginForm
from flask_login import current_user, login_user
from app.models import User
from flask_login import logout_user
from flask_login import login_required

@app.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login request for user{}, remember_me={}'.format(
             form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
        return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or not next_page.startswith('/'):
            next_page = url_for('index')
        return redirect(next_page)
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
    return render_template('index.html', title='Web Page',posts=posts)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
