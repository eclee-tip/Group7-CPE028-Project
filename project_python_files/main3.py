# Add to this file for the web app
from flask import Flask, request, render_template, redirect, url_for, flash, session
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Users.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.secret_key = 'group12'

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "main"

class Users(UserMixin, db.Model):
    tablename = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_username = db.Column(db.String(50))
    user_email = db.Column(db.String(50))
    user_password = db.Column(db.String(50))

    def __init__(self, user_username, user_email, user_password):
        self.user_username = user_username
        self.user_email = user_email
        self.user_password = user_password

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

@app.before_first_request
def create_table():
    db.create_all()

@app.route("/", methods=['GET', 'POST'])
def main():
    if current_user.is_authenticated:
        return render_template('index.html')

    if request.method == "POST": 
        user_username = request.form.get('username')
        user_password = request.form.get('password')
        
        print(user_username)
        print(user_password)

        users = Users.query.filter_by(user_username=user_username, user_password=user_password).first()
        print(users)
        if users:
            session['name'] = user_username
            login_user(users)
            return redirect(url_for('home'))
        else:
            flash("Error Username or Password")
                
    return render_template('index.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        user_username = request.form['username']
        user_email = request.form['email']
        user_password = request.form['password']
        
        if Users.query.filter_by(user_username=user_username).first():
            flash("Username already exists")
            return redirect("/register")
        
        new_user = Users(user_username=user_username, user_email=user_email, user_password=user_password)
        db.session.add(new_user)
        db.session.commit()
        flash("Registered")
        return redirect('/')
            
    return render_template("register.html")

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