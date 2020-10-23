import uuid
import datetime
import json

from common.database import Database


class Transaction:
    def __init__(self, date, amount, description, category, _id=None):
        self._id = uuid.uuid4().hex if _id is None else _id
        self.date = date
        self.amount = amount
        self.description = description
        self.category = category

    def json(self):
        return {
            '_id': self._id,
            'date': self.date,
            'amount': self.amount,
            'description': self.description,
            'category': self.category
        }

    @classmethod
    def all(cls):
        return [cls(**elem) for elem in Database.find("transactions", {})]
    
    @classmethod
    def get_by_id(cls, id):
        return cls(**Database.find_one("transactions", {"_id": id}))

    def save_to_mongo(self):
        Database.update("transactions", {'_id': self._id}, self.json())
    
    def delete(self):
        Database.remove("transactions", {'_id': self._id})
    
    @classmethod
    def get_by_date(cls, date):
        return [cls(**elem) for elem in Database.find("transactions", {"date": date.isoformat()})] 
    
    @classmethod
    def get_by_category(cls, category_id):
        return [cls(**elem) for elem in Database.find("transactions", {"category": category_id})] 
    