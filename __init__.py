from flask import Flask, render_template, request
import datetime
import json
import sys
sys.path.append('/home/flask_app_project/Budget')
from common.database import Database
from models.category import Category
from models.transaction import Transaction

app = Flask(__name__)

with open('/etc/config.json') as config_file:
  config = json.load(config_file)
app.config['SECRET_KEY'] = config.get('SECRET_KEY')
app.config['MONGODB_DATABASE_URI'] = config.get("MONGODB_DATABASE_URI")

@app.before_first_request
def init_db():
    Database.initialize(app.config['MONGODB_DATABASE_URI'])

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/add_transactions', methods=["GET", "POST"])
def add_transaction():
    categories = Category.all()
    if request.method == "POST":
        desc = request.form['description']
        amount = float(request.form["amount"])*-1
        cat = request.form["category"]
        date= datetime.datetime.fromisoformat(request.form["date"])
        Transaction(date, amount, desc, cat).save_to_mongo()
    return render_template('add_transactions.html', categories=categories)

@app.route('/all')
def all_transactions():
    transactions=Transaction.all()
    for item in transactions:
        item.category = Category.get_by_id(item.category).name
    return render_template('all_transactions.html', transactions=transactions)


if __name__ == "__main__":
	app.run(debug=True)
