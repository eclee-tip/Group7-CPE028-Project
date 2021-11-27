# Add to this file for the web app
from enum import unique
from flask import Flask, request, render_template, redirect, url_for, flash
from firebase import firebase
import requests

config = {
  "apiKey": "AIzaSyDWOfOTwNEhMM61NgO6cGZIW0Px0rz6z2k",
  "authDomain": "fir-rest-api-6da29.firebaseapp.com",
  "databaseURL": "https://fir-rest-api-6da29-default-rtdb.firebaseio.com",
  "projectId": "fir-rest-api-6da29",
  "storageBucket": "fir-rest-api-6da29.appspot.com",
  "messagingSenderId": "477618873355",
  "appId": "1:477618873355:web:505fea7796204b79cad30e",
  "measurementId": "G-WL1HFD0VD1"
}

app = Flask(__name__)
app.secret_key = 'group12'

@app.route("/", methods=['GET', 'POST'])
def main():
    if (request.method == 'POST'): 
        usernames = request.form['username']
        passwords = request.form['password']
        print(usernames)
        user = requests.get(f'https://fir-rest-api-6da29-default-rtdb.firebaseio.com/users/{usernames}.json').json()
        parsed_user = user['username']
        parsed_pass = user['password']
        if usernames == parsed_user:
            if passwords == parsed_pass:
                return redirect(url_for("base"))

            flash(u'Invalid password provided', 'error')
            #return "<h1> Incorrect password </h1>"
        #unsuccessful = 'Please check your credentials'
        #return render_template('index.html', umessage=unsuccessful)
        #flash ('Please write your username password')
    return render_template('index.html')  

@app.route("/register", methods=['GET', 'POST'])
def register():
    if (request.method == 'POST'):
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        db = firebase.FirebaseApplication("https://fir-rest-api-6da29-default-rtdb.firebaseio.com")
        db.put(f'/users/{username}', "username", username)
        db.put(f'/users/{username}', "email", email)
        db.put(f'/users/{username}', "password", password)
    return render_template("register.html")

@app.route("/home")
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