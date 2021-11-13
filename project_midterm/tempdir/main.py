# Add to this file for the web app
from enum import unique
from flask import Flask, request, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length
from flask_sqlalchemy import SQLAlchemy
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'group12'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
conn = sqlite3.connect("database.db")
Bootstrap(app)
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=80)])

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=15)])
    email = StringField('Email', validators=[InputRequired(), Length(min=10, max=50)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=80)])

@app.route("/home", methods=['GET', 'POST'])
def main():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if user.password == form.password.data:
                return redirect(url_for('base'))

    return render_template("index.html", form=form)

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        new_user=User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(new_user)
        db.session.commit()

    return render_template("register.html", form=form)

@app.route("/")
def base():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/developer")
def developer():
    return render_template("developer.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)