from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import InputRequired, Length, Email, EqualTo


# TODO: add regular expression for password
class RegisterForm(FlaskForm):
    first_name = StringField(
        'First Name',
        validators=[InputRequired(), Length(min=2, max=50)],
        render_kw={"placeholder": "First name", "class": "form-control", "id": "first-name"})
    last_name = StringField(
        'Last Name',
        validators=[InputRequired(), Length(min=2, max=50)],
        render_kw={"placeholder": "Last name", "class": "form-control", "id": "last-name"})
    email = StringField(
        'Email Address',
        validators=[InputRequired(), Length(min=2, max=50)],
        render_kw={"placeholder": "Email", "class": "form-control", "id": "email", "pattern": "[a-z0-9.+-]+@[a-z0-9.-]+\.[a-z]+", "title" : "Your email is not valid"})
    username = StringField(
        'Username',
        validators=[InputRequired(), Length(min=4, max=50)],
        render_kw={"placeholder": "username", "class": "form-control", "id": "username"})
    password = PasswordField(
        'Password',
        validators=[InputRequired(), Length(min=4)],
        render_kw={"placeholder": "Password", "class": "form-control", "id": "password"})
    confirm = PasswordField(
        'Repeat Password',
        validators=[InputRequired(), EqualTo('password', message='Passwords did not match')],
        render_kw={"placeholder": "Repeat password", "class": "form-control", "id": "confirm"})
    submit = SubmitField('Submit',
                         render_kw={"placeholder": "Repeat password", "class": "btn btn-primary", "id": "submit"})

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Length(min=4, max=40)],
                        render_kw={"placeholder": "Email address", "id": "email", "class": "form-control"})
    password = PasswordField('Password', validators=[InputRequired(), Length(min=4)],
                             render_kw={"placeholder": "Password", "id": "password", "class": "form-control"})
    remember = BooleanField('Remember me', render_kw={"class": "btn btn-primary"})
    submit = SubmitField('Sign in', render_kw={"id": "submit", "class": "btn btn-primary"})


