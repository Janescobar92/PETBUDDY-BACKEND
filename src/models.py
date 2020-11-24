from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, String, Enum, Float, DateTime, Boolean, Text
from datetime import datetime

db = SQLAlchemy()


class Operations(db.Model):
    __tablename__= "operations"
    id = db.Column(Integer, primary_key=True)
    user_id_who_hire = Column(Integer, ForeignKey("user.id"), primary_key=True)
    service_id_hired = Column(Integer, ForeignKey("services.id"), primary_key=True)
    date = Column(DateTime(), nullable=False)
    hired_time = Column(Integer, nullable=False)
    total_price= Column(Float(), nullable= False)
    # realtionships
    user_operation = db.relationship("User", back_populates="services_operation")
    service_operations = db.relationship("Services", back_populates="users_operations")


class User(db.Model):
    __tablename__= "user"
    id = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(80), nullable=False)
    is_active = Column(Boolean(False), nullable=False)
    name = Column(String(200), nullable=False)
    last_name = Column(String(200), nullable=False)
    phone = Column(String(30), unique=True, nullable=False)
    location = Column(String(255), nullable=False)
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

    def create_user(self):
        db.session.add(self)
        db.session.commit()

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
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
    def create_user(self):
        db.session.add(self)
        db.session.commit()
    # def read_user():

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

class Services(db.Model):
    __tablename__= "services"
    id = Column(Integer, primary_key=True)
    id_service_type = Column(Integer, ForeignKey("service_type.id"))
    id_user_offer = Column(Integer, ForeignKey("user.id"))
    description = Column(Text(), nullable=False)
    price_h = Column(Float(),nullable=False)
    # realtionships
    users_operations = db.relationship("Operations", back_populates="service_operations")

    def create_user(self):
        db.session.add(self)
        db.session.commit()
    # def read_user():

    # def update_user():

    # def delete_user():

class Service_type(db.Model):
    __tablename__="service_type"
    id = Column(Integer, primary_key=True)
    service_type = Column(String(255))


