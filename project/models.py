import uuid

from flask_sqlalchemy import SQLAlchemy
from project import db


#we'll add classes here
class User(db.Model):
    __tablename__= 'users'
    _id = db.Column(db.String(250), primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False)
    password_hash = db.Column(db.String(250), nullable=False)
    transactions = db.relationship("Transaction")

    def __init__(self,  name, email, password_hash, _id=None):
        self._id = uuid.uuid4().hex if _id is None else _id
        self.name = name
        self.email = email
        self.password_hash = password_hash

class Category(db.Model):
    __tablename__= 'categories'
    _id = db.Column(db.String(250), primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    transactions = db.relationship("Transaction")
    
    def __init__(self,  name, _id=None):
        self._id = uuid.uuid4().hex if _id is None else _id
        self.name = name
    
class Transaction(db.Model):
    __tablename__= 'transactions'
    _id = db.Column(db.String(250), primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(250), nullable=False)
    category = db.Column(db.String(250), db.ForeignKey('categories._id'))
    user_id = db.Column(db.String(250), db.ForeignKey('users._id'))
    
    def __init__(self, date, amount, description, category, user_id, _id=None):
        self._id = uuid.uuid4().hex if _id is None else _id
        self.date = date
        self.amount = amount
        self.description = description
        self.category = category
        self.user_id = user_id
