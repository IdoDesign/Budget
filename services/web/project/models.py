import uuid
from .common.utils import Utils
from flask_sqlalchemy import SQLAlchemy
from . import db


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
    
    @staticmethod
    def register(email, name, password):
        user = User.query.filter_by(email=email).first()
        if user:
            return False
        user.save()
        return user

    @staticmethod
    def is_login_valid(email, password):
        user = User.query.filter_by(email=email).first()
        if not user:
            return False
        if not Utils.check_hashed_password(password, user.password_hash):
            return False
        return user

class Category(db.Model):
    __tablename__= 'categories'
    _id = db.Column(db.String(250), primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    transactions = db.relationship("Transaction")
    
    def __init__(self,  name, _id=None):
        self._id = uuid.uuid4().hex if _id is None else _id
        self.name = name

    @staticmethod
    def all():
        return Category.query.all()
        
    @staticmethod
    def get_by_id(_id):
        return Category.query.filter_by(_id=_id).first()

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

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_by_user(user_id):
        return db.session.query(Transaction, Category).filter_by(user_id=user_id).join(Category)
        
    @staticmethod
    def get_by_id(_id):
        return Transaction.query.filter_by(_id=_id).first()
    
    @staticmethod
    def get_by_user_sorted(user_id):
        return db.session.query(Transaction, Category).filter_by(user_id=user_id).join(Category).order_by(Transaction.date.desc())


