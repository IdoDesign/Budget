
from .. models import User, Category, Transaction
import uuid
import csv
from .. import db
def create_user():
    user = User(
        _id='62215d2232864736b1a9aa0be99e21d8',
        name='Ido Tarazi',
        email='ido.tarazi@gmail.com',
        password_hash='$pbkdf2-sha512$25000$QSjl3BtDCIGwFkIIYcx5Lw$RiCrjDngZjZAC3e0o6kNa2/ynaTwmw8dM9ES6uNPBUmvvyy74k8rFxd5OU61u0rZWe8qVFqnNeqUivC6X3ABtQ')
    db.session.add(user)
    db.session.commit()


def populateCategories():
    with open ('categories.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            cat= Category(_id=row['_id'], name=row['name'])
            db.session.add(cat)
    db.session.commit()

def populateTransactions():
    #adds the transactions from the csv file
    with open ('transactions.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            db.session.add(Transaction(_id=row['_id'], date=row["date"], amount=(row["amount"])*(-1), description= row["description"], category=row["category"], user_id=row["user_id"]))
    db.session.commit()
