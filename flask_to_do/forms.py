from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import InputRequired, Length, EqualTo

class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired(), Length(max=25, message = 'Name should not be longer than 25 characters')])
    username = StringField('Username', validators=[InputRequired(), Length(max=25, message = 'Username should not be longer than 25 characters')])
    password = PasswordField('Password', validators=[InputRequired()])
    confirm_password = PasswordField('Confirm password', validators=[InputRequired(), EqualTo('password', message = 'Passwords do not match')])
    submit = SubmitField('Sign up')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(max=20)])
    password = PasswordField('Password', validators=[InputRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')