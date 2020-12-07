from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, String, Enum, Float, DateTime, Boolean, Text, Date
from datetime import datetime

db = SQLAlchemy()


class Operations(db.Model):
    __tablename__= "operations"
    id = db.Column(Integer, primary_key=True)
    user_id_who_hire = Column(Integer, ForeignKey("user.id"), primary_key=True)
    service_id_hired = Column(Integer, ForeignKey("services.id"), primary_key=True)
    date = Column(db.Date, unique=False, nullable=False)
    hired_time = Column(Integer, nullable=False)
    total_price= Column(Float(), nullable= False)
    # realtionships
    user_operation = db.relationship("User", back_populates="services_operation")
    service_operations = db.relationship("Services", back_populates="users_operations")

    def serialize(self):
        return {
            "id": self.id,
            "user_id_who_hire": self.user_id_who_hire,
            "service_id_hired": self.service_id_hired,
            "date": self.date,
            "hired_time": self.hired_time,
            "total_price": self.total_price
        }
        
    def read_operations():
        operations = Operations.query.all()
        all_user_operations =  list(map(lambda x: x.serialize(), operations))

        return all_user_operations
    
    def getOperations(param_id):
        historic_operations = Operations.query.filter_by(service_id_hired= param_id)
        all_historic_operations =  list(map(lambda x: x.serialize(), historic_operations))

        for eachOperation in all_historic_operations:
            user_who_hired_name = User.getUserWhoHired(eachOperation["user_id_who_hire"])
            eachOperation["user_who_hired_name"]= user_who_hired_name

        return all_historic_operations


        

class User(db.Model):
    __tablename__= "user"
    id = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(80), nullable=False)
    is_active = Column(Boolean(True), nullable=False)
    name = Column(String(200), nullable=False)
    last_name = Column(String(200), nullable=False)
    phone = Column(String(30), unique=True)
    location = Column(String(255))
    biografy = Column(Text())
    image = Column(Text())
    # realtionships
    animals = db.relationship('Animals', lazy=True)
    services_operation = db.relationship("Operations", back_populates="user_operation")

    # def __repr__(self):
    #     return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "name": self.name,
            "last_name": self.last_name,
            "phone":self.phone,
            "location":self.location,
            "biografy":self.biografy,
            "image": self.image,
            "is_active":self.is_active
            # do not serialize the password, its a security breach
        }

    # def __repr__(self):
    #     return '<User %r>' % self.username

    def create_user(self):
        try:
            print(self,"DEVUELVE EL OBJETO USER")
            db.session.add(self)
            db.session.commit()
        except:
            db.session.rollback()

    @classmethod 
    def read_user(cls, id_user):
        user =   User.query.get(id_user)
        return user

    def update_user(self, id_user, name, email, last_name, phone, location, biografy, image):
        user_to_update = User.query.filter_by(id= id_user).first()
        user_to_update.name = name
        user_to_update.image = image
        user_to_update.email = email
        user_to_update.last_name = last_name
        user_to_update.phone = phone
        user_to_update.location = location
        user_to_update.biografy = biografy
        db.session.commit()

    def getUserWhoHired(param_id):
        historic_user_who_hires = User.query.filter_by(id= param_id)
        all_historic_user_who_hires =  list(map(lambda x: x.serialize(), historic_user_who_hires))

        for eachUserWhoHired in all_historic_user_who_hires:
            result = eachUserWhoHired["name"]

        return result


    def delete_user(id_user):
        user = User.query.get(id_user)
        if user.is_active == True:
            user.is_active= False
            db.session.commit()
        return user



ANIMALS_ENUM = ("perro", "gato", "conejo", "roedores", "aves")

PETS_CHARACTER = ("amigable", "dominante", "nervioso", "agresivo", "jugueton")

class Animals(db.Model):
    __tablename__="animals"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    name = db.Column(db.String(200), nullable=False)
    image = db.Column(db.Text())
    animal_type = db.Column(db.Enum(*ANIMALS_ENUM), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    personality = db.Column(db.Enum(*PETS_CHARACTER), nullable=False)
    gender = db.Column(db.Boolean(False), nullable=True)  #Preguntar si poner mejor enum(array)
    weight = db.Column(db.Float(), nullable=False)
    size = db.Column(db.Float(), nullable=False)
    diseases = db.Column(db.Text(), nullable=False)
    sterilized = db.Column(db.Boolean(False), nullable=False) 

    # def __repr__(self):
    #     return '<User %r>' % self.username

    def serialize(self):
        return {
            "id":self.id,
            "user_id": self.user_id,
            "name": self.name,
            "image": self.image,
            "animal_type":self.animal_type,
            "age":self.age,
            "personality":self.personality,
            "gender":self.gender,
            "weight":self.weight,
            "size":self.size,
            "diseases":self.diseases,
            "sterilized":self.sterilized
            # do not serialize the password, its a security breach
        }

    def create_user_pet(self):
        db.session.add(self)
        db.session.commit()

    @classmethod 
    def read_pets(cls, id_user):
        pets  = Animals.query.filter_by(user_id = id_user)
        all_pets = list(map(lambda x: x.serialize(), pets))
        return all_pets

    def update_pets(self, id_user, id, name, image, animal_type, age, personality, gender, weight, size, diseases, sterilized):
        # name, image, animal_type, age, personality, gender, weight, size, diseases, sterilized
        pet = Animals.query.filter_by(user_id = id_user, id = id).first()
        pet.name = name
        pet.image = image
        pet.animal_type = animal_type
        pet.age = age
        pet.personality = personality
        pet.gender = gender
        pet.weight = weight
        pet.size = size
        pet.diseases = diseases
        pet.sterilized = sterilized
        db.session.commit()
        

    def delete_pet(pet_id):
        pet = Animals.query.filter_by(id= pet_id)
        pet.delete()
        db.session.commit()

class Review(db.Model):
    __tablename__= "review"
    id = db.Column(db.Integer, primary_key=True)
    id_user_author =  db.Column(db.Integer, db.ForeignKey("user.id"))
    points = db.Column(db.Float())
    text = db.Column(db.Text(), nullable=False)
    
    # def create_user(self):
    #     db.session.add(self)
    #     db.session.commit()
    # def read_user():

    # def update_user():

    # def delete_user():

class Service_type(db.Model):
    __tablename__="service_type"
    id = Column(Integer, primary_key=True)
    service_type_id = Column(String(255))
    type_service = db.relationship('Services', lazy=True)

    def serialize(self):
        return {
            "id": self.id,
            "service_type_id": self.service_type_id,
        }

    def getServiceTypeValue(service_type_id):
        historic_service_type = Service_type.query.filter_by(id = service_type_id)
        all_historic_service_type =  list(map(lambda x: x.serialize(), historic_service_type))

        for eachServiceType in all_historic_service_type:
            result = eachServiceType["service_type_id"]

        return result


class Services(db.Model):
    __tablename__= "services"
    id = Column(Integer, primary_key=True)
    id_service_type = Column(Integer, ForeignKey("service_type.id"))
    id_user_offer = Column(Integer, ForeignKey("user.id"))
    description = Column(Text(), nullable=False)
    price_h = Column(Float(),nullable=False)
    # realtionships
    users_operations = db.relationship("Operations", back_populates="service_operations")

    def serialize(self):
        return {
            "id": self.id,
            "id_service_type": self.id_service_type,
            "id_user_offer": self.id_user_offer,
            "description": self.description,
            "price_h": self.price_h
        }

    # def create_user(self):
    #     db.session.add(self)
    #     db.session.commit()
    @classmethod
    def read_service_ofered(cls, id_user_param):
        history_services = cls.query.filter_by(id_user_offer= id_user_param)
        all_history_services = list(map(lambda x: x.serialize(), history_services))

        for eachservice in all_history_services:
            result = Operations.getOperations(eachservice["id"])
            for eachElement in result:
                service_type_value = Service_type.getServiceTypeValue(eachservice["id_service_type"])
                eachElement["service_type"] = service_type_value
                    

        return result

    # def update_user():

    # def delete_user():



