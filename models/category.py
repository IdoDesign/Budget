import json
import uuid
from common.database import Database

class Category:
    def __init__(self, name, _id=None):
        self._id = uuid.uuid4().hex if _id is None else _id
        self.name = name

    def json(self):
        dic = {
            '_id': str(self._id),
            'name': self.name
        }
        return dic

    @classmethod
    def all(cls):
        return [cls(**elem) for elem in Database.find("categories", {})]

    @classmethod
    def get_by_id(cls, id):
        return cls(**Database.find_one("categories", {"_id": id}))

    def save_to_mongo(self):
        Database.update("categories", {'_id': self._id}, self.json())
    
    def delete(self):
        Database.remove("categories", {'_id': self._id})
