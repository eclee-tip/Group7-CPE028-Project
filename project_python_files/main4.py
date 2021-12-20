# Add to this file for the web app
from operator import indexOf
from flask import Flask, request, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms import PasswordField, EmailField, StringField, SubmitField, ValidationError
from wtforms.validators import InputRequired, Length
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Users.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.secret_key = 'group12'
Bootstrap(app)

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "main"

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

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

@app.before_first_request
def create_table():
    db.create_all()

@app.route("/", methods=['GET', 'POST'])
def main():
    form = LoginForm() 
    if request.method == "POST":
        if form.validate_on_submit():
            users = Users.query.filter_by(user_username=form.username.data, 
                                        user_password=form.password.data).first()
            if users:
                login_user(users)
                return redirect(url_for('home'))
            else:
                flash("Error Username or Password")
                
    return render_template('index.html', form=form, title='Login')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == "POST":
        if form.validate_on_submit():
            new_user = Users(user_username=form.username.data, 
                            user_email=form.email.data, 
                            user_password=form.password.data)
            db.session.add(new_user)
            db.session.commit()
            flash('You have successfully registered! You may now login.')
            return redirect('/')     
            
    return render_template("register.html", form=form, title='Register')

@app.route("/home")
@login_required
def home():
    return render_template("home.html")

@app.route("/about")
@login_required
def about():
    return render_template("about.html")

@app.route("/developer")
@login_required
def developer():
    return render_template("developer.html")

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main'))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)