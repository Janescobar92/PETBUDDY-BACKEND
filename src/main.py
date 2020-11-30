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

from utils import APIException, generate_sitemap, token_required
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

@app.route('/services', methods=['GET'])
def get_all_services():  
    try:
        all_services = Services.read_all_services() 
        return jsonify(all_services), 200
    except:
        return "Couldn't find the services",404

@app.route('/user/<int:id_user>/service', methods=['GET'])
def read_user_services(id_user):
    try:  
        user_services = Services.read_user_services(id_user)
        return jsonify(user_services), 200
    except:
        return "Couldn't find the user services",404

if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
