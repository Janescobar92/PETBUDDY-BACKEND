from flask import Flask
from sqlalchemy_utils import create_database, database_exists
from sqlalchemy import create_engine

import models


def create_db(data_base):
    # funcion para crear base de datos 
    if not database_exists(data_base):
        create_database(data_base)

    create_engine(data_base, encoding="latin1", echo=True)


# aqui se cargan los datos de seed_data y se insertan en la tabla
def load_seed_data(data):    
    app = Flask(__name__)

    for table, rows in data.items():
        ModelClass = getattr(models, table)

        for row in rows:
            new_row = ModelClass(
                email = row["email"], 
                password = row["password"], 
                is_active = row["is_active"], 
                name = row["name"], 
                last_name = row["last_name"], 
                phone = row["phone"], 
                location = row["location"], 
                biografy = row["biografy"], 
                image= row["image"]
            )

            new_row.create()
 