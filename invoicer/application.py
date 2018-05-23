from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify, request
from config import config
import auth, requests

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
    
    return json_resp(True, ret)


@app.route('/x/userinfo')
@auth.requires_auth
def user_info():
    auth = request.headers.get("Authorization", None)

    ret = requests.get(
        'https://%s/userinfo'% (config['AUTH0'],),
        headers={'Authorization':auth}
    )

    return json_resp(True, {
        'user' : ret.json()
    })

class User(db.Model):
    id       = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email    = db.Column(db.String(120), unique=True)


#########################
## HELPERS

def json_resp(succ, ret={}, msg=''):
    return jsonify({
        'SUCCESS': succ,
        'MESSAGE': msg,
        'PAYLOAD': ret
    })


#########################
## DEV SERVER
#    - db migrations need to be handled
#    - dev server should be started via command line
    
if __name__ == '__main__':
    # terrible hot fix for db migrations while docker is figured out
    try:
        User.query.all()
    except:
        db.create_all()
        admin = User(username='admin', email='admin@invoicer.com')
        db.session.add(admin); db.session.commit()
        
    app.run(host='0.0.0.0', debug=True)

