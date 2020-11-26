"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
import jwt
import datetime
from werkzeug.security import generate_password_hash, check_password_hash

from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Animals
from init_database import init_db


app = Flask(__name__)
app.app_context().push()
data_base = os.environ['DB_CONNECTION_STRING']

app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = data_base
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)

CORS(app)
setup_admin(app)
app.cli.add_command(init_db)
@app.route('/register', methods=['POST'])
def create_user():
    body=request.get_json()
    # try:
    hashed_password = generate_password_hash(body['password'], method='sha256')
    print(hashed_password,"estoy en hashedpassword register")
    new_user= User( email=body["email"], password=hashed_password, is_active=True, name=body["name"], last_name=body["last_name"])
    #, phone=body["phone"], location=body["location"], biografy=body["biografy"]
    print(new_user,"soy new user")
    new_user.create_user()
    return jsonify(new_user.serialize()), 200
    # except:
        # return "Couldn't create the user",409

@app.route('/user/<int:id_user>/pet', methods=['GET'])
def read_pets_by_user(id_user):
    try:
        user_pets = Animals.read_pets(id_user)
        return jsonify(user_pets), 200
    except:
        print("entro en except")
        return "Couldn't find the pets",404

if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
