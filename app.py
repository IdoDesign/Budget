
import uuid
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from models import db, User, Category, Transaction
app = Flask (__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:1148@localhost:5432/budget"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 

db.init_app(app)
migrate = Migrate(app, db)



@app.route('/')
def hello():
    return "<h1>Hello World</h1>"


if __name__ == '__main__':
    app.run(debug=True)