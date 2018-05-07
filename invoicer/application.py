from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from config import config

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = config['DBURI']

db = SQLAlchemy(app)

@app.route('/')
def index():
    return 'Good Morning Dave...'

@app.route('/x/users')
def users():
    ret = []
    for user in User.query.all():
        ret.append({
            'username': user.username,
            'email'   : user.email,
            'id'      : user.id,
        })
    
    return jsonify(ret)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

