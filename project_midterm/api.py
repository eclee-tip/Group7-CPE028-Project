from operator import indexOf
from flask import Flask, request, jsonify
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Users.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.secret_key = 'group12'

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Users(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=True)
    user_username = db.Column(db.String(50))
    user_email = db.Column(db.String(50))
    user_password = db.Column(db.String(50))

    def __init__(self, id, user_username, user_email, user_password):
        self.id = id
        self.user_username = user_username
        self.user_email = user_email
        self.user_password = user_password

class UserSchema(ma.Schema):
    class Meta:
        fields = ("id", "user_username", "user_email", "user_password")

user_schema = UserSchema()
users_schema = UserSchema(many=True)

@app.route('/users', methods=['POST'])
def user_create():
    id = request.json.get('id')
    user_username = request.json.get('user_username')
    user_email = request.json.get('user_email')
    user_password = request.json.get('user_password')
    new_user = Users(id, user_username, user_email, user_password)
    db.session.add(new_user)
    db.session.commit()
    return user_schema.jsonify(new_user)

@app.route('/users', methods=['GET'])
def read_all():
    users = Users.query.all()
    result = users_schema.dump(users)
    return users_schema.jsonify(result).data

@app.route('/users/<user_username>', methods=['GET'])
def read_user(user_username):
    users = Users.query.filter_by(user_username=user_username).first()
    result = user_schema.dump(users)
    return user_schema.jsonify(result)

@app.route('/users/<user_username>', methods=['PUT'])
def update_user(user_username):
    users = Users.query.filter_by(user_username=user_username).first()
    user_username = request.json.get('user_username')
    user_email = request.json.get('user_email')
    user_password = request.json.get('user_password')
    users.user_username = user_username
    users.user_email = user_email
    users.user_password = user_password
    db.session.commit()
    return user_schema.jsonify(users)

@app.route('/users/<user_username>', methods=['DELETE'])
def delete_user(user_username):
    users = Users.query.filter_by(user_username=user_username).first()
    db.session.delete(users)
    db.session.commit()
    return user_schema.jsonify(users)

if __name__ == '__main__':
    app.run(debug=True) 



