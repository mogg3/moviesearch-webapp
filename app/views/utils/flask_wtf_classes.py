from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import InputRequired, Length, Email, EqualTo


# TODO: add regular expression for password
class RegisterForm(FlaskForm):
    first_name = StringField(
        'First Name',
        validators=[InputRequired(), Length(min=2, max=50)],
        render_kw={"placeholder": "First name", "class": "form-control"})
    last_name = StringField(
        'Last Name',
        validators=[InputRequired(), Length(min=2, max=50)],
        render_kw={"placeholder": "Last name", "class": "form-control"})
    email = StringField(
        'Email Address',
        validators=[InputRequired(), Length(min=2, max=50)],
        render_kw={"placeholder": "Email", "class": "form-control", "pattern": "[a-z0-9.+-]+@[a-z0-9.-]+\.[a-z]+", "title" : "Your email is not valid"})
    username = StringField(
        'Username',
        validators=[InputRequired(), Length(min=4, max=15)],
        render_kw={"placeholder": "username", "class": "form-control"})
    password = PasswordField(
        'Password',
        validators=[InputRequired(), Length(min=4)],
        render_kw={"placeholder": "Password", "class": "form-control"})
    confirm = PasswordField(
        'Repeat Password',
        validators=[InputRequired(), EqualTo('password', message='Passwords did not match')],
        render_kw={"placeholder": "Repeat password", "class": "form-control"})
    submit = SubmitField('Submit',
                         render_kw={"placeholder": "Repeat password", "class": "btn btn-primary"})

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Length(min=4, max=40)],
                        render_kw={"placeholder": "Email address"})
    password = PasswordField('Password', validators=[InputRequired(), Length(min=4)],
                             render_kw={"placeholder": "Password"})
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign in')
