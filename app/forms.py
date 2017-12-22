from flask_wtf import FlaskForm
from wtforms import StingFirld,PasswordField,BooleanField,submitField
from wtforms,validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('username', validators = [DataRequired()])
    password = PasswordField('password', validators = [DataRequired()])
    remember_me = BooleanField('Remember Me')
    Submit = SubmitField('Sign In')
