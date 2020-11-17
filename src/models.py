from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, String, Enum, Float, Date
from datetime import datetime

db = SQLAlchemy()


association_table_services = db.Table('User_Services', db.Model.metadata,
    db.Column("user_id", db.Integer, db.ForeignKey("user.id")),
    db.Column("service_id", db.Integer, db.ForeignKey("services.id")),
    db.Column("service", db.String(255)),
    db.Column("date", db.String(255)),
    db.Column("price", db.Float())

)

association_table_review = db.Table('User_Review', db.Model.metadata,
    db.Column("user_id", db.Integer, db.ForeignKey("user.id")),
    db.Column("review_id", db.Integer, db.ForeignKey("review.id")),
    
)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    is_active = db.Column(db.Boolean(False), nullable=False)
    name = db.Column(db.String(200), nullable=False)
    last_name = db.Column(db.String(200), nullable=False)
    phone = db.Column(db.String(30), unique=True, nullable=False)
    location = db.Column(db.String(255), nullable=False)
    biografy = db.Column(db.Text())
    image = db.Column(db.String(255))
    animals = db.relationship('Animals', lazy=True)
    commerce = db.relationship("Commerce", lazy=True)
    patata = db.relationship("Services",
                secondary=association_table_services,
                back_populates="users") 
    review = db.relationship("Review",
                secondary=association_table_review,
                back_populates="users") 



    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Animals(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    name = db.Column(db.String(200), nullable=False)
    image = db.Column(db.String(255))
    animal_type = db.Column(db.Enum("perro", "gato", "conejo", "roedores", "aves"), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    personality = db.Column(db.Enum("amigable", "dominante", "nervioso", "agresivo", "jugueton"), nullable=False)
    sex = db.Column(db.Boolean(False), nullable=True)  #Preguntar si poner mejor enum(array)
    weight = db.Column(db.Float(), nullable=False)
    size = db.Column(db.Float(), nullable=False)
    diseases = db.Column(db.Text(), nullable=False)
    sterilized = db.Column(db.Boolean(False), nullable=False) 

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comerce_id = db.Column(db.Integer, db.ForeignKey("commerce.id"))
    review = db.Column(db.Float())
    comment = db.Column(db.Text(), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
   
    users= db.relationship("User",
                    secondary=association_table_review,
                    back_populates="review") 

class Services(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service = db.Column(db.Enum("Paseador", "Canguro", "Adiestrador", "Aseo"))
    description = db.Column(db.Text(), nullable=False)
    price = db.Column(db.Float(),nullable=False)
    image = db.Column(db.String(255))
    schedule = db.Column(db.String(255), nullable=False)
    users = db.relationship("User",
                 secondary=association_table_services,
               back_populates="patata") 

class Commerce(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
        service = db.Column(db.Enum("Paseador", "Canguro", "Adiestrador", "Aseo"))
        description = db.Column(db.Text(), nullable=False)
        url = db.Column(db.String(255))
        image = db.Column(db.String(255))
        schedule = db.Column(db.String(255), nullable=False)
        address = db.Column(db.String(255), nullable=False)
        review = db.relationship("Review", lazy=True)
        

