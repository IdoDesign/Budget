import flask
import datetime
import json
import sys
sys.path.append('/home/flask_app_project/Budget')

from common.database import Database
from models.category import Category
from models.transaction import Transaction

from transactions.routes import transactions
from main.routes import main
from users.routes import users



app = flask.Flask(__name__)

with open('etc/config.json') as config_file:
  config = json.load(config_file)
app.config['SECRET_KEY'] = config.get('SECRET_KEY')
app.config['MONGODB_DATABASE_URI'] = config.get("MONGODB_DATABASE_URI")

@app.before_first_request
def init_db():
    Database.initialize(app.config['MONGODB_DATABASE_URI'])

app.register_blueprint(transactions)
app.register_blueprint(main)
app.register_blueprint(users)

if __name__ == "__main__":
	app.run(debug=True)
