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
        




class User(db.Model):
    __tablename__= "user"
    id = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(80), nullable=False)
    is_active = Column(Boolean(False), nullable=False)
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

    # def read_user():

    # def update_user():

    # def delete_user():


class Animals(db.Model):
    __tablename__="animals"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    name = db.Column(db.String(200), nullable=False)
    image = db.Column(db.Text())
    animal_type = db.Column(db.Enum("perro", "gato", "conejo", "roedores", "aves"), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    personality = db.Column(db.Enum("amigable", "dominante", "nervioso", "agresivo", "jugueton"), nullable=False)
    gender = db.Column(db.Boolean(False), nullable=True)  #Preguntar si poner mejor enum(array)
    weight = db.Column(db.Float(), nullable=False)
    size = db.Column(db.Float(), nullable=False)
    diseases = db.Column(db.Text(), nullable=False)
    sterilized = db.Column(db.Boolean(False), nullable=False) 

    # def __repr__(self):
    #     return '<User %r>' % self.username

    def serialize(self):
        return {
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

    def create_pet(self):
        db.session.add(self)
        db.session.commit()

    @classmethod 
    def read_pets(cls, id_user):
        pets = Animals.query.filter_by(user_id = id_user)
        all_pets = list(map(lambda x: x.serialize(),pets))
        return all_pets

    # def update_user():

    # def delete_user():

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

    # def create_user(self):
    #     db.session.add(self)
    #     db.session.commit()

    def create_service(self):
        try:
            print(self,"DEVUELVE EL OBJETO USER")
            db.session.add(self)
            db.session.commit()
        except:
            db.session.rollback()

    @classmethod
    def read_all_services(cls, service_type):
        print("en models")
        services = cls.query.filter_by(id_service_type = service_type, is_active = True)
        print(services,"estoy en models all services")
        all_services =  list(map(lambda x: x.serialize(), services))
        print(all_services,"estoy en models all services 2")
        return all_services

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
        print(service, "estoy en models update")
        # service.id_service_type = id_service_type
        service.is_active = True
        service.description = description
        service.price_h = price_h
        db.session.commit()
    
    @classmethod    
    def delete_service(cls,id_user, id_service):
        print("en models")
        service = cls.query.filter_by(id_user_offer = id_user, id_service_type = id_service).first()
        # service.delete()
        
        service.is_active = False
        db.session.commit()
       
        print(service.is_active, "estoy en delete models")
        
        return service


