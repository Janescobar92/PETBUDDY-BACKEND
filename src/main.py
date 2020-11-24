"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS

from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db

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
    try:
        # if body is None:
            # return "Body content is missing", 400
        new_user= User(user_id= user_id, name= username, email=email, last_name=last_name, phone= phone, location= location, biografy = biografy )
        new_user.add_user()
        return jsonify(new_user.serialize()), 200
    except:
        return "Couldn't create the user",409

if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
