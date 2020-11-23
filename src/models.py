from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, String, Enum, Float, Date, Boolean, Text
from datetime import datetime

db = SQLAlchemy()


class Operations(db.Model):
    __tablename__= "operations"
    id = db.Column(db.Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"), primary_key=True)
    service_id = Column(Integer, ForeignKey("services.id"), primary_key=True)
    service = Column(String(255), nullable=False)
    date = Column(String(255), nullable=False)
    price = Column(Float(), nullable=False)
    # realtionships
    user_operation = db.relationship("User", back_populates="services_operations")
    service_operation = db.relationship("Services", back_populates="users_operations")


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
    commerce = db.relationship("Commerce", lazy=True)
    services_operations = db.relationship("Operations", back_populates="user_operation")

    # def __repr__(self):
    #     return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

    def create(self):
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

class Commerce(db.Model):
    __tablename__="commerce"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    description = db.Column(db.Text(), nullable=False)
    url = db.Column(db.String(255))
    image = db.Column(db.Text())
    schedule = db.Column(db.String(255), nullable=False)
    address = db.Column(db.Text(), nullable=False)
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
    # date = db.Column(db.DateTime, nullable=False)
    review_type = Column(Enum("comercio","usuario"), nullable=False)
    
    __mapper_args__ = {
        'polymorphic_identity': 'review',
        'polymorphic_on': review_type
    }
    # def create_user(self):
    #     db.session.add(self)
    #     db.session.commit()
    # def read_user():

    # def update_user():

    # def delete_user():

class User_review(Review):
    __tablename__= "user_review"
    id_review = db.Column(db.Integer, db.ForeignKey("review.id"), primary_key=True)
    id_user_destination = Column(Integer, ForeignKey('user.id'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity': 'user_review'
    }

class Commerce_review(Review):
    __tablename__= "Commerce_review"
    id_review = db.Column(db.Integer, ForeignKey("review.id"), primary_key=True)
    id_commerce_destination = Column(Integer, ForeignKey('commerce.id'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity': 'commerce_review'
    }

class Services(db.Model):
    __tablename__= "services"
    id = Column(Integer, primary_key=True)
    service = Column(Enum("Paseador", "Canguro", "Adiestrador", "Aseo"))
    description = Column(Text(), nullable=False)
    price = Column(Float(),nullable=False)
    image = Column(Text())
    # realtionships
    users_operations = db.relationship("Operations", back_populates="service_operation")

    def create_user(self):
        db.session.add(self)
        db.session.commit()
    # def read_user():

    # def update_user():

    # def delete_user():



