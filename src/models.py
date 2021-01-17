from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, String, Enum, Float, DateTime, Boolean, Text, Date
from datetime import datetime

db = SQLAlchemy()


class Operations(db.Model):
    __tablename__= "operations"
    id = db.Column(Integer, primary_key=True)
    user_id_who_hire = Column(Integer, ForeignKey("user.id"), nullable=False, unique=False)
    service_id_hired = Column(Integer, ForeignKey("services.id"), nullable=False, unique=False)
    date =  Column(String(250), unique=False, nullable=False)
    hired_time = Column(Integer, nullable=False)
    total_price= Column(Float(), nullable= False)
    # realtionships
    user_operation = db.relationship("User", back_populates="services_operation")
    service_operations = db.relationship("Services", back_populates="users_operations")

    def create_operation(self):
        db.session.add(self)
        db.session.commit()

    def read_operations():
        operations = Operations.query.all()
        all_user_operations =  list(map(lambda x: x.serialize(), operations))

        return all_user_operations
        
    def serialize(self):
        return {
            "id": self.id,
            "user_id_who_hire": self.user_id_who_hire,
            "service_id_hired": self.service_id_hired,
            "date": self.date,
            "hired_time": self.hired_time,
            "total_price": self.total_price
        }
        
    @classmethod
    def read_service_hired(cls, id_user):
        history_services_hired = cls.query.filter_by(user_id_who_hire= id_user)
        all_history_services_hired =  list(map(lambda x: x.serialize(), history_services_hired))
        all_hired_data= []
        for eachOperation in all_history_services_hired:
            user_offer_values = Services.getIdUserOffer(eachOperation["service_id_hired"])
            hired_data = {**eachOperation, **user_offer_values}
            all_hired_data.append(hired_data)
            
        return all_hired_data
    
    def getOperations(param_id):
        historic_operations = Operations.query.filter_by(service_id_hired= param_id)
        all_historic_operations =  list(map(lambda x: x.serialize(), historic_operations))
        all_data_operations = []
        for eachOperation in all_historic_operations:
            user_who_hired_name = User.getUserWhoHired(eachOperation["user_id_who_hire"])
            full_data_operations = {**eachOperation,**user_who_hired_name}
            all_data_operations.append(full_data_operations)

        return all_data_operations       


class User(db.Model):
    __tablename__= "user"
    id = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(80), nullable=False)
    is_active = Column(Boolean(True), nullable=False)
    name = Column(String(200), nullable=False)
    last_name = Column(String(200), nullable=False)
    phone = Column(String(30), unique=False)
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

    def create_user(self):
        try:
            db.session.add(self)
            db.session.commit()
        except:
            db.session.rollback()

    def reactivate_user(self, name, last_name, password, is_active):
        self.name = name
        self.last_name = last_name
        self.password = password
        self.is_active = True
        db.session.commit()

    @classmethod 
    def read_user(cls, id_user):
        user =   User.query.get(id_user)
        return user

    def update_user(self, id_user, name, email, last_name, phone, location, biografy, image):
        user_to_update = User.query.filter_by(id= id_user).first()
        
        if image is not None:
            user_to_update.image = image
        else:
            user_to_update.image = user_to_update.image
            
        user_to_update.name = name
        user_to_update.email = email
        user_to_update.last_name = last_name
        user_to_update.phone = phone
        user_to_update.location = location
        user_to_update.biografy = biografy
        db.session.commit()

    def getUserWhoHired(param_id):
        historic_user_who_hires = User.query.filter_by(id= param_id)
        all_historic_user_who_hires =  list(map(lambda x: x.serialize(), historic_user_who_hires))
        result = {}

        for eachUserWhoHired in all_historic_user_who_hires:
            name = eachUserWhoHired["name"]
            image = eachUserWhoHired["image"]
            result = { "name": name, "image": image}

        return result


    def delete_user(id_user):
        user = User.query.get(id_user)
        if user.is_active == True:
            user.is_active= False
            db.session.commit()
        return user

    def get_address(id_user_offer):
        user = User.query.filter_by(id = id_user_offer).first()
        return user.location

    def get_origin(id_user):
        user_location = User.query.filter_by(id = id_user).first()
        result={"id":user_location.id, "address":user_location.location}
        return result

    def getUserNameAndImage(id_user_offer):
        user = User.query.filter_by(id = id_user_offer).first()
        result = {"image":user.image, "name": user.name}
        return result

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
    gender = db.Column(db.Boolean(False), nullable=True)  
    weight = db.Column(db.Float(), nullable=False)
    size = db.Column(db.Float(), nullable=False)
    diseases = db.Column(db.Text(), nullable=False)
    sterilized = db.Column(db.Boolean(False), nullable=False) 

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
        pets = Animals.query.filter_by(user_id = id_user)
        all_pets = list(map(lambda x: x.serialize(),pets))
        return all_pets

    def update_pets(self, id_user, id, name, image, animal_type, age, personality, gender, weight, size, diseases, sterilized):
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
        all_deleted_pets=  list(map(lambda x: x.serialize(), pet))
        pet.delete()
        db.session.commit()
        return all_deleted_pets

class Review(db.Model):
    __tablename__= "review"
    id = db.Column(db.Integer, primary_key=True)
    id_user_author =  db.Column(db.Integer, db.ForeignKey("user.id"))
    points = db.Column(db.Float())
    text = db.Column(db.Text(), nullable=False)
    
    # def create_review(self):
    #     db.session.add(self)
    #     db.session.commit()
    # def read_review():

    # def update_review():

    # def delete_review():

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
    is_active = db.Column(db.Boolean(True))
    id_user_offer = Column(Integer, ForeignKey("user.id"))
    description = Column(Text(), nullable=False)
    price_h = Column(Float(),nullable=False)
    # realtionships
    users_operations = db.relationship("Operations", back_populates="service_operations")

    def serialize(self):
        return {
            "id": self.id,
            "id_service_type": self.id_service_type,
            "is_active": self.is_active,
            "id_user_offer": self.id_user_offer,
            "description": self.description,
            "price_h": self.price_h
        }

    def create_service(self):
        db.session.add(self)
        db.session.commit()
        

    @classmethod
    def read_all_services(cls, service_type):
        services = cls.query.filter_by(id_service_type = service_type, is_active = True)
        all_services =  list(map(lambda x: x.serialize(), services))
        result = []
        for eachservice in all_services:
            user = User.getUserNameAndImage(eachservice["id_user_offer"])
            data = {**eachservice, **user}
            result.append(data)
            
        return result
    
    @classmethod
    def read_service_ofered(cls, id_user_param):
        history_services = cls.query.filter_by(id_user_offer= id_user_param)
        all_history_services = list(map(lambda x: x.serialize(), history_services))
        result= []
        
        for eachservice in all_history_services:
            all_operations =  Operations.getOperations(eachservice["id"])
            if len(Operations.getOperations(eachservice["id"])) != 0:                
                result.append(all_operations)
        
        return result

    @classmethod 
    def read_user_services(cls, id_user):
        services  = cls.query.filter_by(id_user_offer = id_user,is_active = True)
        all_services = list(map(lambda x: x.serialize(), services))
        return all_services

    @classmethod 
    def read_user_services_disabled(cls, id_user):
        services  = cls.query.filter_by(id_user_offer = id_user,is_active = False)
        all_services = list(map(lambda x: x.serialize(), services))
        return all_services

    @classmethod 
    def update_services(clss, id_service_type, id_user_offer, description, price_h):
        service = clss.query.filter_by(id_user_offer = id_user_offer, id_service_type = id_service_type).first()
        print(service, "ADIOOOOOOOS")
        service.is_active = True
        service.description = description
        service.price_h = price_h
        db.session.commit()
    
    @classmethod    
    def delete_service(cls,id_user, id_service):
        service = cls.query.filter_by(id_user_offer = id_user, id_service_type = id_service).first()
        # service_deleted = list(map(lambda x: x.serialize(), service))

        # service.delete()
        service.is_active = False
        db.session.commit() 
        return service


    def getIdUserOffer(id_param):
        historic_hired = Services.query.filter_by(id= id_param)
        all_historic_services_hired = list(map(lambda x: x.serialize(), historic_hired))
        
        result = {}
        for eachService in all_historic_services_hired:
            user_offer = User.getUserWhoHired(eachService["id_user_offer"])
            service_type = Service_type.getServiceTypeValue(eachService["id_service_type"])
            result = {**user_offer,  "service": service_type}
        return result

    def all_service_destinations(service_type_id):
        destinations = Services.query.filter_by(id_service_type = service_type_id)
        all_destinations_services =  list(map(lambda x: x.serialize(), destinations))

        service_types_locations=[]
        # id_destination = 0

        for eachService in all_destinations_services:
            address = User.get_origin(eachService["id_user_offer"])

            service_types_locations.append(address)

        return service_types_locations





       

