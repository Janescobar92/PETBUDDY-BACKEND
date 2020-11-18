from sqlalchemy_utils import create_database, database_exists
from sqlalchemy import create_engine
import models



def create_db(data_base): 
    # funcion para crear base de datos 
    if not database_exists(data_base):
        create_database(data_base)

    engine = create_engine(data_base, encoding="latin1", echo=True)

    return engine

# aqui se cargan los datos de seed_data y se insertan en la tabla
def load_seed_data(data):
    for table, rows in data.items():
        # print(data, "esta es la data")
        ModelClass = getattr(models, table)
        # print(ModelClass, "este print es el del modelclass")
        # cada row es cada diccionario de cada tabla 
        for row in rows:
            new_user= ModelClass(id = row["id"], email = row["email"], password = row["password"], is_active = row["is_active"], name = row["name"], last_name =  row["last_name"], phone = row["phone"], location = row["location"], biografy = row["biografy"], image= row["image"])
            print(row["password"], "khnasdonoiajndsopiajdso")
            # print(new_user, "esto es el prnt de new user")
            # new_user.create_user()
             #  ModelClass.create(row) esta funcion añade compaginnado con las funciones de models.py  en este caso utiliza la funcion crear
 