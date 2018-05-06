from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
from sqlalchemy import create_engine
from sqlalchemy import *
from flask import jsonify
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
app = Flask(__name__)
metadata = MetaData()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db_uri = 'mysql://root:root@db:3306/users'
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri

db = SQLAlchemy(app)

# engine = create_engine('postgres://%s:%s@%s:%s/%s' % (user, pwd, host, port, db))


engine = create_engine(db_uri)
db.drop_all()
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


#SQL Alchemy DB Definitions
# class User(db.Model):
#     id       = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     email    = db.Column(db.String(120), unique=True, nullable=False)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

admin = User('admin', 'admin@example.com')



User.query.filter_by(username='admin').first()
if __name__ == '__main__': 
    app.run(host='0.0.0.0', debug=True)