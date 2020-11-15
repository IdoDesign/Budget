import uuid
from common.database import Database
from common.utils import Utils
class User:
    def __init__(self,name, email, password_hash, _id=None):
        self._id = uuid.uuid4().hex if _id is None else _id
        self.name = name
        self.email = email
        self.password_hash = password_hash

    def json(self):
        return {
            '_id': self._id,
            'name': self.name,
            'email': self.email,
            'password_hash': self.password_hash
        }  
    
    @classmethod
    def all(cls):
        return [cls(**elem) for elem in Database.find("users", {})]

    @classmethod
    def get_by_id(cls, id):
        return cls(**Database.find_one("users", {"_id": id}))
   
    @classmethod
    def get_by_email(cls, email):
        return cls(**Database.find_one("users", {"email": email}))

    def save_to_mongo(self):
        Database.update("users", {'_id': self._id}, self.json())
    
    def delete(self):
        Database.remove("users", {'_id': self._id})

    @staticmethod
    def register(email,name, password):
        user_data = Database.find_one("users", {"email": email})
        if user_data:
            return False
        user = User(name, email, Utils.hash_password(password))
        user.save_to_mongo()
        return user._id
    
    @staticmethod
    def is_login_valid(email, password):
        user_data = Database.find_one("users", {"email": email})
        if user_data is None:
            return False
        if not Utils.check_hashed_password(password, user_data['password_hash']):
            return False
        return user_data

