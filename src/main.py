"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for, make_response
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
import jwt
import datetime
from werkzeug.security import generate_password_hash, check_password_hash

from utils import APIException, generate_sitemap, token_required, isTrue
from admin import setup_admin
from models import db, User, Animals, Services, Operations, Service_type, ANIMALS_ENUM, PETS_CHARACTER
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

@app.route('/login', methods=['GET','POST'])  
def login_user(): 
    body=request.get_json()
    # auth = request.authorization   
    # print(auth, "este es el AUTH")

    if "x-access-tokens" not in request.headers:
        if not body or not body["email"] or not body["password"]:  
            return 'could not verify', 402, {'WWW.Authentication': 'Basic realm: "login required"'}    

        user = User.query.filter_by(email=body["email"]).first()  
            
        if check_password_hash(user.password, body["password"]):  
            token = jwt.encode({'id': user.id, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=500)}, app.config['SECRET_KEY'])  
            return jsonify({'token' : token.decode('UTF-8')}) 

        return make_response('could not verify',  401, {'WWW.Authentication': 'Basic realm: "login required"'})
    else:
        return make_response("Token admited", 200)

@app.route('/register', methods=['POST'])
def create_user():
    body=request.get_json()
    try:
        hashed_password = generate_password_hash(body['password'], method='sha256')
        new_user= User( email=body["email"], password=hashed_password, is_active=True, name=body["name"], last_name=body["last_name"])
        new_user.create_user()
        return jsonify(new_user.serialize()), 200
    except:
        return "Couldn't create the user",401

@app.route('/user/<int:id_user>', methods=['GET'])
def read_loged_user(id_user):
    try: 
        user = User.read_user(id_user)
        return jsonify(user.serialize()), 200
    except:
        return "Couldn't read user info", 401

@app.route('/user/<int:id_user>', methods=['PUT'])
def update_loged_user(id_user):
    body=request.get_json() 
    try: 
        update_user = User.update_user(id_user)
        return jsonify(update_user.serialize()), 200
    except:
        return "Couldn't read user info", 401

@app.route('/users', methods=['GET'])
def get_all_users():  
    
    users = User.query.all() 
    result = []   

    for user in users:   
        user_data = {}   
        user_data['id'] = user.id  
        user_data['name'] = user.name
        user_data['last_name'] = user.last_name  
        user_data['password'] = user.password
        user_data['email'] = user.email 
        
        result.append(user_data)   

    return jsonify({'users': result})
    
@app.route('/user/<int:id_user>/pet', methods=['POST'])
# @token_required
def create_user_pet(id_user):
    body=request.get_json()
    try:
        new_user_pet = Animals(user_id = id_user, name = body["name"], image = body["image"], animal_type = body["animal_type"], age = body["age"], personality = body["personality"],  gender = isTrue(body["gender"]) , weight= body["weight"], size = body["size"], diseases= body["diseases"], sterilized= isTrue(body["sterilized"]))
        new_user_pet.create_user_pet()
        return jsonify(new_user_pet.serialize()), 200
    except:
        return "Couldn't create the pet",404

@app.route('/user/<int:id_user>/pet', methods=['GET'])
def read_pets_by_user(id_user):
    try:
        user_pets = Animals.read_pets(id_user)
        return jsonify(user_pets), 200
    except:
        return "Couldn't find the pets",404

@app.route('/user/<int:id_user>/pet', methods=['PUT'])
# @token_required
def update_user_pet(id_user):
    body=request.get_json()
    try:
        update_pet = Animals(user_id = id_user, id= body["id"], name = body["name"], image = body["image"], animal_type = body["animal_type"], age = body["age"], personality = body["personality"],  gender = isTrue(body["gender"]) , weight= body["weight"], size = body["size"], diseases= body["diseases"], sterilized= isTrue(body["sterilized"]))
        update_pet.update_pets(id_user, body["id"], body["name"], body["image"], body["animal_type"], body["age"], body["personality"], isTrue(body["gender"]), body["weight"], body["size"], body["diseases"], isTrue(body["sterilized"]))
        return (update_pet.serialize())
    except:
        return "Couldn't update pet", 404

@app.route('/user/<int:id_user>/<int:pet_id>', methods=['DELETE'])
# @token_required
def delete_user_pet(id_user, pet_id):
    try:
        deleted_pet = Animals.delete_pet(pet_id)
        return jsonify(deleted_pet), 202
    except:
        return "Couldn't delete the pet", 409

@app.route('/animals_type', methods=['GET'])
def read_animals_type():
    try:
        return jsonify(ANIMALS_ENUM), 202
    except:
        return "Couldn't get animal_enum", 409

@app.route('/pets_character', methods=['GET'])
def read_pets_character():
    try:
        return jsonify(PETS_CHARACTER), 202
    except:
        return "Couldn't get pets_character", 409

@app.route('/user/workedfor/<int:id_user_param>', methods=['GET'])
def read_history_workedfor(id_user_param):
    try:
        history_service = Services.read_service_ofered(id_user_param)
        return jsonify(history_service), 200
    except:
        return "Couldn't find  history", 409

@app.route('/user/hired/<int:id_user>', methods=['GET'])
def read_history_hired(id_user):
    # try:
    history_service_hired = Operations.read_service_hired(id_user)
    return jsonify(history_service_hired), 200
    # except:
    #     return "Couldn't find  history", 409


if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
