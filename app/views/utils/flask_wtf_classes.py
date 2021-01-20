from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import InputRequired, Length, Email, EqualTo
import flask_wtf


class RegisterForm(FlaskForm):
    first_name = StringField('First Name', validators=[InputRequired(), Length(min=2, max=50)], )
    last_name = StringField('Last Name', validators=[InputRequired(), Length(min=2, max=50)])
    email = StringField('Email Address', validators=[InputRequired(), Email(message='Invalid email'), Length(min=2, max=50)])
    role = StringField("Role", validators=[InputRequired()])
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('Password', [InputRequired(), Length(min=8)])
    confirm = PasswordField('Repeat Password', [EqualTo('password', message='Did not match password')])
    submit = SubmitField('Submit')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Length(min=4, max=40)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=4)])
    remember = BooleanField('Remember me')
    submit = SubmitField('Submit')



