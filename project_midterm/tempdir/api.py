from operator import indexOf
from flask import Flask
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms import PasswordField, EmailField, StringField, SubmitField, ValidationError
from wtforms.validators import InputRequired, Length
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Users.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.secret_key = 'group12'
Bootstrap(app)

db = SQLAlchemy(app)

@app.before_first_request
def create_table():
    db.create_all()

class Users(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_username = db.Column(db.String(50))
    user_email = db.Column(db.String(50))
    user_password = db.Column(db.String(50))

    def __init__(self, user_username, user_email, user_password):
        self.user_username = user_username
        self.user_email = user_email
        self.user_password = user_password

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=3, max=15)])
    email = EmailField('Email', validators=[InputRequired(), Length(max=50)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=4, max=80)])
    submit = SubmitField('Register')

    def validate_username(self, field):
        if Users.query.filter_by(user_username=field.data).first():
            raise ValidationError('Username is already in use.')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=3, max=15)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=4, max=80)])
    submit = SubmitField('Login')