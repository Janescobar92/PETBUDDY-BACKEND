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

from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Animals, Services, Operations, Service_type
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
    
@app.route('/user/<int:id_user>/pet', methods=['GET'])
def read_pets_by_user(id_user):
    try:
        user_pets = Animals.read_pets(id_user)
        return jsonify(user_pets), 200
    except:
        print("entro en except")
        return "Couldn't find the pets",404

@app.route('/user/<int:id_user_param>/worked_for', methods=['GET'])
def read_history(id_user_param):
    param = id_user_param
    # try:
#  userList = users.query.join(friendships).add_columns(users.id, users.userName, users.userEmail, friendships.user_id, friendships.friend_id).filter(users.id == friendships.friend_id).filter(friendships.user_id == userID).paginate(page, 1, False)
    # previous_works_table = User.query.join(Services).add_columns(User.image, User.name, User.id, Services.id, Services.id_user_offer).join
    #  query = session.query(User, Document, DocumentsPermissions).join(Document).join(DocumentsPermissions)
    # previous_works_query = db.session.query(Services).join(User).join(Operations).join(Service_type).add_columns(User.image, User.name, User.id, Services.id, Services.id_user_offer, Operations.id, Operations.date, Operations.hired_time, Operations.service_id_hired, Operations.total_price, Operations.user_id_who_hire, Service_type.id, Service_type.service_type_id).filter(Services.id_user_offer == param)
    # def serialize():
    #     return {
    #         "user_who_hired": 
    #     }
        
    # print(previous_works_query)

    # previous_works = []
    # for each_work in previous_works_query:
    #     print("HEEEELLLOOOOOOOOOOOOOOOOOOOOOOOOOO", each_work)
    #     if each_work["operations_user_id_who_hire"] == each_work["user_id"]:
    #         if each_work["operations_service_id_hired"] == each_work["services_id"] and each_work["services_id_service_type"] == each_work["service_type_service_type_id"]:
    #             works = {}
    #             works["user_who_hire"] = each_work["user_name"]
    #             works["service_type"] = each_work["service_type_service_type_id"]


    #             previous_works.append(works)

    # return previous_works
        
    # services = Services.read_service_ofered(id_user)
    # operations = Operations.read_operations()
    # my_previous_works=[]
    # for service in services:
    #     for operation in operations: 
    #         if service["id"] == operation["service_id_hired"]:

    # return jsonify(my_previous_works), 200
    
    # except:
        # print("entro en except")
        # return "Couldn't find the pets",404

if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
