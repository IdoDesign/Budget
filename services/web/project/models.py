import uuid
from .common.utils import Utils
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_manager

db = SQLAlchemy()

#we'll add classes here
class User(UserMixin, db.Model):
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
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def get_id(self):
           return (self._id)


class Category(db.Model):
    __tablename__= 'categories'
    _id = db.Column(db.String(250), primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    transactions = db.relationship("Transaction")
    
    def __init__(self,  name, _id=None):
        self._id = uuid.uuid4().hex if _id is None else _id
        self.name = name

    def save(self):
        db.session.add(self)
        db.session.commit()
        
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

    @staticmethod
    def group_by_category(user_id):
        sum_by_category =  db.session.query(db.func.sum(Transaction.amount).label('sum'), Category.name).filter_by(user_id=user_id).group_by(Category._id).join(Category)

        amounts = []
        categories = []

        for category in sum_by_category:
            amounts.append(category.sum)
            categories.append(category.name)
        return {
            'labels': categories,
            'values': amounts
            }
    @staticmethod
    def group_by_month(user_id):
        month = db.func.date_trunc('month', Transaction.date)
        sum_by_Month = db.session.query(month.label('month'), db.func.sum(Transaction.amount).label('sum')).filter_by(user_id=user_id).group_by(month).order_by(month.desc())
        
        amounts = []
        months = []

        for month_sum in sum_by_Month:
            amounts.append(month_sum.sum)
            months.append(month_sum.month.strftime("%b"))
        
        return {
            'labels': months,
            'values': amounts
            }
