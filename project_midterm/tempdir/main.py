# Add to this file for the web app
from operator import indexOf
from flask import Flask, request, render_template, redirect, url_for, flash
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
from api import LoginForm, RegistrationForm, Users, app, db



login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "main"

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))



@app.route("/", methods=['GET', 'POST'])
def main():
    form = LoginForm()
    if current_user.is_authenticated:
        return render_template('index.html')

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