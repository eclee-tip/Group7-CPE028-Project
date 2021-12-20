# Add to this file for the web app
from operator import indexOf
from flask import Flask, json, request, render_template, redirect, url_for, flash
#from flask_login import login_required, logout_userm, LoginManager
from api import app
import requests, sqlite3

# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = "main"

# @login_manager.user_loader
# def load_user(user_username):
#     return Users.query.get(user_username)

# @app.before_first_request
# def create_table():
#     db.create_all()

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/", methods=['GET', 'POST'])
def login():
    user_username = request.form.get('username')
    user_password = request.form.get('password')
    json_data = requests.get("http://127.0.0.1:5000/users/" + user_username).json()
    print(json_data)
    if json_data['user_username'] == user_username and json_data['user_password'] == user_password:
        return redirect(url_for('home'))
    else:
        flash('Invalid username or password')
        return redirect("/")

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        user_username = request.form['username']
        user_email = request.form['email']
        user_password = request.form['password']
        
        db = sqlite3.Connection("http://127.0.0.1:5000/users/")
        db.put('/users/{user_username}', "user_username", user_username)
        db.put('/users/{user_username}', "user_email", user_email)
        db.put('/users/{user_username}', "user_password", user_password)
        flash("Registered")
        return redirect('/')
            
    return render_template("register.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/developer")
def developer():
    return render_template("developer.html")

# @app.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     return redirect(url_for('main'))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)